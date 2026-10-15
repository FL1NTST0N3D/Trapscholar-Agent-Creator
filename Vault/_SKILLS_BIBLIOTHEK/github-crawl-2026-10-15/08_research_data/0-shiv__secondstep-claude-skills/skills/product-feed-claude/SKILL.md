# Product Feed Claude — Master Skill

## Overview

This is the master skill for Google Merchant Center product feed optimization. It coordinates 8 specialized sub-skills that cover every aspect of feed quality — from title formulas and image compliance to disapproval resolution and custom label strategy.

Feed quality is the single largest determinant of Shopping and Performance Max campaign performance. Google uses your feed data to match products to search queries, render Shopping ads, and determine auction eligibility. A feed with missing attributes, weak titles, or policy violations will bleed budget and suppress impressions.

## How It Works

When a user runs `/feed audit`, this master skill orchestrates a full analysis:

1. **Parse the feed** — Read CSV, TSV, or XML feed files from the `feed/` directory
2. **Validate structure** — Check for required attributes (id, title, description, link, image_link, availability, price, brand, gtin, condition)
3. **Score each product** — Rate title quality, description completeness, image compliance, and attribute coverage
4. **Flag issues** — Identify disapproval risks, missing data, and optimization opportunities
5. **Generate report** — Produce a prioritized action plan with estimated impact

## Sub-Skills

### 1. Feed Title Optimization (`/feed titles`)
Optimizes product titles using the proven formula: **Brand + Product Type + Key Attributes** (color, size, material). Titles are the #1 factor in Shopping ad relevance. Maximum 150 characters, but only 75 are visible in Shopping ads — front-loading keywords is critical. Includes category-specific templates for apparel, electronics, home goods, and more.

### 2. Feed Description (`/feed descriptions`)
Writes and audits product descriptions for keyword richness and policy compliance. Maximum 5,000 characters. Descriptions must include key features, specifications, and benefits while avoiding promotional language (sale, free shipping, limited time). Natural keyword integration without stuffing.

### 3. Feed Images (`/feed images`)
Audits product images against Google's requirements: minimum 100x100px (250x250 for apparel), no watermarks or promotional overlays, clean/white background preferred, product filling 75-90% of the frame. Flags common violations and recommends fixes.

### 4. Feed Attributes (`/feed attributes`)
Validates required and recommended attribute completeness. Required: id, title, description, link, image_link, availability, price, brand, gtin, condition. Recommended: color, size, material, pattern, gender, age_group, item_group_id. Missing recommended attributes suppress impressions.

### 5. Feed Custom Labels (`/feed labels`)
Configures 5 custom labels (custom_label_0 through custom_label_4) for campaign segmentation. Strategy templates: profit margin tiers, best sellers, seasonal products, price ranges, and new arrivals. Enables differentiated bidding and budget allocation in PMax and Shopping campaigns.

### 6. Feed Disapprovals (`/feed disapprovals`)
Diagnoses and fixes common disapproval reasons: price mismatch (website vs feed), availability mismatch, missing GTIN/MPN, policy violations (prohibited content, misrepresentation), landing page errors (404, redirect chains), and image quality failures.

### 7. Feed Supplemental (`/feed supplemental`)
Sets up supplemental feed strategy for title overrides, attribute enrichment, promotion feeds (sale_price, promotion_id), and local inventory ads. Supplemental feeds let you override primary feed data without modifying your CMS or data pipeline.

### 8. Feed Report (`/feed report`)
Generates a comprehensive feed health report: approval rate, attribute completeness percentage, title quality score (0-100), image compliance rate, and prioritized optimization recommendations with estimated CTR and impression impact.

## Feed Quality Scoring

The master skill uses a weighted scoring model:

| Factor | Weight | What's Measured |
|---|---|---|
| Title Quality | 30% | Keyword placement, length, formula adherence |
| Attribute Completeness | 25% | Required + recommended attributes filled |
| Image Compliance | 20% | Size, background, overlay violations |
| Description Quality | 15% | Length, keyword density, policy compliance |
| Data Accuracy | 10% | Price/availability match, valid GTINs |

**Score Bands:**
- 90-100: Excellent — feed is well-optimized
- 70-89: Good — minor improvements available
- 50-69: Needs Work — significant gaps affecting performance
- Below 50: Critical — major issues causing disapprovals and lost impressions

## Usage

```
# Full feed audit
/feed audit

# Optimize specific aspect
/feed titles
/feed descriptions
/feed images
/feed attributes
/feed labels
/feed disapprovals

# Set up supplemental feed
/feed supplemental

# Generate health report
/feed report
```

## Integration

This skill works with:
- **Google Merchant Center** — primary feed source
- **Google Ads** — Shopping and PMax campaigns
- **Shopify / WooCommerce / BigCommerce** — CMS feed exports
- **DataFeedWatch / Feedonomics / GoDataFeed** — feed management tools

## Author

Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)
