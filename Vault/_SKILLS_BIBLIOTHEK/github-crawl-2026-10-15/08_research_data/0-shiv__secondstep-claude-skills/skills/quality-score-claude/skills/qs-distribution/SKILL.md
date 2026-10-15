# QS Distribution Analysis

## Command
`/qs distribution`

## Purpose

Generate a histogram analysis of Quality Score distribution across all keywords in the account. Identify what percentage of keywords fall into each QS band, benchmark against industry standards, and highlight structural problems revealed by the distribution shape.

## QS Bands

Quality Score keywords are grouped into five bands that represent distinct performance tiers:

| Band | QS Range | Label | Meaning |
|:--:|:--:|:--|:--|
| 1 | 1-2 | **Critical** | Severe issues. These keywords are costing 3-5x what they should. Likely candidates for pause or complete restructuring. |
| 2 | 3-4 | **Poor** | Significant problems. CPC penalty of 100-200%. Fixable but requires structural changes (ad group restructuring, new landing pages). |
| 3 | 5-6 | **Average** | Below the benchmark but functional. CPC penalty of 25-67%. Incremental improvements in ad copy and landing page can push these to 7+. |
| 4 | 7 | **Good** | Baseline performance. No CPC penalty. This is the target for most keywords. |
| 5 | 8-10 | **Excellent** | Above baseline. CPC discounts of 17-50%. These are your best-performing keywords. Study what makes them work. |

## Benchmark Distribution

A healthy Google Ads account should have the following approximate distribution:

```
Benchmark QS Distribution
==========================
QS 1-2  (Critical):    < 5% of keywords
QS 3-4  (Poor):        < 10% of keywords
QS 5-6  (Average):     < 25% of keywords
QS 7    (Good):        20-30% of keywords
QS 8-10 (Excellent):   30-40% of keywords

Target: 60%+ of keywords at QS 7 or above
```

### Industry-Specific Benchmarks

Distribution benchmarks vary by industry due to inherent differences in landing page complexity, keyword competition, and user intent:

| Industry | Target % at QS 7+ | Notes |
|:--|:--:|:--|
| E-commerce | 65%+ | Product pages naturally align with keyword intent |
| SaaS / B2B | 55%+ | Longer consideration cycles can lower CTR |
| Local Services | 60%+ | High-intent keywords with geographic modifiers tend to score well |
| Legal / Insurance | 45%+ | Extremely competitive; harder to differentiate |
| Healthcare | 50%+ | Regulatory constraints limit ad copy optimization |
| Education | 55%+ | Mix of informational and enrollment intent |
| Real Estate | 50%+ | Seasonal fluctuation and broad keyword sets |

## Distribution Analysis Methodology

### Step 1: Count and Categorize

Count the number of keywords in each QS value (1 through 10) and each band. Also count keywords with null QS (new keywords without enough data).

```
Raw QS Distribution
====================
QS 1:    12 keywords (1.0%)     ████
QS 2:    28 keywords (2.2%)     ████████
QS 3:    45 keywords (3.6%)     ████████████
QS 4:    67 keywords (5.4%)     ██████████████████
QS 5:    134 keywords (10.7%)   ████████████████████████████████████
QS 6:    189 keywords (15.1%)   ██████████████████████████████████████████████████████
QS 7:    312 keywords (25.0%)   ████████████████████████████████████████████████████████████████████████████████████████
QS 8:    198 keywords (15.9%)   ████████████████████████████████████████████████████████████
QS 9:    145 keywords (11.6%)   ██████████████████████████████████████████████████
QS 10:   67 keywords (5.4%)     ██████████████████
Null:    50 keywords (4.0%)     —
```

### Step 2: Spend-Weighted Distribution

The raw count is misleading if high-spend keywords cluster at low QS. Weight by monthly spend:

```
Spend-Weighted QS Distribution
================================
QS 1-2:    $3,200/month (7.1%)    — vs 3.2% of keywords → disproportionate spend!
QS 3-4:    $5,800/month (12.9%)   — vs 9.0% of keywords → spending more on bad KWs
QS 5-6:    $9,400/month (20.9%)   — vs 25.8% of keywords
QS 7:      $11,200/month (24.9%)  — vs 25.0% of keywords → balanced
QS 8-10:   $14,200/month (31.6%)  — vs 32.9% of keywords → balanced
Null:      $1,200/month (2.7%)    — vs 4.0% of keywords
```

If the spend percentage on low-QS keywords exceeds their keyword count percentage, the account is over-investing in its worst performers.

### Step 3: Distribution Shape Analysis

The shape of the distribution reveals the account's health:

| Shape | What It Means |
|:--|:--|
| **Right-skewed (peak at 7-9)** | Healthy account. Most keywords perform well. Focus on outliers. |
| **Left-skewed (peak at 3-5)** | Structurally broken account. Needs wholesale restructuring. |
| **Bimodal (peaks at 3 and 8)** | Two distinct populations. Some campaigns are well-optimized, others are neglected. Investigate by campaign. |
| **Flat / Uniform** | No clear optimization pattern. Account is a patchwork of different quality levels. |
| **Single spike (e.g., all at 6)** | Often indicates a single systemic issue (e.g., all keywords share the same slow landing page). |

### Step 4: Segmented Distribution

Break the distribution down by:

- **Campaign** — Which campaigns have the best and worst distributions?
- **Match Type** — Do broad match keywords cluster lower than exact match?
- **Landing Page** — Do all keywords pointing to the same URL have similar QS?
- **Ad Group Size** — Do larger ad groups (20+ keywords) skew lower?
- **Keyword Age** — Do newer keywords trend differently than established ones?

### Step 5: Movement Over Time

If historical data is available, compare distributions across time periods:

```
Distribution Shift (This Month vs Last Month)
===============================================
Band          Last Month    This Month    Change
QS 1-2:      4.2%          3.2%          ▼ -1.0% (improving)
QS 3-4:      10.1%         9.0%          ▼ -1.1% (improving)
QS 5-6:      26.3%         25.8%         ▼ -0.5% (stable)
QS 7:        24.0%         25.0%         ▲ +1.0% (improving)
QS 8-10:     31.4%         32.9%         ▲ +1.5% (improving)

Net shift: Positive (+2.5% moved to 7+)
```

## Key Metrics to Report

| Metric | Description | Benchmark |
|:--|:--|:--|
| **% at QS 7+** | Primary health metric | > 60% |
| **% at QS 1-4** | Critical problem keywords | < 15% |
| **Weighted Avg QS** | Impression-weighted average across all keywords | > 6.5 |
| **Spend Concentration** | % of spend on QS < 7 keywords | < 35% |
| **Median QS** | Middle value | >= 7 |
| **QS Standard Deviation** | Spread of QS values | < 2.0 (lower = more consistent) |

## Actionable Output

The distribution analysis should conclude with:

1. **Overall Grade** — A/B/C/D/F based on the distribution profile
2. **Biggest Opportunity** — The single highest-impact change based on distribution (e.g., "Moving your 189 QS-6 keywords to QS 7 would save an estimated $2,300/month")
3. **Campaign Rankings** — Campaigns sorted by average QS, with specific callouts
4. **Quick Wins** — Keywords at QS 6 with only one Below Average component (easiest to fix)
5. **Lost Causes** — Keywords at QS 1-2 that should be evaluated for pause (unless strategically important)
