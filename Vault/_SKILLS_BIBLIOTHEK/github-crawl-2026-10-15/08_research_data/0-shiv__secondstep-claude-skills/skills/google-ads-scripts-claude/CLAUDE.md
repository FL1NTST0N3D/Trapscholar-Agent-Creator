# Claude Code Configuration — Google Ads Scripts

## Project Overview

A Claude Code skill that generates, debugs, and optimizes Google Ads Scripts — JavaScript automations running directly inside Google Ads accounts. 50+ ready-to-use scripts across 10 categories: budget alerts, bid rules, reporting, link checking, Quality Score, search terms, anomaly detection, labeling, script generation, and script auditing.

## Architecture

```
google-ads-scripts-claude/
├── SKILL.md                      # Master skill reference (loaded by Claude Code)
├── CLAUDE.md                     # This file — project config & dev rules
├── .claudeignore                 # Files excluded from Claude context
├── scripts-skill/
│   └── SKILL.md                  # Script skill entry point
├── skills/                       # Sub-skills (one per script category)
│   ├── script-budget-alerts/     # /script budget
│   ├── script-bid-management/    # /script bids
│   ├── script-reporting/         # /script report
│   ├── script-link-checker/      # /script links
│   ├── script-quality-score/     # /script qs
│   ├── script-search-terms/      # /script search-terms
│   ├── script-anomaly-detection/ # /script anomaly
│   ├── script-labeling/          # /script labels
│   ├── script-generator/         # /script generate
│   └── script-report/            # /script audit
├── agents/                       # Claude Code agents
│   ├── script-builder.md         # Generates scripts from descriptions
│   ├── script-debugger.md        # Diagnoses and fixes script errors
│   └── script-optimizer.md       # Improves script performance
├── scripts/                      # Python utilities
│   ├── validate-script.py        # Syntax validation for generated scripts
│   └── template-renderer.py      # Renders templates with user config
├── templates/                    # JavaScript script templates
│   ├── budget-pacing.js
│   ├── bid-adjustments.js
│   ├── daily-report.js
│   ├── link-checker.js
│   ├── qs-tracker.js
│   ├── search-term-miner.js
│   ├── anomaly-alert.js
│   └── auto-labeler.js
├── docs/                         # Reference documentation
│   ├── google-ads-scripts-api.md
│   ├── execution-limits.md
│   ├── troubleshooting.md
│   └── best-practices.md
└── assets/
    └── .gitkeep
```

## Commands

| Command | Description |
|---------|-------------|
| `/script generate` | Generate a custom script from plain English description |
| `/script budget` | Budget pacing and alert scripts |
| `/script bids` | Bid adjustment and optimization scripts |
| `/script report` | Automated reporting scripts |
| `/script links` | URL validation and broken link detection scripts |
| `/script qs` | Quality Score tracking scripts |
| `/script search-terms` | Search term mining and negative keyword scripts |
| `/script anomaly` | Performance anomaly detection scripts |
| `/script labels` | Auto-labeling scripts |
| `/script audit` | Script inventory and health check |

## Dev Commands

```bash
python scripts/validate-script.py templates/budget-pacing.js   # Validate a template
python scripts/template-renderer.py templates/daily-report.js   # Render with defaults
```

## Dev Rules

### Script Generation
- Always generate complete, runnable JavaScript — never pseudocode
- Include a `CONFIG` object at the top of every script for easy customization
- Add try/catch error handling to every script
- Include `Logger.log()` statements for debugging
- Use GAQL (Google Ads Query Language) for reports — never deprecated AWQL
- Every script must have a `function main() {}` entry point
- Respect execution limits: 30 min runtime, 250K API calls, 50 URL fetches
- For MCC accounts, use `MccApp.accounts()` pattern
- Default date ranges to `LAST_30_DAYS` unless user specifies otherwise
- Cost values from API are in micros — always divide by 1,000,000

### Code Style
- Use `var` for broadest compatibility (some environments are ES5 only)
- Use descriptive variable names
- Group configuration constants at the top
- Use helper functions for reusable logic
- Format email HTML with inline styles (no external CSS in Google Ads email)

### Sub-Skill Loading
When a user runs a `/script` command, load the corresponding sub-skill from `skills/script-*/SKILL.md` for detailed context and templates.

### File Conventions
- JavaScript templates: kebab-case `.js` files in `templates/`
- Skill definitions: `SKILL.md` inside each `skills/script-*/` directory
- Agent definitions: kebab-case `.md` files in `agents/`
- Python utilities: kebab-case `.py` files in `scripts/`
