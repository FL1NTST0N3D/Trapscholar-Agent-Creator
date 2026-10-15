# Frameworks for B2C Ecommerce PDP Audits

This reference file contains the CRO frameworks, principles, and applied research used in the audit. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

Many of the categories below involve checking whether an element is **present, absent, or insufficient** on the page. Examples:
- Cross-sell carousels (often JavaScript-rendered, invisible in HTML)
- Reviews modules (often lazy-loaded)
- Sticky CTAs (only visible after scroll)
- Image galleries with zoom/detail shots (image filenames in HTML do not reveal content)
- Urgency signals, stock counters, wishlist buttons
- "Complete the look" / "Style with" sections

**For every finding in these categories, verify the claim against screenshots before delivering.** The single most common failure mode of this audit is claiming an element is missing when it is visually present but invisible in fetched HTML. A finding that says "no cross-sell module" while the page has a "Style with" carousel is worse than no finding at all — it destroys credibility.

If a finding cannot be visually verified, either:
1. Remove it from the audit, or
2. Convert it to a "research first" finding asking the user to confirm before testing

This rule overrides every other instruction in this file.

---

## CRITICAL — Conditional HTML strings (Shopify, WooCommerce, Magento)

Most ecom platforms ship status strings into the DOM as **conditional placeholders** that JavaScript decides whether to render. The string is always in HTML; the visitor only sees it under specific conditions.

Common examples:
- Shopify: `"Sold out"`, `"Uitverkocht"`, `"Pre-order"`, `"Op voorraad"`, `"Sale"`, `"From €X"`, price-was/price-now markup — all hardcoded in the Liquid template, conditionally displayed based on `product.available`, `variant.inventory_quantity`, `compare_at_price`, etc.
- WooCommerce: `"Out of stock"`, `"In stock"`, `"On backorder"`, variant labels — all present in HTML regardless of actual state.
- Magento: similar pattern with `out-of-stock` / `in-stock` classes always present.

**Implication for the audit:** finding a stock-state string in HTML does NOT mean the visitor sees that state. The string may be invisible, may show a different label, or may be overridden by inventory logic.

**The hard rule:** stock state, availability, pre-order status, and price-status findings rely on screenshots only. Never on HTML strings.

A finding may legitimately say: *"this PDP shows no visible stock indication — consider adding 'in stock' or 'X left' to reduce availability uncertainty (Baymard cart-abandonment research)"*.

A finding may NOT say: *"the HTML says 'sold out' but the CTA is active — likely a bug or conflict"*. That finding is almost always wrong; it is just template-default behavior.

Same logic applies to pricing strings (`compare_at_price` is in HTML for every product but only renders on sale items) and badge strings (`new-arrival`, `featured`, `bestseller` are often template-present but conditionally rendered).

---

## Core frameworks (apply across the entire audit)

### Cialdini's principles of influence
- **Social proof** — reviews, ratings, customer photos, "X people viewing now", bestseller badges
- **Authority** — expert endorsements, certifications, "as seen in" press logos
- **Scarcity** — limited stock, time-limited offers, "only X left"
- **Liking** — relatable models, brand voice, founder story
- **Reciprocity** — free samples, free shipping, useful content
- **Commitment/consistency** — small first commitments (e.g. save to wishlist) leading to purchase

### Kahneman & Tversky — behavioral economics
- **Anchoring** — show original price next to discount price; the higher number anchors perception
- **Loss aversion** — "Don't miss out" frames loss; "limited stock" frames potential loss of access
- **Framing effects** — "free returns" vs. "no cost to return" — same fact, different perception
- **Cognitive ease** — System 1 vs. System 2: PDP should let users decide on autopilot, not require analysis

### Fogg Behavior Model (B = MAT)
Behavior happens when Motivation, Ability, and a Trigger meet at the same moment. Apply to PDP:
- **Motivation:** strong value proposition, social proof, brand affinity
- **Ability:** low friction (clear price, simple variant selection, fast page load)
- **Trigger:** prominent add-to-cart, urgency signal

### Jobs-to-be-Done
What "job" is the customer hiring this product for? PDP copy should speak to the job, not the feature list.
- Feature: "stainless steel water bottle, 750ml"
- Job: "stays cold for 24 hours on long workdays without leaking in your bag"

### MECLABS Conversion Sequence Heuristic
C = 4m + 3v + 2(i−f) − 2a
- m = motivation of user (cannot be changed by PDP)
- v = clarity of value proposition (huge lever)
- i = incentive to take action now
- f = friction in the action
- a = anxiety (concerns, doubts)

Use this as a mental model when scoring impact: clarity (v) is the single biggest lever you control on PDP.

### WiderFunnel LIFT model
Six factors that influence conversion:
1. Value proposition (the foundation)
2. Relevance (does the page match expectation)
3. Clarity (is the offer and CTA clear)
4. Anxiety (what doubts exist)
5. Distraction (what pulls attention away)
6. Urgency (why act now)

LIFT is a strong organizing framework when writing the audit narrative.

---

## Category 1: Hero & imagery

### Baymard Institute research highlights
- **Default image count:** users expect 5+ images for considered purchases; 3 or fewer signals low quality
- **In-context shots are critical** — users want to see scale, fit, usage context. Studio-only shots are insufficient
- **Zoom functionality** is expected; pinch-zoom on mobile and hover-zoom on desktop
- **Video presence** drives PDP-to-cart by 6-30% in Baymard's testing
- **First image should be representative**, not the most stylized — users feel deceived when product differs from hero shot

### Common patterns
- Lifestyle vs. clinical: lifestyle hero for emotion-driven purchases (apparel, home), clinical for utility (electronics, tools)
- Variant-aware imagery: when user selects "red", show red product first
- 360-degree views for considered purchases

### Brand calibration
- Premium brands: editorial lifestyle photography, single hero image, lots of whitespace
- Mid-market: balance of lifestyle and clinical, 5-7 images
- Value brands: clinical clarity, multiple angles, focus on quantity over editorial quality

---

## Category 2: Title & short description

### Best practices
- **Product title structure:** [Brand] [Product name] [Key differentiator/variant]
- **Length:** 60-80 characters is the sweet spot for scanability and SEO
- **Front-load the job-to-be-done** when brand is not the primary purchase driver
- **Short description (just below title):** 1-2 sentences capturing the "job" — not a feature list

### Common failures
- Title only contains brand + product code ("Nike AB-123")
- No short description; user has to scroll to learn what the product does
- Title repeats in description — wasted space

---

## Category 3: Price presentation

### Anchoring (Kahneman/Tversky)
- Always show original price next to discount price when applicable
- Use larger/colored discount price, smaller/grey original price (struck-through)
- Show savings amount AND percentage: "€20 off (-25%)"

### Tax/VAT presentation (EU/NL context)
- Show "incl. BTW" / "incl. VAT" explicitly for consumer markets
- Hide the breakdown unless legally required — users want the total

### Bundle/multi-buy pricing
- "3 for €20 (€7 each — save €1)" beats just "€7 each" because it triggers loss aversion

### Common failures
- Discount-only price without anchor (user can't calibrate value)
- "Was €X" hidden in small text below
- BTW exclusion on consumer-facing PDP (creates checkout surprise — Baymard's #1 abandonment reason: unexpected costs)

---

## Category 4: Variant selectors (color/size)

### Baymard research
- Visual swatches outperform text dropdowns for color (faster selection, lower error)
- Out-of-stock variants should be visible-but-disabled, not hidden
- Selected variant should have clear visual confirmation (border, checkmark, label update)
- "Size guide" should be a non-modal overlay or expandable section, not a new page

### Common failures
- Color dropdown instead of visual swatches
- Hidden out-of-stock options — users repeatedly try unavailable variants
- No indication which size/color is currently selected
- Size guide buried in separate page that loses PDP context

---

## Category 5: Add-to-cart CTA

### Baymard / general best practice
- **Visual prominence:** the add-to-cart button should be visually loudest element above the fold
- **Color:** strong contrast against page background and brand secondary colors
- **Copy:** "Add to cart" / "In winkelwagen" — avoid clever variations that lose clarity. "Get yours" is weaker than "Add to cart"
- **Position:** must be visible above the fold on desktop AND mobile
- **Sticky CTA:** on mobile, sticky bottom-fixed CTA after scroll is standard for high-performing PDPs
- **State feedback:** clear visual confirmation after click (mini-cart slide-in or page redirect)

### Common failures
- Same color as secondary buttons (wishlist, share)
- Below the fold on mobile
- Generic "Buy" instead of "Add to cart" — "Add to cart" implies low commitment, "Buy" implies high
- No sticky CTA on long mobile PDPs

---

## Category 6: Stock & urgency signals

### Honest scarcity (Cialdini)
- "Only 3 left in stock" — honest if true, drives loss aversion
- Stock counters should update in real time, not be static fake numbers
- "X people viewing now" — only if real

### Dark patterns to avoid (and to flag if seen)
- Fake countdown timers that reset on page reload
- Fake "X people viewing" numbers
- "Almost gone" labels permanently on every product

### Brand calibration
- Premium brands: avoid loud urgency entirely; let scarcity be implicit through limited collections
- Value brands: explicit scarcity acceptable
- Mid-market: subtle ("Limited stock") rather than aggressive

---

## Category 7: Reviews

### Baymard / Spiegel Research Center findings
- Products with reviews convert ~270% better than products without (Spiegel)
- Review COUNT matters more than perfect 5-star rating — 4.2-4.5 stars with 100+ reviews outperforms 5.0 stars with 5 reviews (consumers see perfect ratings as suspicious)
- Photo reviews drive significant lift
- Display rating and count above the fold near the title

### Display best practices
- Star rating + numeric average + review count visible above the fold
- Detailed reviews lower on page with sorting (most recent, most helpful, by rating)
- Filter reviews by attribute (size fit, color accuracy)
- Verified buyer badges

### Common failures
- Reviews block only at bottom with no above-the-fold summary
- No filter or sort
- Hiding reviews when count is low (worse than showing 3 honest reviews)

---

## Category 8: Detailed description & specs

### Structure
- **Benefits first, features second.** "Stays cold for 24 hours [benefit] thanks to vacuum double-wall insulation [feature]"
- **Scannable:** bullet points for specs, short paragraphs for narrative
- **Hierarchy:** most important info top, technical specs bottom (or in collapsible tab)
- **Tab/accordion patterns** work well for long content; default to most-relevant tab open

### Specs presentation
- Use structured `product_detail` format: section : attribute : value
- Group logically: dimensions, materials, care, compatibility
- Include unit (metric for EU markets; both metric and imperial for international)

### Common failures
- Wall of unformatted text
- Specs hidden behind extra click
- Marketing fluff before practical info
- No comparison to similar products in line

---

## Category 9: Cross-sell / upsell

### Position and intent
- "Frequently bought together" near add-to-cart: increases AOV
- "You may also like" lower on page: rescues low-intent visitors
- "Complete the look" for fashion: drives bundle conversion

### Friction concerns
- Cross-sell carousel should not push primary product info below the fold
- Don't promote competing products on the PDP — only complements

### Common failures
- Generic "related products" with no contextual relevance
- Cross-sell that distracts from primary add-to-cart
- Bundling that adds friction (forcing user to deselect)

---

## Category 10: FAQ, shipping & returns info

### Anxiety reduction (MECLABS "a" factor)
- Shipping time + cost visible on PDP, not just in checkout
- Free shipping threshold prominent if applicable
- Return policy summary on PDP ("Free returns within 30 days")
- FAQ accessible from PDP without navigation

### Trust signals
- Trusted payment method icons near CTA
- Trustpilot / Google Reviews badge
- NL: Thuiswinkel Waarborg, WebwinkelKeur

### Baymard finding
- 39% of cart abandonment is caused by unexpected costs (shipping, fees) — surface this on the PDP, not in checkout

---

## Category 11: Mobile experience

### Mobile-specific best practices
- **Sticky add-to-cart** on scroll (industry standard for high-performing PDPs)
- **Image gallery:** swipe-able, full-screen tap-to-zoom
- **Variant selectors:** large touch targets (Fitts's Law — minimum 44×44px)
- **Collapsible sections** for description, specs, reviews to keep scroll manageable
- **Price visible** even after scroll (often integrated in sticky CTA)
- **Form fields** (e.g. notify-when-in-stock) optimized for mobile keyboard

### Common failures
- No sticky CTA — user has to scroll all the way back up
- Variant swatches too small for accurate touch
- Long-form description forces excessive scrolling
- Reviews section adds 5+ screens of scroll without collapse

---

## Notes on brand calibration

Always reread the brand snapshot before finalizing recommendations. The same finding category leads to different recommendations depending on brand:

**Example: Urgency signaling**
- Premium brand: do NOT add countdown timers — recommend "limited collection" framing or remove fake urgency
- Mid-market: light urgency acceptable — "Only 5 left in stock"
- Value brand: stronger urgency — countdown timers, stock counters, "X people bought today"

**Example: Imagery**
- Premium: editorial lifestyle, single hero
- Mid-market: 5-7 mixed lifestyle and clinical
- Value: clinical clarity, focus on quantity and angles

Recommendations that don't match the brand snapshot are wrong, even if they would work for a different brand.

---

## Test-readiness check

Before finalizing each finding, verify:
- [ ] Diagnosis cites a specific principle or source
- [ ] Recommendation is concrete (specific copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z" structure
- [ ] Primary metric is named
- [ ] ICE score is justified by the I/C/E breakdown
- [ ] Recommendation matches the brand snapshot

If any box is unchecked, rework the finding before delivering.
