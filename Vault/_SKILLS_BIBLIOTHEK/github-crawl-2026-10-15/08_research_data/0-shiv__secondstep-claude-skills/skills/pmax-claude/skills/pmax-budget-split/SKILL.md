---
name: pmax-budget-split
description: "Optimize the budget allocation between Performance Max and Search campaigns. Provides recommended ratios by account type, analyzes incremental lift, and identifies budget efficiency opportunities."
allowed-tools:
  - Bash
  - Read
  - Grep
---

# PMax Budget Split Skill

## Purpose

The balance between PMax and Search campaign budgets is one of the most consequential decisions in a Google Ads account. Too much budget in PMax risks cannibalization and opacity. Too little misses PMax's cross-channel discovery potential. This skill analyzes your current split and recommends optimal allocation based on your account type, performance data, and business objectives.

## Trigger

Activated by `/pmax budget` or as part of `/pmax audit`.

## Data Requirements

Ask the user for:
1. Total monthly Google Ads budget
2. Current PMax budget and Search budget
3. Campaign performance data (last 90 days): conversions, cost, CPA, ROAS
4. Account type (e-commerce, lead gen, SaaS, local services, etc.)
5. Business objectives (maximize conversions, maximize revenue, target CPA, target ROAS)
6. Account maturity (new <6 months, established 6-24 months, mature 2+ years)
7. Whether branded Search campaigns exist separately

## Recommended Budget Splits by Account Type

### E-Commerce (Feed-Based)

| Scenario | PMax % | Search % | Rationale |
|---|---|---|---|
| Large catalog (1000+ products) | 50-60% | 40-50% | PMax excels at product-level matching with Shopping |
| Small catalog (<100 products) | 35-45% | 55-65% | Search provides more control with fewer products |
| High-margin products | 40-50% | 50-60% | Search for high-intent, PMax for discovery |
| Low-margin/competitive | 45-55% | 45-55% | PMax's efficiency helps in competitive markets |
| New e-commerce store | 30-40% | 60-70% | Establish Search baseline before scaling PMax |
| Mature e-commerce | 50-60% | 40-50% | PMax cross-channel value maximized with data |

### Lead Generation

| Scenario | PMax % | Search % | Rationale |
|---|---|---|---|
| B2B / High-value leads | 20-30% | 70-80% | Lead quality control critical; Search provides it |
| B2B with strong CRM data | 30-40% | 60-70% | Customer lists boost PMax signal quality |
| Local services | 25-35% | 65-75% | PMax Maps/Discovery valuable; Search for intent |
| Professional services | 20-30% | 70-80% | High CPA tolerance; Search precision needed |
| Insurance/Financial | 15-25% | 75-85% | Compliance + lead quality demand Search control |
| Education/Programs | 30-40% | 60-70% | PMax YouTube/Display for awareness funnel |

### SaaS / Software

| Scenario | PMax % | Search % | Rationale |
|---|---|---|---|
| PLG (product-led growth) | 30-40% | 60-70% | PMax for awareness, Search for trial signups |
| Enterprise SaaS | 15-25% | 75-85% | Long sales cycle; Search intent signals crucial |
| Freemium model | 35-45% | 55-65% | PMax helps acquire freemium users at scale |
| Competitive market | 25-35% | 65-75% | Search brand defense + PMax discovery |

### Brand-Heavy Accounts

| Scenario | PMax % | Search % | Rationale |
|---|---|---|---|
| Strong brand, high branded search | 15-25% | 75-85% | Protect branded traffic from PMax cannibalization |
| Growing brand, low awareness | 35-45% | 55-65% | PMax YouTube/Display builds awareness |
| Established brand + e-commerce | 40-50% | 50-60% | PMax Shopping + brand defense in Search |

## Budget Efficiency Analysis

### Key Metrics to Compare

For each campaign type, compare:

| Metric | Search Campaign | PMax Campaign | Flag If |
|---|---|---|---|
| CPA | $X | $Y | PMax CPA >20% higher |
| ROAS | X:1 | Y:1 | PMax ROAS >15% lower |
| Conversion Rate | X% | Y% | PMax CvR >25% lower |
| Cost per Click | $X | $Y | Informational |
| Impression Share | X% | Y% | Search IS dropping while PMax scales |

### Incremental Lift Analysis

The critical question: **Is PMax generating conversions you wouldn't have gotten from Search alone?**

#### Method 1: Marginal CPA Analysis
```
Search CPA at current budget: $50
Search CPA if budget increased 30%: $65 (diminishing returns)
PMax CPA: $55

If PMax CPA < Search marginal CPA → PMax is efficient for incremental volume
If PMax CPA > Search marginal CPA → Budget better spent scaling Search
```

#### Method 2: Total Account Performance
```
Before PMax:
  Total budget: $10,000
  Total conversions: 200
  Blended CPA: $50

After PMax (same total budget):
  Total budget: $10,000
  Total conversions: 230 (+15%)
  Blended CPA: $43.50 (-13%)

  → PMax is providing incremental value
```

```
After PMax (same total budget):
  Total budget: $10,000
  Total conversions: 205 (+2.5%)
  Blended CPA: $48.80 (-2.4%)

  → PMax is mostly cannibalizing Search with marginal gains
```

#### Method 3: Geo-Split Test
- Run PMax in half your target geos, Search-only in the other half
- Compare total conversions and CPA for each group
- Most reliable but requires 2-4 weeks and sufficient volume

### Budget Scaling Signals

#### Scale UP PMax If:
- PMax CPA is 15%+ lower than Search CPA
- Total account conversions increased >10% after PMax launch
- PMax Insights show >40% of traffic from non-Search channels (Display, YouTube, Discover)
- Asset performance ratings are predominantly Best/Good
- Audience signals are strong (custom segments + customer lists)
- Limited impression share loss in branded Search

#### Scale DOWN PMax If:
- PMax CPA is higher than Search CPA for same conversion actions
- Branded Search impression share dropped >15% after PMax
- PMax Insights show >60% of traffic from Search (cannibalization indicator)
- Total account conversions flat or marginal increase despite added budget
- Asset performance ratings predominantly Low/Unrated
- No audience signals configured (PMax running blind)

#### Pause PMax If:
- Total account performance worse than Search-only baseline
- Cannibalization confirmed by incrementality test
- Lead quality significantly worse from PMax (for lead gen accounts)
- Unable to provide minimum viable assets (auto-generated creatives hurting brand)

## Budget Reallocation Framework

### Step-by-Step Budget Optimization

1. **Establish baseline**: Run Search-only for 30 days, record performance
2. **Launch PMax conservatively**: Start at 20% of budget in PMax
3. **Monitor for 30 days**: Compare blended CPA, total conversions, branded IS
4. **Evaluate incrementality**: Use methods above to determine if PMax is incremental
5. **Adjust in 10% increments**: Scale PMax up or down by 10% every 2-4 weeks
6. **Cap PMax**: Set a maximum PMax budget based on account type guidelines above
7. **Continuous monitoring**: Check monthly for cannibalization signals

### Budget Transition Calendar

| Week | Action | Monitor |
|---|---|---|
| Week 1-4 | Baseline (Search only or current state) | CPA, conversions, IS |
| Week 5-8 | Launch/adjust PMax at recommended % | Blended CPA, total conversions |
| Week 9-12 | First evaluation and adjustment | Cannibalization signals, IS |
| Week 13-16 | Optimize to target split | All metrics, incrementality |
| Monthly | Ongoing optimization | Budget efficiency ratio |

## Scoring Rubric (0-100)

| Criteria | Points | Condition |
|---|---|---|
| Budget split aligns with account type | 25 | Within recommended range = 25pts, close = 15pts, far = 5pts |
| PMax CPA competitive with Search CPA | 20 | Lower = 20pts, within 10% = 15pts, 10-20% higher = 8pts, >20% higher = 0pts |
| Evidence of incremental lift | 20 | Confirmed = 20pts, likely = 12pts, unclear = 6pts, no evidence = 0pts |
| Budget scaling direction is correct | 15 | Correct signals = 15pts, neutral = 8pts, wrong direction = 0pts |
| Regular budget optimization cadence | 10 | Monthly review = 10pts, quarterly = 5pts, never = 0pts |
| PMax budget has a cap/guardrail | 10 | Yes = 10pts, no = 0pts |

## Output Format

```
## Budget Split Audit Results

### Budget Efficiency Score: XX/100

### Current Allocation
| Campaign Type | Budget | % of Total | Conversions | CPA | ROAS |
|---|---|---|---|---|---|
| PMax | $X | X% | X | $X | X:1 |
| Search (Brand) | $X | X% | X | $X | X:1 |
| Search (Non-Brand) | $X | X% | X | $X | X:1 |
| Total | $X | 100% | X | $X | X:1 |

### Recommended Allocation
| Campaign Type | Current % | Recommended % | Change | Expected Impact |
|---|---|---|---|---|
| PMax | X% | Y% | +/-Z% | [impact description] |
| Search | X% | Y% | +/-Z% | [impact description] |

### Account Type: [E-Commerce/Lead Gen/SaaS/etc.]
### Recommended PMax Range: X-Y%
### Current PMax %: Z%
### Status: [Within Range/Over-Allocated/Under-Allocated]

### Incremental Lift Assessment
- Method used: [Marginal CPA / Total Account / Geo-Split / None]
- Finding: [PMax incremental / Cannibalizing / Insufficient data]
- Confidence: [High/Medium/Low]

### Scaling Recommendation
- Direction: [Scale Up / Scale Down / Maintain / Pause]
- Target: Move PMax from X% to Y% over Z weeks
- Implementation: [Step-by-step plan]

### Critical Issues
- [List findings]

### Recommendations
1. [Prioritized action items]
```
