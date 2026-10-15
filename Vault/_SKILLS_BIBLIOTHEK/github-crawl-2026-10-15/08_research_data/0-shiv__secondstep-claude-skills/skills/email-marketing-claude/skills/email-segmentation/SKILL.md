# Email Segmentation — Sub-Skill

## Overview

Segmentation is the difference between batch-and-blast and precision email marketing. Segmented campaigns drive 14.31% higher open rates, 100.95% higher click rates, and 760% more revenue than non-segmented sends. This sub-skill covers RFM analysis, behavioral segmentation, engagement scoring, and lifecycle stages.

**Command:** `/email segments`

---

## Segmentation Audit Checklist

- [ ] Subscribers are segmented beyond just "all subscribers"
- [ ] RFM model implemented (or equivalent purchase-based segmentation)
- [ ] Engagement-based segments defined (active, at-risk, dormant)
- [ ] Lifecycle stages mapped (new, active, at-risk, churned)
- [ ] Demographic segments used where relevant
- [ ] Behavioral triggers feed into segments
- [ ] Segments are updated dynamically (not static lists)
- [ ] Different content/offers sent to different segments
- [ ] Suppression segments defined (unengaged, bounced, complained)
- [ ] Segment sizes are monitored for health

---

## 1. RFM Analysis (Recency, Frequency, Monetary)

RFM is the gold standard for customer segmentation in e-commerce and subscription businesses. Score each customer on three dimensions.

### Scoring Matrix

**Recency** — How recently did they purchase/engage?

| Score | E-commerce | SaaS/Subscription |
|-------|-----------|-------------------|
| 5 | Last 7 days | Active this week |
| 4 | Last 30 days | Active this month |
| 3 | Last 90 days | Active last quarter |
| 2 | Last 180 days | Active last 6 months |
| 1 | 180+ days ago | Inactive 6+ months |

**Frequency** — How often do they purchase/engage?

| Score | E-commerce | SaaS/Subscription |
|-------|-----------|-------------------|
| 5 | 10+ purchases | Daily active |
| 4 | 6-9 purchases | Weekly active |
| 3 | 3-5 purchases | Monthly active |
| 2 | 2 purchases | Quarterly active |
| 1 | 1 purchase | One-time only |

**Monetary** — How much do they spend?

| Score | E-commerce | SaaS/Subscription |
|-------|-----------|-------------------|
| 5 | Top 10% spenders | Enterprise tier |
| 4 | Top 25% spenders | Pro tier |
| 3 | Top 50% spenders | Growth tier |
| 2 | Bottom 50% spenders | Starter tier |
| 1 | Bottom 25% spenders | Free tier |

### RFM Segments

| RFM Score | Segment Name | Strategy |
|-----------|-------------|----------|
| 555, 554, 545 | Champions | Reward, ask for reviews, refer-a-friend |
| 543, 444, 435 | Loyal Customers | Upsell, cross-sell, early access |
| 553, 552, 541 | Potential Loyalists | Nurture, recommend related products |
| 512, 511, 422 | Recent Customers | Onboard well, encourage second purchase |
| 525, 524, 433 | Promising | Incentivize next purchase, build habit |
| 443, 434, 343 | Need Attention | Win back with relevant offers |
| 331, 321, 312 | About to Sleep | Urgency, time-limited re-engagement |
| 255, 254, 245 | Can't Lose | Win-back with best offers, personal outreach |
| 155, 154, 144 | At Risk | Re-engagement or sunset |
| 111, 112, 121 | Lost | Remove or final win-back attempt |

---

## 2. Behavioral Segments

Segment based on what subscribers actually do, not just who they are.

### Email Engagement Segments

| Segment | Definition | Size Target | Strategy |
|---------|-----------|-------------|----------|
| Highly Engaged | Opened 5+ of last 10 emails | 15-25% | Send first, most content, VIP offers |
| Engaged | Opened 2-4 of last 10 emails | 30-40% | Regular sends, A/B test subjects |
| Passive | Opened 1 of last 10 emails | 15-20% | Reduce frequency, re-engage |
| At Risk | No opens in 30-60 days | 10-15% | Win-back sequence |
| Dormant | No opens in 60-90 days | 5-10% | Final win-back, then suppress |
| Dead | No opens in 90+ days | <10% | Suppress from regular sends |

### Website Behavior Segments

| Segment | Trigger | Email Strategy |
|---------|---------|---------------|
| Product Viewers | Viewed product page 2+ times | Send product-specific content |
| Cart Abandoners | Added to cart but didn't purchase | Abandoned cart sequence |
| Browse Abandoners | Browsed category but didn't add to cart | Category recommendations |
| Content Consumers | Read 3+ blog posts | Nurture with more content |
| Pricing Page Visitors | Viewed pricing page | Sales follow-up |
| Feature Page Visitors | Viewed specific feature pages | Feature-specific nurture |

---

## 3. Demographic Segments

| Segment Type | Data Source | Use Case |
|-------------|-----------|----------|
| Geography | Signup form, IP | Localized offers, timezone-based sends |
| Industry | Signup form, enrichment | Industry-specific content |
| Company Size | Signup form, enrichment | Appropriate product tier recommendations |
| Job Title/Role | Signup form, enrichment | Content tailored to decision-maker level |
| Age/Gender | Signup form | Product recommendations |
| Language | Browser, form | Localized email content |

---

## 4. Lifecycle Stages

Map every subscriber to a lifecycle stage and tailor communication accordingly.

| Stage | Definition | Email Goal | Frequency |
|-------|-----------|-----------|-----------|
| Subscriber | Signed up, hasn't purchased | Convert to first purchase | 2-3/week |
| First-time Buyer | Made 1 purchase | Drive second purchase (critical) | 2/week |
| Repeat Buyer | Made 2-3 purchases | Build loyalty, increase AOV | 1-2/week |
| Loyal Customer | Made 4+ purchases or high LTV | Retain, reward, refer | 1-2/week |
| VIP | Top 5% by revenue | White-glove treatment, exclusive access | 1/week |
| At Risk | Engaged before but activity declining | Re-engage, incentivize | 1/week |
| Lapsed | Was a buyer, hasn't purchased in 90+ days | Win-back offer | 1/2 weeks |
| Churned | Lapsed 180+ days, no engagement | Final win-back or suppress | Monthly or suppress |

### The Second Purchase Problem

The most critical transition is from first-time buyer to repeat buyer. Stats:
- Probability of selling to a first-time buyer again: 27%
- Probability of selling to a second-time buyer again: 45%
- Probability of selling to a third-time buyer again: 54%

**Action:** Create a dedicated post-first-purchase sequence focused entirely on driving the second purchase. This is the highest-leverage sequence after welcome.

---

## 5. Engagement Scoring Methodology

Assign points for every interaction to create a unified engagement score.

### Point System

| Action | Points | Decay |
|--------|--------|-------|
| Email open | +1 | -0.5/week |
| Email click | +3 | -1/week |
| Website visit | +2 | -0.5/week |
| Page view (product/pricing) | +5 | -1/week |
| Content download | +10 | -2/week |
| Form submission | +15 | -3/week |
| Purchase | +25 | -5/week |
| Unsubscribe click (didn't complete) | -5 | — |
| Spam complaint | -50 | — |
| Hard bounce | Remove | — |

### Score Tiers

| Score | Tier | Action |
|-------|------|--------|
| 50+ | Hot | Priority sends, sales follow-up |
| 25-49 | Warm | Regular cadence, nurture |
| 10-24 | Cool | Reduced frequency, value-focused |
| 1-9 | Cold | Re-engagement sequence |
| 0 or negative | Frozen | Suppress or sunset |

---

## Segmentation Scoring

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| Any segmentation beyond "all" | 20% | 0 or 100 |
| 3+ active segments | 15% | 0-100 |
| Engagement-based segments | 20% | 0 or 100 |
| Lifecycle stages mapped | 15% | 0 or 100 |
| RFM or purchase-based segments | 15% | 0 or 100 |
| Segments are dynamic (auto-updating) | 15% | 0 or 100 |
