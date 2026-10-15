# Frameworks for B2B Ecommerce Product Page Audits

This reference file contains the CRO and B2B-specific frameworks, principles, and applied research used in the B2B product page audit. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

B2B PDPs are uniquely prone to fabricated findings because so much is account-state-dependent and JavaScript-rendered. Examples:
- Tier-pricing tables (often only render after login)
- Customer-specific pricing (only visible to authenticated B2B accounts)
- MOQ enforcement messages (only render below threshold)
- Quote-request forms (modal, only visible on click)
- Bulk-add interfaces (textarea or table, often lazy-loaded)
- Stock/lead-time states (vary per account, per region)
- Punch-out indicators (only render in procurement-system sessions)

**For every finding, verify the claim against screenshots before delivering.** A finding that says "no tier pricing visible" while the screenshot shows it is worse than no finding.

If a finding cannot be visually verified, either remove it or convert it to a "research first" finding.

---

## CRITICAL — Account-state awareness

B2B pages render fundamentally differently for:
- Anonymous visitors (often hidden pricing, "Log in for pricing" CTA)
- Logged-in standard customers (visible pricing, account-level tier)
- Logged-in premium customers (deeper tier discounts, customer-specific products)
- Procurement-system sessions (punch-out workflow, simplified UX)

**Always identify which account-state the screenshot represents.** If the visitor is anonymous and pricing is hidden, that may be by design — recommend testing login conversion, not "adding pricing". If the visitor is logged in and tier pricing is absent, that's a bigger finding.

When in doubt, flag "Account-state not confirmed — recommendations assume [X]" in the audit.

---

## CRITICAL — B2B type-specific calibration

The four B2B types require fundamentally different recommendations:

**Transactional B2B ecom** (office supplies, MRO, hospitality wholesale):
- Pricing visible by default
- Add-to-cart prominent
- MOQ moderate (often 1-12 units)
- Quick reorder flow critical
- Most similar to B2C in UX patterns

**Quote-driven B2B** (industrial equipment, custom manufacturing):
- "Request quote" replaces add-to-cart
- Price often genuinely cannot be displayed (configuration-dependent)
- Spec sheets, CAD files, datasheets prominent
- Sales rep contact prominent
- Anchoring on price ranges where possible

**Wholesale (trade)** (fashion, CPG, specialty retail wholesale):
- Login-gated pricing for verified resellers
- Tier pricing AGGRESSIVE (MOQ often in dozens/cartons)
- Pack sizes critical (per piece vs per case)
- Bulk-add interface essential
- Account approval workflow

**Hybrid:** mix of above patterns per product category

Recommendations for one type are usually wrong for another. The brand snapshot must include B2B type detection, and findings must respect it.

---

## Core frameworks (apply across the entire audit)

### Baymard Institute B2B research
Baymard has expanded into B2B research over the past 5 years:
- 71% of B2B sites have "severe" usability issues on PDP per Baymard's B2B benchmark
- 48% of B2B buyers prefer self-service ecom over sales-rep contact (rising year-over-year)
- B2B PDP optimization typically yields 8-25% conversion lifts on add-to-cart or quote-request
- Mobile B2B usage is now 35-50% of B2B traffic depending on vertical

### MEDDIC framework (B2B sales qualification, applied to UX)
MEDDIC is a B2B sales framework that maps neatly to PDP UX requirements:
- **Metrics** — what business outcome will the customer measure? PDP should reference ROI, payback period, cost-per-unit
- **Economic buyer** — who signs off? PDP should serve both end-user and procurement
- **Decision criteria** — what specs matter? PDP must surface technical specs prominently
- **Decision process** — how does the customer buy? PDP should support comparison, sample requests, quote workflows
- **Identify pain** — what problem are they solving? PDP value framing should connect to operational pain
- **Champion** — who advocates internally? PDP should give the champion shareable proof (PDF datasheets, comparison sheets)

### Challenger Sale (Dixon & Adamson)
B2B buyers respond to "challenger" positioning — brands that teach, tailor, and take control of the conversation. On PDPs this translates to:
- Specific point-of-view content ("Why we engineer this differently")
- Educational framing rather than feature-listing
- Confident positioning vs commodity alternatives
- Authority signals (expertise, certifications, white papers)

### April Dunford positioning
"Obviously Awesome" framework applied to PDP:
- Category context — what is this product, exactly? (B2B buyers often don't know the category by your brand's term)
- Differentiator clarity — why this product vs alternatives the buyer is considering?
- "For who" specificity — which user types is this designed for?
- Trends and forces — why now? what shifted that makes this relevant?

### Edelman B2B Trust Barometer 2024-2025
B2B trust findings:
- 73% of B2B buyers say trust in the supplier is critical to closing (vs 45% in B2C)
- Specific, verifiable claims outperform vague claims by 4-6x in B2B trust impact (even more than B2C)
- Independent third-party signals (certifications, audited specs, case studies) dominate
- Sales-rep contact remains important but lower priority than self-serve information access

### MECLABS Conversion Sequence Heuristic on B2B PDP
C = 4m + 3v + 2(i−f) − 2a

On B2B PDPs:
- **m (motivation):** often very high (specific buying intent, not browsing)
- **v (value):** must be reinforced via technical depth + cost-per-unit clarity
- **i (incentive):** tier pricing, sample programs, first-order discounts
- **f (friction):** longer fields than B2C, account-creation requirements, MOQ enforcement
- **a (anxiety):** quality, lead-time reliability, payment terms, return policy for opened products

### Cialdini's principles on B2B PDPs
- **Authority** — certifications (ISO, CE, FDA), years operating, customer logos, case studies
- **Social proof** — customer count, "trusted by X+ businesses", industry-specific endorsements
- **Scarcity** — limited stock, end-of-line, factory-direct allocation
- **Reciprocity** — free samples, free shipping above threshold, dedicated account manager

### Jobs-to-be-Done on B2B PDPs
B2B visitors on a PDP are doing one of these jobs:
1. **Repeat reorder verification** — quickest path needed (logged-in flow)
2. **Specification evaluation** — depth of tech docs needed
3. **Price/quote evaluation** — clear pricing or fast quote-response
4. **Stakeholder research** — shareable artifacts (datasheets, PDFs, comparison)
5. **Sample request** — proof-before-buying

A B2B PDP must serve multiple jobs simultaneously, often for different stakeholders viewing the same page.

**Important Dutch translation:** never use "huren" for JTBD framing. Use "kiezen voor", "zoeken om X op te lossen", "inkopers die X willen".

---

## Category 1: Hero, product imagery & technical visualization

### Baymard B2B imagery research
B2B imagery requirements differ from B2C:
- **In-context shots** (product in industrial setting, on production line, installed)
- **Scale references** (size comparison, dimension callouts)
- **Technical diagrams** (cross-section, exploded view, schematic)
- **Material/finish close-ups** for tactile categories
- **360° rotation** for complex products
- **CAD model preview** for engineered components

### Best practices
- 5-10 high-quality images per product
- Mix of glamour shots and technical/installation imagery
- Zoom functionality essential (visitors examine details before specifying)
- Video showing operation or installation
- Downloadable images for stakeholder presentations

### Common failures
- Single image only (catalogue-style)
- Studio shots without scale or context
- No technical drawings on technical products
- Images lower resolution than competitors
- Lifestyle shots only (no installation/operation context)

### B2B type calibration
- Transactional: standard product gallery suffices
- Quote-driven: CAD, schematic, datasheet imagery essential
- Wholesale: pack imagery (per piece, per case, on pallet)

---

## Category 2: Title, SKU, and product identification

### MEDDIC — Decision criteria
B2B buyers identify products by multiple identifiers:
- Manufacturer SKU/part number
- Internal SKU
- Industry-standard identifier (UPC, GTIN, ISBN, MPN)
- Material code, ISO designation, EN/DIN reference

The page must surface all relevant identifiers prominently. Procurement workflows depend on exact part-number matching.

### Best practices
- Product title in customer language (industry-standard terminology)
- Manufacturer name prominent for multi-brand resellers
- SKU/part number directly under title, copy-friendly
- Compatible-equivalent part numbers if applicable ("Replaces: 12345, 67890")
- Country-specific identifiers where required

### Common failures
- Title in internal taxonomy unfamiliar to buyer
- SKU buried in spec table instead of next to title
- No equivalent/alternative part numbers for commodity items
- Brand/manufacturer hidden when buyer searches by brand

---

## Category 3: Price presentation & tier pricing

### Baymard B2B pricing research
B2B pricing UX is fundamentally different from B2C:
- Tier pricing tables increase quantity-per-order by 12-28% when prominent
- "Login for pricing" reduces add-to-cart by 30-50% vs visible pricing (but may be required by business model)
- Cost-per-unit visible at all tiers helps buyers compare
- Price-break announcement near MOQ ("Save 8% above 50 units") drives upsell

### Kahneman/Tversky anchoring
Tier pricing inherently anchors. Visitors comparing 25-unit, 100-unit, and 500-unit prices implicitly evaluate value at each. Best practices:
- Show 3-5 tiers (more creates choice paralysis)
- Visual emphasis on "recommended" middle tier
- Cost-per-unit displayed alongside total ("100 units · €4.20 each · €420")
- "Save X%" badge on higher tiers

### Cialdini reciprocity
Tier discount framed as "gift" outperforms framed as "deal":
- ✅ "Volume discount: 8% above 50 units"
- ❌ "Sale: 8% off all orders 50+"

### Best practices
- Visible price by default if business model allows
- Tier pricing table prominent above-the-fold or directly below price
- Currency-clear (€ vs $ vs £ — international visitors)
- Tax-handling explicit ("Prices excl. VAT" or "Prices excl. BTW")
- For login-gated pricing: clear value prop for logging in

### Common failures
- "Call for pricing" with no anchor range
- Tier pricing buried in spec sheet
- Cost-per-unit missing from tier table
- Tax-handling ambiguous (excl vs incl unclear)
- No clear distinction between list price and net price

### B2B type calibration
- Transactional: visible prices, tier table, clear tax handling
- Quote-driven: "Request quote" CTA with optional indicative range; emphasize quote response speed
- Wholesale: login-gated pricing standard; emphasize "Log in to see your trade pricing"

---

## Category 4: MOQ, pack sizes & unit-of-measure clarity

### Baymard B2B quantity research
MOQ (Minimum Order Quantity) and pack size confusion is one of the top-3 B2B PDP friction points:
- 39% of B2B buyers have abandoned a purchase due to unclear pack-size info
- "Per piece vs per case vs per pallet" ambiguity is the dominant friction
- MOQ enforcement that appears as error after add-to-cart is high-abandonment

### Best practices
- Pack size visible at default qty selector ("Sold per case of 24")
- MOQ communicated proactively ("Min. order 12 units")
- Unit-of-measure conversion visible ("12 units = 1 case · 144 units = 1 pallet")
- Cost displayed at relevant unit ("€48 per case · €2 per piece")
- Pack-size switcher if multiple options ("Buy by: piece / case / pallet")

### Common failures
- MOQ enforced silently with error after add-to-cart
- Pack size invisible until checkout
- Price per piece displayed but order requires case quantity (creates total-confusion)
- "Sold per case of 24" without showing individual piece price
- Pallet-only products without clear pallet quantity info

### B2B type calibration
- Transactional: MOQ usually low (1-12), unit-of-measure usually single
- Quote-driven: less relevant (custom quantities)
- Wholesale: MOQ aggressive, pack-size switching essential

---

## Category 5: Primary CTA (add-to-cart, request quote, request sample)

### Baymard B2B CTA research
B2B PDPs often need multiple CTAs serving different jobs:
- Add to cart (transactional flow)
- Request quote (quote-driven)
- Request sample (proof-before-buy)
- Save to list (long evaluation cycles)
- Talk to specialist (high-consideration)

### Hierarchy matters
Multiple CTAs with equal weight create paralysis. Best pattern:
- Primary CTA: most-likely action for this product/visitor combo
- Secondary CTA: alternative path (quote vs cart, sample vs buy)
- Tertiary: save/share/print

### Fogg Behavior Model on B2B
B2B visitors often have high motivation but variable ability:
- Procurement-bound buyers need PO-friendly checkout (see B2B checkout skill)
- Specifier-bound buyers need spec sheets and datasheets
- End-user buyers need installation/operation guidance

The PDP CTA must match the visitor's job, not just the product.

### Best practices
- Primary CTA visually dominant (color, size, position)
- Secondary CTAs visible but de-emphasized
- "Save to list" for long-cycle decisions
- For quote products: clear expectation-setting ("Response within 24h", "Quote typically delivered within 4 business hours")

### Common failures
- All CTAs visually equal (cart + quote + sample + save = paralysis)
- "Add to cart" on a quote-only product
- "Request quote" buried below the fold
- No save-to-list option for high-consideration products
- CTAs without clear expectation ("Request quote — Response time?")

### B2B type calibration
- Transactional: add-to-cart primary, save-to-list secondary
- Quote-driven: request-quote primary, sample-request secondary
- Wholesale: add-to-cart primary post-login, save-for-rep secondary

---

## Category 6: Stock, lead-time & availability signals

### Baymard B2B inventory research
B2B buyers need different inventory information than B2C:
- **Stock quantity** specific (not just "in stock") — buyers need to know if 500 units are available
- **Lead time** for special orders, custom products, restock
- **Backorder policy** clearly stated
- **Multi-location stock** (warehouse A: 240, warehouse B: 80, MOQ depends on location)
- **Cut-off times** for same-day shipping

### MECLABS anxiety axis
Stock anxiety in B2B is about reliability:
- Will my order arrive when I need it for the project?
- Can I get 500 units in time?
- What's the actual lead time vs marketing copy?

### Best practices
- Specific stock numbers when possible ("240 in stock at NL warehouse")
- Lead time stated explicitly ("Custom orders: 2-3 weeks lead time")
- Backorder option with ETA
- Cut-off time for same-day shipping prominent
- Per-location stock if multi-warehouse

### Common failures
- "In stock" without quantity (useless for 500-unit orders)
- No lead time on custom/special-order products
- Backorder hidden (visitor surprised in checkout)
- Cut-off time hidden until checkout
- Inconsistent stock messaging (in-stock badge with checkout error)

---

## Category 7: Technical specifications & documentation

### April Dunford positioning — proof through specificity
B2B buyers trust specifications, not adjectives. Specifications are the proof layer that backs every positioning claim.

### Baymard B2B specs research
Specifications presentation:
- **Categorized spec tables** (dimensions, performance, materials, electrical, etc.)
- **Downloadable datasheets** in PDF for stakeholder sharing
- **CAD files** (DXF, STEP, STL) for engineered products
- **Comparison-friendly format** (visitors compare specs across 3-5 products)
- **Searchable specs** when 30+ attributes exist

### Best practices
- Spec table prominent (not buried below cross-sell)
- Categorized for scanning
- Downloadable PDF datasheet
- Print-friendly layout
- Standards references (ISO, ASTM, EN, DIN)

### Common failures
- Specs in prose paragraphs instead of scannable table
- No PDF datasheet for buyers who need to share internally
- Inconsistent spec terminology vs industry standard
- Marketing copy in spec area instead of factual data
- CAD/3D files absent for engineered products

---

## Category 8: Compliance, certifications & standards

### Edelman B2B Trust — verifiable signals
B2B buyers operate in regulated environments:
- Construction: CE marking, EN standards
- Food: HACCP, IFS, BRC
- Medical: ISO 13485, FDA, CE-IVD
- Electrical: CE, UL, ETL, EMC compliance
- Environmental: ISO 14001, FSC, Blue Angel

Missing certifications on regulated products is a deal-breaker — buyers cannot specify or procure non-compliant items.

### Cialdini authority
Third-party certifications signal legitimacy without self-claims:
- Logos prominent (CE, ISO, industry-specific)
- Certification numbers and dates
- Links to downloadable certificates
- Compliance documentation in customer-relevant languages

### Best practices
- Certifications visible above-the-fold or in dedicated section
- Certificate downloads available (PDF)
- Year of certification visible
- Compliance documentation in relevant EU languages
- REACH/RoHS statements for chemical/electronic products

### Common failures
- Logos without dates (looks dated or fake)
- Missing required certifications for category
- Certificate downloads broken or absent
- Marketing claims of "certified" without specifying which certification
- Out-of-date certifications (lapsed but still displayed)

---

## Category 9: Cross-sell, accessories, and "frequently ordered with"

### Baymard B2B cross-sell research
B2B cross-sell differs from B2C:
- **Required accessories** (cables, mounting hardware, consumables) — high relevance
- **Compatible products** (same series, same supplier) — moderate relevance
- **Frequently ordered with** (algorithm-driven) — lower relevance than B2C
- **Replacement parts** (for installed equipment) — very high relevance for installed-base

### Iyengar choice overload (less applicable for B2B)
B2B buyers have higher tolerance for choice when categorized clearly:
- 5-8 accessories acceptable when grouped by category
- 15+ unrelated items still creates paralysis
- "Required to operate" vs "compatible" vs "alternative" distinctions critical

### Best practices
- Distinct sections: "Required accessories", "Compatible products", "Alternatives"
- Clear product compatibility (this works with these models)
- Cross-sell respects MOQ and pack sizes
- Replacement-parts section for installed-base products

### Common failures
- Cross-sell mixed (accessories + alternatives + unrelated)
- No clear "you need this to use the product" signaling
- B2C-style "you may also like" with weak relevance
- Cross-sell pricing without tier context

---

## Category 10: Account, login & customer-specific content

### Baymard B2B account research
B2B accounts are central to PDP UX:
- Customer-specific tier pricing
- Saved lists / shopping lists / re-order
- Order history reference ("You bought 240 of these in Sept 2024")
- Approval workflows (some users add to list, others approve)
- Multi-shipping-address per account

### MEDDIC — Champion enablement
The B2B Champion needs tools to advocate internally:
- Shareable lists ("Send this list to Procurement")
- Comparison sheets
- Datasheet downloads with their account branding optional
- Email-this-product functionality

### Best practices
- Clear "Log in for your pricing" or "Log in to add to list" CTA
- Login conversion optimized (short form, social login if applicable)
- Logged-in state shows: customer-specific price, order history, saved lists
- "Your last order: 240 units on 12 Sept 2024" prominently for repeat products
- Multi-user account workflow (approver vs requester)

### Common failures
- No login prompt despite hidden pricing
- "Login for pricing" without value prop (why should I log in?)
- Logged-in state identical to anonymous
- No order history reference on PDP for repeat customers
- Lost list functionality (saved items disappear after session)

### B2B type calibration
- Transactional: account enhances UX but not required
- Quote-driven: account often optional (quotes work pre-account)
- Wholesale: account essential, login-gated pricing standard

---

## Category 11: Mobile experience

### Baymard mobile B2B research
B2B mobile is rising but underserved:
- 35-50% of B2B traffic is now mobile (varies by vertical)
- B2B mobile conversion lags desktop by 40-60%
- Sales-rep-on-site research is common (B2B field sales using mobile)
- Procurement-on-mobile growing

### Best practices
- Sticky CTA (add-to-cart / request-quote) on mobile
- Tap targets minimum 44×44px
- Spec table mobile-readable (not horizontal scroll on small screen)
- Image gallery swipeable
- Quote form mobile-optimized (keyboard types, autofill)
- PDF downloads mobile-friendly

### Common failures
- Desktop spec table forcing horizontal scroll on mobile
- Sticky CTA absent
- Tap targets too small
- Mobile pricing not aligned with desktop (rendering bug)
- PDF datasheet links broken on mobile

---

## Brand calibration notes

Always recalibrate by brand snapshot AND B2B type:

**Example: Pricing display**
- Transactional industrial: visible prices, tier table, clear MOQ
- Quote-driven custom manufacturing: "Request quote — 4-hour response" with no price
- Fashion wholesale: login-gated, "Trade prices available after account approval"
- Hybrid: per-product logic ("Standard products priced, custom products quote")

**Example: Primary CTA**
- Transactional: "Add to cart" prominent
- Quote-driven: "Request quote" with response-time microcopy
- Wholesale anonymous: "Log in for trade pricing" primary, "Apply for trade account" secondary
- Wholesale logged-in: "Add to cart" with tier price shown

**Example: Mobile spec presentation**
- Industrial commodity: condensed spec table with expand-to-full
- Engineered component: CAD preview + downloadable datasheet
- Wholesale fashion: pack-size selector dominant, specs secondary

Recommendations that don't match brand snapshot AND B2B type are wrong.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites a specific principle or source
- [ ] Recommendation is concrete
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric is named (B2B PDP metrics: add-to-cart rate, quote-request rate, sample-request rate, save-to-list rate, downstream order placement)
- [ ] ICE score justified by I/C/E breakdown
- [ ] Recommendation matches brand snapshot AND B2B type
- [ ] Dutch output: no "huren" check
- [ ] Account-state assumptions made explicit

If any box unchecked, rework before delivering.
