---
name: bid-auction-insights
description: Auction Insights competitive analysis — impression share breakdown, overlap rate mapping, position above rate assessment, top-of-page rate evaluation, outranking share calculation, and competitive positioning map generation.
allowed-tools:
  - Bash
  - Read
  - Grep
---

# Auction Insights Analysis

You are analyzing Auction Insights data to understand competitive positioning relative to bid strategy performance. Auction Insights reveals who you're competing against, how often, and who's winning. Combined with bid strategy data, this tells you whether your bids are competitive enough, where you're losing ground, and whether your bid strategy is appropriately calibrated for the competitive landscape.

## Auction Insights Metrics Explained

**Impression Share (IS):**
The percentage of eligible impressions your ads actually received. Eligible impressions are determined by your targeting, approval status, and quality.
- Formula: Impressions / Total Eligible Impressions
- Benchmark: Top advertisers typically see 60-80% IS on brand, 20-50% IS on non-brand
- Missing IS = money left on the table (or money saved, depending on efficiency)

**Overlap Rate:**
How often a competitor's ad appeared when your ad also appeared. High overlap = direct competitor in the same auctions.
- Formula: Competitor Impressions When You Also Showed / Your Total Impressions
- Benchmark: > 70% overlap = head-to-head competitor. < 20% = occasional overlap.

**Position Above Rate:**
When both you and a competitor appeared in the same auction, how often their ad was positioned above yours.
- Formula: Competitor Above You / Auctions Where Both Appeared
- Benchmark: > 60% = they consistently outrank you. < 40% = you usually win position.

**Top of Page Rate:**
How often your ad appeared at the top of the page (above organic results).
- Formula: Top-of-Page Impressions / Total Impressions
- Search benchmark: 50-80% for competitive terms. < 30% = your bids or quality are too low.

**Absolute Top of Page Rate:**
How often your ad appeared as the very first ad (position 1).
- Benchmark: 15-40% for competitive terms. > 60% = you may be overbidding.

**Outranking Share:**
How often your ad ranked higher than a competitor's ad, or showed when theirs didn't.
- Formula: (Times You Outranked Competitor + Times You Showed & They Didn't) / Total Eligible Impressions
- Benchmark: > 50% = you're generally winning. < 30% = competitor dominates.

## Analysis Steps

### Step 1: Impression Share Decomposition

Break down impression share loss to understand WHY you're not showing:

```
Total Impression Share: X%
Lost to Budget:         Y%  (campaign ran out of budget)
Lost to Rank:           Z%  (bid or quality not competitive enough)

If Lost to Budget > Lost to Rank:
  Your bids are competitive, but budget is capping your reach.
  Solutions:
  - Increase budget (if profitable at current CPA)
  - Narrow targeting to focus budget on highest-value auctions
  - Lower tCPA target slightly to reduce cost per auction entry

If Lost to Rank > Lost to Budget:
  Your bids or quality scores are not competitive.
  Solutions:
  - Check Quality Scores (< 5 on key terms = you're paying a premium)
  - Review Ad Rank components: bid, quality, ad extensions, format
  - If on tCPA: target may be too low for the auction environment
  - If on Max Conversions: algorithm may be de-prioritizing expensive auctions

Balance check:
  IS > 80%: Dominant position. Good if profitable. Verify not overbidding.
  IS 50-80%: Competitive position. Room to grow if budget allows.
  IS 30-50%: Moderate presence. Missing significant volume.
  IS 15-30%: Limited presence. Either niche strategy or underbidding.
  IS < 15%: Marginal participant. Reconsider targeting or budget.
```

### Step 2: Competitor Mapping

Create a competitive landscape from Auction Insights data:

```
For each competitor (display URL domain), compile:

| Competitor | Overlap Rate | Position Above | Outranking Share | Their IS | Threat Level |
|-----------|-------------|---------------|-----------------|----------|-------------|

Threat Level Classification:
  HIGH THREAT: Overlap > 60%, Position Above > 50%, Their IS > yours
  → This competitor is consistently beating you in shared auctions.
  → They likely have higher bids, better Quality Scores, or both.

  MEDIUM THREAT: Overlap > 40%, Position Above 30-50%
  → Competitive but not dominant. You're trading positions.

  LOW THREAT: Overlap < 40% or Position Above < 30%
  → Occasional competitor. Not significantly impacting your performance.

  NEW ENTRANT: Competitor appeared in last 30 days but not prior 30 days
  → Monitor closely. New competitors can disrupt auction dynamics.

  DECLINING: Competitor's metrics dropping month-over-month
  → Opportunity to capture their impression share as they pull back.
```

### Step 3: Competitive Position vs Bid Strategy Alignment

Cross-reference auction position with bid strategy configuration:

**Scenario: High IS + Low CPA (winning efficiently)**
- Ideal state. Bid strategy is well-calibrated for the competitive environment.
- Action: Maintain. Consider modest budget increases to capture remaining IS.

**Scenario: High IS + High CPA (winning expensively)**
- You're winning auctions but paying too much. Possible overbidding.
- If on Max Conversions: Graduate to tCPA to add efficiency guardrail.
- If on tCPA: Target may be too high, or Quality Score issues inflating CPC.

**Scenario: Low IS + Low CPA (efficient but invisible)**
- Your bid strategy is too conservative. Missing profitable auctions.
- If on tCPA: Target is likely too aggressive (too low), limiting auction entry.
- If budget-limited: Increase budget to capture more eligible impressions.
- Raise tCPA target by 10-15% to enter more auctions.

**Scenario: Low IS + High CPA (losing and expensive)**
- Worst case. You're paying a lot for the impressions you do get, AND missing most auctions.
- Usually indicates Quality Score problems (you're paying an "Ad Rank penalty").
- Fix Quality Score first (landing page, ad relevance, expected CTR).
- Review keyword-level Quality Scores for your highest-spend terms.

### Step 4: Position Strategy by Campaign Type

**Brand Campaigns:**
- Target: 90%+ Impression Share, 80%+ Absolute Top of Page Rate
- Bid strategy: Target Impression Share (90%+ target) or very generous tCPA
- Competitors showing on your brand terms = bid up to defend
- Monitor: new competitors appearing on your brand terms

**Non-Brand Search Campaigns:**
- Target: 40-70% Impression Share (cost-efficient presence, not domination)
- Position Above Rate: 40-60% against top competitors is healthy
- Don't chase 90%+ IS on non-brand — diminishing returns are steep
- Focus on impression share for your highest-converting keywords specifically

**Shopping Campaigns:**
- Auction Insights in Shopping is product-level, not keyword-level
- Focus on: which competitors appear most in your product categories
- Price competitiveness matters more than bid strategy in Shopping
- If losing IS: check product feed quality, pricing, and reviews

**PMax Campaigns:**
- Limited Auction Insights available for PMax
- Focus on the Search-network portion of Auction Insights
- PMax's cross-network optimization makes auction position less actionable

### Step 5: Competitive Trend Analysis

Track competitor metrics over time (monthly comparison):

```
Month-over-Month Changes:

Competitor IS increasing + Your IS decreasing:
  They're gaining ground. Possible responses:
  - Increase budget if IS lost to budget
  - Improve Quality Score if IS lost to rank
  - Raise bid targets if competition is pushing auction prices up
  - Refresh ad creative for better CTR

Your IS increasing + Competitor IS decreasing:
  You're gaining ground. Capitalize:
  - Maintain current strategy (it's working)
  - Consider modest budget increases to accelerate gains
  - Monitor CPA — increasing IS should ideally not spike CPA

Both IS declining:
  New competitor(s) entering the auction. Check for new entrants.

Both IS stable:
  Market equilibrium. Focus on efficiency improvements.
```

### Step 6: Competitive Positioning Map

Generate a 2x2 positioning map:

```
                    High Impression Share
                          |
    Expensive Winner      |      Efficient Winner
    (High CPA, High IS)   |      (Low CPA, High IS)
                          |
   -------- High CPA -----+------- Low CPA --------
                          |
    Expensive Loser       |      Efficient Niche
    (High CPA, Low IS)    |      (Low CPA, Low IS)
                          |
                    Low Impression Share

Plot each campaign on this map.
Goal: Move all campaigns toward "Efficient Winner" quadrant.
```

## Output Format

```
## Auction Insights Analysis

### Impression Share Overview
[Account-level and campaign-level IS breakdown]

### Competitor Map
[Top 5-10 competitors with threat classification]

### Competitive Position Assessment
[Per-campaign position vs bid strategy alignment]

### Trend Analysis
[Month-over-month competitive movement]

### Positioning Map
[2x2 map of campaigns by IS and CPA]

### Recommendations
1. [Campaigns where bid targets need adjustment for competitive position]
2. [Quality Score improvements needed]
3. [Budget reallocation for competitive advantage]
4. [Brand defense actions]
5. [Monitoring alerts for competitive changes]
```
