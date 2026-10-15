# Worked finding examples — B2B checkout quality calibration

These examples show what a high-quality B2B checkout finding looks like across different B2B checkout types and ICE scores. Use them as a reference standard.

---

## Example 1: 🔴 Critical — PO number, customer reference & internal codes (PO-driven industrial)

### 🔴 PO field — PO number field absent despite procurement-driven account base

**Diagnosis**
The checkout flow has no PO (purchase order) number field anywhere across the four steps shown. The account base for this industrial-supply platform is heavily procurement-driven (verified by the visible "Cost center" preference in account settings), meaning the majority of orders need to be traceable to an internal PO for the customer's accounting team. Per Baymard's B2B procurement-field research, **71% of B2B buyers cannot complete a purchase without their PO/cost-center field** — and orders placed without PO traceability create downstream invoicing-and-reconciliation problems for the customer that translate to poor renewal/repeat rates. Per MEDDIC's Decision Process axis, the PO field connects the purchase to internal procurement workflow; missing it makes orders unactionable for the procurement team.

**Recommendation**
Add a "PO number / Inkoopordernummer" field at the appropriate checkout step (typically between shipping and payment, OR at the same step as billing address). Label clearly with optionality based on account configuration: required for accounts with PO-mandatory setting, optional otherwise with a "Skip — we don't use POs" option. Add a format-helper line if account has format requirement ("Format: PO-YYYY-NNNN"). For repeat customers, offer "Save as my default PO format" with auto-fill on next order. Include adjacent fields for accounts that need them: cost center (dropdown of valid options), project code, internal reference. Group all internal-reference fields in a single "Reference & accounting" section.

**Test specification**
- **Hypothesis:** If we add a PO field and adjacent internal-reference fields to the B2B checkout, then checkout completion rate will increase and post-purchase reconciliation issues will decrease because procurement-driven customers can correctly tag the order for internal accounting (Baymard B2B procurement-field research; MEDDIC Decision Process).
- **Variant A:** no PO field anywhere in checkout
- **Variant B:** PO + cost center + project code in dedicated section
- **Primary metric:** checkout completion rate (procurement-driven accounts)
- **Secondary metrics:** repeat-order rate, post-purchase customer-service tickets about missing PO
- **Expected impact:** +8% to +18% on checkout completion rate for procurement-driven accounts
- **ICE:** I=9, C=9, E=6 → 8.0
- **Source:** Baymard Institute B2B procurement-field research; MEDDIC framework (Decision Process axis)

---

## Example 2: 🔴 Critical — Payment method strategy (invoice/NET B2B)

### 🔴 Payment method — "Pay by invoice" option missing despite NET-30 customer base

**Diagnosis**
The payment step shows three options: credit card, iDEAL, and PayPal. There is no "Pay by invoice" option, despite the account-management page indicating NET-30 payment terms are available for approved accounts. Per Baymard's B2B payment research, B2B buyers strongly prefer their established payment terms — forcing card-payment on customers with NET-30 credit terms creates immediate abandonment (the buyer must escalate to finance for a card-payment exception, often a 1-3 day delay). Per MECLABS' anxiety axis, the absence of invoice-payment when expected creates structural anxiety: "Has my account been changed? Why can't I pay on invoice?" The current state actively suppresses checkout completion for credit-approved B2B customers.

**Recommendation**
Add "Pay by invoice" as a payment option for accounts with available credit. Implementation:
1. Detect logged-in customer's account terms (NET-15 / NET-30 / NET-60 / pre-payment-only)
2. Filter payment methods accordingly: credit-approved accounts see invoice + card; non-credit accounts see card only
3. Display payment terms explicitly: "Pay by invoice — NET-30 (€X,XXX remaining on your credit limit)"
4. For accounts at or near credit limit: show clearly with card fallback option
5. Default selection: invoice for credit-approved accounts (matches their expectation)

Order of payment methods: invoice (for eligible) → card → iDEAL → PayPal.

**Test specification**
- **Hypothesis:** If we add "Pay by invoice" as a payment option for credit-approved accounts with NET-30 terms displayed, then checkout completion rate for those accounts will increase substantially because the established payment workflow is restored (Baymard B2B payment research; MECLABS anxiety reduction).
- **Variant A:** card and PayPal only, no invoice option
- **Variant B:** invoice option for credit-approved accounts + card fallback
- **Primary metric:** checkout completion rate (credit-approved accounts)
- **Secondary metrics:** payment-step exit rate, payment-method distribution, support tickets about invoice payment
- **Expected impact:** +25% to +45% on checkout completion rate for credit-approved accounts (massive single-fix impact)
- **ICE:** I=10, C=9, E=7 → 8.7
- **Source:** Baymard Institute B2B payment research; MECLABS Conversion Sequence Heuristic; B2B credit-limit logic

---

## Example 3: 🔴 Critical — Order summary, approval workflow & final commit copy (approval-workflow B2B)

### 🔴 Final commit copy — "Place order" CTA on an approval-pending flow misleads the requester

**Diagnosis**
The final-step CTA reads "Place order — €1,247.50" but the screenshot shows the account is configured for approval workflow (visible at the top: "This order requires approval from your manager"). Clicking the CTA does not place the order — it submits for approval, which the approver then receives via email and approves separately. Per Baymard's B2B research, CTA-copy mismatches in approval workflows are one of the most disorienting B2B checkout failures: the requester believes the order is placed, follows up with the supplier about shipping, and discovers it's still pending approval. This creates customer-service friction AND undermines requester trust in the platform.

**Recommendation**
Change the CTA copy based on the actual action being taken:
- For approval-required accounts: "Verstuur voor goedkeuring" / "Submit for approval"
- For immediate-order accounts: "Plaats bestelling — €1,247.50"
- For PO-bound accounts: "Verstuur bestelling met PO [NNN]"

Detect account configuration and render appropriate CTA. Add adjacent microcopy explaining next step:
- Approval: "Je manager [Name] ontvangt direct een notificatie. Status zichtbaar in 'Mijn bestellingen'."
- Immediate: "Je ontvangt direct een bevestiging per email."
- PO-bound: "Bestelling gekoppeld aan PO [NNN]. Verzending start na goedkeuring."

Update the order-confirmation page accordingly — for approval-pending orders, show "Wacht op goedkeuring van [Name]" status, not "Order confirmed".

**Test specification**
- **Hypothesis:** If we change the final-step CTA to match the actual action (submit for approval vs place order vs send with PO), then requester confidence in the platform will increase and post-purchase customer-service tickets about order status will decrease (Baymard B2B research; Nielsen Norman visibility-of-system-status heuristic).
- **Variant A:** "Place order" CTA regardless of account configuration
- **Variant B:** Conditional CTA copy matching actual action + next-step microcopy
- **Primary metric:** approval-flow completion rate (requesters who successfully submit + approvers who approve)
- **Secondary metrics:** customer-service tickets about order status, time-from-submit-to-approval, requester repeat-order rate
- **Expected impact:** indirect — improves trust and reduces support burden rather than direct conversion lift
- **ICE:** I=7, C=8, E=10 → 8.3
- **Source:** Baymard Institute B2B research; Nielsen Norman heuristics (visibility of system status)

---

## Example 4: 🟠 Important — BTW/VAT, tax-handling & reverse-charge (intra-EU B2B)

### 🟠 BTW handling — No BTW field for EU customers; intra-community reverse-charge unavailable

**Diagnosis**
The B2B checkout has no BTW (VAT) number field anywhere across the flow. Per EU intra-community VAT rules, B2B customers in EU member states with valid VAT registrations are entitled to BTW-verlegging (reverse-charge) on intra-community supplies. Without a BTW field, these customers cannot claim the reverse-charge, are charged BTW they shouldn't be paying, and must manually reclaim through their tax authority (months of delay). Per Baymard's tax-handling UX research, missing BTW fields on B2B checkouts serving EU customers cause 15-30% abandonment for intra-community buyers who routinely encounter BTW-verlegging on competitor platforms. Note: this is a UX issue — the actual tax rules and their correct application are out of audit scope.

**Recommendation**
Add a BTW number field at the appropriate checkout step (typically with billing address). Implementation:
1. Optional field labeled "BTW number / VAT number (for intra-EU B2B)"
2. Country-aware: hide for non-EU billing addresses, show for EU billing addresses
3. Real-time validation against VIES (EU VAT validation service) with clear feedback
4. On valid BTW: update order summary to show "BTW: €0.00 (BTW-verlegd intra-community)"
5. Save BTW number for repeat customers (avoid re-entry)
6. Manual override for edge cases ("My BTW number won't validate but is correct" → flag for manual review)

Tax-handling in the order summary must be explicit at all times: "Prices excl. BTW" or "Prices incl. BTW" labels, with the appropriate BTW line item visible.

**Test specification**
- **Hypothesis:** If we add a VIES-validated BTW field for EU customers, then checkout completion rate for intra-EU B2B buyers will increase because reverse-charge handling is enabled and competitor-parity restored (Baymard tax-handling research).
- **Variant A:** no BTW field; all EU customers charged BTW
- **Variant B:** BTW field with VIES validation + reverse-charge handling
- **Primary metric:** checkout completion rate (EU-non-domestic B2B customers)
- **Secondary metrics:** BTW-field engagement rate, post-purchase BTW reclaim requests, intra-EU customer retention
- **Expected impact:** +10% to +25% on checkout completion rate for intra-EU B2B customers
- **ICE:** I=7, C=8, E=5 → 6.7
- **Source:** Baymard Institute tax-handling UX research; B2B intra-EU VAT UX conventions

---

## Example 5: 🟠 Important — Form field count, business fields & cognitive load (wholesale B2B)

### 🟠 Form field count — 41 fields across 3 steps; no smart defaults for returning customers

**Diagnosis**
The checkout requires 41 total fields across three steps: shipping address (14 fields), billing address (10 fields, with billing-same-as-shipping NOT defaulted), business identity (8 fields including BTW, KvK, company size, industry), and additional internal codes (9 fields). For a wholesale fashion B2B platform serving boutique retailers, this is significantly more than Baymard's B2B benchmark of 14-22 well-optimized fields. Returning customers see no smart defaults — they re-enter their shipping address, BTW number, KvK number, and PO format every single order. Per Baymard's B2B form research, each unnecessary field or re-entered field correlates with measurable abandonment, especially in repeat-purchase B2B contexts where returning customers expect their information to persist.

**Recommendation**
Three changes. First, set "Billing same as shipping" to default-checked (typical case for B2B). Second, eliminate non-essential business identity fields: company size and industry are useful for sales but not required for order fulfillment — move to optional account-profile completion post-purchase. Third, for returning customers, pre-fill every saved field with the value from their last order: shipping address, BTW number, KvK number, PO format, default cost center. Add "Edit" affordances next to pre-filled values for cases requiring change. Result: 14-18 fields for returning customers, 22-26 for first-time.

**Test specification**
- **Hypothesis:** If we eliminate non-essential business fields and pre-fill saved data for returning customers, then per-step abandonment will decrease and time-to-complete-checkout will reduce because returning B2B customers regain workflow efficiency (Baymard B2B form research; Hick's Law).
- **Variant A:** 41 fields, no smart defaults, no pre-fill
- **Variant B:** 14-18 fields for returning customers (pre-filled), 22-26 first-time
- **Primary metric:** checkout completion rate (returning customers)
- **Secondary metrics:** time-to-complete-checkout, per-field abandonment, repeat-order frequency
- **Expected impact:** +8% to +18% on returning-customer checkout completion
- **ICE:** I=7, C=8, E=6 → 7.0
- **Source:** Baymard Institute B2B form-field research; Hick's Law; cognitive load research

---

## Example 6: 🟢 Nice-to-have — Address input UX & multi-shipping (project-based B2B)

### 🟢 Multi-shipping — No multi-shipping support despite project-driven B2B model

**Diagnosis**
The checkout supports only single-shipping-address per order. For this project-based B2B supplier (construction materials, supplying to multiple project sites), this is a structural limitation: B2B customers running multiple active projects must split orders into separate checkouts for each project site, multiplying the friction. Per Baymard's B2B multi-shipping research, multi-shipping is a high-leverage differentiator for project-based, multi-warehouse, or multi-location B2B accounts — and its absence forces customers to bypass the ecom flow entirely (calling the sales rep or splitting orders manually). Note: this is Nice-to-have because the actual impact depends on what portion of customers have legitimate multi-shipping needs, which requires customer-research to validate.

**Recommendation**
Add multi-shipping support: visitor can specify different shipping addresses for different line items in the same order. UX pattern:
1. Default behavior: all items ship to one address (current state)
2. "Ship to multiple addresses" toggle at the shipping step
3. When toggled on: per-line address selector (dropdown of saved addresses + "Add new")
4. Shipping cost calculated per-shipment, shown in order summary
5. Each shipment tracked independently post-order

Implementation is non-trivial — requires backend support for split-shipment orders, per-shipment fulfillment workflow, multi-tracking-number handling. Recommend customer-research first to confirm multi-shipping demand before commit.

**Test specification**
Test not recommended yet — research first:
- Survey active customers to determine what % have legitimate multi-shipping needs
- Analyse current "order splitting" patterns (customers placing 2-3 orders in same session with different addresses)
- Estimate AOV uplift from consolidated multi-shipping orders vs split orders

**ICE:** I=5, C=4, E=2 → 3.7

**Source:** Baymard Institute B2B multi-shipping research; project-based B2B workflow patterns

---

## What makes these examples high-quality

- **B2B-checkout-type-aware:** each example signals which B2B checkout type (card / invoice / PO / hybrid) and calibrates recommendations
- **Account-state-explicit:** findings mention whether observation is from anonymous, logged-in standard, or logged-in approver session
- **B2B-frameworks integrated:** MEDDIC, Baymard B2B research, Edelman B2B Trust Barometer appear alongside core CRO frameworks
- **Specific:** every observation names exact fields, steps, copy, behaviors
- **Sourced:** every claim references a specific principle or institution
- **Honest about impact magnitude:** B2B checkout findings can have very high impact (25-45% on specific metrics) when fundamental (invoice payment, PO field, BTW handling)
- **Honest about uncertainty:** when impact depends on customer-base data (multi-shipping example), recommends research before test
- **Out of security/compliance scope:** none claim "secure" or "AVG-compliant" or "BTW-correct" — staying in UX/trust-signal territory
- **Test-ready:** hypothesis follows "If X, then Y, because Z"; primary metric is B2B-checkout-specific
- **Concrete copy and behavior:** exact CTA copy variants, exact field labels, exact validation patterns
- **Dutch translations natural:** "factuur", "BTW-verlegging", "inkoopordernummer" used appropriately; "huren" never used

Always match this standard. If a finding can't reach this standard, either dig deeper or remove it from the audit.
