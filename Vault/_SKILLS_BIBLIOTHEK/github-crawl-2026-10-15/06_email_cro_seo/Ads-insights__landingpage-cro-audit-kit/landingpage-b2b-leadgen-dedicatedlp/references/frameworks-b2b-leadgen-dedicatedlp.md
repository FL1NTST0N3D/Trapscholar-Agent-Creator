# Frameworks for B2B Leadgen Dedicated Landing Page Audits

This reference file contains the CRO and dedicated-LP-specific frameworks, principles, and applied research. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

B2B dedicated LPs are uniquely prone to fabricated findings because so much is dynamic:
- Form-builders (HubSpot, Marketo, Pardot, Unbounce, Instapage) with conditional fields
- Lead-magnet preview imagery (whitepaper covers, calculator-screenshots)
- Calculator widgets and interactive demo-tools
- Embedded demo videos (sometimes gated, sometimes inline)
- Customer-logo grids (often static on LPs but verify)
- Trust badges (SOC 2, ISO 27001, GDPR) — JS-rendered
- Exit-intent popups (only triggered on visitor behavior)
- Source-personalization (LinkedIn-source-specific headlines, country-based variants)
- Conditional content (industry-tracked, A/B-test variants)
- Chat widgets and sticky CTAs

**For every finding, verify against screenshots before delivering.**

---

## CRITICAL — Single-purpose page logic

A dedicated LP is FUNDAMENTALLY different from servicepage or homepage:

**Single-CTA dogma APPLIES here:**
- One conversion goal per page
- Distraction-removal expected (nav stripped, sidebar removed)
- Secondary CTAs only as exit-intent or fallback for non-converters
- Unbounce 1:1 attention ratio standard
- "Or browse other pages" thinking is a finding (anti-pattern)

**Recommendations valid for multi-purpose pages (homepage especially) are OFTEN wrong here:**
- "Add more navigation options" → wrong, kills focus
- "Add secondary CTAs" → wrong, dilutes conversion
- "Add service-routing grid" → wrong, this is single-service
- "Add comprehensive content depth" → calibrated; depth must serve the conversion-action, not exhaust the visitor

**This is the OPPOSITE of homepage recommendations.** Be careful not to import homepage-thinking into dedicated LP audits.

---

## CRITICAL — Message-match as #1 lever

Message-match is the most important single optimization on a dedicated LP. Per ConversionXL research, mismatch is the #1 cause of LP-bounce:

**What message-match means:**
- Ad-copy/email-subject promises X → LP headline confirms X
- Source visual style → LP visual style consistent
- Source CTA tone → LP CTA tone consistent
- Source target-audience implied → LP language matches

**Levels of message-match:**
1. **Exact match** (verbatim copy): "Free SOC 2 Audit Checklist" in ad → "Free SOC 2 Audit Checklist" in LP headline
2. **Strong scent** (near-match): "Free security audit" in ad → "Free 30-min security audit" in LP headline
3. **Weak scent** (related-topic): "Improve security" in ad → "Enterprise security platform" in LP headline (visitor has to bridge cognitively — friction)
4. **No scent** (visitor lost): "Free audit" in ad → "Welcome to Brand X — we help companies" in LP headline (catastrophic mismatch)

**Implications:**
- If user provides ad/email/source, message-match is the FIRST analysis priority
- If user does NOT provide source, assess INTERNAL coherence (headline ↔ lead-magnet promise ↔ CTA ↔ form-button all aligned?)
- Mismatch findings are typically ICE 8.5-9.5 — highest-leverage findings on the page

---

## CRITICAL — Decision-maker context (same as B2B servicepage)

B2B dedicated LP visitor is fundamentally different from B2C:
- Decides for organization, often with peers
- Anxieties: ROI-justification, internal-sell, vendor-risk, career-risk
- Trust signals: case studies, named customers, certifications, peer-validation
- Decision-cycle: long (weeks to months) but LP-conversion is single step in journey

**Don't import B2C-LP playbook:**
- Scarcity ("Only 3 spots left!") — counterproductive on enterprise B2B (signals desperation)
- Aggressive urgency countdowns — counterproductive on procurement-driven buyers
- Emotional storytelling — calibrated for B2B (warmer for mid-market, professional for enterprise)
- Pure trust-stripping minimalism — wrong for high-ticket B2B (procurement needs depth)

**B2B-context exceptions where urgency works:**
- Event-LP for registration (real deadline)
- Enterprise pricing "Q4 onboarding window" (real capacity-constraint)
- Webinar registration (real time-bound)

If you recommend scarcity/urgency, it must be REAL and credible to procurement audiences.

---

## CRITICAL — Lead-magnet stage matched to form-length

Form-length on dedicated LP must match the lead-magnet stage:

**Top-funnel (research-stage):**
- Whitepaper, e-book, sector-report, industry benchmark
- Visitor in research-mode, not ready for sales-conversation
- Short form: 3-5 fields (naam + work-email + company + role optional)
- Goal: build pipeline for nurture-sequence

**Mid-funnel (evaluation-stage):**
- ROI-calculator, vendor-comparison guide, evaluation-template
- Visitor evaluating options
- Mid-length form: 5-8 fields (+ company-size + use-case)
- Goal: identify evaluation-stage leads for sales-team

**Bottom-funnel (decision-stage):**
- Demo-request, free-audit, custom-quote, consultation
- Visitor close to decision, sales-team time justified
- Longer form: 8-12 fields with BANT/MEDDIC qualification
- Goal: route qualified leads to right sales-rep

**Mismatch is critical finding:**
- 10-field BANT form on whitepaper download = catastrophic over-friction (kills volume)
- 3-field form on enterprise demo-request = catastrophic under-qualification (wastes sales-time)

---

## CRITICAL — Campaign-type calibration

Each campaign-type has different conversion-rules:

**Form-LP** (vraag offerte, contact-sales):
- BANT-qualified form acceptable
- Direct contact-route to sales
- Primary metric: form-completion
- Conversion 5-15% typical for warm B2B traffic

**Download-LP** (whitepaper, e-book, report):
- Short form (3-5 fields)
- Instant-delivery promise
- Primary metric: form-completion rate
- Conversion 15-30% typical

**Calculator-LP** (ROI calc, savings calc):
- Interactive engagement first, email-gate after
- Mid-funnel positioning
- Primary metric: calculator-completion → email-capture
- Conversion 10-25% typical

**Demo-LP** (request demo):
- BANT-qualified form (5-8 fields)
- Calendar-integration ideal
- Primary metric: demo-booking rate
- Conversion 3-10% typical

**Audit-LP** (free security audit, free SEO audit):
- High-value offer, longer form (7-10 fields)
- Sales-team time-commitment justified
- Primary metric: audit-request rate
- Conversion 5-15% typical

**Trial-LP** (free trial signup):
- Minimal form, product-led growth
- Conversion lift through reduced-friction
- Primary metric: trial-signup rate
- Conversion 5-20% typical

**Event-LP** (webinar, conference registration):
- Time-bound urgency works
- Short form (3-5 fields)
- Primary metric: registration rate
- Conversion 15-40% typical

**Consultation-LP** (kennismaking, strategie-gesprek):
- Higher-touch sales-route
- Qualification form (5-8 fields)
- Primary metric: consultation-booking rate
- Conversion 3-10% typical

---

## Core frameworks (apply across the entire audit)

### Unbounce 1:1 attention ratio
The foundational dedicated-LP principle:
- One conversion goal = one CTA (in primary positioning)
- One target audience = one message
- One source = one message-match alignment
- "Attention ratio" = ratio of links to conversion-goal; 1:1 is ideal for dedicated LPs

### ConversionXL message-match research
Key findings:
- Message-match mismatch is the #1 cause of LP-bounce
- Exact-match headlines outperform near-match by 10-30%
- Visual style consistency (ad-creative ↔ LP-hero) matters
- Audience-context match (LinkedIn role-target ↔ LP audience-language) matters

### Hurst Scent of Information (Mark Hurst)
- Each click in a user journey has "scent" — strength of expected destination
- Strong scent = visitor's prediction matches what they find
- Weak scent = visitor must bridge cognitively (friction)
- Lost scent = bounce

Applied to LP: ad-text creates expectation → LP must confirm expectation in 5-8 seconds.

### Hormozi irresistible-offer principles (B2B-adapted)
Value = (Dream outcome × Perceived likelihood) / (Time delay × Effort and sacrifice)

For B2B dedicated LPs:
- **Dream outcome:** concrete business result of accepting the offer
- **Perceived likelihood:** proof via case-studies, customer-counts, named-customers
- **Time delay:** fast-to-value ("rapport in 24h", "calculator-result instant")
- **Effort and sacrifice:** minimal friction (short form for top-funnel, justified longer form for bottom-funnel)

Value-stacking works in B2B mid-market but must avoid "marketer scammy" tone for enterprise.

### April Dunford B2B positioning (applied to dedicated LP)
On dedicated LP, positioning must be SHARP:
- One best-fit customer (campaign target-audience)
- One key value-claim (campaign promise)
- One differentiator (why this vs alternatives)
- One next step (the CTA)

Multi-purpose servicepages can layer positioning; dedicated LPs must commit.

### Challenger Sale insight-led messaging (applied to LP)
B2B decision-makers respond to insight that reframes their problem:
- Hero copy that reframes: "Marketing teams spend 40% of time on data-cleanup. Stop."
- Lead-magnet promise that delivers insight: "5 hidden costs of [common practice]"
- CTA that promises insight: "Get the security audit no other vendor will do for free"

### MEDDIC framework on dedicated LP
For enterprise demo/audit/consultation LPs:
- **Metrics:** business-impact context field
- **Economic buyer:** decision-maker identification field
- **Decision criteria:** priority dropdown
- **Decision process:** timeline + process field
- **Identify pain:** problem-context (textarea)
- **Champion:** "who else is involved?"

### BANT framework on dedicated LP
For mid-market form-LPs:
- **Budget:** range dropdown
- **Authority:** role/title field
- **Need:** use-case dropdown
- **Timeline:** implementation-timeline

### Forrester B2B buyer research applied to LP
- B2B buyers research 70%+ of decision before contacting sales
- Anonymous research → form-fill at decision-stage
- Dedicated LPs serve specific research-stages — calibrate content depth and form-length accordingly

### MECLABS Conversion Sequence Heuristic on B2B LP
C = 4m + 3v + 2(i−f) − 2a

On B2B dedicated LP:
- **m (motivation):** brought by source (ad clicked = motivated)
- **v (value):** lead-magnet value + outcome promise
- **i (incentive):** lead-magnet itself (Cialdini reciprocity)
- **f (friction):** form-length, unclear value, missing message-match
- **a (anxiety):** vendor-risk, ROI-uncertainty, sales-pressure-fear

### Cialdini's principles on B2B dedicated LP
- **Reciprocity** (HEAVY): lead-magnets are reciprocity-engines
- **Authority:** analyst recognition, certifications, expert-quotes
- **Social proof:** customer-logos, case-study count, named-customers
- **Liking:** less dominant than servicepage; LP focused on offer
- **Commitment-consistency:** multi-step forms create commitment
- **Scarcity:** USE WITH CAUTION (often counterproductive in B2B; OK for real events/capacity)

### Fogg Behavior Model on B2B LP
B = MAT
- MOTIVATION: brought by source (ad/email)
- ABILITY: minimal form-friction + clear next-step
- TRIGGER: above-the-fold CTA + repeated triggers at scroll-points

### Jobs-to-be-Done on B2B dedicated LP
Visitors arrive with ONE job (matched to campaign):
1. **Solve specific problem mentioned in ad** (problem-aware visitor)
2. **Get specific resource promised in ad** (resource-seeker)
3. **Evaluate vendor named in ad** (vendor-evaluation)
4. **Calculate value of solution** (ROI-curious)
5. **Schedule conversation** (sales-conversation-ready)

The page must serve ONE job in depth, not multiple jobs shallow.

**Important Dutch translation:** never use "huren" for JTBD framing. Use "kiezen voor", "inzetten voor", "implementeren om X op te lossen".

---

## Category 1: Message match (#1 priority)

### ConversionXL message-match research
Message-match impacts:
- Bounce rate (mismatch = high bounce)
- Conversion rate (exact-match outperforms by 10-30%)
- Trust formation (mismatch breaks trust within seconds)

### Hurst Scent of Information
Each "scent" element:
- Source promise → LP headline (text match)
- Source visual → LP hero (style match)
- Source CTA tone → LP CTA (tone match)
- Source audience-context → LP audience-language (relevance match)

### Ad-to-page coherence research
Research shows:
- 73% of B2B visitors leave LPs within 8 seconds if mismatch detected
- "Verbatim recall" — exact-text recurring across ad and LP — outperforms paraphrased
- Visual-style consistency between ad-creative and LP lifts conversion 15-25%

### Declarative-thinking patterns
Visitors arrive with DECLARATIVE expectation: "I clicked for [specific thing]"
- LP must confirm declarative expectation in headline
- If LP requires translation ("ad said X, page says Y, must mean same thing"), conversion drops
- Cognitive bridging is friction — eliminated by exact-match

### Best practices (when source provided)
- LP headline contains verbatim or near-verbatim ad-copy phrase
- Lead-magnet promise on LP matches ad-promise exactly
- CTA text on LP matches ad-CTA exactly or near-exactly
- Visual style of LP-hero matches ad-creative
- Audience-language matches ad-audience-targeting

### Best practices (when source NOT provided)
Internal coherence assessment:
- LP-headline matches lead-magnet promise
- Lead-magnet promise matches CTA-button text
- CTA-button text matches form-submit-button text
- Promised outcome on LP matches form-success message (if visible)
- Mismatch within the LP itself is a finding

### Common failures
- LP-headline is brand-name not ad-promise
- Lead-magnet on LP is different from ad-promise
- CTA-button is "Submit" while ad promised "Get Free Audit"
- Visual-style mismatch (corporate LP from playful ad)
- Audience-mismatch (general-business LP from role-targeted ad)

### Campaign-type calibration
- Search Ads (Google) → high-intent keyword match, exact-text matching
- LinkedIn Ads → role-targeted message, audience-language matching
- Email campaigns → subject-line ↔ headline matching
- Sponsored content → publication-tone ↔ LP-tone matching

---

## Category 2: Above-the-fold value proposition & business-impact

### April Dunford positioning on dedicated LP
Hero must answer in 5 seconds:
- WAT outcome (business-impact specific)
- VOOR WIE (campaign target-audience)
- WAAROM (offer-specific differentiator)
- WAT NU (the CTA-action)

### Challenger Sale insight-led on dedicated LP
Best LP heroes lead with insight:
- ❌ "Get a free security audit"
- ✅ "Most security audits miss 3 critical configuration gaps. Ours doesn't. Get yours free."

### Outcome-over-feature framing
- ❌ "AI-powered analytics platform"
- ✅ "Cut quarterly reporting from 3 days to 30 minutes"

### MECLABS clarity-first
On dedicated LP, clarity dominates ALL other factors. Vague hero = catastrophic bounce.

### Best practices
- Headline frames business-outcome or insight, not feature
- Sub-headline specifies audience or lead-magnet detail
- Primary CTA visible above-the-fold
- Lead-magnet preview (cover image, calculator screenshot) visible
- Mobile-first hero (key value-prop in mobile viewport)

### Common failures
- Brand-name hero (visitor doesn't know brand from ad)
- Generic "Welcome to..." copy
- Feature-list stacking
- No outcome specified
- CTA below-the-fold

### Campaign-type calibration
- Download-LP: lead-magnet title + preview + download-CTA hero
- Demo-LP: product-outcome + demo-preview + demo-CTA hero
- Audit-LP: audit-outcome + audit-scope-preview + audit-CTA hero
- Event-LP: event-outcome + speakers + register-CTA hero
- Calculator-LP: calculator-promise + calculator-preview + calculate-CTA hero

---

## Category 3: Friction reduction & distraction management

### Unbounce 1:1 attention ratio
The dedicated-LP signature principle:
- Attention ratio = ratio of links to conversion-goals
- Ideal dedicated LP: 1:1 (one link, one goal)
- Each additional link is statistical leakage
- Standard servicepages have 10:1 to 50:1 (homepage navigation, related-services, blog-links)

### Distraction-to-reaction ratio research
- Each non-conversion-link reduces conversion by 5-15% per link
- Hoofdnavigatie removal lifts conversion 10-25% on B2B dedicated LPs
- Footer-links (privacy, terms) acceptable; "Browse our blog" is anti-pattern
- Sidebar elements (related-articles, recent-posts) actively harm conversion

### Single-purpose-page dogma
On dedicated LP:
- NO hoofdnavigatie (or stripped to logo + minimal)
- NO footer-mega-menu
- NO sidebar links
- NO "Read related..." sections
- One primary CTA repeated at scroll-points
- Exit-paths: only privacy-link, terms-link, contact-fallback (minimal footer)

### Navigation-removal patterns
Conventions:
- Logo links to home (or stays inert on LP)
- No menu visible OR minimal "Contact / Sign in" only
- Sticky CTA replaces traditional sticky-nav
- Footer compact: legal-links only

### Best practices
- Hoofdnavigatie stripped or minimal (logo + contact only)
- Footer compact (legal + privacy + minimal)
- No sidebar elements
- No exit-paths besides legal/privacy
- Single primary CTA repeated 2-4× on long pages
- Sticky CTA on long LPs

### Common failures
- Full hoofdnavigatie on dedicated LP (kills focus)
- Footer mega-menu with 20+ links
- "Related articles" or "Latest blog posts" sections
- Multiple competing CTAs (download whitepaper + watch demo + book call)
- Sidebar with social-share or related-content
- "Or visit our homepage" links

### Calibration notes
- Some B2B brands prefer light-nav for trust ("they're not hiding the menu") — this is calibrated, not absolute
- For high-trust enterprise audiences, stripped-nav can signal "non-corporate landing page" — counterintuitive minor downside
- The 1:1 dogma is for OPTIMIZATION priority, not religious adherence

---

## Category 4: Hero imagery / video (campaign-aligned)

### Forrester B2B buyer imagery research
On dedicated LPs, imagery should:
- Match campaign visual-style (continuity from ad)
- Show lead-magnet preview (for download-LP)
- Show product-screenshot (for demo/trial-LP)
- Show outcome-visualization (for ROI-calculator/audit-LP)

### Demo-video impact research
For demo-LPs specifically:
- Hero demo-video lifts demo-request 20-50%
- Short demo (60-90s muted autoplay) outperforms long demos in hero
- Customer-talking-head video (CFO/director quote) builds trust
- Product-screencast shows what visitor gets

### Product-screenshot vs context-environment
For SaaS demo/trial-LPs:
- Product-screenshot (real UI, real data) dominant
- Context-environment (workplace) for non-software services
- Lead-magnet preview (whitepaper cover, calculator screenshot) for download/calculator-LPs

### Best practices
- Campaign visual continuity (style matches ad)
- Lead-magnet preview prominent (for download-LP)
- Product-screenshot for SaaS demo-LP
- Demo-video optional (60-90s, autoplay-muted, looping)
- Mobile-optimized variants

### Common failures
- Generic stock business-imagery
- No imagery (text-heavy hero)
- Marketing-illustrations instead of product-screenshots
- Lead-magnet preview absent on download-LP
- Hero video autoplaying sound
- Heavy video slowing page load

### Authenticity restraint
A finding may recommend verifying imagery authenticity. A finding may NOT assert specific imagery is stock without strong evidence.

---

## Category 5: Customer logos & social proof grid

### Edelman B2B Trust Barometer (LP-calibrated)
On dedicated LP, customer-logos work differently than on servicepage:
- LP focus = single offer; logo-grid is supporting trust, not dominating
- 5-8 logos optimal on LP (vs 8-12 on servicepage)
- Single-row strip below hero or before form is high-leverage
- Industry-relevance more important than logo-quantity

### Logo-credibility research on LPs
- Logo-strip above-the-fold lifts dedicated-LP conversion 10-25%
- "Trusted by 500+ companies including:" framing works in compact form
- Logos near form (within form-zone) drive form-completion

### "Trusted by [brands]" pattern (compact LP version)
On dedicated LP:
- Single-row logo-strip
- 5-8 logos visible
- Optional: small "Trusted by 500+ companies" line above logos
- Monochrome treatment (consistency + premium feel)

### Best practices
- Logo-strip above or directly below hero, OR adjacent to form
- 5-8 customer-logos (compact)
- Industry-relevance prioritized
- Monochrome treatment
- Customer-count text alongside

### Common failures
- No customer-logos on dedicated LP despite having customers
- Too many logos (>12) diluting focus
- Logos buried in footer
- Generic logos not matching target audience industry

### Authenticity restraint
A finding may recommend verifying customer-logo permission. A finding may NOT claim logos are unauthorized without strong evidence.

### Campaign-type calibration
- Download-LP: logos optional (lead-magnet preview dominates)
- Demo-LP: logos critical (peer-validation drives demo-booking)
- Audit-LP: logos critical (vendor-trust drives audit-acceptance)
- Trial-LP: logos optional (product-demo dominates)
- Event-LP: speaker-logos + sponsor-logos relevant

---

## Category 6: Lead-magnet propositie & irresistible-offer

### Cialdini reciprocity in B2B LP context
Lead-magnets ARE the reciprocity-engine on dedicated LP:
- Visitor gives contact info → receives value
- High-value lead-magnet → trust + reciprocity → warmer downstream sales-cycle
- Low-value or vague lead-magnet → distrust + bounce

### Hormozi irresistible-offer (B2B-adapted)
For dedicated LP lead-magnet, the value-equation:

Value = (Dream outcome × Perceived likelihood) / (Time delay × Effort and sacrifice)

**Strong B2B lead-magnet:**
- ✅ "47-page Enterprise SOC 2 Readiness Checklist — used by 200+ CISOs. Delivered to inbox in 60 seconds."
  - Dream outcome: SOC 2 readiness
  - Perceived likelihood: 200+ CISOs proof
  - Time delay: 60 seconds
  - Effort: single email field

**Weak B2B lead-magnet:**
- ❌ "Download our free guide to learn more"
  - Dream outcome: vague
  - Perceived likelihood: no proof
  - Time delay: unclear
  - Effort: unclear

### Marketing Sherpa B2B lead-magnet patterns
High-converting B2B lead-magnets:
1. **Specific & quantified** ("47-page checklist" vs "comprehensive guide")
2. **Time-anchored** ("In your inbox in 60 seconds" vs "We'll be in touch")
3. **Proof-backed** ("Used by 200+ CISOs" vs general claims)
4. **Outcome-specific** ("SOC 2 readiness" vs "security insights")
5. **Preview-enabled** (cover image, ToC, sample-page visible)

### Gated-content economics
Gating decisions:
- Top-funnel content (educational): light gate (email only)
- Mid-funnel content (evaluation): mid gate (email + company + role)
- Decision-funnel content (demo, audit): full BANT gate

Mismatch (heavy gate on top-funnel content) kills lead-volume disproportionately.

### Best practices
- Lead-magnet titled SPECIFICALLY ("47-page Enterprise SOC 2 Checklist")
- Time-anchor visible ("Delivered in 60 seconds")
- Proof-backing (customer-count, named-companies who used it)
- Preview-image (cover, ToC, sample pages)
- Form-length matched to lead-magnet-stage
- Outcome-clarity (what visitor achieves with this)

### Common failures
- Vague lead-magnet ("our guide", "our resources")
- No time-anchor
- No proof-backing
- No preview-image
- Generic title ("Free Guide to Marketing")
- Form-length mismatched to stage

### Campaign-type calibration
- Download-LP: lead-magnet IS the entire LP, dominate hero
- Demo-LP: demo itself is the offer, preview-video helps
- Audit-LP: audit-scope is the offer, sample-report-preview helps
- Calculator-LP: calculator is the offer, calculator-screenshot helps
- Event-LP: event-content + speakers ARE the offer

---

## Category 7: Lead-form design met campaign-aligned kwalificatie

### Form-length matched to lead-magnet stage (CRITICAL)
The single most important form-design decision on B2B LP:

**Top-funnel form (3-5 fields):**
- Whitepaper, e-book, sector-report
- Fields: work-email, naam, company (optional: role)
- Just enough for nurture-sequence

**Mid-funnel form (5-8 fields):**
- Calculator-result, vendor-comparison guide
- + role + company-size + use-case

**Bottom-funnel form (8-12 fields):**
- Demo-request, free-audit, custom-quote
- Full BANT/MEDDIC qualification

### CXL form-research (B2B-adapted)
- Standard "every field costs ~7-11%" applies
- BUT B2B context: lead-quality often more important than volume
- Form-shortening recommendation must specify CAC + sales-capacity context

### Baymard form-field research
- Labels above inputs (not placeholder-only)
- Real-time validation outperforms submit-time
- Single-column on mobile
- Dropdowns for routable data (industry, company-size, use-case)
- Required-only marking (don't mark every required field with asterisks)

### BANT framework in form (for mid-bottom-funnel LPs)
- Budget: tier dropdown ("Under €5k / €5-25k / €25k+ / Not yet defined")
- Authority: role/title field
- Need: use-case dropdown
- Timeline: implementation-timeline

### MEDDIC framework in form (for enterprise LPs)
- Metrics: business-impact context
- Economic buyer: decision-maker identification
- Decision criteria: priority dropdown
- Decision process: timeline + process
- Identify pain: problem-context (textarea)
- Champion: "who else is involved?"

### Best practices
- Form-length matched to lead-magnet-stage (CRITICAL — this is the #1 form decision)
- Labels above fields
- Real-time validation
- Single-column on mobile
- Dropdowns for routable data
- Action-oriented submit-button matching CTA promise
- Privacy reassurance near submit
- BANT/MEDDIC where appropriate (calibrated to stage)

### Common failures
- 10-field BANT form on whitepaper download (kills conversion 60-80%)
- 3-field form on enterprise demo-request (under-qualifies leads)
- Placeholder-only labels
- Submit-time validation only
- Asterisks on every field
- Generic "Submit" CTA (no campaign-match)
- Multi-column on mobile

### Lead-quality vs lead-volume calibration (always state when recommending form-changes)
- "Remove fields X, Y" → "expect +N% form-completion, possible -M% lead-quality; calibrate to current SDR/AE capacity and CAC"
- "Add fields X, Y" → "expect -N% form-completion, possible +M% lead-quality; reduces wasted sales-cycle"

---

## Category 8: Trust signals & B2B credibility (compact)

### B2B trust-signal calibration on focused pages
On dedicated LP, trust signals are SUPPORTING (not dominating):
- Compact strip (3-5 elements)
- Adjacent to form or below hero
- Relevant-to-anxiety-target

**For audit-LP and security-related LPs:**
- SOC 2 Type II badge
- ISO 27001 badge
- GDPR/AVG compliance
- Compact: 3-4 critical badges

**For consultancy/services LPs:**
- Years operating
- Named industry awards
- Branche-organisatie lidmaatschap
- KvK/BTW in footer

**For SaaS LPs:**
- Customer-count ("Trusted by 500+ companies")
- Uptime SLA (for managed/infrastructure)
- Compliance badges

### Cialdini authority (compact)
On LP, authority signals work as TRUST RAILS along the conversion path:
- Above-the-fold: customer-count or named-customer
- Near form: certifications relevant to anxiety
- Footer: legal trust (KvK, BTW, privacy)

### Best practices
- 3-5 critical trust signals visible
- Trust-strip near form OR below hero
- Anxiety-targeted (security-anxieties → security badges; ROI-anxieties → metric proofs)
- Industry-relevant only (no generic logos)
- Compact, not dominating

### Common failures
- Trust signals dominating instead of supporting (LP becomes trust-wall, not offer-page)
- Generic certifications without context
- Compliance badges absent on enterprise security-LPs
- "Years of experience" without specifics

---

## Category 9: Case studies & ROI-bewijs (compact)

### Forrester case-study impact research (LP-calibrated)
On dedicated LP, case-studies and ROI-proof are FOCUSED, not exhaustive:
- 1-2 case-studies maximum on LP (vs 2-4 on servicepage)
- Each must directly support the campaign-promise
- Industry-matched to target-audience
- Specific metric outcome

### Compact case-study card on LP
Structure:
- Customer logo + name + industry
- Person quoted with role
- Concrete metric outcome (one number)
- One-sentence story
- Optional: "Read full case →"

### Outcome-driven B2B (compact)
- One key ROI-metric prominent
- Customer-averaged metric where possible
- Industry-benchmarked where possible

### ROI-calculator engagement (for calculator-LPs)
- Calculator IS the offer; lead-magnet propositie category dominates
- Result-gating (email for full result) ethical when value-clear

### Best practices
- 1-2 case-studies maximum (focused subset)
- Each with named customer + concrete metric
- Industry-matched
- One key ROI-metric prominent
- Customer-averaged ("Customers see avg 47% reduction")

### Common failures
- Case-studies section dominating (LP becomes case-page instead of offer-page)
- Too many cases (>3) diluting focus
- Generic "happy customers" without specifics
- Case studies not aligned to campaign-promise

### Campaign-type calibration
- Download-LP: case-studies optional (lead-magnet dominates)
- Demo-LP: 1-2 cases relevant (peer-validation drives demo-booking)
- Audit-LP: 1-2 cases critical (proof of audit-value)
- Calculator-LP: ROI-metrics dominant, cases supporting
- Trial-LP: cases optional (product-demo dominates)

---

## Category 10: Single CTA strategy & secondary fallback

### Fogg Behavior Model on B2B LP CTA
- MOTIVATION delivered by source (ad/email)
- ABILITY = minimal form-friction
- TRIGGER = visible primary CTA at all scroll-points

### Single-CTA dogma applies
On dedicated LP:
- ONE primary CTA repeated at scroll-points
- NO competing CTAs
- Secondary CTA only as exit-intent fallback or for non-converters
- Sticky CTA on long pages

### Exit-intent secondary-fallback patterns
Acceptable secondary CTAs:
- Exit-intent popup with lower-friction alternative ("Not ready for demo? Download checklist")
- Sticky bottom-bar with phone option for high-intent non-converters
- "Save for later — email me this page" mobile-fallback

### Unbounce attention-ratio compliance
- Above-the-fold: ONE CTA visible
- Scroll-points: ONE CTA repeated
- Footer: ONE CTA + legal (no nav)
- Attention-ratio target: 1:1 to 3:1 maximum

### Best practices
- Primary CTA visible above-the-fold
- Same primary CTA repeated at 2-3 scroll-points on long LPs
- Sticky mobile CTA
- Action-oriented copy matching lead-magnet promise
- Optional exit-intent secondary-fallback
- NO multi-CTA above-the-fold

### Common failures
- Multi-CTA chaos (3-4 competing CTAs)
- "Or watch demo" alongside primary download-CTA (dilutes focus)
- Generic "Submit" or "Contact us"
- CTA below-the-fold only
- Sticky CTA absent on mobile
- Hoofdnavigatie not stripped (effective multi-CTA via nav)

### Campaign-type calibration
- Download-LP: "Download free [magnet] →" primary
- Demo-LP: "Schedule 30-min demo →" primary
- Audit-LP: "Get free [audit-type] →" primary
- Calculator-LP: "Calculate your [outcome] →" primary, then email-gate after
- Event-LP: "Register free →" primary

---

## Category 11: Mobile experience

### B2B mobile-CTR-to-LP-conversion patterns
B2B paid-traffic mobile patterns:
- LinkedIn Ads: 40-60% mobile clicks → low conversion mobile (research-mode visitor)
- Google Search Ads: 30-50% mobile → mid conversion mobile (intent-driven)
- Email campaigns: 50-70% mobile clicks → mobile-to-desktop handoff common

### Baymard mobile research (B2B-context)
- Mobile-LP must be functional, not just responsive
- Form mobile-completable but desktop-handoff option valuable
- Long-form content acceptable mobile (research-mode visitor)
- "Email me this page" mobile-CTA captures mobile-research → desktop-conversion

### Mobile form-optimization on B2B LP
- Single-column always
- Large fields, large submit-button
- Mobile-keyboards for input-type
- Tap-to-call for phone numbers (where applicable)
- "Save / email this page" option

### Best practices
- Mobile-first hero (key value-prop + CTA in viewport)
- Lead-magnet preview mobile-visible
- Form mobile-optimized (single-column, large fields, mobile-keyboards)
- Sticky mobile CTA on long pages
- "Email me this page" mobile-fallback
- Fast page load (Core Web Vitals)
- Trust-signals mobile-visible

### Common failures
- Desktop-only optimization
- Hero requires zoom on mobile
- Form ported desktop-to-mobile without redesign (multi-column)
- Customer-logos invisible on mobile
- Heavy video slowing mobile load
- No mobile sticky CTA
- No mobile fallback for high-friction conversion

---

## Brand and campaign calibration notes

Always recalibrate by brand snapshot AND B2B-service-type AND deal-size AND campaign-type AND traffic-source:

**Example: Headline**
- LinkedIn Ad targeting Marketing Directors → "Marketing Directors: Cut campaign-build time from 3 weeks to 3 days"
- Google Search for "soc 2 audit" → "Free SOC 2 Audit — 47-page checklist used by 200+ CISOs"
- Email to existing leads → "[Name], the 2025 sector-benchmark you requested"
- Sponsored content on industry pub → "How [target-industry] companies are reducing [pain] by 47%"

**Example: Form-length**
- Top-funnel whitepaper from LinkedIn Ads → 3 fields (email, name, company)
- Mid-funnel calculator from Google Ads → 5 fields (+ role + company-size)
- Bottom-funnel enterprise demo from email → 8-12 fields (full BANT/MEDDIC)

**Example: Customer-logos**
- Enterprise demo-LP → 6-8 enterprise logos prominently displayed
- Whitepaper download-LP → 3-5 logos optional, focus on lead-magnet
- Trial-LP → product-demo dominates, logos optional

Recommendations that don't match brand AND B2B-service-type AND deal-size AND campaign-type AND traffic-source zijn fout.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites a specific principle, study, or source
- [ ] Recommendation is concrete (exact copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric is named (form-completion / MQL-rate / cost-per-lead / SQL-conversion)
- [ ] ICE justified by I/C/E breakdown
- [ ] Recommendation matches brand snapshot AND B2B-service-type AND deal-size AND campaign-type
- [ ] Single-purpose page logic respected (single-CTA APPLIES here)
- [ ] Message-match analyzed where source provided, or internal-coherence assessed
- [ ] Decision-maker context respected (no consumer-style recommendations)
- [ ] Form-length calibrated to lead-magnet-stage + deal-size + CAC + sales-capacity
- [ ] Lead-quality vs lead-volume tradeoff explicit in form recommendations
- [ ] Scarcity/urgency recommendations calibrated (often counterproductive in B2B)
- [ ] Distraction-removal logic applied
- [ ] Dutch output: no "huren" check
- [ ] No authenticity claims about logos/case-metrics/certifications without strong evidence

If any box unchecked, rework or remove the finding before delivering.
