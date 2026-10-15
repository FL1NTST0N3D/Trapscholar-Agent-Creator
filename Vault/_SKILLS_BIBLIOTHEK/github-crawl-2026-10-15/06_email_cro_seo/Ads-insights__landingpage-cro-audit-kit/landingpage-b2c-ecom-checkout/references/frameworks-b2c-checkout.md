# Frameworks for B2C Ecommerce Checkout Audits

This reference file contains the CRO frameworks, principles, and applied research used in the checkout audit. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

Checkout audits are uniquely prone to fabricated findings because so much of checkout is session-dependent, JavaScript-rendered, and conditionally displayed. Examples:
- Express-checkout buttons (Apple Pay, Google Pay — only show for compatible devices/browsers)
- Address autocomplete suggestions (only render after typing starts)
- Payment method options (vary by region, cart contents, account state)
- Error states (only appear after validation fires)
- Sticky CTAs (only after scroll)
- Guest-checkout vs login forms (toggled by user choice)

**For every finding in these categories, verify the claim against screenshots before delivering.** A finding that says "no Apple Pay available" while the screenshot shows it (or doesn't show the payment step at all) is worse than no finding.

If a finding cannot be visually verified, either:
1. Remove it from the audit, or
2. Convert it to a "research first" finding asking the user to confirm before testing

This rule overrides every other instruction in this file.

---

## CRITICAL — Stay out of security and compliance territory

Checkout is the obvious place to comment on "is this secure?" and "is this AVG-compliant?". **Do not.** This is a CRO/UX audit, not a security or compliance audit.

**The hard rules:**
- A finding may RECOMMEND adding visible trust signals (lock icons, "Veilige verbinding" microcopy, payment-method badges)
- A finding may RECOMMEND improving the UX of AVG-consent (clarity, position, copy) — this is UX, not legality
- A finding may NOT claim the checkout is "secure" or "insecure"
- A finding may NOT claim the checkout is "AVG-compliant" or "non-compliant"
- A finding may NOT diagnose payment integration failures from a screenshot

When in doubt, frame as: "Visitors lack visible signals of [X]; consider [UX improvement]" rather than "Your checkout is missing [security/compliance feature]."

This protects the user from acting on false legal/security claims and keeps the audit within CRO scope.

---

## CRITICAL — Conditional HTML strings on checkout pages

Most ecom platforms ship status strings into the DOM as **conditional placeholders** that JavaScript decides whether to render. The string is always in HTML; the visitor only sees it under specific conditions.

Checkout-specific examples:
- Shopify: `"Apple Pay"`, `"Shop Pay"`, `"Order summary"`, `"Discount code applied"` — all hardcoded in Liquid templates, conditionally displayed
- WooCommerce: payment-method labels, shipping-method strings, validation messages
- Magento: tax-display strings, billing-vs-shipping toggles

**Implication for the audit:** finding "iDEAL" in HTML does NOT mean it's surfaced to NL visitors. Finding a "guest checkout" string in HTML does NOT mean visitors see the option. Finding a free-shipping calculator does NOT mean it's active.

**The hard rule:** payment-method availability per region, guest-checkout availability per session, error-message presence, and conditional checkout content rely on screenshots only. Never on HTML strings.

---

## Core frameworks (apply across the entire audit)

### Baymard Institute checkout research
Baymard is the gold standard for checkout research:
- 17.8% of users abandon during the checkout flow itself (separate from cart abandonment)
- Average large ecom site has 39-69 checkout usability issues
- The cumulative effect of fixing the top 10 checkout issues averages **20-35% increase in checkout completion rate**
- Checkout is Baymard's most-tested page type — confidence scores for checkout findings can legitimately be higher than for other pages

### MECLABS Conversion Sequence Heuristic
C = 4m + 3v + 2(i−f) − 2a

On checkout pages:
- **m (motivation):** very high — visitor is committing to purchase
- **v (value):** must be reinforced via order summary persistence + total clarity
- **i (incentive):** less relevant on checkout (cart-stage territory)
- **f (friction):** the dominant lever on checkout — form fields, address input, payment selection, error handling
- **a (anxiety):** the second dominant lever — security, payment trust, returns policy, support availability

**The checkout exists to minimize f and a.** Every audit finding ultimately targets one of these two levers.

### Fogg Behavior Model (B = MAT)
Behavior happens when Motivation, Ability, and a Trigger meet:
- **Motivation:** highest on checkout of the entire site — visitor has committed
- **Ability:** must be maximized — forms must be simple, addresses easy, payment frictionless
- **Trigger:** primary CTA per step must be unmissable

The checkout's job is to **maximize Ability** — remove every avoidable obstacle between motivation and completion.

### Cialdini's principles on checkout
- **Authority** — payment-method icons, certification logos, "Veilige verbinding" signals
- **Social proof** — "12,000+ orders shipped this month" — rarely used on checkout but effective
- **Reciprocity** — free shipping framed as gift (continuation from cart-page)
- **Commitment-consistency** — once visitor has reached checkout, they're psychologically committed; small wins (saved address, applied discount) reinforce commitment
- **Liking** — visible support contact (chat, phone, hours) reduces anxiety via approachability

### Nielsen Norman heuristics applied to checkout
- **#1 Visibility of system status** — progress indicator, current step, what's saved
- **#5 Error prevention** — inline validation, masks for phone/postcode, autocomplete
- **#6 Recognition over recall** — order summary persistent across steps
- **#9 Help users recognize and recover from errors** — clear error messages with recovery paths

### Jobs-to-be-Done on checkout
Visitors on checkout pages are doing one of three jobs:
1. **Complete the purchase efficiently** — most common; wants minimal friction
2. **Verify everything is correct before committing** — anxiety-driven; wants visibility
3. **Compare delivery/payment options** — exploration mode; wants choice clarity

A well-designed checkout serves all three. Most failures over-serve #2 (too many confirmation steps) and under-serve #1 (too much friction) and #3 (poor option clarity).

**Important Dutch translation:** never use "huren" for JTBD framing. Instead: "kiezen voor", "zoeken om af te ronden", "bezoekers die willen afrekenen".

---

## Category 1: Progress indicator & flow clarity

### Nielsen Norman heuristic #1 — visibility of system status
The visitor must always know:
- Where they are in the flow
- How many steps remain
- That progress is being saved
- That returning to a previous step is possible without losing data

### Single-page vs multi-step considerations
- **Single-page checkout:** progress is implicit via section presence; the "indicator" is often a clear section headers (Contact, Shipping, Payment)
- **Multi-step checkout:** explicit step-indicator at top is essential (Step 1 of 4, or visual breadcrumb)
- **Hybrid (Shopify Plus accordion):** combines both — clear step indicators that collapse/expand

### Baymard checkout-flow research
- Visible progress indicators reduce abandonment by 5-12% on multi-step checkouts
- "Number of steps remaining" framing outperforms "current step" framing
- Step indicators that show step names (Contact → Address → Shipping → Payment) outperform numbered-only indicators
- For 2-step checkouts: indicator is optional but harmless; for 3+ steps: indicator is essential

### Best practices
- Visible step indicator at top of each step
- Current step visually distinct (filled vs outline, color, weight)
- Completed steps clickable (return path) on multi-step
- Single-page: clear section headings with completion checkmarks
- Mobile: progress indicator must remain visible (sticky top bar or compact pill)

### Common failures
- No step indication on a 4-step checkout (visitors don't know when it ends)
- Step indicator hidden on mobile after scroll
- "Step 2 of 5" with no step names — visitors don't know what each step holds
- Cannot return to earlier step without losing entered data
- Single-page checkout without clear section delineation

---

## Category 2: Guest checkout vs account creation strategy

### Baymard guest-checkout research — one of the most important findings
- **24% of users abandon checkout when forced to create an account**
- This is the **single most fixable checkout abandonment cause** for sites that force account creation
- Guest checkout option must be visually equal to or more prominent than account creation
- "Express checkout" via Apple Pay / Shop Pay effectively bypasses this entirely for returning users

### Fogg Behavior Model — ability axis
Forcing account creation is a massive **ability** reduction:
- Adds 4-8 form fields (email, password, password confirmation, optional profile fields)
- Adds cognitive load (password requirements, email verification)
- Adds friction at the worst possible moment (post-cart commitment)

### Best practices
- Default to guest checkout for first-time visitors
- Make guest checkout the prominent option ("Continue as guest" or "Continue without account")
- Offer account creation as opt-in AFTER purchase ("Create account to track your order — just set a password")
- For returning visitors: show login but never force it
- Use email-only "magic link" or social login as alternatives to password-required accounts

### The "post-purchase account creation" pattern
The strongest pattern Baymard has identified:
1. Visitor checks out as guest with email + address
2. Order confirmation page offers "Set a password to create an account — your details are already filled in"
3. One-click account creation post-purchase

This converts hesitant guests into customers without blocking the purchase.

### Common failures
- "Sign in or Create account" required before any other field
- Guest checkout hidden behind "or continue as guest" small link
- Account creation forced for first-time visitors
- Account creation pre-checked default
- Required password fields visible before visitor commits to creating account

### Brand calibration
- Premium brands: subtle guest checkout, often default; account creation framed as future-purchase convenience
- Mid-market: guest checkout prominent + account creation as clear alternative
- Value brands: aggressive guest checkout; account creation deferred to post-purchase
- Subscription / repeat-purchase brands: stronger account creation push (justifiable here)

---

## Category 3: Form field count & cognitive load

### Baymard form-field research
- The average ecom checkout has 23.5 form fields — but a well-optimized checkout needs **only 8-12 fields**
- Each additional field correlates with a measurable abandonment increase
- The largest field-count reductions come from: removing optional fields, combining first+last name, autocompleting address from postcode, defaulting "billing same as shipping"

### Hick's Law applied
Each field is a decision point. More decisions = longer decision time = higher abandonment.

### Best practices
- Remove every field that isn't strictly necessary for fulfilling the order
- Combine fields where possible:
  - First name + Last name → Full name (controversial — Baymard split, lean toward full name unless billing requires separate)
  - Street + Number → Street address line 1 (with autocomplete)
  - City + State + Zip → Often auto-fillable from postcode in NL/EU
- Default "Billing same as shipping" checked
- Hide optional fields behind expander ("Add a delivery instruction (optional)")
- Phone number: justify why it's needed ("For delivery questions only")

### Common failures
- Asking for phone number without explanation (creates suspicion)
- Required "Company name" field for B2C orders
- "Date of birth" required without clear purpose
- Newsletter signup pre-checked as form field
- Multiple address-line fields all required when one would suffice
- Required password fields (see category 2 — account creation)

### NL-specific considerations
- Postcode + house number → can autofill street + city via postcode API (Postcode.nl, MyParcel, etc.)
- BTW number for facturen is B2C-irrelevant; should not appear in B2C checkout
- "Aanhef" (Dhr/Mevr) is often unnecessary for ecom

### Brand calibration
- Premium brands: minimal fields, generous spacing, single-column layout
- Mid-market: optimized field count with smart defaults
- Value brands: aggressive field minimization, often only email + address required

---

## Category 4: Address input UX

### Baymard address-field research
Address input is one of the highest-abandonment points in checkout:
- 67% of users encounter an address-related error during checkout
- Postcode autocomplete (NL/UK/DE) reduces address errors by 50-70%
- Google Place autocomplete reduces address errors by 40-60%
- Inline validation prevents most errors before submission

### NL/EU postcode-first pattern
The Dutch/Belgian/German/UK standard: visitor types postcode + house number → system fills street, city, sometimes house number suffix. This is the dominant pattern in NL ecom.

Implementation options:
- **Postcode.nl** (NL-specific, paid)
- **MyParcel** (NL/BE, integrated with shipping)
- **Google Place Autocomplete** (international, free up to limits)
- **PostNL / Bpost native APIs** (carrier-integrated)

### Fitts's Law on mobile
Address fields are tap-target heavy. Each field needs:
- Minimum 44px tap height
- Adequate spacing between fields (avoid mis-taps)
- Appropriate keyboard type (numeric for postcode, default for street)

### Best practices
- Postcode-first pattern in NL/EU markets
- Auto-tab to next field after postcode complete
- House number + suffix in separate fields where applicable
- Editable autocompleted fields (visitor must be able to correct)
- "Address not found" recovery path (manual entry option always available)
- Inline validation showing field-by-field success

### Common failures
- Manual address entry without postcode autocomplete (NL/EU)
- Postcode autocomplete that doesn't trigger until tab/blur
- Autocomplete that overwrites manually entered data without warning
- No "Address not found" path (visitor stuck in invalid state)
- Country selector buried instead of detected/defaulted
- Mobile keyboard doesn't switch to numeric for postcode/phone

### Brand calibration
Address UX is largely platform-driven, but small choices matter:
- Premium brands: clean autocomplete with subtle animation
- Mid-market: standard postcode-first pattern
- Value brands: aggressive autocomplete + minimal fields

---

## Category 5: Shipping options presentation

### Baymard shipping-options research
Shipping presentation directly impacts both checkout completion AND average order value:
- Visible delivery date estimates increase completion by 5-12%
- Sorted by speed (fastest first) outperforms sorted by price (cheapest first) for most brands
- 3 shipping options is the sweet spot (Hick's Law); 5+ options creates paralysis
- Free shipping clearly framed as gift outperforms free shipping as default

### Kahneman/Tversky default effect
The default-selected shipping option drives ~70% of selections:
- Defaulting to most expensive: revenue-positive but conversion-negative
- Defaulting to cheapest: conversion-positive but margin-negative
- Defaulting to "recommended" middle option: usually optimal balance

### Best practices
- Show 2-3 clear options with names, delivery dates, and prices
- Default to recommended option (not cheapest, not most expensive)
- Show delivery date (not just "2-3 business days"; actual date "Donderdag 14 mei")
- Premium options framed by benefit ("Tomorrow before 12:00 — €9.95")
- Express options visible but not pre-selected
- Free shipping (when qualified) prominent and framed positively

### Common failures
- "Standard shipping" vs "Express shipping" with no dates
- 5+ shipping carrier options creating paralysis
- Default to most expensive option (revenue grab; trust-damaging)
- Free shipping below threshold not communicated until checkout
- Same-day options shown but not actually available at current time
- Shipping price hidden until later step

### NL-specific considerations
- PostNL vs DHL vs DPD options common
- Pickup point ("ophaalpunt") as alternative to home delivery
- Saturday delivery as paid option
- Specific time windows for premium brands

---

## Category 6: Payment methods presentation

### Baymard payment-options research
Payment method selection is a critical trust + ability moment:
- Showing only 1-2 payment methods reduces completion by 8-15% (visitor's preferred method missing)
- Showing 8+ payment methods reduces completion by 3-7% (choice paralysis)
- Regional payment methods missing is a top-5 abandonment cause in NL/DE/SE/PL markets
- Default selection should be the most common method for the region

### Regional payment method requirements
**Netherlands:**
- iDEAL (60%+ of NL ecom payments) — mandatory
- Klarna Pay Later — high adoption
- Klarna Pay in 3 — growing
- Credit card — necessary for international
- PayPal — moderate adoption

**Germany:**
- SOFORT / Klarna Bank Transfer — mandatory
- PayPal — very high adoption
- Credit card — moderate
- Invoice (Rechnung) — significant share

**Belgium:**
- Bancontact — mandatory
- iDEAL (cross-border NL) — common
- Credit card — moderate

**International:**
- Credit/debit card (Visa, Mastercard)
- PayPal
- Apple Pay / Google Pay

### Cialdini authority — payment trust
Payment method icons signal legitimate operation:
- Visible payment-method logos before selection (not just after)
- Trust badges (Trusted Shops, Thuiswinkel Waarborg, Norton Secured) near payment area
- Security microcopy ("Veilige betaling via [provider]")

### Best practices
- Display 4-6 region-appropriate payment methods
- iDEAL bank selector inline (not modal popup)
- Klarna options grouped (Pay later, Pay in 3, Pay over time)
- Apple Pay / Google Pay above primary CTA when available
- Credit card as universal fallback
- Visual hierarchy: regional default first, then alternatives

### Common failures
- iDEAL missing on NL checkout (instant 60% addressable-market loss)
- Bank list for iDEAL hidden behind dropdown instead of inline
- Klarna not offered (missing growing buy-now-pay-later segment)
- Apple Pay shown to Android users (dead UI)
- Generic "Online banking" instead of named regional methods

---

## Category 7: Trust signals throughout flow

### MECLABS anxiety axis on checkout
Checkout-stage anxiety is highest at:
1. Account creation prompt (resolved via guest checkout — category 2)
2. Address entry (resolved via autocomplete + visible privacy — category 4)
3. Payment selection (resolved via trust signals — this category)
4. Final commit (resolved via summary clarity — category 10)

### High-value trust signals on checkout
- **Payment-method logos** prominent before payment selection
- **SSL / lock icon** visible near payment area
- **"Veilige verbinding" / "Secure checkout"** microcopy
- **Return policy snippet** near commit step ("14 dagen retour, gratis")
- **Customer support availability** ("Vragen? Chat met ons — vandaag 9:00-22:00")
- **Money-back guarantee** if applicable
- **Order confirmation expectation** ("U ontvangt direct een bevestiging per email")

### NL-specific trust signals
- Thuiswinkel Waarborg badge
- WebwinkelKeur / Kiyoh rating with link
- KvK number in footer
- "BTW inbegrepen" clarity

### Best practices
- Trust signals visible at every step, not just final
- Payment-method icons before selection
- Concrete claims (specific return window, specific support hours)
- Microcopy that reduces anxiety at the moment of input ("Email only used for order confirmation")

### Common failures
- Trust signals only in footer (often hidden on checkout pages)
- Generic "secure" badges without context
- Return policy link instead of inline snippet
- Customer support visible only on contact page, not in checkout
- "Your information is safe" vague claim instead of concrete signal

### AVG-consent UX (in scope as UX, not as legality)
The presence and design of AVG-consent affects checkout flow:
- Pre-checked consent boxes create friction when visitor must uncheck
- Burying consent in fine print creates AVG legitimacy questions visitors recognize
- Clear, unchecked consent for marketing is the cleanest UX pattern
- Order-fulfillment consent is implied by purchase — no checkbox needed

A finding may comment on consent UX. A finding may NOT claim the checkout is AVG-compliant or not.

---

## Category 8: Error handling & validation

### Baymard form-error research
Error handling is a make-or-break checkout element:
- 67% of users encounter at least one error during checkout
- Of users who encounter errors, 21% abandon
- Inline validation (on blur) reduces abandonment-after-error by 22% vs submit-time validation
- Clear error messages with recovery instructions outperform generic "Invalid input"

### Nielsen Norman heuristic #5 — error prevention
The best error message is the one that never appears. Prevention via:
- Input masks (postcode format, phone format)
- Autocomplete (address, country)
- Format hints below fields ("Format: 1234 AB")
- Disabled submit until required fields valid

### Best practices
- Validate on blur (after user leaves field), not on every keystroke
- Validate before submit, not only at submit
- Error messages: specific + actionable ("Postcode must be 4 digits + 2 letters, e.g. 1234 AB")
- Errors visible at the field, not at top of page
- Successful field validation shown subtly (checkmark, green border)
- Submit button never shown active if validation fails

### Common failures
- All errors revealed only at submit-time
- Errors at top of page instead of inline
- Generic "Please fill all required fields" without identifying which
- Errors that don't explain the requirement ("Invalid email" without showing valid format)
- Errors that lose data when shown (page reload pattern)
- Submit button always active even when fields invalid

### Mobile error UX
- Errors must not be hidden by keyboard
- Field with error should scroll into view automatically
- Error styling must be visible at small sizes
- Tap on error message should focus the offending field

---

## Category 9: Order summary visibility & persistence

### Baymard order-summary research
Order summary persistence is one of the most impactful checkout UX elements:
- Persistent order summary increases checkout completion by 5-12%
- Visitors check the summary 3-5 times during checkout on average
- Hiding the summary on mobile (collapse to total only) is acceptable when expandable

### Nielsen Norman recognition-over-recall
Visitors should never have to remember what they're buying. The cart contents must be visible (or one tap away on mobile) throughout the checkout flow.

### Best practices
- **Desktop:** persistent sidebar with line items, qty, prices, totals
- **Mobile:** collapsed total at top with tap-to-expand, OR section above form
- All cost components visible: subtotal, shipping, tax, discount, total
- Edit links to return to cart (with confirmation that no data is lost)
- Order summary updates dynamically as shipping/payment selected

### Common failures
- Summary only on first step, hidden on subsequent steps
- Summary requires scrolling to see on mobile
- No way to edit cart from checkout
- Total not visible at all without scrolling
- Discount applied earlier not shown in summary
- Tax/shipping appearing as surprise additions to total

### Brand calibration
- Premium brands: minimalist summary, generous spacing, clean typography
- Mid-market: full information summary with all line items visible
- Value brands: prominent total + savings highlighting

---

## Category 10: Final-step confirmation & button copy

### Baymard final-step research
The final commit button is one of the most-tested elements in CRO history:
- Button copy matters: action-oriented + specific outperforms generic
- Final price visible adjacent to button ("Pay €127.50" beats "Place order")
- Terms-of-service link should not be a checkbox blocker
- Last-moment cross-sell on the commit screen reduces completion by 3-8%

### Loss aversion (Kahneman/Tversky)
At final commit, the visitor is most susceptible to loss aversion:
- "Your order will be confirmed and shipped" reassures
- "Are you sure?" warnings increase abandonment
- Showing what they'll lose if they don't proceed (cart items, savings) reinforces commitment

### Best practices
- Button copy: "Pay €127.50" or "Plaats bestelling — €127,50" or "Confirm order"
- Avoid: "Submit", "Continue", "OK", "Next" (ambiguous at final step)
- Total visible on or directly adjacent to button
- Terms-of-service as text link below button, not blocking checkbox
- Privacy/AVG consent already handled earlier in flow
- No last-moment cross-sell that competes with commit
- Single primary CTA, no choice paralysis

### Common failures
- "Continue" or "Next" at the final step (ambiguous; visitor unsure if this is the commit)
- "I agree to terms" required checkbox blocking the button
- Multiple competing CTAs (Pay + Save + Cancel all visually equal)
- Cross-sell modal appearing before commit
- Final total not visible near button
- Button copy doesn't confirm action ("Submit" vs "Pay €127.50")

### Brand calibration
- Premium brands: "Bevestig bestelling" + final amount, subtle styling
- Mid-market: "Plaats bestelling — €X" with prominent button
- Value brands: "Betaal nu €X" with aggressive CTA styling

---

## Category 11: Mobile checkout-specific friction

### Baymard mobile checkout research
Mobile checkout has unique friction not present on desktop:
- Mobile checkout completion rate averages 1.5-2x lower than desktop
- Sticky CTA on mobile checkout increases completion by 6-12%
- Numeric keyboard for numeric fields increases entry speed by 30%+
- Native autofill compatibility (input names) increases completion materially

### Mobile-specific best practices

**Keyboard types per field:**
- Email: `type="email"` triggers email keyboard with `@` and `.com`
- Phone: `type="tel"` triggers numeric keyboard
- Postcode: `inputmode="numeric"` for digit-only postcodes; default for NL alphanumeric
- Credit card: `inputmode="numeric"` + `autocomplete="cc-number"`
- CVV: `inputmode="numeric"` + `autocomplete="cc-csc"`

**Autofill compatibility:**
- Use standard `autocomplete` attributes (`name`, `email`, `tel`, `street-address`, `postal-code`, `cc-number`, etc.)
- Single-purpose fields (don't combine name fields if autofill conflicts)
- Browser/keychain autofill saves visitors 30-60 seconds

**Sticky elements:**
- Primary CTA sticky at bottom on long checkout forms
- Order total visible at top sticky bar (collapsible to expand summary)
- Step indicator persistent in sticky header

**Payment-app deep links:**
- iDEAL: native bank app integration when bank selected
- Apple Pay: native bottom sheet
- Google Pay: native bottom sheet
- Klarna: native app or in-app web for repeat customers

**Fitts's Law on mobile:**
- All tap targets minimum 44×44px
- Adequate spacing between fields (8-12px minimum)
- CTA button height 48-56px

### Common mobile failures
- Default text keyboard for numeric fields (slow + error-prone)
- No autofill attributes (visitors retype saved data)
- Sticky CTA disabled or absent
- Form fields too close together causing mis-taps
- Modal popups not closeable on mobile
- iDEAL bank selector requiring scroll within a constrained dropdown
- Payment-app deep links broken or absent

### Brand calibration
Mobile checkout is largely platform-driven, but small choices matter:
- Premium brands: subtle sticky elements, refined keyboard behavior
- Mid-market: standard sticky CTA + autofill optimization
- Value brands: aggressive mobile optimization, payment-app priority

---

## Notes on brand calibration

Always reread the brand snapshot before finalizing recommendations. The same finding category leads to different recommendations depending on brand and AOV:

**Example: Guest checkout strategy**
- Premium brand (AOV €500+): guest checkout subtle, account creation post-purchase via order confirmation
- Mid-market: guest checkout prominent + account creation as visible alternative
- Subscription brand: account creation more justifiable (recurring purchase need)
- Value brand: aggressive guest checkout, account deferred entirely

**Example: Payment method emphasis**
- Premium NL brand: iDEAL prominent + credit card; minimal BNPL
- Mid-market NL: iDEAL + Klarna BNPL + credit card + PayPal
- Value brand: aggressive BNPL push (Klarna Pay in 3, Klarna Pay later)

**Example: Final CTA copy**
- Premium: "Bevestig bestelling — €127,50"
- Mid-market: "Plaats bestelling — €127,50"
- Value: "Betaal nu €127,50"

Recommendations that don't match the brand snapshot are wrong, even if they would work for a different brand.

---

## Test-readiness check

Before finalizing each finding, verify:
- [ ] Diagnosis cites a specific principle or source
- [ ] Recommendation is concrete (specific copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z" structure
- [ ] Primary metric is named (checkout metrics: checkout completion rate, per-step abandonment, form-error rate, payment-step conversion)
- [ ] ICE score is justified by the I/C/E breakdown
- [ ] Recommendation matches the brand snapshot and AOV impression
- [ ] No security/compliance claims made (stayed in CRO/UX scope)
- [ ] Dutch output: no literal jargon translation ("huren" check)

If any box is unchecked, rework the finding before delivering.
