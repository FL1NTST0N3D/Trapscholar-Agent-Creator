# Feed Disapprovals Skill

## Command
`/feed disapprovals`

## Overview

Product disapprovals are the most damaging feed issue — a disapproved product cannot appear in Shopping ads or free listings at all. Google reports that 18% of products across all Merchant Center accounts are disapproved at any given time, and many merchants do not monitor their disapproval rates until campaign performance tanks.

Disapprovals fall into two categories: **data quality issues** (fixable by correcting feed data) and **policy violations** (require product or landing page changes). This skill diagnoses the root cause of each disapproval, provides the exact fix, and prioritizes resolution by revenue impact.

## Common Disapproval Reasons

### Data Quality Disapprovals

| Disapproval | Cause | Fix | Priority |
|---|---|---|---|
| **Missing required attribute** | id, title, description, link, image_link, price, availability, brand, or condition is empty | Populate the missing attribute in feed | Critical |
| **Invalid GTIN** | GTIN fails check-digit validation or is not found in GS1 database | Verify GTIN with manufacturer, correct or remove if invalid | High |
| **Price mismatch** | Feed price differs from landing page price | Sync feed price with website price, check for currency mismatches | Critical |
| **Availability mismatch** | Feed says `in_stock` but product is out of stock on website (or vice versa) | Sync availability with real-time inventory, increase feed refresh frequency | Critical |
| **Image too small** | Main image below 100x100px (250x250 for apparel) | Replace with higher resolution image | High |
| **Missing image** | `image_link` is empty or URL returns 404 | Add valid image URL | Critical |
| **Unsupported image format** | Image is SVG, AI, or other non-supported format | Convert to JPEG, PNG, or WebP | Medium |
| **Landing page error** | Product URL returns 404, 500, or redirect loop | Fix URL in feed or fix the landing page | Critical |
| **Duplicate ID** | Two products share the same `id` value | Ensure every product has a unique, stable ID | High |
| **Invalid price format** | Price missing currency code or formatted incorrectly | Use format: `29.99 USD` | High |

### Policy Disapprovals

| Disapproval | Cause | Fix | Priority |
|---|---|---|---|
| **Promotional text in image** | Image contains overlaid text like "Sale" or "50% Off" | Re-shoot or edit image to remove text | High |
| **Watermark in image** | Logo or copyright watermark on product image | Use clean image without watermarks | High |
| **Misrepresentation** | Product claims do not match reality (fake reviews, misleading claims) | Remove misleading claims from title, description, and landing page | Critical |
| **Prohibited content** | Products in prohibited categories (weapons, drugs, counterfeit goods) | Remove product from feed — cannot be fixed | Critical |
| **Restricted content** | Alcohol, gambling, healthcare products need additional verification | Apply for certification in MC, comply with regional requirements | High |
| **Insufficient product identifiers** | Branded product missing both GTIN and MPN | Add GTIN or MPN; if truly no identifier exists, set `identifier_exists` = `false` | Medium |
| **Automatic item updates conflict** | Google's automatic crawl finds different data than your feed | Ensure feed data matches landing page exactly | Medium |
| **Free shipping misrepresentation** | Feed or ad implies free shipping but checkout shows shipping charges | Configure accurate shipping settings in MC or feed | High |
| **Suspicious URL patterns** | Links redirect through tracking URLs or cloaking | Use direct product URLs, move tracking to URL parameters | Medium |

### Account-Level Issues

| Issue | Impact | Fix |
|---|---|---|
| **Account suspended** | All products disapproved | Review MC notification, fix cited violations, request review |
| **Website claim not verified** | Feed cannot be processed | Complete domain verification in MC (HTML tag, DNS, or GA) |
| **Tax settings missing** | US products cannot show | Configure tax settings at account level or per product |
| **Shipping not configured** | Products ineligible for Shopping | Set up shipping services in MC settings |
| **Return policy missing** | Reduced eligibility in some regions | Add return policy in MC settings |

## Diagnosis Process

### Step 1: Export Disapprovals
Get the full list of disapproved products:
1. In Merchant Center, go to Products > Diagnostics
2. Filter by status: "Disapproved" and "Warning"
3. Export the list with disapproval reasons
4. Or use Content API: `products.list` with `destinations` filter

### Step 2: Categorize by Root Cause
Group disapprovals by reason:
1. **Data quality** — fixable in the feed file (price, availability, attributes)
2. **Image issues** — require image replacement or editing
3. **Policy violations** — require landing page or product changes
4. **Account issues** — require MC account-level configuration

### Step 3: Prioritize by Revenue Impact
Not all disapprovals are equally important. Prioritize:
1. Calculate lost revenue: `disapproved_product_price * avg_daily_orders * days_disapproved`
2. Sort by highest revenue impact first
3. Group quick fixes (data quality) vs complex fixes (re-shoots, policy changes)
4. Set target: resolve top 80% of revenue impact in first pass

### Step 4: Apply Fixes
For each disapproval category:
- **Price mismatch:** Update feed with correct prices, implement real-time price sync
- **Availability mismatch:** Connect feed to inventory management, increase refresh to 4x/day
- **Missing GTIN:** Look up GTINs in ICECAT, Google's barcode database, or manufacturer catalogs
- **Image violations:** Remove overlays/watermarks, re-crop, upload clean versions
- **Landing page 404:** Update URLs in feed, implement redirects on the website
- **Policy violations:** Review Google's Shopping policies, modify product listings accordingly

### Step 5: Request Re-Review
After fixing:
1. Re-submit your feed (manual upload or wait for scheduled fetch)
2. For policy disapprovals: click "Request Review" in MC Diagnostics
3. Allow 3-5 business days for re-review
4. Monitor the Diagnostics tab for updated status
5. If still disapproved, check for secondary violations you may have missed

## Scoring Criteria

Score feed disapproval health 0-100:

| Score Range | Classification | Criteria |
|---|---|---|
| 95-100 | Excellent | < 2% disapproval rate, no policy violations |
| 80-94 | Good | 2-5% disapproval rate, only data quality issues |
| 60-79 | Needs Work | 5-15% disapproval rate, some policy violations |
| 40-59 | Poor | 15-30% disapproval rate, multiple policy issues |
| 0-39 | Critical | > 30% disapproved, or account-level warnings |

## Output Format

```
DISAPPROVAL DIAGNOSIS REPORT
=============================
Total Products: [count]
Approved: [count] ([pct]%)
Disapproved: [count] ([pct]%)
Warnings: [count] ([pct]%)
Disapproval Score: [0-100]

BY CATEGORY:
  Data Quality Issues: [count] products
  Image Violations: [count] products
  Policy Violations: [count] products
  Landing Page Errors: [count] products

TOP DISAPPROVAL REASONS:
1. [reason] — [count] products — Est. revenue loss: $[amount]/day
2. [reason] — [count] products — Est. revenue loss: $[amount]/day
3. [reason] — [count] products — Est. revenue loss: $[amount]/day

FIX PLAN (ordered by impact):
  QUICK FIXES (< 1 hour):
  - Fix [reason] on [count] products: [specific action]
  - Fix [reason] on [count] products: [specific action]

  MEDIUM EFFORT (1-4 hours):
  - Fix [reason] on [count] products: [specific action]

  COMPLEX FIXES (requires external changes):
  - Fix [reason] on [count] products: [specific action]

PREVENTION:
- Implement [process] to prevent [category] disapprovals
- Set up [monitoring] alerts for disapproval rate > [threshold]%
```

## Prevention Best Practices

1. **Sync feed 4x daily** — Prevents price and availability mismatches
2. **Validate GTIN before upload** — Check digit validation catches typos
3. **Automated image checks** — Scan for text overlays and size compliance before upload
4. **Landing page monitoring** — Alert on any 404s or 500s on product URLs
5. **Pre-submission validation** — Run `/feed audit` before every feed upload
6. **MC alerts** — Enable email notifications for disapproval spikes

## Impact
- **-60% disapprovals** from systematic diagnosis and fix process
- **+$X,XXX/day revenue** recovered from re-approved high-value products
- **-80% recurring disapprovals** from prevention processes
- **Account health protection** — prevents escalation to account suspension

## Author
Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | Second Step
