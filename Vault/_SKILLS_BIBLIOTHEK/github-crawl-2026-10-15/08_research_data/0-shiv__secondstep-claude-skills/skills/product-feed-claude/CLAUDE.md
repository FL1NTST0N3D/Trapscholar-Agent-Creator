# Product Feed Claude — Architecture

## What This Is

A Claude Code skill suite for auditing and optimizing Google Merchant Center product feeds. Eight sub-skills cover every aspect of feed quality: titles, descriptions, images, attributes, custom labels, disapprovals, supplemental feeds, and health reporting.

## Repository Structure

```
product-feed-claude/
  SKILL.md                    # Master orchestrator — routes /feed commands to sub-skills
  CLAUDE.md                   # This file — architecture and dev rules
  README.md                   # Public-facing documentation

  skills/                     # 8 sub-skill modules
    feed-title-optimization/  # /feed titles — title formula + scoring
    feed-description/         # /feed descriptions — keyword-rich copy
    feed-images/              # /feed images — compliance + quality
    feed-attributes/          # /feed attributes — required + recommended validation
    feed-labels/              # /feed labels — custom label strategy
    feed-disapprovals/        # /feed disapprovals — diagnosis + fixes
    feed-supplemental/        # /feed supplemental — override feeds
    feed-report/              # /feed report — health report generation

  agents/                     # AI agent configurations
    feed-quality.md           # Analyzes title/description/image quality
    feed-compliance.md        # Checks policy violations and disapprovals

  scripts/                    # Python analysis tools
    feed_analyzer.py          # Parses CSV/TSV, scores products, outputs stats
    feed_report.py            # Generates formatted health report

  docs/                       # Reference documentation
    INSTALLATION.md           # Setup instructions
    COMMANDS.md               # Command reference
    SCORING.md                # Scoring methodology

  feed/                       # User places feed files here (gitignored)
  assets/                     # Templates and sample data
```

## Commands

| Command | Sub-Skill | Script |
|---|---|---|
| `/feed audit` | Master SKILL.md | feed_analyzer.py |
| `/feed titles` | feed-title-optimization | — |
| `/feed descriptions` | feed-description | — |
| `/feed images` | feed-images | — |
| `/feed attributes` | feed-attributes | — |
| `/feed labels` | feed-labels | — |
| `/feed disapprovals` | feed-disapprovals | — |
| `/feed report` | feed-report | feed_report.py |

## Scoring Model

Weighted scoring across 5 dimensions:
- Title Quality: 30%
- Attribute Completeness: 25%
- Image Compliance: 20%
- Description Quality: 15%
- Data Accuracy: 10%

Grades: A (90-100), B (80-89), C (70-79), D (60-69), E (50-59), F (0-49)

## Dev Rules

1. **All Google Merchant Center specs must be current.** When in doubt, reference Google's official product data specification.
2. **Scoring must be deterministic.** Same input feed must produce same scores every time.
3. **Sub-skills are independent.** Each sub-skill SKILL.md is self-contained and can be used standalone.
4. **Scripts use only stdlib + pandas/openpyxl.** No unnecessary dependencies.
5. **Feed files are never committed.** The `feed/` directory is gitignored — it contains user data.
6. **Output format is consistent.** All sub-skills follow the same report structure: summary, details, recommendations.
7. **Recommendations are specific.** Never output vague advice like "improve your titles." Always specify what to change, on how many products, with estimated impact.
8. **Policy references are accurate.** When citing Google Shopping policies, use exact policy names and current requirements.

## Testing

```bash
# Run analyzer on a test feed
python scripts/feed_analyzer.py feed/test-feed.csv --output test-scores.csv

# Generate a full report
python scripts/feed_report.py feed/test-feed.csv --output test-report.txt

# Compare with previous run
python scripts/feed_report.py feed/test-feed.csv --previous test-scores.csv
```

## Author

Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)
