# Worked finding examples — cart page quality calibration

These examples show what a high-quality cart page finding looks like across different categories, brand snapshots, and ICE scores. Use them as a reference standard. Findings should match this depth and specificity — not be vaguer, not be more generic.

---

## Example 1: 🔴 Critical — Subtotal & cost transparency (mid-market apparel, NL)

### 🔴 Subtotal & cost transparency — Shipping cost shown as "calculated at checkout"

**Diagnosis**
The cart page shows subtotal (€84.95) and total (€84.95) but indicates shipping as "berekend bij afrekenen" — calculated at checkout. Per Baymard's cart-abandonment research, **unexpected costs are the #1 reason for cart abandonment (39%)**, and "calculated at checkout" is the most common abandonment-triggering pattern. Visitors arriving on the cart page want to confirm the final total before committing to checkout. When shipping is hidden until step 2 or 3 of checkout, abandonment spikes precisely at the cost-reveal step. The site already has shipping rules (free above €69, €4.95 below) — these can be calculated on the cart page based on subtotal, no zip code required for NL/BE delivery.

**Recommendation**
Display shipping cost on the cart page based on subtotal logic: when subtotal < €69, show "Verzendkosten: €4,95" as a line item; when ≥ €69, show "Verzendkosten: Gratis" with checkmark. Update dynamically as items are added/removed. For international addresses where rates depend on country, default to NL/BE rates with a small "Internationale verzending? Bereken hier" link. Position shipping line between subtotal and total in the order summary box.

**Test specification**
- **Hypothesis:** If we display shipping cost on the cart page based on subtotal logic, then cart-to-checkout rate will increase because visitors see the final cost before committing, removing the #1 abandonment trigger (Baymard cart-abandonment research; MECLABS anxiety reduction).
- **Variant A:** "Verzendkosten: berekend bij afrekenen"
- **Variant B:** Shipping cost calculated and shown dynamically as line item
- **Primary metric:** cart-to-checkout rate
- **Secondary metrics:** checkout abandonment rate at shipping step, session-level conversion
- **Expected impact:** +6% to +14% on cart-to-checkout rate
- **ICE:** I=8, C=9, E=8 → 8.3
- **Source:** Baymard Institute cart-abandonment research; MECLABS Conversion Sequence Heuristic (anxiety factor)

---

## Example 2: 🔴 Critical — Discount-code field (mid-market home goods)

### 🔴 Discount-code field — Empty code field prominent in cart sidebar

**Diagnosis**
The cart page shows an empty "Promocode" input field with "Apply" button prominently in the sidebar, directly above the totals. Per Baymard's discount-code research, **prominent empty discount-code fields cause cart abandonment** — 27% of users encountering this field leave the cart to search for a code, and ~75% of those never return. The mechanism is loss aversion (Kahneman/Tversky): the visitor perceives others are getting a discount they're not. The site does not appear to have an active campaign code distributed via marketing, so most visitors leaving to search will find nothing — and never come back. The discount field is doing more harm than good on this configuration.

**Recommendation**
Hide the discount-code field behind a small text link "Heb je een kortingscode?" positioned below the order summary. The link expands an inline input field when clicked. This preserves redemption functionality for visitors who genuinely have a code (via newsletter or campaign) while removing the abandonment trigger for the majority who don't. For active campaigns where most visitors are expected to have codes: auto-apply via URL parameter instead of manual entry.

**Test specification**
- **Hypothesis:** If we hide the discount-code field behind an expander link, then cart-to-checkout rate will increase because the loss-aversion trigger for code-seeking abandonment is removed for visitors without codes, while preserving redemption for those who have them (Baymard discount-code research; Kahneman/Tversky loss aversion).
- **Variant A:** Empty discount field prominent in sidebar
- **Variant B:** Expander link below summary; field appears on click
- **Primary metric:** cart-to-checkout rate
- **Secondary metrics:** discount-code redemption rate (should not significantly drop), cart-page exit rate
- **Expected impact:** +4% to +10% on cart-to-checkout rate
- **ICE:** I=7, C=9, E=10 → 8.7
- **Source:** Baymard Institute discount-code research; Kahneman & Tversky loss aversion

---

## Example 3: 🔴 Critical — Primary CTA to checkout (premium specialty retailer)

### 🔴 Primary CTA — "Verder" button visually identical to "Verder winkelen"

**Diagnosis**
The cart page has two buttons of similar visual weight: "Verder winkelen" (continue shopping) on the left and "Verder" (continue / checkout) on the right. Both use the same brand color (muted bronze), same size, same outline-only treatment, same typography. Per Baymard's primary-CTA research, the checkout CTA must be visually dominant — the loudest element on the cart page. When secondary actions share visual weight, choice paralysis arises (Hick's Law) and visitors hesitate or click the wrong button. Additionally, "Verder" is ambiguous as checkout copy — Baymard's testing consistently shows "Naar afrekenen" or "Bestel veilig" outperform generic forward-direction copy because they confirm the next-step intent explicitly.

**Recommendation**
Three changes. First, make the checkout CTA visually dominant: filled brand color (not outline), full width within the cart-summary column, 56-64px height. Second, demote "Verder winkelen" to a text link with arrow icon, positioned above the cart items in the top-left ("← Verder winkelen") — visible but visually subordinate. Third, change checkout copy from "Verder" to "Naar afrekenen" (or "Bestel veilig" for stronger anxiety reduction). Maintain the premium brand aesthetic — no aggressive colors, no shadow effects, just clear hierarchy.

**Test specification**
- **Hypothesis:** If we make the checkout CTA visually dominant and change copy from "Verder" to "Naar afrekenen", then cart-to-checkout rate will increase because the primary action is unambiguous and visually prioritized (Baymard primary-CTA research; Hick's Law).
- **Variant A:** Two equal-weight buttons, generic "Verder" copy
- **Variant B:** Dominant filled checkout button with "Naar afrekenen" copy + text-link "Verder winkelen"
- **Primary metric:** cart-to-checkout rate
- **Secondary metrics:** time on cart page, mis-click rate on continue-shopping
- **Expected impact:** +5% to +12% on cart-to-checkout rate
- **ICE:** I=8, C=9, E=9 → 8.7
- **Source:** Baymard Institute primary-CTA research; Hick's Law; visual hierarchy principles

---

## Example 4: 🟠 Important — Free-shipping threshold & AOV nudges (mid-market NL retailer)

### 🟠 Free-shipping threshold — No progress indicator toward €50 threshold

**Diagnosis**
The site offers free shipping above €50, but the cart page (subtotal €37.45) shows no progress indication or nudge toward the threshold. Per Baymard's shipping-threshold research, visible progress bars with "Add €X for free shipping" copy increase AOV by 10-25% on average. The current cart shows only the shipping cost as a line item ("Verzendkosten: €4,95") — the visitor sees the cost but not the easy escape from it. Cialdini's reciprocity principle is unused: framed correctly, the threshold becomes a gift the brand offers rather than a cost the visitor pays. The €12.55 gap to free shipping is small enough that a single product addition typically bridges it.

**Recommendation**
Add a progress bar in the order summary, between subtotal and shipping line. Above the bar: "Nog €12,55 tot gratis verzending". Below: a 4-step suggested-product strip showing 3-4 items in the €10-25 range that would bridge the gap. Update dynamically as items are added. When the threshold is crossed: replace with "✓ Gratis verzending inbegrepen" with a small checkmark. Visual style consistent with brand (no aggressive colors, clean typography).

**Test specification**
- **Hypothesis:** If we add a progress indicator and suggested-products nudge to bridge the free-shipping threshold, then average order value will increase because visitors below the threshold see the small gap and have one-tap product additions to close it (Baymard shipping-threshold research; Cialdini reciprocity framing).
- **Variant A:** No threshold indication on cart
- **Variant B:** Progress bar + "Add €X for free shipping" + 3-4 suggested products
- **Primary metric:** average order value (sessions starting below threshold)
- **Secondary metrics:** cart-to-checkout rate (must not decrease), cross-sell click-through, % sessions crossing threshold
- **Expected impact:** +6% to +18% on AOV for sub-threshold sessions
- **ICE:** I=7, C=8, E=6 → 7.0
- **Source:** Baymard Institute shipping-threshold research; Cialdini's reciprocity principle

---

## Example 5: 🟠 Important — Trust signals near CTA (mid-market Dutch webshop)

### 🟠 Trust signals — No payment-method icons or return policy near checkout button

**Diagnosis**
The "Naar afrekenen" button stands alone in the cart-summary area with no surrounding trust signals. Below the button is direct whitespace; payment-method icons appear only in the footer, and the return policy is buried in a navigation submenu. Per MECLABS' Conversion Sequence Heuristic, anxiety reduction at the moment of commitment is one of the two biggest controllable conversion levers on the cart page. The visitor commits to checkout from a position of incomplete trust — they don't know which payment methods are accepted, what the return policy is, or whether the transaction is secure. Baymard's research shows trust signals adjacent to the primary CTA increase cart-to-checkout rate by 5-15% in tested implementations.

**Recommendation**
Add a compact trust block directly below the "Naar afrekenen" button containing: (1) row of 5-6 payment-method icons (iDEAL, Visa, Mastercard, PayPal, Klarna, Apple Pay), (2) small lock icon + "Veilige betaling" microcopy, (3) one-line return-policy snippet "14 dagen retour — gratis", (4) shipping promise if applicable "Voor 22:00 besteld, morgen geleverd". Keep the visual style restrained: small icons, secondary text color, consistent typography. The block should feel reassuring, not loud.

**Test specification**
- **Hypothesis:** If we add a compact trust block directly below the checkout CTA containing payment methods, security, and return policy, then cart-to-checkout rate will increase because the highest-anxiety questions are answered at the moment of commitment (MECLABS anxiety reduction; Baymard trust-element placement research).
- **Variant A:** Checkout CTA with no adjacent trust signals
- **Variant B:** Checkout CTA + trust block (payment icons + secure + return + shipping)
- **Primary metric:** cart-to-checkout rate
- **Secondary metrics:** time on cart page, session-level conversion
- **Expected impact:** +3% to +9% on cart-to-checkout rate
- **ICE:** I=6, C=8, E=9 → 7.7
- **Source:** MECLABS Conversion Sequence Heuristic (anxiety factor); Baymard Institute trust-element placement research; Cialdini authority principle

---

## Example 6: 🟢 Nice-to-have — Empty-cart state (premium curated brand)

### 🟢 Empty-cart state — Generic "Your cart is empty" message with no recovery path

**Diagnosis**
When the cart is empty (visible in empty-cart screenshot), the page shows only "Je winkelwagen is leeg" centered in the content area, with no CTA, no recently-viewed products, no link to recommendations, and no wishlist access. Per Nielsen Norman's empty-state research, the empty cart is a frequently overlooked screen that ~15-20% of cart visits encounter — returning visitors, expired sessions, post-checkout exploration. A dead-end empty state forces visitors to navigate elsewhere or leave entirely. Premium brands often under-invest in this screen because they assume visitors arrive with intent — in reality, returning visitors using saved-cart links, post-purchase explorers, and visitors with expired sessions all encounter it regularly. JTBD applies: each visitor on an empty cart has a different recovery need.

**Recommendation**
Replace the bare message with a layered recovery screen containing: (1) friendly headline "Je winkelwagen is leeg — laten we iets moois vinden" (no blame, sets exploration tone), (2) prominent CTA "Bekijk de collectie" linking to the highest-converting category or curated collection page, (3) if recently-viewed session data exists: a "Recent bekeken" row of 3-4 items with quick add-to-cart, (4) for logged-in users with wishlist items: small link "Of bekijk je opgeslagen items (X)". Maintain the brand's editorial aesthetic — no aggressive promotional elements, no popup-style design.

**Test specification**
- **Hypothesis:** If we replace the bare empty-cart message with a layered recovery screen including a primary CTA and recently-viewed products, then session-level conversion among empty-cart-visiting sessions will increase because visitors have multiple recovery paths into the funnel (Nielsen Norman empty-state research; Jobs-to-be-Done).
- **Variant A:** "Je winkelwagen is leeg" message only
- **Variant B:** Headline + CTA to curated collection + recently viewed + wishlist link (for logged-in users)
- **Primary metric:** session-level conversion (sessions encountering empty-cart state)
- **Secondary metrics:** click-through from empty-cart page, time-to-first-PDP-click after empty-cart encounter
- **Expected impact:** moderate impact on empty-cart-session recovery rate (lower volume but high opportunity)
- **ICE:** I=4, C=6, E=8 → 6.0 (nice-to-have because affected visitor volume is smaller than other categories)
- **Source:** Nielsen Norman Group empty-state research; Jobs-to-be-Done framework

---

## What makes these examples high-quality

- **Specific:** every observation names an exact element with position and behavior
- **Sourced:** every claim references a specific principle, study, or institution
- **Brand-aware:** recommendations consider whether they fit the brand snapshot (premium vs mid-market vs value) and AOV impression
- **Honest about uncertainty:** when data is missing, the finding says so and recommends research, not action
- **Test-ready:** hypothesis follows "If X, then Y, because Z"; primary metric is named (cart page metrics: cart-to-checkout rate, AOV, cart-edit rate, cross-sell click-through, session-level conversion); ICE is justified by the breakdown
- **Concrete copy and behavior:** not "improve the CTA" — actual button copy, exact position, specific trust elements
- **Dutch translations natural:** when output is Dutch, JTBD framing avoids "huren"; terms like "winkelwagen", "afrekenen", "verzendkosten" used naturally; English terms like "discount code" optionally kept untranslated when clearer

Always match this standard. If a finding can't reach this standard, either dig deeper or remove it from the audit.
