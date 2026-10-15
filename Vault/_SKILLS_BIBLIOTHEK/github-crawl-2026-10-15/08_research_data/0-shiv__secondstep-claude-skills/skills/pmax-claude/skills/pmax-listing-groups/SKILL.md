---
name: pmax-listing-groups
description: "Audit Performance Max listing group structure, product feed health, product exclusions, and custom labels for Shopping-enabled PMax campaigns. Ensures optimal product segmentation and feed quality."
allowed-tools:
  - Bash
  - Read
  - Grep
---

# PMax Listing Groups Skill

## Purpose

For e-commerce PMax campaigns, listing groups determine which products appear in Shopping ads and how they're organized for bidding. A poorly structured listing group with feed quality issues can waste significant budget on low-performing products while underserving top performers. This skill audits feed health, listing group architecture, product exclusions, and custom label strategy.

## Trigger

Activated by `/pmax listings` or as part of `/pmax audit`.

## Data Requirements

Ask the user for:
1. Google Merchant Center feed export or feed summary
2. Listing group structure (from Google Ads > Asset Groups > Listing Group)
3. Product performance data (impressions, clicks, conversions by product/category)
4. Custom label definitions and assignment methodology
5. Product exclusion list
6. Feed disapproval/warning report from Merchant Center
7. Number of active products in feed

## Product Feed Health Audit

### Feed Quality Checklist

A healthy product feed is the foundation of PMax Shopping performance. Audit these attributes:

#### Required Attributes (Missing = Disapproval)
| Attribute | Requirement | Common Issues |
|---|---|---|
| `id` | Unique per product | Duplicates, missing |
| `title` | Max 150 chars, descriptive | Too short, keyword-stuffed, all caps |
| `description` | Max 5000 chars | Missing, too short (<100 chars), duplicate of title |
| `link` | Valid product page URL | 404s, redirects, HTTP (not HTTPS) |
| `image_link` | High-quality product image | Low resolution, watermarks, placeholder images |
| `availability` | in_stock / out_of_stock / preorder | Not synced with website, always "in_stock" |
| `price` | Currency + amount | Missing currency, price mismatch with website |
| `brand` | Brand name | Missing for non-private label, inconsistent formatting |
| `condition` | new / refurbished / used | Missing for applicable products |
| `gtin` | Global Trade Item Number | Missing (reduces visibility by 20-40%) |

#### Recommended Attributes (Missing = Reduced Performance)
| Attribute | Impact | Priority |
|---|---|---|
| `sale_price` | Triggers sale badge, higher CTR | High |
| `product_type` | Improves category matching | High |
| `google_product_category` | Required for some categories | High |
| `additional_image_link` | More images = higher engagement | Medium |
| `shipping` | Transparency improves conversion | Medium |
| `return_policy` | Builds trust, affects ad rank | Medium |
| `color`, `size`, `material` | Variant matching, filter eligibility | Medium |
| `custom_label_0` through `custom_label_4` | Segmentation for PMax | High |
| `ads_redirect` | Tracking URLs for analytics | Medium |

### Feed Quality Scoring

| Issue Category | Severity | Impact |
|---|---|---|
| Products disapproved | Critical | Products not showing at all |
| Missing GTINs | High | 20-40% lower visibility |
| Title quality (too short/generic) | High | Lower CTR, poor matching |
| Missing sale prices | Medium | Missing sale badge opportunities |
| Image quality issues | High | Lower CTR, potential disapproval |
| Price mismatches (feed vs. site) | Critical | Account suspension risk |
| Availability mismatches | High | Poor user experience, policy violation |
| Missing product descriptions | Medium | Reduced ad quality |

### Feed Freshness
- **Update frequency**: At minimum daily for e-commerce
- **Critical**: Price and availability must sync within 24 hours
- **Best practice**: Use Google Content API for real-time updates
- **Warning**: Manual feed uploads > weekly = stale data risk

## Listing Group Structure Analysis

### What Are Listing Groups?

Listing groups in PMax replace the "product groups" from Smart Shopping. They determine which products are included in an asset group and allow you to subdivide products for bidding organization.

### Structure Options

#### Flat Structure (All Products)
```
Asset Group
└── All Products (included)
```
- **When**: Small catalog (<50 products), all products similar in value
- **Risk**: No control over which products get priority
- **Verdict**: Usually suboptimal

#### Category-Based Structure
```
Asset Group
├── Category: Electronics (included)
│   ├── Sub: Laptops (included)
│   ├── Sub: Phones (included)
│   └── Sub: Accessories (excluded)
├── Category: Clothing (included)
└── Everything Else (excluded)
```
- **When**: Clear category hierarchy, different margins by category
- **Best for**: Large catalogs with diverse product types

#### Brand-Based Structure
```
Asset Group
├── Brand: Nike (included)
├── Brand: Adidas (included)
├── Brand: Puma (excluded — low margin)
└── Everything Else (excluded)
```
- **When**: Brand-level performance varies significantly
- **Best for**: Multi-brand retailers

#### Custom Label Structure
```
Asset Group: High Performers
├── Custom Label 0: "top-seller" (included)
└── Everything Else (excluded)

Asset Group: Mid Tier
├── Custom Label 0: "mid-tier" (included)
└── Everything Else (excluded)

Asset Group: Testing
├── Custom Label 0: "new-arrival" (included)
└── Everything Else (excluded)
```
- **When**: Performance-based segmentation needed
- **Best for**: Mature accounts with conversion data

### Listing Group Best Practices

1. **Always exclude "Everything Else"** unless you want ALL products in the group
2. **Create separate asset groups for different product segments** — each with tailored assets and audience signals
3. **Exclude low-performers and out-of-stock products** explicitly
4. **Match listing group segments to asset group creative** — shoe images for shoe products
5. **Use subdivision levels wisely** — 2-3 levels max for manageability
6. **Review listing group performance monthly** — subdivide or exclude based on data

## Product Exclusion Strategy

### Products to Exclude

| Exclude Category | Reason | Method |
|---|---|---|
| Out of stock items | Wasted clicks, poor UX | Feed availability attribute |
| Discontinued products | No conversion path | Feed exclusion or custom label |
| Low-margin products | Poor ROAS | Custom label "low-margin" → exclude |
| Products with <3 star reviews | Low conversion rate | Custom label based on review score |
| Seasonal products (off-season) | Low intent, wasted budget | Custom label "seasonal" + schedule |
| Products with feed errors | May cause disapproval cascade | Fix feed or exclude until fixed |
| Variants with low inventory | Backorder frustration | Feed availability or custom label |
| Loss-leader products | Attract wrong audience in PMax | Exclude from PMax, use in Search |

### Exclusion Audit Checklist
- [ ] Out-of-stock products excluded or availability synced
- [ ] Discontinued products removed from feed
- [ ] Low-ROAS products identified and excluded (or in separate asset group with lower targets)
- [ ] High-return-rate products flagged
- [ ] Seasonal products managed with scheduling
- [ ] "Everything Else" category excluded in listing groups

## Custom Labels Strategy

Custom labels (0-4) let you segment your product feed for PMax bidding and listing groups.

### Recommended Custom Label Schema

| Label | Purpose | Example Values |
|---|---|---|
| `custom_label_0` | Performance tier | "top-seller", "mid-tier", "new-arrival", "low-performer" |
| `custom_label_1` | Margin tier | "high-margin", "medium-margin", "low-margin" |
| `custom_label_2` | Seasonality | "evergreen", "spring", "summer", "fall", "winter", "holiday" |
| `custom_label_3` | Promotion status | "on-sale", "clearance", "full-price", "bundle" |
| `custom_label_4` | Priority / Test group | "priority-a", "priority-b", "test", "holdout" |

### Custom Label Assignment Rules

- **Performance tier**: Based on last 30/60/90 day conversion data
  - Top seller: >X conversions/month or top 20% by revenue
  - Mid tier: Average performance
  - Low performer: <Y conversions in 90 days, or high cost with no conversions
  - New arrival: Listed <30 days, insufficient data

- **Margin tier**: Based on COGS data
  - High margin: >40% gross margin
  - Medium margin: 20-40% gross margin
  - Low margin: <20% gross margin

- **Update frequency**: Weekly for performance tier, monthly for margin, seasonally for seasonality

## Scoring Rubric (0-100)

### Feed Health (0-40 points)

| Criteria | Points |
|---|---|
| No disapproved products | 10 |
| All required attributes populated | 8 |
| GTINs present for >80% of products | 5 |
| Titles optimized (50+ chars, descriptive) | 5 |
| Feed updated at least daily | 5 |
| No price/availability mismatches | 5 |
| Additional images present | 2 |

### Listing Group Structure (0-30 points)

| Criteria | Points |
|---|---|
| Products segmented (not "All Products" flat) | 10 |
| Segments match asset group creative/signals | 8 |
| "Everything Else" excluded or intentional | 5 |
| 2-3 subdivision levels (not too flat, not too deep) | 4 |
| Separate asset groups for distinct product categories | 3 |

### Product Exclusions (0-15 points)

| Criteria | Points |
|---|---|
| Out-of-stock products excluded | 5 |
| Low-performers identified and excluded/separated | 5 |
| Exclusion strategy documented and maintained | 3 |
| Seasonal products managed | 2 |

### Custom Labels (0-15 points)

| Criteria | Points |
|---|---|
| Custom labels implemented (at least 2) | 5 |
| Performance-based label exists | 4 |
| Margin-based label exists | 3 |
| Labels updated regularly (weekly/monthly) | 3 |

## Output Format

```
## Listing Group & Feed Health Audit Results

### Listing Group Score: XX/100

### Feed Health Summary
| Metric | Value | Status |
|---|---|---|
| Total products in feed | X | — |
| Active/approved products | X (Y%) | OK/WARNING |
| Disapproved products | X (Y%) | OK/CRITICAL |
| Products with GTINs | X (Y%) | OK/WARNING |
| Average title length | X chars | OK/WARNING |
| Feed update frequency | [daily/weekly/manual] | OK/WARNING |
| Price mismatches | X | OK/CRITICAL |

### Listing Group Structure
| Asset Group | Structure Type | Products Included | Products Excluded | Status |
|---|---|---|---|---|
| [name] | [flat/category/brand/label] | X | Y | OK/WARNING |

### Custom Labels
| Label | Implemented | Values | Products Tagged | Status |
|---|---|---|---|---|
| custom_label_0 | Yes/No | [values] | X% | OK/WARNING |

### Product Exclusion Review
- Out-of-stock excluded: YES/NO
- Low-performers excluded: YES/NO
- Total products excluded: X (Y% of feed)

### Critical Issues
- [List findings]

### Recommendations
1. [Prioritized action items]
```
