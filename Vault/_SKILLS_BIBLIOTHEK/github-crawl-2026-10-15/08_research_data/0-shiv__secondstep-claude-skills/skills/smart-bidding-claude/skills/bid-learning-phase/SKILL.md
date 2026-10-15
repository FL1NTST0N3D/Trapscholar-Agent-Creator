---
name: bid-learning-phase
description: Learning phase detector — identify campaigns stuck in learning for more than 14 days, diagnose causes of learning phase resets, provide actionable recommendations to exit learning and stabilize bid strategy performance.
allowed-tools:
  - Bash
  - Read
  - Grep
---

# Learning Phase Detection & Analysis

You are diagnosing learning phase issues across a Google Ads account. The learning phase is Smart Bidding's calibration period after significant changes. During learning, performance is typically worse (higher CPA, lower ROAS, inconsistent delivery). Campaigns stuck in perpetual learning bleed budget. Your goal is to identify stuck campaigns, diagnose reset causes, and provide concrete steps to exit learning.

## How the Learning Phase Works

When you make a significant change to a Smart Bidding campaign, the algorithm enters a "learning" period where it recalibrates its auction-time predictions. During this period:

- **Duration**: Typically 7-14 days, but can extend to 21+ days if data is sparse
- **Performance**: Expect 20-50% worse performance vs. steady state (higher CPA, lower ROAS)
- **Delivery**: May be erratic — some days overspending, others underspending
- **Status indicator**: Google Ads shows "Learning" or "Learning (new)" in the bid strategy status column
- **Cumulative cost**: A campaign spending $100/day in learning for 14 days costs $1,400 in suboptimal performance. If CPA is 30% higher during learning, that's roughly $420 in wasted spend.

**Key insight**: Each learning phase reset costs money. Frequent resets (from constant changes) create a cycle where the campaign NEVER reaches optimal performance.

## Analysis Steps

### Step 1: Identify Campaigns Currently in Learning

Scan all campaigns for learning phase status:

| Campaign | Strategy | Status | Days in Learning | Est. Learning Cost | Trigger |
|----------|----------|--------|-----------------|-------------------|---------|

**Status values:**
- **Eligible**: Campaign is running and bid strategy is optimizing normally
- **Learning**: Campaign is in active learning phase (recent change detected)
- **Learning (new)**: Campaign or strategy was recently created
- **Limited**: Campaign is limited by budget, audience, or other constraints
- **Limited (data)**: Insufficient conversion data for the bid strategy to optimize
- **Misconfigured**: Strategy configuration issue detected

### Step 2: Identify Stuck Campaigns

A campaign is "stuck in learning" if it has been in learning status for more than 14 days.

```
Days in Learning Assessment:

1-7 days:   NORMAL. Algorithm is recalibrating. Do not make changes.
            Estimated time to exit: 3-7 more days.

8-14 days:  EXTENDED but still normal. Some campaigns need longer,
            especially with lower volume. Do not intervene yet.

15-21 days: WARNING. Campaign is taking longer than expected.
            Likely insufficient conversion volume or conflicting
            signals. Investigate root cause.

22-30 days: PROBLEM. Campaign is stuck. The algorithm cannot
            converge on a bidding model. Intervention needed.

> 30 days:  CRITICAL. Campaign has been in suboptimal state for
            over a month. Significant budget waste. Requires
            immediate strategy reset or structural changes.
```

### Step 3: Diagnose Learning Phase Causes

Every learning phase has a trigger. Identify what caused each active learning phase:

**Change Type 1: Budget Changes (>20% increase or decrease)**
- Impact: Resets learning because the algorithm's bid landscape changes
- Example: Budget from $50 -> $75 (50% increase) triggers learning
- Threshold: Changes < 15-20% usually do NOT trigger full learning reset
- Best practice: Increase budget in increments of 15-20%, waiting 3-5 days between each

**Change Type 2: Target Changes (tCPA or tROAS adjustment)**
- Impact: Directly changes what the algorithm optimizes toward
- Example: tCPA from $50 -> $40 (20% decrease) triggers learning
- Threshold: Any target change typically triggers some recalibration
- Best practice: Adjust targets in 10-15% increments with 14-day waits

**Change Type 3: Conversion Action Changes**
- Impact: Most disruptive change. The algorithm's entire prediction model is invalidated.
- Examples:
  - Adding a new conversion action to "account default conversions"
  - Removing a conversion action
  - Changing conversion counting (one vs every)
  - Changing conversion window (e.g., 30-day to 90-day)
  - Switching attribution model (last-click to DDA)
- Best practice: Make conversion action changes during a low-traffic period. Expect 2-3 weeks of learning.

**Change Type 4: Bid Strategy Change**
- Impact: Full reset — switching from Max Conv to tCPA, or tCPA to tROAS
- The new strategy starts with minimal historical data
- Best practice: Switch strategies no more than once per quarter per campaign

**Change Type 5: Major Ad Changes**
- Impact: Moderate — changing more than 50% of ads in a campaign
- Examples: Pausing all RSAs and adding new ones, changing all headlines
- Smaller ad changes (editing 1-2 ads) typically don't trigger full learning
- Best practice: Rotate ad changes gradually, not all at once

**Change Type 6: Audience Changes**
- Impact: Moderate to significant depending on scope
- Examples: Adding/removing observation audiences, changing audience expansion settings
- Targeting-mode audience changes (added as targeting, not observation) have bigger impact

**Change Type 7: Keyword Changes (Major)**
- Impact: Moderate — adding/removing a large number of keywords
- Adding 1-2 keywords: minimal impact
- Adding/removing 50%+ of keywords: may trigger learning
- Match type changes at scale: can trigger learning

**Change Type 8: Composition Changes**
- Impact: Varies — campaign structural changes
- Examples: Pausing/enabling ad groups, adding new ad groups, changing geo targeting significantly

### Step 4: Learning Phase Cost Estimation

Calculate the financial impact of each learning phase:

```python
# Estimate learning phase cost
normal_cpa = actual_cpa_before_learning  # or 30d avg before change
learning_cpa = actual_cpa_during_learning
daily_spend = average_daily_spend_during_learning
days_in_learning = current_days_in_learning

learning_cost_premium = (learning_cpa - normal_cpa) / normal_cpa
total_spend_during_learning = daily_spend * days_in_learning
wasted_spend = total_spend_during_learning * learning_cost_premium

# Example:
# Normal CPA: $50, Learning CPA: $65, Daily spend: $100, 14 days
# Premium: ($65-$50)/$50 = 30%
# Total spend: $100 * 14 = $1,400
# Wasted: $1,400 * 0.30 = $420 in avoidable excess cost
```

### Step 5: Learning Phase Exit Recommendations

For each stuck campaign, provide a specific exit plan:

**Option A: Wait It Out (if close to exit)**
- Only if the campaign is in days 10-16 and showing improvement trends
- Absolutely NO changes during this period
- Set a calendar reminder to check status in 5 days

**Option B: Increase Volume (most common fix)**
- Broaden match types (exact -> phrase -> broad)
- Increase budget by 15-20% to feed more data to the algorithm
- Temporarily add micro-conversions as secondary conversion actions
- Expand geographic targeting if reasonable
- Extend ad schedule to serve during more hours

**Option C: Simplify the Strategy**
- If using tCPA with insufficient volume -> switch to Max Conversions
- Let Max Conversions gather data, then re-attempt tCPA later
- This resets learning but gives the algorithm a simpler objective

**Option D: Restructure the Campaign**
- Consolidate multiple low-volume campaigns into fewer campaigns
- Combine ad groups that compete against each other
- Move from campaign-level bidding to portfolio bidding (to pool volume)

**Option E: Reset and Restart (last resort)**
- Pause the campaign, wait 24 hours
- Switch to Max Conversions with adequate budget
- Run for 30 days to build conversion history
- Then switch back to tCPA/tROAS with data-informed target

### Step 6: Learning Phase Prevention Plan

Provide a change management protocol:

**Change Scheduling Rules:**
1. Only one significant change per campaign every 14 days
2. Sequence changes: budget first (wait 14d) -> target (wait 14d) -> creative
3. Never change conversion actions and bid strategy in the same period
4. Make changes on Monday (to maximize weekday data collection)
5. Avoid changes during seasonal peaks or promotional periods
6. Document every change with date and expected learning exit date

**Change Impact Classification:**
```
LOW IMPACT (rarely triggers learning):
- Adding 1-3 keywords
- Editing a single ad
- Budget change < 15%
- Adding observation audiences
- Adjusting ad extensions

MEDIUM IMPACT (may trigger partial learning):
- Budget change 15-30%
- Target CPA/ROAS adjustment < 15%
- Adding/pausing 1 ad group
- Adding 10+ keywords
- Geographic targeting change

HIGH IMPACT (will trigger full learning):
- Budget change > 30%
- Target CPA/ROAS adjustment > 20%
- Bid strategy change
- Conversion action change
- Major ad overhaul (50%+ of ads)
- Campaign structure change
```

## Output Format

```
## Learning Phase Analysis

### Current Status
- Campaigns in learning: X / Y total
- Campaigns stuck (>14 days): X
- Estimated wasted spend from learning phases: $X

### Stuck Campaign Details
[Per-campaign diagnosis with trigger, duration, and exit plan]

### Recent Learning Resets (Last 60 Days)
[Timeline of learning phase entries with triggers]

### Change Management Protocol
[Recommended change scheduling and sequencing]

### Prevention Recommendations
1. [Changes to batch together]
2. [Changes to delay]
3. [Structural changes to prevent future stuck-learning scenarios]
```
