# Enterprise MarTech: Stack, Data, Programmatic, Retail Media, CRO

The infrastructure layer: what enterprise marketing systems (HubSpot/Adobe/Salesforce-class)
actually consist of, sized honestly for each client tier, plus programmatic and deep CRO.

## MarTech stack blueprint (by client size)

| Layer | SMB (most clients) | Mid-market | Enterprise |
|---|---|---|---|
| Tag/event layer | Google Tag Manager + dataLayer conventions | GTM + server-side GTM | Server-side tagging + event gateway |
| Analytics | GA4 | GA4/Mixpanel/Amplitude (product analytics for apps/SaaS) | Adobe Analytics / GA4-360 + BI (Looker/Power BI/Tableau) |
| CRM | HubSpot free/Zoho/pipeline sheet | HubSpot/Salesforce | Salesforce + marketing cloud |
| Email/lifecycle | Klaviyo/Mailchimp/Brevo | Klaviyo/Braze + WhatsApp BSP | Braze/Adobe Campaign/SFMC |
| CDP | You don't need one, CRM+GA4+platform audiences | Composable: warehouse (BigQuery) + reverse ETL (Hightouch-class) | Full CDP (Segment/mParticle-class) or warehouse-native |
| Consent | CMP banner + Google Consent Mode v2 | CMP + per-geo policies | Enterprise CMP + preference center |

**Distinctions that clients confuse (know them cold):**
- **CRM** = relationship record (people, deals, comms). **CDP** = unified behavioral
  profile across sources, activated to channels. **DMP** = anonymous third-party cookie
  audiences, functionally dead post-cookie; don't recommend one.
- **ETL/ELT** = batch data → warehouse. **Reverse ETL** = warehouse segments → ad
  platforms/CRM (this is how "audience of high-LTV customers" reaches Meta at enterprise).
- **Identity graph** = mapping one human across devices/emails/cookies; agencies touch it
  via hashed-email uploads (Customer Match, CAPI advanced matching), consent-gated.
- **Feature stores / MLOps** = infrastructure for in-house ML models; only relevant when a
  client has a data team. Don't sell what they can't run.

**Event tracking architecture (do this on EVERY client):** one naming convention
(`object_action`: `product_viewed`, `checkout_started`), a written tracking plan (event,
properties, destinations, owner), dataLayer as single source, server-side (CAPI/sGTM)
mirroring browser events, QA before launch. Bad event taxonomy poisons every downstream
system, this is the highest-leverage infrastructure hour.

**Automation workflows & lead routing:** triggers (behavioral, lifecycle, score-threshold)
→ actions (email/WhatsApp/SMS, CRM task, audience sync, webhook). Lead routing: score →
territory/owner assignment → SLA timers (speed-to-lead: minutes matter, 10x contact rates).

## Programmatic advertising (beyond the walled gardens)

The plumbing: **Advertiser → DSP** (demand-side platform: DV360, The Trade Desk, Amazon
DSP) **→ Ad Exchange** (real-time auction via OpenRTB protocol, ~100ms) **→ SSP**
(supply-side platform representing publishers) **→ Publisher**.

- **RTB open auction:** buy impressions user-by-user across the open web.
- **PMP (private marketplace):** invite-only deals with premium publishers, better
  inventory, fixed floor prices.
- **Programmatic guaranteed:** reserved buys executed programmatically.
- **Header bidding:** publishers auction to many SSPs simultaneously. This is why open-web CPMs
  are efficient but quality varies.
- **Contextual targeting:** page-content targeting (no cookies), resurging in the
  privacy era; strong for compliance-constrained verticals (health, finance).
- **CTV programmatic:** streaming TV via DSPs, fastest-growing lane; premium brand
  budgets.

**When to use:** client spend >$25-50k/month with reach/frequency goals beyond
Meta+Google, B2B site-list plays, CTV ambitions, or geo/publisher-specific needs. Below
that, DSP minimums + fees + ad-fraud tax eat the value, say so. Fraud/viewability
verification (IAS/DV/MOAT-class) is mandatory on open-web buys.

## Retail media (beyond Amazon)

- **Amazon:** Sponsored Products (search shelf) → Sponsored Brands (banner) → DSP
  (off-site retargeting on Amazon data). Bottom-funnel harvest + brand-term defense.
- **Walmart Connect / Target Roundel / Instacart:** same model, US grocery/CPG reach.
- **Flipkart Ads / Amazon India / Blinkit-Zepto ads:** the India retail-media lane, essential for CPG/beauty clients selling on marketplaces.
- **Shopify Audiences:** D2C co-op lookalikes pushed to Meta/Google, worth enabling for
  Shopify Plus clients.
- **Etsy Ads:** handmade/craft sellers; simple CPC, budget-capped.
- Budget logic: retail media captures shoppers already in-store: it defends share and
  harvests demand; it rarely CREATES demand. Fund it from trade/shopper budgets, judge on
  incremental share of shelf, and never let "ROAS 8x on brand terms" fool anyone.

## Analytics tool map (what to reach for)

GA4 (web/traffic truth for most clients) • Mixpanel/Amplitude (product events, funnels,
retention for apps/SaaS) • platform ad managers (delivery diagnostics) • BI dashboards
(Looker Studio free tier covers most agency reporting; Power BI/Tableau at enterprise) •
MMM (Robyn/Meridian, 2+ years data) • server logs/search console (SEO). Rule: one source
of truth per question, declare which tool answers revenue, traffic, product usage, and
delivery, and never argue across tools in a client meeting.

## CRO deep-dive (the conversion multiplier)

**Research stack (diagnose before testing):** analytics funnel (where do they leave) →
heatmaps/scrollmaps (what they see/ignore) → session replays (watch 20 real sessions of
the leak point) → exit polls/post-purchase surveys (why) → VoC review mining (words).

**Prioritize tests with ICE** (Impact × Confidence × Ease). High-frequency winners:
- **LP:** message-match ad↔headline (the #1 fix), one page one goal, social proof above
  fold, mobile speed <3s, sticky CTA.
- **Forms:** cut fields (each optional field costs conversions), multi-step beats long
  single-step, inline validation, phone-optional where possible.
- **Checkout:** guest checkout, wallet payments (UPI/Apple Pay/GPay), shipping-cost
  transparency early (surprise shipping = #1 abandonment), trust badges at payment,
  COD-confirmation flows in COD geos.
- **Offer/pricing tests:** bundles vs discounts, thresholds ("free shipping over X"),
  anchor tiers, trial length, offer tests routinely beat design tests 10x; test the
  OFFER before the button color.
- **Micro vs macro:** optimize micro-conversions (ATC, lead step 1) only when they lift
  the macro (purchase, SQL), watch for junk-lead inflation.

Every CRO win compounds every ad rupee: a +20% LP conversion lift is a -17% CPA cut
across ALL channels. Sequence: tracking → CRO research → media scale.
