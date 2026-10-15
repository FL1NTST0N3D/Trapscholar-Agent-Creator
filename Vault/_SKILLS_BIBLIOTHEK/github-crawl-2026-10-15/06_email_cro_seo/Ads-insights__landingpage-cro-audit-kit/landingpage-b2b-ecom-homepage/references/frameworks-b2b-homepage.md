# Frameworks for B2B Ecommerce Homepage Audits

This reference file contains the CRO and B2B-specific frameworks, principles, and applied research used in the B2B homepage audit. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

B2B homepages are uniquely prone to fabricated findings because so much is account-state-dependent and JavaScript-rendered. Examples:
- Personalized hero (different for anonymous vs logged-in vs approver-role)
- Account-aware navigation (logged-in customers see different menu)
- Trade-program signals (only render for non-logged-in anonymous prospects)
- Customer-specific product carousels (only render after login)
- Reorder shortcuts (only render for repeat customers)
- Punch-out indicators (only render in procurement-system sessions)

**For every finding, verify against screenshots before delivering.** A finding that says "no trade program signal" while the screenshot shows it is worse than no finding.

---

## CRITICAL — Account-state awareness

B2B homepages render fundamentally differently for:
- Anonymous visitors (typically with prospect-focused content)
- Logged-in standard customers (personalized: reorder, saved lists, account-specific pricing)
- Logged-in approvers (approval-queue visibility)
- Procurement-system sessions (simplified punch-out UX)

**Always identify which account-state the screenshot represents.** If the visitor is anonymous, recommend prospect-targeted improvements. If logged-in, recommend personalization improvements. When in doubt, flag "Account-state not confirmed — recommendations assume [X]" in the audit.

---

## CRITICAL — B2B type-specific calibration

The four B2B types require fundamentally different homepage approaches:

**Transactional B2B ecom:**
- Prices visible by default
- Featured products / categories prominent
- Reorder shortcut prominent for logged-in
- Most similar to B2C homepage patterns

**Quote-driven B2B:**
- "Request quote" as primary CTA
- Expertise content prominent (case studies, white papers)
- Sales-team accessibility prominent
- Product showcase secondary to capability showcase

**Wholesale (trade):**
- "Apply for trade account" prominent for anonymous
- Login-gated product/pricing access
- Brand portfolio prominent
- Trade-program benefits framed clearly

**Hybrid:**
- Mixed: prospect path AND customer path
- Often requires segmented hero or dual-CTA structure

Recommendations for one type are usually wrong for another.

---

## Core frameworks (apply across the entire audit)

### Baymard Institute B2B research on homepage
B2B homepage research:
- B2B homepage bounce rates average 38-52% (higher than B2C's 30-45% due to broader visitor diversity)
- Visitor diversity is the central challenge: same homepage must serve prospects evaluating viability AND repeat customers wanting fast reorder
- Account-aware personalization yields 15-30% lifts on logged-in homepage conversion when implemented well

### MEDDIC framework on B2B homepage
- **Metrics:** homepage should reference business outcomes (cost savings, lead-time reliability, ROI)
- **Economic buyer:** homepage serves finance via stability + scale signals
- **Decision criteria:** homepage proves capability via category coverage + certifications
- **Decision process:** homepage routes the visitor to the right next step per stakeholder type
- **Identify pain:** homepage opening signals the operational pain solved
- **Champion enablement:** homepage gives champion shareable proof for internal advocacy

### Challenger Sale (Dixon & Adamson)
B2B homepages that teach + tailor + take control:
- Educational framing of industry problem
- Confident positioning vs commodity alternatives
- Specific point-of-view content

### April Dunford positioning
"Obviously Awesome" framework critical for B2B homepage:
- Category context immediate
- Differentiator clarity in hero
- "For who" specificity (procurement / specifier / installer / reseller)
- Trends and forces — why now?

### Edelman B2B Trust Barometer 2024-2025
B2B trust findings on homepage:
- **73% of B2B buyers say trust in supplier is critical to closing**
- Verifiable claims outperform vague claims by 4-6x
- Trust signals must be above-the-fold for prospect visitors
- Customer logos, certifications, scale signals are top trust-builders

### MECLABS Conversion Sequence Heuristic on B2B homepage
C = 4m + 3v + 2(i−f) − 2a

- **m (motivation):** varies widely — prospect curiosity vs customer urgency
- **v (value):** clear category positioning + differentiator
- **i (incentive):** trade-program benefits, first-order discounts
- **f (friction):** unclear navigation, login-gated content for prospects
- **a (anxiety):** supplier viability, compliance, escalation paths

### WiderFunnel LIFT model on B2B homepage
Six factors:
- **Value proposition** — clear within 5 seconds
- **Clarity** — what to do next obvious
- **Urgency** — less applicable B2B; replaced by "right next step now"
- **Distraction** — multiple CTAs / heavy content reduces conversion
- **Anxiety** — addressed via trust signals
- **Relevance** — different jobs served clearly

### Cialdini's principles on B2B homepage
- **Authority** — certifications, scale signals, industry credentials
- **Social proof** — customer logos, customer count, testimonials
- **Liking** — visible accessibility, leadership visibility
- **Commitment-consistency** — published values
- **Reciprocity** — shared expertise (downloadable resources)
- **Scarcity** — limited capacity, specialized expertise

### Jobs-to-be-Done on B2B homepage
B2B visitors on homepage are doing one of:
1. **Repeat customer reorder** — fastest path to product or saved list
2. **Prospect supplier evaluation** — viability + capability check
3. **Specifier research** — technical depth + downloadable resources
4. **Procurement compliance check** — certifications + escalation paths
5. **Trade-program enrollment** — wholesale / reseller application

A B2B homepage must serve multiple jobs without forcing the wrong path.

**Important Dutch translation:** never use "huren" for JTBD. Use "kiezen voor", "zoeken om X op te lossen", "kopers die X willen".

---

## Category 1: Above-the-fold value proposition & B2B positioning

### April Dunford on B2B hero
The above-the-fold must answer **"What is this company, why should I evaluate it, and what's my next step?"** within 5 seconds.

Bad: "Welcome to [Brand], your trusted partner for business solutions."
Good: "[Brand] supplies [specific category] to [specific industry] across [region]. [Differentiator]."

### Challenger Sale on B2B hero
Teach + tailor:
- Name the industry context immediately
- Position the differentiator relative to alternatives
- Avoid generic "leading provider" language

### WiderFunnel LIFT — value proposition clarity
B2B hero value proposition should:
- Name the product category in customer language
- Identify target customer type
- Communicate differentiator
- Set up clear next step

### Best practices
- Headline names category and target customer
- Subheadline differentiates
- One credibility anchor (years, customer count, scale)
- Primary CTA matched to B2B type (Shop / Request quote / Apply for trade account)
- Authentic operational imagery, not stock

### Common failures
- Generic "leading provider" / "trusted partner" copy
- Category context missing
- No clear next step
- Multiple equal CTAs creating paralysis
- Stock business-people imagery

### B2B type calibration
- Transactional: shop-the-catalog CTA primary
- Quote-driven: request-quote CTA primary
- Wholesale: trade-account-application primary (anonymous) / login (returning)
- Hybrid: segmented hero or dual-CTA with clear distinction

---

## Category 2: Hero imagery & visual context

### Nielsen Norman visual-first on B2B
B2B imagery requirements differ from B2C:
- Authentic operational imagery (warehouse, manufacturing, fulfillment)
- Products in context (installed, in use, in production)
- Team at work (not staged portraits)
- Real customer scenarios when permitted
- Quality of imagery matches brand maturity

### Edelman B2B Trust on imagery
- Authentic operational imagery outperforms glossy corporate stock
- Industry-specific contexts (factories, project sites) outperform generic office shots
- Mismatched imagery (stock + authentic mixed) creates dissonance

### Best practices
- Authentic operational hero
- Imagery matches the B2B category
- Resolution adequate for retina displays
- Video where appropriate (factory tour, customer testimonial)
- Mobile-optimized image variants

### Common failures
- Stock business-people imagery
- Generic warehouse stock photos
- Decorative hero with no content connection
- Heavy hero video that slows page load
- Mobile hero crops badly

---

## Category 3: Navigation, search & account-aware access

### Baymard B2B navigation research
B2B navigation differs from B2C:
- Deeper category hierarchy (technical taxonomies)
- Search dominates over browse for repeat customers (they search SKU)
- Account-aware navigation (logged-in sees different menu options)
- Multi-language and multi-region selectors

### Fitts's Law on B2B navigation
Critical targets must be large and prominent:
- Account/login access (always visible)
- Search bar (prominent, often above fold)
- Primary category routes (mega-menu acceptable for B2B)

### Best practices
- Persistent header with search, account, cart
- Mega-menu for deep categories (B2B-acceptable)
- SKU-aware search (recognize part numbers)
- Account-aware top nav (logged-in sees "My account", "Saved lists", "Approvals")
- Language/region selector visible for international

### Common failures
- Hidden search behind icon (suppresses repeat-customer flow)
- Generic ecom navigation without B2B-specific options
- No SKU search support
- Account menu identical for anonymous and logged-in
- Multi-language selector absent on international site

### B2B type calibration
- Transactional: search + categories prominent
- Quote-driven: "Request quote" prominent in nav
- Wholesale: account/login dominant for anonymous
- Hybrid: dual paths visible

---

## Category 4: Trade/account program signals & login conversion

### Baymard B2B account research
B2B accounts are central:
- "Apply for trade account" CTAs prominent for wholesale anonymous
- "Log in" prominent for repeat customers
- Account-aware personalization on logged-in homepage
- Multi-user account workflow (requester / approver)

### MEDDIC — Decision process
Account creation IS the decision process for wholesale B2B. The homepage must:
- Explain trade-program benefits clearly
- Set expectations for approval timeline
- Show "what you get" (trade pricing, dedicated rep, payment terms)

### Best practices
- For anonymous wholesale homepage: trade-program signals above-the-fold, "Apply for trade account" CTA prominent
- For logged-in homepage: personalized hero (welcome back, reorder suggestions, account-specific content)
- Trade-program benefits visible (tiered pricing, payment terms, dedicated rep)
- Approval timeline transparent ("Trade accounts approved within 2 business days")

### Common failures
- Trade-program hidden in footer
- No value proposition for trade account ("Apply for an account" — why?)
- Generic homepage for logged-in customers (no personalization)
- Approval expectations missing
- Login required for any browsing (suppresses prospect funnel)

### B2B type calibration
- Transactional: light account positioning (account enhances, not required)
- Quote-driven: account less critical pre-purchase
- Wholesale: account positioning dominant
- Hybrid: dual paths

---

## Category 5: Featured categories, products & quick-reorder

### Baymard B2B homepage merchandising
B2B homepage merchandising differs from B2C:
- Featured categories outperform featured products (broader buyer relevance)
- Quick-reorder for logged-in customers high-leverage
- New-arrival positioning less impactful than B2C
- Seasonal merchandising less impactful

### Jobs-to-be-Done on featured content
Different jobs need different featured content:
- Repeat customer: reorder shortcut, saved-list quick access
- Prospect: featured categories spanning capability
- Specifier: featured technical product groups
- Procurement: featured certified product lines

### Best practices
- Featured categories prominent (6-12 categories with clear imagery)
- Quick-reorder section for logged-in customers
- "Browse by industry" / "Browse by application" routing for diverse customer base
- Featured products only if business case is strong (sales-driving promotions)

### Common failures
- Featured products dominant when categories serve better
- No quick-reorder for logged-in repeat customers
- Random product grid without organizing principle
- Featured content identical for anonymous and logged-in

---

## Category 6: Trust signals, scale & credibility

### Edelman B2B Trust Barometer
Trust signals must be visible:
- **Years operating** specific
- **Customer count** verifiable
- **Order/transaction volume** indicated
- **Geographic footprint** explicit
- **Industry tenure** specific
- **Certifications** with verification

### Cialdini authority + social proof
- Specific numbers outperform vague claims
- Third-party signals outperform self-claims
- Industry-specific signals outperform generic

### Best practices
- Trust strip above-the-fold or directly below (years, customers, certifications)
- Specific numbers ("Trusted by 1,800+ businesses across 23 countries")
- Industry-relevant certifications visible
- Geographic operational footprint shown

### Common failures
- "Trusted by businesses worldwide" — unverifiable
- "Decades of experience" — vague
- Certifications hidden in footer
- Trust signals absent from homepage entirely

---

## Category 7: Customer logos, references & social proof

### Cialdini social proof in B2B
- Customer logos recognizable
- Industry diversity signaled
- Named-customer testimonials (with attribution)
- Case-study previews routing deeper

### Spiegel Research Center
Named-photo-attributed testimonials outperform anonymous by 5-7x. B2B effect even stronger.

### Best practices
- Customer logo wall (8-15 recognizable brands)
- Industry-grouped if diverse vertical reach
- 1-2 testimonials with full attribution on homepage
- Case-study CTAs routing to detail pages

### Common failures
- No customer logos
- Stock-looking unrecognizable logos
- Anonymous "Sarah M." testimonials
- Old testimonials (3+ years undated)

### Authenticity restraint
A finding may recommend documenting permission-to-use. A finding may NOT assert displayed logos are unauthorized.

---

## Category 8: Content marketing & educational routes

### Challenger Sale on B2B content
B2B buyers respond to suppliers who teach:
- Educational content (white papers, guides, industry reports)
- Specific industry insights
- Capability content (how-we-do-this)
- Case studies as proof artifacts

### B2B content-led funnel
B2B sales cycles span weeks-to-months. Content keeps the visitor engaged across multi-session journey:
- Email signup for industry insights
- Downloadable resources (gated or ungated based on strategy)
- Webinar/event signup
- Industry-newsletter signup

### Best practices
- "Resources" or "Insights" route prominent in nav and homepage
- 2-4 featured content pieces on homepage
- Mix: educational content, case studies, capability content
- Multi-format (article, video, downloadable)

### Common failures
- No content section on homepage
- Generic blog posts without industry depth
- Content section without clear next step
- All content gated (suppresses prospect engagement)

### B2B type calibration
- Transactional: less content emphasis (product-led)
- Quote-driven: content-led essential
- Wholesale: trade-program content + brand-portfolio content
- Hybrid: layered

---

## Category 9: Sales/contact accessibility & escalation paths

### MECLABS anxiety axis
B2B contact accessibility reduces escalation anxiety:
- Phone number visible (not hidden behind form)
- Account-manager contact for logged-in
- Office hours specified
- Multi-language support indicated

### Cialdini liking via accessibility
Visible accessibility makes the company feel like a partner:
- Named contacts where possible
- Multi-channel (phone, email, chat)
- Response-time commitments

### Best practices
- Phone number in header or hero
- "Contact sales" / "Talk to a specialist" CTA visible
- Office hours specified
- Chat widget for live support (if supported)
- For logged-in: account manager contact visible

### Common failures
- Contact only via form
- No phone number anywhere
- Hours not specified
- Anonymous "info@" emails only

### B2B type calibration
- Transactional: customer-service stack
- Quote-driven: sales-rep contact prominent
- Wholesale: account-manager contact for logged-in
- All: physical signals (office addresses, real numbers)

---

## Category 10: Visual hierarchy, scannability & conversion routing

### Nielsen Norman F-pattern
B2B homepage visitors scan in F-pattern:
- First headline read fully
- Second headline read partially
- Vertical scan down left edge
- Critical information must be in headlines and first sentences

### WiderFunnel LIFT — clarity
Conversion routing on homepage:
- Multiple visitor jobs need clear paths
- Primary CTA for dominant job
- Secondary CTAs for other jobs
- Path to each job clear within 1-2 clicks

### Best practices
- Strong visual hierarchy (hero → trust strip → categories → social proof → content → contact)
- H2 subheadings for each section
- Clear CTAs at each section
- Closing CTA matched to B2B type
- Footer with comprehensive navigation

### Common failures
- Cluttered hero with multiple equal CTAs
- No visual hierarchy
- Sections without clear next step
- Dead-end (no closing CTA)
- Footer-as-only-navigation

---

## Category 11: Mobile experience

### Baymard mobile B2B research
B2B mobile:
- 35-50% of B2B traffic mobile (varies by vertical)
- Field-sales context common (sales rep showing customer on tablet)
- Procurement mobile usage rising
- Approval workflows often mobile-first

### Best practices
- Hero readable without zoom
- Search prominent (often top-priority mobile element)
- Featured categories swipeable
- Account access prominent in mobile menu
- Trust signals adapted for mobile (smaller stat blocks, not full bars)
- Mobile-optimized hero imagery

### Common failures
- Desktop hero ported without optimization
- Search hidden behind icon (kills repeat-customer flow)
- Trust signals not visible above mobile fold
- Featured content stacks awkwardly
- Account menu inaccessible

---

## Brand calibration notes

Always recalibrate by brand snapshot AND B2B type:

**Example: Hero CTA**
- Transactional: "Shop catalog" or "Browse products"
- Quote-driven: "Request a quote" or "Speak to a specialist"
- Wholesale anonymous: "Apply for trade account"
- Wholesale logged-in: "Reorder your favorites"
- Hybrid: dual-CTA with clear distinction

**Example: Trust signals**
- Transactional industrial: scale + reliability metrics
- Quote-driven engineering: expertise + project metrics
- Wholesale fashion: brand portfolio + distribution metrics
- Corporate B2B: scale + financial stability

**Example: Featured content**
- Transactional: featured categories + reorder shortcut
- Quote-driven: case studies + white papers
- Wholesale: brand portfolio + trade-program benefits
- Hybrid: layered for different audiences

Recommendations that don't match brand AND B2B type are wrong.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites specific principle
- [ ] Recommendation concrete
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric B2B-specific (bounce rate, click-through to product-quote-account, login conversion, multi-session return)
- [ ] ICE justified by I/C/E breakdown
- [ ] Recommendation matches brand AND B2B type
- [ ] Dutch output: no "huren" check
- [ ] Account-state assumptions explicit

If any unchecked, rework before delivering.
