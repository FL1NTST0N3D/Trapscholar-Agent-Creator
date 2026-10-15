# Feed Attributes Skill

## Command
`/feed attributes`

## Overview

Google Merchant Center requires specific product attributes to list your products in Shopping ads and free listings. Missing required attributes result in immediate disapproval. Missing recommended attributes silently suppress your impressions — Google simply shows competitors with more complete data instead of your products. Attribute completeness directly correlates with impression volume: merchants with 90%+ attribute fill rates see 25-40% more impressions than those at 60-70%.

This skill validates every attribute in your feed against Google's current requirements, scores completeness, and identifies exactly which attributes to add for maximum impression lift.

## Required Attributes

Every product must have these attributes or it will be disapproved:

| Attribute | Field Name | Requirements |
|---|---|---|
| ID | `id` | Unique, max 50 chars, stable (never reuse IDs) |
| Title | `title` | Max 150 chars, no promotional text |
| Description | `description` | Max 5,000 chars, no HTML |
| Link | `link` | HTTPS preferred, must resolve to product page |
| Image Link | `image_link` | Direct URL to main product image |
| Availability | `availability` | `in_stock`, `out_of_stock`, or `preorder` |
| Price | `price` | Number + ISO 4217 currency code (e.g., `29.99 USD`) |
| Brand | `brand` | Required unless GTIN is provided |
| GTIN | `gtin` | UPC, EAN, JAN, or ISBN-13. Required for all products with a GTIN assigned by the manufacturer |
| Condition | `condition` | `new`, `refurbished`, or `used` |
| MPN | `mpn` | Required only if no GTIN exists |

### Conditional Requirements

These attributes are required for specific product categories:

| Attribute | Required When | Values |
|---|---|---|
| `gender` | Apparel & Accessories | `male`, `female`, `unisex` |
| `age_group` | Apparel & Accessories | `newborn`, `infant`, `toddler`, `kids`, `adult` |
| `color` | Apparel & Accessories | Actual color name, max 100 chars |
| `size` | Apparel (all), Shoes | Standard sizing (S, M, L, 10, 32x30) |
| `item_group_id` | Product variants | Same group ID for all variants of one product |
| `shipping_weight` | When using account shipping | Weight + unit (e.g., `2.5 lb`) |
| `tax` | US-targeted feeds without account-level tax | Tax rate by region |
| `multipack` | Manufacturer-defined multipacks | Number of identical products in the pack |
| `is_bundle` | Custom bundles | `true` or `false` |

## Recommended Attributes

Not required, but each one you add increases impression eligibility:

| Attribute | Field Name | Impact |
|---|---|---|
| Additional Images | `additional_image_link` | +15% CTR (multiple angles) |
| Sale Price | `sale_price` | Enables strikethrough pricing in ads |
| Product Type | `product_type` | Your own category taxonomy, helps relevance |
| Google Category | `google_product_category` | Google's taxonomy ID, improves matching |
| Material | `material` | Helps match material-specific queries |
| Pattern | `pattern` | Solid, striped, plaid, floral, etc. |
| Size Type | `size_type` | `regular`, `petite`, `plus`, `tall`, `big`, `maternity` |
| Size System | `size_system` | `US`, `UK`, `EU`, `AU`, etc. |
| Product Detail | `product_detail` | Additional structured specifications |
| Product Highlight | `product_highlight` | Up to 10 bullet-point highlights, 150 chars each |
| Energy Label | `energy_efficiency_class` | Required in EU for appliances |
| Shipping | `shipping` | Product-level shipping overrides |
| Return Policy | `return_policy_label` | Links to return policy configured in MC |
| Loyalty Points | `loyalty_points` | Points earned on purchase (Japan only) |

## Validation Process

### Step 1: Required Attribute Check
For every product in the feed:
1. Verify all 10 required attributes are present and non-empty
2. Validate format (price has currency code, availability uses exact enum values)
3. Check ID uniqueness — no duplicate IDs in the feed
4. Verify GTIN checksum validity (last digit is a check digit)
5. Confirm links resolve (HTTP 200, no redirect chains)

### Step 2: Conditional Attribute Check
Based on `google_product_category` or `product_type`:
1. If apparel/accessories: require gender, age_group, color, size
2. If variants exist: require item_group_id on all variants
3. If multipack: require multipack count
4. If bundle: require is_bundle = true

### Step 3: Recommended Attribute Completeness
Score the fill rate of recommended attributes:
- Count how many of the 14 recommended attributes are populated
- Calculate percentage: `filled / applicable * 100`
- Flag products below 50% recommended fill rate

### Step 4: Data Quality Validation
Beyond presence, check data quality:
- **Price:** Must be > 0, must match landing page price (within tolerance)
- **GTIN:** Must pass check-digit validation (Luhn for UPC, modulo for EAN)
- **Availability:** Must match landing page (in_stock product must be purchasable)
- **Color:** Must be a real color name (not "Style A" or "Option 1")
- **Size:** Must follow standard conventions (not "Regular" for a shoe size)

## Scoring Criteria

Score each product 0-100 for attribute completeness:

| Score Range | Classification | Criteria |
|---|---|---|
| 90-100 | Excellent | All required + 80%+ recommended attributes filled, valid data |
| 70-89 | Good | All required + 50-79% recommended, minor data quality issues |
| 50-69 | Needs Work | All required present but some recommended missing, or data quality issues |
| 30-49 | Poor | Missing conditional required attributes, < 50% recommended |
| 0-29 | Critical | Missing core required attributes — product will be disapproved |

## Output Format

```
FEED ATTRIBUTE REPORT
=====================
Total Products: [count]
Required Attributes Complete: [count] / [total] ([percentage]%)
Conditional Attributes Complete: [count] / [applicable] ([percentage]%)
Recommended Fill Rate: [percentage]%
Overall Score: [0-100]

CRITICAL ISSUES (will cause disapproval):
- [count] products missing [attribute]
- [count] products with invalid GTIN
- [count] products with price = 0

WARNINGS (suppressing impressions):
- [count] products missing google_product_category
- [count] products without additional_image_link
- [count] apparel products missing size

TOP RECOMMENDATIONS:
1. Add [attribute] to [count] products — estimated +[X]% impressions
2. Fix [attribute] on [count] products — prevents [count] disapprovals
3. Enrich [attribute] for [category] products — +[X]% relevance
```

## Common Mistakes

| Mistake | Impact | Fix |
|---|---|---|
| Reusing product IDs | Historical data loss | Use permanent, unique SKU-based IDs |
| Price without currency | Disapproval | Always include ISO 4217 code: `29.99 USD` |
| Generic brand value | Suppressed impressions | Use actual manufacturer brand name |
| Missing GTIN on branded products | Reduced visibility | Look up GTIN in manufacturer databases |
| `availability` = "Yes" | Disapproval | Use exact values: `in_stock`, `out_of_stock`, `preorder` |
| Color = "Multi" | Low relevance | List primary color: "Red/Blue" or "Multicolor" |

## Impact
- **+25-40% impressions** from complete recommended attributes
- **-50% disapprovals** from fixing required attribute issues
- **+15% CTR** from sale_price enabling strikethrough pricing
- **+20% query matching** from google_product_category and product_type

## Author
Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | Second Step
