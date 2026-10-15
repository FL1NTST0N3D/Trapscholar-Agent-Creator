# Frameworks for B2B Leadgen Contact Page Audits

This reference file contains the CRO and B2B-contactpage-specific frameworks, principles, and applied research. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

B2B contactpages are uniquely prone to fabricated findings because so much depends on visible-routing-logic:
- Contact-route cards/buttons (sales vs support vs partner vs media)
- Form-builders with conditional fields per routing-choice
- Phone-click tracking (numbers that look static but route via dynamic substitution per source)
- Chat widgets (Intercom, Drift, Qualified, Zendesk) — JS-loaded
- Response-time displays ("Average response 4 hours" — sometimes dynamically calculated)
- Office-location maps and vestigingen-listings
- Account-management UI (often behind login, visible-state may misrepresent)
- Sales-team-availability indicators (real-time status)

**For every finding, verify against screenshots before delivering.**

---

## CRITICAL — Decision-maker context

B2B contactpage visitor differs fundamentally from B2C consumer:

**B2C consumer contactpage visitor:**
- Wants direct contact (phone, WhatsApp, form)
- Anxieties: response-time, "will it cost me?"
- High-intent typically — already chose this provider
- One contact-route typically sufficient

**B2B decision-maker contactpage visitor:**
- Wants RIGHT contact-route for their need
- Anxieties: "will I get pitched?", "will I wait 5 days?", "is this the right team?"
- Mixed intent — some evaluating new vendor, some existing customer, some partner-seeking
- Multiple contact-routes often needed

**Implications for findings:**
- Don't recommend WhatsApp on enterprise B2B (signals informality, not B2B-appropriate for many)
- Don't recommend single-CTA dogma (routing-clarity matters more)
- DO recommend specific response-times, role-routing, sales-vs-support distinction
- DO recommend friction-removal on sales-routes specifically

---

## CRITICAL — Account-routing logic (calibrated weight)

"Contact" is ambiguous in B2B. Different visitor-intents need different paths:
- **Sales contact** (new business evaluation): route to sales-team, BANT-light qualification acceptable
- **Support contact** (existing customer with issue): route to support, login-gated optional
- **Partner contact** (reseller, integrator, alliance): route to partner-team, partner-form
- **Media contact** (press, analysts, journalists): route to PR/comms-team
- **Account-management contact** (existing customer expansion/renewal): route to AM/CSM

**Calibrated category weight:**
- Account-routing as own category is appropriate — it captures the FUNDAMENTAL difference from B2C
- BUT findings here are typically Important (ICE 5-7), occasionally Critical only when visible mismatch (enterprise B2B with single generic route)
- Don't push to Critical default — calibrate to actual page-state

**When to push to Critical (ICE 7.5+):**
- Enterprise B2B with multiple business-units and ONE generic contact-route (high lead-leakage)
- Visible routing-mismatch (sales-form receives support-questions, wastes sales-team time)
- No sales-vs-support distinction on managed-services or SaaS where both flows are critical

**When to keep Important (ICE 5-7):**
- MKB-B2B with single team handling all (account-routing less relevant)
- Existing routing acceptable but could be sharper
- Adding routes optional but not critical-volume

---

## CRITICAL — Multi-stakeholder routing (light calibration)

Different visitor-roles arrive with different needs:
- **Economic buyer** (CFO, MD): pricing-discussion, business-impact-focused contact
- **Technical buyer** (IT, engineering): SE/architect contact, integration-questions
- **End-user** (specialist): demo, training, hands-on questions
- **Champion** (internal sponsor): "discovery call", multi-stakeholder-help

**Calibrated category weight (light):**
- Multi-stakeholder routing on contactpage is NUANCE-level
- Most B2B contactpages don't need to differentiate by role explicitly
- Findings here typically land in ICE 4-6 (Important to Nice-to-have)
- Push to Critical only if visible role-routing actively misdirects high-value leads

**Practical guidance:**
- Look for: are there any role-specific routing options? Are they helpful or just noise?
- Don't over-engineer findings here — multi-role routing is "would be nice" not "required"
- Mark category as "checked, brief observation" if no significant finding

---

## CRITICAL — Account-management contact (typically not-applicable)

For most B2B contactpages, account-management contact category should be marked **"category checked, no finding — not applicable to this business-type"**:

**Not applicable for:**
- MKB-B2B (no dedicated AM/CSM model typically)
- Consultancy / agency (project-team handles ongoing relationship)
- Professional services (relationship-driven, no CSM-tier)
- B2B managed services (support handles ongoing, no separate AM)

**Applicable only for:**
- Enterprise SaaS with dedicated CSM-model
- B2B SaaS mid-ticket where named AM is standard
- Large enterprise software where CSM is buyer-expected

**When applicable, findings typically about:**
- "Existing customer? Reach out to your account manager" routing visible
- AM-contact (named) vs generic support routing
- CSM portal-login link visible
- Existing-customer self-service options

Don't force findings here for non-enterprise-SaaS audits.

---

## CRITICAL — Sales-team-time cost calibration

B2B sales-team capacity is expensive (€80-€200/hour loaded cost). Implications:
- Onbeantwoorde contact-attempts = direct lost lead = wasted ad-spend upstream
- Misrouted lead (sales gets support-question) = wasted sales-time (€50-100 per misroute)
- Heavy-qualified form (10+ fields) on contactpage may hurt volume but improves quality
- Response-time accuracy matters more than B2C (decision-makers shopping, not stuck)

**Form-recommendations must specify:**
- Expected volume-impact
- Expected quality-impact
- Sales-team-capacity context

---

## CRITICAL — WhatsApp / chat formality calibration

Chat/WhatsApp recommendations highly calibrated to brand-formality and target-audience:

**Acceptable WhatsApp/chat:**
- MKB-B2B (50-200 employees) consultancy / agency: mid-formality OK
- B2B SaaS low-ticket (€50-500/m): chat acceptable for fast-cycle audiences
- B2B service-providers with younger doelgroep
- Time-sensitive services (managed-IT-emergencies, support-chat)

**Often unwelcome on enterprise B2B:**
- Enterprise SaaS (€5k+/m) with CSO/CFO targeting
- Professional services (accountancy, legal-B2B, financial advisors B2B): too informal
- Government / public-sector targeting
- Regulated-industries targeting

**Default:** verify brand-formality before recommending. Wrong recommendation here can damage brand-positioning.

---

## Core frameworks (apply across the entire audit)

### Forrester B2B buyer contact behavior
Key findings applied to contactpage:
- B2B buyers research 70%+ before contact-form-fill
- They land on contactpage typically late-stage in decision-cycle
- Mismatched routing creates 30-50% drop-off on first contact-attempt
- Response-time accuracy is #1 driver of trust-formation at contact-point

### Edelman B2B Trust Barometer
B2B trust at contact-point comes from:
- Specific response-time commitment ("We respond within 4 hours during business days") > vague ("Soon")
- Named team-members or function-titles ("Sarah from our sales team") > anonymous
- Office-presence credibility (physical address visible)
- Industry-relevant certifications
- Consistent NAP across Google Business

### Nielsen Norman contact-page UX (B2B-adapted)
Key principles:
- Visibility of system status — what happens after form-fill
- Match between system and real world — contact-route labels in visitor-language ("Talk to sales" beats "Submit inquiry")
- Recognition over recall — all routing-options visible, not buried in menus

### Cialdini's principles on B2B contactpage
- **Authority** — named team, certifications, office-presence
- **Social proof** — customer-count or named-customer logos (compact)
- **Liking** — warm-yet-professional tone, founder/team photos
- **Reciprocity** — response-time-commitment AS reciprocity
- **Commitment-consistency** — multi-step routing creates commitment
- **Scarcity** — typically NOT appropriate on contactpage (anxiety-creator, not motivator)

### Fogg Behavior Model on B2B contactpage
- MOTIVATION: visitor brought motivation (high-intent at contactpage)
- ABILITY: clear routing + minimal friction on chosen route
- TRIGGER: visible contact-routes at correct decision-points

### MECLABS anxiety axis (B2B-adapted)
B2B-specific contactpage anxieties:
- "Will I get a sales-pitch instead of a conversation?"
- "How long until response?"
- "Am I contacting the right team?"
- "Will my contact-info be misused (added to spam-list)?"
- "Will I commit to something by submitting this form?"

### MEDDIC framework (lite) on B2B contactpage
For sales-routing form:
- Metrics (light): business-impact context
- Economic buyer (implicit): role/title field
- Decision criteria (light): use-case dropdown
- Decision process: timeline-indicator
- Identify pain: problem-context field
- Champion (implicit): "Are others involved?" optional

Full MEDDIC reserved for dedicated demo-LP, not contactpage.

### Jobs-to-be-Done on B2B contactpage
B2B visitors arrive with ONE of:
1. **Sales-evaluation contact** — "I want to talk to sales about [solution]"
2. **Support contact** — "I have a problem with my existing service"
3. **Partner inquiry** — "We want to reseller/integrate"
4. **Media/press inquiry** — "I need a quote for an article"
5. **Account-management contact** — "I'm an existing customer, need help with renewal/expansion"
6. **General inquiry** — "I'm not sure who to talk to, just want info"

A well-designed B2B contactpage serves multiple jobs without forcing one path.

**Important Dutch translation:** never use "huren" for JTBD framing. Use "kiezen voor", "inzetten voor", "implementeren om X op te lossen".

---

## Category 1: Above-the-fold contact-clarity & response-belofte

### Nielsen Norman contact-page UX (B2B)
Above-the-fold must answer in 5 seconds:
- WAT contact-routes available
- WIE handles each (sales, support, partner)
- WANNEER does visitor get response
- HOE does the visitor proceed

### Forrester B2B buyer expectations
B2B visitors at contactpage are late-stage:
- They've evaluated, now ready to engage
- Vague hero ("Get in touch") forces second-guess
- Specific routing-clarity reduces drop-off 15-25%

### B2B response-time research (Marketing Sherpa)
- Specific time-anchors ("4 business hours") outperform vague ("soon") by 30-50%
- Business-hours-context outperforms 24/7-promise (more credible for B2B)
- "Same business day" beats "ASAP"

### Best practices
- Headline clarifies contact-routes ("How can we help?" with sub-routes visible)
- Specific response-time-commitment per route ("Sales responds within 4 business hours")
- Primary route visible (typically sales for marketing-driven traffic)
- Footer/secondary routes accessible (support, partner, media)

### Common failures
- Generic "Get in touch" hero
- No response-time visible
- Single form for all contact-types (forcing routing ambiguity)
- Brand-poetry hero ("We'd love to hear from you") without action

### B2B-service-type calibration
- SaaS low-ticket: sales-route dominant, support-link secondary
- Enterprise SaaS: sales / support / partner / AM all visible
- Consultancy: project-inquiry vs general-inquiry distinction
- Managed services: support emergency-route critical (often above-the-fold)

---

## Category 2: Account-routing (sales / support / partner / media)

### B2B sales-routing research
Routing-economics on contactpage:
- 30-50% of "contact-form" submissions on single-route B2B pages are misrouted (support questions to sales, sales questions to general inbox)
- Each misroute costs sales-team or support-team 15-45 minutes to triage and re-route
- For 100 contacts/month, misrouting can waste 25-75 hours/month of sales/support time

### Lead-routing economics
Per misroute cost:
- Sales-team time wasted: €50-150 per misroute (at €100/hour loaded cost × 0.5-1.5 hours)
- For 50 misroutes/month: €2.500-€7.500 in wasted sales-capacity monthly
- Routing-UI fixes typically ROI in 1-2 months

### Forrester B2B self-service patterns
- 73% of B2B buyers prefer self-service for clear-route situations
- Mismatched routing forces unwanted contact-form-submission (visitor knows it's wrong, submits anyway)
- Clear routing reduces support-contact-attempts AT THE CONTACTPAGE-LEVEL

### Best practices
- 3-5 visible contact-routes max (sales / support / partner / media / general)
- Each route has clear label + brief description + own CTA
- Visual differentiation (cards, columns, distinct iconography)
- Existing-customer redirect ("Already a customer? Login to support portal →") visible

### Common failures
- Single generic "Contact us" route
- All routes funneling to same form (effectively single-route)
- Routes labeled in jargon ("BDR contact" — visitor doesn't know what BDR is)
- Support route absent on services with ongoing customer-relationships
- Partner route absent on partner-ecosystem businesses

### B2B-service-type and organization-size calibration
- MKB-B2B (small team): 1-2 routes (sales + general) often sufficient
- Mid-market B2B: 3 routes (sales / support / partner)
- Enterprise B2B: 4-5 routes (+ AM + media)
- Consultancy: project-inquiry vs general-inquiry
- Managed services: emergency-support route prominent

### Default Impact calibration (apply this)
- Generic-single-route on enterprise B2B with multiple business-units: ICE-Impact 7-8 (push to Critical)
- Missing support-route on managed-services with active customer-base: ICE-Impact 6-7 (Important+)
- Sub-optimal routing-labels: ICE-Impact 4-5 (Important/Nice)
- Routing exists, could be sharper: ICE-Impact 4-6 (Important)

---

## Category 3: Multi-stakeholder routing & visitor-rol calibration

### Challenger Sale multi-stakeholder framework
Different visitor-roles need different next-steps:
- Economic buyer: "Schedule pricing discussion"
- Technical buyer: "Speak with solutions engineer"
- End-user: "See product demo / training"
- Champion: "Get discovery call" or "Internal-sell collateral"

### MEDDIC role-identification on contactpage
Light role-routing:
- Role-tagged routes ("For IT teams: technical contact" vs "For business leaders: business-impact contact")
- Brief role-routing helps visitors self-select
- Don't over-engineer — too many role-options paralyzes

### B2B persona-routing research
- Role-based routing on contactpage lifts qualified-contact rate 5-15%
- Effect is moderate, not transformative — most B2B contactpages can skip this
- Highest impact for enterprise SaaS with complex multi-stakeholder buying

### Best practices (when applicable)
- 2-3 role-routes max (don't fragment to 6+ personas)
- Role-labels in visitor-language (not internal-jargon)
- Optional, not required (visitor can also use general route)

### Common failures
- Forced role-selection before form
- Too many role-options (paralysis)
- Internal-jargon labels ("For C-level economic buyers")
- Role-routing on MKB-B2B page where it's unnecessary

### Default Impact calibration (apply this — light weight)
- Most findings here: ICE-Impact 4-6 (Important to Nice-to-have)
- Push to ICE-Impact 7+ only if visible high-value lead-misdirection
- Many B2B contactpages don't need role-routing at all — mark category as "checked, brief observation"

### B2B-service-type calibration
- Enterprise SaaS with complex buying-committee: role-routing relevant
- Consultancy: project-type routing instead of role-routing
- Professional services: rarely role-routing needed
- Managed services: technical vs business contact relevant

---

## Category 4: Telefonische bereikbaarheid & sales-team response-windows

### Baymard tap-to-call research (B2B-adapted)
On mobile B2B contactpages:
- Tap-to-call lifts phone-conversion 10-25% (vs 15-30% on B2C — B2B mobile-share lower)
- Phone-number prominent in header / hero acceptable
- Business-hours context essential

### B2B response-window research
B2B sales-teams typically operate:
- Business hours only (Ma-Vr 9-17 or similar)
- Time-zone matters for international teams
- Response within 1-4 business hours is industry-standard
- "We respond within 24 hours" is acceptable for most B2B

### Marketing Sherpa response-time-promise impact
- "Sales responds within 4 business hours Ma-Vr" lifts form-completion 8-15%
- Specific times beat vague ("snel reactie")
- Business-hours-context outperforms 24/7 (more credible)

### Best practices
- Phone number visible (header, hero, or dedicated section)
- Tap-to-call on mobile
- Business-hours explicit
- Response-time-commitment per route
- Time-zone context for international teams
- Optional: "After-hours? Submit form for next-business-day response"

### Common failures
- Phone hidden in footer only
- Phone visible but plain text on mobile (no tap-to-call)
- No business-hours context (24/7 implication is misleading for B2B)
- No response-time-commitment
- Vague "We'll get back to you" without time-anchor

### B2B-service-type calibration
- Enterprise SaaS: phone often secondary (form-driven), AE follow-up
- Consultancy: phone PROMINENT (relationship-driven)
- Professional services: phone primary (formality + relationship)
- Managed services: emergency-phone-line + business-hours-line distinction
- SaaS low-ticket: phone optional (self-service-oriented)

---

## Category 5: Form-design met sales-routing kwalificatie

### Baymard form-field research (B2B-adapted)
On B2B contactpage form, the "every field costs 7-11%" rule applies BUT:
- BANT-light qualification can be acceptable (5-7 fields)
- Routing-field critical (visitor-need dropdown enables back-end routing)
- Optional fields better than required-asterisks-on-all

### BANT-light on contactpage form
Acceptable contactpage fields (5-8 fields):
1. Naam (verplicht)
2. Work-email (verplicht — filter gmail.com voor B2B-qualification)
3. Bedrijfsnaam (verplicht)
4. Role/titel (dropdown — routing-field)
5. Bedrijfsgrootte (dropdown — qualification-light)
6. Use-case (dropdown — routing-field)
7. Bericht / vraag (textarea, verplicht)

Save full MEDDIC for dedicated demo-LP forms, not contactpage.

### CXL form-friction research (B2B-calibrated)
- Single-column form better than multi-column
- Labels above inputs (not placeholder-only)
- Real-time validation outperforms submit-time
- AVG/GDPR-checkbox compact

### Best practices
- 5-7 fields max on standard contactpage form
- Required-only marking (not asterisks on every field)
- Routing-dropdowns to enable back-end CRM-routing
- Action-oriented submit-button ("Send to sales team" beats "Submit")
- Privacy reassurance near submit
- Response-time-promise near form

### Common failures
- 10+ field BANT-form on contactpage (over-qualification for inquiry-stage)
- 3-field form on enterprise contactpage (under-qualification)
- Placeholder-only labels
- Submit-time validation
- Generic "Submit" CTA
- Multi-column form on mobile

### B2B-service-type and organization-size calibration
- MKB-B2B / low-ticket SaaS: 4-5 fields acceptable (faster cycle, less qualification needed)
- Mid-market B2B: 5-7 fields with BANT-light
- Enterprise B2B: 7-10 fields acceptable (qualification ROI higher)
- Consultancy: 5-7 fields with project-type field

---

## Category 6: WhatsApp / chat / messaging kanalen

### Chat-widget impact research
Live-chat on B2B contactpage:
- Lift contact-conversion 15-40% on appropriately-fit B2B contexts
- Drop trust 5-15% on inappropriately-fit B2B contexts (enterprise, formal)
- Effect depends heavily on brand-formality and target-audience

### B2B chat-vs-formality calibration
**Chat-acceptable contexts:**
- Mid-market SaaS with mid-formality audience
- MKB-B2B service-providers
- Time-sensitive B2B (managed-IT, support-services)
- B2B service-businesses with younger doelgroep

**Chat-often-unwelcome contexts:**
- Enterprise SaaS with CFO/CSO targeting
- Professional services (legal-B2B, accountancy targeting businesses)
- Regulated industries (financial services compliance)
- High-trust formal-tone brand-positioning

### Forrester live-chat conversion research
- Generic chat-widgets (Intercom, Drift) work for self-service-oriented B2B
- AI-chatbots have mixed reception — useful for FAQ, risky for sales-routing
- Human-chat with business-hours commitment outperforms 24/7 promises in B2B

### Best practices (when chat appropriate)
- Chat-widget bottom-right (standard position)
- Business-hours visible in chat-status
- Quick-reply options for common routes ("Talk to sales" / "Support question")
- Handoff to form if chat-team unavailable
- Response-time-commitment in chat-status

### WhatsApp in B2B-context
- WhatsApp Business acceptable for MKB-B2B
- WhatsApp typically NEE for enterprise B2B (formality mismatch)
- Pre-filled bericht-templates if used

### Common failures
- Enterprise B2B with overly-casual chat (formality mismatch)
- 24/7 chat-promise that's not delivered
- AI-chatbot routing sales-leads incorrectly
- Chat-widget blocking primary CTA on mobile
- WhatsApp on formal-professional-services brand

### B2B-service-type calibration
- SaaS low/mid-ticket: chat-acceptable, often recommended
- Enterprise SaaS: chat-questionable, calibrate to brand
- Consultancy: chat-acceptable for mid-market consultancy, less for premium
- Professional services: chat-rarely-fit
- Managed services: support-chat often-fit, emergency-chat-line possible

---

## Category 7: Office-locaties & vestigingen

### B2B-trust-signal research (Edelman)
Office-presence on contactpage:
- Physical-office credibility = "real company, not fly-by-night"
- Multi-office presence = "established, scalable"
- Visible address-information lifts trust significantly
- Hidden or unclear addresses raise trust-concerns

### Office-presence-as-credibility patterns
On contactpage:
- Hoofdkantoor address visible (NAP-consistent with Google Business)
- Regional offices listed if applicable
- Embedded Google Maps optional
- Routebeschrijving useful for visitor-bezoek

### Multi-office routing research
For multi-office B2B (regional sales, sector-teams):
- Per-office contact-info acceptable but can fragment
- "Find the right office for you" routing helps
- International offices: country-routing useful

### Best practices
- Hoofdkantoor address prominent
- Multi-office: visual list or map
- Per-office: address + phone + business-hours
- Optional: embedded Google Maps
- NAP-consistency with Google Business

### Common failures
- No office-address visible on contactpage
- Generic "We have offices worldwide" without specifics
- Address-only without phone/hours per office
- NAP-inconsistency with Google Business

### B2B-service-type calibration
- Enterprise SaaS: multi-office relevant (sales-territories)
- MKB-B2B: single hoofdkantoor sufficient
- Consultancy with multi-office: per-office contact relevant
- Online-only services: hoofdkantoor for trust-anchor, but no map needed

---

## Category 8: Trust signals & B2B credibility (compact)

### B2B trust-signal calibration on contactpage
On contactpage, trust signals are SUPPORTING (not dominating):
- Compact strip (3-5 elements)
- Customer-count or named-customer (compact)
- Certifications relevant to anxiety (SOC 2, ISO 27001 for SaaS; KvK/BTW for NL-business)
- Industry-membership badges

### Cialdini authority (compact)
On contactpage, authority signals work as trust-rails along the conversion path:
- Above-the-fold: customer-count or response-time-promise
- Near form: certifications-relevant-to-anxiety
- Footer: legal-trust (KvK, BTW, privacy)

### Best practices
- Trust-strip near form OR below hero
- 3-5 critical signals
- Anxiety-targeted
- Industry-relevant only
- Compact, not dominating

### Common failures
- Trust signals dominating (contactpage becomes trust-wall)
- Generic certifications without context
- KvK/BTW absent (NL commercial sites)
- Self-claims without third-party validation

---

## Category 9: FAQ & B2B contact-specifieke objection handling

### MECLABS anxiety axis (B2B contactpage-adapted)
Contact-specific B2B anxieties:
- "Will I get a sales-pitch instead of a useful conversation?"
- "How long until response?"
- "Am I contacting the right team?"
- "Will my contact-info be added to spam-list?"
- "Will I commit to something by submitting this?"

### Pre-emptive objection handling
Best B2B contactpages address objections BEFORE they form:
- Inline microcopy at form ("We use your info only to respond to this inquiry")
- FAQ section addressing top contact-specific questions
- Response-time-clarity near every contact-option

### Best practices
- Microcopy at form addressing top anxieties
- Short FAQ (3-5 questions) contact-specific
- Categories: response-time, what-happens-next, privacy, no-sales-pitch-promise
- AVG-compliance microcopy compact and clear

### Common failures
- Generic FAQ unrelated to contact-anxieties
- No privacy-reassurance at form
- No "what happens next" clarity
- FAQ-jargon ("Will we route via our SDR funnel?" — visitor doesn't know SDR)

### B2B-service-type calibration
- SaaS: "Will I be added to a marketing list?" common anxiety
- Consultancy: "Is this a free intake or paid consultation?"
- Professional services: "What's the first-step process?"
- Managed services: "Is this for support or sales?"

---

## Category 10: Account-management contact

### Enterprise SaaS CSM patterns
For enterprise SaaS with dedicated CSM-model:
- Existing customers expect named-AM contact
- AM-contact distinct from new-business-sales-contact
- CSM-portal login link visible
- "Already a customer?" routing prominent

### Customer-success contact-routing
- Self-service portal-login prominent for existing customers
- Account-management-team contact-info visible
- Renewal/expansion discussions routed to AM
- Onboarding-questions routed to CSM

### Best practices (when applicable)
- "Existing customer?" routing visible
- AM/CSM contact-info distinct from sales-contact
- Portal-login link prominent
- Renewal/expansion-question routing

### Common failures (when applicable)
- AM-contact buried (existing customers route to sales-team accidentally)
- No portal-login link
- Generic support-route catches AM-conversations

### Default: not-applicable
For most B2B audits, mark this category:
**"Category checked, no finding — not applicable to this business-type"**

This is EXPECTED for:
- MKB-B2B
- Consultancy / agency
- Professional services
- B2B managed services
- B2B suppliers without dedicated AM-model

Only audit findings here for enterprise SaaS with visible CSM-model.

---

## Category 11: Mobile experience

### Baymard mobile research (B2B-context)
B2B contactpage mobile patterns:
- 40-55% mobile traffic on B2B contactpages (lower than B2C)
- Mobile conversion lags desktop on B2B (research-mode-mobile, conversion-mode-desktop)
- Tap-to-call critical on mobile
- Mobile form-friction higher impact (longer forms harder on mobile)

### Mobile contact-page patterns
- Sticky bottom-CTA acceptable
- Tap-to-call phone-numbers
- Mobile-optimized form (single-column, large fields)
- Office-map mobile-lightweight

### Best practices
- Mobile-first hero with key routes visible
- Tap-to-call live on mobile
- Form mobile-optimized
- Sticky bottom CTA option
- Fast page load

### Common failures
- Desktop-only optimization
- Phone visible but plain-text on mobile
- Multi-column form on mobile
- Heavy map-embed slowing load
- No sticky CTA on long-form mobile

---

## Brand and B2B-service-type calibration notes

Always recalibrate by brand snapshot AND B2B-service-type AND organization-size:

**Example: Hero content**
- MKB-B2B consultancy: warm hero, phone + form-CTA prominent
- Mid-market SaaS: "Talk to sales / support" routing-cards hero
- Enterprise SaaS: "Sales / Support / Partners / Press" full-routing hero
- Professional services: formal hero, "Contact your relationship manager / new-client inquiry" routing

**Example: Chat/WhatsApp**
- MKB-B2B managed-IT: WhatsApp emergency-line acceptable, chat-widget useful
- Enterprise SaaS: human-chat OK with business-hours, AI-chatbot risky
- Professional services targeting CFOs: chat/WhatsApp questionable
- Government/public-sector B2B: chat/WhatsApp NEE

**Example: Form-length**
- MKB-B2B: 4-5 fields acceptable
- Mid-market B2B: 5-7 fields with BANT-light
- Enterprise B2B: 7-10 fields acceptable

Recommendations that don't match brand AND service-type AND organization-size zijn fout.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites a specific principle, study, or source
- [ ] Recommendation is concrete (exact copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric is named (total contact-conversion / sales-form completion / routing-accuracy / response-time accuracy)
- [ ] ICE justified by I/C/E breakdown with category-specific calibration
- [ ] Account-routing finding calibrated to Important default unless visible mismatch
- [ ] Multi-stakeholder routing finding calibrated to Important/Nice default
- [ ] Account-management finding only included for applicable business-type
- [ ] Recommendation matches brand snapshot AND B2B-service-type AND organization-size
- [ ] Decision-maker context respected (no consumer-style recommendations)
- [ ] Sales-team-time-cost context applied to lead-quality recommendations
- [ ] WhatsApp/chat recommendations calibrated to brand formality
- [ ] Dutch output: no "huren" check
- [ ] No authenticity claims about phone/routing/response-time without evidence

If any box unchecked, rework or remove the finding before delivering.
