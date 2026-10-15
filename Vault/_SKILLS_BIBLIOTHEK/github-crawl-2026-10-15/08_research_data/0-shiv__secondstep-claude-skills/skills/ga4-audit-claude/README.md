# GA4 Audit Claude Skill

> **80% of GA4 implementations are broken or incomplete. This skill audits every setting, event, and conversion in your GA4 property.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://github.com/0-shiv/ga4-audit-claude)

---

## The Problem

Google Analytics 4 is powerful but notoriously complex to implement correctly. The data tells the story:

| Stat | Reality |
|------|---------|
| **80%** | of GA4 setups are misconfigured or incomplete |
| **34%** | of events fire incorrectly on average |
| **12%** | of properties use custom dimensions properly |
| **67%** | have broken or missing e-commerce tracking |
| **45%** | never configure attribution settings from defaults |
| **90%** | miss critical recommended events for their business type |

Bad analytics = bad decisions = lost revenue.

## What This Skill Does

This Claude Code skill performs a comprehensive audit of any GA4 property across **10 audit dimensions**, producing a **GA4 Health Score (0-100)** and actionable fix recommendations.

## Commands

| Command | Description |
|---------|-------------|
| `/ga4 audit` | Run a full GA4 property audit across all dimensions |
| `/ga4 streams` | Audit web/app data stream configuration |
| `/ga4 events` | Audit event implementation and naming conventions |
| `/ga4 conversions` | Audit conversion event setup and Google Ads import |
| `/ga4 audiences` | Audit audience configuration and predictive audiences |
| `/ga4 attribution` | Audit attribution model and lookback window settings |
| `/ga4 ecommerce` | Audit e-commerce event implementation |
| `/ga4 dimensions` | Audit custom dimension and metric registration |
| `/ga4 reporting` | Audit report configuration and exploration setup |
| `/ga4 integrations` | Audit Google product integrations (Ads, SC, BQ) |
| `/ga4 report` | Generate the final audit report with scores and fixes |

## GA4 Health Score

The Health Score (0-100) is calculated across 8 weighted dimensions:

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| Data Streams | 10% | Stream config, enhanced measurement, filters |
| Events | 20% | Event coverage, naming, parameter validation |
| Conversions | 15% | Conversion setup, counting method, Ads import |
| Audiences | 10% | Audience creation, predictive, Ads export |
| Attribution | 10% | Model selection, lookback windows, paths |
| E-commerce | 15% | Purchase funnel events, revenue tracking |
| Custom Dimensions | 10% | Dimension registration, quota usage |
| Integrations | 10% | Google product linking status |

### Score Ranges

| Score | Grade | Meaning |
|-------|-------|---------|
| 90-100 | A | Excellent — production-ready, well-optimized |
| 75-89 | B | Good — minor gaps, mostly functional |
| 50-74 | C | Fair — significant gaps affecting data quality |
| 25-49 | D | Poor — major issues, unreliable data |
| 0-24 | F | Critical — fundamentally broken, needs rebuild |

## Installation

```bash
# Clone the repo
git clone https://github.com/0-shiv/ga4-audit-claude.git

# Run the installer
cd ga4-audit-claude
chmod +x install.sh
./install.sh

# Or manual install — copy to your Claude Code skills directory
cp -r skills/* ~/.claude/skills/
cp SKILL.md ~/.claude/skills/ga4-audit/SKILL.md
```

## Requirements

- Claude Code CLI
- Python 3.8+ (for report generation scripts)
- Google Analytics 4 property access (Admin or Viewer role)
- Google Analytics Data API credentials (optional, for automated audits)

## Project Structure

```
ga4-audit-claude/
├── SKILL.md                    # Main skill routing file
├── README.md                   # This file
├── CLAUDE.md                   # Claude Code project instructions
├── CONTRIBUTING.md             # Contribution guidelines
├── CHANGELOG.md                # Version history
├── LICENSE                     # MIT License
├── install.sh                  # Installation script
├── uninstall.sh                # Uninstallation script
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── ga4/                        # GA4 reference data
├── skills/                     # Sub-skill definitions
│   ├── ga4-data-streams/       # Data stream audit
│   ├── ga4-events/             # Event audit
│   ├── ga4-conversions/        # Conversion audit
│   ├── ga4-audiences/          # Audience audit
│   ├── ga4-attribution/        # Attribution audit
│   ├── ga4-ecommerce/          # E-commerce audit
│   ├── ga4-custom-dimensions/  # Custom dimensions audit
│   ├── ga4-reporting/          # Reporting audit
│   ├── ga4-integrations/       # Integrations audit
│   └── ga4-report/             # Report generation
├── agents/                     # Agent definitions
├── scripts/                    # Python utility scripts
├── templates/                  # Report templates
├── docs/                       # Documentation
└── assets/                     # Static assets
```

## Usage Examples

### Full Property Audit
```
/ga4 audit
```
Runs all 10 audit dimensions and produces a comprehensive report with Health Score.

### Targeted Event Audit
```
/ga4 events
```
Checks event naming conventions, parameter validation, and coverage against recommended events.

### E-commerce Funnel Check
```
/ga4 ecommerce
```
Validates the complete purchase funnel from `view_item_list` through `purchase` and `refund`.

## Author

**Shivendra Rawat** ([@0-shiv](https://github.com/0-shiv))

- Agency: [Second Step](https://getsecondstep.com)
- Focus: Performance marketing, Google Ads, analytics, AI automation

## License

MIT License. See [LICENSE](LICENSE) for details.
