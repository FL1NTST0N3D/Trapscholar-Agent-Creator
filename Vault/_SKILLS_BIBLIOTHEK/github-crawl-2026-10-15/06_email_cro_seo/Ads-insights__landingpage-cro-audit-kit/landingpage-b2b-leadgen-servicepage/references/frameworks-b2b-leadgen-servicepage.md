# Frameworks for B2B Leadgen Service Page Audits

This reference file contains the CRO and B2B-leadgen-specific frameworks, principles, and applied research. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

B2B leadgen servicepages are uniquely prone to fabricated findings because so much is dynamic:
- Customer-logo grids (often rotating carousels with limited subset visible)
- Case-study cards (often filtered by industry/role)
- G2/Capterra/Trustpilot review widgets (JS-loaded)
- ROI-calculators and interactive demo-widgets
- Form-builders (HubSpot, Marketo, Pardot, custom) with conditional fields
- Embedded demo videos (often gated or interactive)
- Pricing display ("Contact us" vs visible tiers — conditional rendering common)
- Trust badges (SOC 2, ISO 27001, GDPR) often JS-rendered
- Chat widgets (Drift, Intercom, Qualified) with conditional triggers
- Industry/country-based content conditional rendering

**For every finding, verify against screenshots before delivering.**

---

## CRITICAL — Decision-maker context

The B2B servicepage visitor is fundamentally different from B2C:

**B2C consumer visitor:**
- Decides for themselves
- Anxieties: cost, fit, regret
- Trust signals: reviews, photos, warmth
- Decision-cycle: short (minutes to days)

**B2B decision-maker visitor:**
- Decides for organization, often with peers
- Anxieties: ROI-justification, internal-sell, vendor-risk, career-risk
- Trust signals: case studies, named customers, certifications, peer-validation
- Decision-cycle: long (weeks to months)

**Implications for findings:**
- Don't recommend warmth-driven copy on enterprise B2B
- Don't recommend aggressive scarcity (signals desperation in B2B)
- Don't recommend stripping forms to 3 fields if deal-size requires qualification
- DO recommend ROI-clarity, internal-sell-collateral, peer-validation, risk-mitigation signals

---

## CRITICAL — Multi-stakeholder logic

A B2B servicepage is often read by multiple roles at different moments:

**Economic buyer** (CFO, MD, director, owner):
- Focus: ROI, financial-impact, budget-justification
- Anxiety: "Can I justify this investment internally?"
- Content needs: business-impact metrics, ROI-calculator, pricing-transparency where strategically appropriate

**Technical buyer** (IT, engineering, operations):
- Focus: technical-fit, integration, security, compliance
- Anxiety: "Will this integrate with our stack? Is it secure?"
- Content needs: technical specs, integration partners, security certifications, API docs

**End-user** (specialist who'll use the service):
- Focus: usability, workflow-fit, productivity-gain
- Anxiety: "Will this make my job easier or harder?"
- Content needs: product-screenshots, use-case examples, training/onboarding info

**Champion** (someone who'll sell-internally):
- Focus: shareable-proof, internal-presentation collateral
- Anxiety: "How do I get this approved internally?"
- Content needs: exportable content, ROI-calculator results, case-study one-pagers

**Multi-role page implications:**
- Layered content (ROI section + technical section + use-case section)
- Multi-path CTAs matched to roles (demo / spec-sheet / pricing-discussion / free-audit)
- Don't force single visitor-job — accommodate multiple

---

## CRITICAL — Case studies dominate over reviews

For B2B, named-customer proof is heavier than aggregated reviews:

**Why case studies > reviews on B2B:**
- B2B decision-makers want named-companies-like-theirs as proof, not anonymous "users"
- Specific metrics (saved X hours, increased Y revenue, reduced Z cost) > generic 5-star ratings
- Named contact (CFO of Brand X) > anonymous "Sarah M."
- Customer-logo grid = brand-presence at-a-glance trust
- Story-format case study = procurement-ready collateral

**Reviews still relevant but lighter:**
- G2/Capterra reviews for SaaS (peer-validation in software-buying)
- Trustpilot for B2B services (lower weight than B2C but still relevant)
- Named B2B reviews ("Reviewer: Director of Marketing, mid-market SaaS") > anonymous stars

**Implications for findings:**
- Logo-wall absence = critical finding
- Case-study absence = critical finding
- Generic anonymous reviews without B2B-context = low impact finding
- "Trusted by [bekende namen]" pattern is high-leverage trust element

---

## CRITICAL — Lead-quality vs lead-volume tradeoff (CAC-and-sales-capacity calibrated)

In B2B, the form-shortening reflex is often wrong:

**Why B2B forms can be longer than B2C:**
- B2B CAC is typically 5-50x higher than B2C
- Sales-team capacity is limited and expensive (€80-€200/hour SDR/AE cost)
- Unqualified lead = wasted sales-cycle = high opportunity cost
- BANT/MEDDIC qualification reduces SQL-friction

**When to recommend shorter forms:**
- Low-ticket SaaS (€50-500/m): volume matters, self-service possible
- Demo/trial flows: low-friction first-step, qualification in onboarding
- Top-funnel content downloads: get email, nurture later

**When to recommend longer forms:**
- Enterprise sales: qualify before sales-time invested
- High-ticket consultancy: lead-quality matters more than volume
- Multi-stakeholder evaluation: more context needed to route to right sales rep

Form-shortening recommendation must specify:
- Expected lead-volume increase
- Expected lead-quality decrease (qualitative)
- Recommended downstream qualification mechanism
- Acknowledgment of CAC-and-sales-capacity context

---

## CRITICAL — B2B-service-type calibration

Recommendations vary heavily by B2B-service-type:

**B2B SaaS low-ticket (€50-500/m):**
- Self-service trial possible, demo-driven
- Short sales-cycle (days to weeks)
- Volume-driven economics
- Form-shortening more justified
- Reviews (G2, Capterra) more relevant
- Pricing transparency dominant

**B2B SaaS mid-ticket (€500-5k/m):**
- Sales-assisted, demo-required
- Mid sales-cycle (2-8 weeks)
- Mix of volume + quality
- 5-8 field forms acceptable
- Case studies + reviews balanced
- Pricing visible but with "Contact for enterprise" option

**B2B SaaS enterprise (€5k+/m):**
- Fully sales-driven
- Long sales-cycle (3-12+ months)
- Quality-driven economics
- 8-12 field forms acceptable
- Named-customer case studies dominant
- "Contact us" pricing standard

**B2B consultancy / agency:**
- Project-based or retainer
- RFP-driven or referral-based
- Long sales-cycle
- Named-expertise critical
- Case studies dominant
- "Vraag offerte"-CTA primary

**B2B professional services** (accountancy, legal, financial advisors):
- Relationship-driven, long sales-cycle
- Trust + credentials dominant
- Named partners visible
- Sector-expertise per-vertical content

**B2B managed services** (IT, infrastructure, security):
- Risk-mitigation-driven
- Technical-buyer present
- Compliance + security badges critical
- Uptime/SLA proof essential

---

## Core frameworks (apply across the entire audit)

### April Dunford B2B positioning
B2B servicepages must position for:
- **Best-fit customer** (specific industry, role, company-size)
- **Competitive alternatives** (visitor compares; LP must address)
- **Unique attributes** (what only this brand does)
- **Value enabled by attributes** (concrete outcomes)
- **Market category** (frame correctly for buying motion)

### Challenger Sale (Dixon & Adamson)
B2B decision-makers respond to insight-led messaging, not feature-listing:
- Teach: lead with insight that reframes the visitor's problem
- Tailor: speak to specific industry/role
- Take control: confident assertion, not soft suggestion

Applied to LP: hero copy should reframe the problem ("Stop juggling 7 tools — this is what consolidation actually saves") not just list features.

### BANT framework (Budget, Authority, Need, Timeline)
Classic B2B qualification, used in form-design:
- Budget: tier/range fields
- Authority: role/title field
- Need: use-case dropdown
- Timeline: implementation timeline field

### MEDDIC framework (Metrics, Economic buyer, Decision criteria, Decision process, Identify pain, Champion)
Modern enterprise B2B qualification:
- Metrics: business-impact form-fields
- Economic buyer: who's making decision
- Decision criteria: priorities
- Decision process: how they buy
- Identify pain: problem-context
- Champion: who's championing internally

### Edelman B2B Trust Barometer
B2B trust differs from B2C trust:
- Peer-validation (customers like me) > general reviews
- Third-party validation (analyst reports, awards from B2B-specific sources)
- Certifications (SOC 2, ISO 27001, GDPR compliance) carry heavy weight
- Customer logo-presence drives "they trust them, so I can trust them"

### Forrester B2B buyer research
Key findings applied to servicepage:
- B2B buyers research 70%+ of decision before contacting sales
- They consume 3-7 content pieces on average before form-fill
- They prefer self-service for early-stage research
- Anonymous research → form-fill at decision-stage

This shapes lead-magnet strategy: provide early-stage value without form-gate, gate later-stage content (demos, audits, pricing).

### Hormozi irresistible-offer principles (B2B-adapted)
For lead-magnets and offers:
- **Dream outcome** — concrete business result (revenue, savings, time)
- **Perceived likelihood** — proof via case studies and metrics
- **Time delay** — fast-to-value ("get audit in 24h")
- **Effort and sacrifice** — minimize friction in claiming offer

Hormozi B2B-specific: value-stacking ("plus: bonus templates, ROI calculator, 1-hour consult worth €X") works in B2B but must avoid "marketer scammy" tone for enterprise audiences.

### MECLABS Conversion Sequence Heuristic on B2B
C = 4m + 3v + 2(i−f) − 2a

On B2B servicepages:
- **m (motivation):** variable by visitor-role and stage (research mode vs evaluation mode)
- **v (value):** business-impact + competitive-alternative differentiation
- **i (incentive):** lead-magnet (ROI calc, free audit, demo, whitepaper)
- **f (friction):** unclear ROI, missing proof, long opaque forms, hidden pricing without value framing
- **a (anxiety):** ROI uncertainty, vendor-risk, integration risk, scaling risk

### Cialdini's principles on B2B
- **Authority** — analyst reports, awards, expert quotes, founder-credentials
- **Social proof** — customer-logos, case studies, customer counts ("Trusted by 500+ companies")
- **Liking** — less dominant on B2B than B2C, but warm-yet-professional tone wins on mid-market
- **Reciprocity** — gated lead-magnets, free audits, free templates
- **Commitment-consistency** — multi-step forms create commitment-momentum
- **Scarcity** — typically NOT appropriate on B2B (signals desperation) — exception: enterprise pricing-tier "limited slots for Q4 onboarding"

### Fogg Behavior Model on B2B servicepages
- MOTIVATION: build via insight-led copy + proof-density
- ABILITY: clear next-step (demo / audit / download) + minimal-required form
- TRIGGER: above-the-fold CTA + repeated triggers at proof-density-peaks

### Nielsen Norman heuristics applied to B2B
- **#1 Visibility of system status** — clarity about what visitor gets after form-fill
- **#2 Match real world** — industry/role-appropriate language
- **#5 Error prevention** — inline form validation, format hints
- **#6 Recognition over recall** — proof visible, not buried
- **#9 Help users recover from errors** — clear form-error messages

### Jobs-to-be-Done on B2B servicepages
B2B visitors are doing ONE of:
1. **Research mode** — "Learn about category and approaches" (top-funnel)
2. **Evaluation mode** — "Is this vendor right for us?" (mid-funnel)
3. **Justification mode** — "How do I sell this internally?" (decision-stage)
4. **Verification mode** — "Confirm this vendor before contacting"
5. **Procurement mode** — "Get pricing/contract details"

Each job needs different content. A high-converting servicepage layers content for multiple jobs without forcing one path.

**Important Dutch translation:** never use "huren" for JTBD framing. Use "kiezen voor", "inzetten voor", "implementeren om X op te lossen".

---

## Category 1: Above-the-fold value proposition & business-impact positionering

### April Dunford positioning on B2B
Hero must answer in 5-8 seconds:
- WAT (service in business-impact terms)
- VOOR WIE (target industry/role/company-size)
- WAAROM (vs alternatives, vs status quo)
- WAT NU (demo / audit / download CTA matched to role)

### Challenger Sale insight-led messaging
Best B2B heroes lead with INSIGHT that reframes the problem:
- Bad: "Best-in-class marketing automation platform"
- Good: "Marketing teams spend 40% of time on data-cleanup. Stop. Here's what automation actually saves."

### MECLABS Conversion Sequence on hero
On hero: clarity (v-factor) dominates. Visitor must immediately understand: WAT do they get, VOOR WIE is this, WAT does it solve.

### Outcome-over-feature framing
B2B buyers respond to outcomes, not features:
- ❌ Feature: "AI-powered analytics dashboard"
- ✅ Outcome: "Cut quarterly reporting from 3 days to 30 minutes"
- ❌ Feature: "Multi-tenant architecture"
- ✅ Outcome: "Onboard new entities in hours, not weeks"

### Best practices
- Headline frames business-outcome, not feature
- Sub-headline specifies audience (industry/role/size)
- One credibility-anchor visible (customer-count, named-customer, analyst-recognition)
- Primary CTA matched to dominant visitor-stage (research → download, evaluation → demo, decision → contact-sales)
- Optional: secondary CTA for different stage (e.g. "Or get pricing →" alongside "Request demo →")

### Common failures
- Generic "Best-in-class solution for..." copy
- Feature-list hero ("AI · Automation · Analytics")
- Brand-name as headline
- No credibility anchor in hero
- Multi-CTA chaos (4+ equally weighted)
- Buzzword overload ("synergize", "leverage", "transform")

### B2B-service-type calibration
- SaaS low-ticket: outcome + trial-CTA dominant
- SaaS enterprise: outcome + demo-CTA + customer-logos hero
- Consultancy: case-study-led + offerte-CTA
- Professional services: credentials-led + consult-CTA

---

## Category 2: Hero imagery / video (service-in-business-context)

### Forrester B2B buyer imagery research
B2B imagery serves different functions than B2C:
- Show service in actual business-environment (not generic stock office)
- Product-screenshots for SaaS (real interface, real data) > marketing-illustrations
- Customer-environment shots (factory, office, lab) for industry-specific services
- Founder/team visible for consultancy and professional-services (people-trust matters)

### Marketing Sherpa B2B visual patterns
- Product-demo videos in hero lift demo-request conversion 20-50% (when actually showing product)
- Customer-quote videos (CFO/VP-level talking head) outperform generic testimonial-text
- Animated product-explainers work for complex SaaS
- Static product-screenshot beats stock-illustration for software

### Product-screenshot vs customer-environment trade-offs
- For SaaS: product-screenshot dominant (visitor needs to see what they buy)
- For consultancy: customer-environment or team-photos dominant
- For managed services: outcome-visualization (uptime dashboards, security metrics)
- For agencies: portfolio-thumbnails or work-samples

### Best practices
- Authentic, service-relevant imagery
- Product-screenshot for SaaS (real UI, real data)
- Customer-environment for services-in-context
- Optional hero video (demo or customer-testimonial)
- Mobile-optimized variants

### Common failures
- Generic stock business-imagery (smiling diverse-team in glass office)
- Marketing-illustrations instead of product-screenshots for SaaS
- Hero video auto-playing sound
- Stock-style customer-environment photos (clearly staged)
- No imagery at all (text-heavy hero)

### Authenticity restraint
A finding may recommend verifying imagery authenticity. A finding may NOT assert specific photos are stock without strong evidence.

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
- Logo-wall above-the-fold lifts conversion 15-30% on first-time visitors
- Industry-specific logos (peer-companies) outperform diverse-industry mix for niche audiences
- "As featured in" press-logos work alongside customer-logos for credibility-stacking
- Logo-quality matters: high-res monochrome > low-res mixed-color

### "Trusted by [bekende namen]" pattern impact
This single pattern is the most concise high-impact trust signal in B2B:
- Visitor sees [Bekende klant] → "they're legit"
- 5-15 logos optimal (under 5: not enough proof; over 15: dilutes impact)
- Hero-zone or directly-below-hero positioning
- Optional: small heading "Trusted by 500+ companies including:" with logos

### Best practices
- Logo-strip above or directly below hero
- 6-12 customer-logos visible
- Industry-relevant logos prioritized
- Monochrome treatment (consistency + premium feel)
- Clickable optional (links to case-study for that customer)
- Customer-count text alongside ("Trusted by 500+ companies")

### Common failures
- No customer-logos visible despite having customers
- Logos buried in footer or below-the-fold
- Mix of customer logos and partner logos (visitor confused)
- Logos without permission documentation
- Generic logos that don't match audience industry
- Logo-carousel with only 1-2 visible at a time

### Authenticity restraint
A finding may recommend verifying customer-logo permission. A finding may NOT claim logos are unauthorized without strong evidence (e.g. mismatch with public customer-list, customer-relations history).

### B2B-service-type calibration
- SaaS: customer-logos critical, often above-the-fold
- Consultancy: customer-logos + named-client list
- Professional services: named-clients + sector-logos
- Managed services: customer-logos + certifications mixed
- Early-stage / startup: customer-counts beat sparse-logos

---

## Category 4: Case studies & named-customer proof

### Cialdini social proof in B2B context
B2B social proof is named, specific, and metric-driven:
- Named customer (company name, person's name, role)
- Specific outcome (saved X hours, increased Y revenue, reduced Z cost)
- Verifiable details (industry, company-size, use-case)
- Story-format with before/after

### Forrester case-study impact research
- 73% of B2B decision-makers cite case studies as critical content in evaluation
- Named-metric case studies outperform anonymous-outcome by 5-7x
- Industry-specific case studies (visitor's industry) lift relevance-perception 40-60%
- Video case studies (customer talking head) outperform text-only by 30-50%

### Named-customer testimonials with metrics
Structure of high-converting case-study card:
1. Customer logo + company name + industry/size
2. Person quoted with name + role
3. Specific metric outcome (concrete number)
4. Short story (1-2 sentences)
5. "Read full case study →" CTA

### Best practices
- 2-4 case-study highlights on servicepage
- Each with named customer + metric + quote
- Industry-tagged for filtering on multi-industry pages
- Optional: video case study
- Link to full case study (longer content)
- Sector-relevant when visitor-industry is known

### Common failures
- Generic "happy customers" without specifics
- Case studies without metrics (just praise)
- Anonymous case studies ("Fortune 500 financial services company")
- Stock-quote testimonials
- Case studies disconnected from service explained
- No case studies on page despite having them
- Outdated case studies (3+ years)

### Authenticity restraint
A finding may recommend verifying case-study authenticity. A finding may NOT claim case-metrics are inflated or testimonials are fabricated without strong evidence.

### B2B-service-type calibration
- SaaS: 2-4 case studies with quantitative metrics (hours saved, revenue impact)
- Consultancy: 2-3 detailed case studies with project-outcome stories
- Professional services: 1-2 deep client-stories with named partners
- Managed services: uptime/reliability metrics + customer-named

---

## Category 5: ROI/impact-bewijs

### Outcome-driven B2B research
B2B decision-makers need concrete ROI proof to justify internally:
- Quantified outcomes ("47% reduction in X") beat qualitative claims
- Time-to-value metrics ("payback in 3 months") drive urgency
- Comparison-baselines ("vs industry-average") strengthen claim
- ROI calculator interactivity engages visitor + collects data

### Hormozi value-equation
Value = (Dream outcome × Perceived likelihood) / (Time delay × Effort and sacrifice)

For B2B servicepage ROI:
- **Dream outcome:** concrete business result
- **Perceived likelihood:** case-study proof + metric average
- **Time delay:** time-to-value clarity
- **Effort and sacrifice:** implementation effort transparency

### ROI-calculator engagement patterns
- Interactive ROI calculators lift form-completion 30-80% on pages where present
- Calculator-result gating (email for full result) is effective lead-magnet
- Industry/role-specific calculators outperform generic
- "Calculate your ROI in 60 seconds" promise needs to be true

### Best practices
- ROI/impact section with 3-4 key metrics
- Customer-averaged metrics ("Customers see avg 47% reduction")
- Time-to-value visible
- Optional: interactive ROI calculator
- Comparison baselines for context
- Industry-benchmark mentions

### Common failures
- ROI section absent on servicepage
- Vague claims ("dramatic improvement") without numbers
- Metrics without source-customers
- Calculator without industry-relevance
- Time-to-value vague or absent

### B2B-service-type calibration
- SaaS: hours-saved, revenue-impact, error-reduction metrics
- Consultancy: project-outcome metrics + ROI multiplier
- Professional services: cost-savings + risk-reduction
- Managed services: uptime, security-incident-reduction, cost-of-downtime

---

## Category 6: Trust signals & B2B credibility

### Cialdini authority in B2B
B2B authority signals:
- Analyst recognition (Gartner Magic Quadrant, Forrester Wave)
- Industry awards (relevant to vertical)
- Certifications (SOC 2 Type II, ISO 27001, HIPAA, GDPR)
- Compliance badges (PCI DSS, SOX where applicable)
- Founder/team credentials (visible authority)
- Press mentions in B2B-relevant publications

### Certifications and compliance signals
Critical for B2B (especially enterprise):
- **SOC 2 Type II** — security audit baseline for SaaS
- **ISO 27001** — info-security management baseline
- **GDPR / AVG compliance** — EU privacy
- **HIPAA** — healthcare US
- **PCI DSS** — payment card industry
- **Industry-specific** — depends on vertical

These appear as badges typically in footer-strip + dedicated security/compliance section.

### Forrester B2B trust patterns
Trust signals decision-makers prioritize:
1. Existing customer evidence (logos + case studies)
2. Third-party validation (analyst reports, awards)
3. Security/compliance certifications
4. Peer-network referrals (less visible on LP)
5. Vendor financial-stability signals (revenue, funding, longevity)

### Best practices
- Trust-strip near hero (customer-count + key cert)
- Dedicated security/compliance section
- Analyst-recognition badges where applicable
- Industry awards visible
- Press logos (B2B-relevant only)
- Customer-stability signals (years operating)

### Common failures
- Generic certification badges without context
- Compliance section absent on enterprise-targeting page
- Self-claims without third-party validation
- Press-logos from irrelevant publications
- "Years of experience" without specifics

### Note: Reviews calibrated lighter on B2B
Reviews appear in this category as one trust element, not primary:
- G2/Capterra reviews relevant for SaaS
- Trustpilot reviews lighter weight than for B2C
- Named-reviewer testimonials more valuable than star-ratings
- Reviews work alongside case-studies, not in replacement

---

## Category 7: Lead-magnet propositie & value-exchange

### Cialdini reciprocity in B2B
Lead-magnets are reciprocity-engines: visitor gives contact info, receives value:
- High-value lead-magnet → trust + reciprocity → faster sales-cycle
- Low-value lead-magnet → "marketing fluff" → distrust + slower cycle

### Hormozi irresistible-offer principles for B2B lead-magnets
- **Dream outcome** in lead-magnet promise (what they actually get)
- **Specificity** ("47-page enterprise security audit checklist") beats vague ("free resources")
- **Time delay** ("in your inbox in 60 seconds") beats ("we'll be in touch")
- **Effort minimal** (single field, instant download where possible)

### Marketing Sherpa B2B lead-magnet patterns
High-converting B2B lead-magnets:
- **Industry benchmark reports** ("State of [industry] 2025") — research-stage value
- **ROI/cost calculators** — evaluation-stage value
- **Audit templates** ("Security audit checklist") — actionable value
- **Comparison guides** ("Vendor comparison framework") — decision-stage value
- **Demo videos** (gated) — late-stage value
- **Free audit / consultation** — high-trust + qualification

### Gated-content economics
- Top-funnel content (educational): NOT gate, build SEO + trust
- Mid-funnel content (evaluation): gate with light form (email + company)
- Decision-funnel content (demo, pricing, audit): gate with full BANT/MEDDIC form

Mismatch (gating top-funnel content with heavy forms) kills lead-volume.

### Best practices
- Lead-magnet specific and time-anchored
- Value-promise visible at form
- Preview of lead-magnet content (cover, ToC, sample pages)
- Response-time commitment ("In your inbox within 60 seconds")
- Form-length matched to lead-magnet stage
- Industry/role-relevance where possible

### Common failures
- Generic "Contact us for info" without value-promise
- "Vraag offerte" without time-anchor or scope-clarity
- Gating top-funnel content with full BANT-form
- No preview of gated content
- Vague lead-magnet ("Our resources") without specifics

### B2B-service-type calibration
- SaaS: free trial + demo dominant; whitepapers + ROI-calc secundair
- Consultancy: free audit + sector-benchmark report
- Professional services: free initial consultation + sector-guide
- Managed services: security-audit-template + assessment-call

---

## Category 8: Lead-form design met BANT/MEDDIC-kwalificatie

### CXL/ConversionXL form research (B2B-adapted)
Standard CXL finding (every field reduces conversion ~7-11%) applies BUT calibrated to deal-size:
- Low-ticket B2B: aggressively short (3-5 fields)
- Mid-ticket B2B: moderate (5-8 fields with BANT lite)
- Enterprise B2B: longer acceptable (8-12 fields with MEDDIC qualification)

### Baymard form-field research (B2B context)
- Field-label above input outperforms placeholder-only
- Real-time validation outperforms submit-time
- Single-column form outperforms multi-column
- Dropdown-fields outperform free-text where applicable (reduces errors, enables routing)
- Required-only marking outperforms required-asterisks-on-every-field

### BANT framework in form-design
- Budget: tier dropdown ("Under €5k / €5-25k / €25k+ / Not yet defined")
- Authority: role/title field
- Need: use-case dropdown
- Timeline: implementation-timeline ("Within 30 days / 1-3 months / 3-6 months / Researching")

### MEDDIC framework in form-design
For enterprise:
- Metrics: business-impact context field
- Economic buyer: "Who else is involved in decision?"
- Decision criteria: priority dropdown
- Decision process: "When do you plan to decide?"
- Identify pain: problem-context textarea
- Champion: optional "Have you discussed this internally?"

### Multi-step vs single-step (B2B specific)
- Single-step: lead-magnets, demo-requests
- Multi-step: enterprise quote-requests (commitment-momentum)
- Progressive profiling: re-engage known visitors with new fields

### Best practices
- Form-length matched to deal-size + lead-magnet stage
- Labels above fields
- Required-only marking
- Real-time validation with format hints
- Single-column on mobile
- BANT/MEDDIC qualification fields where appropriate
- Submit-CTA action-oriented and matched to next-step ("Schedule demo" not "Submit")
- Privacy reassurance near submit ("We use your data only to respond to this request")

### Common failures
- Too many fields for deal-size (3 fields on enterprise = under-qualified)
- Too few fields for lead-quality needs
- Placeholder-only labels
- Submit-time validation only
- Asterisks on every field
- Generic "Submit" CTA
- Multi-column on mobile
- BANT/MEDDIC fields as free-text instead of dropdown (un-routable)

### Lead-quality vs lead-volume calibration (B2B-specific)
- Always specify CAC + sales-capacity context in recommendation
- "Remove field X" → "expect +N% form-completion, possible -M% lead-quality; calibrate to current SDR/AE capacity"
- "Add field Y" → "expect -N% form-completion, possible +M% lead-quality; reduces wasted sales-cycle"

---

## Category 9: CTA strategy (multi-path matched aan visitor-rol)

### Fogg Behavior Model on B2B CTAs
Trigger must be available at each stage of visitor-evaluation:
- Research-stage: download / whitepaper CTAs
- Evaluation-stage: demo / case-study CTAs
- Decision-stage: contact-sales / pricing-discussion CTAs

### Challenger Sale multi-stakeholder CTAs
Different visitor-roles need different next-steps:
- Economic buyer: "Calculate ROI" or "Get pricing"
- Technical buyer: "View technical docs" or "Try free tier"
- End-user: "See product tour" or "Watch demo"
- Champion: "Get internal-sell deck" or "Schedule discovery call"

### "Demo / contact-sales / download" calibration
- Demo-CTA: dominant for SaaS evaluation-stage
- Contact-sales CTA: dominant for enterprise high-touch
- Download CTA: dominant for top-funnel + lead-magnet
- Free-trial CTA: dominant for low-ticket SaaS

### Best practices
- Primary CTA matched to dominant visitor-role + dominant funnel-stage
- Secondary CTA for different role/stage
- CTA copy action-oriented and outcome-specific ("Schedule 30-min demo" beats "Contact us")
- Multi-path CTAs visible (download / demo / pricing) but not chaotic (max 3 paths)
- Sticky CTA on mobile + long-page-scroll points

### Common failures
- Single-CTA dogma applied to multi-stakeholder B2B page
- Generic "Contact us" or "Learn more"
- 4+ equally-weighted CTAs creating paralysis
- Sticky CTA absent on mobile
- CTA mismatched to dominant visitor-stage
- "Submit" instead of action-oriented copy

### B2B-service-type calibration
- SaaS low-ticket: "Start free trial" primary, "Watch demo" secondary
- SaaS enterprise: "Request demo" primary, "Contact sales" secondary, "Download spec sheet" tertiary
- Consultancy: "Vraag offerte aan" primary, "Bekijk cases" secondary
- Professional services: "Plan kennismaking" primary, "Download sector-guide" secondary

---

## Category 10: FAQ & B2B objection handling

### MECLABS anxiety axis (B2B-adapted)
B2B-specific anxieties on servicepage:
- **Procurement-anxiety:** "How do we get this through procurement?"
- **Security-anxiety:** "Is this compliant with our security standards?"
- **Integration-anxiety:** "Will this integrate with our [stack]?"
- **Scaling-anxiety:** "Will this scale as we grow?"
- **Vendor-risk-anxiety:** "Is this vendor stable? Will they be here in 3 years?"
- **Internal-sell-anxiety:** "How do I justify this internally?"
- **ROI-uncertainty:** "Will we actually see the promised outcomes?"

### Pre-emptive objection handling
Best B2B servicepages address objections BEFORE they form:
- Inline microcopy at form ("We'll route to right team — typically reply within 4 business hours")
- FAQ section addressing top procurement / security / integration questions
- Comparison-page links for "vs alternatives" anxieties
- Customer-stories addressing similar implementations

### Best practices
- 6-10 FAQs based on actual decision-maker questions
- Categories: procurement, security, integration, ROI, implementation
- Schema.org FAQ markup for SEO
- Link to deeper resources (security whitepaper, integration docs)
- Optional: "Common questions from [role]" segmentation

### Common failures
- Generic FAQs ("What does your platform do?")
- FAQs not matched to actual objections
- Long-winded answers
- No FAQ on enterprise-targeting page
- FAQs disconnected from real procurement-cycle questions

---

## Category 11: Mobile experience

### B2B desktop-dominance acknowledgment
B2B traffic patterns differ from B2C:
- 50-70% desktop on enterprise B2B
- Higher mobile share on SMB-targeting and travel-time consumption
- Decision-makers often research mobile, decide desktop

### Baymard mobile research (B2B-context)
B2B mobile patterns:
- Long-form content acceptable mobile (visitor in research mode)
- Tap-to-call for sales-driven services
- Sticky CTA on mobile for long pages
- Form mobile-optimized but form-length can stay longer than B2C
- Heavy interactive elements (calculators) need mobile-fallback

### Mobile-readability for travel-time consumption
B2B decision-makers often consume content during:
- Commute / travel
- Between meetings
- Evening research on tablet/phone

Implications: content must be skim-friendly mobile, key proof above-the-fold on mobile, form-fillability optimized for desktop-handoff if needed.

### Best practices
- Mobile-optimized hero with key value-prop visible
- Customer-logos mobile-visible
- Form mobile-friendly (single column, large fields)
- Sticky mobile CTA on long pages
- Calculators mobile-fallback if interactivity-limited
- Fast page load (Core Web Vitals)
- "Save for later / email me link" option (mobile-to-desktop handoff)

### Common failures
- Desktop-only optimization (mobile broken)
- Hero requires zoom on mobile
- Customer-logos invisible on mobile
- Heavy calculator without mobile-fallback
- Long form ported desktop-to-mobile without redesign
- No mobile sticky CTA

---

## Brand and B2B-service-type calibration notes

Always recalibrate by brand snapshot AND B2B-service-type AND deal-size AND visitor-role:

**Example: Hero CTA**
- SaaS low-ticket: "Start free trial — no credit card" primary
- SaaS mid-ticket: "Schedule 30-min demo" primary, "Watch product tour" secondary
- SaaS enterprise: "Request enterprise demo" primary, "Talk to sales" secondary
- Consultancy: "Plan kennismakingsgesprek" primary, "Bekijk klantcases" secondary
- Professional services: "Plan vrijblijvend gesprek" primary, "Download sector-benchmark" secondary
- Managed services: "Schedule security audit" primary, "Download compliance overview" secondary

**Example: Customer logos emphasis**
- SaaS enterprise: 12+ logos with named industries above-the-fold
- SaaS mid-market: 6-8 logos with industry-tag
- Consultancy: named-client list + 4-6 logos
- Professional services: named-clients + sector-logos
- Early-stage: customer-count text + 3-5 logos

**Example: Form length**
- Low-ticket SaaS trial: 3-4 fields (email + name + company + use-case)
- Mid-ticket demo: 5-7 fields (+ role + timeline + size)
- Enterprise demo: 8-12 fields (+ budget + decision-maker + current-stack + use-case)

Recommendations that don't match brand AND B2B-service-type AND deal-size AND visitor-role zijn fout.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites a specific principle, study, or source
- [ ] Recommendation is concrete (exact copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric is named (form-completion / MQL / demo-request / SQL-conversion / CPL)
- [ ] ICE justified by I/C/E breakdown
- [ ] Recommendation matches brand snapshot AND B2B-service-type AND deal-size AND visitor-role
- [ ] Decision-maker context respected (no consumer-style recommendations)
- [ ] Multi-stakeholder logic acknowledged where relevant
- [ ] Case-studies > reviews calibration applied
- [ ] Form-length calibrated to deal-size + CAC + sales-capacity
- [ ] Lead-quality vs lead-volume tradeoff explicit in form recommendations
- [ ] Dutch output: no "huren" check
- [ ] No authenticity claims about customer-logos/case-metrics/certifications without strong evidence

If any box unchecked, rework or remove the finding before delivering.
