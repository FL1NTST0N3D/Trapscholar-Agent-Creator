---
name: meta-ads-expert
description: Expert-level Meta Ads (Facebook/Instagram) skill. Use whenever the user mentions Meta Ads, Facebook Ads, Instagram Ads, FB Ads Manager, Business Manager, Advantage+ Shopping, ASC, CBO/ABO, Lookalike audiences, Custom Audiences, Conversions API (CAPI), iOS 14.5 attribution, aggregated event measurement, pixel setup, catalog ads, DPA, creative testing, 1-day click attribution, or any paid social campaign on Meta platforms. Also trigger for "run Facebook ads," "Instagram lead gen," "creative iteration," "UGC ad scripts," "hook testing," or auditing a Meta ad account. Do NOT use for organic social, TikTok ads, LinkedIn ads, or Google Ads. Covers account structure, campaign objectives, bidding, audience strategy, creative frameworks, CAPI setup, attribution, scaling playbooks, and troubleshooting.
---

# Meta Ads Expert

## When to Use This Skill
- Building or restructuring a Meta Ads account
- Planning campaign architecture (CBO vs ABO, Advantage+ vs manual)
- Creative strategy, hook testing, UGC scripting
- Troubleshooting delivery, frequency, CPM spikes, or low CTR
- Setting up Conversions API and resolving iOS attribution gaps
- Scaling winning campaigns without breaking learning phase
- Auditing an existing account

## Core Account Architecture

### The 3-Tier Hierarchy
- **Campaign**: objective + budget (if CBO) + bid strategy
- **Ad Set**: audience + placements + budget (if ABO) + optimization event
- **Ad**: creative + copy + CTA + destination

### Campaign Objectives (2024+ ODAX framework)
- **Sales** - purchase/lead conversions (most common for DTC & services)
- **Leads** - instant forms or website leads
- **Traffic** - rarely worth using; only for top-funnel content distribution
- **Engagement** - retargeting warm audiences, message conversions
- **Awareness** - reach/brand lift (mid-to-enterprise only)
- **App Promotion** - app installs/events

## Account Structure Playbooks

### For DTC Ecommerce
- 1 Advantage+ Shopping Campaign (ASC) - 80% of budget
- 1 Broad Targeting Campaign (manual) - 15%
- 1 Retargeting Campaign (180-day window) - 5%
- Creative refresh cadence: 2-4 new ads/week into ASC

### For Lead Gen (Services, Dental, Contractors)
- 1 Conversion Campaign optimizing for lead event (not form fills)
- Broad audience + detailed targeting expansion ON
- Location-specific ad sets if serving multiple markets
- Instant Form + Website Lead split test

### For High-Ticket B2B
- Lead campaign with enriched Instant Form (qualifying questions)
- Lookalike 1% of past closed-won clients
- CAPI with offline conversion uploads critical
- Longer attribution window (7-day click/1-day view)

## Creative Framework

### The Hook-Problem-Solution-Proof-CTA Framework
1. **Hook** (first 3 seconds): Pattern interrupt, curiosity, bold claim, or relatability trigger
2. **Problem**: Agitate pain point the audience feels
3. **Solution**: Introduce product as the fix
4. **Proof**: Testimonial, before/after, data, social proof
5. **CTA**: Clear action + urgency

### Creative Testing Methodology (Hook Testing)
- Test 3-5 hooks against same body/CTA to isolate variable
- Minimum $50-100 spend per hook before calling it
- CTR (outbound) and Hook Rate (3s video views / impressions) are your leading indicators
- Scale winners, kill losers at statistical significance

### Creative Diversity Requirements
Per ad set, run at minimum:
- 1 UGC talking-head video
- 1 product demo or static
- 1 testimonial/review format
- 1 problem-solution static or carousel

## iOS 14.5+ Attribution Strategy

### Conversions API (CAPI) - Non-Negotiable
- Deploy server-side via GTM Server, Stape, or native Shopify/WP integration
- Deduplicate with Pixel events using `event_id`
- Match quality score target: 7+ out of 10
- Send these events minimum: PageView, ViewContent, AddToCart, InitiateCheckout, Purchase, Lead

### Aggregated Event Measurement (AEM)
- Verify domain in Business Manager
- Prioritize 8 events per domain (Purchase/Lead always in slot 1)
- Value optimization requires value parameter + slot reservation

### Attribution Windows
- Default: 7-day click / 1-day view
- For considered purchases ($500+): stick with 7-day click
- For impulse DTC: 1-day click can speed up learning

## Budget & Bidding

### Learning Phase Rules
- 50 optimization events per ad set per week to exit learning
- Don't edit ad sets mid-learning (restarts the phase)
- Starting budget = 3-5x target CPA minimum

### CBO vs ABO Decision Tree
- **CBO**: 3+ ad sets, similar audience sizes, proven creatives
- **ABO**: Testing new audiences, uneven ad set sizes, constrained budgets

### Bid Strategies
- **Highest Volume** (default): Use 80% of the time
- **Cost Cap**: When you have reliable CPA data and want to scale predictably
- **Bid Cap**: Advanced only - when you know exact auction dynamics
- **ROAS Goal**: Ecommerce with consistent AOV and value optimization

## Scaling Playbooks

### Vertical Scaling (same campaign)
- Increase budget by 20-30% every 3-4 days if CPA holds
- Don't 2x overnight - kills learning

### Horizontal Scaling
- Duplicate winning ad set to new audience (Lookalike variations)
- Duplicate to new placement (Reels-only, Stories-only)
- Geographic expansion (new markets/countries)

### Creative Scaling
- Take winning ad → 5 variations (new hook, new format, new CTA)
- Iterate fast; winning creative has a shelf life of 2-4 weeks

## Troubleshooting Cheat Sheet

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| High CPM, low CTR | Creative fatigue | Refresh creative, expand audience |
| Low delivery | Audience too narrow or bid too low | Broaden audience, raise bid/budget |
| Learning Limited | <50 events/week | Raise budget or consolidate ad sets |
| CAPA worse than last month | Creative/offer/market shift | Audit creative performance, check seasonality |
| Pixel/CAPI mismatch | Deduplication broken | Verify event_id pass-through |

## Reporting Standards
- Primary KPIs: CPA, ROAS, Frequency, CTR (outbound), Hook Rate
- Always report attribution window used
- Separate platform (Meta reported) vs source of truth (GA4/Shopify)
- Triangulate with post-purchase surveys for brand awareness spend

## Anti-Patterns
- Don't use Traffic objective hoping to get conversions
- Don't stack multiple Lookalikes in one ad set (they overlap)
- Don't run <$20/day ad sets on lead gen - won't exit learning
- Don't optimize for landing page views on a Sales objective campaign
- Don't edit live ads mid-learning unless killing them
- Don't trust 1-day view attribution for paid social (inflates results)
