#!/usr/bin/env python3
"""Check expert profiles, catalog.json, and every file generated from them.

Usage (from anywhere):  python3 scripts/validate.py

Checks catalog.json fields, each `scientific-agents/<slug>/AGENTS.md` (title,
standard headings, size, near-duplicate content), that every file
scripts/build.py generates is up to date, that each profile folder is a
conforming Agent Plugin (agent-plugins.org manifest + Agent Skills SKILL.md), and
that the two local copies of the create-scientific-agent skill match. Exits 1 if any error is found; warnings
are printed but do not fail the run. Standard library only, so it runs in CI.
"""

import itertools
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import build

ROOT = build.ROOT
PROFILES = build.PROFILES

# Codex truncates project docs past `project_doc_max_bytes` (default 32 KiB).
MAX_BYTES = 32 * 1024

# Share of a profile's content lines found verbatim in another profile. Distinct
# profiles overlap by under 10%; copied bodies sit at 50-99%.
MAX_OVERLAP = 0.25

# Standard section headings from the skill's agents-md-template.md.
CANONICAL_HEADINGS = [
    "Mindset And First Principles",
    "How You Frame A Problem",
    "How You Work",
    "Tools, Instruments, And Software",
    "Data, Resources, And Literature",
    "Rigor And Critical Thinking",
    "Troubleshooting Playbook",
    "Communicating Results",
    "Standards, Units, Ethics, And Vocabulary",
    "Definition Of Done",
]

CATALOG_TYPES = {
    "profession": str,
    "slug": str,
    "path": str,
    "domain": str,
    "work_mode": str,
    "summary": str,
    "version": str,
    "created": str,
    "updated": str,
    "source_count": int,
}

# Agent Plugins 1.0.0 manifest: a closed schema (agent-plugins.org/specification §5).
PLUGIN_FIELDS = {
    "$schema": str,
    "name": str,
    "version": str,
    "description": str,
    "author": dict,
    "homepage": str,
    "repository": str,
    "license": str,
    "keywords": list,
    "extensions": dict,
}
PLUGIN_NAME = re.compile(r"(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?")

# Agent Skills SKILL.md frontmatter (agentskills.io/specification).
SKILL_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
MAX_SKILL_DESCRIPTION = 1024

SKILL_COPIES = [
    ROOT / ".agents/skills/create-scientific-agent",
    ROOT / ".claude/skills/create-scientific-agent",
]

errors = []
warnings = []


def error(where, msg):
    errors.append(f"{where}: {msg}")


def warn(where, msg):
    warnings.append(f"{where}: {msg}")


def heading_key(text):
    """Collapse punctuation, case, and '&' vs 'And' so spelling variants match."""
    words = re.sub(r"[^a-z ]", "", text.lower().replace("&", "and")).split()
    return " ".join(w for w in words if w != "and")


CANONICAL_BY_KEY = {heading_key(h): h for h in CANONICAL_HEADINGS}


def check_catalog():
    try:
        data = json.loads(build.CATALOG.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        error("catalog.json", f"cannot load JSON ({exc})")
        return {}
    catalog = {}
    for i, entry in enumerate(data.get("agents", [])):
        slug = entry.get("slug", "")
        where = f"catalog.json:{slug or i}"
        for field, kind in CATALOG_TYPES.items():
            if not isinstance(entry.get(field), kind):
                error(where, f"missing or non-{kind.__name__} field '{field}'")
        if slug in catalog:
            error(where, "duplicate slug")
        catalog[slug] = entry
        if entry.get("domain") not in build.DOMAINS:
            error(where, f"domain '{entry.get('domain')}' is not one of: {'; '.join(build.DOMAINS)}")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(entry.get("version", ""))):
            error(where, "version is not semver (e.g. 1.0.0)")
        for field in ("created", "updated"):
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(entry.get(field, ""))):
                error(where, f"'{field}' is not YYYY-MM-DD")
        if str(entry.get("updated", "")) < str(entry.get("created", "")):
            error(where, "'updated' is earlier than 'created'")
        if "|" in str(entry.get("summary", "")):
            error(where, "summary contains '|', which breaks the README table")
        if entry.get("source_count") == 0:
            warn(where, "source_count is 0 (no recorded research)")
    return catalog


def check_profile(slug, entry, body):
    where = f"scientific-agents/{slug}/AGENTS.md"
    size = len(body.encode())
    if size > MAX_BYTES:
        error(where, f"{size} bytes exceeds the {MAX_BYTES}-byte Codex default")

    title = body.split("\n", 1)[0]
    expected_title = f"# AGENTS.md — {entry.get('profession', '')} Agent"
    if title != expected_title:
        error(where, f"title should be '{expected_title}', found '{title}'")

    for heading in re.findall(r"^## (.+?)[ \t]*$", body, re.M):
        canonical = CANONICAL_BY_KEY.get(heading_key(heading))
        if canonical and canonical != heading:
            error(where, f"heading '## {heading}' should be '## {canonical}'")


def check_agent_plugin(slug):
    """The profile folder must load in any Agent Plugins 1.0.0 client."""
    where = f"scientific-agents/{slug}/plugin.json"
    try:
        manifest = json.loads((PROFILES / slug / "plugin.json").read_text())
    except (OSError, json.JSONDecodeError) as exc:
        error(where, f"cannot load JSON ({exc})")
        return
    if not isinstance(manifest, dict):
        error(where, "manifest is not a JSON object")
        return
    for field in sorted(set(manifest) - set(PLUGIN_FIELDS)):
        error(where, f"'{field}' is not an Agent Plugins manifest field")
    for field, kind in PLUGIN_FIELDS.items():
        if field in manifest and not isinstance(manifest[field], kind):
            error(where, f"'{field}' must be a {kind.__name__}")
    if manifest.get("$schema") != build.AGENT_PLUGINS_SCHEMA:
        error(where, f"'$schema' must be {build.AGENT_PLUGINS_SCHEMA}")
    name = manifest.get("name", "")
    if not (isinstance(name, str) and 1 <= len(name) <= 64 and PLUGIN_NAME.fullmatch(name)):
        error(where, f"name '{name}' breaks the Agent Plugins naming rules")
    author = manifest.get("author", {})
    if isinstance(author, dict) and (set(author) - {"name", "email", "url"} or not all(isinstance(v, str) for v in author.values())):
        error(where, "author may hold only string 'name', 'email', and 'url' fields")
    if isinstance(manifest.get("keywords"), list) and not all(isinstance(k, str) for k in manifest["keywords"]):
        error(where, "keywords must all be strings")
    if isinstance(manifest.get("extensions"), dict) and not all(isinstance(v, dict) for v in manifest["extensions"].values()):
        error(where, "each extensions value must be an object")


def skill_frontmatter(text):
    """Top-level `key: value` pairs from a SKILL.md frontmatter block, or None."""
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        if line[:1] in (" ", "\t") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        fields[key] = json.loads(value) if value.startswith('"') else value
    return fields


def check_skill(slug):
    """skills/<slug>/SKILL.md must satisfy the Agent Skills specification."""
    where = f"scientific-agents/{slug}/skills/{slug}/SKILL.md"
    path = PROFILES / slug / "skills" / slug / "SKILL.md"
    if not path.is_file():
        error(where, "missing; run python3 scripts/build.py")
        return
    fields = skill_frontmatter(path.read_text())
    if fields is None:
        error(where, "no YAML frontmatter block")
        return
    for field in sorted(set(fields) - SKILL_FIELDS):
        error(where, f"'{field}' is not an Agent Skills frontmatter field")
    name = fields.get("name", "")
    if not (1 <= len(name) <= 64 and SKILL_NAME.fullmatch(name)):
        error(where, f"name '{name}' breaks the Agent Skills naming rules")
    if name != slug:
        error(where, f"name '{name}' must match its directory '{slug}'")
    description = fields.get("description", "")
    if not 1 <= len(description) <= MAX_SKILL_DESCRIPTION:
        error(where, f"description is {len(description)} characters; Agent Skills allows 1-{MAX_SKILL_DESCRIPTION}")


def check_generated():
    """Every file build.py owns must match what it would write now."""
    try:
        outputs = build.render()
    except (build.BuildError, json.JSONDecodeError) as exc:
        error("build", str(exc))
        return
    for path in build.stale_files(outputs):
        error(str(path.relative_to(ROOT)), "out of date; run python3 scripts/build.py")


def check_overlap(bodies):
    """Flag pairs of profiles that share a large block of verbatim lines."""
    lines = {}
    for slug, body in bodies.items():
        lines[slug] = {
            line.strip().lower()
            for line in body.splitlines()
            if len(line.strip()) >= 40 and not line.lstrip().startswith("#")
        }
    owners = defaultdict(list)
    for slug, content in lines.items():
        for line in content:
            owners[line].append(slug)
    shared = defaultdict(int)
    for slugs in owners.values():
        # Skip lines nearly every profile has; they are boilerplate, not copying.
        if 1 < len(slugs) < 50:
            for pair in itertools.combinations(sorted(slugs), 2):
                shared[pair] += 1
    for (a, b), count in sorted(shared.items()):
        smaller = min(len(lines[a]), len(lines[b])) or 1
        if count / smaller > MAX_OVERLAP:
            error("scientific-agents", f"'{a}' and '{b}' share {count / smaller:.0%} of their lines verbatim")


def check_skill_copies():
    # The skill folders are gitignored, so a fresh clone has neither; skip then.
    present = [copy for copy in SKILL_COPIES if copy.is_dir()]
    if not present:
        return
    if len(present) == 1:
        missing = next(c for c in SKILL_COPIES if c not in present)
        warn(str(missing.relative_to(ROOT)), "skill copy missing; only one copy exists")
        return
    first, second = (
        {p.relative_to(copy): p.read_bytes() for p in copy.rglob("*") if p.is_file()} for copy in SKILL_COPIES
    )
    for rel in sorted(set(first) | set(second)):
        if first.get(rel) != second.get(rel):
            error("skills", f"{rel} differs between .agents/skills and .claude/skills")


def main():
    catalog = check_catalog()
    folders = {p.name for p in PROFILES.iterdir() if p.is_dir()}
    for slug in sorted(folders - set(catalog)):
        error(f"scientific-agents/{slug}", "folder has no catalog.json entry")
    for slug in sorted(set(catalog) - folders):
        error("catalog.json", f"entry '{slug}' has no scientific-agents/{slug}/ folder")

    bodies = {}
    for slug in sorted(folders & set(catalog)):
        agents_md = PROFILES / slug / "AGENTS.md"
        if not agents_md.is_file():
            error(f"scientific-agents/{slug}", "missing AGENTS.md")
            continue
        bodies[slug] = agents_md.read_text()
        check_profile(slug, catalog[slug], bodies[slug])
        check_agent_plugin(slug)
        check_skill(slug)

    if any(msg.startswith("catalog.json") for msg in errors):
        warn("build", "generated-file check skipped until catalog.json errors are fixed")
    else:
        check_generated()
    check_overlap(bodies)
    check_skill_copies()

    for msg in warnings:
        print(f"warning: {msg}")
    for msg in errors:
        print(f"error: {msg}")
    print(f"\n{len(catalog)} profiles checked: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
