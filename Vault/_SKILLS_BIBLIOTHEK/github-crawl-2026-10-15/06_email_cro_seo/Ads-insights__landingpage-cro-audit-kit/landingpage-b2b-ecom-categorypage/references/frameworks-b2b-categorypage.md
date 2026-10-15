# Frameworks for B2B Ecommerce Category Page Audits

This reference file contains the CRO and B2B-specific frameworks, principles, and applied research used in the B2B category page audit. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

B2B category pages are uniquely prone to fabricated findings because so much is account-state-dependent and JavaScript-rendered:
- Login-gated pricing (only "Log in for pricing" placeholder visible to anonymous)
- Customer-specific tier pricing (only renders after login)
- Bulk-add interfaces (often lazy-loaded or feature-flagged)
- Comparison-list widgets (modal, only visible on click)
- Faceted filters (often JS-rendered, dependent on result set)
- Stock/lead-time states (vary per account, per region)
- Reorder shortcuts (only render for repeat customers)

**For every finding, verify against screenshots before delivering.**

---

## CRITICAL — Account-state awareness

B2B category pages render fundamentally differently for:
- Anonymous visitors (pricing hidden, login CTA, prospect-targeted content)
- Logged-in standard customers (visible pricing, account-specific MOQ, customer-specific tiers)
- Procurement-system sessions (simplified punch-out UX)

**Always identify which account-state the screenshot represents.**

---

## CRITICAL — B2B type-specific calibration

The four B2B types require fundamentally different category-page approaches:

**Transactional B2B ecom:**
- Prices visible per card
- Add-to-cart per card prominent
- Filters technical + practical
- Most similar to B2C category pages

**Quote-driven B2B:**
- "Request quote" per card
- Spec hints prominent on card
- Comparison-list essential
- Filters technical-spec-driven

**Wholesale (trade):**
- Login-gated pricing on cards
- Bulk-add interface essential
- Pack-size hints on card
- Tier-pricing hints visible

**Hybrid:**
- Mixed per product

---

## Core frameworks (apply across the entire audit)

### Baymard Institute B2B category page research
- 57% of B2B sites have severe usability issues on category pages
- Filter UX is the #1 friction area on B2B category pages (worse than B2C)
- B2B specifiers spend 2-3x longer on category pages than B2C browsers
- Bulk-add interfaces yield 15-35% AOV lifts on wholesale categories

### MEDDIC framework on B2B category page
- **Metrics:** category page should signal business outcomes (lead time, MOQ, tier discount potential)
- **Decision criteria:** filters MUST match specifier's decision criteria
- **Decision process:** category page is where specifier shortlists; comparison tools support this
- **Champion enablement:** save-to-list + share-list lets champion advocate internally

### Challenger Sale on B2B category content
Category-level content can teach + tailor:
- Category intro educates ("How to choose hydraulic systems")
- Filter labels in customer language (not internal jargon)
- Featured subcategories tailored to common buyer paths

### April Dunford positioning at category level
Each category should answer:
- What is this category exactly?
- Who is it for?
- What differentiates these products from alternatives?

### MECLABS on B2B category page
- **m (motivation):** specifier search-intent often very high
- **v (value):** clear filtering + specifications + tier hints
- **i (incentive):** tier-pricing signals, MOQ discounts
- **f (friction):** filter complexity, hidden pricing, slow load
- **a (anxiety):** stock reliability, lead time

### Cialdini on B2B category page
- **Authority** — certification badges on relevant cards
- **Social proof** — "Most ordered" / "Top in category" labels
- **Scarcity** — low-stock warnings (when real)
- **Reciprocity** — tier-discount hints

### Nielsen Norman heuristics on B2B category page
- **#1 Visibility** — active filters, sort state, pagination state visible
- **#3 User control** — easy filter clear, easy sort change
- **#5 Error prevention** — empty-result-state handled gracefully
- **#6 Recognition** — card content sufficient to identify product

### Jobs-to-be-Done on B2B category page
B2B visitors on a category page are doing one of:
1. **Specification-driven shortlist** — filter to 3-5 options, compare deeply
2. **Reorder by category** — find previously-ordered SKU within category
3. **Bulk procurement** — order multiple SKUs by category quickly
4. **Capability evaluation** — assess breadth of offering in category
5. **Compliance check** — filter for certified/compliant products

**Important Dutch translation:** never use "huren" for JTBD. Use "kiezen voor", "zoeken om X te selecteren".

---

## Category 1: Above-the-fold category framing & B2B positioning

### April Dunford on B2B category framing
Each category page should answer immediately:
- What is this category?
- Who is it for?
- What's the differentiator?

### WiderFunnel LIFT
Category page value proposition:
- Category name clear
- Number of products signaled
- Filter route obvious
- Category-level differentiator (if applicable)

### Best practices
- Category heading + 1-2 sentence intro
- Product count visible
- Category-level value proposition (only when adds value)
- Featured subcategories or related categories
- Authentic operational imagery (only when adds context, not decoration)

### Common failures
- Category name only, no context
- Generic "Browse our [category]" intro
- Marketing copy that competes with filters for attention
- No product count
- Lifestyle photography on technical B2B category

### B2B type calibration
- Transactional: short intro + immediate filter/products
- Quote-driven: brief category-capability intro
- Wholesale: tier-program hint + login-gated pricing note
- Hybrid: clear distinction between transactional and quote products

---

## Category 2: Filter UX & specification-driven faceting

### Baymard B2B filter research
Filter UX is the #1 friction area on B2B category pages:
- 71% of B2B sites have inadequate filter coverage for category complexity
- Filter labels in industry jargon (vs internal taxonomy) outperform by 18-30%
- Persistent filters across pagination essential
- Multi-select within facet essential (specifiers often select 2-3 values per facet)
- Result-count per facet (e.g., "Stainless steel (47)") signals what's available

### Hick's Law on filter complexity
Each facet is a decision point. Balance:
- Sufficient facets for specifier needs (often 8-15 facets in technical B2B)
- Grouping and hiding less-used facets behind "More filters"
- Active filters visible at all times

### Best practices
- Filter panel left-rail (desktop) / drawer (mobile)
- Most-used facets visible by default
- Secondary facets behind "Show all filters"
- Result-count per facet value
- Active filters visible (with one-click remove)
- "Clear all" prominent
- Range sliders for numerical specifications (dimensions, capacity, weight)
- Search-within-facet for facets with 20+ values

### Common failures
- B2C-style minimal filters on technical B2B category
- Filter labels in internal jargon
- No result-count per facet
- Active filters hidden
- Range inputs without slider (specifier must enter numbers)
- Filter clear hidden
- Facets reset on pagination

### B2B type calibration
- Transactional: practical facets (brand, price, in-stock)
- Quote-driven: spec-heavy facets (capacity, dimensions, materials, compliance)
- Wholesale: pack-size, MOQ, tier facets
- All: industry-standard terminology

---

## Category 3: Sort options & default ordering

### Baymard B2B sort research
B2B sort options must match B2B buyer jobs:
- "Best match" / "Relevance" usually best default
- "Price: low to high" / "high to low" essential for transactional B2B
- "Lead time: shortest first" valuable for urgent-need scenarios
- "MOQ: lowest first" valuable for trial orders
- "Recently added" / "Newest" lower priority than B2C

### Kahneman/Tversky default effect
~70% of users accept the default sort. Choose carefully:
- For specifiers: relevance default
- For repeat customers: "Recently ordered" or "Best-selling" default
- For wholesale: tier-price-low-first

### Best practices
- Sort dropdown prominent
- Default optimized for dominant job
- 4-6 sort options (more = paralysis)
- B2B-specific sort options (lead time, MOQ)
- Sort state visible after page interaction

### Common failures
- B2C-style sort (only price + newest) on B2B
- No "Best match" default
- Missing lead-time sort
- Default optimized for sales, not specifier

---

## Category 4: Product card content & specification hints

### Baymard B2B card research
B2B product cards need different content than B2C:
- SKU/part number visible
- Brief specification hints (3-5 key specs)
- Stock/lead time signal
- Price (or "Log in for pricing")
- Tier-price hint when applicable
- Certification badges when relevant

### April Dunford — proof through specificity
Card content must support specification-driven evaluation:
- Specific numbers ("Capacity: 500L/min" beats "High capacity")
- Material/finish information
- Standards compliance ("ISO 9001 certified", "CE marked")

### Best practices
- Title in customer language
- SKU visible
- Image consistent across cards
- 3-5 key spec hints
- Stock/lead-time signal
- Price (or login prompt)
- Quick-view CTA
- Compare checkbox

### Common failures
- Title only, no specs
- SKU absent (specifier can't shortlist by SKU)
- Image inconsistent (some technical, some lifestyle)
- No stock signal
- Generic "Buy now" without context

---

## Category 5: Product card interaction (quick view, quick add, bulk add)

### Baymard B2B bulk-add research
Bulk-add interfaces are high-leverage for wholesale and repeat-order B2B:
- 15-35% AOV lift when implemented well
- Critical for procurement-driven categories
- Must handle MOQ enforcement gracefully

### Quick-add patterns
- Per-card quantity selector + add-to-cart for transactional
- "Request quote" CTA per card for quote-driven
- Bulk-add textarea ("Paste SKUs and quantities") for power users
- Save-to-list per card for multi-session evaluation

### Best practices
- Quick-add visible without leaving listing
- Quantity selector aware of MOQ
- Bulk-add textarea for power users (especially wholesale)
- "Add multiple to cart" workflow when bulk-add absent
- Save-to-list one-click

### Common failures
- No quick-add (must click into PDP)
- Quick-add ignores MOQ (error after add)
- No bulk-add for wholesale category
- Save-to-list requires multiple clicks
- Quick-view modal that hides critical info

---

## Category 6: Pricing display, tier hints & login-gated patterns

### Baymard B2B pricing on category page
Pricing visibility decisions:
- Visible pricing for anonymous: highest add-to-cart, highest funnel breadth, but loses B2B-specific positioning
- Login-gated pricing: lower add-to-cart, but signals B2B-only positioning, supports customer-specific tiers
- Hybrid (anonymous see list price, logged-in see tier): best of both for many B2B businesses

### Tier-pricing hints on cards
Even when full tier pricing lives on PDP, category cards can hint:
- "Tier pricing available" badge
- "From €4.20 — Save 30% in bulk" microcopy
- "Volume discounts: 50+, 100+, 500+" hint

### Best practices
- Pricing strategy clear and consistent (don't show some prices, hide others on same page)
- Login-gated pricing with clear value framing
- Tier-pricing hints on cards when applicable
- Currency and tax handling explicit ("Prices excl. BTW")

### Common failures
- Inconsistent pricing visibility (some cards show, some hide)
- "Log in for pricing" without value framing
- No tier-pricing hint despite tier program
- Tax-handling ambiguous

### B2B type calibration
- Transactional: visible pricing
- Quote-driven: "Request quote" CTA, no price
- Wholesale: login-gated standard
- Hybrid: per-product logic, consistently applied

---

## Category 7: Pagination, load behavior & "view all"

### Baymard pagination research
B2B pagination preferences:
- Numbered pagination (vs infinite scroll) preferred for specifier workflow
- "Load more" acceptable for shorter result sets
- "View all" valuable when result set under 200 products
- Persistent filters across pages essential

### Nielsen Norman load patterns
- Numbered pagination supports F-pattern and shortlist workflow
- Infinite scroll breaks "where am I?" awareness
- "Load more" preserves position better than pagination

### Best practices
- Numbered pagination for technical B2B
- Configurable products-per-page (24, 48, 96)
- Result count visible ("Showing 1-24 of 247")
- Persistent filters across pagination
- "View all" link when feasible

### Common failures
- Infinite scroll on technical B2B
- No products-per-page setting
- Filters lost on pagination
- No result count

---

## Category 8: Breadcrumbs & cross-category navigation

### Nielsen Norman wayfinding
Breadcrumbs essential for B2B category navigation:
- Show full hierarchy (often deeper than B2C)
- Clickable to parent categories
- Visible above category heading

### Baymard breadcrumb research
- Breadcrumb usage 3-5x higher on B2B vs B2C (specifiers navigate up/down hierarchy frequently)
- Mobile breadcrumbs essential (often condensed)

### Best practices
- Breadcrumb above category heading
- Full hierarchy shown (or smart-collapsed for very deep)
- Clickable links to parents
- Mobile-optimized breadcrumb

### Common failures
- No breadcrumb on deep category
- Breadcrumb truncated invisibly
- Mobile breadcrumb hidden

---

## Category 9: Comparison-list & save-for-later patterns

### Baymard B2B comparison research
Comparison tools high-leverage for specifier workflow:
- 38% of B2B specifiers use comparison tools when available
- Multi-product comparison essential for engineered categories
- Persistent comparison list across categories

### MEDDIC — Decision criteria
Comparison tools serve Decision Criteria evaluation:
- Side-by-side spec comparison
- Highlight differences
- Shareable comparison links

### Best practices
- "Add to compare" checkbox per card
- Persistent comparison tray ("3 products in comparison")
- Comparison view with side-by-side specs
- Save comparison to list / share comparison link
- Maximum 4-6 products in comparison (more = unreadable)

### Common failures
- No comparison feature on technical B2B
- Comparison limited to 2 products
- Comparison list lost on navigation
- Comparison view without spec highlight

---

## Category 10: Out-of-stock, lead-time & inventory signals

### Baymard B2B inventory research
B2B inventory signaling on category page:
- Stock status per card (in stock / low stock / lead time / backorder)
- Specific quantities when relevant ("240 in stock")
- Lead time for special orders
- Don't suppress out-of-stock products from listing (specifier still wants to see)

### MECLABS anxiety axis
Inventory anxiety on category page:
- "Will I find anything in stock?"
- "What's the typical lead time?"
- Filter by "in stock" valuable

### Best practices
- Stock signal per card
- "Filter: in stock only" facet
- Out-of-stock shown with clear "Backorder · 2-3 week lead time" rather than hidden
- Low-stock warnings when real
- Backorder option visible

### Common failures
- No stock signal on cards
- Out-of-stock products hidden (specifier doesn't know they exist)
- Generic "In stock" without quantity or lead time
- Misleading stock badges

---

## Category 11: Mobile experience

### Baymard mobile B2B research
B2B mobile category page:
- Filter UX is the #1 mobile friction
- Card density must support scanning without zoom
- Bulk-add interface mobile-challenging

### Best practices
- Filter drawer with bottom-sheet pattern
- Apply/clear all filters prominent
- 2-column card grid on mobile
- Card content scannable without zoom
- Sticky sort + filter CTAs
- Pagination tap targets adequate

### Common failures
- Desktop filter panel inaccessible on mobile
- Single-column cards (too sparse)
- Filter changes require full page reload
- Tap targets too small
- Bulk-add unusable on mobile

---

## Brand calibration notes

Always recalibrate by brand snapshot AND B2B type:

**Example: Filter strategy**
- Transactional industrial: practical filters (brand, price, in-stock, MOQ)
- Quote-driven engineering: spec-heavy filters (capacity, materials, standards, compliance)
- Wholesale fashion: pack-size, MOQ, tier, season filters
- Hybrid: layered with clear distinction

**Example: Card content**
- Transactional: price + stock + brief specs
- Quote-driven: specs + request-quote + save-to-list
- Wholesale: pack size + login-gated price + bulk-add
- Hybrid: per-product card variant

**Example: Default sort**
- Transactional: best match / relevance
- Quote-driven: relevance / spec-relevance
- Wholesale: tier price low-first
- Repeat-customer logged-in: "Recently ordered first"

Recommendations that don't match brand AND B2B type are wrong.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites specific principle
- [ ] Recommendation concrete
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric B2B-specific (PLP-to-PDP CTR, PLP-to-cart-add, filter engagement, comparison-list usage, downstream PDP conversion)
- [ ] ICE justified by I/C/E breakdown
- [ ] Recommendation matches brand AND B2B type
- [ ] Account-state assumption explicit
- [ ] Dutch output: no "huren" check

If any unchecked, rework before delivering.
