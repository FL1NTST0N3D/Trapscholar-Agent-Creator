# YouTube Bidding Strategy Skill

**Command:** `/yt bidding`

## Purpose

Analyzes and optimizes YouTube campaign bidding strategies. Bidding on YouTube is fundamentally different from Search or Shopping — the available bid strategies, optimization signals, and maturity requirements vary by campaign format and objective. Choosing the wrong bid strategy is one of the most common and costly YouTube advertising mistakes. This skill maps bid strategies to objectives and provides data-driven recommendations for bid optimization.

## YouTube Bid Strategies — Complete Reference

### Target CPV (tCPV) — Cost Per View

**What It Is:** You set a target price you are willing to pay per view. A "view" is counted when a user watches 30 seconds of your ad (or the full ad if shorter than 30 seconds) or interacts with it.

**When to Use:**
- Skippable In-Stream campaigns focused on consideration
- When you want qualified viewers only (people who choose to watch)
- Accounts with limited conversion data
- Product/service education campaigns where watch time matters

**When NOT to Use:**
- Awareness campaigns (CPM is more efficient for reach)
- Conversion campaigns (use Max Conversions or tCPA instead)
- Bumper or non-skippable formats (views are automatic — CPV has no filtering benefit)

**Benchmarks:**
- Average CPV across industries: $0.10 - $0.30
- B2B CPV: $0.15 - $0.35 (higher due to narrower targeting)
- E-commerce CPV: $0.08 - $0.20
- Mobile app CPV: $0.05 - $0.15

**Optimization Tips:**
- Start with a CPV bid 20% above your target to win initial auctions
- After 2 weeks of data, reduce bid by 5-10% increments
- If view rate drops below 20%, the bid may be too low (losing quality inventory)
- Monitor competitive landscape — CPV increases during Q4, back-to-school, and major shopping events

### Target CPM (tCPM) — Cost Per 1,000 Impressions

**What It Is:** You set a target price per 1,000 impressions. Google optimizes delivery to hit your CPM target on average.

**When to Use:**
- Bumper ads (6-second, non-skippable)
- Non-skippable in-stream ads (15-second)
- Shorts ads
- Brand awareness campaigns focused on maximum reach
- Video ad sequencing campaigns

**Benchmarks:**
- Bumper CPM: $2.00 - $6.00
- Non-skippable CPM: $4.00 - $10.00
- Shorts CPM: ~$4.00
- Premium inventory CPM: $10.00 - $20.00

**Optimization Tips:**
- Set tCPM 10-15% above your target initially for delivery ramp-up
- Monitor unique reach vs. total impressions — high frequency with low reach means tCPM is too low
- Use dayparting to shift budget toward cheaper time slots if reach is the goal
- Exclude expensive placements (music videos, major creator channels) if CPM is too high

### Maximize Conversions

**What It Is:** Google automatically sets bids to get the most conversions within your budget. No target CPA is set — Google spends the full daily budget.

**When to Use:**
- Early-stage conversion campaigns (building conversion data)
- When you have fewer than 30 conversions per month
- Testing phase to establish baseline CPA before moving to tCPA
- Accounts transitioning from awareness to performance

**When NOT to Use:**
- Mature accounts with established CPA targets (use tCPA instead)
- Limited budgets where CPA must be controlled (Maximize Conversions can overspend on expensive conversions)

**Requirements:**
- Conversion tracking must be active and accurately counting conversions
- Recommended minimum budget: $50/day per campaign
- Allow 2-3 weeks for learning phase (do not adjust during this period)

### Target CPA (tCPA) — Cost Per Acquisition

**What It Is:** You set a target cost per conversion. Google automatically adjusts bids to achieve your target CPA on average.

**When to Use:**
- Mature conversion campaigns with 30+ conversions per month
- Lead generation campaigns with established cost-per-lead targets
- E-commerce campaigns after initial Maximize Conversions learning phase

**Requirements:**
- Minimum 30 conversions in the last 30 days (Google's recommendation)
- Realistic tCPA target — set at or slightly above your actual CPA from Maximize Conversions
- Conversion tracking verified and stable

**Optimization Tips:**
- Set initial tCPA 10-20% above your actual CPA to avoid throttling
- Reduce tCPA by no more than 10% per week
- If delivery drops significantly, your tCPA is too aggressive
- Use portfolio bid strategies to share conversion data across campaigns

### Target ROAS (tROAS) — Return on Ad Spend

**What It Is:** You set a target return on ad spend (e.g., 400% means $4 revenue per $1 spent). Google optimizes bids to hit this target.

**When to Use:**
- E-commerce with dynamic revenue values
- Demand Gen campaigns with purchase value data
- Mature accounts with 50+ conversions per month and revenue tracking

**When NOT to Use:**
- Lead generation (no revenue values per lead — use tCPA instead)
- Accounts with fewer than 50 conversions per month
- New campaigns without historical conversion value data

**Benchmarks:**
- YouTube tROAS is typically lower than Search tROAS (YouTube is upper-funnel)
- Realistic YouTube tROAS targets: 200-400% for most e-commerce
- Include view-through conversions in ROAS calculation (YouTube drives delayed conversions)

### Maximum CPV

**What It Is:** You set the maximum price per view. Unlike tCPV, this is a hard cap, not an average target.

**When to Use:**
- Strict budget control scenarios
- Testing new campaigns where you need cost predictability
- Small daily budgets where overspend risk must be eliminated

## Bidding Maturity Model

YouTube campaigns should progress through bidding strategies as they mature:

```
Stage 1: Launch (Week 1-3)
  └── Manual CPV or Manual CPM
      Goal: Establish baseline metrics, gather initial data

Stage 2: Learning (Week 3-6)
  └── Maximize Conversions (if conversion goal) or tCPM (if awareness)
      Goal: Build conversion data, let algorithm learn

Stage 3: Optimization (Week 6-12)
  └── Target CPA (after 30+ conversions) or Target CPV (for engagement)
      Goal: Efficiency optimization, cost control

Stage 4: Scale (Month 3+)
  └── Target ROAS (if revenue data) or Portfolio Bidding
      Goal: Maximize profitable scale
```

## Seasonal Adjustment Strategies

YouTube CPMs and CPVs fluctuate significantly by season:

| Period | CPM Impact | Strategy |
|--------|-----------|----------|
| Q4 (Oct-Dec) | +40-80% CPM | Shift budget to Bumpers (cheaper CPM), reduce conversion targets |
| January | -20-30% CPM | Increase spend — cheap inventory, New Year intent |
| Back to School (Aug) | +15-25% CPM | Focus on education/youth targeting |
| Summer (Jun-Jul) | -10-15% CPM | Good for testing new creatives at lower cost |
| Black Friday/Cyber Monday | +50-100% CPM | Pre-build remarketing lists, run awareness in Oct |

**Seasonal Bid Adjustments in Google Ads:**
- Use seasonality bid adjustments (Advanced > Bid Adjustments > Seasonality) for short events (3-14 days)
- For longer seasons, manually adjust tCPA/tCPM targets
- Never use seasonality adjustments for periods longer than 14 days

## Bidding Audit Checklist

Score each item (0-10 points, total /100):

1. **Strategy Alignment** (/10): Is the bid strategy appropriate for the campaign objective?
2. **Maturity Stage** (/10): Is the campaign using the right strategy for its data maturity?
3. **Conversion Volume** (/10): Does the campaign have enough conversions for automated bidding?
4. **Bid Targets** (/10): Are CPV/CPM/CPA targets realistic based on historical data?
5. **Learning Phase** (/10): Has the campaign cleared learning phase without disruption?
6. **Seasonal Adjustments** (/10): Are bids adjusted for seasonal CPM fluctuations?
7. **Budget Sufficiency** (/10): Is the daily budget at least 10x the target CPA?
8. **Portfolio Strategy** (/10): Are related campaigns sharing conversion data via portfolio bidding?
9. **Conversion Window** (/10): Is the conversion window set to 30 days (not 1 day)?
10. **View-Through Tracking** (/10): Are view-through conversions included in bidding signals?

## Output Format

```
## Bidding Strategy Analysis: [Score]/100

### Current Setup
| Campaign | Bid Strategy | Target | Actual | Status |
|----------|-------------|--------|--------|--------|
| | | | | |

### Strategy Recommendations
| Campaign | Current | Recommended | Reason |
|----------|---------|-------------|--------|
| | | | |

### Maturity Assessment
- Conversion volume: [X] per month
- Current stage: [Launch/Learning/Optimization/Scale]
- Ready for next stage: [Yes/No — reason]

### Seasonal Considerations
- Current period: [Season]
- CPM impact: [+/- X%]
- Recommended adjustment: [Action]

### 30-Day Bid Optimization Plan
Week 1: ...
Week 2: ...
Week 3: ...
Week 4: ...
```
