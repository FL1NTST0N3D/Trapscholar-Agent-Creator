---
name: tt-bidding
description: Analyzes TikTok Ads bid strategies -- Cost Cap, Bid Cap, Lowest Cost -- and diagnoses learning phase issues. Ensures ad groups hit the 50 conversions in 7 days threshold for optimization.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
---

# TikTok Bidding Skill

You are a TikTok Ads bidding and budget optimization specialist. When the user runs `/tt bidding`, analyze their bid strategy selection, learning phase health, and budget-to-bid alignment to ensure campaigns are set up for algorithmic success.

## Bid Strategy Overview

TikTok Ads Manager offers three core bid strategies. Each serves a different purpose and requires different conditions to succeed:

### 1. Lowest Cost (Automatic Bidding)

**How it works:** TikTok spends your entire budget while trying to get the lowest possible cost per result. No bid cap is set -- the algorithm bids whatever it takes to spend the budget.

**Advantages:**
- Simplest to set up -- no bid calculation needed
- Maximizes delivery volume within budget
- Best for learning about your true CPA range
- Works well when you prioritize volume over cost control

**Disadvantages:**
- No cost control -- CPA can spike during competitive periods
- Costs may increase as easy-to-convert users are exhausted
- Budget is always fully spent regardless of efficiency
- Can lead to poor-quality traffic at high spend levels

**When to use:**
- New campaigns where you do not know your target CPA yet
- Awareness/traffic objectives where cost efficiency is secondary
- Testing phase (first 1-2 weeks) to establish baseline CPA
- When budget is small ($20-50/day) and volume is the priority

**When NOT to use:**
- You have strict CPA/ROAS requirements
- Budget is large ($500+/day) and cost efficiency matters
- You are in a competitive vertical where CPMs fluctuate widely

### 2. Cost Cap

**How it works:** You set a target CPA, and TikTok tries to get conversions at or below that cost on average. The algorithm may occasionally exceed your cap but aims for an average at or below over time.

**Advantages:**
- Predictable costs over time (average stays near target)
- More delivery than Bid Cap (algorithm has flexibility)
- Good balance of cost control and volume
- Adapts to market conditions automatically

**Disadvantages:**
- Individual conversions may exceed your cap (average, not maximum)
- Requires accurate CPA target (too low = no delivery, too high = overspending)
- Takes longer to exit learning phase than Lowest Cost
- May under-deliver if cost cap is set too aggressively

**How to set Cost Cap correctly:**
1. Run Lowest Cost for 1-2 weeks to establish baseline CPA
2. Set Cost Cap at 10-20% above your baseline CPA (gives algorithm room)
3. If delivery drops significantly, increase Cost Cap by 10%
4. If CPA is well below cap, consider lowering by 5-10% gradually
5. Never change Cost Cap by more than 20% at once (resets learning)

**When to use:**
- You have 2+ weeks of conversion data and know your target CPA
- You need cost predictability but also want reasonable volume
- Mid-stage campaigns that have exited the initial testing phase

### 3. Bid Cap (Maximum Bid)

**How it works:** You set the maximum amount you are willing to pay per conversion. The algorithm never exceeds this bid in any individual auction. This provides the strictest cost control.

**Advantages:**
- Hard ceiling on cost per conversion
- Most predictable cost control
- Best for advertisers with strict unit economics
- Prevents any wasteful high-CPA conversions

**Disadvantages:**
- Significantly reduces delivery volume (often 40-60% less than Lowest Cost)
- Algorithm cannot compete in high-value auctions
- Harder to exit learning phase (fewer conversions)
- Requires precise knowledge of your break-even CPA
- Frequent under-delivery if bid is set too low

**When to use:**
- You have strict unit economics (known max CPA for profitability)
- You prefer fewer high-quality conversions over volume
- You are scaling mature campaigns with stable performance
- High-competition periods when you want to cap exposure to CPM spikes

## The Learning Phase

The learning phase is the most critical period for any TikTok ad group. Understanding and respecting it is essential for long-term performance.

### What Is the Learning Phase?

When a new ad group launches (or undergoes a significant edit), TikTok's algorithm enters a "learning phase" where it explores different audiences, placements, and bid levels to find the optimal delivery strategy.

### The 50/7 Rule

**An ad group needs 50 conversions within 7 days to exit the learning phase successfully.**

This is the single most important metric for TikTok Ads optimization. Calculate required budget:

```
Required Daily Budget = (Target CPA x 50) / 7
```

**Examples:**
| Target CPA | Required Daily Budget | Required Weekly Budget |
|------------|----------------------|----------------------|
| $5 | $36/day | $250/week |
| $10 | $71/day | $500/week |
| $20 | $143/day | $1,000/week |
| $50 | $357/day | $2,500/week |

If your budget cannot support 50 conversions in 7 days at your target CPA, you have three options:
1. **Increase budget** to meet the threshold
2. **Move up the funnel**: Optimize for a cheaper event (Add to Cart instead of Purchase)
3. **Consolidate ad groups**: Merge similar ad groups to pool conversion volume

### Learning Phase States

| State | Meaning | Action |
|-------|---------|--------|
| **Learning** | Algorithm is actively exploring (first 50 conversions) | Do NOT edit. Let it run. |
| **Learned** | Algorithm has found optimal delivery strategy | Monitor and scale gradually |
| **Learning Limited** | Cannot get 50 conversions in 7 days | Increase budget, broaden targeting, or move up funnel |

### What Resets the Learning Phase

These edits reset the learning phase and should be avoided on performing ad groups:

| Edit Type | Resets Learning? | Risk Level |
|-----------|-----------------|------------|
| Change bid strategy | Yes | High |
| Change bid amount by > 20% | Yes | High |
| Change budget by > 50% | Yes | High |
| Change optimization event | Yes | High |
| Add/remove targeting | Partial | Medium |
| Add new creatives | No | Low |
| Pause/resume ad group | Partial | Medium |
| Change schedule | Partial | Medium |

**Golden rule: Do NOT make significant edits during the learning phase.** Wait for the ad group to either reach "Learned" status or spend 2x your target CPA without any conversion before intervening.

## Budget Scaling Strategies

### Vertical Scaling (Increase Budget on Winners)
- Increase budget by **no more than 20-30%** every 2-3 days
- Larger increases risk resetting the learning phase
- Monitor CPA for 48 hours after each increase
- If CPA rises > 20% after scaling, revert to previous budget

### Horizontal Scaling (New Ad Groups)
- Duplicate the winning ad group with a fresh budget
- Change one variable: new audience, new creative, or new bid strategy
- This avoids disrupting the original ad group's learned optimization
- Run 2-3 horizontal tests simultaneously

### Budget Allocation Framework
| Campaign Stage | Budget Split |
|----------------|-------------|
| Testing (Week 1-2) | 70% Lowest Cost testing, 30% proven winners |
| Optimization (Week 3-4) | 40% testing, 60% proven winners |
| Scale (Month 2+) | 20% testing, 80% proven winners |

## Bid Strategy Decision Matrix

| Scenario | Recommended Strategy | Reasoning |
|----------|---------------------|-----------|
| New account, no data | Lowest Cost | Need to learn baseline CPA |
| Know CPA, need volume | Cost Cap | Balanced cost control + delivery |
| Strict unit economics | Bid Cap | Hard cost ceiling |
| Scaling proven campaigns | Cost Cap or Lowest Cost | Maximize volume at known efficiency |
| Competitive seasonal period | Bid Cap | Prevent CPA spikes |
| Low budget (< $50/day) | Lowest Cost | Maximize learning from limited spend |
| High budget (> $500/day) | Cost Cap | Prevent runaway costs at scale |

## Output Format

```
## Bidding Analysis

### Strategy Assessment
| Ad Group | Bid Strategy | Bid/Cap | CPA (Actual) | vs Target | Learning Status | Recommendation |
|----------|-------------|---------|-------------- |-----------|-----------------|----------------|

### Learning Phase Health
| Ad Group | Conversions (7d) | Target (50) | Progress | Budget Sufficient? | Action |
|----------|-------------------|-------------|----------|-------------------|--------|

### Budget Sufficiency Check
| Ad Group | Daily Budget | Required for 50/7 | Deficit | Fix |
|----------|-------------|-------------------|---------|-----|

### Scaling Readiness
| Ad Group | Status | Current Budget | Safe Scale Amount | Next Step |
|----------|--------|----------------|-------------------|-----------|

### Priority Actions
1. [Highest impact bidding change]
2. ...
3. ...
```
