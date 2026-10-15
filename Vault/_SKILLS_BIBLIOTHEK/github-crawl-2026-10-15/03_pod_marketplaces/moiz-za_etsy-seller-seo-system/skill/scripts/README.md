# Scripts

Two standalone utilities for the etsy-seller skill. Neither is required for
normal skill use — the AI invokes `bootstrap.py` automatically, and
`sync_etsy_policy.py` is a maintainer tool.

## `bootstrap.py`

**Purpose:** create `~/etsy-listings/` with empty markdown templates on the first skill invocation. Idempotent — does nothing on subsequent runs.

**Called from:** SKILL.md Phase 0 (auto-bootstrap), every run.

**Dependencies:** Python 3.8+. Pure stdlib — no third-party packages.

**Manual usage (not normally needed):**

```bash
# Default — creates ~/etsy-listings/ if missing
python3 bootstrap.py

# Custom state location
python3 bootstrap.py --state-dir /custom/path

# Quiet mode (no stdout)
python3 bootstrap.py --quiet
```

### Why this is a CLI, not Python imports

The skill runs INSIDE an AI tool (Claude/Cowork). The AI executes shell commands
to invoke this script. Keeping it as a standalone CLI makes it:

- Testable on its own
- Portable across AI tools that support bash
- Independent of the AI tool's Python runtime

Once state is bootstrapped, the AI uses its native Edit/Write tools to update
markdown state files directly — no Python scripting needed for ongoing operations.

## `sync_etsy_policy.py`

**Purpose:** maintainer utility that (a) keeps the shared rulebooks in sync
between this repo and the companion `svg-design-intelligence-system` repo, and
(b) rebuilds the packaged `etsy-seller.skill` archive.

**Not used by the skill at runtime.**

```bash
# Bidirectional cross-repo sync (requires the sibling repo to be present)
python3 sync_etsy_policy.py

# Rebuild only etsy-seller.skill from skill/ + state-templates/ (no sibling repo needed)
python3 sync_etsy_policy.py --build
```

**Synced files:** `listing-guide.md`, `seo-guide.md`, `policies.md`, and the
playbooks listed in `PLAYBOOKS`.

**Intentionally not synced:** `system-laws.md`, `operations.md`,
`pinterest-guide.md`, and `data-model/SCHEMA.md` — these are owned by this repo
and edited independently in the companion.

**Archive build:** `--build` produces a deterministic `etsy-seller.skill` (fixed
timestamps, sorted entries). CI runs it and fails if the committed archive
differs from the source tree, so the downloadable skill can never drift.

## What state files this creates

Reads from `state-templates/etsy-listings/` — a sibling of `skill/` in a clone
layout, or bundled inside the installed skill in the `.skill` zip layout:

```
~/etsy-listings/
├── keyword-map.md
├── refresh-schedule.md
├── listings/
│   └── _TEMPLATE_listing.md     (the AI references this when creating new L###-*.md files)
└── sqr-imports/
    └── README.md                (instructions for SQR paste workflow)
```
