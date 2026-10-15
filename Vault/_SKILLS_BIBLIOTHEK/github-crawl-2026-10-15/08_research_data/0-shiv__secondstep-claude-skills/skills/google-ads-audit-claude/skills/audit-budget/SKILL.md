---
name: audit-budget
description: Analyzes budget pacing, campaigns limited by budget, impression share breakdown (lost to budget vs rank), budget-to-performance allocation efficiency, daily vs monthly analysis, shared budgets, opportunity sizing, and seasonal budget planning.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Budget Audit

## Overview

Budget allocation is where strategy meets execution. The most brilliantly structured account will underperform if budgets are misallocated — over-funding poor performers while starving top converters. This audit examines how budgets are distributed, whether campaigns are constrained or overfunded, and quantifies the opportunity cost of suboptimal allocation.

**Core budget principle:** Every dollar should flow toward the highest marginal return. A budget-limited campaign with a $20 CPA should receive funds before a campaign with a $60 CPA has its budget exhausted — assuming both drive the same type of conversion.

**The "Limited by Budget" trap:** Google's "Limited by Budget" flag is one of the most common yet misunderstood signals. It doesn't always mean "spend more" — sometimes it means the campaign needs optimization before it deserves more budget.

## Audit Checks (20 Total)

### Budget Pacing Analysis (4 checks)

**Check 1: Monthly Budget Utilization Rate**
- Pass: 85-100% of monthly budget is being utilized (slight underspend is okay; overspend > 2x daily budget signals issues)
- Fail: < 70% utilization (leaving money on table) or > 110% of planned monthly budget (overspending without client awareness)
- Scoring: 6 points
- Note: Google can spend up to 2x daily budget on any given day, but monthly spend shouldn't exceed daily budget x 30.4
- Benchmark: 90-100% utilization = optimal | 70-90% = underperforming | > 100% = over-delivery risk

**Check 2: Daily Budget Pacing Pattern**
- Pass: Spend is relatively consistent day-to-day (no extreme spikes or troughs indicating budget exhaustion)
- Fail: Campaigns exhausting daily budget by early afternoon consistently (missing evening/night traffic)
- Scoring: 4 points
- Detection: If average time of budget exhaustion is before 3 PM local time, the campaign is severely budget-constrained

**Check 3: Day-of-Week Spend Consistency**
- Pass: Spend distribution across days of week reflects business performance patterns
- Fail: Equal daily spend despite significant day-of-week conversion rate variation (e.g., spending same on Saturday as Tuesday for B2B)
- Scoring: 3 points

**Check 4: Budget vs Spend Variance Tracking**
- Pass: Monthly budget vs actual spend tracked and reported with variance explanations
- Fail: No budget tracking or reporting — actual spend unknown until month-end
- Scoring: 3 points

### Campaigns Limited by Budget (4 checks)

**Check 5: "Limited by Budget" Campaign Identification**
- Pass: All campaigns with "Limited by Budget" status identified and triaged
- Fail: Campaigns limited by budget without acknowledgment or action plan
- Scoring: 5 points
- Triage framework:
  - High CPA, limited by budget → Don't increase; optimize first
  - Low CPA, limited by budget → Increase budget (profitable headroom)
  - Brand campaign, limited by budget → Almost always increase (brand has best ROAS)

**Check 6: Budget Constraint Impact Quantification**
- Pass: For each budget-limited campaign, the estimated additional conversions from 20/50/100% budget increase is calculated
- Fail: No quantification of opportunity cost from budget constraints
- Scoring: 5 points
- Calculation: Use Google's budget simulator or: Additional conversions = (Current conversions) x (Impression Share Lost to Budget / Current Impression Share)

**Check 7: Budget-Limited Campaign Performance Quality**
- Pass: Budget-limited campaigns that are performing above target CPA/ROAS are prioritized for budget increases
- Fail: Budget-limited campaigns with poor performance — limiting budget is actually protecting the account from more waste
- Scoring: 4 points

**Check 8: Budget Headroom Analysis**
- Pass: Total account budget headroom calculated (how much more could be spent profitably across all campaigns)
- Fail: No headroom analysis — operating blindly on budget capacity
- Scoring: 3 points
- Method: Sum impression share lost to budget across all campaigns, multiply by estimated additional conversions at current CPA

### Impression Share Breakdown (3 checks)

**Check 9: Impression Share Lost to Budget Analysis**
- Pass: IS lost to budget is < 20% on priority campaigns; causes identified for high-loss campaigns
- Fail: > 40% IS lost to budget on important campaigns without action
- Scoring: 5 points
- Benchmark: Brand campaigns: < 5% IS lost to budget | Non-brand priority: < 20% | Experimental: up to 40% acceptable

**Check 10: Impression Share Lost to Rank vs Budget Ratio**
- Pass: Analysis distinguishes between IS lost to budget (solvable with money) vs IS lost to rank (needs QS/bid improvement)
- Fail: No differentiation — treating all IS loss as a budget problem
- Scoring: 4 points
- Decision matrix:
  - High IS lost to budget, low IS lost to rank → Increase budget
  - Low IS lost to budget, high IS lost to rank → Improve QS and bids
  - High both → Improve QS first, then increase budget

**Check 11: Search Impression Share Trend**
- Pass: Impression share is stable or improving for priority campaigns
- Fail: Declining impression share (indicates increasing competition or QS degradation)
- Scoring: 3 points

### Budget Allocation Efficiency (4 checks)

**Check 12: Budget-to-Performance Alignment**
- Pass: Budget allocation correlates with campaign performance — top CPA/ROAS campaigns get proportionally more budget
- Fail: Equal budgets across all campaigns regardless of performance (the "peanut butter spread" problem)
- Scoring: 7 points
- Analysis method: Rank campaigns by CPA (ascending) or ROAS (descending), then check if budget follows the same order
- Benchmark: Top 20% of campaigns by performance should receive 40-60% of total budget

**Check 13: Budget Reallocation Opportunities**
- Pass: Specific budget shift recommendations identified with projected impact (move $X from Campaign A to Campaign B for Y additional conversions)
- Fail: No reallocation analysis despite clear performance disparities
- Scoring: 5 points
- Method: Calculate marginal CPA for each campaign — shift budget from highest marginal CPA to lowest until marginal CPAs equalize

**Check 14: Brand vs Non-Brand Budget Split**
- Pass: Brand campaign budget is sufficient for 90%+ IS; not over-allocated at the expense of growth campaigns
- Fail: Excessive budget on brand (where competition is minimal) starving non-brand growth campaigns, or brand campaign budget insufficient to capture demand
- Scoring: 4 points
- Benchmark: Brand typically represents 10-25% of budget (depends on brand search volume and competition)

**Check 15: Campaign Lifecycle Budget Strategy**
- Pass: New campaigns have appropriate launch budgets (higher than maintenance to gather data quickly); mature campaigns optimized for efficiency
- Fail: New campaigns under-budgeted (can't exit learning phase) or over-budgeted (wasting spend during learning)
- Scoring: 3 points
- Benchmark: New campaign launch budget should support 30+ conversions in first 30 days to exit smart bidding learning phase

### Shared Budgets (2 checks)

**Check 16: Shared Budget Usage Assessment**
- Pass: Shared budgets used appropriately for campaigns with similar goals that benefit from flexible budget pooling
- Fail: Shared budgets grouping unrelated campaigns (e.g., brand + competitor campaigns sharing budget, causing brand to starve competitor or vice versa)
- Scoring: 4 points
- When to use shared budgets: Similar campaign types with similar CPAs and goals; when individual budgets are too granular to manage
- When NOT to use: Campaigns with very different CPAs, different goals, or requiring strict budget control

**Check 17: Shared Budget Optimization**
- Pass: Shared budget pools are monitored to ensure no single campaign dominates the shared budget
- Fail: One campaign in a shared budget consuming 80%+ of the pool, starving others
- Scoring: 3 points

### Budget Opportunity & Seasonality (3 checks)

**Check 18: Budget Opportunity Sizing**
- Pass: Total profitable budget opportunity calculated (how much more could the account spend at or below target CPA/ROAS)
- Fail: No opportunity sizing — unknown how much growth is available
- Scoring: 4 points
- Method: Sum of (IS lost to budget x estimated additional conversions at current CPA) across all campaigns performing at or below target

**Check 19: Seasonal Budget Planning**
- Pass: Budget adjustments planned for seasonal peaks/troughs based on historical data
- Fail: Flat budget year-round despite significant seasonal patterns (e.g., e-commerce not increasing budget for Q4/Black Friday)
- Scoring: 3 points
- Key seasonal considerations: Q4 holiday (e-commerce), tax season (financial), summer (travel/outdoor), back-to-school, industry-specific patterns
- CPC seasonality: CPCs typically increase 20-50% during peak seasons due to competition

**Check 20: Budget Buffer / Emergency Fund**
- Pass: Account has 10-15% budget buffer for competitive spikes, algorithm fluctuations, or opportunity capture
- Fail: Budget is 100% allocated with zero flexibility for unforeseen opportunities or competitive pressure
- Scoring: 2 points

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | Budget optimally allocated; maximum efficiency achieved |
| 75-89 | Good | Well-managed budgets with specific reallocation opportunities |
| 60-74 | Average | Functional budget management but leaving money on the table |
| 40-59 | Below Average | Significant misallocation causing missed opportunities |
| 0-39 | Poor | Budget management requires fundamental restructuring |

**Total possible points: 95** (normalized to 100-point scale)

## Benchmark Data

| Metric | Excellent | Good | Average | Poor |
|--------|-----------|------|---------|------|
| Monthly budget utilization | 95-100% | 85-95% | 70-85% | < 70% |
| IS lost to budget (brand) | < 2% | 2-5% | 5-15% | > 15% |
| IS lost to budget (non-brand) | < 10% | 10-20% | 20-40% | > 40% |
| Budget-performance correlation | > 0.8 | 0.6-0.8 | 0.3-0.6 | < 0.3 |
| Campaigns limited by budget (performing) | 0 | 1-2 | 3-5 | 5+ |
| Waste from misallocation | < 5% | 5-10% | 10-20% | > 20% |

## Output Format

```markdown
## Budget Audit Results

**Overall Score: [X]/100 — [Rating]**

### Budget Overview
| Metric | Value |
|--------|-------|
| Total Monthly Budget | $X |
| Actual Monthly Spend | $X |
| Utilization Rate | X% |
| Campaigns Limited by Budget | X |
| Est. Monthly Opportunity (profitable headroom) | $X |

### Campaign Budget Breakdown
| Campaign | Budget | Spend | CPA | IS | IS Lost Budget | IS Lost Rank | Action |
|----------|--------|-------|-----|-----|---------------|-------------|--------|
| ... | ... | ... | ... | ... | ... | ... | Increase/Decrease/Hold |

### Reallocation Recommendations
| From Campaign | To Campaign | Amount | Est. Additional Conv | Est. CPA |
|--------------|------------|--------|---------------------|----------|
| ... | ... | $X | +Y | $Z |

### Projected Impact of Recommendations
- Additional monthly conversions: +[X]
- Improved blended CPA: $[X] → $[Y]
- Additional profitable spend capacity: $[X]/month

### Seasonal Notes
- [Upcoming seasonal adjustments needed]
```
