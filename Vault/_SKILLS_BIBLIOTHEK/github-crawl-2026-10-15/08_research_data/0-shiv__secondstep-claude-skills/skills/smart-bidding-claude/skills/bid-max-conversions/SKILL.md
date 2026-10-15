---
name: bid-max-conversions
description: Analysis of Max Conversions and Max Conversion Value campaigns — budget utilization efficiency, CPA trend tracking, overspending detection, and graduation criteria to determine when campaigns should transition to tCPA or tROAS.
allowed-tools:
  - Bash
  - Read
  - Grep
---

# Max Conversions / Max Conversion Value Analysis

You are analyzing campaigns using Max Conversions or Max Conversion Value bidding strategies. These "uncapped" strategies aggressively spend the full daily budget to maximize conversion volume or revenue. While powerful for data gathering and budget utilization, they have no efficiency guardrails. Your job is to identify whether these campaigns are spending wisely, track CPA/ROAS trends, detect overspending, and determine which campaigns are ready to graduate to target-based strategies.

## Understanding Max Conversions vs Max Conversion Value

**Max Conversions:**
- Optimizes for the highest number of conversions within your daily budget
- Treats all conversions equally regardless of value
- Will spend the full budget every day (or close to it)
- No CPA cap — individual conversion costs can vary wildly
- Best for: new campaigns, fixed budgets, volume-priority goals

**Max Conversion Value:**
- Optimizes for the highest total conversion value within your daily budget
- Weights bids toward higher-value conversions
- Also spends the full budget aggressively
- No ROAS floor — will accept low-ROAS conversions if they add total value
- Best for: e-commerce with varied product values, revenue-priority goals

## Analysis Steps

### Step 1: Budget Utilization Analysis

Max Conversions/Value should spend close to 100% of daily budget. If not, there's a problem.

```
Spend Rate = Actual Daily Spend / Daily Budget (avg last 14 days)

95-105%: NORMAL. Budget is fully utilized. Google may overshoot by up
         to 2x on individual days (averaged over the month).

80-95%:  WARNING. Underspending. Possible causes:
         - Budget recently increased (algorithm needs time to scale)
         - Keyword targeting too narrow (not enough eligible auctions)
         - Ad schedule restrictions limiting serving hours
         - Low Quality Scores reducing auction eligibility
         - Geographic targeting too restrictive

50-80%:  PROBLEM. Significant underspending. The algorithm can't find
         enough auctions to spend the budget. Investigate:
         - Are keywords paused or disapproved?
         - Is the campaign eligible to serve? (ad disapprovals, policy issues)
         - Is the audience too small?

< 50%:   CRITICAL. Campaign is barely spending. Either there's a
         technical issue or the targeting is far too restrictive for
         the budget.

> 120%:  NOTE. Google can spend up to 2x daily budget on a given day,
         but monthly spend won't exceed 30.4x daily budget. If the
         average spend consistently exceeds budget, Google's
         overdelivery may be aggressive. Not necessarily a problem
         but worth monitoring.
```

### Step 2: CPA Trend Analysis (Max Conversions)

Track CPA week-over-week to identify trends:

```
Week-over-Week CPA Change:
- Calculate CPA for each of the last 8 weeks
- Plot the trend: rising, falling, or stable?

RISING CPA TREND:
  Possible causes:
  - Audience saturation (showing ads to the same people)
  - Increased competition (auction prices rising)
  - Quality Score decline (paying more per click)
  - Conversion rate decline (landing page issues, seasonal)
  - Algorithm finding diminishing returns as it exhausts
    high-probability audiences
  Action: Consider adding tCPA cap, refreshing creative,
  expanding audience, or improving landing page.

FALLING CPA TREND:
  Algorithm is learning and optimizing. Great sign.
  If CPA stabilizes for 2+ weeks, ready for tCPA graduation.

STABLE CPA:
  Algorithm has found equilibrium. This is the actual CPA
  for this campaign/audience/offer combination.
  Graduation criteria met if stable for 2+ weeks.

ERRATIC CPA (high variance week to week):
  Algorithm hasn't found a pattern, or external factors
  are disrupting performance. Not ready for tCPA.
  Investigate root causes before changing strategy.
```

### Step 3: Overspending Detection

Max Conversions has no CPA guardrail. Detect wasteful spending:

**Individual Conversion Cost Analysis:**
- What is the most expensive single conversion in the last 30 days?
- What percentage of conversions cost more than 2x the average CPA?
- Are there specific days/times when CPA spikes dramatically?

```
Overspending Indicators:
1. Top 10% of conversions cost more than 3x the average CPA
   → Algorithm is occasionally overbidding on uncertain auctions

2. Weekend CPA is 50%+ higher than weekday CPA
   → Consider ad schedule adjustments or campaign-level day parting

3. Mobile CPA is 2x+ desktop CPA (or vice versa)
   → Consider device bid adjustment (-100% to exclude worst device)

4. Specific keywords drive CPA 3x+ higher than campaign average
   → These keywords may not be conversion-worthy. Pause or move to
     a separate campaign with different treatment.

5. Daily CPA varies by more than 100% day to day
   → Increase budget to give algorithm more room, or add a tCPA
     cap to limit overspending.
```

### Step 4: ROAS Trend Analysis (Max Conversion Value)

For Max Conversion Value campaigns, track ROAS trends:

```
Week-over-Week ROAS:
- Calculate ROAS (conv value / cost) for each of last 8 weeks
- Is ROAS improving, declining, or stable?

IMPROVING ROAS: Algorithm learning value patterns. Good sign.
DECLINING ROAS: Algorithm may be overbidding or audience is saturated.
STABLE ROAS: Ready for tROAS graduation if stable 2+ weeks.
ERRATIC ROAS: Need more data or external factors disrupting.
```

**AOV (Average Order Value) Tracking:**
- Is AOV stable or changing?
- If AOV is dropping while volume increases, the algorithm may be
  prioritizing cheap, easy conversions over valuable ones
- If AOV is rising, algorithm is successfully identifying high-value users

### Step 5: Graduation Assessment

Determine which campaigns are ready to move from uncapped to target-based bidding:

**Max Conversions -> tCPA Graduation Criteria:**

| Criterion | Threshold | Status |
|-----------|-----------|--------|
| Conversions (30d) | >= 30 | |
| CPA stability (2-week variance) | < 20% | |
| CPA trend | Stable or falling | |
| Budget utilization | > 90% | |
| Campaign age | > 4 weeks | |
| No major changes in last 14d | No keyword/ad/budget changes | |

**If all criteria met:**
1. Set tCPA target = actual CPA from last 30 days (do NOT set it lower)
2. Monitor for 14 days (learning phase)
3. After learning: evaluate and begin ratcheting if appropriate

**If criteria NOT met:**
- List which criteria failed and why
- Provide specific actions to reach graduation readiness
- Estimated timeline to graduation

**Max Conversion Value -> tROAS Graduation Criteria:**

| Criterion | Threshold | Status |
|-----------|-----------|--------|
| Conversions with value (30d) | >= 50 | |
| ROAS stability (2-week variance) | < 25% | |
| ROAS trend | Stable or improving | |
| Revenue tracking validated | < 15% discrepancy vs backend | |
| AOV stability | < 30% variance | |
| Budget utilization | > 90% | |
| Campaign age | > 6 weeks | |

**If all criteria met:**
1. Set tROAS target = actual ROAS from last 30 days
2. Monitor for 14 days
3. Begin ratcheting after learning phase completes

### Step 6: When to Stay on Max Conversions

Not every campaign should graduate. Stay on Max Conversions if:

- Budget is fixed and must be fully spent regardless of CPA
- Campaign is used for brand awareness with conversion as a secondary metric
- Conversion volume is seasonally volatile (tCPA would constantly reset learning)
- The campaign serves as a "catch-all" for broad traffic
- Business stakeholders prioritize volume over efficiency

However, even in these cases, consider adding a "Max CPA" limit through tCPA with a very generous target (150% of actual CPA) to prevent extreme outlier costs.

## Output Format

```
## Max Conversions / Max Conv Value Analysis

### Budget Utilization
[Per-campaign spend rate assessment]

### CPA/ROAS Trends
[8-week trend charts per campaign]

### Overspending Detection
[Flagged campaigns with wasteful spending patterns]

### Graduation Assessment
[Per-campaign readiness checklist]

### Recommendations
1. [Campaigns ready to graduate — with target suggestions]
2. [Campaigns needing more data — timeline to graduation]
3. [Campaigns that should stay on Max Conv — with guardrail suggestions]
4. [Overspending fixes needed]
```
