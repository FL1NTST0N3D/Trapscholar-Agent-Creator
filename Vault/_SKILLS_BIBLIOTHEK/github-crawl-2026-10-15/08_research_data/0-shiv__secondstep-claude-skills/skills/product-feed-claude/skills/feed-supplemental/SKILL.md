# Feed Supplemental Skill

## Command
`/feed supplemental`

## Overview

Supplemental feeds are the power user's best tool for feed optimization. They let you override, enrich, or add attributes to your primary feed without modifying your CMS, data pipeline, or ecommerce platform. This is critical when your primary feed comes from a platform like Shopify or WooCommerce where you have limited control over the feed export format.

A supplemental feed is simply a file (CSV, TSV, or Google Sheets) that contains product IDs and the attributes you want to override or add. Google merges it with your primary feed — supplemental data takes precedence for any attribute you include. You can have up to 100 supplemental feeds per Merchant Center account.

Supplemental feeds cannot add new products — they can only modify products that already exist in the primary feed.

## Use Cases

### 1. Title Overrides
Override weak CMS-generated titles with optimized titles without touching your ecommerce platform:

| Primary Feed Title | Supplemental Title |
|---|---|
| Blue Shirt | Ralph Lauren Men's Oxford Shirt Blue Slim Fit Large |
| Laptop Computer | Dell Inspiron 15 Laptop Intel i5 8GB RAM 256GB SSD |
| Face Cream | CeraVe Moisturizing Cream 16oz Fragrance-Free for Dry Skin |

### 2. Attribute Enrichment
Add missing attributes that your CMS does not export:

| Attribute | Source | Example |
|---|---|---|
| `google_product_category` | Manual classification | 166 (Apparel > Shoes) |
| `product_highlight` | Marketing copy | "Waterproof", "Machine Washable", "Organic Cotton" |
| `custom_label_0` through `4` | Business data | "high_margin", "bestseller", "summer" |
| `product_type` | Your taxonomy | "Clothing > Men > Shirts > Oxford" |
| `material` | Product specs | "100% Cotton" |
| `color` | Product data | "Navy Blue" |

### 3. Promotional Pricing
Apply sale prices and promotion IDs without modifying your product catalog:

```csv
id,sale_price,sale_price_effective_date,promotion_id
SKU-001,19.99 USD,2026-03-15T00:00:00-05:00/2026-03-31T23:59:59-05:00,SPRING_SALE
SKU-002,49.99 USD,2026-03-15T00:00:00-05:00/2026-03-31T23:59:59-05:00,SPRING_SALE
```

### 4. Local Inventory Ads
Add store-level inventory data for local Shopping ads:

| Attribute | Purpose |
|---|---|
| `store_code` | Identifies the physical store |
| `quantity` | Units available at that store |
| `price` | Store-specific price (if different from online) |
| `pickup_method` | `buy`, `reserve`, `ship_to_store`, `not_supported` |
| `pickup_sla` | `same_day`, `next_day`, `2-day`, `3-day`, `4-day`, `5-day`, `6-day`, `multi-week` |

### 5. A/B Testing
Test optimized feed data against current data:
1. Create a supplemental feed with optimized titles/descriptions for 50% of products
2. Run for 2-4 weeks
3. Compare CTR, impressions, and conversions between test and control groups
4. Roll out winners to the primary feed

### 6. Feed Rule Workarounds
When Merchant Center feed rules cannot achieve the transformation you need:
- Complex conditional logic (if category = X AND price > Y, set label to Z)
- Lookups against external data (margin from ERP, bestseller status from analytics)
- Multi-attribute transformations (combine brand + category + color into a new field)

## Setup Process

### Step 1: Create the Supplemental Feed File
Structure your file with `id` as the first column, plus only the attributes you want to override:

```csv
id,title,custom_label_0,custom_label_1,google_product_category
SKU-001,"Nike Men's Air Max 90 Running Shoes Black Size 10",high_margin,bestseller,187
SKU-002,"Adidas Women's Ultraboost 22 White Size 8",medium_margin,strong_performer,187
```

Rules:
- **id column is mandatory** — must match the `id` in your primary feed exactly
- Only include columns you want to override — omitted columns are untouched
- Empty values in supplemental feed will NOT clear primary feed values
- Use the same delimiter and encoding as your primary feed

### Step 2: Upload to Merchant Center
1. Go to Merchant Center > Feeds > Supplemental feeds
2. Click the "+" button to add a new supplemental feed
3. Choose upload method:
   - **Google Sheets** — best for small feeds, easy collaboration
   - **Scheduled fetch** — for automated updates from your server
   - **Upload** — manual CSV/TSV file upload
   - **Content API** — programmatic updates via API
4. Link the supplemental feed to your primary feed

### Step 3: Map the Feed
After upload, Merchant Center shows a mapping preview:
1. Verify the `id` column maps to your primary feed IDs
2. Check that attribute names match Google's expected field names
3. Review sample merged data to confirm overrides are correct
4. Submit the feed

### Step 4: Verify Merge Results
After processing (usually 15-30 minutes):
1. Go to Products > All products
2. Click on a product that should be overridden
3. Check the "Feed" tab to see which values come from primary vs supplemental
4. Verify the correct data is showing in the "Active" view
5. Check Diagnostics for any new errors introduced by the supplemental data

## Scoring Criteria

Score supplemental feed strategy 0-100:

| Score Range | Classification | Criteria |
|---|---|---|
| 90-100 | Excellent | Supplemental feeds actively used for title optimization, labels, and enrichment |
| 70-89 | Good | At least one supplemental feed for attribute enrichment or labels |
| 50-69 | Basic | Supplemental feed exists but only used for minor fixes |
| 0-49 | Unused | No supplemental feeds configured, all optimization blocked by CMS limitations |

## Output Format

```
SUPPLEMENTAL FEED ANALYSIS
===========================
Primary Feed Products: [count]
Supplemental Feeds Active: [count]

PER SUPPLEMENTAL FEED:
  Feed: [name]
  Type: [Google Sheets / Scheduled Fetch / Upload]
  Products Covered: [count] / [total] ([pct]%)
  Attributes Overridden: [list]
  Last Updated: [date]
  Status: [Processing / Active / Error]

COVERAGE GAPS:
- [count] products have weak titles not covered by title override feed
- [count] products missing custom labels (no label supplemental feed)
- [count] products missing google_product_category

RECOMMENDATIONS:
1. Create [type] supplemental feed for [purpose] — covers [count] products
2. Add [attribute] column to existing [feed name] — enriches [count] products
3. Increase refresh frequency of [feed name] to [frequency] — prevents stale data
```

## Best Practices

1. **Use Google Sheets for small, manually managed feeds** — easy to edit, version-controlled
2. **Use scheduled fetch for automated feeds** — connect to your data pipeline
3. **Keep supplemental feeds focused** — one feed per purpose (titles, labels, promotions)
4. **Document which attributes come from which feed** — prevents confusion when debugging
5. **Test before full rollout** — override a small batch first, verify in MC, then expand
6. **Monitor processing errors** — supplemental feed errors are silent; check MC Diagnostics regularly
7. **Refresh schedule** — promotional feeds need daily refresh; label feeds can be weekly

## Common Mistakes

| Mistake | Impact | Fix |
|---|---|---|
| ID mismatch between primary and supplemental | Override fails silently | Ensure exact ID match (case-sensitive) |
| Including all attributes in supplemental | Unnecessary complexity | Only include attributes you are overriding |
| Stale supplemental data | Overrides become incorrect | Set appropriate refresh schedules |
| Not checking merge results | Bad data goes live | Always verify merged product data in MC |
| Using supplemental to "fix" primary feed permanently | Dependency on manual process | Fix root cause in CMS/primary feed when possible |

## Impact
- **+35% attribute coverage** from enrichment supplemental feeds
- **+20-40% CTR** from title override supplemental feeds
- **Unblocks optimization** when CMS changes are slow or impossible
- **Enables A/B testing** without touching production systems

## Author
Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | Second Step
