# Bid Management Scripts

## Command: `/script bids`

## Overview

Bid management scripts automate the tedious process of adjusting bids based on performance data. While Smart Bidding handles this for many advertisers, there are scenarios where manual or script-based bidding is superior: low-volume accounts, specific dayparting strategies, geographic bid optimization, or accounts where Smart Bidding consistently underperforms.

These scripts analyze conversion data across dimensions (hour of day, device, geography) and apply bid modifiers based on actual performance. They bridge the gap between fully manual bidding and fully automated Smart Bidding, giving you control with data-driven precision.

## Script Templates

### 1. Hourly Bid Adjustments (Dayparting)
Analyzes conversion performance by hour of day over the last 30 days and sets ad schedule bid modifiers. Hours with high conversion rates get bid increases; hours with low performance get decreases.

**Key Configuration:**
- `LOOKBACK_DAYS` — Days of data to analyze (default: 30)
- `MIN_CLICKS` — Minimum clicks in an hour slot to make adjustments (default: 20)
- `MAX_BID_INCREASE` — Maximum upward modifier (default: 1.40 = +40%)
- `MAX_BID_DECREASE` — Maximum downward modifier (default: 0.60 = -40%)
- `CAMPAIGN_LABEL` — Only adjust campaigns with this label (optional)

**How it works:**
1. Queries hourly performance report for the lookback period
2. Calculates conversion rate by hour across the account
3. Compares each hour's CVR to the account average
4. Sets bid modifiers proportional to the deviation from average
5. Caps modifiers at MAX_BID_INCREASE and MAX_BID_DECREASE

### 2. Device Bid Adjustments
Analyzes performance by device type (desktop, mobile, tablet) and sets device bid modifiers at the campaign level. Uses conversion value and ROAS as the primary optimization signal.

**Key Configuration:**
- `TARGET_ROAS` — Your target return on ad spend
- `LOOKBACK_DAYS` — Days of data to analyze (default: 30)
- `MIN_COST` — Minimum spend on a device to make adjustments (default: $50)

**How it works:**
1. Queries device-level performance for each campaign
2. Calculates ROAS by device: conversion value / cost
3. Compares device ROAS to TARGET_ROAS
4. Sets device modifiers: if mobile ROAS is 2x target, increase mobile bid modifier
5. Logs all changes to Logger for auditing

### 3. Geo Bid Adjustments
Optimizes location bid modifiers based on conversion performance by geographic area. Works at the state, metro, or city level depending on data volume.

**Key Configuration:**
- `GEO_LEVEL` — "State", "Metro", or "City"
- `TARGET_CPA` — Target cost per acquisition
- `MIN_CONVERSIONS` — Minimum conversions in a geo to adjust (default: 5)
- `MAX_MODIFIER` — Maximum bid modifier change (default: 0.50 = +/-50%)

**How it works:**
1. Queries geographic performance report
2. Calculates CPA by location
3. Locations with CPA below target get bid increases
4. Locations with CPA above target get bid decreases
5. Locations with insufficient data are left unchanged

### 4. ROAS-Based Keyword Bidding
Adjusts keyword-level bids based on individual keyword ROAS. High-ROAS keywords get bid increases; low-ROAS keywords get decreases; zero-conversion keywords with sufficient spend get bid reductions.

**Key Configuration:**
- `TARGET_ROAS` — Target return on ad spend
- `HIGH_ROAS_MULTIPLIER` — Bid increase for keywords exceeding target (default: 1.15)
- `LOW_ROAS_MULTIPLIER` — Bid decrease for keywords below target (default: 0.85)
- `ZERO_CONV_SPEND_THRESHOLD` — Spend threshold for zero-conversion keywords to lower bids
- `MIN_BID` — Floor bid to never go below (default: $0.10)
- `MAX_BID` — Ceiling bid to never exceed (default: $50.00)

## Best Practices

- **Use sufficient data**: Never adjust bids with fewer than 20 clicks or 3 conversions per segment. Small sample sizes lead to noisy, unreliable adjustments.
- **Apply changes incrementally**: Limit bid changes to 15-20% per adjustment cycle. Drastic changes cause auction volatility.
- **Run weekly, not daily**: Bid adjustment scripts should run weekly to accumulate enough data between runs. Daily runs on low-volume accounts create noise.
- **Exclude Smart Bidding campaigns**: These scripts are for manual CPC or Enhanced CPC campaigns only. Smart Bidding campaigns manage their own bids.
- **Set bid floors and ceilings**: Always configure MIN_BID and MAX_BID to prevent runaway bids in either direction.
- **Log everything**: Write all bid changes to Logger or a Google Sheet for auditing and rollback capability.
- **Test on a single campaign first**: Apply to one campaign, monitor for 2 weeks, then roll out to the full account.

## Common Pitfalls

1. **Stacking modifiers**: Hour + device + geo modifiers multiply together. A +40% hour modifier combined with +30% device modifier results in +82% total adjustment. Be conservative with each individual modifier.
2. **Smart Bidding conflicts**: Applying bid scripts to Smart Bidding campaigns causes erratic behavior. Always filter by bidding strategy type.
3. **Seasonal data**: A 30-day lookback during a promotional period will skew all bid adjustments. Consider using a longer lookback or excluding promo dates.
4. **New campaigns**: Don't apply bid scripts to campaigns less than 2 weeks old — not enough data to be meaningful.
5. **Currency formatting**: Bids must be set in the account's currency. Always use micros for API operations.

## GAQL Queries Used

```sql
-- Hourly performance
SELECT segments.hour, metrics.clicks, metrics.conversions, metrics.cost_micros
FROM campaign
WHERE segments.date DURING LAST_30_DAYS

-- Device performance
SELECT segments.device, campaign.name, metrics.cost_micros, metrics.conversions_value
FROM campaign
WHERE segments.date DURING LAST_30_DAYS

-- Geographic performance
SELECT geographic_view.country_criterion_id, geographic_view.location_type,
       metrics.cost_micros, metrics.conversions
FROM geographic_view
WHERE segments.date DURING LAST_30_DAYS
```

## Template Reference

See `templates/bid-adjustments.js` for the complete hourly bid adjustment script.
