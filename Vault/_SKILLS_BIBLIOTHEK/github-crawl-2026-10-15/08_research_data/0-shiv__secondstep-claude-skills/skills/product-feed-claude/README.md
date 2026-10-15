# Product Feed Claude

> Your product feed is the foundation of Shopping & PMax. This skill audits and optimizes titles, descriptions, images, attributes & disapprovals.

## Why Feed Quality Matters

- **76%** of Shopping ad spend is determined by feed quality
- **Optimized titles** increase CTR by 40%
- **18%** of products get disapproved due to feed errors

Your Google Merchant Center product feed is the single most important lever for Shopping and Performance Max campaigns. A poorly optimized feed means wasted budget, missing impressions, and lost revenue. This skill suite gives you everything you need to audit, fix, and optimize every aspect of your feed.

## Commands

| Command | Description |
|---|---|
| `/feed audit` | Full feed health audit — approval rates, attribute completeness, title quality |
| `/feed titles` | Optimize product titles using proven formulas for higher CTR |
| `/feed descriptions` | Write keyword-rich, policy-compliant descriptions |
| `/feed images` | Audit images for compliance and optimization opportunities |
| `/feed attributes` | Check required and recommended attributes for completeness |
| `/feed labels` | Set up custom labels (0-4) for campaign segmentation |
| `/feed disapprovals` | Diagnose and fix product disapprovals |
| `/feed report` | Generate a comprehensive feed health report with recommendations |

## Quick Start

1. Export your product feed from Google Merchant Center (CSV, TSV, or XML)
2. Place the file in the `feed/` directory
3. Run `/feed audit` for a full health check
4. Follow the skill-specific recommendations to optimize

## Project Structure

```
product-feed-claude/
  feed/              # Place your feed files here (CSV, TSV, XML)
  skills/            # 8 optimization skill modules
  agents/            # AI agent configurations
  scripts/           # Python analysis scripts
  docs/              # Reference documentation
  assets/            # Templates and sample data
```

## Skills Overview

| Skill | Focus Area | Impact |
|---|---|---|
| Title Optimization | Front-load keywords, category templates | +40% CTR |
| Description | Keyword-rich, policy-compliant copy | +15% relevance |
| Images | Compliance, quality, white background | -30% disapprovals |
| Attributes | Required + recommended completeness | +25% impressions |
| Custom Labels | Segmentation for bidding strategy | +20% ROAS |
| Disapprovals | Diagnosis and automated fixes | -60% disapprovals |
| Supplemental Feeds | Title overrides, enrichment | +35% coverage |
| Feed Report | Health scoring and recommendations | Actionable insights |

## Requirements

- Python 3.8+ (for analysis scripts)
- Google Merchant Center account
- Product feed export (CSV, TSV, or XML format)

## Author

**Shivendra Rawat** ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)

## License

MIT
