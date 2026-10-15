---
name: bid-strategy-audit
description: Identify current bid strategy per campaign, assess strategy fit based on conversion volume and campaign type, check target alignment against actual performance, and flag strategy mismatches.
allowed-tools:
  - Bash
  - Read
  - Grep
---

# Bid Strategy Audit

You are analyzing the bid strategy configuration across a Google Ads account. Your goal is to identify every campaign's current bidding strategy, evaluate whether it is the optimal choice given the campaign's data, and flag any mismatches that are costing performance.

## Analysis Framework

### Step 1: Inventory All Campaigns and Their Bid Strategies

Create a complete inventory table with these columns:

| Campaign | Type | Bid Strategy | Target | 30d Conv | 30d Cost | 30d CPA | 30d Value | 30d ROAS | Budget | Status |
|----------|------|-------------|--------|----------|----------|---------|-----------|----------|--------|--------|

For each campaign, classify the bid strategy into one of:
- **tCPA** — Target CPA (Maximize Conversions with target)
- **tROAS** — Target ROAS (Maximize Conversion Value with target)
- **Max Conv** — Maximize Conversions (no target)
- **Max Value** — Maximize Conversion Value (no target)
- **Manual CPC** — Manual cost-per-click bidding
- **eCPC** — Enhanced CPC (DEPRECATED)
- **Portfolio** — Part of a portfolio bid strategy (note which one)
- **Max Clicks** — Maximize Clicks (typically wrong for conversion campaigns)
- **Target Imp Share** — Target Impression Share (brand campaigns only)

### Step 2: Assess Strategy Fit Per Campaign

For each campaign, evaluate strategy fit using this decision matrix:

**Search Campaigns:**
- < 15 conversions/month: Manual CPC or Max Conversions
- 15-29 conversions/month: Max Conversions (preparing for tCPA)
- 30-49 conversions/month: tCPA (if CPA is stable) or Max Conversions
- 50+ conversions/month: tCPA or tROAS (if value tracking exists)
- Brand campaigns: Target Impression Share (90%+ target) or tCPA with low target

**Performance Max Campaigns:**
- Always automated — only choice is Max Conversions, tCPA, Max Value, or tROAS
- < 30 conversions/month: Max Conversions or Max Value
- 30+ conversions/month: tCPA
- 50+ conversions/month with value tracking: tROAS
- PMax campaigns benefit most from tROAS when revenue data is clean

**Shopping Campaigns (Standard):**
- Same thresholds as Search
- tROAS is often preferred because product values vary
- Ensure Merchant Center revenue matches Google Ads conversion value

**Display Campaigns:**
- tCPA is usually the best option (Display has high volume, low intent)
- Set tCPA higher than Search — Display CPA is naturally higher
- Max Conversions can overspend on low-quality placements

**Video Campaigns (YouTube):**
- Max Conversions for action campaigns (TrueView for Action)
- tCPA once you have 30+ conversions/month
- CPV bidding for awareness campaigns (not Smart Bidding)

**Discovery / Demand Gen Campaigns:**
- Max Conversions or tCPA
- Similar thresholds to Display
- tROAS available but needs high volume

### Step 3: Check Target Alignment

For campaigns using tCPA or tROAS, evaluate target accuracy:

**tCPA Target Assessment:**
```
Target vs Actual Ratio = Target CPA / Actual CPA (last 30 days)

< 0.60  = CRITICAL: Target is dangerously aggressive. Smart Bidding is
          severely throttling spend to try to hit an impossible target.
          Expected impact: 50-80% volume loss.

0.60-0.79 = WARNING: Target is too aggressive. Campaign is likely
            under-delivering. Volume is being sacrificed for efficiency.
            Expected impact: 20-40% volume loss.

0.80-0.89 = MINOR: Slightly aggressive but workable. May see some
            volume pressure. Monitor weekly.

0.90-1.20 = OPTIMAL: Target is well-calibrated. Smart Bidding has
            room to optimize without sacrificing volume.

1.21-1.50 = CONSERVATIVE: Target is loose. You're likely paying more
            per conversion than necessary. Tighten gradually.

> 1.50   = WARNING: Target is far too conservative. You're significantly
           overpaying. Smart Bidding has no incentive to find cheaper conversions.
```

**tROAS Target Assessment:**
```
Target vs Actual Ratio = Target ROAS / Actual ROAS (last 30 days)

> 1.50  = CRITICAL: Target ROAS is far above actual. Smart Bidding is
          only bidding on the most profitable auctions, missing volume.

1.21-1.50 = WARNING: Target is aggressive. Volume is being limited.

1.00-1.20 = OPTIMAL: Target is well-calibrated.

0.80-0.99 = CONSERVATIVE: You could push for better returns.

< 0.80   = WARNING: Target is far too conservative. You're accepting
           poor returns when the account could do better.
```

### Step 4: Flag Strategy Mismatches

Identify these common mismatches:

1. **tCPA with insufficient volume**: Campaign has < 30 conversions/month but is using tCPA. Smart Bidding lacks signal. Recommend: Switch to Max Conversions until volume builds.

2. **tROAS without value tracking**: Campaign uses tROAS but all conversions have the same value (or no value). tROAS degrades to tCPA behavior. Recommend: Switch to tCPA or fix value tracking.

3. **Max Conversions on mature campaign**: Campaign has 50+ conversions/month and stable CPA but is still on Max Conversions. It's leaving efficiency on the table. Recommend: Graduate to tCPA.

4. **eCPC still active**: Campaign is using Enhanced CPC, which Google deprecated in 2025. The algorithm is no longer being improved. Recommend: Migrate to Max Conversions immediately, then graduate to tCPA.

5. **Max Clicks on conversion campaign**: Campaign has conversion tracking and a conversion goal but is using Max Clicks. Bidding is optimizing for clicks, not conversions. Recommend: Switch to Max Conversions.

6. **Target Impression Share on non-brand**: Non-brand campaign using Target Impression Share. You're paying for visibility, not conversions. Recommend: Switch to tCPA or Max Conversions.

7. **Manual CPC on high-volume campaign**: Campaign has 50+ conversions/month but uses Manual CPC. You're leaving significant optimization opportunity on the table. Recommend: Test Max Conversions, then graduate to tCPA.

8. **tCPA on campaign with high CPA variance**: CPA fluctuates more than 40% week-over-week. Smart Bidding's target is a moving target. Recommend: Investigate conversion tracking (delayed conversions? micro + macro mixed?), or use Max Conversions until CPA stabilizes.

9. **Portfolio bidding with mismatched campaigns**: Brand and non-brand campaigns in the same portfolio. Brand CPAs are typically 5-10x lower, which skews the portfolio's optimization. Recommend: Separate into distinct portfolios.

10. **Multiple conversion actions with different values**: Campaign is optimizing for multiple conversion actions but Smart Bidding treats them equally. Recommend: Set conversion values that reflect true business value, or use a single primary conversion action.

### Step 5: Generate Strategy Recommendations

For each mismatch found, provide:
- **Current state**: What's happening now
- **Problem**: Why this is suboptimal
- **Recommendation**: What to change
- **Expected impact**: Estimated improvement (conservative)
- **Risk**: What could go wrong
- **Timeline**: How long before you see results (always include 2-week learning phase)

## Output Format

```
## Bid Strategy Audit Results

### Account Overview
- Total campaigns analyzed: X
- Using optimal strategy: X (X%)
- Strategy mismatches found: X
- Campaigns needing graduation: X

### Strategy Distribution
[Table showing count of campaigns per strategy type]

### Findings

#### Critical (Act Immediately)
[List critical mismatches]

#### Warning (Plan Changes)
[List warnings]

#### Info (Monitor)
[List informational findings]

### Recommendations (Priority Order)
1. [Highest impact change]
2. [Second highest]
...

### Implementation Timeline
Week 1: [Changes]
Week 3: [Evaluate + next changes]
Week 5: [Evaluate + next changes]
```
