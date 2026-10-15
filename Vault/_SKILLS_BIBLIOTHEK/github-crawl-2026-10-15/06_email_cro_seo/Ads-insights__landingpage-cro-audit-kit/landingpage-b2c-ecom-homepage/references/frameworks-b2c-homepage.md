# Frameworks for B2C Ecommerce Homepage Audits

This reference file contains the CRO frameworks, principles, and applied research used in the homepage audit. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

Many of the categories below involve checking whether an element is **present, absent, or insufficient** on the page. Examples:
- Hero sliders and carousels (often JavaScript-rendered)
- Newsletter popups (timing-triggered, may not appear on first load)
- Sticky elements that only appear after scroll
- Personalised product recommendations (vary by session)
- Cookie/consent banners
- Promotional banners with conditional rendering
- Trust badges, review widgets, chat bubbles

**For every finding in these categories, verify the claim against screenshots before delivering.** The single most common failure mode of this audit is claiming an element is missing when it is visually present but invisible in fetched HTML. A finding that says "no newsletter signup" while the page has a delayed-trigger popup is worse than no finding at all — it destroys credibility.

If a finding cannot be visually verified, either:
1. Remove it from the audit, or
2. Convert it to a "research first" finding asking the user to confirm before testing

This rule overrides every other instruction in this file.

---

## CRITICAL — Conditional HTML strings (Shopify, WooCommerce, Magento)

Most ecom platforms ship status strings into the DOM as **conditional placeholders** that JavaScript decides whether to render. The string is always in HTML; the visitor only sees it under specific conditions.

Homepage-specific examples:
- Shopify: `"Sale"`, `"New"`, `"Bestseller"`, promotional banner content, hero-slide content (often a slider that defaults to the first slide visually but contains all slides in HTML)
- WooCommerce: featured-product flags, sale-badges, category-banner content
- Magento: CMS-block content (often editor-friendly placeholders rendered conditionally)

**Implication for the audit:** finding promotional copy or a sale badge in HTML does NOT mean the visitor sees it. Sliders rotate; conditional banners may be active only for logged-in users; personalisation modules vary per session.

**The hard rule:** promotional state, sale activeness, slider position, and personalisation findings rely on screenshots only. Never on HTML strings.

A finding may legitimately say: *"this homepage shows no visible seasonal/campaign anchor — consider adding a hero banner tied to current season or campaign"*.

A finding may NOT say: *"the HTML contains 'summer-sale' banner code but it doesn't appear on the page — likely a bug"*. That finding is almost always wrong; it is template-default behavior or a deactivated campaign block.

---

## Core frameworks (apply across the entire audit)

### WiderFunnel LIFT model
Six factors that influence conversion:
1. **Value proposition** (the foundation — why your brand, why now)
2. **Relevance** (does the page match the visitor's expectation given how they arrived)
3. **Clarity** (is the offer and primary path forward clear)
4. **Anxiety** (what doubts exist — trust, security, return policy)
5. **Distraction** (what pulls attention away from the primary path)
6. **Urgency** (why act now)

LIFT is the dominant organizing framework for homepage audits. Most findings can be placed against one of these six levers.

### Eisenberg buyer modalities
Visitors fall into one of four decision-making types:
1. **Competitive** — wants the best, fast, no fluff. Needs: clear positioning, comparison cues, decisive CTAs
2. **Methodical** — wants details, evidence, structure. Needs: specs, FAQs, structured navigation
3. **Spontaneous** — wants emotion, lifestyle, immediate appeal. Needs: hero imagery, deals, instant gratification
4. **Humanistic** — wants connection, story, values. Needs: brand story, team, mission, testimonials

A well-designed homepage addresses all four. Most homepages favor one or two and lose the others. Use this lens when auditing hero, navigation, and content sequence.

### Nielsen Norman F-pattern and Z-pattern
Eye-tracking research on how people scan webpages:
- **F-pattern** dominates content-heavy or list-heavy pages — readers scan the top horizontally, then a second horizontal line shorter, then down the left edge
- **Z-pattern** appears on visual/sparse pages — eyes go top-left → top-right → diagonal to bottom-left → bottom-right
- Homepages typically blend both: F-pattern in the main content area, Z-pattern in the hero
- Critical implication: the most important message and CTA must land where eyes naturally go

### Cialdini's principles of influence
- **Social proof** — reviews, ratings, "X+ klanten", bestseller badges, press logos
- **Authority** — certifications, expert endorsements, "as seen in" media
- **Liking** — relatable photography, brand voice, founder story
- **Reciprocity** — newsletter signup with welcome discount, free content
- **Scarcity** — limited collections, seasonal availability (use carefully on homepages — easy to overdo)
- **Commitment** — quiz-driven product finders, wishlist functionality

### MECLABS Conversion Sequence Heuristic
C = 4m + 3v + 2(i−f) − 2a
- m = motivation of user (cannot be changed by homepage; user already arrived)
- v = clarity of value proposition (huge lever on homepage)
- i = incentive to take action now
- f = friction in taking action
- a = anxiety (concerns, doubts, distrust)

On homepages, **v (value clarity)** and **a (anxiety reduction)** are the biggest controllable levers. The 5-second test maps directly onto value clarity.

### Fogg Behavior Model (B = MAT)
Behavior happens when Motivation, Ability, and a Trigger meet at the same moment. Apply to homepage:
- **Motivation:** strong value proposition, social proof, brand affinity
- **Ability:** low friction (clear navigation, fast load, intuitive search)
- **Trigger:** prominent CTA, well-timed popup, clear "next step"

### Jobs-to-be-Done
What "job" is the visitor on the homepage to do? Usually one of:
1. Discover (browsing, no specific need)
2. Find specific (search-driven, has a product in mind)
3. Compare (research mode, comparing options)
4. Re-buy (returning customer, wants to repurchase or restock)

Different jobs need different homepage routes. A homepage that only serves "discover" loses re-buyers and search-users.

**Important Dutch translation:** never use "huren" for JTBD framing. Instead: "kiezen voor", "zoeken om X op te lossen", "bezoekers die X willen".

---

## Category 1: Above-the-fold clarity & value proposition

### The 5-second test
Show the homepage for 5 seconds, then ask:
- What does this site sell?
- Who is it for?
- What makes it different?

If a visitor can't answer all three, the value proposition fails. This is the single most important homepage audit question.

### WiderFunnel LIFT value-proposition factor
A strong value proposition contains:
- **Headline** — clear product category or job-to-be-done
- **Sub-headline** — differentiator or proof
- **Primary CTA** — the obvious next step

### Common failures
- Headline is brand-name only ("Brand X") with no category context
- Generic taglines ("Welcome to our store", "Discover quality")
- Multiple competing headlines from slider rotations that contradict each other
- Hero focused on a single product with no broader category positioning

### Brand calibration
- Premium brands: minimal headline, strong imagery, sub-headline as restraint
- Mid-market: explicit category + USP in headline
- Value brands: deal/promotion-driven headline acceptable

---

## Category 2: Hero imagery & messaging

### Eisenberg buyer modalities applied
The hero is the single most-viewed element. Best practice addresses 2-3 modalities, not just one:
- Visual (spontaneous) + headline (competitive) + sub-text or CTA structure (methodical)
- Lifestyle imagery (humanistic) + clear benefit (competitive)

### Hero patterns
- **Single static hero** — most common, best for clarity, easiest to test
- **Slider/carousel** — Baymard research consistently shows carousels underperform single heroes; only ~1% of visitors interact with slides beyond the first
- **Video hero** — high impact when relevant, can hurt load speed
- **Split hero** — two product/category routes side by side; works for retailers with two clear segments

### Common failures
- Multiple competing CTAs in hero (Hick's Law)
- Hero is decorative without functional CTA
- Slider with 5+ slides — Nielsen Norman: 95% of slides beyond #1 are ignored
- Stock photography that doesn't match brand or product

---

## Category 3: Primary navigation & search

### Baymard navigation research
- Main categories should be 5-9 (Miller's 7±2 principle)
- Mega-menus outperform simple dropdowns for sites with >100 SKUs
- "All categories" or "Shop" megamenu hides intent; better: prominent category labels
- Search should be visible in the top bar, not hidden behind an icon, for sites where SKU count >50
- Search-bar prominence increases search usage 2-3x in Baymard's testing

### Search-bar best practices
- Visible input field, not just icon (on desktop; mobile can use icon if space-constrained)
- Placeholder text that hints at search behavior ("Zoek op merk, type, …")
- Autocomplete with product/category suggestions
- Recent searches for returning users

### Common failures
- Hamburger menu on desktop (hides navigation)
- Search behind a click-to-reveal icon on a desk shopping site with 1000+ SKUs
- Navigation that doesn't survive scroll (no sticky top bar)
- Category labels that mirror internal taxonomy instead of customer language

### Brand calibration
- Premium brands: minimal navigation, often hides categories behind a menu icon (acceptable when SKU count is low and brand discovery dominates)
- Mid-market: full visible navigation
- Value brands: even more visible navigation, often with promotional category-tile rows

---

## Category 4: USP-banner / trust strip

### Position and purpose
The thin strip (usually below header or above footer) carrying USPs like:
- "Free shipping above €X"
- "30-day returns"
- "Voor 22:00 besteld, morgen geleverd"
- "Customer rating 9.X/10"

### MECLABS anxiety reduction
This element directly addresses the "a" factor — anxiety. Done well, it raises conversion by reducing doubt early.

### Best practices
- 3-5 USPs maximum (Hick's Law)
- Specific and verifiable: "9.4/10 from 12,000 reviews" beats "Loved by customers"
- Highest-anxiety USPs first (free returns > free shipping for considered purchases)
- Icons reinforce text but don't replace it

### Common failures
- USPs that contradict each other ("Free shipping over €50" + "Free shipping always")
- Auto-true USPs ("Free shipping above €X" when entire homepage shows products below that threshold)
- USPs that don't fit the brand promise (a luxury brand emphasising "lowest price")
- Trust strip below the fold where 50%+ of users never see it

---

## Category 5: Featured products / collections

### Iyengar choice overload research
Showing 6-9 featured products outperforms showing 24+ on homepage. Too many choices reduces decision likelihood.

### Featured-product logic types
- **Bestsellers** — strong social proof signal, Cialdini approved
- **New arrivals** — drives discovery, useful for returning visitors
- **Seasonal/curated** — editorial position, strong for premium brands
- **Personalised** — most effective when done well, requires customer data
- **Algorithmic "recommended for you"** — high variance in quality

### Best practices
- Label the logic ("Bestsellers this month" beats unlabeled grid)
- Show price, name, and 1-2 visual cues (rating, badge, savings)
- Make the CTA per card clear (Quick view, Add to cart, Bekijk)
- Limit to 4-8 cards per row, 1-2 rows on homepage

### Common failures
- Generic "Our products" grid with no editorial position
- Massive product carousels that exceed 12 items
- Featured products that don't match brand snapshot (mid-market generic products on a premium-positioned brand)

---

## Category 6: Social proof & trust signals

### Spiegel Research Center / Cialdini
Sites prominently displaying reviews convert ~270% better than sites without. The effect is strongest on the homepage where the visitor is forming first impressions.

### Trust signal types
- **Aggregate review widget** (Trustpilot, Kiyoh, WebwinkelKeur, Google Reviews)
- **Numbered claims** ("Joined by 12,000+ customers")
- **Press logos** ("Featured in NRC, Volkskrant, …")
- **Certifications** (Thuiswinkel Waarborg, B-corp, environmental)
- **Real customer testimonials with photos** (high-impact, high-effort)
- **Founder photo + brief note** (humanistic modality)

### Best practices
- Above the fold or immediately below — visitor must encounter trust signal in first scroll
- Specific and verifiable beats vague claims
- Combine quantitative (review count) and qualitative (testimonial quote) for layered proof
- For Dutch market: Thuiswinkel Waarborg and Kiyoh carry significant weight

### Common failures
- "9.X/10" badge without context (from what platform? based on how many reviews?)
- Generic stock testimonials with no name or photo
- Trust badges all in footer — never seen by bouncing visitors
- Authority logos that are decorative rather than substantive

---

## Category 7: Brand story / about-snippet

### StoryBrand (Donald Miller) framework
The visitor is the hero, the brand is the guide. A homepage brand snippet should:
- Identify a customer problem
- Position the brand as the guide with a solution
- Show transformation (what life looks like after the purchase)

### When to include
- New or niche brands where positioning isn't established
- Premium brands where craftsmanship/heritage is part of value
- Mission-driven brands (sustainable, local, founder-led)

### When to skip
- Established commodity retailers (visitors already know what they do)
- Pure-utility shops where speed and price dominate

### Best practices
- Keep it short on homepage: 2-3 sentences linking to fuller about page
- Visual element (founder photo, atelier shot, ingredient close-up)
- Connect to product range visually

### Common failures
- Verbose company history dominating homepage real estate
- Generic mission statements ("We believe in quality")
- About snippet on a homepage where visitor only wants to shop

---

## Category 8: Content / category-routes

### Information scent (Nielsen Norman)
Visitors follow visual and verbal "scent" toward their goal. Strong category-routes have clear scent: customer-language labels, recognizable imagery, intuitive grouping.

### Route types
- **Category tiles** — visual grid linking to top-level categories
- **Shop-by-X** — by type, brand, price, occasion (depends on category)
- **Editorial entry points** — "Lookbook", "Style guide", "How to choose"
- **Buyer-journey routes** — "First time shopping?", "Returning customer?"

### Best practices
- Match labels to customer language, not internal taxonomy
- Visual cues per route (product photo, color, icon)
- Hierarchical clarity: don't compete with main navigation
- For wide assortment: enable multiple discovery patterns (by type AND by brand AND by occasion)

### Common failures
- Category tiles that duplicate main navigation without adding info-scent value
- "Browse our collection" generic CTA without category breakdown
- Editorial content placed before commercial routes (premium brand may justify; value brand will not)

---

## Category 9: Email capture / personalisation

### Fogg Behavior Model — trigger timing
Newsletter popups work when: motivation exists (user is engaged), ability exists (popup is low-friction), trigger arrives at the right moment. Wrong moment kills conversion.

### Popup timing best practices
- Not on first 5 seconds (no engagement context yet)
- Trigger after scroll-depth (>30%) or after specific intent action (cart-add abandonment, exit-intent)
- Frequency: capped per-session and per-week
- Mobile: full-screen popups penalize SEO and frustrate users

### Email capture incentive
Cialdini reciprocity in action:
- "10% off first order" — most common, works
- "Inside access to new arrivals" — for premium/lifestyle brands
- "Free guide / lookbook" — for considered-purchase categories

### Personalisation patterns
- Returning-visitor greeting ("Welcome back, [name]") — modest impact, requires login
- Recently-viewed products row — high impact for considered purchases
- Personalised hero — high impact when data quality supports it; high risk when not
- Geo-based currency/language switching — table stakes for international retailers

### Common failures
- Immediate full-screen popup on landing
- Popup with no clear close button (dark pattern, GDPR risk)
- Email signup with no incentive ("Sign up for our newsletter") — converts <1%
- Personalisation that gets it wrong (showing kids' products to a buyer without kids)

---

## Category 10: Visual hierarchy & scanability

### Gestalt principles applied
- **Proximity** — group related elements; separate unrelated ones with whitespace
- **Similarity** — similar elements (CTAs, product cards) should look similar
- **Continuity** — natural reading flow guides the eye toward CTAs
- **Closure** — incomplete visual cues (overflow carousels, "scroll for more" hints) drive engagement

### F-pattern and Z-pattern application on homepage
- Top section follows F-pattern: header, hero with horizontal CTAs, sub-hero promotional row
- Mid-section often F-pattern: section headers, product/category grids scanned in F
- Sliding/visual-heavy sections follow Z-pattern: visitor's eyes diagonal across

### Whitespace and density
- Premium brands: high whitespace, low density, deliberate restraint
- Mid-market: moderate density, breathing room between sections
- Value brands: high density acceptable, deal-driven layouts crowd intentionally

### Common failures
- Too many competing focal points above the fold (3+ buttons, multiple animations)
- Section transitions unclear (no visual break between hero and feature row)
- Inconsistent visual weight between sections of equal importance
- Mobile layout that just stacks desktop without rethinking hierarchy

---

## Category 11: Mobile experience

### Mobile-specific best practices
- **Tap target minimum 44×44px** (Apple HIG / Fitts's Law)
- **Sticky search bar or sticky primary CTA** — accessible regardless of scroll position
- **Single-column hero** with primary CTA visible without scrolling
- **Burger menu acceptable** on mobile (universal pattern); category-tile grid below hero compensates
- **No popups within first 15 seconds** — Google mobile-first penalises intrusive interstitials
- **Image-heavy sections**: ensure fast load, lazy-loading, progressive enhancement

### Baymard mobile commerce research
- Mobile bounce rates are 1.5-2x desktop on average — small mobile UX wins compound dramatically
- Search usage on mobile is 2-3x higher than desktop relatively — search-bar prominence matters more
- Hero CTA on mobile must be visible above the fold; many sites push it below

### Common failures
- Desktop hero compressed to mobile makes text unreadable
- Multiple CTAs stacked vertically without visual hierarchy
- Slow load on first paint (often the hero image is too large)
- Cookie banner blocking the entire mobile viewport
- Navigation hidden behind two clicks (burger → category → sub-category) for primary pages

---

## Notes on brand calibration

Always reread the brand snapshot before finalizing recommendations. The same finding category leads to different recommendations depending on brand:

**Example: Featured products / collections**
- Premium brand: 4-6 curated items, no badges, editorial photography, restraint
- Mid-market: 6-9 items with "Bestseller" / "New" badges, mix of categories
- Value brand: 9-12 items, prominent prices and savings, deal-driven labels

**Example: Email capture**
- Premium brand: subtle bottom-bar signup with "Inside access" framing — no aggressive popup
- Mid-market: timed popup with discount, acceptable after engagement signal
- Value brand: aggressive popup with prominent discount, exit-intent acceptable

Recommendations that don't match the brand snapshot are wrong, even if they would work for a different brand.

---

## Test-readiness check

Before finalizing each finding, verify:
- [ ] Diagnosis cites a specific principle or source
- [ ] Recommendation is concrete (specific copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z" structure
- [ ] Primary metric is named (homepage metrics: bounce rate, scroll-to-click, navigation engagement, click-to-PDP, session conversion)
- [ ] ICE score is justified by the I/C/E breakdown
- [ ] Recommendation matches the brand snapshot
- [ ] Dutch output: no literal jargon translation ("huren" check)

If any box is unchecked, rework the finding before delivering.
