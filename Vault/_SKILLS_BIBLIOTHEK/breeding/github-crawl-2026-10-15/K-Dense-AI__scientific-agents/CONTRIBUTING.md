# Contributing to Scientific Agents

Thanks for helping grow this collection. This repo holds **expert-thinking
profiles**: one `AGENTS.md` per scientific or engineering profession, each
teaching an AI agent to reason like a senior practitioner in that field.

There are two ways to contribute:

1. **Request or report** — open an issue to request a new profession or flag a
   problem with an existing profile. No writing required.
2. **Author** — open a pull request that adds a new profile or improves an
   existing one.

Both are welcome. If you only have 30 seconds, an issue is genuinely useful.

---

## The one thing that matters: specificity

Every profile lives or dies by one test, the **generic-swap test**:

> Read any sentence in the profile. Mentally swap in a *different* profession's
> name. If the sentence still reads as true, it is filler — cut it or replace it
> with a real specific.

- ❌ *"Always use rigorous statistical methods and think critically."* — true for
  everyone → **cut.**
- ✅ *"Correct GWAS p-values for genome-wide significance at 5×10⁻⁸."* — true only
  for this field → **keep.**

A strong profile names the field's actual databases, instruments, units,
controls, thresholds, standards, journals, and **named failure modes** — the
things a practitioner would recognize as true and useful and an outsider could
not have written. A weak profile is a "be rigorous, be careful" essay wearing a
profession's name tag. We only merge the former.

The house style for the one-line summary (used in `catalog.json`, the README
table, and the plugin description) is a single dense sentence:

> *Reasons from `<first-principles foundations>` through `<specific named tools,
> methods, standards>` while treating `<3–5 specific, field-distinctive failure
> modes>` as first-class failure modes.*

Look at existing entries in [`catalog.json`](catalog.json) before writing yours.

---

## Reporting a problem or requesting a profession

Open an issue using one of the templates:

- **New expert profile** — name the profession, sub-specialty, and (if you know
  the field) a few concrete tools/databases/failure modes that a good profile
  must include. That head start meaningfully improves the result.
- **Profile correction** — point to the file and line, describe what's wrong
  (a wrong tool name, an out-of-date threshold, a missing failure mode), and
  cite a source if you have one. **Wrong specifics are worse than honest gaps**,
  so these reports are high-value.

---

## Authoring a profile (pull request)

### Recommended path: the skill

Profiles are normally generated with the **`create-scientific-agent`** skill,
which runs the required multi-source research, applies the quality bar, fills the
template, and updates every registry. If you have access to it (it ships with
K-Dense's Claude Code tooling), use it — it handles the mechanics below for you.
The rest of this section is what the skill does, written out so a profile can be
authored or reviewed by hand.

### What a profile must contain

Write `AGENTS.md` in the **second person** ("You are…", "When you…"), dense and
scannable — headers and bullets, no filler. Ground it in real research (name your
sources); internal knowledge alone produces plausible-but-generic profiles, and
the gap shows. Cover, in the field's own terms:

- **Mindset / first principles** the agent reasons *from*, not just recalls.
- **Problem-framing**, including the field's named red herrings.
- **Workflow** — how the field actually sequences work.
- **Tools / instruments / software** — named, with when-to-use and gotchas.
- **Data / databases / literature** — named and findable.
- **Controls** — the field's actual positive and negative controls.
- **Statistics & uncertainty** — dominant methods, error model, units, reporting.
- **Confounders / threats to validity** specific to the field.
- **Troubleshooting** — named artifacts and failure modes, and how to detect each.
- **Communication** — reporting structure, figure norms, hedging register,
  standards by name.
- **Units, ethics, vocabulary** the agent must get right.

Existing profiles run ~10–31 KB, and the hard cap is **32 KiB** (Codex's default
`project_doc_max_bytes`; anything longer is silently truncated). Length must be
**earned by specificity**, never padded.

### File layout

Each profession is a directory under `scientific-agents/<slug>/`, where `<slug>`
is the profession as a **kebab-case** slug (e.g. `tissue-engineer`,
`clinical-epidemiologist`). You write **one** file there; the build script
generates the rest, which make the folder both an
[Agent Plugin](https://agent-plugins.org/) and a Claude Code plugin:

```
scientific-agents/<slug>/
├── AGENTS.md                     # the profile — you write this
├── CLAUDE.md                     # generated: byte-identical copy of AGENTS.md
├── plugin.json                   # generated: Agent Plugins 1.0.0 manifest
├── skills/<slug>/SKILL.md        # generated: Agent Skill (frontmatter + body)
├── .claude-plugin/plugin.json    # generated: Claude Code plugin manifest
└── agents/<slug>.md              # generated: Claude Code subagent (frontmatter + body)
```

Start `AGENTS.md` with `# AGENTS.md — <Profession> Agent` and use the standard
section headings (`## Mindset And First Principles`, `## How You Frame A Problem`,
`## How You Work`, `## Tools, Instruments, And Software`,
`## Data, Resources, And Literature`, `## Rigor And Critical Thinking`,
`## Troubleshooting Playbook`, `## Communicating Results`,
`## Standards, Units, Ethics, And Vocabulary`, `## Definition Of Done`). Add
field-specific sections as needed.

### Register the profile in `catalog.json`

[`catalog.json`](catalog.json) is the only registry you edit by hand. Add an
entry under `agents` (or update the existing one in place when regenerating):

```json
{
  "profession": "Tissue Engineer",
  "slug": "tissue-engineer",
  "domain": "Biology & Life Sciences",
  "work_mode": "wet-lab / regenerative medicine",
  "summary": "Reasons from … while treating … as first-class failure modes.",
  "version": "1.0.0",
  "created": "YYYY-MM-DD",
  "updated": "YYYY-MM-DD",
  "source_count": 0
}
```

- `profession` must match the `AGENTS.md` title.
- `domain` picks the README section: Mathematics & Statistics · Computer
  Science, Data & AI · Physics · Astronomy & Space Science · Chemistry ·
  Materials, Nanoscience & Energy · Earth, Environmental & Atmospheric Science ·
  Biology & Life Sciences · Medicine & Clinical Science · Agriculture, Food &
  Veterinary Science · Engineering.
- `summary` is the house-style sentence. It is reused as the README row, the
  plugin descriptions, the subagent description, and (after a one-line lead-in)
  the skill description, so it must not contain `|`.
- `version` starts at `1.0.0`. When you change an existing profile, bump the
  minor version (`1.0.0` → `1.1.0`) and refresh `updated` and `source_count`, so
  that installed plugin copies update.
- Entry order and `path` don't matter; the build sorts entries and fills `path`.

### Build and validate

From the repo root:

```
python3 scripts/build.py      # regenerate everything derived from AGENTS.md + catalog.json
python3 scripts/validate.py   # check the result
```

`build.py` writes the generated files in each profile folder,
[`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json), and the
[`README.md`](README.md) Agents tables, section counts, total, and badge. Never
edit those by hand; your changes will be overwritten or fail CI. Rerun the build
instead.

`validate.py` checks catalog fields, the title line, the standard headings, the
32 KiB cap, that every generated file is current, and that each profile folder
conforms to the Agent Plugins manifest schema and the Agent Skills `SKILL.md`
rules. It also flags any profile
that shares more than 25% of its lines verbatim with another. CI runs it on every
pull request. Fix every `error:` line; `warning:` lines are advisory. Both
scripts use only the Python standard library.

### Clean up

Delete any temporary files created during research or drafting (including any
`.json` scratch files from search/research tooling) before committing.

---

## Pull request checklist

Copy this into your PR description and tick each box:

- [ ] `AGENTS.md` passes the generic-swap test top to bottom — no filler lines.
- [ ] Specifics are **real** (named tools, databases, thresholds, standards). No
      invented specifics; honest gaps over wrong facts.
- [ ] Second person, scannable, no padding.
- [ ] `catalog.json` entry added or updated (`domain`, `summary`, `version`
      bumped if changing an existing profile).
- [ ] Ran `python3 scripts/build.py` and committed the generated files.
- [ ] `python3 scripts/validate.py` reports 0 errors.
- [ ] Temporary/scratch files removed.

Thanks again — every well-researched profile makes the whole collection more
useful.
