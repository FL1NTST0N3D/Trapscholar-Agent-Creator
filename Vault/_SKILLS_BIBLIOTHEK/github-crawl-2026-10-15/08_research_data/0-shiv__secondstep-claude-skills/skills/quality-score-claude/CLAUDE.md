# Quality Score Claude — Project Reference

## Overview

A Claude Code skill for deep Google Ads Quality Score analysis, optimization, and reporting. Analyzes QS across all three components (Expected CTR, Landing Page Experience, Ad Relevance), calculates CPC waste, and generates actionable fix lists sorted by dollar impact.

## Architecture

```
quality-score-claude/
├── SKILL.md                          # Main skill definition & command routing
├── qs/                               # Core QS logic
├── skills/                           # 10 sub-skills (one per /qs command)
│   ├── qs-component-analysis/        # /qs components
│   ├── qs-cpc-impact/                # /qs impact
│   ├── qs-trend-tracker/             # /qs trends
│   ├── qs-distribution/              # /qs distribution
│   ├── qs-keyword-level/             # /qs keywords
│   ├── qs-landing-page/              # /qs landing-pages
│   ├── qs-ad-relevance/              # /qs relevance
│   ├── qs-expected-ctr/              # /qs ctr
│   ├── qs-optimizer/                 # /qs optimize
│   └── qs-report/                    # /qs report
├── agents/                           # 4 agent definitions
│   ├── qs-analyst.md                 # Full account analysis agent
│   ├── qs-monitor.md                 # QS trend monitoring agent
│   ├── qs-optimizer.md               # Optimization recommendation agent
│   └── qs-reporter.md                # Report generation agent
├── scripts/                          # Python analysis scripts
│   ├── qs_analyzer.py                # Core analyzer
│   ├── qs_distribution.py            # Distribution histogram
│   ├── cpc_impact_calculator.py      # CPC waste calculator
│   └── generate_qs_report.py         # Report generator
├── templates/                        # Report & export templates
├── docs/                             # Extended documentation
└── assets/                           # Static assets
```

## Commands

| Command | Description | Sub-skill |
|---------|-------------|-----------|
| `/qs analyze` | Full QS analysis across account | Runs all sub-skills |
| `/qs components` | Break down QS into 3 components | qs-component-analysis |
| `/qs impact` | Calculate CPC waste from low QS | qs-cpc-impact |
| `/qs trends` | Track QS changes over time | qs-trend-tracker |
| `/qs distribution` | Histogram of QS across keywords | qs-distribution |
| `/qs keywords` | Per-keyword audit by savings | qs-keyword-level |
| `/qs landing-pages` | Landing Page Experience analysis | qs-landing-page |
| `/qs relevance` | Ad Relevance deep dive | qs-ad-relevance |
| `/qs ctr` | Expected CTR analysis | qs-expected-ctr |
| `/qs optimize` | Actionable optimization playbook | qs-optimizer |
| `/qs report` | Full audit report with savings | qs-report |

## Development Rules

- Each sub-skill lives in its own directory under `skills/` with a `SKILL.md`
- All output follows the format: Summary > Key Metrics > Analysis > Action Items > Estimated Impact
- Always attach dollar values to QS findings, never report QS in isolation
- Prioritize by spend-weighted QS gap (high-spend low-QS keywords first)
- Group fixes by root cause (e.g., 15 keywords pointing to same bad landing page = 1 fix)
- Python scripts require Python 3.9+
- Templates in `templates/` are user-facing export formats

## Requirements

- Claude Code CLI
- Python 3.9+
- Google Ads API access or CSV export
