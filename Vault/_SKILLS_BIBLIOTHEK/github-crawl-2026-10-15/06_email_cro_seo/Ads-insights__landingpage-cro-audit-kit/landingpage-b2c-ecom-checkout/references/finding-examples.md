# Worked finding examples — checkout quality calibration

These examples show what a high-quality checkout finding looks like across different categories, brand snapshots, and ICE scores. Use them as a reference standard. Findings should match this depth and specificity — not be vaguer, not be more generic.

---

## Example 1: 🔴 Critical — Guest checkout strategy (mid-market NL apparel)

### 🔴 Guest checkout strategy — Account creation forced before checkout begins

**Diagnosis**
The first step of the checkout flow shows two options: "Inloggen" and "Account aanmaken" — both visually identical, both required. There is no visible "Continue as guest" option. Per Baymard's checkout research, **24% of users abandon checkout when forced to create an account** — this is the single most fixable abandonment cause in ecommerce, and one of the highest-impact findings on any checkout audit. The site likely loses approximately 1 in 4 first-time-buyer sessions at this exact step. Per the Fogg Behavior Model, forcing account creation reduces ability dramatically at the worst possible moment (post-cart commitment): it adds 4-8 fields (email, password, password confirmation, optional profile), adds password-strength requirements, and adds email verification flow. The visitor already has high motivation — the system is the problem.

**Recommendation**
Add a third visually prominent option: "Doorgaan als gast" / "Bestellen zonder account". Make this the default selected option for first-time visitors. Keep "Inloggen" available as the explicit choice for returning customers (their email auto-detected can also surface a returning-customer prompt). Move account-creation OUT of the pre-checkout flow entirely — instead, on the order confirmation page, offer "Maak een account aan om je bestelling te volgen — je gegevens staan al ingevuld. Stel een wachtwoord in." This converts hesitant guests into customers without blocking the purchase. Use the email already collected to seamlessly pre-fill the account.

**Test specification**
- **Hypothesis:** If we add prominent guest checkout and move account creation to the post-purchase confirmation page, then checkout completion rate will increase because the largest single friction point (forced account creation) is removed for first-time visitors (Baymard guest-checkout research; Fogg Behavior Model ability axis).
- **Variant A:** Account creation or login required to start checkout
- **Variant B:** Guest checkout as default + post-purchase account creation offer
- **Primary metric:** checkout completion rate (first-time visitors)
- **Secondary metrics:** account-creation rate post-purchase, returning-customer retention rate
- **Expected impact:** +15% to +25% on checkout completion rate for first-time visitors
- **ICE:** I=9, C=9, E=7 → 8.3
- **Source:** Baymard Institute guest-checkout research; Fogg Behavior Model

---

## Example 2: 🔴 Critical — Payment methods presentation (NL ecom, missing iDEAL)

### 🔴 Payment methods — iDEAL absent on Dutch checkout; only credit card and PayPal offered

**Diagnosis**
The payment step shows only credit/debit card and PayPal as options. **iDEAL is absent.** For a checkout serving the Dutch market, this is a critical gap: per Baymard's regional payment research, iDEAL accounts for approximately 60%+ of all NL ecommerce payments. NL visitors who don't have a PayPal account and prefer not to enter card details face an immediate dead-end at the payment step — abandonment is near-certain. Per Cialdini's authority principle, the absence of regional payment methods also reduces perceived legitimacy (visitors interpret "no iDEAL on a Dutch site" as suspicious). This is one of the highest-impact and lowest-effort findings possible on a Dutch checkout — most platforms (Shopify, WooCommerce, Magento, custom) integrate iDEAL via standard providers (Mollie, Stripe, Adyen, Buckaroo).

**Recommendation**
Add iDEAL as the **first and default-selected** payment method for visitors detected as NL (via shipping address or IP). Implement an inline bank selector (no modal popup) showing the major Dutch banks (ABN, ING, Rabobank, Bunq, SNS, ASN, Triodos, etc.) with logos. Order: iDEAL → Klarna (Pay Later, Pay in 3) → Credit card → PayPal. Show payment-method logos above the selection area as trust signals before selection. If integration cost is a concern, Mollie offers iDEAL pay-per-transaction without monthly fees — implementation is typically 1-3 days.

**Test specification**
- **Hypothesis:** If we add iDEAL as the first and default payment method for NL visitors, then payment-step conversion will increase substantially because the dominant regional payment method becomes available (Baymard regional payment research; Cialdini authority).
- **Variant A:** Only credit card and PayPal available
- **Variant B:** iDEAL + Klarna + credit card + PayPal, iDEAL default for NL
- **Primary metric:** payment-step conversion rate (visitors entering payment step → completing order)
- **Secondary metrics:** overall checkout completion rate, share of orders per payment method
- **Expected impact:** +20% to +40% on payment-step conversion (massive single-fix impact)
- **ICE:** I=10, C=10, E=7 → 9.0
- **Source:** Baymard Institute regional payment-method research; Cialdini's authority principle

---

## Example 3: 🔴 Critical — Form field count & cognitive load (mid-market, 22 fields)

### 🔴 Form field count — 22 required fields across checkout vs Baymard's 8-12 optimal

**Diagnosis**
The checkout requires 22 fields across all steps: email, password, password confirmation, first name, last name, salutation, company name (B2C site), street, house number, addition, postcode, city, country, phone, date of birth, gender, billing-same-as-shipping toggle (defaulted off), separate billing address (6 more fields if toggle off), newsletter signup (pre-checked), terms agreement, and "How did you hear about us?". Per Baymard's form-field research, a well-optimized B2C ecom checkout needs only **8-12 fields**. Each excess field correlates with measurable abandonment increase. Per Hick's Law, every field is a decision point — 22 decisions create cognitive overload at the worst moment. Specific issues: required "Company name" on B2C site (not needed), required date of birth (no purchase justification), required gender (no purchase justification), required salutation (largely unnecessary), required "How did you hear about us?" (analytics, not order fulfillment).

**Recommendation**
Reduce required fields to: email, full name (single field), street + house number, postcode, city (auto-filled from postcode), country (auto-detected), phone (justified inline: "Voor vragen over de bezorging"). Default "Billing same as shipping" to checked. Remove: salutation, company name, date of birth, gender, "how did you hear about us". Move newsletter signup OUT of required fields — offer as separate opt-in on confirmation page. Terms agreement: text link below button, no blocking checkbox required. Result: ~9 required fields.

**Test specification**
- **Hypothesis:** If we reduce required form fields from 22 to ~9 by removing fields not required for order fulfillment, then checkout completion rate will increase because cognitive load and friction are dramatically reduced (Baymard form-field research; Hick's Law).
- **Variant A:** 22 required fields including DOB, gender, salutation, company name, "how did you hear"
- **Variant B:** ~9 required fields (email, name, address basics, phone)
- **Primary metric:** checkout completion rate
- **Secondary metrics:** time to complete checkout, form-error rate, field-correction rate
- **Expected impact:** +10% to +22% on checkout completion rate
- **ICE:** I=9, C=9, E=7 → 8.3
- **Source:** Baymard Institute form-field research; Hick's Law; cognitive load research

---

## Example 4: 🟠 Important — Address input UX (NL mid-market, manual postcode)

### 🟠 Address input UX — Postcode autocomplete missing on NL checkout; visitors enter address manually

**Diagnosis**
The address step has separate fields for postcode, street, house number, and city — all manually entered. There is no postcode-based autocomplete. Per Baymard's address-field research, 67% of users encounter address-related errors during checkout; postcode autocomplete in NL/UK/DE markets reduces address errors by 50-70%. The Dutch standard pattern — postcode + house number → auto-fill street and city — is missed entirely. This adds typing time, increases error likelihood (typos in street name, mismatched city), and creates friction at one of the higher-anxiety steps of checkout. The implementation cost is low: NL postcode APIs (Postcode.nl, MyParcel, PostNL) integrate with most platforms in 1-2 days, or Google Place Autocomplete works for international fallback.

**Recommendation**
Implement postcode-first pattern: visitor enters postcode + house number, system auto-fills street and city (editable). Use a NL-specific provider (Postcode.nl recommended for accuracy in NL/BE) with Google Place Autocomplete as international fallback. Auto-tab from postcode to house number after valid postcode entered. Show field-level success indicator (green checkmark) when address resolves. Provide "Adres niet gevonden? Vul handmatig in" recovery path for edge cases. On mobile, ensure postcode field triggers appropriate keyboard (default for NL alphanumeric postcodes).

**Test specification**
- **Hypothesis:** If we implement postcode-first autocomplete for NL/BE addresses, then form-error rate will decrease and address-step completion rate will increase because the dominant regional pattern reduces friction and typos (Baymard address-field research; Fitts's Law).
- **Variant A:** Manual entry of all address fields
- **Variant B:** Postcode + house number → auto-fill street and city
- **Primary metric:** address-step completion rate (visitors entering address step → continuing to next step)
- **Secondary metrics:** form-error rate, time to complete address step, address-correction rate
- **Expected impact:** +4% to +12% on address-step completion; -30% to -50% on address-related errors
- **ICE:** I=7, C=8, E=6 → 7.0
- **Source:** Baymard Institute address-field research; Fitts's Law

---

## Example 5: 🟠 Important — Trust signals throughout flow (mid-market specialty retailer)

### 🟠 Trust signals — No trust signals visible during payment selection

**Diagnosis**
The payment selection screen shows payment method radio buttons (iDEAL, credit card, PayPal) with no surrounding trust signals. No lock icon, no "Veilige verbinding" microcopy, no payment-method logos above selection, no return-policy snippet, no customer support availability. Per MECLABS' Conversion Sequence Heuristic, anxiety is at its peak during payment selection — visitors are about to commit financial details, and the absence of trust signals leaves anxiety unresolved at the critical moment. Per Cialdini's authority principle, payment-method logos before selection (not just after) and visible security indicators are standard authority signals. Per Baymard's checkout research, trust signals adjacent to the payment area increase payment-step conversion by 5-15% in tested implementations.

**Recommendation**
Add a trust block adjacent to the payment selection area containing: (1) row of payment-method logos visible BEFORE selection (iDEAL, Visa, Mastercard, PayPal, Klarna) — shows what's accepted, signals legitimacy; (2) lock icon + "Veilige betaling via [provider]" microcopy; (3) one-line return-policy snippet "14 dagen retour, gratis"; (4) support availability "Vragen? Chat met ons — vandaag 9:00-22:00" with click-to-chat. Keep the visual style restrained — small icons, secondary text color, consistent with brand. The block should reassure, not shout.

**Test specification**
- **Hypothesis:** If we add a compact trust block adjacent to payment selection containing payment-method logos, security signals, return policy, and support availability, then payment-step conversion will increase because anxiety at the highest-anxiety moment is reduced (MECLABS Conversion Sequence Heuristic; Cialdini authority; Baymard checkout research).
- **Variant A:** Payment selection with no adjacent trust signals
- **Variant B:** Payment selection + trust block (payment logos + security + return policy + support)
- **Primary metric:** payment-step conversion rate
- **Secondary metrics:** overall checkout completion rate, time on payment step
- **Expected impact:** +4% to +10% on payment-step conversion rate
- **ICE:** I=7, C=8, E=8 → 7.7
- **Source:** MECLABS Conversion Sequence Heuristic (anxiety factor); Cialdini's authority principle; Baymard Institute checkout trust research

---

## Example 6: 🟢 Nice-to-have — Final-step button copy (mid-market, ambiguous CTA)

### 🟢 Final-step button copy — "Doorgaan" button at final commit step is ambiguous

**Diagnosis**
The final commit button at the payment step reads "Doorgaan". The visitor cannot tell from this copy whether this is the final commit (charge my card now) or another intermediate step. Per Baymard's final-step research, button copy at the commit step must explicitly confirm the action — generic forward-direction words ("Continue", "Next", "OK", "Doorgaan") create hesitation and increase abandonment. The strongest pattern Baymard has identified: button copy that includes the action AND the amount ("Pay €127.50", "Betaal €127,50", "Plaats bestelling — €127,50"). This pattern combines commitment clarity with loss-aversion framing (Kahneman/Tversky) — visitors see exactly what they're committing to and feel certainty about the outcome.

**Recommendation**
Change the final-step button copy from "Doorgaan" to "Betaal €[amount]" or "Plaats bestelling — €[amount]" depending on brand voice. Premium brands: "Bevestig bestelling — €127,50" (subtle, certain). Mid-market: "Plaats bestelling — €127,50" (clear, balanced). Value brands: "Betaal nu €127,50" (action-led). Ensure the total amount in the button matches the order summary total dynamically. Place the button below the order summary so the total is visible adjacent to the button. Keep the button as the single primary CTA — no competing buttons at this step.

**Test specification**
- **Hypothesis:** If we change the final-step button copy from "Doorgaan" to "Plaats bestelling — €[amount]", then payment-step conversion will increase because the action is unambiguous and the visible amount reinforces commitment (Baymard final-step research; Kahneman/Tversky loss aversion).
- **Variant A:** "Doorgaan" generic button copy
- **Variant B:** "Plaats bestelling — €127,50" specific button copy with amount
- **Primary metric:** payment-step conversion rate
- **Secondary metrics:** overall checkout completion rate, time on final step
- **Expected impact:** +2% to +6% on payment-step conversion (smaller impact magnitude because it's a single copy change at an already-converting step)
- **ICE:** I=4, C=8, E=10 → 7.3 — *Marginal between Important and Nice-to-have; placed Nice-to-have because the impact magnitude is lower than other findings, even though ease and confidence are very high.*
- **Source:** Baymard Institute final-step research; Kahneman & Tversky loss aversion

---

## What makes these examples high-quality

- **Specific:** every observation names an exact field, step, button, or screen element
- **Sourced:** every claim references a specific principle, study, or institution
- **Brand-aware:** recommendations consider whether they fit the brand snapshot (premium vs mid-market vs value)
- **Region-aware:** NL-specific findings (iDEAL, postcode autocomplete) acknowledge regional payment landscape
- **Honest about uncertainty:** when data is missing, the finding says so and recommends research, not action
- **Test-ready:** hypothesis follows "If X, then Y, because Z"; primary metric is named (checkout metrics: checkout completion rate, per-step abandonment, form-error rate, payment-step conversion); ICE is justified by the breakdown
- **Concrete copy and behavior:** not "improve the form" — actual field counts, exact button copy, specific payment method orders
- **Out of security/compliance scope:** none of the examples claim "secure" or "AVG-compliant" — they stay in UX/trust-signal territory
- **Honest about impact magnitude:** checkout findings often have very high impact (15-40%+ on specific metrics) when fundamental like guest checkout or iDEAL; smaller copy changes are honest at +2-6%
- **Dutch translations natural:** when output is Dutch, JTBD framing avoids "huren"; terms like "afrekenen", "bestelling", "veilige betaling" used naturally; payment-method names kept in original form

Always match this standard. If a finding can't reach this standard, either dig deeper or remove it from the audit.
