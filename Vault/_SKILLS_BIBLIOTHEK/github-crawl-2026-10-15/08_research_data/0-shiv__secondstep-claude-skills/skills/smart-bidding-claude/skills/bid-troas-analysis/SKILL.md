---
name: bid-troas-analysis
description: Deep dive analysis of Target ROAS bidding campaigns — actual vs target ROAS, revenue tracking accuracy validation, product-level ROAS variation, and target optimization strategy.
allowed-tools:
  - Bash
  - Read
  - Grep
---

# Target ROAS (tROAS) Deep Dive Analysis

You are performing a specialized analysis of all campaigns using Target ROAS bidding. tROAS is the most powerful Smart Bidding strategy for revenue-focused accounts but also the most sensitive to data quality. Bad revenue data produces confidently wrong bids. Your goal is to validate revenue tracking, assess target accuracy, analyze product/service-level ROAS variation, and optimize targets.

## How tROAS Differs from tCPA

tROAS optimizes for **revenue per ad dollar** rather than cost per conversion. This distinction matters:

- tCPA treats all conversions equally. A $10 purchase and a $1,000 purchase are the same "conversion."
- tROAS weights bids by expected conversion value. It bids more for users likely to make high-value purchases and less for low-value ones.
- tROAS needs MORE data than tCPA (50+ conversions/month vs 30+) because it's learning value patterns, not just conversion probability.
- tROAS is sensitive to conversion value accuracy. If your revenue tracking is off by 20%, your ROAS calculation is meaningless.

## Analysis Steps

### Step 1: Revenue Tracking Validation

Before analyzing ROAS performance, verify the data is trustworthy:

**Revenue Tracking Checklist:**

1. **Dynamic value tracking**: Are conversion values being passed dynamically from the cart/CRM, or is a static default value being used?
   - Static value = tROAS has no value signal to optimize on. It degrades to tCPA behavior.
   - Check: Do conversions show varied values, or all the same amount?

2. **Value accuracy**: Compare Google Ads conversion value (last 30 days) against backend revenue (Shopify, WooCommerce, CRM, POS).
   - Discrepancy < 10%: Acceptable
   - Discrepancy 10-20%: Needs investigation (returns, attribution, delayed transactions)
   - Discrepancy > 20%: Revenue tracking is unreliable. Fix before trusting tROAS.

3. **Revenue includes the right components**: Does the tracked value include:
   - Product price only? (Most common, usually correct)
   - Shipping costs? (Inflates ROAS artificially)
   - Tax? (Inflates ROAS, inconsistent by state/country)
   - Subscription LTV? (If so, over what period?)

4. **Currency consistency**: Are conversion values in the same currency as the Google Ads account? Mixed currencies produce garbage ROAS numbers.

5. **Return/refund handling**: Are refunds deducted from conversion value? If not, ROAS is overstated. Google Ads supports conversion value adjustments via the API or Offline Conversion Import.

6. **Cross-device and cross-session attribution**: Is the attribution model capturing the full customer journey? Data-Driven Attribution (DDA) is recommended for tROAS. Last-click undercounts conversions and undervalues ROAS.

### Step 2: tROAS Campaign Inventory

For each tROAS campaign, collect:

| Metric | What to Check |
|--------|--------------|
| Target ROAS | Current target (as % or ratio, e.g., 400% = 4:1) |
| Actual ROAS (7d) | Recent trend |
| Actual ROAS (30d) | Stable baseline |
| Actual ROAS (90d) | Long-term average, seasonality context |
| Conversions (30d) | Volume sufficiency (need 50+) |
| Conv value (30d) | Total revenue attributed |
| Avg order value | Revenue / Conversions — is this realistic? |
| AOV variance | StdDev of order values — high variance = more data needed |
| Cost (30d) | Total spend |
| Search Impr Share | Is the target limiting auction participation? |
| Search Lost IS (Rank) | Rank-limited often means target is too aggressive |
| Campaign type | Search, Shopping, PMax — each behaves differently |

### Step 3: Target vs Actual ROAS Assessment

```
ratio = target_roas / actual_roas_30d

> 1.50:
    CRITICAL: Target ROAS is far above actual performance.
    Smart Bidding is cherry-picking only the most profitable auctions.
    Volume is severely limited. You're likely missing 50%+ of
    profitable opportunities because they don't meet the inflated target.
    Fix: Lower target to 100-110% of actual ROAS.

1.21-1.50:
    WARNING: Target is aggressive. Campaign is under-delivering.
    Smart Bidding is being selective, sacrificing volume for efficiency.
    Fix: Lower target by 15-20%. Monitor for 2 weeks.

1.00-1.20:
    OPTIMAL: Target is well-calibrated. Smart Bidding has room
    to optimize without excessive volume loss.
    Action: Monitor. Consider gradual tightening if stable.

0.80-0.99:
    CONSERVATIVE: Actual ROAS exceeds target. You could push
    for better returns without losing significant volume.
    Fix: Raise target by 10-15%. Wait 2 weeks.

0.50-0.79:
    WARNING: Target is far too conservative. You're accepting
    poor returns. Smart Bidding is overbidding because it easily
    exceeds your low bar.
    Fix: Raise target to 90-100% of actual ROAS.

< 0.50:
    CRITICAL: Target is unreasonably conservative. Smart Bidding
    is bidding as if any return is acceptable. CPC is inflated.
    Fix: Raise target significantly, or switch to Max Conv Value
    and re-evaluate what ROAS is achievable.
```

### Step 4: Product/Service-Level ROAS Variation

tROAS works best when there is meaningful variation in conversion values. Analyze the spread:

**AOV Distribution Analysis:**
```
Coefficient of Variation (CV) = StdDev(order_values) / Mean(order_values)

CV < 0.10: Very low variation. All orders are similar value.
           tROAS adds minimal benefit over tCPA. Consider switching
           to tCPA for simpler optimization.

CV 0.10-0.30: Moderate variation. tROAS can differentiate between
              low and high-value prospects. Good fit.

CV 0.30-0.60: High variation. tROAS is highly valuable here.
              The algorithm can prioritize high-value transactions.
              Ensure conversion values are accurate.

CV > 0.60: Very high variation. tROAS is essential but needs more
           data. Ensure you have 50+ conversions/month and that
           outlier values (very high or very low) are legitimate.
```

**Product Category ROAS Breakdown:**
For Shopping and PMax campaigns, analyze ROAS by product category:
- Which categories drive the highest ROAS?
- Which categories drag ROAS down?
- Should low-ROAS categories be split into a separate campaign with different targets?
- Are high-ROAS categories getting enough budget allocation?

**New vs Returning Customer ROAS:**
- New customer ROAS is typically 30-50% lower than returning customer ROAS
- If a campaign is heavy on new customer acquisition, a lower tROAS target is appropriate
- Consider separate campaigns (or audience segments) for new vs returning customers

### Step 5: tROAS Optimization Strategy

**Ratcheting Up (improving returns):**
1. Confirm actual ROAS has met or exceeded target for 2+ consecutive weeks
2. Increase target by no more than 10-15% at a time
3. Wait 14 days before next adjustment
4. Monitor conversion volume — if it drops > 20%, the target is too high
5. Stop ratcheting when volume begins to decline meaningfully

**Ratcheting Down (increasing volume):**
1. If ROAS target is above actual ROAS and volume is limited
2. Decrease target by 15-20%
3. Wait 14 days — volume should increase
4. Continue until you find the volume/efficiency equilibrium

**Seasonal ROAS Adjustments:**
- E-commerce Q4 (Nov-Dec): ROAS naturally higher due to holiday purchasing intent. Raising target slightly is appropriate.
- Post-holiday Q1 (Jan-Feb): ROAS typically drops. Lower target proactively or Smart Bidding will throttle spend.
- Sales/promotion periods: Lower target temporarily — discounted prices mean lower per-order value but higher volume.

### Step 6: tROAS vs tCPA Decision

Sometimes accounts on tROAS should switch to tCPA. Evaluate:

**Switch to tCPA if:**
- All conversions have the same (or very similar) value
- Revenue tracking is unreliable and can't be fixed quickly
- Conversion volume is 30-49/month (insufficient for tROAS but okay for tCPA)
- The business optimizes for lead volume, not revenue (B2B lead gen)

**Stay on tROAS if:**
- Product/service values vary meaningfully (CV > 0.15)
- Revenue tracking is accurate and validated
- 50+ conversions/month with value data
- Business goal is revenue or ROAS, not CPA

## Output Format

```
## tROAS Analysis Results

### Revenue Tracking Validation
- Tracking method: [Dynamic/Static]
- Value accuracy: [X% match vs backend]
- Issues found: [List any tracking problems]

### Campaign Analysis
[Per-campaign tROAS assessment]

### Product/Category ROAS Breakdown
[ROAS by product category or service type]

### Target Optimization Plan
[Per-campaign ratcheting timeline]

### Recommendations
1. [Revenue tracking fixes needed]
2. [Target adjustments]
3. [Campaign structure changes]
4. [Strategy switches (tROAS -> tCPA where appropriate)]
```
