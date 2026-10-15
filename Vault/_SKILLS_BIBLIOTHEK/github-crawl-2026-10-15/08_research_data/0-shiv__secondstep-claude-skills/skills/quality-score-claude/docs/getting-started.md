# Getting Started with Quality Score Claude

## Prerequisites

1. **Claude Code CLI** installed and authenticated
2. **Python 3.9+** for analysis scripts
3. **Google Ads account access** with keyword data

## Installation

### Option 1: Install from GitHub
```bash
claude skill install 0-shiv/quality-score-claude
```

### Option 2: Manual Clone
```bash
git clone https://github.com/0-shiv/quality-score-claude.git ~/.claude/skills/quality-score-claude
```

## Exporting Data from Google Ads

To run a QS analysis, you need keyword-level data with Quality Score columns. Here is how to export it:

### Step 1: Navigate to Keywords
1. Log into Google Ads
2. Go to **Keywords** > **Search keywords**

### Step 2: Add QS Columns
1. Click the **Columns** icon (three vertical lines)
2. Click **Modify columns**
3. Expand **Quality Score** section
4. Add these columns:
   - Quality Score
   - Exp. CTR
   - Ad relevance
   - Landing page exp.
5. Also ensure you have: Keyword, Match type, Campaign, Ad group, Impressions, Clicks, CTR, Avg. CPC, Cost, Conversions, Conv. rate, Cost/conv., Final URL
6. Click **Apply**

### Step 3: Download
1. Click the **Download** icon (down arrow)
2. Select **CSV** format
3. Save the file

### Step 4: Analyze
```bash
# Quick analysis
python scripts/qs_analyzer.py your_export.csv

# CPC impact calculation
python scripts/cpc_impact_calculator.py your_export.csv

# Distribution histogram
python scripts/qs_distribution.py your_export.csv

# Full audit report
python scripts/generate_qs_report.py your_export.csv --account-name "Your Account" --output report.md
```

Or use the Claude Code skill commands:
```
/qs analyze
/qs impact
/qs distribution
/qs report
```

## Quick Start Commands

| What You Want | Command |
|:--|:--|
| Full account analysis | `/qs analyze` |
| See where money is wasted | `/qs impact` |
| See QS distribution | `/qs distribution` |
| Get a fix list | `/qs optimize` |
| Generate client report | `/qs report` |

## Next Steps

- Read the [QS Fundamentals](./qs-fundamentals.md) doc for deeper understanding
- Check the [FAQ](./faq.md) for common questions
- Review the [CPC Impact methodology](./cpc-impact-methodology.md) for how savings are calculated
