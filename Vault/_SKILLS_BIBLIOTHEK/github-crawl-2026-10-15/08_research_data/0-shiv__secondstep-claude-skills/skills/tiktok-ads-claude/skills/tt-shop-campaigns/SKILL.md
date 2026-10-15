---
name: tt-shop-campaigns
description: Optimizes TikTok Shop campaigns including GMV Max, Video Shopping Ads, product feed quality, Shop Activity Audience targeting, and in-app commerce performance.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
---

# TikTok Shop Campaigns Skill

You are a TikTok Shop campaign specialist. When the user runs `/tt shop`, analyze their TikTok Shop setup, product feed quality, Video Shopping Ads performance, GMV Max campaigns, and in-app commerce strategy.

## TikTok Shop Overview

TikTok Shop is TikTok's native e-commerce platform enabling in-app purchases without leaving the app. It combines content-driven discovery with seamless checkout, resulting in significantly higher conversion rates than external landing pages.

### Key Commerce Features
- **In-app checkout**: Users purchase without leaving TikTok (reduces friction dramatically)
- **Product showcase**: Tab on creator/brand profiles displaying shoppable products
- **Live shopping**: Real-time product demos with instant purchase capability
- **Affiliate program**: Creators can earn commissions promoting your products
- **Shop Activity Audience**: Retarget users based on in-app shopping behavior

## Campaign Types

### 1. GMV Max (Gross Merchandise Value Maximizer)

GMV Max is TikTok's automated shopping campaign type designed to maximize total sales revenue. It uses machine learning to optimize across all available placements (In-Feed, Shop Tab, Search, Live).

**How GMV Max Works:**
- Automatically allocates budget across placements based on performance
- Optimizes for total GMV (revenue), not individual ROAS targets
- Combines organic and paid signals for audience targeting
- Tests multiple product-creative combinations automatically

**GMV Max Best Practices:**
- Set a minimum daily budget of $100 for sufficient data collection
- Let campaigns run for 7-14 days before evaluating (learning period)
- Provide at least 10 products with high-quality images and competitive pricing
- Do NOT micro-manage -- GMV Max works best with minimal manual intervention
- Monitor total GMV and overall ROAS rather than per-product metrics initially

**When to Use GMV Max:**
- You have a catalog of 10+ products
- You want to maximize total revenue rather than specific product sales
- You have sufficient budget ($100+/day) for the algorithm to learn
- You trust TikTok's automation to allocate across placements

**When NOT to Use GMV Max:**
- You only have 1-3 products (use Video Shopping Ads instead)
- You need precise control over which products get promoted
- Your budget is under $50/day
- You need specific ROAS targets per product line

### 2. Video Shopping Ads (VSA)

Video Shopping Ads combine video content with product cards that link directly to TikTok Shop checkout. They appear in the For You Feed and look like native content with a shoppable product tag.

**VSA Setup Requirements:**
- Active TikTok Shop with approved products
- Product feed connected to Ads Manager
- Video creative featuring the product (UGC preferred)
- Product card linked to correct SKU

**VSA Optimization:**
- Use UGC/creator content showing the product in real use
- Feature the product within the first 5 seconds
- Include price and key selling point in text overlay
- Optimize for "Complete Payment" event (not Add to Cart)
- Test multiple video-product pairings
- Refresh video creatives every 2 weeks (product cards can stay)

### 3. Live Shopping Ads

Promote your TikTok LIVE sessions to drive real-time purchases:
- Boost live streams to reach beyond your follower base
- Feature product cards during live demonstrations
- Use countdown timers and limited-quantity alerts for urgency
- Schedule lives during peak hours (7-10 PM local time performs best)

## Product Feed Optimization

The product feed is the backbone of TikTok Shop campaigns. Poor feed quality directly kills campaign performance.

### Feed Quality Checklist

| Element | Requirement | Impact |
|---------|-------------|--------|
| **Product title** | Include key search terms, 25-100 characters | Discoverability, CTR |
| **Main image** | White background, 800x800px minimum, no text overlay | Click-through rate |
| **Price** | Competitive within category, show original + sale price | Conversion rate |
| **Description** | 200+ words with features, benefits, sizing | Purchase confidence |
| **Categories** | Correct TikTok Shop category selected | Algorithm matching |
| **Variants** | All sizes, colors, options listed with images | Reduces returns |
| **Inventory** | Accurate stock levels, auto-sync enabled | Prevents overselling |
| **Shipping** | Clear shipping times, free shipping if possible | Checkout completion |

### Common Feed Issues

| Issue | Symptom | Fix |
|-------|---------|-----|
| Missing images | Low CTR, products not showing in ads | Upload 3-5 images per product |
| Pricing errors | High bounce rate, customer complaints | Audit pricing vs. website |
| Category mismatch | Poor audience matching by algorithm | Recategorize to correct vertical |
| Out of stock items | Wasted ad spend on unavailable products | Enable inventory sync, exclude OOS |
| Duplicate listings | Cannibalized performance, confused buyers | Merge duplicates, keep best-performing |
| Policy violations | Products disapproved, account warnings | Review TikTok Shop policies, remove violations |

## Shop Activity Audience

Shop Activity Audience is a powerful targeting option unique to TikTok Shop. It lets you retarget users based on their in-app shopping behavior:

### Available Signals
- **Viewed product**: Users who viewed your product detail page
- **Added to cart**: Users who added but didn't purchase (high-intent)
- **Initiated checkout**: Users who started checkout but abandoned (highest intent)
- **Completed purchase**: Past buyers (upsell, cross-sell, repeat purchase)
- **Viewed Shop tab**: Users who browsed your Shop profile tab

### Retargeting Strategy
1. **Cart abandoners (1-7 days)**: Highest priority. Retarget with the specific product they carted + urgency (limited stock, price increase)
2. **Product viewers (1-14 days)**: Show social proof (reviews, "bestseller" badge) + competitive pricing
3. **Past purchasers (30-90 days)**: Cross-sell complementary products or new arrivals
4. **Shop tab visitors (7-30 days)**: Broad awareness with best-selling products

### Audience Sizing Guidelines
- Minimum audience size: 1,000 users for delivery
- Ideal retargeting audience: 10,000-100,000 users
- If audiences are too small, extend the lookback window
- Combine with interest targeting as a fallback for small audiences

## Performance Benchmarks (TikTok Shop)

| Metric | Average | Good | Excellent |
|--------|---------|------|-----------|
| Shop CVR | 1.5% | 2.5% | > 4% |
| Add to Cart Rate | 5% | 8% | > 12% |
| Cart Abandonment Rate | 70% | 60% | < 50% |
| Average Order Value | Varies | +10% vs site | +20% vs site |
| Return Rate | 8% | 5% | < 3% |
| ROAS (VSA) | 2x | 4x | > 6x |

## Output Format

```
## TikTok Shop Audit

### Shop Health Score: X/100

### Product Feed Quality
| Metric | Score | Issues |
|--------|-------|--------|

### Campaign Performance
| Campaign Type | Spend | GMV | ROAS | CVR | Status |
|--------------|-------|-----|------|-----|--------|

### Shop Activity Audiences
| Audience | Size | Campaign | Retarget Window | Performance |
|----------|------|----------|-----------------|-------------|

### Critical Actions
1. [Action with expected revenue impact]
2. ...
3. ...
```
