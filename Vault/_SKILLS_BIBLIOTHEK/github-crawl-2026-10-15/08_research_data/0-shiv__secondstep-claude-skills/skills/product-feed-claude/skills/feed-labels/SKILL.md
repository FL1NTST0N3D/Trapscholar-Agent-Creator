# Feed Custom Labels Skill

## Command
`/feed labels`

## Overview

Custom labels (custom_label_0 through custom_label_4) are the most underused feature in Google Merchant Center. They let you tag products with any classification you choose, then use those labels to segment products into different Shopping and PMax campaign structures with differentiated bidding, budgets, and targets.

Without custom labels, you are forced to segment by Google product category or brand alone — blunt instruments that do not reflect your actual business priorities. Custom labels let you segment by profit margin, seasonality, bestseller status, price tier, and clearance status — the dimensions that actually determine how much a click is worth to your business.

You have 5 custom label slots (0-4). Each accepts a text value up to 100 characters. Plan your label strategy before implementation — changing labels after campaigns are structured requires rebuilding campaign segmentation.

## Custom Label Strategy Templates

### Label 0: Profit Margin Tier
Segment by margin to bid aggressively on high-margin products and conservatively on low-margin:

| Value | Definition | Bidding Strategy |
|---|---|---|
| `high_margin` | Margin > 50% | Maximize Conversions, aggressive tCPA |
| `medium_margin` | Margin 25-50% | Target ROAS 300-500% |
| `low_margin` | Margin < 25% | Target ROAS 600%+, or exclude from paid |
| `loss_leader` | Margin < 10% or negative | Exclude from Shopping, use for free listings only |

### Label 1: Product Performance
Classify by historical sales velocity:

| Value | Definition | Bidding Strategy |
|---|---|---|
| `bestseller` | Top 20% by revenue (last 90 days) | Highest budget allocation, maximize volume |
| `strong_performer` | Top 21-50% by revenue | Standard budget, target ROAS |
| `underperformer` | Bottom 50% by revenue | Lower bids, test with limited budget |
| `new_arrival` | Listed < 30 days, no sales data | Separate campaign for learning period |
| `zombie` | Zero sales in 90+ days, still in stock | Review for exclusion or price adjustment |

### Label 2: Seasonality
Tag products by their peak demand season:

| Value | Definition | When to Boost |
|---|---|---|
| `spring` | Spring seasonal products | Feb-Apr |
| `summer` | Summer seasonal products | May-Jul |
| `fall` | Fall seasonal products | Aug-Oct |
| `holiday` | Holiday/gift products | Nov-Dec |
| `evergreen` | Year-round demand | Always on |
| `back_to_school` | School supplies, dorm items | Jul-Sep |
| `valentines` | Gifts, flowers, jewelry | Jan-Feb |

### Label 3: Price Tier
Segment by price point for different campaign strategies:

| Value | Definition | Strategy |
|---|---|---|
| `premium` | > $200 | Longer consideration, higher CPA tolerance |
| `mid_range` | $50-$200 | Standard Shopping campaigns |
| `value` | $15-$49 | Volume-focused, lower CPA targets |
| `impulse` | < $15 | Free listings + low-bid Shopping |

### Label 4: Inventory / Lifecycle Status
Track product lifecycle and stock levels:

| Value | Definition | Action |
|---|---|---|
| `full_stock` | > 50 units available | Standard bidding |
| `low_stock` | 10-50 units remaining | Consider pausing or reducing bids |
| `clearance` | Marked for clearance | Aggressive bidding to move inventory |
| `discontinued` | No restock planned | Exclude when < 5 units remain |
| `preorder` | Not yet available | Separate campaign, awareness focus |

## Implementation Process

### Step 1: Audit Current Labels
Check existing custom_label_0 through custom_label_4:
1. Which labels are currently populated?
2. What values are being used?
3. Are values consistent (no misspellings, no mixed casing)?
4. Are any labels unused (opportunity to add a new dimension)?

### Step 2: Define Label Strategy
Based on business goals, assign each label slot:
1. Map each label (0-4) to a business dimension
2. Define the exact values for each label (keep to 3-7 values per label)
3. Document the definitions so team members apply labels consistently
4. Use lowercase_with_underscores for values (consistent, no whitespace issues)

### Step 3: Populate Labels in Feed
Methods to populate custom labels:
- **In-feed rules (MC):** Set up rules in Merchant Center to auto-assign labels based on other attributes (price ranges, categories, brands)
- **Supplemental feed:** Upload a supplemental feed with just `id` and `custom_label_X` columns
- **Feed management tool:** DataFeedWatch, Feedonomics, or GoDataFeed can auto-classify
- **CMS plugin:** Many Shopify/WooCommerce feed plugins support custom label mapping
- **Script:** Use `feed_analyzer.py` to generate label assignments from feed data

### Step 4: Build Campaign Structure Around Labels
Once labels are in the feed:
1. Create separate PMax asset groups or Shopping campaigns per label value
2. Set differentiated tROAS or tCPA targets by segment
3. Allocate budget proportionally to expected return
4. Monitor performance by label to validate the segmentation strategy

### Step 5: Ongoing Maintenance
Labels are not set-and-forget:
- **Monthly:** Re-classify bestsellers vs underperformers based on latest 90-day data
- **Quarterly:** Review seasonality labels and update for upcoming season
- **On price change:** Update price tier labels when prices shift significantly
- **On new products:** Assign all 5 labels before the product goes live

## Scoring Criteria

Score feed label readiness 0-100:

| Score Range | Classification | Criteria |
|---|---|---|
| 90-100 | Excellent | All 5 labels populated, consistent values, mapped to campaign structure |
| 70-89 | Good | 3-4 labels populated, mostly consistent, some campaign segmentation |
| 50-69 | Partial | 1-2 labels populated, or inconsistent values needing cleanup |
| 0-49 | Not Using | No custom labels, or labels populated with meaningless/random values |

## Output Format

```
CUSTOM LABEL ANALYSIS
=====================
Total Products: [count]

LABEL UTILIZATION:
  custom_label_0: [filled]% populated — [dimension or "UNUSED"]
  custom_label_1: [filled]% populated — [dimension or "UNUSED"]
  custom_label_2: [filled]% populated — [dimension or "UNUSED"]
  custom_label_3: [filled]% populated — [dimension or "UNUSED"]
  custom_label_4: [filled]% populated — [dimension or "UNUSED"]

VALUE DISTRIBUTION (per label):
  custom_label_0:
    high_margin: [count] products ([pct]%)
    medium_margin: [count] products ([pct]%)
    low_margin: [count] products ([pct]%)
    [unlabeled]: [count] products ([pct]%)

DATA QUALITY ISSUES:
- [count] products with inconsistent casing in label values
- [count] products with label values not in defined set
- [count] unused label slots (opportunity for segmentation)

RECOMMENDATIONS:
1. Assign [label slot] to [dimension] — enables [strategy]
2. Fix [count] inconsistent values in [label] — standardize to [values]
3. Reclassify [count] products in [label] based on updated [metric]
```

## Common Mistakes

| Mistake | Impact | Fix |
|---|---|---|
| Using labels for data already in other attributes | Wasted label slot | Use labels for business dimensions only (margin, performance, season) |
| Too many values per label (20+) | Unmanageable campaign structure | Keep to 3-7 values per label |
| Inconsistent casing (High_Margin vs high_margin) | Broken campaign filters | Standardize to lowercase_with_underscores |
| Never updating labels | Stale segmentation, wrong bids | Monthly refresh for performance labels |
| Not mapping labels to campaigns | Labels exist but unused | Build campaign structure that leverages labels |

## Impact
- **+20% ROAS** from margin-based bid differentiation
- **+30% revenue** during seasonal peaks with season-tagged products
- **-15% wasted spend** by excluding or limiting low-margin products
- **+25% efficiency** from bestseller vs zombie product separation

## Author
Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | Second Step
