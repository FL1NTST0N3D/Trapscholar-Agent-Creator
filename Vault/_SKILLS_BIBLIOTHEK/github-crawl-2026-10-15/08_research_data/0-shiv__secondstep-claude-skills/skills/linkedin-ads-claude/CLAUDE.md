# LinkedIn Ads Claude

LinkedIn B2B Ads audit and optimization skill for Claude Code.

## Architecture

- `SKILL.md` — Main skill definition, routes all `/li` commands
- `skills/li-*/SKILL.md` — 8 specialized sub-skills (targeting, lead-gen, budget, etc.)
- `agents/*.md` — 3 agents: auditor, strategist, reporter
- `scripts/*.py` — Python utilities for health scoring and benchmarking
- `docs/*.md` — Reference docs: glossary, funnel framework, benchmarks, ABM playbook

## Commands

| Command | Sub-Skill |
|---------|-----------|
| `/li audit` | Full 25-point LinkedIn Ads health audit |
| `/li targeting` | Targeting layer analysis & ABM review |
| `/li lead-gen` | Lead Gen Form optimization audit |
| `/li formats` | Content format mix & performance review |
| `/li budget` | Budget allocation & CPL benchmark analysis |
| `/li audiences` | Matched Audiences & retargeting audit |
| `/li tracking` | Conversion tracking & attribution review |
| `/li report` | Generate full audit report with scores |

## Development Rules

- Keep SKILL.md files under 500 lines
- Use kebab-case for directory names
- Agents run via Task tool with `context: fork`
- All output files go to current working directory
- Always reference LinkedIn-specific benchmarks (CTR, CPC, CPL)
- Health score system is 0-100 across 8 weighted dimensions
