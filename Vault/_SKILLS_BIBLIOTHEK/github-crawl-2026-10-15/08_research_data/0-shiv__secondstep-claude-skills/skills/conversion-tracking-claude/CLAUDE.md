# Conversion Tracking Claude

Cross-platform conversion tracking audit and validation skill for Claude Code.

## Architecture

- `SKILL.md` — Main orchestrator, routes all `/track` commands, scoring rubric
- `skills/track-*/SKILL.md` — 10 specialized sub-skills (Google Tag, EC, sGTM, Offline, Meta Pixel, CAPI, LinkedIn, TikTok, Attribution, Report)
- `agents/*.md` — 4 parallel subagents (audit orchestrator, tag inspector, data quality, report generator)
- `scripts/*.py` — Python validation scripts (tag validator, EC checker, pixel auditor, report generator)
- `templates/*.md` — Audit report and checklist templates
- `tracking/tracking_config.yaml` — Platform configuration

## Commands

| Command | Sub-Skill |
|---------|-----------|
| `/track audit` | Full cross-platform audit with Health Score |
| `/track google-tag` | Google Tag (gtag.js) validation |
| `/track ec` | Enhanced Conversions audit (Web + Leads) |
| `/track server-side` | Server-side GTM validation |
| `/track offline` | Offline conversion import check |
| `/track meta-pixel` | Meta Pixel audit |
| `/track capi` | Meta Conversions API validation |
| `/track linkedin` | LinkedIn Insight Tag check |
| `/track tiktok` | TikTok Pixel audit |
| `/track attribution` | Attribution model analysis |
| `/track report` | Generate full audit report |

## Development Rules

- Keep SKILL.md files under 500 lines
- Use kebab-case for directory names
- Agents run via Task tool with `context: fork`
- All output files go to current working directory
- Tracking Health Score uses the 100-point rubric defined in SKILL.md
- Python scripts require Python 3.8+
