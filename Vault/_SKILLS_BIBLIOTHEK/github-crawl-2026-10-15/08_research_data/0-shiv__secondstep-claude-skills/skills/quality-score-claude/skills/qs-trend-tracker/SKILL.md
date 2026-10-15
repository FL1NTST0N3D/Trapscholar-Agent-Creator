# QS Trend Tracker

## Command
`/qs trends`

## Purpose

Track Quality Score changes over time, identify declining keywords before they become expensive problems, detect seasonal QS patterns, and alert on sudden QS drops that indicate landing page issues, competitive shifts, or account structure degradation.

## Why Trends Matter

A keyword's Quality Score today is a snapshot. The trend tells you whether things are getting better or worse. A keyword at QS 6 that was QS 8 last month is a very different situation than a keyword at QS 6 that was QS 4 last month.

Google updates visible QS periodically, and the timing is not consistent. Some keywords update weekly, others may hold the same QS for months. Tracking trends across multiple snapshots reveals the real trajectory.

## Data Collection Strategy

### Snapshot Approach
Quality Score is a point-in-time metric. Google Ads does not store historical QS data by default. To track trends, you need periodic snapshots:

1. **Weekly QS Export** — Download keyword report with QS columns every Monday
2. **Google Ads Scripts** — Automate daily QS capture to Google Sheets
3. **Third-Party Tools** — Use tools like Optmyzr, Adalysis, or custom scripts to log QS daily
4. **Manual Tracking** — At minimum, export monthly and store in a consistent format

### Required Data Points Per Snapshot
- Date of snapshot
- Keyword ID (for reliable matching across exports)
- Keyword text
- Quality Score (1-10)
- Expected CTR status
- Ad Relevance status
- Landing Page Experience status
- Campaign name
- Ad Group name
- Impressions (for weighting)
- Clicks
- Avg CPC
- Cost

## Trend Analysis Methodology

### 1. QS Movement Classification

For each keyword, classify its QS trajectory over the analysis period:

| Classification | Definition | Action |
|:--|:--|:--|
| **Improving** | QS increased by 1+ points in last 30 days | Monitor, reinforce what is working |
| **Stable** | QS unchanged for 30+ days | Acceptable if QS >= 7; investigate if below |
| **Declining** | QS decreased by 1+ points in last 30 days | Investigate immediately |
| **Volatile** | QS changed direction 2+ times in 60 days | Unstable; review component fluctuations |
| **New** | Keyword added in last 14 days | Too early to trend; flag for review at day 30 |
| **Null-to-Score** | QS went from null to a number | First QS assignment; set baseline |

### 2. Decline Root Cause Detection

When a keyword's QS drops, check which component changed:

- **Expected CTR dropped** — Something changed in ad performance. Check: new competitor ads? Ad fatigue? Changed match types? Seasonal CTR shift?
- **Ad Relevance dropped** — Ad copy or ad group structure changed. Check: recent ad edits? New keywords added to the ad group? Paused ads that were the best performers?
- **Landing Page dropped** — Landing page changed or degraded. Check: site redesign? Speed regression? Content changes? SSL certificate expired? Mobile rendering broken?

### 3. Seasonal Pattern Detection

Some keywords have natural QS cycles tied to seasonality:

- **Seasonal demand keywords** — "tax preparation," "snow removal," "pool cleaning" may see QS fluctuate with search volume. Lower volume periods often lead to QS instability because Google has less data.
- **Competitive cycle keywords** — Keywords in industries with seasonal competition (e.g., retail during Black Friday) may see QS drop when more competitors enter the auction.
- **Budget-constrained keywords** — If budget limits cause your ads to stop showing during peak hours, you may lose high-CTR impressions, which can lower Expected CTR.

### 4. Cohort Analysis

Group keywords by:
- **QS at creation** — What QS did keywords start with? Track how they evolve over 30/60/90 days.
- **Campaign** — Are certain campaigns systematically declining?
- **Landing page** — Do all keywords pointing to a specific URL show the same trend?
- **Ad group** — Are newly restructured ad groups showing improving trends?
- **Match type** — Do broad match keywords trend differently than exact match?

## Alert Thresholds

Define alert levels for automated monitoring:

| Alert Level | Trigger | Response |
|:--|:--|:--|
| **Critical** | QS dropped 3+ points on a keyword spending > $500/month | Immediate investigation. Check landing page, ad changes, competitor activity. |
| **Warning** | QS dropped 2 points on any keyword with > 100 impressions/week | Review within 48 hours. Identify component change. |
| **Watch** | QS dropped 1 point on any keyword | Add to weekly review list. May be normal fluctuation. |
| **Positive** | QS increased 2+ points | Document what changed. Replicate the improvement pattern to similar keywords. |

## Trend Reporting Output

### Summary View
```
QS Trend Summary (Last 30 Days)
================================
Keywords analyzed:         1,247
Improving (QS up):         142 (11.4%)
Stable:                    891 (71.4%)
Declining (QS down):       187 (15.0%)
Volatile:                   27 (2.2%)

Net QS movement:           -0.3 (account weighted average)
Spend on declining KWs:    $8,450/month
Estimated waste increase:   $1,900/month if declines continue
```

### Decline Details Table
```
Top Declining Keywords (by spend impact)
=========================================
Keyword              | QS Then | QS Now | Change | Component Changed    | Monthly Spend
"emergency plumber"  |    7    |    4   |  -3    | Landing Page (↓)     | $2,400
"plumber near me"    |    8    |    6   |  -2    | Expected CTR (↓)     | $1,800
"drain cleaning"     |    6    |    5   |  -1    | Ad Relevance (↓)     | $950
```

### Improvement Opportunities
```
Keywords Closest to QS Threshold
=================================
These keywords are at QS 6 with improving trends — one more point puts them at the 7+ benchmark:

Keyword              | QS Now | Trend  | Weakest Component     | Fix Complexity
"water heater"       |    6   | ↑ +1   | Landing Page (Avg)    | Medium
"pipe repair"        |    6   | Stable | Ad Relevance (Avg)    | Low
```

## Actionable Recommendations from Trends

1. **Declining QS + Same Landing Page** — "12 keywords pointing to /services saw QS drop in the last 30 days. All show Landing Page Experience decline. Check page speed and recent changes to /services."

2. **Declining QS + Recent Ad Changes** — "8 keywords in the [Brand] campaign saw Ad Relevance drop after ad copy was updated on March 1. Review new ads against keyword list."

3. **Seasonal QS Drop** — "Keywords in the [Snow Removal] campaign historically drop 1-2 QS points in March-April as search volume decreases. This is expected. Plan to refresh ads for next season in October."

4. **New Keywords Stabilizing Low** — "35 keywords added 45 days ago have stabilized at QS 4-5. They need immediate attention: tighter ad groups, dedicated landing pages, and keyword-specific ad copy."

## Scripts Integration

For automated tracking, reference `scripts/qs_analyzer.py` which can:
- Parse multiple QS export CSV files
- Calculate period-over-period changes
- Identify declining keywords
- Generate trend reports
