# Commands Reference

## Overview

All commands use the `/feed` prefix. Each command triggers a specialized sub-skill that analyzes a specific aspect of your Google Merchant Center product feed.

## Commands

### `/feed audit`

**Full feed health audit.** Runs all sub-skills and produces a comprehensive analysis covering approval rates, attribute completeness, title quality, description quality, image compliance, and custom label utilization.

**When to use:** First-time feed analysis, monthly health checks, after major feed changes.

**Output:** Overall score (0-100), component scores, top issues, prioritized action plan.

**Example:**
```
/feed audit
> Analyzing feed: my-products.csv (2,847 products)
> Overall Score: 72/100 (Grade: C)
> Top Issue: 340 products missing GTIN — est. -15% impressions
```

---

### `/feed titles`

**Optimize product titles.** Scores every title against the proven formula: Brand + Product Type + Key Attributes. Identifies titles that are too short, missing brand, keyword-stuffed, or contain promotional text.

**When to use:** After initial audit flags title quality issues, when adding new products, quarterly optimization.

**Output:** Per-product title scores, category-specific rewrite suggestions, before/after examples.

---

### `/feed descriptions`

**Audit and optimize descriptions.** Checks length, keyword integration, policy compliance, and completeness. Flags promotional text, placeholder descriptions, and HTML tags.

**When to use:** When descriptions score below 70, after adding new products, when targeting long-tail queries.

**Output:** Per-product description scores, template-based rewrites, policy violation flags.

---

### `/feed images`

**Image compliance audit.** Validates image URLs, checks dimensions against category-specific minimums, flags potential watermarks/overlays, and assesses additional image coverage.

**When to use:** After image-related disapprovals, when onboarding new product photography, quarterly compliance check.

**Output:** Image compliance rate, broken URL list, policy violation flags, additional image recommendations.

---

### `/feed attributes`

**Attribute completeness check.** Validates all required attributes (id, title, description, link, image_link, availability, price, brand, condition) and scores recommended attribute fill rates.

**When to use:** After disapprovals for missing attributes, when adding new product categories, monthly data quality check.

**Output:** Required attribute completion rate, recommended fill rate, GTIN validity check, category-specific attribute compliance.

---

### `/feed labels`

**Custom label strategy.** Audits custom_label_0 through custom_label_4 utilization, checks value consistency, and recommends segmentation strategies for campaign structure.

**When to use:** When setting up new PMax/Shopping campaigns, quarterly label refresh, when labels are unused.

**Output:** Label utilization report, value distribution, consistency issues, strategy recommendations.

---

### `/feed disapprovals`

**Disapproval diagnosis.** Categorizes disapproved products by root cause (data quality, image violations, policy violations, landing page errors) and provides exact fixes prioritized by revenue impact.

**When to use:** When disapproval rate exceeds 5%, after receiving MC policy warnings, when products stop showing in ads.

**Output:** Disapproval breakdown by category, root cause analysis, fix plan with effort estimates, prevention checklist.

---

### `/feed report`

**Comprehensive health report.** Consolidates all sub-skill findings into an executive summary with weighted scoring, trend tracking, benchmarks, and a prioritized action plan.

**When to use:** Weekly/monthly reporting, stakeholder updates, before/after optimization comparison.

**Output:** Full formatted report with overall score, component breakdown, score distribution, top issues, and recommendations.

---

## Command Combinations

| Goal | Commands to Run |
|---|---|
| First-time audit | `/feed audit` (runs everything) |
| Fix disapprovals fast | `/feed disapprovals` then `/feed attributes` |
| Improve CTR | `/feed titles` then `/feed images` |
| Campaign restructure | `/feed labels` |
| Monthly health check | `/feed report` |
| Pre-launch checklist | `/feed audit` then `/feed report` |

## Using with Scripts

The Python scripts provide the same analysis programmatically:

```bash
# Quick analysis with summary
python scripts/feed_analyzer.py feed/my-products.csv

# Full report with export
python scripts/feed_report.py feed/my-products.csv --output report.txt --scores scores.csv

# Trend comparison
python scripts/feed_report.py feed/my-products.csv --previous last-month-scores.csv
```
