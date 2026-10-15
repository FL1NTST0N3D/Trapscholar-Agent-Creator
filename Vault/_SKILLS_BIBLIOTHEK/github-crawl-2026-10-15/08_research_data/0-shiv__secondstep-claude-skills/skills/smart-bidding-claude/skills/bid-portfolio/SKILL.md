---
name: bid-portfolio
description: Portfolio bidding strategy analysis — evaluate campaign grouping logic, cross-campaign similarity assessment, shared vs individual target performance, budget redistribution effectiveness, and portfolio optimization recommendations.
allowed-tools:
  - Bash
  - Read
  - Grep
---

# Portfolio Bidding Analysis

You are analyzing portfolio bid strategies across a Google Ads account. Portfolio bidding allows multiple campaigns to share a single bid strategy, pooling conversion data and enabling budget redistribution across campaigns. When implemented correctly, portfolio bidding can improve performance for low-volume campaigns and optimize budget allocation. When implemented poorly, it creates cross-campaign contamination and obscures individual campaign performance.

## How Portfolio Bidding Works

1. **Shared target**: All campaigns in a portfolio optimize toward the same tCPA or tROAS target. The algorithm treats the portfolio as a single optimization unit.

2. **Cross-campaign learning**: Conversion data from all campaigns is pooled. A campaign with 10 conversions/month benefits from the 40 conversions across the portfolio.

3. **Budget redistribution**: Google can shift budget between campaigns in the portfolio based on where it finds the best opportunities. A campaign hitting its daily budget may receive more spend while an underperforming one gets less.

4. **Shared learning phase**: Changes to the portfolio target trigger learning phase across ALL campaigns in the portfolio simultaneously.

## Analysis Steps

### Step 1: Portfolio Inventory

Map all portfolio bid strategies in the account:

| Portfolio Name | Strategy Type | Target | Campaigns | Total Conv (30d) | Total Cost (30d) | Portfolio CPA/ROAS |
|---------------|---------------|--------|-----------|-----------------|-------------------|-------------------|

For each portfolio, list all member campaigns with their individual metrics:
- Campaign name and type
- Individual 30d conversions, cost, CPA/ROAS
- Individual daily budget
- Campaign conversion action (must match across portfolio)

### Step 2: Campaign Similarity Assessment

Campaigns in a portfolio should be similar enough that a shared target makes sense. Evaluate:

**CPA Similarity (for tCPA portfolios):**
```
CPA Range = Max Campaign CPA / Min Campaign CPA (within portfolio)

Range < 1.5x:  EXCELLENT. Campaigns have similar CPAs. Portfolio
                grouping is well-suited.

Range 1.5-2.0x: ACCEPTABLE. Some variation but manageable.
                Monitor for the low-CPA campaign subsidizing
                the high-CPA campaign.

Range 2.0-3.0x: WARNING. Significant CPA disparity. The portfolio
                target is likely too high for efficient campaigns
                and too low for expensive ones. Consider splitting.

Range > 3.0x:   CRITICAL. These campaigns should NOT be in the
                same portfolio. The shared target is a compromise
                that hurts all campaigns. Split immediately.
```

**Campaign Type Compatibility:**
```
COMPATIBLE groupings:
- Multiple Search campaigns targeting similar keywords/audiences
- Multiple Shopping campaigns in the same product category
- Search campaigns in the same funnel stage (all top-of-funnel, or all bottom)

INCOMPATIBLE groupings (split these):
- Search + Display (fundamentally different intent signals and CPA ranges)
- Brand + Non-brand (brand CPA is typically 5-10x lower)
- Search + PMax (PMax has its own cross-network optimization)
- Campaigns with different conversion actions
- Campaigns targeting different geographies with different market dynamics
- Lead gen + e-commerce campaigns in the same portfolio
```

**Conversion Action Consistency:**
All campaigns in a portfolio MUST optimize for the same conversion action(s). If Campaign A counts "form submissions" and Campaign B counts "phone calls," the portfolio is optimizing for a blended metric that may not reflect either campaign's true goal.

### Step 3: Performance Impact Analysis

Evaluate whether the portfolio is helping or hurting compared to individual strategies:

**Budget Redistribution Assessment:**
- Is budget flowing from low-performing to high-performing campaigns? (Good)
- Is budget flowing from high-CPA to low-CPA campaigns? (Good)
- Or is budget being drained from efficient campaigns to feed inefficient ones? (Bad)

```
For each campaign in the portfolio:
  Individual CPA vs Portfolio CPA

  If Campaign CPA < Portfolio CPA:
    This campaign is SUBSIDIZING the portfolio. It could perform
    better with its own lower tCPA target.

  If Campaign CPA > Portfolio CPA:
    This campaign is BENEFITING from the portfolio. It would likely
    see higher CPA or reduced volume with its own strategy.

  If Campaign CPA ≈ Portfolio CPA (within 10%):
    Campaign is aligned with portfolio performance. Good grouping.
```

**Volume Contribution Analysis:**
- What percentage of total portfolio conversions does each campaign contribute?
- If one campaign contributes > 70% of conversions, the portfolio is essentially optimizing for that one campaign while the others ride along.
- Small campaigns (< 10% of volume) get minimal algorithmic attention within the portfolio.

### Step 4: Shared vs Individual Target Comparison

Estimate what performance would look like with individual targets:

**Simulation Approach:**
1. For each campaign, calculate its individual 30d CPA/ROAS
2. Compare to portfolio CPA/ROAS
3. If the campaign's individual CPA is significantly lower than portfolio target, it's being held back
4. If the campaign's individual CPA is significantly higher, it's being propped up

**When Portfolio Outperforms Individual:**
- Low-volume campaigns (< 20 conversions/month) benefit from pooled data
- Campaigns with complementary search intent (different stages of same journey)
- Budget flexibility allows capturing opportunities the individual budget couldn't

**When Individual Outperforms Portfolio:**
- High-volume campaigns (50+/month) that don't need pooled data
- Campaigns with very different CPA economics
- When budget redistribution pulls spend from your best campaign

### Step 5: Portfolio Optimization Recommendations

**Portfolio Restructuring Options:**

1. **Split by CPA tier**: Group campaigns with similar CPA into separate portfolios
   - Low CPA portfolio (brand + high-intent)
   - Medium CPA portfolio (mid-funnel)
   - High CPA portfolio (top-funnel, competitive terms)

2. **Split by campaign type**: Separate Search, Shopping, Display into distinct portfolios

3. **Graduate high-volume campaigns**: Campaigns with 50+ conversions/month should have their own individual tCPA/tROAS strategy

4. **Consolidate low-volume campaigns**: Campaigns with < 15 conversions/month should either be in a portfolio or merged into larger campaigns

5. **Align conversion actions**: Ensure all campaigns in a portfolio use the same primary conversion action

**Target Adjustment for Portfolios:**
- Portfolio target should be set at the weighted average CPA of all member campaigns
- Weight by spend, not by campaign count
- Adjust portfolio target using the same ratcheting rules as individual tCPA (max 15-20% change, 14-day wait)

### Step 6: Single-Campaign Portfolios

Identify portfolios that contain only one campaign. This is a common configuration issue:

- Single-campaign portfolios provide NO benefit over individual campaign-level strategies
- They add unnecessary complexity to the account structure
- They may be remnants of campaigns that were removed from the portfolio but the strategy was kept
- Recommendation: Convert to campaign-level bid strategy (same type and target)

## Output Format

```
## Portfolio Bidding Analysis

### Portfolio Inventory
[All portfolios with member campaigns]

### Similarity Assessment
[Per-portfolio campaign compatibility check]

### Performance Impact
[Is each portfolio helping or hurting its member campaigns?]

### Redistribution Patterns
[Where is budget flowing within each portfolio?]

### Recommendations
1. [Portfolios to restructure — with proposed new groupings]
2. [Campaigns to graduate to individual strategies]
3. [Low-volume campaigns to consolidate]
4. [Single-campaign portfolios to eliminate]
5. [Target adjustments needed]
```
