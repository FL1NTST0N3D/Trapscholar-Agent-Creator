#!/usr/bin/env python3
"""Generate every derived file from each profile's AGENTS.md and catalog.json.

Usage (from anywhere):
  python3 scripts/build.py           rewrite any derived file that is out of date
  python3 scripts/build.py --check   list out-of-date files and exit 1; write nothing

Sources of truth: `scientific-agents/<slug>/AGENTS.md` and `catalog.json`.
Generated from them:
  scientific-agents/<slug>/CLAUDE.md                 byte-identical copy of AGENTS.md
  scientific-agents/<slug>/plugin.json               Agent Plugins manifest (agent-plugins.org)
  scientific-agents/<slug>/skills/<slug>/SKILL.md    Agent Skill: frontmatter + AGENTS.md
  scientific-agents/<slug>/agents/<slug>.md          Claude Code subagent: frontmatter + AGENTS.md
  scientific-agents/<slug>/.claude-plugin/plugin.json  Claude Code plugin manifest
  .claude-plugin/marketplace.json                    plugin list; top-level fields kept
  README.md                                          Agents tables, total, and badge
`catalog.json` itself is re-sorted by slug with its fields in a fixed order, and
each entry's `path` is filled in from its slug.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILES = ROOT / "scientific-agents"
CATALOG = ROOT / "catalog.json"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
README = ROOT / "README.md"

# README section order. Every catalog entry's `domain` must be one of these.
DOMAINS = [
    "Mathematics & Statistics",
    "Computer Science, Data & AI",
    "Physics",
    "Astronomy & Space Science",
    "Chemistry",
    "Materials, Nanoscience & Energy",
    "Earth, Environmental & Atmospheric Science",
    "Biology & Life Sciences",
    "Medicine & Clinical Science",
    "Agriculture, Food & Veterinary Science",
    "Engineering",
]

CATALOG_FIELDS = [
    "profession",
    "slug",
    "path",
    "domain",
    "work_mode",
    "summary",
    "version",
    "created",
    "updated",
    "source_count",
]

AUTHOR = {"name": "K-Dense-AI", "url": "https://github.com/K-Dense-AI"}
HOMEPAGE = "https://github.com/K-Dense-AI/scientific-agents"
LICENSE = "MIT"

# Agent Plugins 1.0.0 is the published spec; 1.1.0 is still a working draft.
AGENT_PLUGINS_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
AGENT_PLUGINS_AUTHOR = {"name": "K-Dense", "url": "https://www.k-dense.ai"}


class BuildError(Exception):
    pass


def to_json(data, trailing_newline=True):
    return json.dumps(data, indent=2, ensure_ascii=False) + ("\n" if trailing_newline else "")


def normalized_catalog(data):
    entries = []
    for i, entry in enumerate(data.get("agents", [])):
        slug = entry.get("slug")
        if not slug:
            raise BuildError(f"catalog.json[{i}] has no slug")
        entry = {**entry, "path": f"{slug}/AGENTS.md"}
        missing = [f for f in CATALOG_FIELDS if f not in entry]
        if missing:
            raise BuildError(f"catalog.json entry '{slug}' is missing {', '.join(missing)}")
        if entry["domain"] not in DOMAINS:
            raise BuildError(f"catalog.json entry '{slug}' has unknown domain '{entry['domain']}'")
        if "|" in entry["summary"]:
            raise BuildError(f"catalog.json entry '{slug}' summary contains '|', which breaks the README table")
        # Known fields first in a fixed order; keep any extra fields after them.
        ordered = {f: entry[f] for f in CATALOG_FIELDS}
        ordered.update({k: v for k, v in entry.items() if k not in ordered})
        entries.append(ordered)
    entries.sort(key=lambda e: e["slug"])
    return {**data, "agents": entries}


def plugin_manifest(entry):
    return {
        "name": entry["slug"],
        "version": entry["version"],
        "description": entry["summary"],
        "author": AUTHOR,
        "homepage": HOMEPAGE,
        "keywords": ["science", "agents-md", "expert-profile", entry["slug"]],
    }


def agent_plugin_manifest(entry):
    return {
        "$schema": AGENT_PLUGINS_SCHEMA,
        "name": entry["slug"],
        "version": entry["version"],
        "description": entry["summary"],
        "author": AGENT_PLUGINS_AUTHOR,
        "homepage": HOMEPAGE,
        "repository": HOMEPAGE,
        "license": LICENSE,
        "keywords": ["science", "agents-md", "expert-profile", entry["slug"]],
    }


def skill_description(entry):
    """Agent Skills descriptions say what the skill does and when to use it."""
    profession = entry["profession"]
    return f"Think and work like an expert {profession}. Use when a task calls for {profession} judgment. {entry['summary']}"


def skill_md(entry, body):
    front = "\n".join(
        [
            "---",
            f"name: {entry['slug']}",
            f"description: {json.dumps(skill_description(entry), ensure_ascii=False)}",
            f"license: {LICENSE}",
            "metadata:",
            f"  author: {AGENT_PLUGINS_AUTHOR['name']}",
            f"  version: {json.dumps(entry['version'])}",
            "---",
        ]
    )
    return f"{front}\n\n{body}"


def marketplace_entry(entry):
    return {
        "name": entry["slug"],
        "source": f"./scientific-agents/{entry['slug']}",
        "description": entry["summary"],
        "version": entry["version"],
        "category": "science",
        "keywords": ["science", "expert-profile", entry["slug"]],
        "metadata": {"profession": entry["profession"], "work_mode": entry["work_mode"]},
    }


def render_readme(text, entries):
    total = len(entries)
    text = re.sub(r"Expert_Profiles-\d+-", f"Expert_Profiles-{total}-", text)
    text = re.sub(r"All \d+ expert profiles", f"All {total} expert profiles", text)
    agents_heading = text.find("\n## Agents\n")
    start = text.find("<details>", agents_heading)
    if agents_heading < 0 or start < 0:
        raise BuildError("README.md has no '## Agents' section followed by <details> tables")
    blocks = []
    for domain in DOMAINS:
        rows = sorted((e for e in entries if e["domain"] == domain), key=lambda e: e["profession"].lower())
        if not rows:
            continue
        noun = "profile" if len(rows) == 1 else "profiles"
        lines = [
            "<details>",
            f"<summary><b>{domain}</b> — {len(rows)} {noun}</summary>",
            "",
            "| Agent | How it reasons |",
            "| --- | --- |",
        ]
        lines += [f"| [{e['profession']}](scientific-agents/{e['slug']}/AGENTS.md) | {e['summary']} |" for e in rows]
        lines += ["", "</details>"]
        blocks.append("\n".join(lines))
    return text[:start] + "\n\n".join(blocks) + "\n"


def render():
    """Return {path: expected content} for every file this script owns."""
    catalog = normalized_catalog(json.loads(CATALOG.read_text()))
    entries = catalog["agents"]
    outputs = {CATALOG: to_json(catalog, trailing_newline=False)}

    for entry in entries:
        slug = entry["slug"]
        folder = PROFILES / slug
        agents_md = folder / "AGENTS.md"
        if not agents_md.is_file():
            raise BuildError(f"catalog.json lists '{slug}' but scientific-agents/{slug}/AGENTS.md does not exist")
        body = agents_md.read_text()
        front = f"---\nname: {slug}\ndescription: {json.dumps(entry['summary'], ensure_ascii=False)}\n---\n\n"
        outputs[folder / "CLAUDE.md"] = body
        outputs[folder / "plugin.json"] = to_json(agent_plugin_manifest(entry))
        outputs[folder / "skills" / slug / "SKILL.md"] = skill_md(entry, body)
        outputs[folder / "agents" / f"{slug}.md"] = front + body
        outputs[folder / ".claude-plugin" / "plugin.json"] = to_json(plugin_manifest(entry))

    market = json.loads(MARKETPLACE.read_text())
    market["plugins"] = [marketplace_entry(e) for e in entries]
    outputs[MARKETPLACE] = to_json(market)
    outputs[README] = render_readme(README.read_text(), entries)
    return outputs


def stale_files(outputs):
    return [p for p, content in outputs.items() if not p.is_file() or p.read_text() != content]


def main(argv):
    check = "--check" in argv
    try:
        outputs = render()
    except (BuildError, json.JSONDecodeError) as exc:
        print(f"error: {exc}")
        return 1
    stale = stale_files(outputs)
    for path in stale:
        rel = path.relative_to(ROOT)
        if check:
            print(f"out of date: {rel}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(outputs[path])
            print(f"wrote {rel}")
    if check and stale:
        print(f"\n{len(stale)} generated files are out of date; run: python3 scripts/build.py")
        return 1
    if not stale:
        print("all generated files are up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
