---
name: pmax-report
description: "Generate comprehensive Performance Max audit reports with health scores, dimensional breakdowns, critical findings, and prioritized action items. Supports full audit and individual dimension reports."
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
---

# PMax Report Generation Skill

## Purpose

This skill produces structured, actionable PMax audit reports. It aggregates findings from individual dimension audits into a cohesive report with executive summary, detailed scores, and a prioritized action plan. Reports can be generated as markdown, HTML, or fed into PDF generation pipelines.

## Trigger

Activated by `/pmax report` or automatically at the end of `/pmax audit`.

## Report Structure

### 1. Executive Summary

A 3-5 sentence overview that any stakeholder can understand:
- Overall PMax Health Score and rating
- Most critical finding
- Estimated budget impact
- Top priority recommendation

Template:
```
Your Performance Max campaign scored [SCORE]/100 ([RATING]). The most significant
finding is [CRITICAL_ISSUE], which is estimated to cost approximately $[AMOUNT]/month
in wasted or inefficient spend. The top priority action is [TOP_ACTION], which should
be implemented within [TIMEFRAME] to address [EXPECTED_IMPACT].
```

### 2. PMax Health Score Dashboard

```
╔══════════════════════════════════════════════════════╗
║           PMax Health Score: XX/100                  ║
║           Rating: [Excellent/Good/Fair/Poor/Critical]║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  Asset Completeness    [██████████░░░░] XX/100 (25%) ║
║  Asset Performance     [████████░░░░░░] XX/100 (20%) ║
║  Audience Signals      [██████████████] XX/100 (20%) ║
║  URL & Search Config   [██████░░░░░░░░] XX/100 (10%) ║
║  Cannibalization Risk  [████░░░░░░░░░░] XX/100 (15%) ║
║  Budget Efficiency     [████████████░░] XX/100 (10%) ║
║                                                      ║
║  Composite: (25×AC + 20×AP + 20×AS + 10×UC +        ║
║              15×CR + 10×BE) / 100 = XX               ║
╚══════════════════════════════════════════════════════╝
```

### 3. Dimension Deep Dives

For each of the 6 dimensions, include:

#### a. Score and Rating
- Numerical score (0-100)
- Letter grade (A/B/C/D/F)
- Trend indicator (improving/stable/declining) if historical data available

#### b. Key Findings
- 3-5 bullet points of the most important observations
- Each finding labeled: CRITICAL / WARNING / INFO / OPPORTUNITY

#### c. Evidence
- Specific data points that support the findings
- Comparisons to benchmarks
- Screenshots or data references

#### d. Recommendations
- Numbered list, priority-ordered
- Each recommendation includes:
  - What to do (specific action)
  - Why (expected impact)
  - How long it takes (effort estimate)
  - Expected improvement (quantified if possible)

### 4. Asset Performance Summary

```
Asset Inventory by Type
═══════════════════════════════════════════
Type              Count  Required  Ideal  Status
───────────────────────────────────────────
Headlines           X       3       15    [OK/WARN/CRIT]
Long Headlines      X       1        5    [OK/WARN/CRIT]
Descriptions        X       2        5    [OK/WARN/CRIT]
Landscape Images    X       1       4+    [OK/WARN/CRIT]
Square Images       X       1       4+    [OK/WARN/CRIT]
Portrait Images     X       0       2+    [OK/WARN/CRIT]
Horizontal Videos   X       0       2+    [OK/WARN/CRIT]
Vertical Videos     X       0       2+    [OK/WARN/CRIT]
Square Videos       X       0       1+    [OK/WARN/CRIT]
Square Logos        X       1        1    [OK/WARN/CRIT]
Landscape Logos     X       0        1    [OK/WARN/CRIT]

Performance Distribution
═══════════════════════════════════════════
Rating     Count    %     Target    Status
───────────────────────────────────────────
Best         X     X%     >30%     [OK/WARN]
Good         X     X%     >40%     [OK/WARN]
Low          X     X%     <15%     [OK/WARN]
Unrated      X     X%     <15%     [OK/WARN]
```

### 5. Channel Breakdown Estimates

PMax doesn't provide native channel-level reporting. Estimate based on available signals:

```
Estimated Channel Distribution
═══════════════════════════════════════════
Channel              Est. %    Spend     Convs
───────────────────────────────────────────
Search               X%       $X        X
Shopping             X%       $X        X
Display Network      X%       $X        X
YouTube              X%       $X        X
Discover             X%       $X        X
Gmail                X%       $X        X
Maps                 X%       $X        X
───────────────────────────────────────────
Total               100%      $X        X

Note: Channel estimates derived from Insights tab,
placement reports, and search terms data. Actual
distribution may vary.
```

### 6. Competitive Context

If competitive data is available or inferable:

- Industry benchmarks vs. account performance
- Estimated impression share by channel
- Competitive positioning (premium, mid-market, value)
- Seasonal performance context

### 7. Prioritized Action Plan

Structure as a tiered action plan:

```
PRIORITY 1 — Immediate (This Week)
═══════════════════════════════════
□ [Action item with specific steps]
  Impact: [High/Medium/Low]
  Effort: [Hours/Minutes]
  Expected improvement: [Quantified]

□ [Action item]
  ...

PRIORITY 2 — Short-Term (This Month)
═══════════════════════════════════
□ [Action item with specific steps]
  ...

PRIORITY 3 — Ongoing (Monthly Cadence)
═══════════════════════════════════
□ [Action item with specific steps]
  ...
```

### 8. Monitoring Plan

Recommend ongoing monitoring metrics and cadence:

| Metric | Check Frequency | Alert Threshold |
|---|---|---|
| PMax Health Score | Monthly | Drop >10 points |
| Asset performance ratings | Bi-weekly | >30% Low-rated |
| Branded Search impression share | Weekly | >10% decline |
| PMax CPA vs Search CPA | Weekly | PMax >20% higher |
| Feed disapprovals | Daily | Any increase |
| Conversion volume | Daily | >25% decline |

## Report Formats

### Markdown Report (Default)
- Full markdown with tables, headers, and formatting
- Suitable for GitHub, Notion, or direct reading

### HTML Report
- Styled HTML with CSS for professional presentation
- Suitable for sharing with clients or stakeholders
- Uses dark theme with orange accents (Second Step branding)

### CSV Data Export
- Raw scores and metrics in CSV format
- For importing into spreadsheets or dashboards

### JSON Structured Output
- Machine-readable format for automation pipelines
- Schema: `{ health_score, dimensions[], findings[], actions[] }`

## Report Generation Workflow

1. **Collect all dimension scores** from individual audit results
2. **Calculate composite score** using weighted formula
3. **Rank findings** by severity (Critical > Warning > Info > Opportunity)
4. **Generate action items** from findings, prioritized by impact and effort
5. **Estimate budget impact** where quantifiable
6. **Format report** in requested output format
7. **Save report** to specified location

## Historical Tracking

If previous audit reports exist:
- Compare current scores to previous scores
- Calculate score trends per dimension
- Highlight improvements and regressions
- Track action item completion status

## Report Customization

The report can be customized based on audience:

| Audience | Focus | Detail Level | Include |
|---|---|---|---|
| PPC Manager | Technical details | Deep | All dimensions, raw data |
| Marketing Director | Strategic overview | Medium | Summary, key metrics, actions |
| C-Suite / Client | Business impact | High-level | Score, $ impact, top 3 actions |
| Agency Partner | Collaborative | Medium | Findings, shared action plan |

## Scoring Rubric (Meta — Report Quality)

This dimension doesn't have its own health score. Instead, the report skill is evaluated on:

| Criteria | Check |
|---|---|
| All 6 dimensions scored | Report includes all dimension scores |
| Composite score calculated correctly | Weighted formula applied accurately |
| Findings are evidence-based | Each finding references specific data |
| Action items are specific and actionable | Not vague — includes what, why, how |
| Budget impact estimated | Dollar amounts where calculable |
| Priorities are logical | Critical issues ranked above minor ones |
| Report is appropriate for audience | Detail level matches reader |
| Next steps defined | Clear follow-up plan with timeline |
