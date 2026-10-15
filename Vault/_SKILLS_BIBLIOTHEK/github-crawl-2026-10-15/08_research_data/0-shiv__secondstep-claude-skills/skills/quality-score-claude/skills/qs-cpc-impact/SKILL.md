# QS CPC Impact Calculator

## Command
`/qs impact`

## Purpose

Calculate the exact dollar amount your account wastes every month due to suboptimal Quality Scores. This is not an abstract metric — this is real money leaving your budget that could be saved or reallocated to profitable keywords.

## The Core Formula

Google's CPC discount/penalty relative to a QS 7 baseline follows an approximate curve. The multiplier for any Quality Score can be estimated as:

```
CPC_multiplier = 1 + (7 - QS) × 0.167    (simplified linear approximation)
```

More accurately, the empirical CPC adjustments are:

| QS | CPC Multiplier | CPC Adjustment vs QS 7 |
|:--:|:--------------:|:----------------------:|
| 10 | 0.50x | -50% |
| 9  | 0.67x | -33% |
| 8  | 0.83x | -17% |
| 7  | 1.00x | Baseline (0%) |
| 6  | 1.25x | +25% |
| 5  | 1.67x | +67% |
| 4  | 2.00x | +100% |
| 3  | 3.00x | +200% |
| 2  | 4.00x | +300% |
| 1  | 5.00x | +400% |

## Waste Calculation Methodology

### Per-Keyword Waste

For each keyword with QS below 10, calculate the theoretical CPC at QS 10 and compare it to the actual CPC:

```
theoretical_CPC_at_QS10 = actual_CPC × (multiplier_at_current_QS / multiplier_at_QS10)
                        = actual_CPC × (multiplier_at_current_QS / 0.50)

Wait — we need to reverse this. If QS 7 = baseline:

theoretical_CPC_at_QS10 = actual_CPC × (0.50 / multiplier_at_current_QS)

per_keyword_waste = clicks × (actual_CPC - theoretical_CPC_at_QS10)
```

**Example:**
- Keyword: "plumber near me"
- Current QS: 4
- Actual CPC: $8.50
- Clicks: 320/month
- Multiplier at QS 4: 2.00x
- Multiplier at QS 10: 0.50x
- Theoretical CPC at QS 10: $8.50 × (0.50 / 2.00) = $2.125
- Monthly waste: 320 × ($8.50 - $2.125) = **$2,040/month**

### Account-Level Waste

Sum per-keyword waste across all keywords:

```
total_monthly_waste = SUM(per_keyword_waste) for all keywords where QS < 10
```

### Realistic vs Theoretical Savings

Not every keyword can reach QS 10. A more realistic analysis uses tiered targets:

| Current QS | Realistic Target | Notes |
|:--:|:--:|:--|
| 1-2 | 5-6 | Significant structural issues; achieving 5-6 is a realistic first milestone |
| 3-4 | 6-7 | Fixable with ad group restructuring and landing page improvements |
| 5-6 | 7-8 | Incremental improvements in ad copy and landing page speed |
| 7 | 8-9 | Fine-tuning: better extensions, tighter ad groups |
| 8-9 | 9-10 | Diminishing returns; focus elsewhere unless high spend |

Calculate both:
1. **Maximum theoretical savings** — if every keyword reached QS 10
2. **Realistic savings** — if keywords hit their realistic target tier
3. **90-day achievable savings** — what can be fixed in the next quarter

## Analysis Tiers

### Tier 1: High-Impact Keywords (top 20% by spend)
These keywords consume the most budget. Even small QS improvements yield significant savings. Calculate impact per QS point gained.

### Tier 2: Medium-Impact Keywords (next 30% by spend)
These are the long tail of meaningful spend. Group by ad group and landing page to find batch fixes.

### Tier 3: Low-Impact Keywords (bottom 50% by spend)
Individual optimization is not worth the time. Look for systemic fixes (e.g., one landing page improvement that lifts QS for 200 keywords at once).

## Output Metrics

For each keyword analyzed, report:

| Metric | Description |
|--------|-------------|
| Keyword | The keyword text |
| Current QS | Current Quality Score (1-10) |
| Actual CPC | Current average CPC |
| Monthly Clicks | Clicks in the analysis period |
| Monthly Cost | Total spend in the analysis period |
| Theoretical CPC (QS 10) | What CPC would be at QS 10 |
| Realistic CPC (target QS) | What CPC would be at realistic target |
| Monthly Waste (theoretical) | Excess spend vs QS 10 |
| Monthly Waste (realistic) | Excess spend vs realistic target |
| Weakest Component | Which QS component is Below Average |

## Summary Table

Always present a summary:

```
QS CPC Impact Summary
=====================
Total monthly spend analyzed:          $45,000
Keywords analyzed:                     1,247
Keywords with QS below 7:             487 (39%)

Maximum theoretical savings (QS 10):   $12,450/month ($149,400/year)
Realistic savings (target tier):       $7,200/month ($86,400/year)
90-day achievable savings:             $4,800/month ($57,600/year)

Top 5 Keywords by Waste:
1. "emergency plumber" — QS 3 — $2,040/mo waste
2. "plumbing services" — QS 4 — $1,780/mo waste
3. "drain cleaning"   — QS 5 — $890/mo waste
4. "water heater repair" — QS 4 — $750/mo waste
5. "pipe repair near me" — QS 3 — $620/mo waste
```

## Visualization

When possible, generate or describe:
- **Waste waterfall chart** — Keywords sorted by waste amount, showing cumulative savings
- **QS vs CPC scatter plot** — Showing the CPC penalty curve with each keyword plotted
- **Spend allocation by QS band** — How much budget goes to QS 1-4 vs 5-6 vs 7+ keywords

## Context and Caveats

Always include these caveats in the analysis:

1. **CPC adjustments are approximate.** The exact relationship between QS and CPC varies by auction, competition level, and ad format. The multipliers used are industry-standard estimates based on aggregate data.

2. **Improving QS does not guarantee CPC reduction.** If competitors also improve, relative position may not change. However, QS improvement always improves ad rank efficiency.

3. **Some keywords have structural CPC floors.** Highly competitive keywords in regulated industries (legal, insurance, finance) may have CPCs that remain high even at QS 10 due to auction dynamics.

4. **Volume may change.** Improving QS often increases impression share and click volume, which can increase total spend even as CPC decreases. This is generally positive (more clicks at lower cost per click) but total budget may need adjustment.

5. **Time to impact.** QS changes are not instant. Budget for 2-4 weeks before visible QS updates, and 4-8 weeks before CPC impact is measurable in the data.
