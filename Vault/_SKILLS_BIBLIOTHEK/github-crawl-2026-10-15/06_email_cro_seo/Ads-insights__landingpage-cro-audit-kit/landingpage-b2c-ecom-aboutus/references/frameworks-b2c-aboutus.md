# Frameworks for B2C Ecommerce About Us Page Audits

This reference file contains the CRO and trust frameworks, principles, and applied research used in the about us page audit. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

Many of the categories below involve assessing **visual authenticity, photo quality, layout, and emotional tone** that simply cannot be derived from HTML text. Examples:
- Real team photography vs. stock photos
- Authentic workplace/founder imagery vs. generic business photography
- Genuine customer testimonials with photos vs. text-only quotes that feel fabricated
- White space, typography, and design quality
- Video presence and quality
- Mobile rendering of long-form content

**For every finding in these categories, verify the claim against screenshots before delivering.** The most common failure mode is fabricating findings about visual quality from text analysis. A finding that says "improve photography" without visual evidence is generic; a finding that points to specific photos with specific observations is concrete and credible.

If a finding cannot be visually verified, either:
1. Remove it from the audit, or
2. Convert it to a "research first" finding asking the user to confirm before testing

This rule overrides every other instruction in this file.

---

## CRITICAL — Authenticity claims require restraint

It is tempting to look at corporate-style team photos and label them "stock photos", or to assume testimonials are fabricated when they look polished. **Do not do this.** Many small companies legitimately use professionally-shot team photos that look corporate. Many testimonials are real but appear suspicious because of polished editing.

**The hard rule for authenticity findings:**
- A finding may RECOMMEND that the user verify their photography is authentic and consider alternatives if not
- A finding may RECOMMEND adding visible signals of authenticity (names, dates, locations on testimonials)
- A finding may NOT assert that specific existing photos are stock or that specific testimonials are fabricated

When in doubt, frame as: "Consider verifying [X] and replacing if [Y]" rather than "Your [X] is fake."

This protects the user from acting on false accusations and protects audit credibility.

---

## CRITICAL — Sustainability/ethics is brand-conditional

Category 7 (Sustainability/ethics/impact) is the only one of the 11 that may legitimately be marked "not applicable" without further effort. If a brand:
- Makes no sustainability, ethics, or social-impact claims on this or any other page
- Operates in a product category where impact claims would feel forced (e.g. a Pokémon card retailer, a generic dropshipping shop, a discount commodity seller)
- Has a brand voice fundamentally about other things (heritage, craft, design, performance)

...then **do not invent sustainability recommendations**. Greenwashing recommendations are worse than no recommendation — they push the brand toward inauthentic claims that erode trust rather than building it.

When the brand DOES have sustainability/ethics content, this category becomes important — assess specificity, verifiability, and consistency with the rest of the brand voice.

---

## Core frameworks (apply across the entire audit)

### Nielsen Norman about us research
Nielsen Norman's longitudinal research has consistently identified about us as an underestimated conversion page:
- About us pages receive 1-3% of total site traffic on average
- Visitors who view about us convert at 2-3x the rate of non-viewers (selection effect + trust-building)
- 89% of about us visitors are evaluating trust before committing to a purchase
- Visitors skim about us pages in F-pattern; ~80% scan rather than read

### StoryBrand framework (Donald Miller)
The most actionable framework for about us positioning. Key principle: **the brand is the GUIDE, not the HERO. The customer is the hero.**

Standard about us pages fail by making the brand the hero ("We started in 2012 with a dream to..."). StoryBrand structure:
1. **Character** (customer) wants something
2. **Has a problem** (external, internal, philosophical)
3. **Meets a guide** (the brand) who has empathy and authority
4. **Gives them a plan**
5. **Calls them to action**
6. Result: success / avoided failure

About us pages that follow this structure speak to the customer's situation first, then position the brand as the helper.

### Edelman Trust Barometer
Annual research on trust in businesses. Key findings relevant to about us:
- 2024: 71% of consumers say "I need to be able to trust the brand to buy from it"
- Trust in business has overtaken trust in government and media
- Younger consumers (18-34) weight values-alignment more heavily than older consumers
- "Show, don't tell" — concrete proof outperforms claims by 3-4x in trust impact

### Cialdini's principles on about us pages
- **Liking** — visitors trust people they relate to: founder photos, team faces, personal stories
- **Authority** — credentials, experience years, awards, certifications, press mentions
- **Social proof** — testimonials, customer count, "trusted by X+ customers"
- **Commitment-consistency** — values stated explicitly create accountability and trust
- **Reciprocity** — sharing genuine knowledge or stories before asking for purchase

### MECLABS Conversion Sequence Heuristic — anxiety axis
About us pages do their work primarily on the **anxiety** axis. Visitors arrive with uncertainty — about quality, legitimacy, fit, ethics, support — and the page must reduce that anxiety enough to continue engaging.

### Jobs-to-be-Done on about us
Visitors on about us pages are doing one of these jobs:
1. **Pre-purchase trust verification** — "Should I buy from this company?" (most common)
2. **Values alignment check** — "Are these my kind of people?" (rising importance, especially in younger demographics)
3. **Authority verification** — "Do they actually know what they're doing?" (B2C industries with technical complexity)
4. **Post-purchase reassurance** — "Did I buy from the right place?" (less common but real)
5. **Press/partnership research** — non-buyer audiences (journalists, potential partners)

Each job has different needs. A well-designed about us serves the dominant job (usually #1 or #2) without ignoring the others.

**Important Dutch translation:** never use "huren" for JTBD framing. Instead: "kiezen voor", "zoeken om vertrouwen op te bouwen", "bezoekers die bevestiging zoeken".

---

## Category 1: Above-the-fold positioning & promise

### StoryBrand opening
The above-the-fold of about us must answer one question: **"Why should I keep reading?"**

Bad openings: "Welcome to [Brand], where we believe..."
StoryBrand opening: "[Brand] helps [audience] [achieve outcome] without [common pain]."

### WiderFunnel LIFT relevance factor
Visitors arrive from various entry points (footer link, navigation, search). The above-the-fold must immediately confirm relevance:
- For homepage-referred visitors: about-page-specific framing different from homepage
- For search-referred visitors: clear identification of company name and what they do
- For internal-link-referred visitors: continuation of brand voice

### Best practices
- Headline names the customer or their situation, not the brand
- Subheadline names the brand and what it does
- One sentence (max) of company tagline
- Visual: usually a hero image of team, founders, or workplace (not stock photography)
- Length: total above-the-fold copy under 50 words; image carries weight

### Common failures
- Generic "About [Brand]" headline that wastes prime real estate
- Long company history starting "Founded in [year]" before establishing relevance
- Stock photography that contradicts later authentic team imagery
- Walls of text above the fold — visitors bounce before scrolling
- Marketing-speak headlines that say nothing concrete

### Brand calibration
- Premium brands: editorial opening — single strong image + brand-voice tagline
- Mid-market: customer-focused opening with team or workplace image
- Value brands: clear capability + scale claim (customers served, years operating)

---

## Category 2: Brand story & narrative arc

### StoryBrand narrative structure for about us
Effective brand stories follow narrative arc, not chronological CV:

**Bad chronological:** "In 2015, we started. In 2017, we grew. In 2020, we expanded..."

**Effective narrative arc:**
1. **The problem we saw** — what frustrated us / our customers
2. **The insight that changed things** — what we realized
3. **The solution we built** — what we did differently
4. **The impact today** — what's changed for customers

This frames the brand as a problem-solver for the customer, not a self-congratulatory timeline.

### Jobs-to-be-Done framing
The story should make the customer feel: "These people understand my problem."

A about us story that primarily says "look how clever we are" fails. A story that says "we got into this because we saw [customer problem] and built [solution] differently" succeeds.

### Best practices
- Open with the problem or insight, not the company history
- Concrete details (specific founder names, specific year of insight, specific first product)
- Anti-corporate tone in mid-market and below; controlled formal tone for premium
- Show evolution: where we started → where we are now (without being a CV)
- Length: 200-400 words for the main story; longer is rarely better

### Common failures
- Pure chronological history that buries customer relevance
- Aspirational claims without concrete evidence ("We strive for excellence...")
- Generic founding story that could be any company ("started in a garage...")
- Heroic self-positioning — "We are committed to changing the industry"
- Story is just a longer version of the homepage value proposition

### Brand calibration
- Premium heritage brands: emphasize craft, lineage, expertise — formal tone
- Mid-market modern brands: emphasize insight + customer empathy — informal tone
- Value brands: emphasize scale + capability + transparency — direct tone
- Niche specialty: emphasize passion + depth of category knowledge

---

## Category 3: Founder/team presentation

### Cialdini liking principle
Visitors trust people they can see and relate to. Anonymous companies feel risky; companies with visible humans feel trustworthy. Edelman's research consistently shows founder-led brands outperform anonymous brands on trust metrics in B2C.

### Edelman Trust Pyramid applied
The trust pyramid for B2C ecom about us:
1. **Names + faces** (foundation — without this, anonymous)
2. **Roles + responsibilities** (who does what)
3. **Personal stories or context** (depth)
4. **Direct contact paths** (accessibility — see category 9)

### Best practices for small/founder-led brands
- Founder photos: authentic, warm, professional but not corporate-glossy
- Founder names + role + brief story (2-3 sentences)
- If multiple founders: equal presentation, no hidden hierarchy
- Optional: signature, handwritten note, video greeting

### Best practices for mid-sized brands
- Team grid: 6-12 key people with photos and roles
- Consistent photo treatment (same background, similar framing)
- Departments organized if team is large (Customer Service, Product, Design)
- For very large companies: leadership only, not full headcount

### Best practices for corporate brands
- Leadership team photos with bios
- Less personal, more credential-focused
- Often accompanied by board, advisors, investors as additional authority signals

### Common failures
- "Our team" as headline with no photos, only text
- Stock photos that look professional but feel generic
- Hidden team — only "Our team" as a sentence without showing anyone
- Inconsistent photo styles (some shot in studio, others in conference room, others candid)
- Founder photo prominent but no team mentioned at all (signals dependency on one person)

### Brand calibration
- Solo founder / small team: prominent founder photo + warm context
- 10-30 person company: team grid with mix of leadership and key roles
- Larger: leadership only, more formal
- Premium luxury: often creative director / designer rather than full team
- Niche craft: artisans at work, hands shown, process visible

### Mobile specifics
- Team grids must adapt — 4-column desktop → 2-column mobile minimum
- Photos must remain large enough to read faces (avoid 80×80px team grids on mobile)
- Bio expansion via tap (not hover) — hover doesn't exist on mobile

---

## Category 4: Values & mission statement

### Edelman Trust Barometer findings
Values claims are increasingly important to B2C consumers, but **concrete values beat vague values by 3-4x in trust impact**.

Bad values statement: "We believe in quality, integrity, and innovation."
(Says nothing; could be any company.)

Concrete values statement: "We work only with OEKO-TEX certified cotton. Our manufacturers in Portugal pay 30% above the legal minimum wage. We publish our supply chain twice a year."
(Specific, verifiable, accountable.)

### Cialdini commitment-consistency
Stating values creates internal pressure for the brand to live up to them. Visitors recognize this and trust commitment-bound claims more than aspirational claims.

### Best practices
- 3-5 core values maximum (more dilutes signal)
- Each value followed by concrete evidence — what the brand actually does
- Avoid corporate buzzwords ("synergy", "innovation", "excellence", "passion")
- Use verbs not nouns where possible ("We pay above minimum" vs "Fair compensation")
- Reference category 7 (sustainability) only if brand has genuine claims there

### Common failures
- Aspirational corporate values list with no evidence
- "Mission" and "vision" sections that read like consulting templates
- Values that contradict the brand's actual visible behavior (e.g. "sustainability" with no concrete environmental claims)
- Values that nobody could disagree with ("quality", "service") — meaning they're not actually values

### Brand calibration
- Heritage brands: craft, lineage, expertise as values
- Modern brands: transparency, customer-first, specific commitments
- Niche brands: deep category knowledge, passion, community
- Value brands: scale, efficiency, accessibility, transparency about price

---

## Category 5: Proof & credibility signals

### Cialdini authority + social proof stacked
The strongest proof on about us pages comes from independent verification:
- **Customer count** — "Trusted by 50,000+ customers since 2015"
- **Years in business** — "Specialists since 1987"
- **Awards and certifications** — third-party recognition
- **Press mentions** — "As featured in [Publication]"
- **Industry partnerships** — credible brand partners
- **Certifications** — ISO, B-Corp, fair trade, etc.

### Spiegel Research Center principle
Verifiable proof signals (with specific numbers, dates, sources) outperform vague claims by 3-5x in conversion impact.

### Best practices
- Specific numbers ("12,847 customers" beats "thousands of customers")
- Dated claims ("Since 2015" beats "for years")
- Source-attributed claims ("featured in The Guardian" beats "press mentions")
- Logo strip of recognizable press/partner brands
- Awards displayed with year and category

### NL-specific proof signals
- Thuiswinkel Waarborg
- WebwinkelKeur / Kiyoh rating with link to public page
- KvK registration (visible)
- BTW number visible (signals legitimate business)
- Lokaal verankerd: showroom locatie, lokaal team, "uit [stad]"

### Common failures
- "Thousands of happy customers" — unverifiable, suspicious
- Awards displayed without year (looks old or made up)
- Generic press logos without explaining what was covered
- Customer count rounded suspiciously ("over 100,000+") suggesting estimate not data
- No proof signals at all (most common failure on small brand about us)

### Brand calibration
- Premium heritage: awards, craft certifications, lineage proof
- Mid-market modern: customer count, press mentions, partner logos
- Value brands: scale claims (millions served, orders shipped), efficiency proof
- Niche specialty: deep category authority, industry recognition

---

## Category 6: Visual storytelling

### Nielsen Norman visual-first research
On about us pages, photos communicate trust faster and more deeply than text:
- Authentic team photo: 2 seconds to establish "real company"
- Same message in text: 30+ seconds to read, less emotional impact
- Photo-text combinations outperform either alone

### Edelman Trust photo findings
- Authentic, slightly imperfect photos outperform glossy corporate photography in trust metrics
- Workplace candid photos outperform staged team grids
- Founder portraits with eye contact outperform action shots
- Mobile-quality photos can hurt premium brands; corporate-quality photos can hurt approachable brands — match to brand voice

### Best practices
- Mix of photo types: portraits, workplace, product-in-context, customer-facing moments
- Consistent visual treatment (same color grading, similar mood)
- Resolution high enough for retina displays (2x source images minimum)
- Avoid stock photography — even good stock looks generic and dilutes authenticity
- Video where appropriate: founder greeting, workshop tour, process showcase

### Common failures
- All stock photography (genericism kills trust)
- Mixed authentic and stock photography in same page (creates dissonance)
- Low-resolution photos that signal cheap operation
- Single photo dominating with no visual depth
- Decorative photos that don't tell story (pretty but content-empty)
- Inconsistent photo treatment (some bright, some moody, some grainy)

### Mobile specifics
- Hero photos must scale well — wide desktop crops often fail on mobile portrait
- Team grids must not become illegible at mobile sizes
- Video must have mobile-friendly controls and not autoplay with sound

### Brand calibration
- Premium brands: editorial photography, controlled color palette, generous white space
- Mid-market: authentic mix of portraits, workplace, customer moments
- Value brands: practical photography showing scale, efficiency, real operations
- Niche craft: hands-at-work, process shots, materials, detail close-ups

---

## Category 7: Sustainability / ethics / impact (where applicable)

**Brand-conditional category. If brand makes no sustainability claims AND product category is not impact-driven, mark as "not applicable" in category sweep. Do NOT invent recommendations.**

### Edelman Trust Barometer 2024-2025 — sustainability findings
- 78% of consumers say they want to buy from brands that align with their values
- BUT trust in sustainability claims has fallen sharply (greenwashing fatigue)
- Specific, verifiable claims outperform general environmental statements by 4-5x
- Third-party certifications outperform self-claims by 2-3x

### Cialdini commitment-consistency on sustainability
Public commitments to sustainability create accountability — and visitors recognize this. Vague commitments ("we care about the environment") create no accountability and read as marketing.

### Best practices (when applicable)
- Specific, verifiable claims ("We've eliminated 4.2 tons of plastic packaging since 2022")
- Third-party certifications visible (B-Corp, OEKO-TEX, FSC, etc.)
- Annual impact reports linked
- Honest about limits ("We're not perfect — here's where we're working")
- Concrete supply chain transparency

### Common failures
- Generic "We care about the environment" statements
- Sustainability section that contradicts product category (fast fashion claiming sustainability)
- Stock photography of forests/leaves without substantive claims
- Vague commitments with no measurement or timeline
- Certifications displayed without explanation of what they cover

### When NOT to recommend sustainability content
- Brand makes no claims and product category is impact-neutral
- Brand voice is fundamentally about other things (heritage, design, performance)
- Adding sustainability would feel forced and erode authenticity

---

## Category 8: Customer voice & testimonials

### Distinction: testimonials vs reviews
- **Review:** customer rates a specific product (4 stars, "Great quality")
- **Testimonial:** customer tells the story of their experience with the brand ("I was struggling with X, then I found [Brand]...")

About us pages benefit from testimonials more than reviews. Reviews belong on PDPs and category pages.

### Cialdini social proof on about us
Testimonials work hardest when:
- Customer is named and identifiable (full name + photo + optionally location)
- The story has a narrative arc (problem → discovery → resolution)
- Specific details ground the claim in reality (specific products, specific outcomes)
- Customer profile matches the target audience the visitor identifies with

### Spiegel Research Center finding
Specific, named, photo-attributed testimonials outperform anonymous quotes by 5-7x in trust and conversion impact.

### Best practices
- 3-5 high-quality testimonials beats 15 generic quotes
- Customer photo + name + role/context + story
- Video testimonials where possible (highest trust impact but production cost)
- Diverse customer profiles representing different jobs-to-be-done
- Recent testimonials (dated within 2 years) outperform old/undated

### Common failures
- Anonymous "Sarah M." quotes without context
- Stock photo "customers" — visually identifiable and trust-damaging
- Generic quotes that could be about any brand ("Great service!", "Love the products!")
- Testimonials all from the same customer profile (lack of representation)
- Testimonial wall that becomes scroll fatigue

### Brand calibration
- Premium brands: refined, narrative-driven testimonials, often from notable customers
- Mid-market: diverse customer mix with photos and contexts
- Value brands: high-volume testimonial walls with star ratings
- Niche specialty: deep technical testimonials from category experts

---

## Category 9: Contact & approachability

### MECLABS anxiety axis on contact
The presence of accessible contact channels reduces anxiety substantially. Visitors interpret "easy to contact" as "easy to resolve problems" — a critical pre-purchase signal.

### Cialdini liking principle
Approachability signals (real phone number, real address, named human contact) make the brand feel like real people rather than a faceless operation.

### Best practices
- Visible phone number (not behind 3 clicks)
- Email address that's responded-to (or honest mention of response time)
- Physical address if applicable (showroom, office, warehouse)
- Customer service hours
- Live chat or messenger access where applicable
- For NL: KvK and BTW visible as business legitimacy signals
- Map embed if there's a physical location to visit

### Common failures
- Contact only via web form (creates anxiety about whether it gets through)
- "Contact us" link without showing channels (forces extra click)
- No phone number anywhere (signals unwillingness to talk)
- Hours not mentioned (signals "we'll get to it when we get to it")
- Anonymous "info@" email instead of named contact

### Brand calibration
- Premium brands: personal customer service contact, often named individuals
- Mid-market: standard customer service contact stack
- Value brands: efficient self-service first, contact as fallback
- Local/specialty: emphasis on physical location, visit, in-person service

---

## Category 10: Cross-links to conversion paths

### WiderFunnel LIFT framework — clarity factor
The about us page must not be a dead-end. Once trust is built, visitors need a clear next step. Without clear cross-links, visitors who finished reading bounce or navigate to homepage instead of continuing the journey.

### Jobs-to-be-Done — the next job
After trust-verification, the visitor's next job is usually one of:
- Browse the product range
- Look at a specific category they were considering
- Read more depth (FAQ, shipping, returns)
- Sign up for newsletter or save for later

### Fogg Behavior Model (B = MAT) — trigger placement
The about us page is rich in motivation and ability (trust is high after reading). The missing element is often the trigger — a clear, well-placed CTA. Effective triggers:
- "Bekijk onze collectie" at end of story
- "Onze meest geliefde producten" with 3-4 product cards
- "Wat klanten kopen na het lezen" (curated based on referrer)

### Best practices
- 1-2 clear CTAs near the end of the page
- Subtle product highlights mid-page (especially if page is long)
- Newsletter signup AFTER trust is built (not before)
- Optional: "Vind een product voor jouw situatie" (recommender quiz) for complex product categories
- Link to FAQ, shipping, returns at the page bottom (anxiety-resolving secondary paths)

### Common failures
- Dead-end at page bottom (no CTA, no cross-links)
- Aggressive CTAs that feel like sales pitches after a trust-building story
- Newsletter popup before visitor has finished reading
- Generic "Shop now" without context
- Too many CTAs creating choice paralysis

### Brand calibration
- Premium brands: subtle, single CTA aligned with brand voice
- Mid-market: 2-3 path options (collection / FAQ / contact)
- Value brands: aggressive cross-link stack with promotional emphasis

---

## Category 11: Visual hierarchy & scanability

### Nielsen Norman F-pattern eye-tracking
~80% of about us visitors scan rather than read. F-pattern findings:
- Horizontal sweep across top (headline area)
- Second shorter sweep (subhead and opening paragraph)
- Vertical scan down the left edge

Implication: critical information must be in the headlines, subheads, and first sentences of each section. Walls of text without scanning aids lose readers.

### Cognitive load research
Long-form content (about us is often 600-1500 words) requires visual rhythm:
- Section breaks every 100-200 words
- Subheadings that summarize the section
- Image/video breaks between text sections
- Pull quotes to highlight key claims
- White space between sections

### Best practices
- H2 subheadings for each major section
- Short paragraphs (3-5 sentences max)
- Image or visual break every 150-300 words
- Numbered or bulleted lists for values, principles, milestones
- Pull quotes for the strongest single sentences
- Consistent typography hierarchy (H1 once, H2 for sections, H3 for sub-points)

### Common failures
- Walls of unbroken text
- Tiny body font on long-form content
- No subheadings within long sections
- Inconsistent typography (some sections styled, others plain)
- Multi-column body text that breaks F-pattern reading

### Mobile specifics
- Mobile portrait orientation makes long content feel longer — shorter paragraphs essential
- Image-to-text ratio must increase on mobile (more visual breaks needed)
- Subheadings become navigation anchors on long mobile pages
- Avoid multi-column layouts entirely on mobile

---

## Notes on brand calibration

Always reread the brand snapshot before finalizing recommendations. The same finding category leads to different recommendations depending on brand, company size, and values footprint:

**Example: Founder/team presentation**
- Solo founder craft brand: prominent founder photo + handwritten note feel
- 12-person mid-market: team grid with consistent photography
- 200-person mid-cap: leadership only, more formal
- Luxury heritage: creative director or designer-as-personality, not team

**Example: Values & mission**
- Sustainability-led brand: detailed concrete claims with certifications
- Premium heritage: craft, lineage, expertise as the values
- Discount value brand: efficiency, accessibility, transparency about price

**Example: Visual storytelling**
- Editorial premium: cinematic photography with controlled palette
- Approachable mid-market: candid workplace and customer moments
- Niche specialty: hands-at-work, materials, process detail
- Value brand: scale and operations shots

Recommendations that don't match the brand snapshot are wrong, even if they would work for a different brand.

---

## Notes on confidence calibration for about us

About us has a smaller public A/B-test base than PDP or cart. Calibrate ICE Confidence scores accordingly:

- **Confidence 8-9:** when recommendation is directly supported by Baymard, Nielsen Norman, or Cialdini with explicit about-us evidence (rare)
- **Confidence 6-7:** when recommendation follows sound trust-building principles with strong but indirect evidence
- **Confidence 4-5:** when recommendation is principle-grounded but lacks direct test evidence
- **Confidence 2-3:** when recommendation requires research first

This is honest, not weak. Faking high confidence on under-tested page types damages audit credibility.

---

## Test-readiness check

Before finalizing each finding, verify:
- [ ] Diagnosis cites a specific principle or source
- [ ] Recommendation is concrete (specific copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z" structure
- [ ] Primary metric is named (about us metrics: about-us exit rate, click-through to category/product, time on page, multi-session conversion)
- [ ] ICE score is justified by the I/C/E breakdown
- [ ] Recommendation matches the brand snapshot (team size, premium/value, values footprint)
- [ ] Dutch output: no literal jargon translation ("huren" check)
- [ ] Sustainability recommendation only if brand has genuine claims

If any box is unchecked, rework the finding before delivering.
