# Competitor Analysis Claude

Competitive intelligence skill for Claude Code. Systematic competitor analysis across 9 dimensions.

## Architecture

- `competitor/CLAUDE.md` — Main orchestrator, routes all `/comp` commands
- `skills/comp-*/CLAUDE.md` — 9 specialized sub-skills
- `agents/*.md` — 3 CI agents (Researcher, Analyst, Strategist)
- `scripts/*.py` — Python utilities for data scraping and analysis

## Commands

| Command | Sub-Skill |
|---------|-----------|
| `/comp teardown` | Full competitor teardown |
| `/comp positioning` | Perceptual mapping & positioning matrix |
| `/comp swot` | SWOT analysis with strategic implications |
| `/comp pricing` | Pricing intelligence & packaging analysis |
| `/comp ads` | Ad intelligence & spend estimation |
| `/comp content` | Content gap analysis |
| `/comp tech` | Technology stack detection |
| `/comp battlecard` | Sales battlecard generator |
| `/comp report` | Full competitive intelligence report |

## Development Rules

- Keep CLAUDE.md files focused and under 500 lines
- Use kebab-case for directory names
- Agents run via Task tool with `context: fork`
- All data points must have confidence tags (Confirmed / Estimated / Inferred)
- Cite sources for all claims
- Use only publicly available, ethical data sources
- All output files go to current working directory
