# Frameworks for B2B Ecommerce Cart Page Audits

This reference file contains the CRO and B2B-specific frameworks, principles, and applied research used in the B2B cart page audit. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

B2B cart pages are uniquely prone to fabricated findings because cart state is dynamic and account-state-dependent:
- MOQ enforcement messages (only render when item below MOQ)
- Tier-pricing updates (only render when quantity crosses tier)
- BTW/VAT toggling (depends on customer registration)
- Save-as-list interfaces (often modal, only on click)
- Quote-conversion CTAs (often feature-flagged per account)
- Multi-shipping split (only renders when toggled)
- Approval-workflow CTAs (only for requester-role accounts)

**For every finding, verify against screenshots before delivering.**

---

## CRITICAL — Account-state awareness

B2B cart pages render fundamentally differently for:
- Anonymous (often required to log in before checkout)
- Logged-in standard customer (visible tier pricing, account-specific MOQ)
- Approver-role (sees pending-approval carts from team requesters)
- Procurement-system session (simplified UX)

**Always identify which account-state the screenshot represents.**

---

## CRITICAL — Stay out of security and compliance territory

Cart-to-checkout transitions touch payment-related territory. **Do not comment on security or compliance:**
- A finding may RECOMMEND adding visible trust signals
- A finding may NOT claim the cart is "secure" or "AVG-compliant"
- A finding may NOT claim BTW handling is "correct" or "incorrect"

---

## CRITICAL — B2B type-specific calibration

The four B2B types require different cart approaches:

**Transactional B2B ecom:**
- Standard cart-to-checkout flow
- Tier-pricing updates visible
- Save-as-list as secondary
- Most similar to B2C cart

**Quote-driven B2B:**
- Cart functions as quote-builder
- "Request quote for this cart" primary CTA alongside or instead of "Checkout"
- No immediate-payment expectation

**Wholesale (trade):**
- Large multi-SKU carts (15-50+ items typical)
- Bulk-update essential
- Save-as-list for recurring orders critical
- MOQ enforcement frequent

**Hybrid:**
- Cart supports both checkout AND quote-conversion
- Per-line "Add to quote" + "Add to order" possible

---

## Core frameworks (apply across the entire audit)

### Baymard Institute B2B cart research
- B2B cart abandonment averages 32-44% (higher than B2C's 26% due to longer evaluation cycles)
- Multi-stakeholder cart-handling (champion builds cart, approver approves) creates 12-22% additional friction
- Save-as-list features yield 8-18% multi-session conversion lift

### MEDDIC framework on B2B cart
- **Metrics:** cart must show clear cost math (per-line, subtotal, BTW, total)
- **Economic buyer:** cart must support requester-then-approver flow
- **Decision criteria:** cart must support PO/cost-center assignment
- **Decision process:** "Save as list" supports multi-session decision-making
- **Identify pain:** unclear cart cost-math causes abandonment ("How much will I actually pay?")
- **Champion enablement:** "Share this cart" / "Save as quote" lets champion advocate internally

### Challenger Sale on B2B cart
B2B buyers respond to confident, clear flows:
- Transparent cost math
- Clear next-step options (checkout / quote / save / share)
- Educational microcopy where needed (MOQ explanation, tier benefit, lead time)

### MECLABS Conversion Sequence Heuristic on B2B cart
- **m (motivation):** very high at cart-page (deep funnel)
- **v (value):** reinforced via persistent cost-breakdown + savings clarity
- **i (incentive):** tier-discount visible, free-shipping threshold visible
- **f (friction):** unclear costs, hidden BTW, MOQ surprises
- **a (anxiety):** delivery reliability, payment terms, return policy

### Fogg Behavior Model (B = MAT) on B2B cart
Cart-page Ability is dominant lever:
- One-click quantity edit
- Inline MOQ feedback
- One-click save-as-list
- Clear CTA hierarchy

### Cialdini on B2B cart
- **Authority** — payment-method icons, lead-time signals
- **Liking** — visible account-manager contact for high-AOV carts
- **Reciprocity** — tier savings framed as gift ("Save €X by upgrading 50 units")
- **Commitment** — cart is commitment moment; respect it

### Nielsen Norman heuristics applied to B2B cart
- **#1 Visibility** — cost math, MOQ, lead time visible
- **#5 Error prevention** — inline MOQ + tier feedback
- **#6 Recognition over recall** — per-line cost breakdown + cart-line images
- **#9 Help users recover** — clear path when MOQ violated, when item OOS

### Jobs-to-be-Done on B2B cart
B2B visitors on a cart page are doing one of:
1. **Review-and-checkout** — fastest path to checkout
2. **Save-for-approval** — save cart, submit to approver
3. **Convert-to-quote** — turn cart into quote-request
4. **Save-for-later** — save as recurring list for next session
5. **Bulk-edit** — update quantities across many lines

**Important Dutch translation:** never use "huren" for JTBD. Use "kiezen voor", "afrekenen", "opslaan voor later".

---

## Category 1: Cart-item presentation & order verification

### Baymard B2B cart research
B2B cart items need different content than B2C:
- SKU/part number visible (procurement workflow)
- Spec hint (key spec for verification)
- Pack-size context ("24 per case × 5 cases")
- Unit-price + total-per-line clear
- Tier-price hint when applicable
- Stock/lead-time signal per line
- Image (sufficient for verification)

### Nielsen Norman recognition over recall
Cart-item presentation supports recall:
- "Did I actually order this configuration?"
- "Is this the right SKU for my project?"
- "How many cases vs pieces did I add?"

### Best practices
- Per-line: image + title + SKU + key specs + qty + unit-price + total
- Pack-size context visible
- Tier-price applied + hint to next tier
- Stock/lead-time per line
- Edit/remove one-click

### Common failures
- B2C-style minimal lines (title + qty + price only)
- SKU absent
- Pack-size context invisible (visitor unsure if 24 = pieces or cases)
- No per-line tier-price
- No stock/lead-time per line

---

## Category 2: Quantity-edit, MOQ enforcement & bulk-update

### Baymard B2B quantity research
B2B quantity editing differs from B2C:
- Quantities often large (24, 100, 500, 1000)
- MOQ enforcement critical (avoid silent backend errors)
- Tier-price updates real-time when quantity crosses tier
- Bulk-update (multiple lines at once) for large carts

### Hick's Law on quantity edit
- One-step quantity edit (number input) beats per-card +/- for large quantities
- Pack-size hint inline ("Sold per case of 24" next to qty)
- "Increase to next tier (50 — save €X)" suggestion

### Best practices
- Direct number input for quantity (not just +/-)
- Inline MOQ feedback ("Min. 12 units")
- Tier-price update on quantity change (immediate, not on submit)
- Bulk-update interface for carts with 10+ lines
- "Apply 0 to all" option for clearing
- Pack-size hint per line

### Common failures
- +/- only buttons (slow for large quantities)
- MOQ enforced silently (error after checkout-click)
- Tier-price updates only after submit
- No bulk-update for large carts
- Quantity edit triggers full page reload

---

## Category 3: Cost transparency, tier-pricing & BTW handling

### Baymard B2B pricing on cart page
Cost transparency on B2B cart:
- Per-line: unit price × qty = line total
- Tier-price applied + savings indicated
- Subtotal (excl. BTW)
- Shipping cost (or "calculated at checkout")
- BTW line clear (excl/incl/reverse-charge)
- Total (final)

### Kahneman/Tversky anchoring
Tier savings framed as gain:
- "Save €120 — upgrade to next tier (50 units)"
- "Volume discount applied: -€340"

### Best practices
- Per-line cost breakdown visible
- Tier-discount visible per line + cart total
- Subtotal + BTW + shipping + total clear
- Currency + tax handling explicit
- Free-shipping threshold visible (if applicable)
- BTW-reverse-charge note for intra-EU customers

### Common failures
- Only cart total visible (no per-line)
- Tier-discount hidden
- BTW handling ambiguous ("Total: €X — incl. or excl.?")
- Shipping cost "calculated later" without estimate
- Free-shipping threshold hidden

### Note on tax scope
A finding may comment on UX of tax presentation. A finding may NOT claim tax calculations are correct or incorrect.

---

## Category 4: PO/reference assignment & internal codes

### Baymard B2B procurement-field research
PO and reference fields are decision-critical for procurement:
- PO can be assigned at cart-stage (lets requester save with PO before approval)
- Cost center per cart or per line
- Internal reference / project code
- Notes field for delivery instructions

### MEDDIC — Decision process
PO at cart-stage supports the multi-session B2B workflow:
- Requester builds cart, assigns PO, submits for approval
- Approver reviews cart with PO already attached
- Order placed reflects PO from cart-stage

### Best practices
- PO field optional at cart-stage (mandatory at checkout if account requires)
- Cost-center dropdown of valid options
- Project code free text or dropdown
- Notes for delivery instructions
- Save PO format for next time

### Common failures
- PO only at checkout (forces re-entry if requester saves cart and returns later)
- No cost-center support
- PO format unspecified
- Notes field absent

### B2B type calibration
- Transactional: PO optional at cart-stage
- Invoice/NET B2B: PO often required
- PO-driven: PO mandatory, prominent at cart-stage
- Hybrid: visibility per account configuration

---

## Category 5: Primary CTA: proceed to checkout vs request quote vs save

### Baymard B2B CTA on cart page
B2B cart pages often need multiple CTAs:
- Primary: "Proceed to checkout" (transactional B2B)
- Or primary: "Request quote for this cart" (quote-driven B2B)
- Secondary: "Save as list" / "Save and continue shopping"
- Tertiary: "Share cart" / "Send to approver"

### Hierarchy matters
Multiple equal CTAs create paralysis. Hierarchy:
- Primary CTA: dominant action for B2B type
- Secondary CTA: alternative path (quote vs checkout)
- Tertiary: workflow support (save, share, send-for-approval)

### Fogg Behavior Model
Ability maximized when CTA-action mapping is clear:
- "Plaats bestelling" / "Place order" → checkout
- "Vraag offerte aan" / "Request quote" → quote conversion
- "Verstuur voor goedkeuring" / "Submit for approval" → approval workflow
- "Opslaan als lijst" / "Save as list" → save for later

### Best practices
- Primary CTA visually dominant + amount-adjacent
- Secondary CTAs visible but de-emphasized
- "Save as list" for repeat-order workflows
- "Send for approval" for approval-workflow accounts
- "Convert to quote" for hybrid B2B

### Common failures
- All CTAs visually equal
- "Place order" only (no quote-conversion path)
- No save-as-list option
- Approval-workflow accounts see "Place order" (misleading — same issue as in checkout)

### B2B type calibration
- Transactional: checkout primary, save-as-list secondary
- Quote-driven: request-quote primary, save secondary
- Wholesale: checkout primary, save-as-list secondary
- Hybrid: per-cart context

---

## Category 6: Trust signals, lead-time & shipping signals

### MECLABS anxiety on B2B cart
B2B cart anxiety:
- "Will this arrive when I need it?"
- "Will the invoice payment terms work?"
- "Are returns possible if there's a problem?"

### Best practices
- Lead-time visible per line (or aggregate)
- Shipping cost estimated (or threshold for free)
- Return policy linked
- Payment-method icons visible (anchoring expectation)
- Customer-service contact

### Common failures
- No lead-time on cart
- Shipping cost hidden
- Return policy absent
- Trust signals only in footer

---

## Category 7: Save-as-list, recurring order & multi-session workflows

### Baymard B2B save-list research
Save-as-list highest-leverage for B2B repeat customers:
- 8-18% multi-session conversion lift
- Saved lists support recurring-order workflow (monthly stock, quarterly stock)
- Multi-list organization for different customer departments

### JTBD framework
B2B save-list jobs:
- Recurring stock order (save and reorder monthly)
- Multi-stakeholder approval (save, send to approver)
- Multi-session evaluation (save, return next week to finalize)
- Spec library (save canonical product configurations)

### Best practices
- "Save as list" one-click from cart
- Name the list (e.g., "Engineering quarterly", "Maintenance recurring")
- "Save and continue shopping" preserves cart-as-list
- "Load saved list to cart" prominent in account
- Multi-list management in account dashboard

### Common failures
- Save-as-list absent
- Saved lists hidden in account
- Cannot name lists
- Load-to-cart workflow broken (must add SKUs individually)

---

## Category 8: Quote-conversion path (cart → quote request)

### B2B hybrid workflow
Many B2B platforms support both checkout AND quote-conversion from cart:
- Customer builds cart of products
- Optionally clicks "Request quote for this cart" → triggers quote-request workflow
- Sales team responds with custom quote (volume discount, custom terms)

### When relevant
- Hybrid B2B platforms (transactional + quote-driven products)
- High-AOV carts (often above threshold trigger quote opportunity)
- Multi-product carts requiring custom terms

### Best practices
- "Request quote for this cart" CTA visible for eligible accounts/carts
- Quote-request preserves cart contents (sales team sees what customer assembled)
- Expected response time stated ("Quote within 4 business hours")
- Customer can convert quote back to checkout if standard terms accepted

### Common failures
- No quote-conversion path despite hybrid B2B model
- Quote-request loses cart contents
- No response-time expectation
- Quote-to-checkout conversion broken

### B2B type calibration
- Transactional: quote-conversion usually not needed
- Quote-driven: quote-conversion IS the primary path
- Wholesale: quote-conversion for high-AOV custom orders
- Hybrid: both paths essential

---

## Category 9: Cross-sell, accessories & "frequently ordered with"

### Baymard B2B cross-sell on cart
B2B cart cross-sell differs from B2C:
- Required-accessories highest leverage (cables, mounting, consumables)
- Replacement parts for items in cart
- "You forgot" cross-sell ("Items often ordered with X")
- Less B2C-style "you may also like"

### Iyengar choice overload
B2B tolerates more cross-sell IF categorized:
- "Required accessories" vs "Compatible products" vs "Frequently ordered"

### Best practices
- Cross-sell categorized clearly
- Required-accessories prominent (compatibility-driven)
- Replacement-parts section for installed-base items
- Cross-sell respects MOQ
- Easy add-to-cart from cross-sell

### Common failures
- Cross-sell mixed (accessories + alternatives + unrelated)
- No clear "required" signaling
- B2C-style "you may also like" with weak relevance
- Cross-sell pricing without tier context

---

## Category 10: Empty-cart state & continued-shopping behavior

### Nielsen Norman empty-state research
Empty-cart state matters more in B2B than B2C:
- B2B visitors often arrive at cart by navigation accident
- "Continue shopping" must route well (last category, saved lists, reorder)
- Empty cart is recovery opportunity

### Best practices
- Empty-cart state with clear recovery paths
- "Continue shopping" → last category
- "Reorder previous order" → quick reorder
- "Load saved list" → recurring workflow
- "Speak to specialist" for high-consideration B2B

### Common failures
- Generic "Your cart is empty" with no recovery
- No saved-list access from empty cart
- No reorder option from empty cart
- "Continue shopping" routes to homepage (wastes navigation)

---

## Category 11: Mobile experience

### Baymard mobile B2B cart research
B2B mobile cart:
- Field-sales context: sales rep showing customer on tablet
- Approval-workflow on mobile (approver reviews on phone)
- Bulk-update mobile-challenging
- Cost-math must be scannable on small screen

### Best practices
- Sticky CTA at bottom (mobile)
- Per-line edit collapse/expand
- Bulk-update via mobile-friendly interface
- Cost-math always visible (sticky total)
- Save-as-list one-tap

### Common failures
- Desktop cart ported to mobile
- Cost-math hidden behind scroll
- Bulk-update unusable on mobile
- Edit buttons too small (Fitts's Law violation)
- Sticky CTA absent

---

## Brand calibration notes

Always recalibrate by brand snapshot AND B2B type:

**Example: Primary CTA**
- Transactional: "Proceed to checkout — €X"
- Quote-driven: "Request quote for this cart"
- Wholesale: "Proceed to checkout — €X" (post-login)
- Hybrid: dual CTA "Checkout — €X" + "Request quote instead"

**Example: Save-as-list emphasis**
- Transactional: secondary
- Quote-driven: less critical
- Wholesale: prominent (recurring orders essential)
- Hybrid: layered

**Example: Cost transparency**
- High-AOV B2B: full per-line breakdown + BTW handling explicit
- Low-AOV high-frequency: simplified cost-math acceptable
- Quote-driven: cart cost-math less critical (final pricing in quote)

Recommendations that don't match brand AND B2B type are wrong.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites specific principle
- [ ] Recommendation concrete
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric B2B-cart-specific (cart-to-checkout, cart abandonment, cart-to-quote, save-as-list, quantity-edit completion)
- [ ] ICE justified by I/C/E breakdown
- [ ] Recommendation matches brand AND B2B type
- [ ] Account-state assumption explicit
- [ ] No security/compliance claims
- [ ] No tax-correctness claims
- [ ] Dutch output: no "huren" check

If any unchecked, rework before delivering.
