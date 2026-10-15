# Feed Report Skill

## Command
`/feed report`

## Overview

The feed health report is the executive summary of your entire product feed quality. It consolidates findings from all other sub-skills (titles, descriptions, images, attributes, labels, disapprovals) into a single scored report with prioritized recommendations. Run this after a full `/feed audit` or on a regular schedule (weekly or monthly) to track feed health over time.

The report uses a weighted scoring model that reflects each factor's impact on Shopping and PMax campaign performance. A feed scoring 90+ is well-optimized; below 50 indicates critical issues that are actively costing revenue.

## Report Sections

### 1. Executive Summary
One-page overview for stakeholders:
- Overall feed health score (0-100)
- Total products in feed vs approved vs disapproved
- Estimated revenue impact of identified issues
- Top 3 highest-impact recommendations
- Trend vs previous report (improving, stable, declining)

### 2. Approval Status
Product approval breakdown:

| Status | Definition | Target |
|---|---|---|
| Approved | Active in Shopping ads and free listings | > 95% |
| Disapproved | Blocked from all surfaces | < 2% |
| Pending | Under review or processing | < 3% |
| Warning | Approved but with issues that may escalate | < 5% |
| Expiring | Feed data older than 30 days, will auto-expire | 0% |

### 3. Title Quality Score
Aggregated title analysis:
- Average title length (target: 80-120 characters)
- Percentage following brand-first formula
- Percentage with key attributes present (color, size, material)
- Distribution across score bands (excellent/good/needs work/critical)

### 4. Description Quality Score
Aggregated description analysis:
- Average description length (target: 750-1,500 characters)
- Percentage with 500+ character descriptions
- Policy compliance rate (no promotional text)
- Keyword density assessment

### 5. Image Compliance Score
Image quality summary:
- Percentage meeting size requirements
- Compliance rate (no watermarks, overlays, borders)
- Additional image utilization (products with 3+ images)
- Average fill ratio

### 6. Attribute Completeness Score
Required and recommended attribute fill rates:
- Required attribute completion rate (target: 100%)
- Recommended attribute completion rate (target: 80%+)
- GTIN coverage and validity rate
- Category-specific attribute compliance (apparel, electronics)

### 7. Custom Label Utilization
Label strategy assessment:
- Number of label slots in use (target: 4-5 of 5)
- Value consistency check
- Campaign segmentation coverage
- Label freshness (when last updated)

### 8. Data Accuracy
Feed-to-landing-page consistency:
- Price match rate (feed vs website)
- Availability match rate
- URL health (200 status, no redirect chains)
- GTIN validity rate

## Scoring Model

### Weighted Score Calculation

| Factor | Weight | Measurement |
|---|---|---|
| Title Quality | 30% | Average title score across all products |
| Attribute Completeness | 25% | Required (15%) + Recommended (10%) fill rate |
| Image Compliance | 20% | Compliance rate * quality score |
| Description Quality | 15% | Average description score across all products |
| Data Accuracy | 10% | Price + availability + URL + GTIN accuracy |

**Overall Score = (Title * 0.30) + (Attributes * 0.25) + (Images * 0.20) + (Description * 0.15) + (Accuracy * 0.10)**

### Score Bands

| Score | Grade | Status | Action |
|---|---|---|---|
| 90-100 | A | Excellent | Maintain current practices, focus on marginal gains |
| 80-89 | B | Good | Minor optimizations available, low urgency |
| 70-79 | C | Average | Noticeable gaps, prioritize top recommendations |
| 60-69 | D | Below Average | Significant issues, schedule remediation sprint |
| 50-59 | E | Poor | Major problems, immediate action required |
| 0-49 | F | Critical | Feed is actively losing revenue, emergency fix needed |

## Output Format

```
====================================
  PRODUCT FEED HEALTH REPORT
  Generated: [date]
  Feed: [filename]
  Products: [count]
====================================

OVERALL SCORE: [XX] / 100 — [Grade: A-F]
Trend: [+X / -X / stable] vs previous report

APPROVAL STATUS:
  Approved:     [count] ([pct]%)  [bar chart]
  Disapproved:  [count] ([pct]%)  [bar chart]
  Warnings:     [count] ([pct]%)  [bar chart]
  Pending:      [count] ([pct]%)  [bar chart]

COMPONENT SCORES:
  Title Quality:          [XX]/100  [bar]  Weight: 30%
  Attribute Completeness: [XX]/100  [bar]  Weight: 25%
  Image Compliance:       [XX]/100  [bar]  Weight: 20%
  Description Quality:    [XX]/100  [bar]  Weight: 15%
  Data Accuracy:          [XX]/100  [bar]  Weight: 10%

KEY METRICS:
  Avg Title Length:       [XX] chars (target: 80-120)
  Avg Description Length: [XXX] chars (target: 750-1,500)
  GTIN Coverage:          [XX]% (target: 95%+)
  Image Compliance:       [XX]% (target: 98%+)
  Recommended Attr Fill:  [XX]% (target: 80%+)
  Custom Labels Used:     [X] / 5 slots

TOP 5 ISSUES (by revenue impact):
  1. [issue] — [count] products — est. $[amount]/mo impact
  2. [issue] — [count] products — est. $[amount]/mo impact
  3. [issue] — [count] products — est. $[amount]/mo impact
  4. [issue] — [count] products — est. $[amount]/mo impact
  5. [issue] — [count] products — est. $[amount]/mo impact

PRIORITIZED ACTION PLAN:
  THIS WEEK (quick wins):
  [ ] [action] — fixes [count] products — [XX] min effort
  [ ] [action] — fixes [count] products — [XX] min effort

  THIS MONTH (medium effort):
  [ ] [action] — fixes [count] products — [X] hours effort
  [ ] [action] — fixes [count] products — [X] hours effort

  THIS QUARTER (strategic):
  [ ] [action] — estimated +[XX]% impressions
  [ ] [action] — estimated +[XX]% ROAS

CATEGORY BREAKDOWN:
  [Category 1]: [count] products, score [XX]/100
  [Category 2]: [count] products, score [XX]/100
  [Category 3]: [count] products, score [XX]/100
```

## Report Generation Process

### Step 1: Run All Sub-Skills
Execute each analysis module:
1. `/feed titles` — generate title scores
2. `/feed descriptions` — generate description scores
3. `/feed images` — generate image compliance scores
4. `/feed attributes` — generate attribute completeness scores
5. `/feed labels` — generate label utilization scores
6. `/feed disapprovals` — generate disapproval diagnosis

### Step 2: Calculate Weighted Score
1. Collect component scores from each sub-skill
2. Apply weights (30/25/20/15/10)
3. Calculate overall score
4. Determine grade (A-F)

### Step 3: Identify Top Issues
1. Rank all issues by estimated revenue impact
2. Categorize by effort level (quick win, medium, strategic)
3. Create prioritized action plan
4. Estimate time to fix each issue

### Step 4: Generate Trend Data
If previous reports exist:
1. Compare overall score vs last report
2. Identify improving and declining areas
3. Track disapproval rate trend
4. Note which previous recommendations were implemented

## Benchmarks

Industry benchmarks for feed quality (based on Google Merchant Center data):

| Metric | Poor | Average | Good | Excellent |
|---|---|---|---|---|
| Approval Rate | < 80% | 80-90% | 90-95% | > 95% |
| Avg Title Length | < 40 chars | 40-70 | 70-100 | 100-130 |
| Description Fill Rate | < 50% | 50-75% | 75-90% | > 90% |
| GTIN Coverage | < 50% | 50-70% | 70-90% | > 90% |
| Recommended Attr Fill | < 30% | 30-50% | 50-70% | > 70% |
| Custom Labels Used | 0 | 1-2 | 3-4 | 5 |
| Image Compliance | < 70% | 70-85% | 85-95% | > 95% |

## Impact
- **Visibility into feed health** — single score tracks overall quality
- **Prioritized action** — focus effort on highest-revenue-impact fixes
- **Trend tracking** — monitor improvement over time
- **Stakeholder communication** — executive-friendly format for reporting

## Author
Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | Second Step
