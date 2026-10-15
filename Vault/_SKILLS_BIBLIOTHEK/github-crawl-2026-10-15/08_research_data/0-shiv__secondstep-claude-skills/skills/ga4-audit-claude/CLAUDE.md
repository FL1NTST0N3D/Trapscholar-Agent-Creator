# GA4 Audit Claude Skill — Project Guide

## Overview

This is a Claude Code skill that performs comprehensive audits of Google Analytics 4 properties. It evaluates 10 audit dimensions and produces a GA4 Health Score (0-100) with actionable fix recommendations.

## Architecture

```
ga4-audit-claude/
├── SKILL.md                    # Main skill router — maps /ga4 commands to sub-skills
├── skills/                     # 10 sub-skill definitions (one per audit dimension)
│   ├── ga4-data-streams/       # Stream config, enhanced measurement, filters
│   ├── ga4-events/             # Event coverage, naming, parameter validation
│   ├── ga4-conversions/        # Conversion setup, counting method, Ads import
│   ├── ga4-audiences/          # Audience creation, predictive, Ads export
│   ├── ga4-attribution/        # Model selection, lookback windows
│   ├── ga4-ecommerce/          # Purchase funnel events, revenue tracking
│   ├── ga4-custom-dimensions/  # Dimension registration, quota usage
│   ├── ga4-reporting/          # Reports and explorations
│   ├── ga4-integrations/       # Google product linking (Ads, SC, BQ)
│   └── ga4-report/             # Final report compilation
├── agents/                     # Agent definitions for orchestration
│   ├── audit-orchestrator.md   # Full audit flow coordinator
│   ├── event-validator.md      # Event naming and parameter checks
│   ├── ecommerce-debugger.md   # E-commerce funnel debugging
│   └── report-generator.md     # Report compilation and formatting
├── scripts/                    # Python utilities
│   ├── health_score.py         # Health Score calculator (weighted scoring)
│   ├── event_validator.py      # Event naming convention validator
│   └── report_generator.py     # Audit report generator
├── docs/                       # Reference documentation
│   ├── ga4-event-reference.md  # Complete GA4 event reference
│   ├── audit-methodology.md    # Audit methodology details
│   └── common-issues.md        # Common GA4 misconfigurations
└── templates/                  # Report output templates (future)
```

## Commands

All commands are prefixed with `/ga4`:

| Command | What It Does |
|---------|-------------|
| `/ga4 audit` | Full audit — runs all 10 dimensions in sequence |
| `/ga4 streams` | Audit data stream configuration |
| `/ga4 events` | Audit event implementation and naming |
| `/ga4 conversions` | Audit conversion event setup |
| `/ga4 audiences` | Audit audience configuration |
| `/ga4 attribution` | Audit attribution model settings |
| `/ga4 ecommerce` | Audit e-commerce event implementation |
| `/ga4 dimensions` | Audit custom dimension registration |
| `/ga4 reporting` | Audit report and exploration setup |
| `/ga4 integrations` | Audit Google product integrations |
| `/ga4 report` | Generate the final scored audit report |

## Health Score Calculation

The Health Score (0-100) uses weighted scoring across 8 dimensions. E-commerce and non-e-commerce properties use different weight distributions. See `scripts/health_score.py` for the implementation.

## Development Rules

1. **Skill files are markdown** — Each sub-skill lives in `skills/<name>/SKILL.md`. These files define the audit checklist, scoring criteria, and output format for that dimension.

2. **Snake_case for GA4 events** — Always reference GA4 events in snake_case (e.g., `add_to_cart`, not `AddToCart`).

3. **Audit output format** — All audit findings must follow the standard format defined in the main `SKILL.md`: passed checks, failed checks (with impact/current/recommended/fix), and warnings.

4. **Python scripts** — Located in `scripts/`. Require Python 3.8+. No external dependencies beyond the standard library (json, argparse, sys, typing).

5. **Agent definitions** — Located in `agents/`. Each agent markdown file defines the agent's role, capabilities, and orchestration rules.

6. **Do not modify SKILL.md routing** — The main SKILL.md maps commands to sub-skills. Changes to routing should be deliberate and reflected in README.md.

7. **Testing** — Run `python scripts/health_score.py --scores '{"events": 80, "conversions": 65}' --json` to verify the scoring calculator works.

## Running Python Scripts

```bash
# Health Score Calculator
python scripts/health_score.py --interactive
python scripts/health_score.py --scores '{"events": 80, "conversions": 65, "data_streams": 90}'
python scripts/health_score.py --file audit_results.json --json

# Event Validator
python scripts/event_validator.py

# Report Generator
python scripts/report_generator.py
```
