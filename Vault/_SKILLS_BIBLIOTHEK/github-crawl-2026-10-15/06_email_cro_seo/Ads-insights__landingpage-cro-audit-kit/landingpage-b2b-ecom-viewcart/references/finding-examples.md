# Worked finding examples — B2B cart page quality calibration

These examples show what a high-quality B2B cart page finding looks like across different B2B types and ICE scores. Use them as a reference standard.

---

## Example 1: 🔴 Critical — Quantity-edit, MOQ enforcement & bulk-update (wholesale CPG)

### 🔴 MOQ enforcement — MOQ violation surfaces only at checkout, not on cart line

**Diagnosis**
The cart page shows 18 SKUs with quantities at or above MOQ except one line (SKU-78432, ordered at 8 pieces when MOQ is 12). The cart page renders no MOQ warning on the offending line — no inline message, no visual highlight, no minimum-required indicator. The visitor proceeds to checkout believing the cart is valid, encounters a backend error at checkout-step-1, and must return to the cart to fix. Per Baymard's B2B quantity research, silent MOQ enforcement is one of the top-3 highest-abandonment patterns in wholesale ecom — and the cart page is the appropriate surface for MOQ feedback per Nielsen Norman's error-prevention heuristic. For a wholesale CPG platform serving boutique retailers (who routinely build 15-30 SKU carts), MOQ violations are common but should be communicated proactively, not as a checkout surprise.

**Recommendation**
Add inline MOQ enforcement on the cart page. Concrete pattern:
1. **Inline warning per offending line**: red border + microcopy "Minimum 12 pieces required for this SKU · You have 8 · Add 4 more"
2. **One-click fix CTA**: "Increase to 12" button next to the warning, auto-updates the quantity
3. **Cart-level summary banner**: top of cart shows "1 item below MOQ · Fix to proceed" with anchor link to the offending line
4. **Checkout CTA disabled** while MOQ violations exist, with hover/tap microcopy explaining why
5. **Pack-size hint** on every line ("Sold per case of 12") to prevent the issue at source

Implementation requires cart-rendering to validate against MOQ rules on every state change (qty edit, item add, item remove). Modern cart platforms support this natively; legacy platforms may need work.

**Test specification**
- **Hypothesis:** If we add inline MOQ enforcement on the cart page (warning + fix-CTA + checkout-CTA gating), then cart-to-checkout conversion will increase and post-checkout MOQ-error abandonment will decrease because visitors are prevented from proceeding with invalid carts (Baymard B2B quantity research; Nielsen Norman error-prevention).
- **Variant A:** No cart-level MOQ enforcement; errors surface at checkout
- **Variant B:** Inline cart-line warnings + one-click fix + cart-banner + disabled checkout CTA
- **Primary metric:** cart-to-successful-checkout conversion rate
- **Secondary metrics:** MOQ-error-correction rate, checkout-step-1 abandonment from MOQ, time-from-cart-to-checkout-complete
- **Expected impact:** +8% to +18% on cart-to-successful-checkout conversion
- **ICE:** I=8, C=8, E=6 → 7.3
- **Source:** Baymard Institute B2B quantity research; Nielsen Norman heuristic #5 (error prevention)

---

## Example 2: 🔴 Critical — Cost transparency, tier-pricing & BTW handling (transactional industrial)

### 🔴 Cost transparency — Only cart total visible; no per-line cost, BTW handling ambiguous

**Diagnosis**
The cart page shows 14 line items with title, image, quantity, and remove button per line — but no per-line cost. Only a cart total appears at the bottom: "Total: €1,847.20". There is no subtotal, no BTW line, no shipping estimate, no per-line unit-price × quantity = line-total breakdown. For a transactional industrial customer who has built a 14-SKU cart, this is structural cost-blindness — the visitor cannot verify the math, cannot identify which line is the cost driver, cannot confirm whether tier-discounts have been applied, and cannot tell whether the total is excl. or incl. BTW. Per Baymard's B2B pricing research, cost transparency on B2B cart is a 5-10% conversion-lift opportunity (more on high-AOV carts). Per Kahneman/Tversky, anchoring works only when buyers can see the math.

**Recommendation**
Add full per-line and cart-level cost transparency. Concrete elements:
1. **Per-line cost**: unit price × quantity = line total, with tier-discount badge if applied ("€4.20 × 100 = €420 · Tier discount: -€60 · Net: €360")
2. **Cost summary section** (above CTA): Subtotal (excl. BTW) → BTW (or "BTW-verlegd" for intra-EU B2B) → Shipping (estimated or "calculated at checkout") → Total
3. **Tax handling explicit**: label "Prices excl. BTW" or equivalent throughout; BTW line on summary
4. **Free-shipping threshold visible** if applicable ("Free shipping above €2,500 — add €653 more")
5. **Currency clear** (€ vs $ vs £ for international visitors)

Update cost math in real-time on quantity changes — visitors confirming a cart make multiple small edits and need immediate feedback. Note: this audit covers UX of cost presentation, not validity of the tax calculation itself.

**Test specification**
- **Hypothesis:** If we add per-line cost breakdown, tier-discount visibility, and explicit BTW handling on the cart page, then cart-to-checkout conversion will increase because visitors can verify the math and confirm savings before committing (Baymard B2B pricing research; Kahneman/Tversky anchoring).
- **Variant A:** Only cart total visible; no per-line cost
- **Variant B:** Full per-line breakdown + cost summary section + explicit BTW handling
- **Primary metric:** cart-to-checkout conversion rate
- **Secondary metrics:** cart-edit rate, time-on-cart, abandonment after cart view
- **Expected impact:** +5% to +12% on cart-to-checkout conversion (more for high-AOV carts)
- **ICE:** I=7, C=8, E=8 → 7.7
- **Source:** Baymard Institute B2B pricing research; Kahneman & Tversky anchoring; Nielsen Norman recognition over recall

---

## Example 3: 🔴 Critical — Primary CTA: proceed to checkout vs request quote (hybrid B2B)

### 🔴 Primary CTA — "Place order" only; no quote-conversion path despite €18,000 cart

**Diagnosis**
The cart page (industrial equipment supplier) shows an €18,000+ cart with 6 line items, primary CTA "Place order — €18,247". No "Request quote for this cart" CTA appears, despite the cart value being well above the threshold where custom-quote workflows typically apply for this category. For a hybrid B2B supplier (catalog products available immediate-order AND custom quote-driven sales), this is a missed conversion path: customers with high-AOV carts often want custom terms (volume discount, extended payment, customized shipping) but cannot access the quote-workflow without abandoning checkout to phone or email the sales team. Per Baymard's hybrid B2B research, providing both "Checkout" and "Request quote" CTAs on high-AOV carts captures 8-18% of carts that would otherwise abandon for off-platform sales contact. Per MEDDIC's Decision Process, high-AOV B2B decisions typically involve custom-term negotiation — restricting cart-conversion to standard-terms-only misses that workflow.

**Recommendation**
Add quote-conversion path on the cart page. Concrete pattern:
1. **Dual primary CTAs above-the-fold**: "Place order — €18,247" + "Request quote for this cart" with clear visual distinction (primary filled, secondary outlined or text-link prominent)
2. **Quote-CTA threshold**: appears automatically when cart exceeds threshold (e.g., €5,000 for this category) OR for all logged-in customers with NET payment terms
3. **Quote-workflow preserves cart**: clicking "Request quote" opens a form prefilled with cart contents; submission notifies sales team with full cart visibility
4. **Response-time expectation**: "Quote within 4 business hours · Custom terms negotiable"
5. **Quote-to-checkout conversion path**: when sales returns the quote, customer can accept and check out from the quote (round-trip workflow)

For accounts that should be encouraged toward custom-quote (high-AOV regulars, specialty customers), the "Request quote" CTA can be visually emphasized over "Place order".

**Test specification**
- **Hypothesis:** If we add a "Request quote for this cart" CTA on high-AOV carts alongside "Place order", then high-AOV cart conversion (combined order + quote conversion) will increase because customers who want custom terms can stay in the platform workflow rather than abandoning to off-platform contact (Baymard hybrid B2B research; MEDDIC Decision Process).
- **Variant A:** "Place order" only
- **Variant B:** Dual CTAs ("Place order" + "Request quote for this cart") above threshold
- **Primary metric:** combined high-AOV cart conversion (order completion + quote requests)
- **Secondary metrics:** quote-request rate, quote-to-order conversion downstream, abandonment from cart on high-AOV
- **Expected impact:** +10% to +22% on combined high-AOV cart conversion
- **ICE:** I=8, C=7, E=6 → 7.0
- **Source:** Baymard hybrid B2B research; MEDDIC framework (Decision Process)

---

## Example 4: 🟠 Important — Save-as-list, recurring order & multi-session workflows (wholesale repeat customer)

### 🟠 Save-as-list — Feature absent despite wholesale recurring-order customer base

**Diagnosis**
The cart page provides no "Save as list" or "Save cart" feature. For a wholesale platform where boutique retailers reorder similar SKU baskets monthly or quarterly, this is a structural workflow gap. Per Baymard's B2B save-list research, save-as-list features yield **8-18% multi-session conversion lift** by supporting recurring-order workflow. Per Jobs-to-be-Done framework, the recurring-order job is one of the dominant B2B cart workflows — customers building a cart that mirrors last quarter's order want one-click to save and reorder without rebuilding from scratch. The current platform forces customers to either rebuild the cart manually each cycle or maintain external spreadsheets (driving customers to phone orders, where neither retention nor analytics work).

**Recommendation**
Add save-as-list functionality. Concrete pattern:
1. **"Save as list" button** prominent in cart-actions area (alongside "Continue shopping" and primary CTA)
2. **Name the list** at save-time ("Q1 stock order", "Monthly maintenance", "Engineering recurring")
3. **Multi-list support**: customers can maintain multiple named lists for different ordering scenarios
4. **List management** in account dashboard: view, rename, delete, duplicate, share with team-members
5. **"Load list to cart"** one-click from account dashboard — replaces current cart OR adds-to-current (customer choice)
6. **Saved-list recommendations on empty cart**: empty-cart state shows "Reorder from saved lists" prominently

For accounts with multi-user workflows (requester + approver), saved lists are shareable across team members — the team's procurement specialist maintains canonical lists that requesters reorder from.

**Test specification**
- **Hypothesis:** If we add save-as-list functionality with naming, multi-list support, and account-dashboard management, then multi-session conversion rate (return customers building carts from saved lists) will increase substantially because the recurring-order workflow is supported in-platform (Baymard B2B save-list research; Jobs-to-be-Done framework).
- **Variant A:** No save-as-list feature
- **Variant B:** Save-as-list with naming, multi-list management, load-to-cart, empty-cart integration
- **Primary metric:** multi-session conversion rate (repeat customers reaching checkout via saved-list)
- **Secondary metrics:** save-as-list adoption rate, average lists per customer, list-to-cart conversion rate
- **Expected impact:** +12% to +25% on multi-session conversion rate
- **ICE:** I=6, C=7, E=5 → 6.0
- **Source:** Baymard Institute B2B save-list research; Jobs-to-be-Done framework

---

## Example 5: 🟠 Important — Trust signals, lead-time & shipping signals (project-driven B2B)

### 🟠 Lead-time signals — No per-line lead-time on cart despite mixed stock + custom-order products

**Diagnosis**
The cart page (industrial supplier serving construction project customers) shows 11 line items with no per-line lead-time signal — only a generic "Shipping calculated at checkout" footer note. The cart mixes in-stock products (ship today) with custom-order products (2-3 week lead time) but the customer cannot distinguish which is which from the cart view. Per MECLABS' anxiety axis, lead-time reliability is the #1 anxiety for project-driven B2B customers — and the absence of per-line lead-time on the cart page surfaces the anxiety at the highest-friction moment (right before checkout commitment). Per Baymard's B2B inventory research, per-line lead-time signaling reduces checkout-step-1 abandonment by 5-10% on multi-stock carts.

**Recommendation**
Add per-line lead-time signals on cart. Concrete pattern:
1. **Per-line status**: "In stock · Ships today" (green) OR "Backorder · 2-3 week lead time" (yellow) OR "Custom order · 4-6 weeks" (orange)
2. **Cart-level aggregate**: "Cart contains items with mixed lead times. Earliest delivery: tomorrow. Latest: 6 weeks."
3. **Split-shipment option**: "Ship in-stock items separately?" toggle (when applicable) — visitors can split urgent items from custom-order items
4. **Project-deadline support**: optional "Required by [date]" field on cart; if dates conflict with lead-times, surface warning
5. **Cut-off time for same-day**: "Order within 2h 14min for same-day dispatch" countdown when applicable

For project-deadline-driven customers, split-shipment support is particularly valuable — they can take immediate stock now and follow up with custom-order items later without rebuilding the cart twice.

**Test specification**
- **Hypothesis:** If we add per-line lead-time signals and split-shipment option on the cart page, then cart-to-checkout conversion will increase for project-driven customers because lead-time anxiety is addressed at the right moment with the right granularity (Baymard B2B inventory research; MECLABS anxiety axis).
- **Variant A:** No per-line lead-time signals
- **Variant B:** Per-line status + cart aggregate + split-shipment option
- **Primary metric:** cart-to-checkout conversion rate (project-driven customers)
- **Secondary metrics:** cart-edit rate around mixed-lead-time items, split-shipment adoption rate, post-purchase customer-service tickets about delivery timing
- **Expected impact:** +5% to +12% on cart-to-checkout conversion for project-driven customers
- **ICE:** I=6, C=7, E=6 → 6.3
- **Source:** Baymard Institute B2B inventory research; MECLABS Conversion Sequence Heuristic

---

## Example 6: 🟢 Nice-to-have — Cross-sell, accessories & "frequently ordered with" (transactional MRO)

### 🟢 Cross-sell — "You may also need" section absent despite MRO accessory-heavy category

**Diagnosis**
The cart page (MRO supplier) shows the line items and totals but no cross-sell or "you may also need" section. For an MRO category where many products require accessories or consumables (mounting hardware, cables, replacement filters, lubricants), this is a missed AOV opportunity. Per Baymard's B2B cross-sell research, cart-page cross-sell yields 4-9% AOV lift on accessory-heavy categories — but only when cross-sell is genuinely relevant (required-accessory > compatible > "you may also like"). Note: marked Nice-to-have because the impact depends heavily on data quality (which cross-sells are genuinely needed vs decorative), and implementation requires order-history analysis or accessory-relationship data in the PIM.

**Recommendation**
Add cart-page cross-sell when accessory-relationship data is available. Concrete pattern:
1. **"You may also need" section** below cart lines, above cost summary
2. **3-6 items per cross-sell**, focused on required-accessories first ("Required for installation"), then compatibles ("Frequently ordered with")
3. **One-click add** with quantity selector and MOQ awareness
4. **Cross-sell limited per cart** (3-6 items max; more becomes noise)
5. **Cross-sell respects MOQ and pack-size**

Implementation prerequisite: accessory-relationship data must exist in the PIM (product → required-accessories, product → compatible-products). Without this data, generic algorithm-driven cross-sell underperforms and risks recommending unrelated items. Recommend data-quality review before implementation.

**Test specification**
Test not recommended yet — data quality first:
- Audit current accessory-relationship data in PIM
- Identify top-50 products by sales volume and verify their accessory-relationships are complete
- Build cross-sell rules from co-purchase order history (90+ days of data) as fallback

**ICE:** I=4, C=5, E=4 → 4.3

**Source:** Baymard Institute B2B cross-sell research; Iyengar choice overload (lower applicability for B2B)

---

## What makes these examples high-quality

- **B2B-type-aware:** each example signals which B2B type and calibrates recommendations
- **Account-state-explicit:** findings mention whether observation is from anonymous or logged-in screenshots
- **B2B-frameworks integrated:** MEDDIC, Baymard B2B research, JTBD framework appear alongside core CRO frameworks
- **Specific:** every observation names exact cart elements, copy alternatives, behaviors
- **Sourced:** every claim references specific principle or institution
- **Honest about data dependencies:** Example 6 shows how to mark a category as data-dependent rather than forcing implementation
- **Out of security/compliance scope:** none claim "secure" or "AVG-compliant" or "BTW-correct" — staying in UX/trust-signal territory
- **Test-ready:** hypothesis follows "If X, then Y, because Z"; primary metric is B2B-cart-specific
- **Concrete copy:** exact CTA labels, exact warning microcopy, exact section structures
- **Dutch translations natural:** "winkelwagen", "subtotaal", "opslaan als lijst", "BTW-verlegd" used appropriately; "huren" never used

Always match this standard. If a finding can't reach this standard, either dig deeper or remove it from the audit.
