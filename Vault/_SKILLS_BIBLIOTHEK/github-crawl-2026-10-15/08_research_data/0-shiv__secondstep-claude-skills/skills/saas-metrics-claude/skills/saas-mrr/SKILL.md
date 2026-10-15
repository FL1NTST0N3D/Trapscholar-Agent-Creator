# SaaS MRR Calculator

> Calculate Monthly Recurring Revenue with full movement decomposition, ARR projection, and growth rate tracking.

## Trigger
`/saas mrr`

## What This Skill Does

MRR (Monthly Recurring Revenue) is the single most important metric for any subscription business. This skill calculates MRR with complete movement decomposition, showing you exactly where your revenue is coming from and where it is leaking. It does not just give you a number — it gives you a waterfall that tells the full story of your revenue dynamics.

## Core Calculations

### MRR Components
MRR is not a single number. It is the sum of four movements that tell you the health of your business:

- **New MRR**: Revenue from customers acquired this month. This is the output of your sales and marketing engine. If New MRR is declining month-over-month, your growth engine is stalling regardless of what total MRR says.
- **Expansion MRR**: Additional revenue from existing customers — upgrades, add-ons, seat expansions, usage overages. This is the purest signal of product-market fit. Healthy SaaS companies generate 20-40% of gross new MRR from expansion.
- **Churned MRR**: Revenue lost from customers who cancelled entirely. Track this as a positive number that gets subtracted. If churned MRR exceeds new MRR, you are in a death spiral.
- **Contraction MRR**: Revenue lost from customers who downgraded but did not leave. Often overlooked, but contraction is an early warning signal — these customers are on the path to churning.

### The MRR Waterfall Formula
```
End MRR = Start MRR + New MRR + Expansion MRR - Churned MRR - Contraction MRR
```

This is the MRR movements waterfall. Every SaaS board deck should include this chart. It shows whether you are growing because of new business or because existing customers are expanding — and these have very different implications for capital efficiency.

### ARR (Annual Recurring Revenue)
```
ARR = MRR x 12
```

ARR is simply MRR annualized. Use ARR for fundraising conversations, valuation multiples, and annual planning. Use MRR for operational decisions. Never mix them — pick one unit and stick with it within a given analysis.

### MRR Growth Rate
```
MRR Growth Rate = (End MRR - Start MRR) / Start MRR x 100
```

Month-over-month MRR growth is the heartbeat metric. Benchmarks by stage:
- **Pre-seed / Seed**: 15-20% MoM (the "triple triple double double" path)
- **Series A**: 10-15% MoM
- **Series B**: 7-10% MoM
- **Growth / Scale**: 3-5% MoM

### Committed MRR (CMRR)
```
CMRR = Active MRR + Signed-not-yet-live MRR - Known upcoming churns
```

CMRR is forward-looking MRR. It accounts for contracts signed but not yet onboarded, and customers who have given notice but have not yet churned. CMRR is more accurate than MRR for forecasting because it includes leading indicators.

## How To Use

Provide your data in any of these formats:

1. **Monthly totals**: "We had $50K MRR last month, added $8K new, $3K expansion, lost $2K to churn and $500 to downgrades"
2. **Customer-level data**: CSV or JSON with customer_id, plan, mrr, start_date, and optionally end_date or plan_changes
3. **Multi-month series**: Monthly MRR figures for trend analysis

## Output Format

The skill produces:
- MRR movements waterfall (table format)
- ARR calculation
- MoM growth rate with trend
- Net New MRR (New + Expansion - Churned - Contraction)
- Quick Ratio = (New MRR + Expansion MRR) / (Churned MRR + Contraction MRR)
- Commentary on what the numbers mean

### Quick Ratio Benchmarks
The SaaS Quick Ratio tells you how efficient your growth is:
- **>4.0**: Excellent — you are adding revenue much faster than losing it
- **2.0-4.0**: Healthy — sustainable growth
- **1.0-2.0**: Concerning — growth is being eaten by churn
- **<1.0**: Shrinking — you are losing more than you are adding

## Example

Input: "January MRR: $100K. New: $15K. Expansion: $5K. Churned: $8K. Contraction: $2K."

Output:
```
MRR Waterfall — January
========================
Starting MRR:      $100,000
+ New MRR:         + $15,000
+ Expansion MRR:   +  $5,000
- Churned MRR:     -  $8,000
- Contraction MRR: -  $2,000
========================
Ending MRR:        $110,000
Net New MRR:       + $10,000
MoM Growth:        +10.0%
ARR:               $1,320,000
Quick Ratio:       2.0 (Healthy)
```

## Related Skills
- `/saas churn` — Deep dive into the churn component
- `/saas nrr` — Net Revenue Retention (related to expansion vs churn)
- `/saas forecast` — Use MRR trends for revenue forecasting
