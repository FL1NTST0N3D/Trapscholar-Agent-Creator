# YouTube Ads Claude

YouTube campaign audit and optimization skill for Claude Code.

## Architecture

- `SKILL.md` — Main orchestrator, routes all `/yt` commands
- `skills/yt-*/SKILL.md` — 9 specialized sub-skills
- `agents/*.md` — 4 autonomous audit agents
- `scripts/*.py` — Python utilities for data analysis
- `docs/` — Reference documentation and glossary

## Commands

| Command | Sub-Skill |
|---------|-----------|
| `/yt audit` | Full campaign audit across all dimensions |
| `/yt creative` | Video ad creative scoring (ABCD framework) |
| `/yt targeting` | Targeting strategy analysis |
| `/yt shorts` | Shorts ad readiness assessment |
| `/yt bumper` | 6-second bumper ad strategy |
| `/yt bidding` | Bidding strategy analysis by objective |
| `/yt placements` | Placement hygiene and brand safety |
| `/yt remarketing` | Remarketing funnel analysis |
| `/yt report` | Generate full audit report with scores |

## Development Rules

- Keep SKILL.md files under 500 lines
- Use kebab-case for directory names
- Agents run via Task tool with `context: fork`
- All output files go to current working directory
- YouTube Ads Score uses 8 weighted dimensions (see SKILL.md)
- Include real YouTube/Google Ads benchmarks in all analysis
- Reference Google ABCD framework for creative scoring
