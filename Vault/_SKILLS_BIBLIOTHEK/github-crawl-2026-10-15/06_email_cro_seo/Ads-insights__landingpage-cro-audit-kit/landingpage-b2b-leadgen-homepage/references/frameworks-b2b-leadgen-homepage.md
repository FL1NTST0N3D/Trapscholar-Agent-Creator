# Frameworks for B2B Leadgen Homepage Audits

This reference file contains the CRO and B2B-homepage-specific frameworks, principles, and applied research. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

B2B leadgen homepages are uniquely prone to fabricated findings because so much is dynamic:
- Hero carousels (which slide is current visitor seeing?)
- Customer-logo grids (often rotating carousels with limited subset visible)
- Service-card grids (sometimes JS-rendered or conditionally shown)
- Case-study cards (often filtered by industry/role)
- G2/Capterra/Trustpilot review widgets (JS-loaded)
- ROI-calculators and interactive demo-widgets
- Embedded demo videos
- Pricing display ("Contact us" vs visible tiers — conditional rendering common)
- Trust badges (SOC 2, ISO 27001, GDPR) often JS-rendered
- Chat widgets (Drift, Intercom, Qualified) with conditional triggers
- A/B-test variants from third-party tools (Optimizely, VWO, native split-test)
- Industry/country-based conditional content

**For every finding, verify against screenshots before delivering.**

---

## CRITICAL — Multi-purpose entry-point logic

B2B homepages are FUNDAMENTALLY different from single-purpose pages (dedicated LP, contactpage). Recommendations valid for single-purpose pages may be the wrong call:

**Do NOT automatically recommend on B2B homepages:**
- "Single primary CTA" — multi-CTA is CORRECT on homepages serving multiple visitor-jobs
- "Hide hoofdnavigatie" — navigation IS the routing on multi-service homepages
- "Remove secondary paths" — secondary paths serve different visitor-jobs
- "Apply 1:1 attention ratio" — that's dedicated-LP-logic, wrong for homepage
- "Add aggressive scarcity/urgency" — wrong for first-touch B2B context (creates anxiety, signals desperation)

**DO recommend (when appropriate):**
- Multi-path CTA strategy matched to visitor-jobs (demo / contact / download / login)
- Clear service-routing (cards, grid, or navigation)
- Customer-logos prominent (peer-validation for first-touch)
- Trust signals for first-time-visitor evaluation
- Multi-stakeholder content layering (when audience is mixed)

The multi-purpose rule trumps single-CTA dogma on this page-type.

---

## CRITICAL — Decision-maker context (same as B2B servicepage)

B2B homepage visitor is fundamentally different from B2C:
- Decides for organization, often with peers
- Anxieties: ROI-justification, internal-sell, vendor-risk, career-risk
- Trust signals: case studies, named customers, certifications, peer-validation
- Decision-cycle: long (weeks to months)

**Don't import B2C-homepage playbook:**
- Scarcity ("Limited spots") — counterproductive on enterprise B2B
- Aggressive urgency countdowns — wrong for procurement-driven buyers
- Reviews-prominence above customer-logos — wrong for B2B (case-studies dominate)
- "We love our customers" warmth-driven copy — calibrate for B2B formality

---

## CRITICAL — Case studies and named-customer logos dominate over reviews

For B2B homepage, named-customer proof is heavier than aggregated reviews:

**Why case studies > reviews on B2B homepage:**
- B2B decision-makers want named-companies-like-theirs as proof, not anonymous "users"
- Customer-logo grid = brand-presence at-a-glance trust
- Specific metrics (saved X hours, increased Y revenue, reduced Z cost) > generic 5-star ratings
- Named contact (CFO of Brand X) > anonymous "Sarah M."

**Reviews still relevant but lichter:**
- G2/Capterra reviews for SaaS (peer-validation in software-buying)
- Trustpilot for B2B services (lower weight than B2C but still relevant)
- Named B2B reviews ("Reviewer: Director of Marketing, mid-market SaaS") > anonymous stars

**Implications for findings:**
- Logo-wall absence above-the-fold = critical finding
- Case-study absence = critical finding
- Generic anonymous reviews without B2B-context = low impact finding
- "Trusted by [bekende namen]" pattern is high-leverage trust element

---

## CRITICAL — Multi-stakeholder content layering (calibrated weight)

On B2B homepage, different visitor-roles arrive simultaneously:
- **Economic buyer** (CFO, MD): pricing-impact, business-outcome content
- **Technical buyer** (IT, engineering): integration, security, compliance content
- **End-user** (specialist): usability, workflow content
- **Champion** (internal sponsor): shareable-proof, internal-sell collateral

**Calibrated category weight (Important/Nice default):**
- Multi-stakeholder content layering on homepage matters BUT findings here typically Important (ICE 4-6), not automatic Critical
- Don't over-engineer findings — most homepages don't need full role-segmentation
- Push to Critical (7+) only if visible active mismatch: bv. enterprise-targeting homepage met ALLEEN end-user content (technical-buyer en economic-buyer voelen geen aansluiting)

**Practical guidance:**
- Look for: are different visitor-roles served by different page-sections?
- Don't force role-segmentation if audience is mostly single-role
- Mark category as "checked, brief observation" if no significant finding

---

## CRITICAL — Lead-magnet propositie on homepage (calibrated weight)

Lead-magnets on B2B homepage are entry-points among other CTAs, not the dominant offer:

**Calibrated category weight (Important default):**
- Lead-magnet propositie on homepage typically Important (ICE 5-7)
- Push to Critical (7+) only if homepage is clearly lead-magnet-driven brand strategy and lead-magnet ontbreekt OF catastrofaal slecht is gepositioneerd
- Many B2B homepages function fine without homepage-level lead-magnets (demo/contact dominant)

**When lead-magnet on homepage matters:**
- SaaS with content-marketing strategy: whitepaper + report-downloads visible
- Consultancy: sector-benchmark reports + free audit-offers
- Managed services: assessment-tool + security-audit downloads
- Enterprise with long sales-cycle: high-value lead-magnets for nurture-pipeline

**When lead-magnet less critical:**
- Self-service SaaS low-ticket (trial-CTA dominant)
- Professional services (relationship-driven, kennismakingsgesprek dominant)

---

## CRITICAL — B2B-service-type calibration

Recommendations vary heavily by B2B-service-type:

**B2B SaaS low-ticket (€50-500/m):**
- Self-service trial possible
- Product-screenshots dominant in hero
- Pricing transparency dominant
- Reviews (G2, Capterra) more relevant on homepage
- Trial-CTA primary, demo-CTA secondary

**B2B SaaS mid-ticket (€500-5k/m):**
- Sales-assisted, demo-required
- Product-screenshot + demo-video hero
- Pricing visible with "Enterprise contact us"
- Case studies + reviews balanced
- Demo-CTA primary

**B2B SaaS enterprise (€5k+/m):**
- Fully sales-driven
- Multi-stakeholder content layering most relevant
- Customer-logos above-the-fold critical
- Named-customer case studies dominant
- "Contact sales" pricing standard
- Demo-CTA primary, "Talk to sales" secondary

**B2B consultancy / agency:**
- Named-expertise critical
- Case studies dominant on homepage
- Sector-vertical expertise visible
- "Vraag offerte" or "Plan kennismaking"-CTA primary

**B2B professional services** (accountancy, legal, financial advisors):
- Relationship-driven, long sales-cycle
- Credentials + sector-expertise dominant
- Named partners visible
- "Plan kennismaking"-CTA primary

**B2B managed services** (IT, infrastructure, security):
- Compliance + security badges critical
- Customer-portfolio visible
- Uptime/SLA proof
- "Audit"-CTA + "Contact"-CTA mixed

---

## Core frameworks (apply across the entire audit)

### April Dunford B2B positioning
B2B homepages must position for:
- **Best-fit customer** (specific industry, role, company-size)
- **Competitive alternatives** (visitor compares; homepage must address)
- **Unique attributes** (what only this brand does)
- **Value enabled by attributes** (concrete outcomes)
- **Market category** (frame correctly for buying motion)

### Challenger Sale (Dixon & Adamson)
B2B decision-makers respond to insight-led messaging:
- Teach: lead with insight that reframes the visitor's problem
- Tailor: speak to specific industry/role
- Take control: confident assertion, not soft suggestion

Applied to homepage hero: reframe the problem, don't just list features.

### Forrester B2B buyer research
Key findings applied to homepage:
- B2B buyers research 70%+ of decision before contacting sales
- They consume 3-7 content pieces on average before form-fill
- They prefer self-service for early-stage research
- Anonymous research → form-fill at decision-stage
- Homepage often serves multiple stages simultaneously

### Edelman B2B Trust Barometer
B2B trust on homepage comes from:
- Peer-validation (customers like me) > general reviews
- Third-party validation (analyst reports, awards from B2B-specific sources)
- Certifications (SOC 2, ISO 27001, GDPR compliance) carry heavy weight
- Customer logo-presence drives "they trust them, so I can trust them"

### Cialdini's principles on B2B homepage
- **Authority** — analyst recognition, certifications, expert-quotes
- **Social proof** — customer-logos, case studies, customer-counts ("Trusted by 500+ companies")
- **Liking** — calibrated to brand-formality (warmer for mid-market, professional for enterprise)
- **Reciprocity** — lead-magnets as entry-points
- **Commitment-consistency** — multi-step engagement creates commitment
- **Scarcity** — typically NOT appropriate (signals desperation; exception: real events/capacity)

### MECLABS Conversion Sequence Heuristic on B2B homepage
C = 4m + 3v + 2(i−f) − 2a

On B2B homepage:
- **m (motivation):** variable by visitor-stage (research vs evaluation vs decision)
- **v (value):** business-impact + competitive-alternative differentiation
- **i (incentive):** lead-magnet, demo, free trial
- **f (friction):** unclear positionering, missing proof, complex navigation, hidden pricing
- **a (anxiety):** vendor-risk, ROI-uncertainty, integration-risk

### Fogg Behavior Model on B2B homepage
- MOTIVATION: build via insight-led copy + proof-density
- ABILITY: clear next-step + service-routing + multiple paths
- TRIGGER: above-the-fold CTA + repeated triggers at proof-density-peaks

### Nielsen Norman heuristics applied to B2B homepage
- **#1 Visibility of system status** — brand-positioning visible, services visible
- **#2 Match real world** — industry/role-appropriate language
- **#3 User control and freedom** — multi-path navigation
- **#5 Error prevention** — clear service-card scoping
- **#6 Recognition over recall** — all services visible, not hidden in menus
- **#8 Aesthetic and minimal design** — balanced against content depth

### Mark Hurst Information Scent
Each navigation item or service-card is a "scent" leading to the right destination:
- Generic labels ("Solutions") have weak scent
- Specific labels ("Marketing Automation", "Sales Enablement", "Customer Success") have strong scent

### Hormozi value-equation (B2B-adapted)
For lead-magnets on homepage:
Value = (Dream outcome × Perceived likelihood) / (Time delay × Effort and sacrifice)

### Jobs-to-be-Done on B2B homepage
B2B visitors on homepage are doing ONE of:
1. **Brand-evaluation** — "Wat doet dit bedrijf, is dit voor mij?" (first-time)
2. **Service-finding** — "Ik zoek service X, waar staat dat?"
3. **Trust-verification** — "Is dit een geloofwaardige vendor?"
4. **Solution-research** — "Ik onderzoek mijn opties in deze categorie"
5. **Lead-magnet research** — "Ik zoek content voor m'n probleem"
6. **Existing-customer access** — "Ik wil inloggen / support"
7. **Champion-collateral** — "Ik wil shareable info om intern te delen"

Each job needs different page support. A high-converting B2B homepage serves multiple jobs without forcing one path.

**Important Dutch translation:** never use "huren" for JTBD framing. Use "kiezen voor", "inzetten voor", "implementeren om X op te lossen".

---

## Category 1: Above-the-fold value proposition & business-impact positionering

### April Dunford B2B positioning on homepage
The hero must answer in 5 seconds:
- WAT (service in business-impact terms)
- VOOR WIE (target industry/role/company-size)
- WAAROM (vs alternatives, vs status quo)
- WAT NU (the CTA — typically demo / contact / trial)

### Challenger Sale insight-led messaging
Best B2B homepage heroes lead with INSIGHT that reframes:
- ❌ "Best-in-class marketing automation platform"
- ✅ "Marketing teams spend 40% of time on data-cleanup. Stop. Here's what automation actually saves."

### Outcome-over-feature framing
B2B buyers respond to outcomes, not features:
- ❌ Feature: "AI-powered analytics dashboard"
- ✅ Outcome: "Cut quarterly reporting from 3 days to 30 minutes"

### MECLABS clarity-first
On homepage hero: clarity (v-factor) dominates. Visitor must immediately understand WAT, VOOR WIE, WAT-LEVERT-HET-OP.

### Best practices
- Headline frames business-outcome, not feature
- Sub-headline specifies audience (industry/role/size)
- One credibility-anchor visible (customer-count, named-customer, analyst-recognition)
- Primary CTA matched to dominant visitor-stage
- Authentic, service-relevant imagery

### Common failures
- Generic "Best-in-class solution for..." copy
- Feature-list hero ("AI · Automation · Analytics")
- Brand-name as headline
- No credibility anchor in hero
- Buzzword overload ("synergize", "leverage", "transform")

### B2B-service-type calibration
- SaaS low-ticket: outcome + trial-CTA + product-screenshot hero
- SaaS enterprise: outcome + demo-CTA + customer-logos hero
- Consultancy: outcome + case-study-led + offerte-CTA
- Professional services: credentials-led + consult-CTA

---

## Category 2: Service-routing & navigation clarity

### Nielsen Norman recognition-over-recall (heuristic #6)
On multi-service B2B homepages, visitors should not have to remember what's offered. ALL services should be visible — through navigation, service-cards, or both.

### Mark Hurst Information Scent
Each navigation item or service-card is a "scent":
- Generic labels ("Solutions", "Wat wij doen") have weak scent
- Specific labels ("Marketing Automation", "Sales Enablement", "Customer Onboarding") have strong scent

### B2B service-navigation patterns
- Service-card grids on B2B homepage outperform menu-only routing by 15-30% on multi-service sites
- 3-6 service-cards optimal (B2B fewer than B2C consumer-service-providers)
- Icon + service-name + 1-line outcome-description per card
- Service-cards with "Learn more →" CTA per card lift CTR per card

### Best practices
- Service-cards visible on homepage (3-6 services typical for B2B)
- Each card: icon + name + 1-line outcome-description + CTA
- Navigation includes service-categories
- Service-names in business-outcome language (not internal-jargon)
- Clear visual hierarchy between services

### Common failures
- Hidden services behind "Solutions" megamenu only
- Service-names in internal-jargon
- Service-card grid with 8+ items
- Service-cards with name-only (no description)
- Generic icons

### B2B-service-type calibration
- Single-service brand: service-routing minder relevant
- Multi-service SaaS (3-6 services): service-card grid dominant
- Consultancy with vertical-expertise: industry-routing relevant
- Managed services: service-tier-routing acceptable

---

## Category 3: Customer logos & social proof grid

### Edelman B2B Trust Barometer — logo credibility
B2B "Trusted by [brands]" pattern is one of the highest-leverage trust elements:
- Named brands visitor recognizes = instant trust transfer
- Industry-relevant brands > generic Fortune 500
- 6-12 logos in a strip is the sweet spot
- Position: hero or directly below hero

### Logo-credibility research
Specific findings:
- Logo-wall above-the-fold lifts B2B homepage conversion 15-30% on first-time visitors
- Industry-specific logos (peer-companies) outperform diverse-industry mix for niche audiences
- "As featured in" press-logos work alongside customer-logos
- Logo-quality matters: high-res monochrome > low-res mixed-color

### "Trusted by [bekende namen]" pattern impact
This single pattern is the most concise high-impact trust signal in B2B:
- Visitor sees [Bekende klant] → "they're legit"
- 6-12 logos optimal on homepage (vs 5-8 on dedicated LP)
- Hero-zone or directly-below-hero positioning
- Optional: "Trusted by 500+ companies including:" tekst

### Best practices
- Logo-strip above or directly below hero
- 6-12 customer-logos visible
- Industry-relevant logos prioritized
- Monochrome treatment (consistency + premium feel)
- Customer-count text alongside

### Common failures
- No customer-logos visible despite having customers
- Logos buried in footer or below-the-fold
- Mix of customer logos and partner logos
- Generic logos that don't match audience industry
- Logo-carousel with only 1-2 visible at a time

### Authenticity restraint
A finding may recommend verifying customer-logo permission. A finding may NOT claim logos are unauthorized without strong evidence.

### B2B-service-type calibration
- SaaS enterprise: customer-logos critical, often above-the-fold
- Consultancy: customer-logos + named-client list
- Professional services: named-clients + sector-logos
- Early-stage/startup: customer-counts beat sparse-logos

---

## Category 4: Case studies & named-customer proof

### Forrester case-study impact research
- 73% of B2B decision-makers cite case studies as critical content in evaluation
- Named-metric case studies outperform anonymous-outcome by 5-7x
- Industry-specific case studies (visitor's industry) lift relevance-perception 40-60%
- Video case studies (customer talking head) outperform text-only by 30-50%

### Cialdini social proof in B2B context
B2B social proof is named, specific, and metric-driven:
- Named customer (company name, person's name, role)
- Specific outcome (saved X hours, increased Y revenue, reduced Z cost)
- Verifiable details (industry, company-size, use-case)

### Named-customer testimonials with metrics
Structure of high-converting case-study card on homepage:
1. Customer logo + company name + industry/size
2. Person quoted with name + role
3. Specific metric outcome (concrete number)
4. Short story (1-2 sentences)
5. "Read full case study →" CTA

### Best practices
- 2-4 case-study highlights on homepage
- Each with named customer + metric + quote
- Industry-tagged for multi-industry pages
- Video case study optional (high-leverage)
- Link to full case studies

### Common failures
- Generic "happy customers" without specifics
- Case studies without metrics (just praise)
- Anonymous case studies ("Fortune 500 financial services company")
- Stock-quote testimonials
- Outdated case studies (3+ years)

### Authenticity restraint
A finding may recommend verifying case-study authenticity. A finding may NOT claim case-metrics are inflated or testimonials are fabricated without strong evidence.

### B2B-service-type calibration
- SaaS: 2-4 case studies with quantitative metrics (hours saved, revenue impact)
- Consultancy: 2-3 detailed case studies with project-outcome stories
- Professional services: 1-2 deep client-stories with named partners
- Managed services: uptime/reliability metrics + customer-named

---

## Category 5: ROI/impact-bewijs en metrics

### Outcome-driven B2B research
B2B decision-makers need concrete ROI proof to justify internally:
- Quantified outcomes ("47% reduction in X") beat qualitative claims
- Time-to-value metrics ("payback in 3 months") drive urgency
- Comparison-baselines ("vs industry-average") strengthen claim
- Customer-aggregate metrics ("Customers see avg 47% reduction") on homepage

### Hormozi value-equation on homepage
For homepage ROI-proof:
- **Dream outcome:** concrete business result
- **Perceived likelihood:** customer-aggregate metrics + case-study proof
- **Time delay:** time-to-value clarity
- **Effort and sacrifice:** implementation effort transparency

### ROI-calculator engagement patterns
- Interactive ROI calculators on homepage lift demo-conversion 15-30%
- Calculator-result gating (email for full result) is effective lead-magnet
- Industry/role-specific calculators outperform generic

### Best practices
- ROI/impact section with 3-4 key metrics
- Customer-averaged metrics
- Time-to-value visible
- Optional: interactive ROI calculator
- Comparison baselines

### Common failures
- ROI section absent on homepage
- Vague claims ("dramatic improvement") without numbers
- Metrics without source-customers
- Time-to-value vague or absent

### B2B-service-type calibration
- SaaS: hours-saved, revenue-impact, error-reduction metrics
- Consultancy: project-outcome metrics + ROI multiplier
- Professional services: cost-savings + risk-reduction
- Managed services: uptime, security-incident-reduction

---

## Category 6: Trust signals & B2B credibility

### Cialdini authority in B2B
B2B authority signals on homepage:
- Analyst recognition (Gartner Magic Quadrant, Forrester Wave)
- Industry awards (relevant to vertical)
- Certifications (SOC 2 Type II, ISO 27001, HIPAA, GDPR)
- Compliance badges (PCI DSS, SOX where applicable)
- Founder/team credentials
- Press mentions in B2B-relevant publications

### Edelman Trust Barometer — verifiable signals
B2B trust on homepage:
- **Years operating** — "Sinds 2014" beats "Jarenlange ervaring"
- **Customer count** — specific number
- **Industry membership** — branche-organisatie lidmaatschap
- **Press / media mentions** — concrete sources
- **Awards / recognitions** — with year and issuer

### Certifications and compliance signals
Critical for B2B (especially enterprise):
- **SOC 2 Type II** — security audit baseline for SaaS
- **ISO 27001** — info-security management
- **GDPR / AVG compliance** — EU privacy
- **HIPAA** — healthcare US
- **Industry-specific** — depends on vertical

These appear typically in footer-strip + dedicated security/compliance section.

### Best practices
- Trust-strip near hero (customer-count + key cert)
- Dedicated security/compliance section
- Analyst-recognition badges where applicable
- Industry awards visible
- Press logos (B2B-relevant only)

### Common failures
- Generic certification badges without context
- Compliance section absent on enterprise-targeting page
- Self-claims without third-party validation
- Press-logos from irrelevant publications

### Note: Reviews calibrated lighter on B2B homepage
Reviews appear in this category as one trust element, not primary:
- G2/Capterra reviews relevant for SaaS
- Trustpilot reviews lighter weight than for B2C
- Named-reviewer testimonials more valuable than star-ratings
- Reviews work alongside case-studies, not in replacement

---

## Category 7: Lead-magnet propositie op homepage

### Cialdini reciprocity in B2B
Lead-magnets are reciprocity-engines:
- High-value lead-magnet → trust + reciprocity → warmer downstream sales-cycle
- Low-value or vague lead-magnet → distrust

### Marketing Sherpa B2B lead-magnet patterns
High-converting B2B homepage lead-magnets:
1. **Industry benchmark reports** ("State of [industry] 2025")
2. **ROI/cost calculators**
3. **Audit templates** ("Security audit checklist")
4. **Comparison guides** ("Vendor comparison framework")
5. **Free audit / consultation**

### Homepage entry-point research
Lead-magnets on homepage:
- Top-funnel for research-stage visitors (whitepapers, reports)
- Mid-funnel for evaluation (calculators, comparison-guides)
- Bottom-funnel rarely on homepage (more on dedicated LP)

### Calibrated weight
Lead-magnet propositie on homepage typically Important (ICE 5-7):
- One of many entry-points (not the dominant offer)
- High-leverage for content-marketing-driven brands
- Less critical for self-service SaaS or relationship-driven consultancy

Push to Critical only when:
- Homepage is clearly lead-magnet-driven brand strategy
- Lead-magnet ontbreekt OR catastrofaal slecht gepositioneerd
- Content-marketing is primary lead-source

### Best practices (when applicable)
- Lead-magnet specific and time-anchored
- Preview of content (cover, ToC, sample-pages)
- Form-length matched to stage (top-funnel: 3-5 fields)
- Industry/role-relevance

### Common failures
- No lead-magnet on content-marketing-driven brand homepage
- Generic "Get our resources" without value-promise
- Heavy-gated top-funnel content
- Lead-magnet preview absent

---

## Category 8: Multi-stakeholder content layering

### Challenger Sale multi-stakeholder framework
Different visitor-roles need different content:
- **Economic buyer** (CFO, MD): pricing-discussion, business-outcome
- **Technical buyer** (IT, engineering): technical-fit, integration, security
- **End-user** (specialist): usability, workflow-fit
- **Champion** (internal sponsor): shareable-proof, internal-sell collateral

### B2B persona-targeting research
Multi-stakeholder homepages serve different roles in different sections:
- Hero: dominant-role-targeted
- ROI section: economic-buyer-targeted
- Integration section: technical-buyer-targeted
- Use-case section: end-user-targeted

### Content-by-role patterns
Three approaches to multi-stakeholder homepage:
1. **Layered (most common):** single homepage with role-relevant sections
2. **Role-routing (enterprise):** "For executives / For IT / For end-users" navigation
3. **Single-audience (focused):** homepage targets one dominant role

### Calibrated weight (Important/Nice default)
Multi-stakeholder findings typically Important (ICE 4-6):
- Most B2B homepages serve mixed audiences acceptably with general content
- Push to Critical (7+) only when visible active mismatch
- Don't force role-segmentation where audience is mostly single-role

**When to push to Critical:**
- Enterprise-targeting homepage met ALLEEN end-user content (technical/economic-buyer feel no relevance)
- Heavy technical-content op homepage waar end-users dominant zijn
- Generic-everywhere content waar role-differentiation duidelijk nodig is

### Best practices (when applicable)
- Hero targets dominant role
- ROI section visible for economic buyers
- Integration/security section visible for technical buyers
- Use-case examples visible for end-users
- Optional: role-tagged navigation ("For Marketing / For Sales / For IT")

### Common failures
- Generic single-audience content for clearly multi-stakeholder buying
- Heavy technical-jargon hero on mixed-audience homepage
- Over-segmentation (10+ role-pages confusing visitor)

### Practical guidance for findings
- Mark category as "checked, brief observation" if no significant finding
- Don't over-engineer findings here

---

## Category 9: CTA strategy multi-path matched aan visitor-job

### Fogg Behavior Model on B2B homepage
Different visitor-jobs need different CTAs:
- Brand-evaluation visitor → service-routing CTAs
- Service-finding visitor → specific service-page CTAs
- Trust-verification visitor → case-studies, about-us CTAs
- Lead-magnet research → download CTAs
- Decision-stage visitor → demo / contact-sales CTAs

### Multi-purpose-page CTA patterns
Unlike dedicated LPs (single-CTA dogma), homepages benefit from:
- Primary CTA in hero (most likely visitor-job)
- Secondary CTAs in service-cards (service-routing)
- Tertiary CTAs in proof-sections (case-studies)
- Multi-channel contact CTAs (form, phone, chat)
- Sticky mobile CTA matched to primary intent

### Best practices
- Hero CTA matched to primary visitor-job + brand goal
- Service-card CTAs ("Learn more →")
- Multi-channel contact options visible
- Sticky mobile CTA
- CTA copy specific and action-oriented

### Common failures
- Single-CTA dogma applied to multi-purpose homepage
- Generic "Klik hier" or "Submit"
- 6+ equally weighted CTAs (paralysis)
- Sticky mobile CTA absent

### B2B-service-type calibration
- SaaS low-ticket: "Start free trial" primary, "Watch demo" secondary
- SaaS enterprise: "Request demo" primary, "Contact sales" secondary
- Consultancy: "Plan kennismaking" primary, "Bekijk klantcases" secondary
- Professional services: "Plan vrijblijvend gesprek" primary

---

## Category 10: FAQ & B2B objection handling (light op homepage)

### MECLABS anxiety axis (homepage-context)
On homepage, FAQs serve LIGHT objection-handling (deeper FAQ on servicepage):
- Vendor-risk anxiety
- ROI-uncertainty anxiety
- Integration-anxiety
- Pricing-anxiety

### Light homepage-FAQ patterns
- 3-5 high-level FAQs (not exhaustive)
- Focus: most-common decision-cycle questions
- Link to deeper resources

### Best practices
- 3-5 FAQs covering top objections
- Categories: pricing, integration, security, implementation
- Link to deeper FAQ on servicepage
- Schema.org FAQ markup for SEO

### Common failures
- Generic FAQs unrelated to actual objections
- Long-winded FAQ section on homepage (more appropriate for servicepage)
- No FAQ at all on enterprise-targeting

---

## Category 11: Mobile experience

### B2B desktop-dominance acknowledgment
B2B traffic patterns:
- 50-70% desktop on enterprise B2B
- Higher mobile share on SMB-targeting
- Decision-makers research mobile, decide desktop

### Baymard mobile research (B2B-context)
- Mobile homepage must be functional, not just responsive
- Long-form content acceptable mobile (research-mode)
- Sticky CTA on mobile valuable
- Customer-logos mobile-visible

### Best practices
- Mobile-first hero with key value-prop visible
- Customer-logos mobile-visible
- Service-cards single column on mobile
- Sticky mobile CTA
- Fast page load (Core Web Vitals)
- Mobile-to-desktop handoff option

### Common failures
- Desktop-only optimization
- Hero requires zoom on mobile
- Customer-logos invisible on mobile
- Multi-column service-grid on mobile
- No mobile sticky CTA

---

## Brand and B2B-service-type calibration notes

Always recalibrate by brand snapshot AND B2B-service-type AND organization-size:

**Example: Hero CTA**
- SaaS low-ticket: "Start free trial — no credit card" primary
- SaaS mid-ticket: "Schedule 30-min demo" primary
- SaaS enterprise: "Request enterprise demo" primary, "Talk to sales" secondary
- Consultancy: "Plan kennismaking" primary, "Bekijk klantcases" secondary
- Professional services: "Plan vrijblijvend gesprek" primary
- Managed services: "Schedule security audit" primary

**Example: Customer logos emphasis**
- SaaS enterprise: 12+ logos with named industries above-the-fold
- SaaS mid-market: 6-8 logos with industry-tag
- Consultancy: named-client list + 4-6 logos
- Professional services: named-clients + sector-logos
- Early-stage: customer-count text + 3-5 logos

**Example: Service-routing**
- Single-service brand: not relevant
- Multi-service SaaS: 3-6 service-cards dominant
- Consultancy with verticals: industry-routing OR service-routing
- Managed services: service-tier-routing

Recommendations that don't match brand AND service-type AND organization-size zijn fout.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites a specific principle, study, or source
- [ ] Recommendation is concrete (exact copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric is named (service-page CTR / demo-request / lead-magnet downloads / contact-conversion)
- [ ] ICE justified by I/C/E breakdown with category-specific calibration
- [ ] Multi-stakeholder finding calibrated Important/Nice default
- [ ] Lead-magnet propositie finding Important default
- [ ] Recommendation matches brand snapshot AND B2B-service-type AND organization-size AND dominant-visitor-role
- [ ] Multi-purpose entry-point logic respected (no single-CTA dogma)
- [ ] Decision-maker context respected
- [ ] Case-studies > reviews calibration applied
- [ ] Dutch output: no "huren" check
- [ ] No authenticity claims about logos/case-metrics/certifications without strong evidence

If any box unchecked, rework or remove the finding before delivering.
