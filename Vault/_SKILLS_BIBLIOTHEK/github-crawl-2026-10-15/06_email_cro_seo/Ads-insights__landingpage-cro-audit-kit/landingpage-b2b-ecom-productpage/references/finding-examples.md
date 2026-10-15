# Worked finding examples — B2B product page quality calibration

These examples show what a high-quality B2B PDP finding looks like across different B2B types, brand snapshots, and ICE scores. Use them as a reference standard.

---

## Example 1: 🔴 Critical — Price presentation & tier pricing (transactional industrial supplies)

### 🔴 Price presentation — Tier pricing absent despite quantity-driven category

**Diagnosis**
The product page shows a single price (€4.20 per unit) with no tier-pricing table, despite the product being a high-volume industrial fastener with typical orders ranging 50-2000 units. Per Baymard's B2B pricing research, tier pricing tables on quantity-driven products increase order size by 12-28% on average through anchoring effects (Kahneman/Tversky). The current display gives buyers no incentive to order in larger quantities, and no signal that volume discounts exist. For a transactional B2B ecom site in this category, this is a missed AOV lever at the most material moment of the funnel. Industry competitors all show tier pricing prominently — visitors comparing suppliers will notice the absence.

**Recommendation**
Add a tier-pricing table directly below the unit price, showing 4-5 price breaks: 1-49 units (€4.20), 50-99 units (€3.90, save 7%), 100-499 units (€3.50, save 17%), 500-999 units (€3.20, save 24%), 1000+ units (€2.95, save 30%). Display cost-per-unit at each tier and total cost when a quantity is entered. Use visual emphasis on the recommended tier (often middle-second-from-top). Frame discounts as "Save X%" rather than negative percentage. For logged-in customers with negotiated rates, show their tier alongside list tiers ("Your price: €2.85 — Save 32%").

**Test specification**
- **Hypothesis:** If we add a tier-pricing table directly below the unit price, then average order value (AOV) will increase because the anchoring effect of visible volume discounts encourages larger orders (Baymard B2B pricing research; Kahneman/Tversky anchoring).
- **Variant A:** single unit price only
- **Variant B:** unit price + 4-5 tier table with cost-per-unit and save-% framing
- **Primary metric:** average order value (AOV) on add-to-cart sessions
- **Secondary metrics:** units per order, add-to-cart rate, scroll-to-tier-table rate
- **Expected impact:** +12% to +25% on AOV for this category
- **ICE:** I=8, C=9, E=8 → 8.3
- **Source:** Baymard Institute B2B pricing research; Kahneman & Tversky anchoring; Cialdini reciprocity framing

---

## Example 2: 🔴 Critical — MOQ, pack sizes & unit-of-measure clarity (wholesale CPG)

### 🔴 MOQ — Pack-size enforcement silent; visitors hit error after add-to-cart

**Diagnosis**
The product page shows price per piece (€2.40) and a quantity selector defaulting to 1. There is no visible MOQ indication, no "Sold per case of 24" label, and no pack-size context. Adding 1 to cart triggers a backend error "Minimum order quantity is 1 case (24 units)" — discovered only after the visitor attempted to purchase. Per Baymard's B2B quantity research, **39% of B2B buyers have abandoned a purchase due to unclear pack-size info**, and silent MOQ enforcement is one of the top-3 highest-abandonment patterns in wholesale ecom. For a fashion-wholesale platform serving boutique retailers, this fundamental UX gap actively suppresses conversion at the cart-add moment.

**Recommendation**
Three changes. First, replace the "1" default quantity with the actual MOQ ("24"), with quantity selector incrementing by case size (24, 48, 72...). Second, add explicit pack-size label directly below product title: "Sold per case of 24 · Min. order 1 case". Third, show cost-per-case alongside cost-per-piece ("€2.40 per piece · €57.60 per case"). For complex products with multiple pack-size options (piece / case / pallet), add a pack-size switcher above the quantity selector. Validation should be inline at the quantity field, not at cart-add.

**Test specification**
- **Hypothesis:** If we display MOQ and pack-size proactively (default quantity = MOQ, pack-size label visible, cost-per-case shown), then cart-add success rate and add-to-cart rate will increase because visitors no longer encounter silent MOQ errors that trigger abandonment (Baymard B2B quantity research).
- **Variant A:** "1" default quantity, no pack-size info, MOQ error at cart-add
- **Variant B:** Default quantity = MOQ, "Sold per case of 24" visible, cost-per-case shown
- **Primary metric:** successful add-to-cart rate (cart-adds that don't trigger MOQ error)
- **Secondary metrics:** cart abandonment rate after error, add-to-cart rate overall, average units per order
- **Expected impact:** +10% to +25% on successful add-to-cart rate
- **ICE:** I=9, C=9, E=8 → 8.7
- **Source:** Baymard Institute B2B quantity research; Nielsen Norman error-prevention heuristic

---

## Example 3: 🔴 Critical — Primary CTA (quote-driven industrial equipment)

### 🔴 Primary CTA — "Request quote" buried below the fold with no response-time expectation

**Diagnosis**
The product page shows technical specifications prominently above the fold but the "Request quote" CTA appears below the spec table, requiring 2-3 scrolls on desktop and 5+ on mobile. There is no response-time expectation set ("Quotes typically returned within 4 business hours" or similar). Per Baymard's B2B CTA research, primary CTAs on quote-driven products must be visually prominent and above-the-fold — buried quote CTAs reduce quote-request rate by 25-40%. Per Fogg's Behavior Model, the visitor's motivation is high (they're researching for a specific need) and ability should be maximized — but the current placement turns a high-motivation visitor into a scroller. MECLABS' anxiety axis applies: without response-time signaling, visitors hesitate ("Will this quote take 3 weeks like the last supplier?") which suppresses CTA clicks.

**Recommendation**
Move the "Request quote" CTA above-the-fold, positioned to the right of the product imagery on desktop (or below the imagery on mobile). Make it visually dominant: filled brand color, 56-64px height, full-width on mobile. Below the CTA, add a response-time microcopy block: "Quotes typically delivered within 4 business hours · Mon-Fri 9:00-17:00 CET". Add secondary CTAs below: "Download datasheet (PDF)" and "Save to list for later". Make sure the quote-request form is short (4-6 fields max — company, name, email, phone, quantity needed, application context).

**Test specification**
- **Hypothesis:** If we move "Request quote" CTA above-the-fold with explicit response-time microcopy, then quote-request rate will increase because high-motivation visitors immediately see the primary path and gain confidence in response speed (Baymard B2B CTA research; Fogg Behavior Model; MECLABS anxiety reduction).
- **Variant A:** "Request quote" CTA below the spec table, no response time
- **Variant B:** Primary CTA above-the-fold + "Quotes within 4 business hours" microcopy
- **Primary metric:** quote-request rate (form submissions / page visits)
- **Secondary metrics:** time to CTA click, scroll depth, save-to-list rate
- **Expected impact:** +15% to +35% on quote-request rate
- **ICE:** I=9, C=8, E=8 → 8.3
- **Source:** Baymard Institute B2B CTA research; Fogg Behavior Model; MECLABS Conversion Sequence Heuristic

---

## Example 4: 🟠 Important — Account, login & customer-specific content (transactional MRO supplier)

### 🟠 Account — No login prompt despite hidden tier pricing

**Diagnosis**
The page shows list price (€18.50 per unit) with no tier table for anonymous visitors. There is no visible "Log in for your trade pricing" CTA, no value proposition explaining why an account benefits the buyer, and no signal that customer-specific pricing exists for logged-in customers. Per Baymard's B2B account research, login conversion on B2B PDPs is one of the highest-leverage UX moves — and requires explicit value framing ("Log in to see your discounted pricing", "Your last order: 240 units in Sept", "Access your saved lists"). For this MRO supplier serving repeat-customer accounts, anonymous visitors who are actually existing customers cannot easily access their negotiated rates from the product page.

**Recommendation**
Add a "Log in for your trade pricing" prompt directly below the anonymous list price. Frame value explicitly: "Logged-in customers see negotiated pricing, save lists, and reorder past purchases in one click." Show one-tap social/SSO login if applicable; otherwise minimal email-password form. After login, display: (1) customer-specific price prominently ("Your price: €14.20 — saved 23%"), (2) "Last ordered 240 units on 12 Sept 2024 — reorder?", (3) "Add to existing list: [Engineering / Maintenance / Field Service]". For brand-new (anonymous) prospects, add secondary "Create trade account" CTA.

**Test specification**
- **Hypothesis:** If we add an explicit "Log in for your trade pricing" prompt with clear value framing, then login conversion from PDP will increase and post-login add-to-cart rate will improve because existing customers easily access negotiated rates and re-order workflows (Baymard B2B account research; MEDDIC Champion enablement).
- **Variant A:** No login prompt; list price only for anonymous
- **Variant B:** "Log in for your trade pricing" with value framing + post-login personalized content
- **Primary metric:** PDP-to-login conversion rate
- **Secondary metrics:** post-login add-to-cart rate, re-order rate from PDP, save-to-list rate
- **Expected impact:** +20% to +50% on PDP-to-login conversion (large because baseline is near zero)
- **ICE:** I=7, C=7, E=6 → 6.7
- **Source:** Baymard Institute B2B account research; MEDDIC framework (Champion enablement)

---

## Example 5: 🟠 Important — Technical specifications & documentation (engineered components)

### 🟠 Technical specifications — No downloadable PDF datasheet for stakeholder sharing

**Diagnosis**
The product page shows full technical specifications in an HTML table, but offers no downloadable PDF datasheet for stakeholder sharing. Per MEDDIC's Champion enablement principle, B2B buyers (champions) need shareable artifacts to advocate internally — engineers send datasheets to procurement, procurement forwards to finance, finance archives for compliance. Without a PDF, the champion must screenshot, copy-paste, or print-from-browser to share — all of which lose formatting, brand context, and trust signaling. April Dunford's positioning framework supports this: B2B buyers trust documents (PDF, signed, branded, dated) more than web pages because documents feel "official". For an engineered-component supplier serving specification-driven buyers, this is a significant champion-enablement gap.

**Recommendation**
Generate a branded PDF datasheet for each product, accessible via "Download datasheet (PDF)" button prominent in or near the spec table. The PDF should include: brand logo and contact info, product title and SKU, technical drawing (or rendered CAD preview), full specifications table, certifications list, ordering information, document revision and date. PDF generation can be on-demand from the same product database that renders the HTML page — most B2B platforms (PIM, headless ecom) support this natively. Track datasheet downloads as a meaningful funnel metric (champion-enablement signal).

**Test specification**
- **Hypothesis:** If we add a downloadable branded PDF datasheet to the product page, then quote-request rate, save-to-list rate, and downstream order placement will increase because champions can share authoritative documentation with internal stakeholders (MEDDIC Champion enablement; April Dunford positioning).
- **Variant A:** No PDF datasheet; specs only in HTML table
- **Variant B:** "Download datasheet (PDF)" button with branded PDF generation
- **Primary metric:** quote-request rate or save-to-list rate (whichever is the primary B2B conversion goal)
- **Secondary metrics:** datasheet downloads per page visit, time-to-conversion on sessions with download, multi-session conversion rate
- **Expected impact:** +5% to +12% on primary B2B conversion metric (impact builds over weeks due to longer sales cycle)
- **ICE:** I=6, C=7, E=6 → 6.3
- **Source:** MEDDIC framework (Champion enablement); April Dunford positioning; Edelman B2B Trust Barometer

---

## Example 6: 🟢 Nice-to-have — Cross-sell, accessories & "frequently ordered with" (transactional)

### 🟢 Cross-sell — "Frequently ordered with" section absent for replacement-parts category

**Diagnosis**
The product page (an industrial pump replacement part) shows no "Frequently ordered with" section or accessories block. Per Baymard's B2B cross-sell research, replacement-parts and consumables categories benefit substantially from "frequently ordered with" cross-sell because B2B buyers ordering replacement parts often need related consumables (seals, gaskets, mounting hardware, lubricants) — items they may have forgotten or assumed they have in stock. The current page misses this AOV opportunity entirely. Note: this is Nice-to-have because the impact depends heavily on the actual order patterns (need data to validate which products are genuinely "frequently ordered with"), and implementation requires order-history analysis or algorithm tuning.

**Recommendation**
Add a "Frequently ordered with" section below the spec table containing 4-6 algorithm-driven cross-sell items based on co-purchase history. Each cross-sell card should show: product image, SKU, title, unit price (or "Log in for pricing" if account-gated), tier-price hint, and add-to-cart button. For replacement-parts specifically, group cross-sell by category: "Compatible accessories", "Required consumables", "Recommended spare parts". Ensure cross-sell respects MOQ and pack-size — adding 1 of a 24-unit-pack item should not silently fail. Track cross-sell click-through and incremental cart-add to validate impact.

**Test specification**
Test not recommended yet — research first:
- Analyse order history for actual co-purchase patterns on top-50 SKUs (which products are genuinely ordered together)
- A/B testing requires baseline cross-sell impression and click-through data
- Build algorithm-driven recommendations with at least 90 days of order data behind them

**ICE:** I=4, C=5, E=5 → 4.7

**Source:** Baymard Institute B2B cross-sell research; Iyengar choice overload (lower applicability for B2B)

---

## What makes these examples high-quality

- **B2B-type-aware:** each example signals which B2B type it applies to (transactional, quote-driven, wholesale) and calibrates recommendations accordingly
- **Account-state-explicit:** findings mention whether the observation is from anonymous or logged-in screenshots
- **B2B-frameworks integrated:** MEDDIC, Challenger Sale, April Dunford appear alongside Baymard and Cialdini
- **Specific:** every observation names exact elements with position and behavior
- **Sourced:** every claim references a specific principle, study, or institution
- **Honest about longer sales cycle:** impact estimates note that B2B effects often build over weeks
- **Honest about uncertainty:** when data is missing (cross-sell algorithm needs validation), recommends research rather than test
- **Test-ready:** hypothesis follows "If X, then Y, because Z"; primary metric is B2B-specific (add-to-cart, quote-request, sample-request, save-to-list, downstream order)
- **Concrete copy and behavior:** exact tier-price tables, exact MOQ defaults, exact CTA copy
- **Dutch translations natural:** when output is Dutch, MOQ/PO/RFQ kept as natural untranslated terms where appropriate; "huren" never used

Always match this standard. If a finding can't reach this standard, either dig deeper or remove it from the audit.
