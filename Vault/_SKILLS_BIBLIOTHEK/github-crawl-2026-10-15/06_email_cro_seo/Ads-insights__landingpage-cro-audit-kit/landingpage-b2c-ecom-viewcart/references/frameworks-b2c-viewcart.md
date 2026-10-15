# Frameworks for B2C Ecommerce Cart Page Audits

This reference file contains the CRO frameworks, principles, and applied research used in the cart page audit. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

Many of the categories below involve checking whether an element is **present, absent, or insufficient** on the page. Examples:
- Express-checkout buttons (Apple Pay, Google Pay, Shop Pay — often JavaScript-rendered based on device/browser)
- Free-shipping progress indicators (often only render when below the threshold)
- Discount-code field (sometimes hidden behind "Have a code?" expander)
- Cross-sell carousels (lazy-loaded, may not appear in static HTML)
- Trust badges and payment-method icons (often image-only, invisible in HTML scan)
- Sticky CTAs that only appear after scroll
- Empty-cart messaging (only renders when cart is empty)

**For every finding in these categories, verify the claim against screenshots before delivering.** The most common failure mode is claiming an element is missing when it is visually present but invisible in fetched HTML. A finding that says "no express-checkout" while the page actually has an Apple Pay button is worse than no finding at all — it destroys credibility.

If a finding cannot be visually verified, either:
1. Remove it from the audit, or
2. Convert it to a "research first" finding asking the user to confirm before testing

This rule overrides every other instruction in this file.

---

## CRITICAL — Conditional HTML strings on cart pages

Most ecom platforms ship status strings into the DOM as **conditional placeholders** that JavaScript decides whether to render. The string is always in HTML; the visitor only sees it under specific conditions.

Cart-page-specific examples:
- Shopify: `"You qualified for free shipping"`, `"Add €X for free shipping"`, `"Sold out"`, `"Apply discount code"` — all hardcoded in Liquid templates, conditionally displayed
- WooCommerce: `"Coupon applied"`, shipping calculator strings, fee labels
- Magento: tax-display strings, shipping-method labels, gift-options strings

**Implication for the audit:** finding a free-shipping message string in HTML does NOT mean the visitor sees it (it may only render below threshold). Finding a "discount applied" badge in HTML does NOT mean a discount is active.

**The hard rule:** message state, calculation accuracy, button availability per session, and conditional cart content rely on screenshots only. Never on HTML strings.

A finding may legitimately say: *"the cart page shows no visible progress toward free shipping — consider adding a progress bar to nudge AOV (Baymard shipping-threshold research)"*.

A finding may NOT say: *"the HTML contains a free-shipping message but it's missing — likely a bug"*. That finding is almost always wrong; it is template-default behavior.

---

## Core frameworks (apply across the entire audit)

### Baymard Institute cart usability research
Baymard's longitudinal research identifies the cart page as a heavily underestimated conversion choke point:
- ~30% of all cart-page visitors abandon **on** the cart page (before checkout)
- Average large ecom site has 9-12 cart-page usability issues that materially hurt conversion
- 39% of abandonments are caused by **unexpected costs** (shipping, fees, taxes) — surfaced too late
- 49% of users abandon when they can't see total cost without proceeding to checkout
- Trust signals near the primary CTA increase cart-to-checkout rate by 5-15% in tested implementations

### MECLABS Conversion Sequence Heuristic
C = 4m + 3v + 2(i−f) − 2a
- m = motivation (high on cart page — visitor has chosen items)
- v = clarity of value (must be reinforced; total price + savings + benefits visible)
- i = incentive (free shipping threshold, discount opportunity, urgency if honest)
- **f = friction** (extra steps, hidden costs, confusing layout — biggest controllable lever on cart)
- **a = anxiety** (trust, return policy, security, payment methods — second biggest lever)

On cart pages, **f (friction)** and **a (anxiety)** are the dominant levers. The cart page exists to remove friction and reduce anxiety on the way to checkout.

### Kahneman/Tversky — framing and anchoring
- **Loss aversion** — empty discount-code fields create perceived loss ("I'm missing a discount others have")
- **Anchoring** — showing original price next to discounted price increases perceived value
- **Framing** — "Free shipping" vs "no shipping cost" — same fact, different perception; positive framing wins
- **Endowment effect** — items in cart already feel "owned"; removing them feels like loss → can be leveraged for retention

### Cialdini's principles on cart pages
- **Authority** — payment method icons (Visa, Mastercard, PayPal, iDEAL) signal legitimate operation
- **Social proof** — "12,000+ customers checked out this week" — useful but rarely used on cart pages
- **Reciprocity** — free shipping threshold framed as a gift
- **Scarcity** — "Low stock on this item" — use only when honest and visible per item

### Fogg Behavior Model (B = MAT)
Behavior happens when Motivation, Ability, and a Trigger meet:
- **Motivation:** high on cart page (visitor selected items); maintained by clear value + trust
- **Ability:** must be maximized — single primary CTA, no confusion, fast load, mobile-friendly
- **Trigger:** primary CTA visible above the fold + sticky on mobile scroll

### WiderFunnel LIFT — distraction factor
Cart page is where distraction kills conversion:
- Aggressive cross-sell pushing checkout below the fold
- "Continue shopping" button competing visually with checkout CTA
- Newsletter popup on cart page (worst possible timing)
- Live chat widget covering the CTA area

### Jobs-to-be-Done on cart pages
Visitors arrive on the cart page to do one of three jobs:
1. **Verify** — confirm they picked the right items before committing
2. **Complete checkout** — they're ready, just need the path
3. **Compare totals** — checking final price with shipping/tax before deciding

A well-designed cart page serves all three. Most cart pages over-serve #1 (too much detail) and under-serve #2 (CTA hidden) and #3 (totals confusing).

**Important Dutch translation:** never use "huren" for JTBD framing. Instead: "kiezen voor", "zoeken om X te bevestigen", "bezoekers die X willen".

---

## Category 1: Cart-item presentation & recognizability

### Nielsen Norman recognition-over-recall
Visitors arrive at the cart page from various paths — sometimes minutes after adding items, sometimes hours or days. They need to **recognize** what they added without recalling it. Effective cart items show:
- Product image (consistent crop with PDP image)
- Brand + product name (clearly readable)
- Selected variant (size, color, material)
- Price per item AND quantity multiplier (€19.95 × 2 = €39.90)
- Stock/availability state if relevant (low stock, backorder)

### Baymard cart-item research
- 30% of users have abandoned a cart due to "unable to verify what was added"
- Variant information (size, color) is critical — missing this causes verification anxiety
- Image-text mismatch (image shows color A, label says color B) is a common confidence-killer
- Quantity displayed must match what was added (off-by-one errors break trust)

### Common failures
- Tiny product thumbnails that don't match the PDP hero quality
- Variant not shown ("T-shirt" without "Size M, Blue")
- Price per unit hidden behind hover
- No stock indication when stock is constrained
- Inconsistent product display between cart and PDP (different crop, different angle)

### Brand calibration
- Premium brands: editorial cart-item display with generous whitespace, single line per variant attribute
- Mid-market: full information cart-items with image + brand + name + variant + price + qty
- Value brands: dense cart-items with prominent prices, savings, and any applicable badges

---

## Category 2: Quantity-edit & remove behavior

### Baymard cart-edit research
- 71% of users edit something on the cart page (quantity, removal, variant change)
- Edit friction directly correlates with abandonment
- Best pattern: inline +/- buttons with immediate update; no "Update cart" button required
- Remove should be a single click with optional undo, not a confirm-dialog

### Fitts's Law applied
- Tap targets for +/- and remove must be minimum 44×44px on mobile
- Spacing between +/- and remove must prevent mis-taps
- Hover states on desktop should make interactive elements obvious

### Best practices
- Quantity editor visible directly next to the item (no modal, no separate page)
- Remove button visible but visually de-emphasized (X icon, "Remove" link, or trash icon)
- Optional "Save for later" / wishlist as an alternative to remove
- Undo affordance after removal ("Item removed — Undo")

### Common failures
- Dropdown quantity selector (slower than +/- buttons, hides max-quantity boundary)
- Quantity field that requires Enter or Tab to commit
- "Update cart" button required after edits (extra step that suppresses editing)
- Remove with confirm dialog that adds friction without preventing accidents
- Remove icon too close to product image causing mis-tap on mobile

### Mobile specifics
- +/- buttons must be visibly tappable (not text links)
- Remove must be reachable without accidental product-click
- Swipe-to-delete acceptable but should not be the only option (gesture not discoverable)

---

## Category 3: Subtotal & cost transparency

### Baymard cart-abandonment research
- **39% of cart abandonments are caused by unexpected costs** — the single largest abandonment reason
- Of those, the primary issue is costs revealed too late (in checkout instead of cart)
- Shipping cost is the most common surprise (no shipping calculator on cart page)
- Tax / VAT surprise less common in EU markets (often inclusive) but critical in mixed markets

### Cost transparency hierarchy
1. **Subtotal** (sum of items) — always visible
2. **Shipping** — show on cart page if possible; if zip/country needed, offer calculator
3. **Discount** (if applied) — visible reduction line
4. **Tax / VAT** — explicit when applicable; "Tax included" if inclusive
5. **Total** — visually prominent, larger font, distinct color

### Best practices
- All cost lines stacked in a clear summary box (top-right desktop; below items on mobile)
- "Free shipping" framed as positive ("Free shipping included") not absence
- VAT shown as line item or explicit "Prices include VAT"
- Estimated delivery date if known

### Common failures
- Total shown without breakdown
- "Estimated shipping" or "Calculated at checkout" — Baymard's #1 abandonment trigger
- Tax appearing as a surprise line in checkout when prices excluded VAT
- Discount code applied but no visible reduction line (visitor distrusts application)

### Framing effects
- "€10 shipping" vs "Add €5 for free shipping" — same fact, different perception
- "Total €127.50 (incl. VAT)" vs "€105 + €22.50 VAT" — first feels lower

---

## Category 4: Discount-code field

### Baymard discount-code research
This is one of the most counterintuitive findings in cart UX:
- **Prominent empty discount-code fields cause cart abandonment**
- 27% of users who see an empty discount-code field leave the cart to search for codes
- Of those who leave, ~75% don't return
- Visitor logic: "If there's a discount field, others are getting a discount I'm not"

### The loss aversion mechanism
Empty discount-code field activates loss aversion (Kahneman/Tversky): the visitor perceives they're missing out on what others have. The discount they're searching for is hypothetical, but the loss feels real. They leave to find a code, and the cart is abandoned.

### Best practices
- Hide the discount-code field behind a small "Have a discount code?" expander link
- Or display it but de-emphasize visually (small, grey, below other elements)
- For brands with active campaign codes: auto-apply via URL parameter, no manual entry
- Loyalty-only discounts: gate the field behind login

### When the field SHOULD be prominent
- If discounts are a core part of the brand promise (heavy-discount retailers)
- When a campaign is actively distributing codes and most visitors have one
- When testing shows redemption rate is high enough to justify the abandonment cost

### Common failures
- Empty discount field prominent in cart sidebar
- "Apply" button with no feedback whether the code worked
- Generic error messages ("Invalid code") that don't explain why
- Discount applied without showing the reduction amount

### Brand calibration
- Premium brands: hide discount field entirely or behind a small expander
- Mid-market: expander link, never prominent input
- Value brands / promo-driven: acceptable to be visible but should still de-emphasize

---

## Category 5: Primary CTA to checkout

### Baymard primary-CTA research
The "Proceed to checkout" / "Naar afrekenen" button is the single most important element on the cart page. Best practices:
- **Visual dominance**: loudest element on the page, distinct color from secondary actions
- **Above the fold**: visible without scrolling on both desktop and mobile
- **Copy clarity**: "Proceed to checkout" or "Naar afrekenen" — not "Continue" (ambiguous)
- **Sticky on mobile**: bottom-fixed CTA after scroll past initial position
- **Repeat at bottom**: long carts benefit from a second CTA after the items

### Fitts's Law
- Large tap target (44×48px minimum on mobile, ideally 56-64px)
- Positioned where the thumb naturally rests on mobile (bottom-right or full-width bottom)
- Adequate spacing from other clickable elements

### Common failures
- CTA same color as secondary buttons (continue shopping, save for later)
- CTA below the fold on mobile (visitor scrolls past it and back)
- Copy: "Continue", "Next", "OK" — ambiguous compared to "Proceed to checkout"
- Multiple primary CTAs (checkout + express checkout treated as equals — see category 6)
- Missing sticky behavior on long mobile cart pages
- CTA inside summary box on desktop where it visually competes with totals

### Express vs. primary CTA hierarchy
Express-checkout buttons (Apple Pay, Shop Pay) are valuable but must NOT visually compete with the primary CTA. See category 6 for placement guidance.

---

## Category 6: Express-checkout options

### Baymard express-checkout research
Express-checkout buttons (Apple Pay, Google Pay, Shop Pay, PayPal Express) are high-impact for returning visitors and mobile users:
- Reduce checkout flow by 60-80% (no form filling)
- Mobile express-checkout conversion is 1.5-2x manual checkout
- However, presence does not equal performance — placement and prominence matter

### Best practices
- **Position**: above OR below the primary CTA, with clear visual hierarchy
- **Above the primary CTA**: signals "fast path" — common in Shopify default
- **Below the primary CTA**: signals "alternative path" — common in custom builds
- **Both work**; key is they should not be equal in visual weight to the primary CTA
- Show only relevant methods (Apple Pay on iOS, Google Pay on Android, geographic relevance)
- Include trust indicator: small lock icon, "Secure checkout" microcopy

### Common failures
- Express buttons same size and color as primary CTA, creating choice paralysis
- Showing all methods regardless of device (Apple Pay button on Android user is dead space)
- No express-checkout when 50%+ of traffic is mobile
- Express button placed without separator from primary CTA (visually merges)
- "Buy with Shop Pay" copy that confuses non-Shopify-savvy visitors

### Fogg Behavior Model — trigger optimization
Express-checkout addresses the "ability" axis directly by removing form-filling friction. Combined with the high motivation present on the cart page, this creates near-frictionless conversion for returning users.

### Mobile specifics
- Express-checkout buttons should be visually distinct from primary CTA
- Apple Pay / Google Pay should auto-detect device and show only relevant
- Tap targets minimum 44×48px

---

## Category 7: Trust signals near CTA

### MECLABS anxiety reduction
Trust signals on the cart page reduce the anxiety factor at the moment of commitment. Most effective placements: directly adjacent to or below the primary CTA where the visitor's eye lands at decision time.

### High-value trust signals on cart pages
- **Payment method icons** (Visa, Mastercard, iDEAL, PayPal, Klarna, Apple Pay) — Cialdini authority
- **SSL / Secure checkout indicator** — small lock icon + microcopy
- **Return policy snippet** — "14 dagen retour" / "30-day returns"
- **Money-back guarantee** — if applicable
- **Customer rating** — "9.4/10 op Trustpilot" with link
- **Shipping promise** — "Voor 22:00 besteld, morgen geleverd"

### NL-specific trust signals
- Thuiswinkel Waarborg badge
- WebwinkelKeur / Kiyoh rating
- iDEAL logo prominently shown

### Best practices
- Group 3-5 trust signals in a single visual block near the CTA
- Use icons + microcopy, not icons alone (visitors must understand what each represents)
- Verifiable claims ("9,4/10 from 12,000 reviews") beat vague claims ("Trusted by thousands")
- Maintain brand consistency — no glossy badges on a premium minimalist site

### Common failures
- Trust signals only in the footer (never seen by cart-abandoning users)
- Generic "Secure" badge without context
- Payment method icons in footer instead of near CTA
- "Customers love us" without quantification

---

## Category 8: Free-shipping threshold & AOV nudges

### Baymard shipping-threshold research
Free-shipping nudges are one of the most reliably positive interventions on cart pages:
- Visitors who see "Add €X for free shipping" increase AOV by 10-25%
- Visitors who *already qualify* still benefit from confirmation ("Free shipping included")
- Visual progress indicator (bar showing % to threshold) increases compliance by 5-15% over text alone

### Best practices
- **Below threshold**: "Voeg €7 toe voor gratis verzending" + progress bar + suggested products link
- **Above threshold**: "Gratis verzending inbegrepen ✓"
- Update dynamically as items are added/removed
- Suggest specific products that bring the cart over the threshold (curated cross-sell)
- Show clearly in the cost summary, not as a popup

### Cialdini reciprocity framing
"Free shipping above €X" frames the threshold as a gift the brand offers, not a cost the visitor avoids. The visitor feels they're capturing value, not avoiding loss.

### Common failures
- Threshold not communicated at all (visitor surprised by shipping cost in checkout)
- Threshold communicated as cost ("Shipping €5 below €50") instead of gift framing
- No progress indicator (visitor doesn't know how close they are)
- Threshold message buried in fine print instead of prominent

### Brand calibration
- Premium brands: free shipping should be standard or threshold very high; framing should be subtle
- Mid-market: progress bar + "Add X for free shipping" works well
- Value brands: aggressive threshold communication with prominent progress + recommended add-ons

---

## Category 9: Continue-shopping vs. checkout balance

### WiderFunnel LIFT distraction factor
The "Continue shopping" link/button is necessary but commonly over-prominent:
- Too prominent: distracts visitors from the checkout intent they already have
- Absent: visitors feel trapped, may leave the site entirely instead of returning to PDPs
- Right balance: visible but visually secondary to the primary CTA

### Best practices
- "Continue shopping" as a text link or low-emphasis button, never as a button equal to checkout
- Position: top-left of cart area (return path) or above the items list
- Copy: "Continue shopping" / "Verder winkelen" — not "Back" (ambiguous)
- Optional: contextual "Back to [category]" link based on referrer

### Jobs-to-be-Done balance
Visitors who arrived on cart from PDP are mostly in "complete" mode (job #2). Visitors who arrived from email/saved-cart link may be in "verify" mode (job #1). The cart page must serve both without forcing either path.

### Common failures
- "Continue shopping" as a large button equal to checkout (splits attention)
- No "Continue shopping" option at all (visitor opens new tab to return to PDP, breaking flow)
- "Continue shopping" copy that suggests undoing ("Go back", "Discard cart")
- Both CTA and continue-shopping at the bottom only — neither visible above the fold

---

## Category 10: Cross-sell without distraction

### Baymard cross-sell-on-cart research
Cart-page cross-sell is high-impact when done right and high-damage when done wrong:
- Well-placed cross-sell can increase AOV by 5-12%
- Distracting cross-sell can decrease cart-to-checkout rate by 3-8%
- Best position: below the cart items and totals, never above or competing with the CTA

### Cross-sell logic types
- **Complementary** — accessories for the products in cart (sleeves for a deck box, batteries for an electronic) — highest conversion
- **Frequently bought together** — algorithm-driven pairings based on purchase patterns
- **Recommended for you** — personalized based on cart contents — moderate conversion
- **You may also like** — generic last-resort — lowest conversion, can feel substitutive

### Iyengar choice overload applied
3-5 cross-sell items is the sweet spot. 8+ items creates choice paralysis and dilutes signal.

### Best practices
- Position below totals and CTA, not competing for above-the-fold attention
- Label clearly: "Complete your order with these accessories" not "More products"
- Show price prominently (cross-sell on cart is price-sensitive)
- "Add to cart" button per item with immediate feedback (no PDP detour)
- Skip cross-sell entirely if AOV is high and visitor is at threshold (don't disrupt the checkout intent)

### Common failures
- Cross-sell carousel above the primary CTA (steals attention)
- Substitutive cross-sell ("People also viewed these similar products") that re-opens the comparison loop
- 10+ cross-sell items causing scroll fatigue
- Cross-sell that requires PDP navigation (loses cart context)
- Same cross-sell items repeated across multiple visits (algorithm not refreshing)

### Brand calibration
- Premium brands: minimal cross-sell, often curated by stylist/buyer
- Mid-market: algorithm-driven 3-5 items with clear "add to cart" affordance
- Value brands: aggressive cross-sell with discount badges acceptable

---

## Category 11: Empty-cart state

### Nielsen Norman empty-state research
The empty cart is a frequently overlooked screen:
- ~15-20% of all cart visits encounter an empty state (returning visitors, expired sessions, post-checkout)
- Default empty-cart messages are dead-ends ("Your cart is empty.")
- Effective empty states route the visitor back into the funnel

### Best practices
- Friendly headline that doesn't blame the visitor ("Your cart is empty" not "You haven't added anything")
- Single primary CTA: "Continue shopping" / "Bekijk producten" leading back to a high-converting page (homepage, bestsellers, or last viewed category)
- Show recently viewed products if session data exists
- Show personalized recommendations if returning visitor
- For logged-in users: link to saved carts, wishlist, or order history

### Jobs-to-be-Done on empty cart
The visitor on an empty-cart page is doing one of:
- Returning to a previously-saved cart that has been cleared (frustration risk)
- Following a cart link from email or marketing (broken expectation)
- Post-checkout exploration (positive intent)
- Accidentally clearing cart (recovery need)

Different paths need different routes. A well-designed empty-cart page provides multiple recovery paths.

### Common failures
- Plain text "Your cart is empty" with no CTA
- CTA leads to homepage where the visitor must re-navigate
- No acknowledgment of returning visitors (no recently viewed, no wishlist link)
- Empty cart shown with no header/footer (looks like an error page)

---

## Notes on brand calibration

Always reread the brand snapshot before finalizing recommendations. The same finding category leads to different recommendations depending on brand and AOV:

**Example: Discount-code field**
- Premium brand (AOV €500+): hide entirely behind expander; discount fields cheapen the brand
- Mid-market (AOV €50-200): expander link, never prominent input
- Value brand (AOV €20-80): acceptable to be visible if discount-driven brand promise

**Example: Cross-sell intensity**
- Premium: 2-3 curated items, no badges, editorial framing
- Mid-market: 4-5 algorithm-driven items with clear add-to-cart
- Value: 6-8 items with prominent prices and savings

**Example: Trust signals**
- Premium: minimal but high-quality (1-2 authority signals near CTA)
- Mid-market: full stack (payment icons + return policy + shipping + rating)
- Value: aggressive trust stack with prominent badges

Recommendations that don't match the brand snapshot are wrong, even if they would work for a different brand.

---

## Test-readiness check

Before finalizing each finding, verify:
- [ ] Diagnosis cites a specific principle or source
- [ ] Recommendation is concrete (specific copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z" structure
- [ ] Primary metric is named (cart page metrics: cart-to-checkout rate, AOV, cart-edit rate, cross-sell click-through, session-level conversion)
- [ ] ICE score is justified by the I/C/E breakdown
- [ ] Recommendation matches the brand snapshot and AOV impression
- [ ] Dutch output: no literal jargon translation ("huren" check)

If any box is unchecked, rework the finding before delivering.
