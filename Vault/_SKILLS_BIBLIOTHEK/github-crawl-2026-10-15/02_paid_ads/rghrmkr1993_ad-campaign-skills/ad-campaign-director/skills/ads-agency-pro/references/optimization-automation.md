# Optimization & Automation: The Agent's Decision Algorithms

The platforms run ML at the auction layer. This file is the agent's OWN algorithm layer:
budget allocation, bidding selection, creative rotation, pacing, lifecycle automation, and
ecommerce intelligence, expressed as executable rules, not textbook names.

## Budget allocation (portfolio logic)

1. **Marginal, not average:** allocate the next rupee/dollar to the channel/campaign with
   the highest MARGINAL return (discovered via budget stair-steps), not highest average
   ROAS. Average ROAS flatters saturated retargeting.
2. **Explore/exploit split:** 70-80% budget to proven winners, 20-30% to structured
   exploration (new concepts, audiences, channels). This is a multi-armed bandit run at
   human cadence, Thompson-sampling thinking without the math: sample new arms in
   proportion to their plausible upside.
3. **CBO vs ABO:** campaign-budget optimization for scale campaigns (let the platform
   allocate); ad-set budgets only when you must force spend into a strategic segment
   (new language market, test cell).
4. **Pacing rules:** daily check = spend vs plan ±20%. Under-pacing → loosen targets/
   audiences or raise bids; over-pacing with target CPA/ROAS met → let it run (that's
   success, not a problem).
5. **Profit-based budgeting:** budget to margin, not revenue, when SKU margins differ
   (feed margin via value rules / conversion values). ROAS targets per margin tier:
   a 70%-margin product can win at 2x; a 20%-margin one needs 5x+.
6. **Incrementality budgeting:** channels proven incremental get scale priority; channels
   living on click-attribution glory (brand search, deep retargeting) get capped.

## Bidding selection tree

```
New account / <50 conv-events per week?
  → Maximize Conversions / Lowest Cost (no target) until signal exists
Stable volume + clear CPA goal?
  → tCPA (Google) / Cost Cap (Meta), set 10-15% above achieved CPA, tighten stepwise
Ecom with value variance across SKUs/customers?
  → tROAS / Max Conversion Value (+ value rules for margin/LTV weighting)
Strict efficiency ceiling (cash-constrained)?
  → Cost cap / bid cap, accept volume loss knowingly
Awareness/reach flights?
  → CPM buying with frequency caps
```
Never change bid strategy AND budget AND creative in one move. One lever at a time,
with 7-10 day observation windows (except emergencies).

## Creative rotation algorithm (the agent's bandit)

- Maintain ≥10-15 live concepts; platforms auto-shift spend to winners (their bandit).
- Weekly: rank by spend-weighted results. Kill CONCEPTS (all variants) that got fair spend
  (>3-5x CPA target in spend) with no conversions. Never kill mid-learning.
- Winners: cut new variations of the winning ANGLE (hook swaps, format swaps), exploit.
- Keep 20-30% of new-creative slots for unproven angles, explore.
- Fatigue watch: frequency >3-4 + CTR decay >30% from peak + rising CPA = refresh cycle
  (2-3 week half-life expectation per platforms-2026.md).

## Scale/kill thresholds (defaults; tune per client economics)

| Signal | Action |
|---|---|
| CPA ≤ target for 7 days, volume stable | Scale +20-30%, hold 7 days, repeat |
| CPA 1-1.5x target | Hold; refresh creative before touching budget |
| CPA >1.5-2x target after learning + fair spend | Kill concept / pause ad set |
| Spend with zero conversions ≥3x target CPA | Kill unless strategic test |
| ROAS above target but volume tiny | Loosen target 10-15% to buy volume |
| Sudden collapse account-wide | STOP, check tracking breakage FIRST, not creative |

## Marketing automation & lifecycle (the free revenue layer)

Build these for every ecom/lead client, they compound and cost ~nothing per send:
- **Triggers:** welcome series (signup), abandoned cart (1h/24h/72h, recovers meaningful
  % of carts), browse abandon, post-purchase (delivery → review ask → replenishment timed
  to product usage cycle), win-back (60/90-day lapsed).
- **Channels by geo:** email everywhere; WhatsApp journeys where dominant (India, LatAm,
  SEA, utility templates + opt-in rules); SMS for US/UK flash moments (DNC/TCPA rules).
- **Lead scoring (B2B/lead-gen):** score = fit (firmographics) × intent (behavior);
  route hot to sales same-day; nurture the rest. Feed closed-won back to platforms as
  offline conversions, this is the single biggest lead-gen optimization lever.
- **Segmentation:** RFM (recency/frequency/monetary) is the workhorse, VIPs (exclude
  from discounts, early access), at-risk (win-back), one-timers (second-purchase push).
- **Personalization:** dynamic product blocks, language-matched journeys, geo-timed sends
  (festival calendars from geo-playbooks.md).

## Ecommerce intelligence

- **Feed = targeting:** titles keyword-front-loaded (attribute order: brand + type + key
  attribute), all attributes filled, price/availability synced real-time, image policy-
  clean. Weekly feed-health check is non-negotiable for catalog/PMax spend.
- **Catalog structure:** product sets by margin tier / bestsellers / new-in / clearance, different ROAS targets each.
- **Dynamic ads:** catalog retargeting (viewed/carted) + broad catalog prospecting
  (Advantage+ Catalog); creative overlays for offers.
- **Price/discount logic:** protect margin, bundle (AOV up) before discounting; tiered
  thresholds ("free shipping over X" just above current AOV); festival pricing planned
  against the geo calendar, never panic-discounting mid-flight.
- **Cross-sell/upsell:** post-purchase flows + "complete the routine/look" bundles beat
  paid retargeting for owned buyers.
- **Abandoned cart recovery:** WhatsApp/email sequence + dynamic retargeting; COD-heavy
  geos get order-confirmation flows to cut refusals (geo-playbooks.md).

## SEO/AEO/GEO adjacency (paid + organic compounding)

Paid data feeds organic: winning ad hooks → title tags/meta; search-term reports → content
topics; product feed → schema markup. Organic feeds paid: top content → retargeting pools;
GBP hygiene → local campaign quality. For deep SEO/AEO work invoke the dedicated SEO
skills, this skill's job is the handshake, not the discipline.
