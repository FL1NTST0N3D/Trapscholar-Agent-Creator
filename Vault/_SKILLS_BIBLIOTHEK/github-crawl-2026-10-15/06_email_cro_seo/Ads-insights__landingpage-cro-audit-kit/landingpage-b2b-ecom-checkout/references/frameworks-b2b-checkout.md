# Frameworks for B2B Ecommerce Checkout Audits

This reference file contains the CRO and B2B-specific frameworks, principles, and applied research used in the B2B checkout audit. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

B2B checkout audits are uniquely prone to fabricated findings because so much is account-state-dependent and JavaScript-rendered. Examples:
- PO number field (only renders for accounts with PO-billing enabled)
- Invoice payment option (only renders for accounts under credit limit)
- BTW number field (only renders for EU intra-community customers)
- Multi-shipping interface (only renders for accounts with multiple ship-to addresses)
- Approval-workflow indicators (only render for requester-role accounts under approval threshold)
- Punch-out indicators (only render in procurement-system sessions)

**For every finding, verify the claim against screenshots before delivering.** A finding that says "no PO field" while the screenshot shows it is worse than no finding.

---

## CRITICAL — Stay out of security and compliance territory

B2B checkout is the obvious place to comment on "is this secure?" or "is this AVG/GDPR-compliant?" or "is the BTW-handling correct?". **Do not.**

**The hard rules:**
- A finding may RECOMMEND adding visible trust signals (lock icons, "Veilige verbinding", payment-method badges)
- A finding may RECOMMEND improving the UX of consent/PO/invoice flows
- A finding may NOT claim the checkout is "secure" or "insecure"
- A finding may NOT claim the checkout is "AVG-compliant" or "non-compliant"
- A finding may NOT claim the BTW-handling is "correct" or "incorrect"
- A finding may NOT diagnose ERP/payment integration failures

When in doubt, frame as: "Visitors lack visible signals of [X]; consider [UX improvement]" rather than "Your checkout is [security/compliance claim]."

---

## CRITICAL — B2B checkout type-specific calibration

The four B2B checkout types require different recommendations:

**Card-payment B2B:**
- Most similar to B2C checkout
- PO field optional
- Business address required
- BTW number optional or required (depends on customer registration)
- Cart-to-checkout-to-payment in standard flow

**Invoice/NET-payment B2B:**
- "Pay by invoice" option prominent
- Credit limit shown to logged-in customer
- Payment terms displayed (NET-15, NET-30, NET-60)
- Approval workflow may apply
- No card-entry step needed

**PO-driven B2B:**
- PO number field MANDATORY
- Customer reference / cost center fields common
- Often integrated with procurement systems (punch-out)
- Approval workflow standard
- Order goes to "pending approval" not "paid"

**Hybrid:**
- Customer chooses card OR invoice (based on credit limit, account terms)
- Both flows must work cleanly

Recommendations for one type are usually wrong for another. The brand snapshot must include B2B checkout type detection.

---

## Core frameworks (apply across the entire audit)

### Baymard Institute B2B checkout research
Baymard's B2B research:
- B2B checkout abandonment averages 23-32% (higher than B2C's 17.8% due to longer forms, approval friction, PO complexity)
- 67% of B2B sites have severe usability issues in checkout
- The cumulative effect of fixing top 8 B2B checkout issues averages **18-30% checkout completion lift**
- Approval workflows add 12-18% per-step abandonment compared to non-approval flows

### MEDDIC framework on B2B checkout
- **Metrics:** B2B buyers verify the order math (cost-per-unit, total, tax) — visible math is essential
- **Economic buyer:** the buyer may not be the approver; checkout must support requester-then-approver flow
- **Decision criteria:** PO, cost center, project codes are not optional fields — they're decision-critical for procurement
- **Decision process:** approval workflow IS the checkout for many B2B accounts
- **Identify pain:** unclear payment terms cause abandonment ("Can I pay on invoice or do I need to use my card?")
- **Champion:** the requester is the champion; the checkout must let them advocate to approval ("Submit for approval" CTA)

### Challenger Sale (Dixon & Adamson) on B2B checkout
B2B buyers respond to confident, clear flows — not aggressive sales tactics. On checkout:
- Clear payment terms upfront ("NET-30 available for approved accounts")
- Confident handling of approval workflow ("Submit for approval — your approver will receive notification within 2 minutes")
- Educational microcopy ("Cost center? Required for accounting allocation")

### MECLABS Conversion Sequence Heuristic on B2B checkout
C = 4m + 3v + 2(i−f) − 2a

On B2B checkout:
- **m (motivation):** high (visitor has navigated through B2B funnel)
- **v (value):** must be reinforced via persistent order summary
- **i (incentive):** less applicable on checkout
- **f (friction):** dominant lever — PO complexity, multi-field forms, approval steps
- **a (anxiety):** anxiety about lead time, return policy, invoice payment terms

### Fogg Behavior Model (B = MAT) on B2B checkout
B2B checkout's job: maximize **Ability** without breaking required procurement workflows.

### Cialdini's principles on B2B checkout
- **Authority** — payment-method icons, BTW-registered indicator, AVG-statement icon (UX, not legality)
- **Liking** — visible account-manager contact for high-AOV checkouts
- **Reciprocity** — net terms framed as gift ("NET-30 standard for approved accounts")
- **Commitment-consistency** — multi-step flows reinforce commitment

### Nielsen Norman heuristics applied to B2B checkout
- **#1 Visibility of system status** — approval workflow visibility ("Pending approver: John Doe")
- **#5 Error prevention** — inline validation, masks for BTW (validates against VIES), PO format
- **#6 Recognition over recall** — order summary persistent across steps + per-line cost breakdown
- **#9 Help users recover from errors** — clear path when approval fails or credit limit hit

### Jobs-to-be-Done on B2B checkout
B2B visitors on checkout are doing one of:
1. **Reorder repeat purchase** — fastest path; minimal steps
2. **Complete first-time purchase** — needs guidance, account-creation friction
3. **Submit for approval** — requester role; "save and submit for approval"
4. **Validate before approval** — approver role; "review and approve"
5. **Procurement-system checkout** — punch-out flow; minimize UX, return data to source system

Different jobs need different optimizations. A well-designed B2B checkout serves multiple jobs without forcing the wrong path.

**Important Dutch translation:** never use "huren" for JTBD. Use "kiezen voor", "zoeken om af te ronden", "inkopers die willen afrekenen".

---

## Category 1: Progress indicator & flow clarity

### Baymard B2B checkout-flow research
B2B checkouts are typically longer than B2C (4-6 steps common vs B2C's 2-4):
- Visible progress indicators reduce abandonment by 5-12% on multi-step checkouts (same as B2C)
- Step indicators that show NAMES outperform numbered-only (Step 2 of 5 vs Contact → Shipping → Payment → PO → Review)
- For approval-workflow checkouts, the "pending approval" step must be clearly indicated

### Best practices
- Visible step indicator at top of each step
- Step names visible
- Current step distinct
- Completed steps clickable (return path)
- For approval flows: clear "Submit for approval" labeled as final step (not "Place order")
- Mobile: sticky progress indicator

### Common failures
- No step indication on 5+ step checkout
- Step indicator hidden on mobile
- Approval flow not distinguished from immediate-order flow
- Cannot return to earlier step without losing data
- "Step 3 of ???" — unclear total

### B2B checkout type calibration
- Card-payment: similar to B2C (3-4 steps typical)
- Invoice/NET: same length, with invoice-terms step
- PO-driven: longer (5-6 steps), approval indication critical
- Hybrid: must show payment-choice step clearly

---

## Category 2: Account/login strategy (vs guest checkout)

### Baymard B2B account research
B2B differs fundamentally from B2C on account strategy:
- B2B is naturally account-first (repeat business model)
- Guest checkout is often inappropriate (PO, invoice, account-credit require account)
- BUT: forcing account creation for first-time buyers is still the #1 conversion killer for B2B prospects exploring the platform

### The "transactional first" pattern (recommended)
For B2B platforms serving new prospects:
- First-time buyers: simplified account creation INTEGRATED into checkout (email + business name + basic contact = account created automatically)
- "Become a customer" workflow integrated, not separate
- Account approval (for credit/NET terms) handled post-purchase, not blocking

### Best practices
- Logged-in customers see frictionless checkout (saved everything)
- New prospects can complete a card-payment order with minimal account-creation friction
- Approval-required accounts (NET, invoice) flagged at the right step ("This requires a verified business account — apply here")
- Returning-customer login should not force re-entry of any information

### Common failures
- Heavy account-creation form before any checkout activity
- "Apply for trade account" required before any order possible
- Login required even for first-time prospects who would pay by card
- Logged-in checkout identical to anonymous (no personalization)

### B2B checkout type calibration
- Card-payment B2B for new prospects: light account creation in-checkout
- Invoice/NET: account approval required, but flagged appropriately
- PO-driven: account essential, often pre-existing (procurement-system integrated)
- Wholesale: account approval required, very common to block first-time order

---

## Category 3: Form field count, business fields & cognitive load

### Baymard B2B form research
B2B checkouts legitimately need more fields than B2C:
- Business name, VAT/BTW, KvK, billing address vs shipping
- Cost center, project code, internal reference
- PO number, approver contact
- Delivery instructions for receiving dock

But the principle still holds: **every unnecessary field costs conversion**. Baymard's B2B research shows that:
- Average B2B checkout has 31 fields — but well-optimized B2B needs only 14-22
- Smart defaults and auto-fill reduce perceived field count
- "Save this address" / "Save this PO format" speed repeat orders

### Hick's Law on B2B
Each field is a decision point. B2B's longer fields are tolerable IF organized into logical groups:
- Personal contact (name, email, phone)
- Business identity (company, BTW, KvK)
- Shipping address
- Billing address (default = same as shipping)
- Internal reference (PO, cost center, project)
- Payment

### Best practices
- Group fields by logical section, not random order
- Smart defaults: country detected, billing-same-as-shipping checked, last-used address pre-filled
- Optional fields visually de-emphasized
- Justify business-specific fields ("BTW number — required for tax-free intra-EU orders")
- Save preferences for next time (saved PO format, saved cost center default)

### Common failures
- All fields presented as flat list (no grouping)
- Required fields and optional fields visually identical
- No smart defaults for returning customers
- Business-specific fields unexplained
- BTW field required even for non-EU or non-VAT-registered customers

### B2B checkout type calibration
- Card-payment: shorter form (similar to B2C + business name)
- Invoice/NET: + invoice-billing fields, payment terms confirmation
- PO-driven: + PO number, cost center, approver contact
- Hybrid: payment-method-dependent fields shown after payment choice

---

## Category 4: Address input UX & multi-shipping support

### Baymard address research (B2B-specific)
B2B addresses are more complex than B2C:
- Business name + attention (who at the company receives)
- Often deliveries to specific dock/department/floor
- Receiving hours specification
- Multiple addresses per account (head office, warehouse, project site)
- Address validation must accept legitimate business addresses (units in industrial estates, addresses without standard street naming)

### Multi-shipping (B2B-specific)
B2B buyers often need to split orders across multiple addresses:
- Different products to different warehouses
- Same product to multiple project sites
- Hold-for-pickup at carrier depot

Multi-shipping support is a high-leverage B2B differentiator.

### Best practices
- Address selector for saved addresses (logged-in)
- "New address" option always available
- Multi-shipping option visible (if relevant for vertical)
- Address verification with manual override
- Receiving instructions field (optional but valued)
- Receiving hours field for restricted-access locations

### Common failures
- Single-address-only on order with multiple deliveries
- No address book for repeat customers
- Strict address validation rejecting legitimate business addresses
- No "attention" field forcing visitors to add it to street field
- Receiving hours and dock info missing

### NL-specific
- Postcode-autocomplete still applies but must accept business addresses (industrial estates have unusual street/number combinations)
- "Aanwezig adres" vs "Postadres" common requirement
- "Magazijn" / "Bouwplaats" / "Projectlocatie" labels for non-standard delivery types

---

## Category 5: PO number, customer reference & internal codes

### Baymard B2B procurement-field research
PO number and internal codes are B2B-defining fields:
- 71% of B2B buyers cannot complete a purchase without their PO/cost-center field
- PO format varies by company (free text, alphanumeric, length-limited)
- "Optional" PO field for customers who don't use POs is critical
- Customer reference / cost center / project code are equally critical for some accounts

### MEDDIC — Decision process
PO and reference fields ARE the decision process — they connect the purchase to internal procurement workflow. Missing or broken PO fields make the order unactionable for procurement.

### Best practices
- PO field clearly labeled ("Purchase Order number (optional/required based on account)")
- Format helper if account has specific format ("Format: PO-YYYY-NNNN")
- Multiple internal-reference fields when account configuration requires (PO + cost center + project)
- Save format for next time
- "Skip — we don't use POs" option for accounts that don't require

### Common failures
- PO field required for all customers (including those who don't use POs)
- PO field invisible for accounts that DO require POs (renders only after later step)
- No format guidance (visitor enters "12345" when "PO-2024-12345" required)
- Cost center field without dropdown of valid cost centers (free text causes accounting errors)
- No "Save my standard PO format" option

### B2B checkout type calibration
- Card-payment B2B: PO usually optional
- Invoice/NET: PO often required for invoice routing
- PO-driven: PO mandatory, full procurement-field set
- Hybrid: visibility depends on payment choice

---

## Category 6: Payment method strategy (card / invoice / NET / PO-bound)

### Baymard B2B payment research
B2B payment offers fundamentally different options than B2C:
- **Card** (credit/debit) — for low-volume, first-time, or non-credit-limit customers
- **Pay by invoice** — NET-15, NET-30, NET-60 terms for credit-approved customers
- **PO/bound payment** — invoiced against PO, procurement-managed
- **Bank transfer / SEPA** — for high-value B2B, EU intra-community
- **Direct debit / SEPA Direct Debit** — recurring/repeat B2B customers

### Account credit limit logic
Logged-in B2B customers should see payment options filtered by their account credit limit:
- Above credit limit: card or bank transfer only
- Within credit limit: invoice option available
- Approved customer: full payment-method choice

### Best practices
- Show available payment methods FOR THIS ACCOUNT (not generic list)
- Explain credit limit if relevant ("You have €X,XXX credit remaining — pay by invoice available")
- "Pay by invoice" terms visible (NET-30, payment instructions)
- Card-payment option for any account
- For procurement-system sessions: PO-bound payment automatic

### Common failures
- Generic payment method list ignoring account state
- "Pay by invoice" offered but credit limit not shown
- Payment terms (NET-30) hidden until after order placement
- Card-only checkout for B2B customers who expect invoice
- iDEAL absent on NL B2B (still highly relevant for low-value B2B)

### B2B checkout type calibration
- Card-payment: card methods + maybe iDEAL/SEPA
- Invoice/NET: invoice prominent + card as fallback
- PO-driven: PO-bound primary, others optional
- Hybrid: clear choice with explanation of when each applies

---

## Category 7: BTW/VAT, tax-handling & reverse-charge (B2B-specific)

### EU intra-community VAT (UX considerations only, not legality)
B2B EU customers with valid VAT numbers are entitled to BTW-verlegging (reverse-charge):
- Visitor enters BTW number
- System validates against VIES (EU VAT validation service)
- Order shown without BTW (BTW-verlegd)
- Invoice generated with BTW-verlegging notation

The UX of this flow is critical — visitors who can't easily enter BTW or see verified BTW status abandon.

### Best practices (UX only)
- BTW field optional for non-EU or non-VAT-registered customers, required for EU intra-community
- Real-time validation against VIES with clear feedback ("BTW validated — BTW-verlegging applied")
- Tax-handling visible in order summary (excl. BTW, BTW-verlegd, incl. BTW)
- For non-VAT-eligible orders: clear "BTW will be applied" messaging
- Saved BTW number for repeat customers

### Common failures
- No BTW field on B2B checkout (visitor unable to claim BTW-verlegging)
- BTW field unvalidated (orders go through with invalid BTW, fixed manually later)
- Tax-handling ambiguous in order summary (visitor unsure if final price is excl/incl BTW)
- No saved BTW for repeat customers
- BTW validation error without clear recovery path

### IMPORTANT
This category covers the UX of tax-handling. It does NOT cover whether the tax rules are correctly applied (that's a tax compliance question, out of audit scope). A finding may say "BTW field UX needs improvement" but not "BTW-handling is incorrect".

---

## Category 8: Trust signals throughout flow

### MECLABS anxiety axis on B2B checkout
B2B checkout anxiety is different from B2C:
- "Will this order arrive when I committed to my project deadline?" (lead time)
- "Will the invoice payment terms work for our finance?" (NET-30)
- "Can my approver actually approve this from a mobile email?" (approval workflow)
- "Is the product actually compliant with our specification?" (certifications)

### Cialdini authority on B2B checkout
- Payment-method icons (visible before selection)
- BTW-registered indicator
- "Customer service: Mon-Fri 8:00-18:00, +31 X XXX XXXX"
- Account manager contact (for high-AOV)
- Industry certifications visible
- Years operating, customer logos in footer

### Edelman B2B Trust Barometer
Verifiable claims outperform vague claims:
- "12,000+ B2B customers" beats "Trusted by businesses worldwide"
- "ISO 9001 certified — view certificate (PDF)" beats "Quality certified"
- "30-day return for unopened items, contact account manager for opened" beats "Easy returns"

### Best practices
- Trust signals visible at every step
- Account manager contact prominent for high-AOV
- Lead-time commitment visible at payment step
- Industry-specific compliance signals
- Return / cancellation policy explicit for B2B context (often different from B2C)

### Common failures
- Trust signals only in footer (not visible on checkout)
- Generic "secure checkout" without B2B-specific context
- No account-manager contact on high-AOV checkouts
- Lead-time hidden until order confirmation
- Return policy generic (B2C-style) when B2B requires different terms

---

## Category 9: Error handling & validation

### Baymard form-error research on B2B
B2B has unique error scenarios:
- Invalid BTW number (validation failure)
- PO format mismatch (account requires specific format)
- Address rejected by carrier validation
- Credit limit exceeded (invoice payment not available)
- Approver email invalid (approval workflow breaks)
- Quantity exceeds available stock (when MOQ-rounded)

### Best practices
- Inline validation on blur
- Specific error messages with recovery path
- Errors visible at the field, not at top
- BTW errors: explain validation failure + offer manual override or alternative path
- Credit-limit errors: explain + offer card-payment fallback
- Approval-workflow errors: clear recovery (resend, change approver)

### Common failures
- All errors at submit
- Generic "Invalid input" without explanation
- BTW validation hard-fail with no manual override
- Credit-limit error blocking checkout with no alternative
- Approver email error without re-send option

---

## Category 10: Order summary, approval workflow & final commit copy

### Baymard order-summary research on B2B
B2B order summaries are more complex than B2C:
- Per-line cost (price × qty = subtotal per item)
- Tax handling clear (excl/incl BTW, BTW-verlegd)
- PO number reflected
- Cost center / project reference visible
- Shipping costs per shipment (if multi-shipping)
- Approval status (if approval-workflow active)

### Approval-workflow patterns (B2B-specific)
For accounts with approval workflow:
- Requester sees "Submit for approval" CTA, not "Place order"
- Order goes to "Pending approval" state, not "Confirmed"
- Approver receives notification with one-click approve/reject
- Status visible to requester throughout

### Final-step commit copy (B2B-specific)
- For immediate-payment B2B: "Plaats bestelling — €X" (similar to B2C)
- For invoice B2B: "Plaats bestelling — factuur van €X volgt" or "Bevestig bestelling"
- For approval-pending B2B: "Verstuur voor goedkeuring" or "Submit for approval"
- For PO-bound B2B: "Verstuur bestelling met PO-nummer [NNN]"

The CTA copy must match the actual action being taken — never "Place order" when the order will sit in pending-approval.

### Best practices
- Persistent order summary across all steps
- Per-line cost breakdown clear
- Tax handling explicit
- For approval flows: status visible at every step
- CTA copy matches actual action

### Common failures
- Order summary only shown on final step
- Per-line costs hidden, only total shown
- "Place order" CTA on an approval-pending flow
- Approval status not visible to requester
- Multi-shipping costs not broken down

---

## Category 11: Mobile B2B checkout

### Baymard mobile B2B research
B2B mobile is rising:
- 35-50% of B2B traffic is mobile (varies by vertical, often field-sales context)
- B2B mobile checkout completion lags desktop by 50-65% (worse than B2C's 30-40% lag)
- Approval workflows are increasingly mobile-first (approver receives email, taps approve on phone)

### Mobile B2B-specific patterns
- Sticky CTA on long checkout forms
- Numeric keyboards for BTW, postcode, phone
- Autofill compatibility for business addresses (limited; some platforms lack proper autocomplete attributes for business fields)
- One-touch approve/reject for approval workflow emails
- Field-sales context: tablet form factor common, requires mid-size optimization

### Best practices
- Sticky CTA on long B2B forms
- Numeric keyboards for numeric fields
- Autofill for business fields (use proper HTML autocomplete attributes)
- Approval emails mobile-optimized with deep-link to approve/reject
- Tablet-friendly layouts (B2B field-sales)

### Common failures
- Desktop-style multi-column forms on mobile
- Sticky CTA absent
- Approval workflow email broken on mobile
- BTW field with text keyboard instead of numeric
- Multi-shipping interface unusable on mobile (table requires horizontal scroll)

---

## Brand calibration notes

Always recalibrate by brand snapshot AND B2B checkout type:

**Example: Account strategy**
- Transactional small-B2B (office supplies): light account creation, card-friendly
- Industrial supplier: account approval required, NET terms standard
- Wholesale fashion: heavy account approval, no card option, MOQ-driven
- Procurement-integrated: punch-out flow, minimize UX

**Example: Payment method emphasis**
- Card-payment B2B: card methods + iDEAL/SEPA for region
- Invoice B2B: invoice prominent, card fallback
- PO-driven: PO-bound payment automatic, others optional
- High-AOV (€10k+): account manager contact + flexible payment

**Example: Final CTA copy**
- Immediate-payment B2B: "Plaats bestelling — €X,XXX"
- Invoice B2B: "Plaats bestelling — factuur volgt"
- Approval B2B: "Verstuur voor goedkeuring"
- PO B2B: "Verstuur bestelling met PO [NNN]"

Recommendations that don't match brand AND B2B checkout type are wrong.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites a specific principle
- [ ] Recommendation is concrete
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric is B2B-specific (checkout completion, per-step abandonment, PO-error rate, invoice-vs-card distribution, approval-flow completion)
- [ ] ICE justified by I/C/E breakdown
- [ ] Recommendation matches brand AND B2B checkout type
- [ ] Account-state assumption explicit
- [ ] No security/compliance claims
- [ ] No tax-correctness claims
- [ ] Dutch output: no "huren" check

If any unchecked, rework before delivering.
