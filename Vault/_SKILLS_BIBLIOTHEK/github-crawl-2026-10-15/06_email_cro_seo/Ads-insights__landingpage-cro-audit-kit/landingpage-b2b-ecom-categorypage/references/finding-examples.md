# Worked finding examples — B2B category page quality calibration

These examples show what a high-quality B2B category page finding looks like across different B2B types and ICE scores. Use them as a reference standard.

---

## Example 1: 🔴 Critical — Filter UX & specification-driven faceting (quote-driven engineered components)

### 🔴 Filter UX — Only 4 facets visible on a 340-product engineered-components category

**Diagnosis**
The category page shows a 340-product result set with only four filter facets visible (brand, price range, in-stock, availability). For an engineered-components category (hydraulic systems with technical specifications spanning capacity, working pressure, materials, mounting type, certification, dimensions), this is structurally insufficient. Per Baymard's B2B filter research, **71% of B2B sites have inadequate filter coverage for category complexity**, and technical-B2B categories typically need 8-15 facets to support specifier shortlisting. The current state forces specifiers to scroll through 340 cards manually to compare specifications — a workflow that fails per Hick's Law (no decision support) and MECLABS (high friction at the moment specifiers most need filtering). For a category serving offshore-wind and heavy-lift engineering customers, the filter gap actively suppresses shortlist creation.

**Recommendation**
Add specification-driven facets matching the category's technical decision criteria. For hydraulic systems, concrete facets:
1. **Capacity** (range slider: L/min)
2. **Working pressure** (range slider: bar)
3. **Mounting type** (multi-select: foot, flange, swivel)
4. **Material** (multi-select: stainless steel, carbon steel, anodized aluminum)
5. **Compliance** (multi-select: CE, ATEX, marine-grade, food-grade)
6. **Connection type** (multi-select: BSP, NPT, JIC, flange)

Show result-count per facet value ("Stainless steel (47)"). Keep most-used facets visible by default; secondary facets behind "Show all filters" expander. Make all filters persistent across pagination and sort changes. Add "Clear all filters" prominent at the top of the filter panel. Use industry-standard terminology (BSP, NPT, ATEX) — not internal taxonomy.

**Test specification**
- **Hypothesis:** If we add specification-driven facets matching engineered-component decision criteria, then filter engagement rate and downstream PDP click-through will increase substantially because specifiers can shortlist 340 products to 5-10 candidates efficiently (Baymard B2B filter research; Hick's Law).
- **Variant A:** 4 facets (brand, price, in-stock, availability)
- **Variant B:** 8-12 specification-driven facets with result-counts and industry-standard labels
- **Primary metric:** filter engagement rate (% sessions using filters)
- **Secondary metrics:** PLP-to-PDP click-through rate, time-to-PDP-click, shortlist usage
- **Expected impact:** +25% to +55% on filter engagement; +10% to +20% on PDP click-through
- **ICE:** I=8, C=8, E=5 → 7.0
- **Source:** Baymard Institute B2B filter research; Hick's Law; MECLABS Conversion Sequence Heuristic

---

## Example 2: 🔴 Critical — Product card content & specification hints (transactional industrial)

### 🔴 Card content — Title and price only; no SKU, no specs, no stock signal

**Diagnosis**
Product cards on the category page show only product title, image, and price. SKU is not visible, no specification hints are shown, no stock or lead-time signal appears, and no certification badges are present. Per Baymard's B2B card research, B2B specifiers and procurement need card-level information to shortlist without clicking into each PDP — the missing content forces every comparison to a PDP visit, multiplying friction. Per April Dunford's "proof through specificity", specifiers trust specific numbers over adjectives — and the current cards offer neither. For a transactional industrial-supply category, the structural gap suppresses PLP-to-PDP click-through quality (visitors click hopefully, leave on PDP).

**Recommendation**
Redesign product cards to surface scan-friendly information. Concrete elements per card:
1. **Title** in customer language
2. **SKU / Part number** directly under title (copy-friendly)
3. **3-5 spec hints** (e.g., "Capacity: 500L/min · Pressure: 250 bar · Material: SS316")
4. **Stock/lead-time signal** ("In stock (240) · Ships today" or "Lead time 2-3 weeks")
5. **Price** with currency and tax-handling ("€4.20 excl. BTW · Tier pricing available")
6. **Certification badges** when relevant (CE, ISO, ATEX)
7. **Quick-add** with quantity selector and MOQ awareness
8. **Compare checkbox** (for comparison-list feature)

Keep card layout consistent across the grid — same image proportions, same content structure. Cards should be scannable in 2-3 seconds for shortlist decisions.

**Test specification**
- **Hypothesis:** If we add SKU, spec hints, stock signal, and certification badges to product cards, then PLP-to-PDP click-through quality (visitors who reach PDP and engage) and PLP-to-cart-add rate will increase because specifiers can shortlist directly from the listing (Baymard B2B card research; April Dunford proof through specificity).
- **Variant A:** Cards with title + image + price only
- **Variant B:** Cards with SKU + 3-5 spec hints + stock + certification + price + quick-add
- **Primary metric:** PLP-to-cart-add rate (or PLP-to-PDP for non-quick-add categories)
- **Secondary metrics:** time-to-PDP-click, PDP bounce rate (lower = better card matching), comparison-list usage
- **Expected impact:** +12% to +25% on PLP-to-cart-add or PDP engagement
- **ICE:** I=8, C=8, E=6 → 7.3
- **Source:** Baymard Institute B2B card research; April Dunford "Obviously Awesome"

---

## Example 3: 🔴 Critical — Product card interaction (wholesale CPG)

### 🔴 Bulk-add — No bulk-add interface despite wholesale repeat-order pattern

**Diagnosis**
The category page (food-service wholesale, 180 SKUs) shows individual product cards with single-product quick-add but no bulk-add interface (no SKU+quantity textarea, no multi-product add-to-cart workflow). For a wholesale-CPG platform where customers routinely reorder 15-40 SKUs per session across categories, this is a structural friction gap. Per Baymard's B2B bulk-add research, bulk-add interfaces yield **15-35% AOV lifts on wholesale categories** by removing the per-SKU click overhead. The current workflow forces a customer reordering a quarterly stock list to click 30 individual SKUs across multiple pages — a workflow that drives customers to phone orders or PDF spreadsheet workarounds.

**Recommendation**
Add bulk-add capability to the category page. Two complementary patterns:
1. **Bulk-add textarea (power-user workflow)**: prominent button "Bulk add SKUs" opening a textarea where customer pastes SKUs and quantities (one per line, e.g., "SKU-12345 24" / "SKU-67890 12"). On submit, validate SKUs, enforce MOQ, add all to cart with summary feedback ("18 items added · 2 SKUs not found · 1 below MOQ").
2. **Multi-add from listing (visual workflow)**: each card has a quantity selector; "Add all to cart" CTA at top of listing adds every card with quantity >0 to cart in one action. Filter affects which products are shown; sort affects ordering.

Both patterns must handle MOQ enforcement gracefully (inline validation, not silent backend error). For repeat customers, integrate with "Saved lists" — a saved list opens with quantities pre-filled, ready to bulk-add.

**Test specification**
- **Hypothesis:** If we add bulk-add textarea and multi-add-from-listing workflows, then category-level AOV and orders-per-session will increase because wholesale repeat-order customers can complete their reorder in one workflow rather than 30+ individual interactions (Baymard B2B bulk-add research; Fitts's Law).
- **Variant A:** Per-card single-add only
- **Variant B:** Per-card quick-add + bulk-add textarea + multi-add-from-listing
- **Primary metric:** category-page-initiated cart AOV
- **Secondary metrics:** SKUs-per-session, time-to-checkout, bulk-add adoption rate, saved-list usage
- **Expected impact:** +18% to +35% on category-page-initiated AOV
- **ICE:** I=9, C=8, E=5 → 7.3
- **Source:** Baymard Institute B2B bulk-add research; Fitts's Law

---

## Example 4: 🟠 Important — Comparison-list & save-for-later patterns (quote-driven technical)

### 🟠 Comparison list — No comparison feature on technical-spec-driven category

**Diagnosis**
The category page (industrial pumps, 47 active products) provides no comparison-list feature: no "Add to compare" checkbox per card, no comparison tray, no side-by-side spec view. For a quote-driven engineering category where specifiers shortlist 3-5 products and compare specifications before quote-requesting, this is a structural workflow gap. Per Baymard's B2B comparison research, **38% of B2B specifiers use comparison tools when available**, and the absence on a technical-spec-driven category suppresses the shortlist-to-quote conversion path. Per MEDDIC's Decision Criteria axis, side-by-side comparison serves the procurement evaluation directly — without it, specifiers either open multiple browser tabs (high cognitive load) or skip detailed comparison (lower confidence in shortlist).

**Recommendation**
Add a comparison feature with three components:
1. **Per-card "Add to compare" checkbox** in a consistent card location (typically top-right)
2. **Persistent comparison tray** at bottom of viewport showing "X products in comparison · View comparison" CTA; persists across pagination, category navigation, and session
3. **Comparison view** with side-by-side spec table: highlighted differences, full spec coverage (matching the PDP spec table), action CTAs per product ("Request quote", "Save to list", "Remove from compare")

Limit comparison to 4 products (5+ becomes unreadable). Allow saving/sharing the comparison ("Save this comparison" creates a saved-list; "Share comparison" generates a shareable URL — valuable for champion-to-procurement advocacy per MEDDIC Champion enablement).

**Test specification**
- **Hypothesis:** If we add a 4-product comparison feature with side-by-side spec view, then specifier shortlist-to-quote conversion will increase because specifiers gain the decision-support tool that matches their evaluation workflow (Baymard B2B comparison research; MEDDIC Decision Criteria + Champion enablement).
- **Variant A:** No comparison feature
- **Variant B:** Per-card compare checkbox + persistent tray + side-by-side comparison view
- **Primary metric:** PLP-to-quote-request conversion rate
- **Secondary metrics:** comparison-list usage rate, average products per comparison, comparison-to-PDP CTR, save-comparison rate
- **Expected impact:** +8% to +18% on PLP-to-quote-request conversion
- **ICE:** I=6, C=7, E=4 → 5.7
- **Source:** Baymard Institute B2B comparison research; MEDDIC framework

---

## Example 5: 🟠 Important — Out-of-stock, lead-time & inventory signals (transactional industrial)

### 🟠 Inventory signals — Generic "in stock" badge without quantity or lead time on technical category

**Diagnosis**
Product cards show "In stock" badges on most cards but provide no quantity ("In stock — 240 units" vs the current "In stock"), no lead-time signal on cards that ARE backordered, and no filter for "in stock only". For a transactional industrial category serving project-driven customers (where lead-time reliability is critical), the binary "in stock" badge fails the specifier's actual question: "Can I get 500 units in time for my project deadline?" Per Baymard's B2B inventory research, specific quantity signals on category cards reduce PDP bounce-back (visitors clicking through to find quantity is insufficient) by 12-22%. Per MECLABS' anxiety axis, lead-time anxiety is high in project-driven B2B contexts — and the current cards don't address it.

**Recommendation**
Three changes:
1. **Specific quantity per card** when quantity exceeds typical order size: "In stock — 240 units at NL warehouse" or "In stock — 1,200+ units"; for low-stock items: "Low stock — 8 remaining"
2. **Lead-time signal on backordered/special-order products** as part of the listing, not hidden: "Backorder · 2-3 week lead time" rather than hiding the card
3. **"In stock only" filter facet** in the filter panel (critical for urgent-need scenarios; valued by project-driven specifiers under deadline pressure)

For multi-warehouse stock, show per-warehouse breakdown on card OR aggregate with location hint ("In stock at 3 warehouses"). Avoid suppressing out-of-stock products from the listing — specifiers still want to know products exist and what the lead time is, especially for shortlisting future orders.

**Test specification**
- **Hypothesis:** If we add specific quantity signals, lead-time on backorders, and "in stock only" filter, then category-page conversion (PLP-to-cart-add) for project-driven customers will increase because lead-time reliability is communicated proactively (Baymard B2B inventory research; MECLABS anxiety reduction).
- **Variant A:** Generic "In stock" badge, no quantity, no lead-time, no in-stock filter
- **Variant B:** Specific quantity + lead-time on backorders + in-stock-only filter
- **Primary metric:** PLP-to-cart-add rate
- **Secondary metrics:** PDP bounce rate (lower when expectations match), filter engagement on "in stock only", time-to-cart-add
- **Expected impact:** +5% to +12% on PLP-to-cart-add rate
- **ICE:** I=6, C=7, E=7 → 6.7
- **Source:** Baymard Institute B2B inventory research; MECLABS Conversion Sequence Heuristic (anxiety axis)

---

## Example 6: 🟢 Nice-to-have — Above-the-fold category framing (commodity transactional B2B)

### 🟢 Category framing — Minimal category intro, but appropriate for commodity transactional B2B

**Diagnosis**
The category page (office paper supplies) shows category heading + product count + immediate product grid, with no extended category intro, no featured-subcategory navigation, and no category-level content. For a commodity transactional B2B category where the dominant buyer job is "find SKU and reorder", this minimal framing is appropriate — extended content competes with filters and products for attention, adding friction without adding value. Per Challenger Sale framework, educational category content matters for expertise-positioned suppliers; commodity transactional B2B competes on product/price/service, not on category-level teaching. Note: this is Nice-to-have because the current state may be correctly aligned to strategy, and changes should be tested rather than assumed.

**Recommendation**
Two paths, depending on strategic position:
1. **If brand position is commodity efficiency**: keep current minimal framing. Don't add educational content that competes with filtering. Optionally test removing even the current intro if scroll-to-filter is suboptimal.
2. **If brand position is expertise + advisory**: add a brief category intro (2-3 sentences) covering category overview, key considerations for buyers, and link to deeper category-buying-guide content. Position above the fold but visually subordinate to filters and products.

Recommend strategic decision first. For a true commodity category, less is more — don't force content where it doesn't add value. For a category where expertise is part of brand differentiation, lightweight educational intro can boost prospect engagement.

**Test specification**
Test optional — strategy decision first:
- Decide whether category-level educational content is part of brand strategy
- If yes: A/B test minimal intro (2-3 sentences) vs current state
- If no: leave category framing minimal and focus on filter/sort/card UX

**ICE:** I=4, C=5, E=8 → 5.7

**Source:** Challenger Sale (Dixon & Adamson); WiderFunnel LIFT model (relevance factor)

---

## What makes these examples high-quality

- **B2B-type-aware:** each example signals which B2B type and calibrates recommendations
- **Account-state-explicit:** findings mention whether observation is from anonymous or logged-in screenshots
- **B2B-frameworks integrated:** MEDDIC, April Dunford, Baymard B2B research appear alongside core CRO frameworks
- **Specific:** every observation names exact card elements, exact filter facets, exact behaviors
- **Sourced:** every claim references specific principle or institution
- **Honest about strategy dependencies:** Example 6 shows how to mark a category as strategy-dependent
- **Test-ready:** hypothesis follows "If X, then Y, because Z"; primary metric is B2B-category-specific
- **Concrete:** exact filter facets, exact card elements, exact bulk-add patterns
- **Dutch translations natural:** "filteropties", "sorteren", "MOQ" used appropriately; "huren" never used

Always match this standard. If a finding can't reach this standard, either dig deeper or remove it from the audit.
