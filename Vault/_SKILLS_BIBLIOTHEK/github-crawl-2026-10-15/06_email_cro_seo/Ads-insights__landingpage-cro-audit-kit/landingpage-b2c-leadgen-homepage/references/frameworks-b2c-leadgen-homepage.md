# Frameworks for B2C Leadgen Homepage Audits

This reference file contains the CRO and homepage-specific frameworks, principles, and applied research. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

B2C leadgen homepages are uniquely prone to fabricated findings because so much is JavaScript-rendered:
- Hero carousels (which slide is current visitor seeing?)
- Service-card grids (often dynamic or conditionally rendered)
- Google review widgets, Klantenvertellen badges, Trustpilot embeds
- Form builders (Gravity Forms, Formidable, Typeform, HubSpot, custom)
- Sticky CTAs, exit-intent popups, chat widgets
- WhatsApp click-to-chat buttons
- "We zijn nu open"-status indicators (real-time)
- Multi-vestiging zoekers / store locators
- Location-based conditional content
- A/B-test variants from third-party tools (Optimizely, VWO, native split-test)

**For every finding, verify against screenshots before delivering.**

---

## CRITICAL — Multi-purpose entry-point logic

Homepages are FUNDAMENTALLY different from single-purpose pages. Recommendations from servicepage, dedicated LP, or contactpage may NOT apply:

**Do NOT automatically recommend on homepages:**
- "Single primary CTA" — multi-CTA is CORRECT on homepages serving multiple visitor-jobs
- "Hide hoofdnavigatie" — navigation IS the routing on multi-service homepages
- "Remove secondary paths" — secondary paths serve different visitor-jobs
- "Add aggressive scarcity/urgency" — wrong for first-touch context (creates anxiety)
- "Lead-magnet propositie" — wrong page type, that belongs on dedicated LPs

**DO recommend (when appropriate):**
- Multi-path CTA strategy matched to visitor-jobs (offerte / phone / WhatsApp / service-routing / boeking)
- Clear service-routing (cards, grid, or navigation)
- Trust + clarity for first-time visitors
- Reviews as conviction-builder (not just reinforcement)
- Brand-positionering work (this is the first-touch moment)

The multi-purpose rule trumps single-CTA dogma on this page-type.

---

## CRITICAL — First-time-visitor context

Many homepage visitors are NEW — they don't know the brand yet. Treatment differs from contactpage (where visitor has chosen) or dedicated LP (where visitor came from campaign):

- Trust signals heavier than on contactpage (visitor is evaluating)
- Brand-positionering critical (5-second clarity test)
- Reviews carry full weight (Spiegel 270% lift applies fully here)
- Local relevance signals important (where are they, what do they do, who is their audience)
- Service explanation needed (not just service names — what does this brand do for me?)

This context drives ICE-Impact calibration: reviews-prominence and brand-positionering are typically HIGHER impact on homepage than on contactpage.

---

## CRITICAL — Business-type calibration

Recommendations vary heavily by business-type:

**Lokaal fysiek bedrijf** (kapsalon, restaurant, winkel, sportschool, garage, kliniek):
- Adres + openingstijden + visit-conversion prominent
- Phone-CTA dominant
- Lokale signalen (Google Business, lokale reviews)
- Multi-vestiging: zoeker prominent
- "We zijn nu open"-status if walk-in/last-minute is typical

**Lokale service-provider** (tandarts, makelaar, fysio, advocaat, fotograaf, klusbedrijf):
- Service-routing dominant (multiple diensten, clear paths)
- Reviews kritiek (first-time visitor evaluatie)
- Form + phone gelijkwaardig
- Vestigingen tellen
- Expertise/team-leden zichtbaar

**Online-only service-provider** (online consultants, virtuele services):
- Adres minder relevant (alleen voor trust)
- Service-routing + form dominant
- Trust-signals heavy (geen fysieke locatie als trust-anker)
- Geen kaart of map
- Vaak: webinar / download / consultation als entry

**Multi-vestiging organisatie** (kapsalon-keten, tandartsketens, restaurant-keten):
- Vestigingen-zoeker prominent
- Dichtstbijzijnde vestiging-detectie waardevol
- Per-vestiging variatie zichtbaar
- Service-routing + locatie-routing parallel

**Hybrid leadgen + content** (veel B2C service-businesses):
- SEO-content secundair aan leadgen-routing
- Blog-posts gedoseerd, niet dominant op homepage
- Educatie-content als trust-builder, niet als hoofdfunctie

---

## Core frameworks (apply across the entire audit)

### Nielsen Norman homepage UX research
The authority on homepage-design heuristics:
- Heuristic #1 (visibility of system status) — what is this brand, what do they offer, where are they
- Heuristic #2 (match real world) — service-names in consumer language, not jargon
- Heuristic #6 (recognition over recall) — show all services, don't make visitor remember
- 5-second clarity test — within 5 seconds visitor knows what brand does, for whom, and how to proceed

### Marketing Sherpa homepage benchmarks
- Average B2C leadgen homepage conversion: 8-12% (varies by industry)
- Top-performing homepages (90th percentile): 15-22%
- Homepage bounce rate average 50-60%; top-performing 35-45%
- Mobile bounce rate typically 5-10pp higher than desktop
- Reviews on homepage lift conversion 2-3x vs no-reviews homepages

### ConversionXL homepage CRO patterns
- Clear value proposition above-the-fold lifts conversion 10-30%
- Service-card grids with icons + descriptions outperform text-only menus
- Reviews-prominence in hero zone lifts conversion 15-30% on first-time visits
- Multi-channel contact options on homepage outperform single-CTA dogma for service-businesses

### MECLABS Conversion Sequence Heuristic on homepages
C = 4m + 3v + 2(i−f) − 2a

On B2C leadgen homepages:
- **m (motivation):** variable (organic search high, direct visit medium, social ad lower)
- **v (value):** brand positionering + service value
- **i (incentive):** clear paths to value (service-routing, contact options)
- **f (friction):** unclear positionering, hidden services, complex navigation
- **a (anxiety):** unknown brand, no proof, missing contact info, generic content

### Cialdini's principles on homepages
- **Authority** — certifications, years operating, named expertise, awards
- **Social proof** — reviews, customer count, named testimonials, case studies — heavy weight on first-touch
- **Liking** — warm tone, founder photo, local context if applicable
- **Reciprocity** — free consultation, free quote, free info-blog
- **Scarcity** — limited slots ("only 3 spots this month" — only if real)

### Fogg Behavior Model (B = MAT) on homepages
Homepages need to:
- Build MOTIVATION through brand-positionering and proof
- Provide ABILITY through clear navigation and service-routing
- Place TRIGGERS at strategic points (hero CTA, after social proof, in service-cards)

### Nielsen Norman heuristics applied to homepages
- **#1 Visibility of system status** — brand-positioning visible, services visible, contact visible
- **#2 Match real world** — consumer language, not industry jargon
- **#3 User control and freedom** — multi-path navigation, no forced single-route
- **#5 Error prevention** — clear service-card scoping (don't make visitor click wrong service)
- **#6 Recognition over recall** — all services visible, not hidden in menus
- **#8 Aesthetic and minimal design** — but balance against need for content depth

### Jobs-to-be-Done on B2C leadgen homepages
B2C consumers on a homepage are doing ONE of:
1. **Brand-evaluation** — "Wat doet dit bedrijf, en is dit voor mij?" (first-time visitor)
2. **Service-finding** — "Ik zoek dienst X, waar staat dat?" (returning visitor with intent)
3. **Trust-verification** — "Is dit bedrijf legit? Wie zijn ze?" (anxiety-driven)
4. **Contact-seeking** — "Hoe bereik ik ze?" (high-intent visitor, often shortcut to contactpage)
5. **Pre-research** — "Save voor later, vergelijk met alternatieven"

Each job needs different page support. A high-converting homepage serves multiple jobs without forcing one path.

**Important Dutch translation:** never use "huren" for JTBD framing. Use "kiezen voor", "zoeken om X op te lossen", "consumenten die X willen".

---

## Category 1: Above-the-fold value proposition & brand-positionering

### April Dunford positioning on B2C leadgen homepages
The hero must answer: **"Wat doet dit bedrijf, voor wie, en wat is mijn volgende stap?"** within 5 seconds.

Bad: "Welkom bij [Brand], uw partner voor mooie momenten"
Good: "Bruidsfotografie in Utrecht — natuurlijk, ongedwongen, op één werkdag geleverd. Bekijk diensten of vraag offerte aan."

### WiderFunnel LIFT — value proposition factor
Homepage hero must communicate:
- WAT (services/specialisatie)
- VOOR WIE (target consumer)
- DIFFERENTIATOR (why this brand)
- WAT NU (clear next step — service-page, contact, of beide)

### MECLABS clarity as first lever
On homepages, clarity-as-conversion-driver is amplified by first-time-visitor context. Vague hero = bounce within 5-8 seconds.

### Best practices
- Headline names what the brand does in consumer language
- Sub-headline differentiates (specialisatie, geografie, doelgroep, approach)
- One credibility anchor visible (years, customer count, rating, specialty)
- Multi-path CTA visible (form, phone, service-routing)
- Authentic, brand-relevant imagery

### Common failures
- Generic "Uw partner voor..." copy
- Brand-name only as headline (brand-first thinking)
- No credibility anchor in hero
- Stock business-people imagery
- Multi-CTA chaos (4+ equally weighted)

### Business-type calibration
- Lokaal fysiek: services + adres + openingstijden + phone hero
- Lokale service-provider: services + form-CTA + reviews-snippet hero
- Online-only: services + form-CTA + trust-signals hero
- Multi-vestiging: services + vestigingen-zoeker hero

---

## Category 2: Hero imagery / video (brand-establishment)

### Nielsen Norman visual-first
On homepages, visual sets the emotional tone before copy is read. First-time visitor processes brand-feel through imagery:
- Premium service → premium photography
- Warm service → warm imagery (people, faces)
- Technical service → clean, professional imagery
- Lokaal bedrijf → lokale context zichtbaar

### Marketing Sherpa imagery research
- Homepages with authentic imagery convert 2-3x better than stock imagery
- Hero video on homepages lifts engagement 30-60% (varies by execution)
- Video <30s with autoplay-muted-loop is high-performing
- Founder/team photo when warmth is brand-relevant

### Authentic-vs-stock imagery impact
- Stock imagery on a brand-positioning page actively damages trust
- Authentic team/operation imagery builds connection
- Outcome imagery (the result of the service) outperforms process imagery

### Best practices
- Authentic operational or outcome imagery
- Match brand-positioning (premium = premium photo)
- Founder/team photo if warmth/personality is brand-relevant
- 3-5 images covering brand essence
- Optional hero video (short, muted, looping)
- Mobile-optimized variants

### Common failures
- Stock imagery contradicting brand quality
- Generic "team meeting" stock photos
- Hero carousel with 8 slides (decision paralysis)
- Auto-playing video with sound
- Heavy video that slows page load (Core Web Vitals impact)

### Authenticity restraint
A finding may recommend verifying imagery authenticity. A finding may NOT assert specific photos are stock without strong evidence.

---

## Category 3: Service-routing & navigation clarity

### Nielsen Norman recognition-over-recall (heuristic #6)
On multi-service homepages, visitors should not have to remember what's offered. ALL services should be visible — through navigation, service-cards, or both.

### Information scent (Mark Hurst)
Each navigation item or service-card is a "scent" leading to the right destination. Generic labels ("Diensten", "Wat wij doen") have weak scent. Specific labels ("Implantaten", "Wortelkanaalbehandeling") have strong scent.

### Homepage-routing patterns research
- Service-card grids on homepage outperform menu-only routing by 20-30% on multi-service sites
- 4-8 service cards is the sweet spot (under 4: under-served; over 8: paradox of choice)
- Icon + service-name + 1-line description per card outperforms name-only
- Service-cards with "Lees meer →" CTA on each card lift CTR per card

### Best practices
- Service-cards visible on homepage (4-8 services typical)
- Each service-card: icon + name + 1-line description + CTA
- Navigation includes service-categories (not buried in "Diensten" megamenu)
- Service-names in consumer language (not industry-jargon)
- Clear visual hierarchy between services (no equal-weight chaos)
- "Anders, anders, of zoek je iets specifieks?"-route for edge cases

### Common failures
- Hidden services behind "Diensten" megamenu only
- Service-names in jargon ("Endodontologie" vs "Wortelkanaalbehandeling")
- Service-card grid with 12+ items (paradox of choice)
- Service-cards with name-only (no description, no scent)
- Generic icons (every service looks identical)
- "Veel meer..." as routing instead of explicit services

### Business-type calibration
- Lokaal fysiek met één service: service-routing minder relevant, "wat wij doen" sectie volstaat
- Lokale service-provider met 4-8 diensten: service-card grid dominant
- Multi-vestiging: services + vestigingen parallel routing
- Online-only: services + use-cases parallel routing

---

## Category 4: Reviews & ratings (independent category, high weight)

### Spiegel Research Center on reviews
- Products/services with visible reviews convert up to **270% better** than those without
- Optimum review-display range: 4.2-4.7 (perfect 5.0 triggers skepticism)
- Named reviews with photo outperform anonymous by 5-7x in trust impact
- Recent reviews (within 3 months) outperform old reviews

### BrightLocal local-service research
For local B2C service businesses (most B2C leadgen homepages):
- 87% of consumers read reviews for local businesses
- Google reviews dominate (followed by Facebook, Trustpilot, Klantenvertellen)
- Average rating of 4.5+ is the consumer-shortlist threshold
- Quantity matters: 20+ reviews trusted more than 5+ at same rating

### First-time-visitor trust patterns
On homepage specifically (high first-time-visitor share):
- Reviews above-the-fold or in hero-zone lift conversion 15-30%
- Reviews near service-cards lift service-page CTR
- Recent dated reviews outperform timeless testimonials
- Multi-platform reviews (Google + Klantenvertellen + sectorspecifiek) build trust depth

### Best practices
- Review widget visible above-the-fold or directly below hero
- Specific rating + count ("Google 4,8 op basis van 248 reviews")
- 3-4 named testimonials with photo deeper on page
- Recent reviews dated and prominently shown
- Multi-platform when applicable
- Negative-review handling visible (responses to lower-star reviews build trust)
- Star-rating snippets near service-cards (per-service review-context)

### Common failures
- No reviews visible despite having them
- Anonymous "Sarah M." testimonials without photo or context
- Old reviews (3+ years undated)
- "5/5 stars" perfection that triggers skepticism
- Reviews only in footer or hidden below fold
- Generic "We love our customers" without specifics

### Calibration logic
- First-time visitors expected (organic search, social ads): reviews dominant, near hero
- Returning visitors expected (direct visit, branded search): reviews still important but can be deeper
- Multi-vestiging: aggregate review + per-vestiging breakdown

### Authenticity restraint
A finding may recommend verifying review authenticity. A finding may NOT claim displayed reviews are fabricated without strong evidence.

---

## Category 5: Trust signals & credibility

### Edelman Trust Barometer — verifiable signals
B2C consumers need verifiable trust signals on homepage:
- **Years operating** — "Sinds 2014" beats "Jarenlange ervaring"
- **Customer count** — "8.000+ klanten geknipt" specific
- **Certifications relevant to service** (BIG-register voor zorg, NVM voor makelaars, KvK-nummer)
- **Awards / press** — concrete names ("Als gezien in [media]")
- **Local recognition** — buurtkeurmerk, Google Business top-rated badge
- **Industry membership** — branche-organisatie lidmaatschap

### Cialdini authority via third-party
- Logos van bekende klanten (alleen met permissie)
- Press logos ("Als gezien in [media]")
- Branche-organisatie lidmaatschap
- Verzekerd / gegarandeerd door X

### Homepage-specific trust patterns
- Trust strip near hero (years, customer count, key cert) is high-leverage
- Press logos in dedicated band-strip
- Customer logos for B2C only when relevant (kapsalon: niet relevant; makelaar: customer-namen kunnen relevant zijn)
- Founder/team photos as trust-anchor for service-businesses

### Best practices
- Trust strip near hero (years, customer count, key cert) — concrete
- Industry-relevant certifications visible
- Press/media logos when applicable
- Specific over vague always
- KvK-nummer in footer (NL commercial sites)

### Common failures
- "Jarenlange ervaring" — unverifiable
- Generic certification logos without context
- Trust signals only in footer
- Self-claims without third-party validation

---

## Category 6: Use cases, case studies & before-after proof

### Cialdini social proof through narrative
Consumers see themselves in stories of others. Use cases and case studies provide:
- Specific outcome
- Specific starting point
- Verifiable details (name, photo, where applicable)

### StoryBrand framework (Donald Miller) — customer as hero
B2C homepage narrative pattern:
- Customer = hero with a problem
- Brand = guide with expertise
- Plan = the services
- Call-to-action = the next step
- Avoid failure → achieve success

This pattern outperforms "we are great" framing significantly in B2C.

### Transformation-narrative research
- Before-after imagery on outcome-driven services (esthetisch, makelaardij, klusbedrijven) drives 40-60% lift on engagement
- Time-anchoring ("van probleem X naar oplossing Y in [tijdsduur]") increases conversion
- Numbered outcomes outperform vague outcomes

### Best practices
- 2-3 case studies / use cases on homepage (deeper detail on dedicated pages)
- Each with: customer context, problem, service approach, outcome with specifics
- Photo of customer where permission granted
- Before-after for visual services (makelaar, klusbedrijf, fotograaf, esthetisch)
- Pulled-out quote with full story link

### Common failures
- Generic "tevreden klanten" without specifics
- Use cases without outcomes
- Stock-quote testimonials
- No use cases on outcome-driven businesses
- Use cases without permission documentation

### Business-type calibration
- Lokaal fysiek (kapsalon, restaurant): use cases minder dominant, reviews zwaarder
- Lokale service-provider (makelaar, fotograaf, klusbedrijf): use cases + before-after dominant
- High-ticket service (juridisch, financieel): named case-study quotes met outcome
- Online-only: virtual use cases met specifieke outcomes

---

## Category 7: Multi-channel contact options

### Multi-channel conversion patterns
B2C consumers convert through different channels by preference:
- Phone: urgency-driven, conversation-preference, older demographics
- WhatsApp: low-friction-preference, younger demographics, mobile-dominant
- Email: formal-preference, audit-trail-need, detail-oriented
- Form: deliberation-driven, asynchronous-comfortable
- Chat: question-driven, browse-mode, immediate-response expectation
- In-person visit: lokaal fysiek bedrijven

### Contact-visibility-on-homepage patterns
On homepage, contact options serve different visitor-jobs:
- Some visitors come to homepage with intent to contact directly (shortcut to contactpage)
- Others need to find specific contact info (telefoon van vestiging X)
- Visible contact options reduce bounces from contact-seeking visitors

### Best practices
- Phone number visible in header (sticky on scroll)
- WhatsApp icon/button where audience supports it
- Contact CTA in primary navigation
- Sticky mobile CTA bar with phone + WhatsApp
- Contact-channels-overview section if multi-channel is strategy
- Form-CTA visible on homepage (link to form or inline mini-form)

### Common failures
- Phone hidden in footer only
- WhatsApp absent despite mobile-dominant audience
- Contact-options only on /contact page (forcing extra click)
- No sticky mobile contact CTA
- Generic "Contact" link without channel-options preview

### Business-type calibration
- Lokaal fysiek: phone dominant in header
- Lokale service-provider: phone + form CTAs in header, WhatsApp afhankelijk doelgroep
- High-ticket service: phone + named-contact prominent
- Online-only: form-CTA dominant, phone optioneel, chat indien capaciteit
- Multi-vestiging: vestiging-zoeker met per-vestiging contact

---

## Category 8: Pricing transparency

### Baymard pricing research applied to homepage
Pricing display on B2C leadgen homepages is debated:
- **Visible "vanaf"-pricing** works for commodity services (kapsalon, schoonheidssalon) — anchors expectation
- **Pakket-overzichten** work for tier-able services (klusbedrijf, fotograaf) — anchors + paradox-of-choice management
- **Quote-only** works for custom/complex services (juridisch, custom builds) — forces consultation, prevents false anchoring
- Hidden pricing on commodity services hurts conversion
- Visible pricing on truly custom services creates false anchors

### Kahneman/Tversky anchoring on services
- "Vanaf €X" creates anchor before discussion
- Package tiers (basic / plus / premium) drive middle-tier selection
- Discount framing ("Save €X" beats "20% off")
- Decoy pricing (3 tiers with middle clearly favored) increases conversion to middle

### "Vanaf"-pricing psychology in services
- Removes price-anxiety as conversion blocker
- Sets expectation, doesn't commit
- Best paired with "afhankelijk van [variabele]" microcopy
- Works across mid-ticket and high-ticket when transparently framed

### Best practices
- For commodity services: full transparent pricing on homepage (with link to per-service detail)
- For custom services: "vanaf" pricing with package indication
- For high-ticket: optional indicative range + quote-CTA dominant
- Price visible in same viewport as primary CTA
- Tax-handling explicit ("inclusief BTW" for B2C)

### Common failures
- No pricing on commodity services (forces phone call for €15 service)
- Hidden pricing without value framing
- "Pricing on request" without anchor
- Multiple package tiers without clear distinction
- Inclusive/exclusive BTW ambiguity

### Business-type calibration
- Commodity (kapsalon, schoonheidssalon, was-service): full pricing visible
- Mid-ticket consideration (fysio, tandarts, fotograaf): "vanaf" + pakket
- High-ticket consideration (juridisch, financieel adviseur): indicative range optional, quote-CTA dominant
- Multi-vestiging: per-vestiging variatie indien relevant (geografische prijsverschillen)

---

## Category 9: CTA strategy multi-path

### Fogg Behavior Model on homepage CTAs
Homepages serve multiple visitor-jobs, so multiple CTAs are needed:
- Brand-evaluation visitor → service-routing CTAs
- Service-finding visitor → specific service CTAs
- Trust-verification visitor → reviews, about-us CTAs
- Contact-seeking visitor → phone, WhatsApp, contact CTAs
- Pre-research visitor → bookmark, read-more CTAs

### Multi-purpose-page CTA patterns
Unlike dedicated LPs (single-CTA dogma), homepages benefit from:
- Primary CTA in hero (most likely visitor-job)
- Secondary CTAs in service-cards (service-routing)
- Tertiary CTAs in trust/reviews sections (deeper engagement)
- Multi-channel contact CTAs (phone, WhatsApp, form)
- Sticky mobile CTA matched to primary intent

### Baymard CTA research
- CTA visibility above-the-fold critical
- Sticky mobile CTA on long pages is non-negotiable
- Action-oriented CTA copy outperforms generic ("Vraag offerte aan" beats "Klik hier")
- CTA color contrast and size matter (Fitts's Law)

### Best practices
- Hero CTA matched to primary visitor-job
- Service-card CTAs ("Lees meer →" or "Plan afspraak")
- Trust-section CTAs (no aggressive ask, but anchor back to action)
- Multi-channel contact CTAs in header + footer
- Sticky mobile CTA matching hero CTA
- CTA copy specific and action-oriented

### Common failures
- Single-CTA dogma applied to multi-purpose homepage
- Generic "Klik hier" or "Verzenden"
- Multi-CTA chaos (8+ equally weighted)
- Sticky mobile CTA absent
- CTA not visible above-the-fold
- CTAs matched to wrong visitor-jobs

### Business-type calibration
- Lokaal fysiek: phone-CTA primair, visit-CTA secundair, WhatsApp tertiair
- Lokale service-provider: form-CTA + phone-CTA balanced, service-routing CTAs
- High-ticket service: phone + plan-gesprek CTAs, conservatieve multi-CTA
- Online-only: form-CTA dominant, service-routing CTAs secundair

---

## Category 10: Lokale relevantie & multi-vestiging

### BrightLocal local-business research
For local B2C service businesses (most B2C leadgen homepages):
- 78% of mobile local searches result in offline conversion within 24 hours
- Local signals on homepage lift conversion 20-35% vs no-local-context homepages
- NAP (Name-Address-Phone) consistency between site and Google Business critical

### Google Business integration patterns
- Embedded Google reviews / rating from Google Business
- Address consistent with Google Business
- Openingstijden consistent met Google Business
- "We zijn nu open"-status van Google Business

### Multi-location homepage patterns
- Vestigingen-zoeker prominent op homepage van multi-vestiging organisaties
- Dichtstbijzijnde-vestiging-detectie via geolocation of postcode-input
- Per-vestiging openingstijden, telefoon, route
- Algemene contact-info als fallback

### Best practices
- Adres + telefoon in header/footer (NAP-consistent met Google Business)
- Embedded Google reviews/rating
- Area-served signalen ("Werkzaam in regio Amsterdam-Utrecht")
- Multi-vestiging: zoeker met visuele kaart van vestigingen
- "We werken in jouw buurt" / "Vestiging dicht bij jou" lokale framing
- Lokale referenties / klanten waar passend

### Common failures
- Geen lokale signalen op lokaal-fysiek bedrijf homepage
- Multi-vestiging zonder zoeker (forceer extra klik)
- NAP-inconsistentie met Google Business
- Geen area-served bij service-provider
- Lokale referenties ontbreken bij lokaal bedrijf

### Business-type calibration
- Lokaal fysiek (één vestiging): adres + map + openingstijden hero-relevant
- Lokaal fysiek (multi-vestiging): zoeker dominant
- Lokale service-provider met mobiel team: area-served + werkgebied-kaart
- Online-only: lokale signalen NIET relevant (geen forceren)

---

## Category 11: Mobile experience

### Baymard mobile commerce research
B2C leadgen homepages zijn mobile-dominant:
- 60-80% van B2C service-business homepage traffic is mobile
- Mobile conversion lags desktop by 30-50% on average
- Sticky CTA op mobiel non-negotiable voor long homepages

### Google mobile-first indexing
Mobile experience drijft ranking AND conversie. Mobile audit is core.

### Thumb-zone usability (Hoober)
Mobile tap-targets in thumb-bereik:
- Sticky CTA bottom (primair thumb-zone)
- Phone number prominent in header (tap-to-call)
- Service-cards thumb-friendly (grote tap-area's)

### Mobile homepage patterns
- **Mobile-first navigation:** hamburger met service-categories niet diep verstopt
- **Mobile-optimized service-cards:** single-column op kleine schermen
- **Sticky mobile CTA-bar:** phone + WhatsApp + primary form-CTA
- **Mobile hero:** single-screen ideal, key copy + CTA boven de vouw
- **Mobile-optimized reviews:** widget mobile-friendly (geen desktop-port)

### Best practices
- Sticky bottom CTA op long pages
- Phone tap-to-call live op mobile
- WhatsApp click-to-chat live waar relevant
- Service-cards single column op mobile
- Hero readable zonder zoom
- Fast page load (Core Web Vitals)
- Reviews widget mobile-friendly

### Common failures
- Geen sticky mobile CTA
- Phone visible maar plain text
- Desktop service-card-grid ge-port naar mobile (multi-column te smal)
- Hero requires zoom
- Heavy hero video slows mobile load
- Hamburger menu met diepe verstopte services

---

## Brand calibration notes

Always recalibrate by brand snapshot AND business-type AND conversie-doel:

**Example: Hero CTA**
- Lokaal kapsalon: "Boek online" + phone + WhatsApp
- Tandartspraktijk: "Plan afspraak" + phone + reviews-snippet
- Klusbedrijf: "Vraag offerte aan" + phone + WhatsApp + before-after-portfolio
- Restaurant: "Reserveer tafel" + phone + openingstijden status
- Online financieel adviseur: "Plan kennismaking" + form + response-time-belofte
- Multi-vestiging keten: "Vind vestiging" + service-finder + algemene contact

**Example: Reviews emphasis**
- First-touch dominant homepage (veel organic search traffic): reviews kritiek near hero
- Branded-search dominant homepage (returning visitors): reviews kunnen deeper
- Multi-vestiging: aggregate rating + per-vestiging breakdown

**Example: Service-routing prominence**
- Eén-dienst bedrijf (specialist tandarts implantaten): service-routing niet relevant, content-deepening dominant
- Multi-dienst bedrijf (algemeen klusbedrijf): service-card grid dominant
- Hybrid bedrijf (content + leadgen): leadgen-routing primair, content secundair

Recommendations that don't match brand AND business-type AND conversie-doel zijn fout.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites a specific principle, study, or source
- [ ] Recommendation is concrete (exact copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric is named (service-page CTR / contact-conversion / bounce / scroll-depth)
- [ ] ICE justified by I/C/E breakdown
- [ ] Recommendation matches brand snapshot AND business-type AND conversie-doel
- [ ] Multi-purpose entry-point logic respected (no single-CTA dogma)
- [ ] First-time-visitor context respected where relevant
- [ ] Reviews findings calibrated for high weight on homepage
- [ ] Dutch output: no "huren" check
- [ ] No authenticity claims about photos/reviews/certifications

If any box unchecked, rework or remove the finding before delivering.
