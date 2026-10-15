# CPC Impact Methodology

## How We Calculate QS Waste

The CPC impact calculation estimates how much extra you are paying per click due to suboptimal Quality Scores. This document explains the methodology, assumptions, and limitations.

## The Formula

### Step 1: Determine CPC Multiplier

Based on empirical data from thousands of Google Ads accounts, the approximate CPC multiplier for each QS level relative to QS 7 is:

| QS | Multiplier |
|:--:|:--:|
| 1 | 5.00x |
| 2 | 4.00x |
| 3 | 3.00x |
| 4 | 2.00x |
| 5 | 1.67x |
| 6 | 1.25x |
| 7 | 1.00x (baseline) |
| 8 | 0.83x |
| 9 | 0.67x |
| 10 | 0.50x |

### Step 2: Calculate Theoretical CPC

For any keyword, the theoretical CPC at a target QS is:

```
theoretical_CPC = actual_CPC × (target_multiplier / current_multiplier)
```

**Example:** Keyword at QS 4, Avg CPC = $8.00, Target QS = 10
```
theoretical_CPC = $8.00 × (0.50 / 2.00) = $2.00
```

### Step 3: Calculate Per-Keyword Waste

```
monthly_waste = clicks × (actual_CPC - theoretical_CPC)
```

**Example:** 300 clicks/month
```
monthly_waste = 300 × ($8.00 - $2.00) = $1,800/month
```

### Step 4: Sum Across Account

```
total_waste = SUM(monthly_waste) for all keywords below target QS
```

## Two Savings Estimates

We always report two numbers:

### Theoretical Maximum (Target QS 10)
What savings would be if every keyword reached QS 10. This is aspirational and unlikely to be fully achieved.

### Realistic Savings (Tiered Targets)
Uses conservative target QS based on current level:

| Current QS | Realistic Target |
|:--:|:--:|
| 1 | 5 |
| 2 | 5 |
| 3 | 6 |
| 4 | 7 |
| 5 | 7 |
| 6 | 7 |
| 7 | 8 |
| 8 | 9 |
| 9 | 10 |

The realistic estimate is what we use for client communications and ROI projections.

## Assumptions and Limitations

1. **CPC multipliers are estimates.** The actual QS-to-CPC relationship varies by auction, keyword, industry, and time. Our multipliers are based on aggregate industry data and are directionally accurate but not exact.

2. **All else equal assumption.** The calculation assumes bid, competition, and ad rank of competitors remain constant. In reality, the auction is dynamic.

3. **Improving QS may change volume.** Better QS often increases impression share and click volume. Total spend may increase even as CPC decreases. This is generally positive (more clicks at lower CPCs).

4. **Not all QS improvements reduce CPC linearly.** The relationship has diminishing returns at higher QS levels. Moving from QS 3 to QS 5 saves more per point than moving from QS 7 to QS 9.

5. **Auction-time QS may differ.** The visible QS used in this analysis is a proxy for the real-time auction QS. They correlate but are not identical.

## Sources

- WordStream aggregate data on QS-CPC relationship
- Google Ads API documentation on Quality Score
- Adalysis research on QS component weights
- Optmyzr QS benchmark data
- Direct testing across managed accounts
