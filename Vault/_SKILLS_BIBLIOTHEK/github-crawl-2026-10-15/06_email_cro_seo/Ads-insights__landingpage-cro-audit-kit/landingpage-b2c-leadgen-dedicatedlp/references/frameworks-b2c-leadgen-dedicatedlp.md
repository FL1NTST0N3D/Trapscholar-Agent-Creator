# Frameworks for B2C Leadgen Dedicated Landing Page Audits

This reference file contains the CRO and dedicated-LP-specific frameworks, principles, and applied research. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

Dedicated LPs are uniquely prone to fabricated findings because so much is dynamic:
- Dynamic Text Replacement (DTR) per UTM keyword — HTML shows default, visitor sees variant
- A/B-test variants from Unbounce, Instapage, Optimizely, VWO — HTML may show all variants or random pick
- Countdown timers, scarcity counters ("nog 3 plekken"), live-visitor widgets — all JS
- Form-builders (HubSpot, Gravity, Typeform, native LP-tool) — fields and validation invisible to HTML
- Exit-intent popups, sticky CTAs, chat widgets — conditional rendering
- Personalized hero based on traffic-source — server-side or JS injection
- Calculator/audit-tools — interactive widget invisible to HTML

**For every finding, verify against screenshots before delivering.**

---

## CRITICAL — Single-purpose page logic

Recommendations valid on multi-purpose pages are often WRONG on dedicated LPs. Specifically:

**Do NOT automatically recommend:**
- "Add secondary CTAs" — Unbounce attention-ratio research shows 1:1 (one link, one CTA) is ideal
- "Restore navigation" — Marketing Sherpa data: removing nav lifts conversion 10-25% on paid LPs
- "Add cross-sell" — distracts from single conversion goal
- "Link to homepage" — exit-path, conversion-killer
- "Add related services" — interest-fragmenter

**DO recommend (when appropriate):**
- Single CTA repeated multiple times (one offer, many trigger-points)
- Anchor-link CTAs (scroll-to-form)
- Sticky bottom CTA on mobile (same CTA, always available)
- Phone number as secondary path ONLY if it's the same conversion-funnel

The single-purpose rule trumps the multi-CTA-best-practice on this page-type.

---

## CRITICAL — Traffic-source-aware recommendations

Dedicated LP recommendations are useless without knowing or assuming the traffic-source:

**Google Search Ads:**
- Visitor arrived with intent and a specific search query
- Message-match with the AD HEADLINE is critical (Hurst's Scent of Information)
- DTR (Dynamic Text Replacement) per keyword is a powerful tactic
- Hero copy should echo the ad-promise verbatim
- Long-form content acceptable if intent is research-mode

**Meta/Instagram/TikTok:**
- Visitor arrived in interest/discovery-mode, not transaction-mode
- Hero IMAGE matters more than headline copy
- Visual continuity with ad-creative is critical
- Shorter, more visual page wins
- Mobile is dominant (90%+ traffic)

**Email:**
- Visitor is warm, often a customer or subscriber
- Less proof needed (trust pre-established)
- Faster-to-form acceptable
- Risk: assuming warm-traffic-level patience when traffic is actually mixed

**Affiliate:**
- Pre-sold by the affiliate's content (review, blog, comparison)
- Visitor expects what affiliate promised
- Trust signals from affiliate's site (not LP) may already be doing the work
- Risk: LP may need to re-establish trust if affiliate doesn't pre-sell well

**Display/programmatic:**
- Cold, interrupted traffic
- Trust signals dominate
- Lower conversion expectations, higher reliance on retargeting

If traffic-source is not provided, state the assumption in the relevant findings.

---

## CRITICAL — Lead-quality vs lead-volume tradeoff (CAC-calibrated)

Every form-design recommendation must acknowledge this tradeoff:

- **Shorter form** = higher form-completion rate, lower lead quality
- **Longer form** = lower form-completion rate, higher lead quality

For dedicated LPs the calibration depends on **paid-traffic CAC economics:**
- **Low-CAC campaigns** (low-ticket consumer, broad audience): cannot afford friction; 3-4 fields max
- **Mid-CAC campaigns** (mid-ticket consumer, qualified traffic): 5-7 fields acceptable
- **High-CAC campaigns** (high-ticket consumer, niche audience): 8-12 fields acceptable if leads are valuable enough

A common mistake: recommending "shorten form" without considering downstream economics. If the brand pays €40 per click and needs qualified leads to justify it, a 3-field form may flood the sales team with garbage. If the brand pays €0.50 per click and any phone-number is valuable, even a 2-field form is acceptable.

When in doubt, recommend testing both directions OR ask for CAC context.

---

## Core frameworks (apply across the entire audit)

### Unbounce LP conversion benchmarks
The leading research source on dedicated LP performance:
- Average B2C LP conversion: 9-12% (varies wildly by industry: finance 11%, health 8%, e-commerce 14%)
- Top-performing LPs (90th percentile): 25%+ conversion
- Attention ratio matters: 1:1 (one CTA, one link) outperforms 1:5+ by 30-50%
- LPs with navigation hidden outperform LPs with navigation by 10-25%
- LPs with single hero CTA + repeated CTA pattern outperform single-CTA-only by 8-15%
- Mobile conversion lags desktop by 30-50% on average across most B2C verticals

### ConversionXL message-match research (Bryan Eisenberg, Peep Laja)
Message-match is the #1 leverage point on most dedicated LPs:
- LPs that mirror ad-headline copy convert 2-5x higher than generic LPs
- LPs that mirror ad-imagery (color, model, scene) outperform generic by 15-30%
- LPs with DTR (Dynamic Text Replacement) per keyword outperform static LPs by 10-40% on search traffic
- "Scent of Information" (Mark Hurst): visitor follows scent of their original query through ad → LP → form. Any break in scent loses them.

### Marketing Sherpa LP studies
- LP-specific benchmark: 17% average leadgen conversion, 25%+ for top quartile
- Long-form LPs (3000+ words) outperform short-form on consideration-products, lose on impulse-products
- Above-the-fold conversion rate is typically 40-70% of total conversion — most visitors don't scroll
- Video on hero increases conversion 20-50% (varies by audience)
- Single offer LPs convert 2-3x multi-offer LPs

### MECLABS Conversion Sequence Heuristic on LPs
C = 4m + 3v + 2(i−f) − 2a

On B2C dedicated LPs:
- **m (motivation):** highly variable by source (Google Search high, Display low)
- **v (value):** SINGLE clear value proposition matched to ad-promise
- **i (incentive):** lead-magnet (free, gratis, exclusive, limited)
- **f (friction):** ANY navigation, ANY secondary CTA, ANY unnecessary form-field
- **a (anxiety):** privacy, sales-call fear, hidden cost suspicion

### Cialdini's principles on dedicated LPs
- **Authority** — certifications, named experts, "als gezien in [media]"
- **Social proof** — customer count ("12.000+ klanten"), reviews, recent activity
- **Liking** — warm tone, founder photo, local context if relevant
- **Commitment-consistency** — multi-step forms create commitment-momentum
- **Reciprocity** — value-rich lead-magnet (free, valuable, immediate)
- **Scarcity** — limited slots, time-limited offers (ONLY when real and verifiable)

### Fogg Behavior Model (B = MAT) on dedicated LPs
LP's job: make conversion ACTION effortless at the moment of TRIGGER, when MOTIVATION is highest.
- Motivation is HIGHEST in the hero (visitor arrived with intent)
- Motivation decays with each scroll
- Trigger must be immediate (above-the-fold CTA non-negotiable)
- Ability must be effortless (short form, single field, clear next step)

### Nielsen Norman heuristics applied to LPs
- **#1 Visibility of system status** — form-submission feedback, "wat gebeurt er na klik?" copy
- **#2 Match real world** — copy matches consumer search vocabulary AND ad copy
- **#3 User control and freedom** — but: LPs often DELIBERATELY constrain control (no nav). This is OK on dedicated LPs.
- **#5 Error prevention** — inline form validation, format hints
- **#8 Aesthetic and minimal design** — single-purpose pages benefit from minimalism

### Hormozi's irresistible-offer principles
For lead-magnets and offers on dedicated LPs:
- **Dream outcome** — what the visitor most wants
- **Perceived likelihood of achievement** — proof, evidence, social proof
- **Time delay** — how fast they get the outcome
- **Effort and sacrifice** — how easy the conversion-step is

A lead-magnet that scores high on all four converts massively higher than one that scores low.

### Jobs-to-be-Done on B2C dedicated LPs
B2C consumers on a dedicated LP are doing ONE of:
1. **Offer-evaluation** — "Is this offer right for me?" (dominant for promo LPs)
2. **Quick-conversion** — "Yes, claim this" (impulse offers)
3. **Resource-collection** — "Get this guide/tool" (lead-magnet LPs)
4. **Comparison-verification** — "Is this still the best option?" (after research)

Each job needs different page support. Dedicated LP serves ONE job well, not multiple. Identifying the job is critical for calibration.

**Important Dutch translation:** never use "huren" for JTBD framing. Use "kiezen voor", "zoeken om X op te lossen", "consumenten die X willen".

---

## Category 1: Message match & traffic-source congruentie

### ConversionXL message-match research (Eisenberg)
The visitor arrives with an expectation set by the ad/email/referrer. The LP must confirm that expectation within 5 seconds, or the visitor bounces (back-button, exit, conversion lost).

### Scent of Information (Mark Hurst)
Visitors follow the "scent" of their original query/intent through:
- Ad headline → LP headline (must match)
- Ad imagery → LP imagery (must align)
- Ad offer → LP offer (must be the same)
- Ad tone → LP tone (must be congruent)

Any break in scent reduces conversion.

### Best practices
- LP headline echoes ad headline (verbatim or near-verbatim)
- LP imagery aligns with ad imagery (style, models, scenery)
- LP offer matches ad offer exactly (no bait-and-switch)
- DTR per UTM keyword for search-driven LPs
- LP tone matches ad tone (urgent ad → urgent LP; warm ad → warm LP)

### Common failures
- Generic brand headline on LP despite specific ad copy
- Ad promises "50% off"; LP shows "save money" without specific offer
- Ad imagery is lifestyle; LP imagery is product-only
- LP doesn't acknowledge the campaign at all (looks like a homepage)
- Multi-campaign LP (one LP for all ads) with no DTR
- Bait-and-switch: ad promises X, LP delivers Y

### Traffic-source calibration
- Search: headline match dominant; visitor knows what they searched
- Social: image match dominant; visitor scrolled past, didn't read ad text closely
- Email: subject-line match dominant; visitor came for the email's promise
- Affiliate: affiliate's copy is the scent, not the brand's; LP must continue affiliate's argument

### Visual verification requirement
A finding may claim "message-match weak" only if both the ad (or proxy for it) AND the LP are visible to assess. If only LP visible, frame as: "kan niet beoordelen tegen ad, maar LP-hero is generiek genoeg dat message-match-risico waarschijnlijk is."

---

## Category 2: Above-the-fold value proposition & single-purpose clarity

### April Dunford positioning on LPs
The above-the-fold must answer: **"Wat is dit aanbod, voor wie, en wat is mijn volgende stap?"** within 5 seconds. On a dedicated LP, this is more critical than on any other page-type — visitors often convert without scrolling.

### 5-second clarity test
- Show LP to a stranger for 5 seconds
- Ask: "What is this page offering? What do they want me to do?"
- If answer unclear, hero fails

### WiderFunnel LIFT — value proposition factor
LP hero must communicate:
- The specific offer (concrete, in customer language)
- For whom (target consumer)
- Differentiator (why this offer beats alternatives)
- Clear single next step (CTA)

### MECLABS clarity-as-conversion-driver
Clarity is the #1 conversion driver on LPs. Vague hero copy = bounced traffic.

### Best practices
- Headline names the specific offer (not generic brand statement)
- Subheadline differentiates / specifies (audience, benefit, mechanism)
- One credibility anchor visible (customer count, rating, certification)
- Single primary CTA visible above-the-fold
- Form visible above-the-fold OR scroll-to-form CTA prominent
- Authentic, campaign-relevant imagery

### Common failures
- Generic "Welkom bij [Brand]" or "Uw partner in X" hero copy
- Brand name as headline (brand-first thinking)
- Multiple equal CTAs creating paralysis
- Stock imagery contradicting offer
- Hero too long (>2 visual elements competing)
- CTA below-the-fold

### Campaign-type calibration
- Form-driven LP: form IN the hero, headline + CTA flow into form
- Download-driven LP: lead-magnet visual (book cover, PDF preview) prominent
- Demo/trial-driven LP: product screenshot or demo-video
- Calculator-driven LP: calculator widget IN the hero
- Booking-driven LP: calendar widget or "Plan binnen 60s" CTA

---

## Category 3: Hero imagery / video (campagne-specifiek)

### Nielsen Norman visual-first
On LPs, visual is processed first. If the visual contradicts the headline, visitor experiences confusion (anxiety in MECLABS). The visual sets the EMOTIONAL tone before the copy is read.

### Marketing Sherpa imagery research
- LPs with authentic, campaign-relevant imagery convert 2-3x better than stock-image LPs
- Video on hero increases conversion 20-50% (varies; works best when video shows outcome or testimonial)
- Hero video <30s with autoplay-muted-loop is the high-performing pattern
- Hero video that auto-plays sound is universally penalized

### Campaign-imagery congruence
On dedicated LPs specifically, hero imagery must:
- Match the ad-creative visual style
- Show the OUTCOME of the offer (not the process)
- Not introduce new themes not in the ad

### Best practices
- Authentic operational or outcome imagery
- Match ad-creative style (color palette, lighting, models)
- Show the result (transformation imagery)
- Optional hero video (short, muted, looping)
- Mobile-optimized variants
- Lead-magnet visual when relevant (book cover, dashboard screenshot, calculator preview)

### Common failures
- Stock imagery contradicting offer
- Generic business-people photos on consumer-LPs
- Process imagery instead of outcome imagery
- Hero video with auto-sound
- Heavy video that slows page load (Core Web Vitals impact)
- LP imagery completely unrelated to ad-creative

### Authenticity restraint
A finding may recommend verifying imagery authenticity. A finding may NOT assert specific photos are stock without strong evidence.

---

## Category 4: Single primary CTA strategy

### Unbounce attention-ratio research
The defining metric of LP CTA-strategy:
- **Attention ratio = links / conversion-goals**
- Ideal: 1:1 (one link, one conversion goal)
- Most LPs run 5:1 to 10:1 (navigation, footer, social, etc.)
- Reducing attention ratio from 10:1 to 1:1 lifts conversion 30-50%

### Hick's Law on LPs
Each choice slows decision-making. Multiple equal CTAs create paralysis. Single CTA repeated removes decision-friction.

### Fitts's Law on CTA placement
- CTA buttons must be large (40px+ on mobile, 48px+ touchable)
- CTA placement in thumb-zone on mobile
- CTA color contrast with surrounding (button-blindness test)

### Best practices
- ONE primary CTA, repeated at strategic points (hero, after social proof, after FAQ, sticky mobile)
- CTA copy action-oriented and specific ("Download de gids" beats "Submit")
- CTA button large, contrasting, in primary visual focus
- No competing secondary CTAs ("Of bekijk hier...")
- Sticky bottom CTA on mobile
- Phone number as secondary path acceptable if it leads to same conversion-funnel

### Common failures
- Multiple equal CTAs ("Download" / "Vraag demo" / "Bekijk video") competing
- CTA copy generic ("Verzenden" / "Verstuur" / "Submit")
- Tiny CTA button (under 40px)
- Low-contrast CTA blending into background
- CTA only above-the-fold (long pages need repeated CTAs)
- No sticky CTA on mobile

### Single-CTA logic
Multi-CTA recommendations from other contexts (servicepage, homepage) do NOT apply here. The dedicated LP exists to convert traffic to ONE action. Adding paths kills it.

---

## Category 5: Reviews & ratings (independent category)

### Spiegel Research Center on reviews
- Products/services with visible reviews convert up to **270% better** than those without
- Optimum review-display range: 4.2-4.7 (perfect 5.0 triggers skepticism)
- Named reviews with photo outperform anonymous by **5-7x** in trust impact
- Recent reviews (within 3 months) outperform old reviews

### BrightLocal local-service review research
For local B2C dedicated LPs (e.g. local-service campaigns):
- 87% of consumers read reviews for local businesses
- Google reviews dominate (followed by Facebook, Trustpilot, Klantenvertellen)
- Average rating of 4.5+ is the consumer-shortlist threshold
- Quantity matters: 20+ reviews trusted more than 5+ even at same rating

### Testimonial placement research (Marketing Sherpa)
On dedicated LPs specifically:
- Reviews above-the-fold (near CTA) lift conversion 10-30%
- Photo-testimonial dedicated section after offer increases scroll-depth
- Star-rating + count snippet is high-leverage low-cost addition
- Embedded review-widgets (Google/Klantenvertellen) outperform static review-text

### Best practices
- Review widget visible above-the-fold or directly below hero (especially for cold traffic)
- Specific rating + count ("Klantenvertellen 9,3 op basis van 248 reviews")
- Named-reviewer testimonials with photo deeper on page
- Recent reviews dated and prominently shown
- Multiple platforms when applicable (Google + Klantenvertellen + sector-specific)

### Common failures
- No reviews visible despite having them
- Anonymous "Sarah M." testimonials without context
- Old undated reviews (3+ years)
- "5/5 stars" perfection that triggers skepticism
- Reviews only in footer or hidden below fold

### Campaign-type calibration
- Cold traffic (Display, Meta interest): reviews MUST be near hero
- Warm traffic (email, retargeting): reviews can be deeper on page
- Affiliate: affiliate may have done review-work; LP can have less

### Authenticity restraint
A finding may recommend verifying review authenticity. A finding may NOT claim displayed reviews are fabricated without strong evidence.

---

## Category 6: Trust signals & credibility (context-loosheid extra-weight)

### Edelman Trust Barometer — verifiable signals
On dedicated LPs, the visitor has NO sitemap context (no navigation, no homepage visit). Trust signals carry extra weight:
- **Years operating** — "Sinds 2014" beats "Jarenlange ervaring"
- **Customer count** — "850+ klanten" specific, not "duizenden"
- **Certifications relevant to service** (BIG-register, NVM, KvK-nummer)
- **Awards / press** — concrete names
- **Privacy / security signals** — AVG-compliant, "wij delen niet met derden"
- **Money-back / guarantee** — risk-reversal lowers anxiety

### Cialdini authority via third-party
- Logos van bekende klanten (alleen met permissie)
- Press logos ("Als gezien in [media]")
- Branche-organisatie lidmaatschap
- Verzekerd / gegarandeerd door X

### LP-specific trust extras
Because LPs often hide navigation, visitors lose normal trust-anchors. Compensate with:
- Contact info visible (address, phone, email at minimum in footer)
- Company name + KvK clearly visible
- Privacy-policy link near form
- "Wat gebeurt er na klik?" microcopy

### Best practices
- Trust strip near hero (years, customer count, key cert)
- Industry-relevant certifications visible
- Privacy/security signals near form
- Money-back or satisfaction guarantee if applicable
- Footer with minimum contact info

### Common failures
- "Jarenlange ervaring" — unverifiable
- Generic certification logos without context
- No contact info at all (extreme nav-hiding)
- Trust signals only in footer despite long page
- Self-claims without third-party validation
- Missing privacy-policy link near form

---

## Category 7: Use cases / social proof / case studies

### Cialdini social proof through narrative
Consumers see themselves in stories of others. Case studies and use cases provide:
- Specific outcome
- Specific starting point
- Verifiable details (name, photo where applicable)

### StoryBrand framework (Donald Miller) — customer as hero
B2C dedicated LP narrative pattern:
- Customer = hero with a problem
- Brand = guide with expertise
- Plan = the offer / lead-magnet
- Call-to-action = the conversion step
- Avoid failure → achieve success

### Transformation-narrative research
- Before-after imagery on outcome-driven offers drives 40-60% lift on engagement
- Time-anchoring ("in [tijdsduur] van X naar Y") increases conversion
- Specific numbered outcomes outperform vague outcomes

### Best practices
- 2-4 named-customer use cases on page
- Each with: context, problem, offer-use, outcome with specifics
- Photo of customer where permission granted
- Before-after for visual outcomes
- Pulled-out quote with full story available

### Common failures
- Generic "tevreden klanten" without specifics
- Use cases without outcomes
- Stock-quote testimonials
- No use cases on consideration-offers
- Use cases without permission documentation

### Campaign-type calibration
- Low-CAC quick-conversion LPs: 1-2 short use cases acceptable
- Mid-CAC consideration LPs: 2-4 detailed use cases with photos
- High-CAC niche LPs: 1-2 deep case studies with metrics and named experts

---

## Category 8: Lead-magnet propositie & exchange value

### Cialdini reciprocity on dedicated LPs
On lead-magnet driven LPs, the value-exchange clarity is THE conversion driver:
- What does the consumer give? (contact info, time)
- What does the consumer get? (specific, valuable, immediate)
- Is the exchange clearly valuable?

### Hormozi irresistible offer principles
The lead-magnet must score high on:
- **Dream outcome** — what they most want
- **Perceived likelihood** — proof it works
- **Time delay** — fast outcome
- **Effort/sacrifice** — minimal friction

A high-converting lead-magnet hits all four. A weak lead-magnet usually misses on perceived likelihood (no proof) or time delay (vague "we'll be in touch").

### Value-exchange-clarity research (Marketing Sherpa)
- Specific lead-magnets ("Ontvang binnen 24u een gratis bespaaranalyse van €350-waarde") convert 40-60% higher than vague ones ("vraag info aan")
- Time-anchored lead-magnets outperform open-ended
- Lead-magnets matched to consumer-job outperform generic ones

### Lead-magnet types and best practices
- **Whitepaper / e-book / gids:** show cover/preview, list contents, specify length, name author
- **Calculator / audit-tool:** show example output, "Beste resultaat in 60s"
- **Demo / trial:** show product, specify trial length, specify what's included
- **Free consultation / quote:** specify call-length, specify what's discussed, name the expert
- **Sample / coupon:** show what they get, value-anchor ("ter waarde van €X")

### Common failures
- "Vraag info aan" without value promise
- "Neem contact op" without specifying what happens
- No response-time commitment
- Vague reciprocity ("we helpen je graag")
- Lead-magnet visually invisible (no preview)
- Lead-magnet name vague ("Onze gids")

---

## Category 9: Lead-form design & field optimization

### CXL/ConversionXL form research
The #1 leverage point on most dedicated LPs:
- Each unnecessary field reduces conversion ~7-11%
- Average B2C LP form: 3-5 fields
- Required fields: typically name + contact (phone OR email, not both — unless high-CAC)

### Baymard form-field research
- Field-label above input outperforms placeholder-only labels
- Real-time validation outperforms submit-time validation
- Mobile-appropriate keyboards for numeric fields
- Single-column form outperforms multi-column

### Hick's Law on forms
Each field is a decision point. Balance:
- Sufficient fields for lead qualification
- Minimum fields for completion rate
- Smart defaults where possible

### Multi-step vs single-step (LP-specific)
- Single-step: 1-4 fields, low commitment
- Multi-step: 5+ fields, creates commitment-momentum (start with low-friction field)
- Progress indicator critical on multi-step
- Multi-step can OUTPERFORM single-step on longer forms by 20-40%

### LP-specific form patterns
- **Hero form:** form IN the hero (form-driven LPs)
- **Scroll-to-form:** form lower, multiple anchor-CTAs scroll to it
- **Multi-step LP:** entire LP is the form (no copy, just questions one-at-a-time)
- **Calculator-to-form:** tool engagement first, email-gate for results
- **Modal/popup form:** form opens on CTA-click (mobile-friendly variant)

### Best practices
- Field count matches campaign-type and CAC
- Labels above fields
- Required-only marking (mark optional, not required)
- Real-time validation with format hints
- Single-column on mobile
- Mobile-optimized keyboards
- Action-oriented submit CTA ("Stuur aanvraag" / "Download direct" / "Plan gesprek")
- Privacy reassurance near submit ("We bellen alleen na jouw verzoek")

### Common failures
- Too many required fields for campaign-CAC
- Placeholder-only labels (disappear on typing)
- Submit-time validation only
- Multi-column form on mobile
- Generic "Submit" CTA
- No format hints (phone, postcode)
- Asterisks on EVERY field
- No privacy reassurance
- Hidden submit button below fold

### Lead-quality vs lead-volume calibration
Always acknowledge this tradeoff:
- "Verwijder veld X" → "verwacht meer leads, mogelijk lagere kwaliteit"
- "Voeg veld Y toe" → "verwacht minder leads, hogere kwaliteit"

Calibrate to known or assumed CAC.

---

## Category 10: Friction reduction & distraction management

### Unbounce attention-ratio research
- Attention ratio = links / conversion goals
- Ideal 1:1 — every additional link is a potential exit
- LPs without hidden navigation have 15-25% lower conversion than nav-hidden equivalents

### Navigation-hiding research
- Hidden full nav on dedicated LP lifts conversion 10-25%
- Footer with minimal contact info acceptable (trust requirement)
- "Back to homepage" link in footer is exit-path; consider removing

### Exit-path reduction
Every link off the LP is a conversion-risk:
- Social media links (open new tab, often lost)
- "Bekijk meer producten/diensten" links
- "Over ons" link
- Blog links
- Footer navigation
- External press logos that link out

### Distraction elements
- Auto-playing sound
- Hero video that competes with form
- Excessive animation
- Multiple urgency/scarcity elements competing
- Chat popups that obscure CTA

### Best practices
- Hide hoofdnavigatie (or simplify to logo + phone)
- Minimal footer (contact, privacy-policy, KvK only)
- External links open in new tab when essential (rare)
- No social-media-share buttons (exit-path)
- Single urgency element if any (not multiple competing)
- Chat as overlay-only (not blocker)

### Common failures
- Full site navigation on dedicated LP
- Social-share buttons on LP
- Press logos linking out to publication
- Multiple competing urgency elements
- Chat popup blocking CTA on mobile
- "Bekijk meer..." links pulling visitor off-funnel

### When NOT to hide navigation
- If the LP is hybrid (sometimes campaign-LP, sometimes organic landing) — nav helps organic visitors
- If brand is so established that nav is part of trust signal
- If LP has companion-pages essential to conversion decision (rare on B2C)

Acknowledge nuance; don't recommend nav-removal as default without considering hybrid use.

---

## Category 11: Mobile experience

### Baymard mobile research applied to dedicated LPs
B2C dedicated LPs are mobile-dominant:
- 60-90% of B2C campaign LP traffic is mobile (especially Meta/TikTok)
- Mobile conversion lags desktop by 30-50% on average
- Sticky CTA on mobile is non-negotiable for long pages

### Google mobile-first indexing
Mobile experience drives quality score (paid) AND conversion. Mobile audit is core.

### Thumb-zone usability (Hoober)
Mobile tap-targets must be in thumb-reachable zone:
- Sticky CTA at bottom (primary thumb-zone)
- Top-nav CTA secondary
- Avoid mid-screen-only primary CTAs

### LP-specific mobile patterns
- **Form mobile-optimized:** single column, large fields, mobile keyboards
- **Hero mobile-readable:** no zoom needed
- **Single-screen hero ideal:** offer + CTA visible without scroll
- **Sticky CTA mobile-prominent:** matches primary CTA copy
- **Tap-to-call for phone-fallback:** `tel:` links

### Best practices
- Sticky bottom CTA on long pages
- Phone number tap-to-call
- Form mobile-optimized (single column, large fields, mobile keyboards)
- Hero readable without zoom
- Imagery mobile-optimized variants
- Fast page load (Core Web Vitals critical for paid traffic)

### Common failures
- No sticky mobile CTA
- Phone visible but not clickable
- Desktop form ported to mobile (multi-column)
- Hero requires zoom to read
- Slow page load (Core Web Vitals fail = paid penalty)
- Form fields too small for thumbs

---

## Brand and campaign calibration notes

Always recalibrate by brand snapshot AND campaign-type AND traffic-source:

**Example: Hero CTA**
- Form-driven LP (offerte): "Vraag offerte aan" + form in hero
- Download-driven LP (gids): "Download gratis" + lead-magnet visual
- Demo-driven LP (proefperiode): "Start gratis proefperiode" + product preview
- Calculator-driven LP: "Bereken nu" + calculator IN hero
- Booking-driven LP: "Plan binnen 60 seconden" + calendar widget

**Example: Reviews emphasis**
- Cold traffic (Display, broad Meta): reviews critical near hero
- Warm traffic (email, retargeting): reviews can be deeper
- Affiliate-pre-sold: reviews can be lighter

**Example: Form length**
- Low-CAC campaign: 3-4 fields max
- Mid-CAC campaign: 5-7 fields
- High-CAC campaign: 8-12 fields acceptable if leads valuable

**Example: Trust signals**
- Cold traffic + no nav: heavy trust signals required
- Warm traffic + minimal nav: lighter trust signals acceptable
- Brand-known: less trust-work needed
- Brand-unknown: heavy trust required

Recommendations that don't match brand AND campaign-type AND traffic-source are wrong.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites a specific principle, study, or source
- [ ] Recommendation is concrete (exact copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric is named (conversion rate / form-completion / bounce / CPL)
- [ ] ICE justified by I/C/E breakdown
- [ ] Recommendation matches brand snapshot AND campaign-type AND traffic-source
- [ ] Lead-quality vs lead-volume tradeoff acknowledged where relevant
- [ ] Single-purpose page logic respected (no automatic multi-CTA recommendations)
- [ ] Dutch output: no "huren" check
- [ ] No authenticity claims about photos/reviews/certifications/countdowns

If any box unchecked, rework or remove the finding before delivering.
