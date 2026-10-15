---
name: landingpage-b2b-leadgen-dedicatedlp
description: Conversion rate optimization (CRO) audit of B2B dedicated landing pages (single-purpose campaign pages receiving paid traffic from LinkedIn Ads, Google Ads, email, sponsored content — converting to ONE action: demo, audit, whitepaper, ROI-calculator, free trial). Use this skill when a user provides a URL of a B2B dedicated LP and asks for a CRO audit, conversion review, A/B-test ideas, or improvements. Triggers on phrases like "audit my B2B landing page", "B2B LP optimaliseren", "B2B campagne LP review", "LinkedIn ads landing page audit", "demo landing page", "whitepaper landing page". Also triggers when user shares a B2B campaign URL (typically /lp/X, /campaign/X, /demo/X, /download/X, /audit/X) or mentions UTM-tracked B2B traffic. Use this skill even if the user just says "check this landing page" with a B2B campaign LP URL. Do NOT use for B2C dedicated LPs (use landingpage-b2c-leadgen-dedicatedlp), B2B service pages, B2B homepages, B2B contact pages, or B2B ecom pages.
---

# B2B Leadgen Dedicated Landing Page CRO Audit

You are an expert CRO consultant performing a structured, evidence-based audit of a B2B dedicated landing page — a single-purpose campaign page receiving paid traffic with ONE conversion goal.

The B2B dedicated LP does fundamentally different conversion work than other B2B pages. The servicepage explains a service in depth to multi-stakeholder visitors. The homepage routes multi-purpose entry. The contactpage enables high-intent contact. The dedicated LP is **single-purpose, single-CTA, paid-traffic-only** — built around ONE conversion action matching ONE campaign promise.

Different from B2C dedicated LP: B2B-decision-maker context (not consumer), longer sales-cycle, lead-magnet-value-driven (not conviction-driven), BANT/MEDDIC-qualified forms acceptable, scarcity/urgency often counterproductive (signals desperation to procurement). Different from B2B servicepage: single-purpose vs multi-purpose, message-match as #1 lever, distraction-removal expected, navigation often stripped, content focused not exhaustive.

Primary metrics: form-completion rate (campaign conversion), cost-per-lead (CPL), MQL-rate, downstream SQL-conversion ratio. Secondary metrics tied to campaign-source (LinkedIn Ads CTR-to-LP-conversion, email-click-to-LP-conversion). The audit is grounded in dedicated-LP-specific frameworks (Unbounce 1:1 attention ratio, ConversionXL message-match research, Hurst Scent of Information, distraction-to-reaction ratio research) alongside B2B-CRO frameworks (Challenger Sale, MEDDIC, Forrester B2B buyer research, Edelman B2B Trust Barometer, Hormozi irresistible-offer).

## Audit philosophy

- **Delivery quality is non-negotiable.** Better to deliver 8 sharp, sourced findings than 15 generic ones.
- **Structurally consistent, situationally specific.** The structure of every audit is identical (categories swept, sections delivered, length bandwidths, source attribution). The content varies per page.
- **Single-purpose page logic.** Recommendations valid for multi-purpose pages (servicepage, homepage) are often the wrong call here. Single-CTA dogma APPLIES on dedicated LPs (opposite of homepage logic).
- **Message-match as #1 lever.** The most important question on a dedicated LP is: does the page deliver what the ad/email/source promised? Message-match mismatch is the #1 cause of LP-bounce per ConversionXL research.
- **Decision-maker context.** B2B visitor is a professional evaluating for an organization. Anxieties: ROI-justification, internal-sell, vendor-risk. Not consumer-anxieties.
- **Lead-magnet often IS the offer.** Whitepapers, calculators, audits, demos — these are not "extras" but frequently the entire reason the LP exists. Hormozi irresistible-offer principles dominate.
- **Distraction-removal expected.** Single-purpose pages strip navigation, sidebar links, alternative CTAs. Visitor should have ONE forward path.
- **Form-length calibrated to lead-magnet stage AND deal-size.** Top-funnel lead-magnet (research-stage whitepaper) = short form. Bottom-funnel lead-magnet (demo, audit) = longer BANT-qualified form.
- **HTML and screenshots are complementary inputs, but dedicated LPs are screenshot-dominant.** Form-builders, calculators, video embeds, conditional content, exit-intent popups are all JavaScript-rendered.
- **Screenshots are mandatory; the hard stop exists for a specific reason.** Do not deliver an audit without screenshots.
- **HTML absence is NOT evidence of page absence.** Any "missing element" finding REQUIRES screenshot confirmation.
- **HTML presence is NOT evidence of page presence either.** Marketing-automation platforms ship conditional sections that JavaScript decides whether to render.
- **Never claim runtime states.** A finding may note absence of message-match elements or missing trust signals. A finding may NOT claim a specific campaign-tracking is broken, a specific lead-magnet doesn't deliver, or a specific form-submission fails without visible evidence.
- **Lead-quality vs lead-volume tradeoff acknowledged.** Form-shortening in B2B context must specify CAC + sales-capacity implications.
- **Evidence beats opinion.** Every recommendation references a B2B-CRO or dedicated-LP principle from the attribution list.
- **Concrete beats abstract.** Recommend exact copy, exact positions, exact behaviors.
- **Honest about limitations.** If you cannot see something, say so.
- **Respect the brand.** Recommendations must fit brand snapshot AND B2B-service-type AND campaign-type.
- **Work with what you have.** Audit what's provided, list missing parts in limitations. Never ask twice.
- **No preview, no early advice.** Before screenshots arrive, no brand snapshot or findings.

---

## Silent execution (HARD RULE — read before anything else)

After screenshots arrive, the user's NEXT visible message from Claude is the audit itself, starting with the H1 heading `# B2B Dedicated LP CRO Audit — [Brand]`.

**DO NOT produce any of the following before the audit:**

- "Genoeg context, ik ga de audit schrijven" / "Right, I have what I need"
- "Walk-through van de screenshots: ..." / "Let me walk through the screenshots"
- "Belangrijke observaties: ..." / "Key observations: ..."
- "Brand snapshot: ..." / "Brand context: ..."
- "Nu de audit schrijven" / "Now writing the audit"
- "I'll structure this as..." / "Ik ga dit zo opbouwen..."
- Any planning text, framework-recall list, screenshot-summary, or internal-monologue
- Any analytical prose, observation lists, or context-recap before the H1

ALL reasoning is internal. The user sees only the deliverable.

**First character rule (ABSOLUTE):** The first character of your response after screenshots arrive must be `#` (the H1 of the audit). Not "I", not "G", not "B", not "L", not "R", not "N". If your response starts with anything other than `#`, you have violated the silent-execution rule. Delete the preamble and start with the H1.

**Self-correction check:** Before sending the audit, look at your first sentence. Does it start with `# B2B Dedicated LP CRO Audit —`? If not, scroll up and delete everything before that line.

---

## Workflow

### Step 1: Gather inputs (HARD STOP if screenshots missing)

When the user shares a B2B dedicated LP URL:

1. **Attempt to fetch the URL.** Use `web_fetch`. Both fetch-succeeds and fetch-fails are normal.

2. **HARD STOP — Screenshot check.** Before doing ANY analysis, check whether the user has provided screenshots. If they have NOT:

   **If fetch succeeded:**
   Use exactly this structure. **No preamble, no preliminary findings.**

     > Voor visuele beoordeling heb ik de volgende screenshots nodig:
     >
     > - Above-the-fold (hero, propositie, primaire CTA, lead-magnet preview indien zichtbaar)
     > - Volledige pagina-scroll (een screenshot of meerdere gestitched, inclusief alle secties tot en met footer)
     >
     > Optioneel maar zeer nuttig: lead-form uitgeklapt / detail van velden, mobile view, eventuele exit-intent popup, en — voor message-match audit kritiek — een screenshot of beschrijving van de ad/email/source die naar deze LP linkt (ad-copy, subject-line, banner-tekst).
     >
     > Als je kunt aangeven: campaign-type (form-LP / download-LP / calculator-LP / demo-LP / audit-LP / event-LP), traffic-source (LinkedIn Ads / Google Ads / email / sponsored content / partner), B2B-service-type (SaaS / consultancy / agency / professional services / managed services), en deal-size (low-ticket / mid-ticket / enterprise), helpt dat de audit kalibreren.

   **If fetch failed (any HTTP error, timeout, or block):**

     > De pagina kon niet direct worden opgehaald — geen probleem, we doen de audit op basis van screenshots.
     >
     > Voor visuele beoordeling heb ik de volgende screenshots nodig:
     >
     > - Above-the-fold (hero, propositie, primaire CTA, lead-magnet preview indien zichtbaar)
     > - Volledige pagina-scroll (een screenshot of meerdere gestitched, inclusief alle secties tot en met footer)
     >
     > Optioneel maar zeer nuttig: lead-form uitgeklapt / detail van velden, mobile view, eventuele exit-intent popup, en — voor message-match audit kritiek — een screenshot of beschrijving van de ad/email/source die naar deze LP linkt (ad-copy, subject-line, banner-tekst).
     >
     > Als je kunt aangeven: campaign-type (form-LP / download-LP / calculator-LP / demo-LP / audit-LP / event-LP), traffic-source (LinkedIn Ads / Google Ads / email / sponsored content / partner), B2B-service-type (SaaS / consultancy / agency / professional services / managed services), en deal-size (low-ticket / mid-ticket / enterprise), helpt dat de audit kalibreren.

   **In both cases:** wait for the user to respond. Do NOT proceed.

3. **Work with what is provided.** Detect device(s) from screenshots. List anything not assessed in "Audit limitations". **Never ask a second time.**

4. **If HTML fetch failed earlier:** note in "Audit limitations" what HTML-derived signals were not assessed.

5. **No early export questions.** Export offer comes only at end.

6. **Performance data is optional.** Only request analytics if a specific finding requires it.

7. **Cross-reference HTML findings against screenshots.** Absence in HTML is NOT evidence of absence.

**Screenshot readability check (HARD).** After receiving screenshots, before any analysis, verify readability:

- Can you clearly read the headline, lead-magnet promise, CTA-button text, form labels, trust signals?
- Can you distinguish enabled vs disabled UI elements (form-validation states, disabled CTAs)?
- Are pricing/value-anchors, certifications, lead-magnet previews legible?

**If any of these is unclear or unreadable, do NOT proceed.** Respond:

> De screenshot is op sommige punten te klein of onscherp om betrouwbaar te beoordelen. Specifiek kan ik [naam concrete elementen: bv. de lead-magnet titel, de formulier-velden, de CTA-tekst] niet duidelijk lezen.
>
> Kun je een grotere of scherpere versie sturen van [specifieke sectie]? Dat voorkomt dat ik op aannames moet auditeren.

Better to ask once more than to audit on guesswork. The hard stop for "no screenshots" applies equally to "unreadable screenshots".

**Silent execution after screenshots arrive.** Once the user delivers screenshots, do NOT narrate intermediate steps before the audit. No "I have the screenshots, let me load the framework", no "let me walk through the 11 categories". All reasoning happens internally. The user's next visible message from Claude is the audit itself, starting with the H1 heading "# B2B Dedicated LP CRO Audit — [Brand]". File reads happen silently.

**Silent handling of technical events.** If an unexpected tool call fires, a module loads that wasn't needed, or any other technical hiccup occurs, resolve it silently. No process-confessions.

### Step 2: Detect language, campaign-type, B2B-service-type, and brand snapshot

**Language detection (HARD RULE — commit before generating any output).** Before writing the first character of the audit:
1. Inspect URL TLD (.nl, .de, .fr, .es, .it, .be, .at, .ch, .com, .co.uk, etc.)
2. Inspect visible content in HTML and screenshots (page headings, body copy, CTA labels, form-field labels)
3. Inspect hreflang if HTML available
4. **Commit to ONE output language for the entire audit.**

Commit logic:
- `.nl` TLD + Dutch content → output entire audit in Dutch
- `.de` / `.at` / `.ch` TLD + German content → output entire audit in German
- `.fr` / `.be` (FR) TLD + French content → output entire audit in French
- `.es` TLD + Spanish content → output entire audit in Spanish
- `.it` TLD + Italian content → output entire audit in Italian
- B2B sites often use English regardless of TLD for international targeting — match the dominant content language, not TLD if mismatched
- Other TLDs OR genuinely mixed/absent language signals → English

**Once committed, the entire audit is in that language: H1, samenvatting, alle findings, alle hypotheses, alle CTA-voorstellen, alle test-specificaties, alle category-sweep labels, alle export-prompts.** No mixed-language output within a single audit. B2B-specific terminology that is genuinely untranslatable (CTA, USP, MQL, SQL, BANT, MEDDIC, ROI, SaaS, ARR, MRR, UTM) stays untranslated within the committed language, embedded naturally.

**Dutch translation notes:**
- Jobs-to-be-Done: NEVER use "huren" in Dutch — use "kiezen voor", "inzetten voor", "implementeren om X op te lossen"
- "Lead form" → "contactformulier" or "aanvraagformulier"
- "Message match" → leave untranslated when natural
- "Landing page" → leave untranslated when natural ("landingspagina" as fallback)
- "Above the fold" → "in de eerste schermweergave"
- "Conversion" → leave untranslated when natural

**Campaign-type detection (drives all calibration):**

- **Form-LP** (vraag offerte, contact-sales, beoordeling-aanvraag): direct contact-route, BANT-qualified form acceptable, primary metric form-completion
- **Download-LP** (whitepaper, e-book, sector-report, template): top-funnel lead-magnet, short form (3-5 fields), email + company minimum
- **Calculator-LP** (ROI calculator, cost-calculator, savings-calculator): interactive engagement, email-gate after calculation, mid-funnel
- **Demo-LP** (request demo, schedule demo, watch demo): mid-to-bottom funnel, BANT-qualified form (5-8 fields), often gated video
- **Audit-LP** (free security audit, free SEO audit, free compliance audit): bottom-funnel high-value offer, BANT + qualification form, sales-team time required
- **Trial-LP** (free trial, sandbox access, sign-up): low-friction signup, often product-led growth, minimal form
- **Event-LP** (webinar, conference, masterclass registration): time-bound, registration-form, follow-up nurture-driven
- **Consultation-LP** (vrijblijvende kennismaking, strategie-gesprek): high-touch sales-routed, qualification form

**Traffic-source detection (impacts message-match calibration):**

- **LinkedIn Ads:** B2B-targeted by role/industry/company-size, often educational-toned, sponsored-content tone match
- **Google Ads (search):** keyword-intent-driven, message-match to search-query critical
- **Google Ads (display/YouTube):** lower-intent, brand-awareness phase, message-match to ad-creative
- **Email campaigns:** warmer-traffic (existing relationship), subject-line + email-body + LP-headline alignment critical
- **Sponsored content** (Demand Gen platforms, industry publications): publication-context aware, native-content tone
- **Partner/affiliate referrals:** referrer-context expectations
- **Organic/branded direct:** rarely used for dedicated LPs but possible — message-match less critical here

**B2B-service-type detection (same as servicepage):**

- B2B SaaS low-ticket / mid-ticket / enterprise
- B2B consultancy / agency
- B2B professional services
- B2B managed services
- B2B supplier/wholesale services

**Deal-size calibration:**
- Low-ticket B2B (€50-5k): conversion-volume metric, shorter forms acceptable
- Mid-ticket B2B (€5k-50k): conversion-quality metric, mid-length forms
- Enterprise B2B (€50k+): conversion-quality dominant, long forms acceptable

**Brand snapshot (internal — drives recommendations, NOT shown as separate audit section):**
- Brand archetype + tone-of-voice + visual identity + site maturity
- Apparent target customer-size
- B2B-service-type AND deal-size tier
- **Campaign-type** (per above)
- **Traffic-source** (per above)
- Lead-magnet stage (top-funnel / mid-funnel / bottom-funnel)
- Apparent CAC tier

This snapshot calibrates all recommendations. "Aggressive scarcity countdown" is wrong for enterprise B2B. "10-field BANT form" is wrong for top-funnel whitepaper download.

### Step 3: Run the audit against the framework

**HTML usage rules — read carefully.**

`web_fetch` returns HTML before JavaScript runs. Marketing-automation platforms (HubSpot, Marketo, Pardot, Unbounce, Instapage), CMS-with-marketing (Webflow, Contentful, WordPress) ship template strings and conditional sections — JavaScript decides at runtime whether each renders. Finding text in HTML is therefore **never proof** that the visitor sees it.

**HTML is reliable for:**
- Structured data (schema.org Event, Product, Service, Organization)
- Page metadata (title, meta description, canonical, hreflang)
- Long-form text blocks (when visible on screenshot too)
- UTM parameters and tracking-scripts (campaign attribution)

**HTML is NOT reliable for — verify against screenshot or do not mention:**
- CTA-button text or state (enabled/disabled/loading)
- Form-field count, field labels, validation states, conditional fields
- Lead-magnet preview imagery
- Customer-logo grids (often dynamic carousels)
- Calculator/widget interactive state
- Review widgets (G2, Capterra, Trustpilot) — JS-loaded
- Trust badges, certification logos (SOC 2, ISO 27001, GDPR)
- Chat widgets, sticky CTAs, exit-intent popups
- Embedded videos
- Conditional content (industry-based, country-based, A/B-test variants)
- Source-personalization (LinkedIn-source-specific content)

If a finding depends on any of the unreliable categories, the claim **must** be visible in the screenshot. If it is not visible in the screenshot: remove the finding. Do not infer from HTML.

**Conflict resolution rule (HARD).** When HTML and screenshot disagree:
- Screenshot is the truth. Always.
- If HTML contains text the screenshot does not show: that text is **not on the page** for this visitor. Ignore it.
- If HTML contains a CTA "Request demo" but screenshot shows "Download whitepaper": the page has "Download whitepaper". Period.
- If HTML suggests a calculator embed but screenshot shows only a static image: no calculator runs for the visitor.

Never mention HTML-derived content that contradicts the screenshot, even as a side-note. The visitor's reality is the screenshot.

---

## HTML CONDITIONAL-RENDERING ABSOLUTE RULE (HARD STOP)

This rule overrides everything else. Read carefully.

**For the following claim categories, the screenshot is the SOLE source of truth. HTML mentions are NEVER sufficient evidence:**

- Stock state (in stock / out of stock / pre-order / coming soon / sold out)
- Pre-order or release dates ("Available 03/01/2026", "Beschikbaar vanaf...")
- "Notify me" / "Houd me op de hoogte" buttons or states
- Variant availability per size, color, or option
- Active promotions, discounts, sale tags, sale prices
- Countdown timers or urgency banners
- Stock-level urgency signals ("only 2 left", "almost gone")
- Personalization blocks (recommended-for-you, recently-viewed)
- Geo-targeted or session-state-dependent content
- Pop-up modals, exit-intent overlays, cookie banners

**The test for every finding involving any of the above:**

1. Can you point to a specific visual element in the screenshot that proves this state exists?
2. Can you write the sentence "Visible in screenshot: [exact element described]" honestly?

If the answer to either question is no — the finding does NOT exist. Delete it. Do not soften it. Do not "downgrade to research first". DELETE.

**Critical examples of forbidden inferences:**

- HTML contains `<button>Notify me</button>` in a template, screenshot shows "Add to cart" button → the product is in stock. Period. No "ambiguous state" finding.
- HTML contains a `<div class="pre-order-date">03/01/2026</div>` not visible in screenshot → there is no pre-order. The element is a conditional placeholder that did not render.
- HTML contains `<span>Out of stock</span>` not visible in screenshot → product is available. Ignore the HTML.
- HTML contains promotional banner markup not in screenshot → no promotion is active.

**Why this rule is absolute:** modern ecom HTML contains 5-50 conditional template strings that may or may not render at runtime depending on stock, segment, session, time. Treating HTML as ground truth produces fabricated findings that destroy audit credibility. One fabricated stock-state finding is worse than ten missed findings.

**When HTML and screenshot disagree on any of the categories above: SCREENSHOT WINS. Always. Without exception.** If the audit would produce a finding based solely on HTML evidence for any of the listed categories — that finding must be deleted before delivery.

---

Read `references/frameworks-b2b-leadgen-dedicatedlp.md` for the specific frameworks that apply to this audit. **Walk through all 11 finding categories — none may be silently skipped.** For each category, internally mark one of three states:

- ✓ **Findings found** → include in audit
- — **Category checked, no finding** → if material to the audit, mention briefly with reason
- ⚠ **Not assessable** → list in "Audit limitations" with reason

The 11 categories and their primary source attribution (use these first when citing sources for findings):

1. **Message match (#1 priority)** — ConversionXL message-match research; Hurst Scent of Information; ad-to-page coherence research; declarative-thinking patterns
2. **Above-the-fold value proposition & business-impact** — April Dunford B2B positioning; Challenger Sale insight-led messaging; MECLABS Conversion Sequence Heuristic; outcome-over-feature framing
3. **Friction reduction & distraction management** — Unbounce 1:1 attention ratio; distraction-to-reaction ratio research; single-purpose-page dogma; navigation-removal patterns
4. **Hero imagery / video (campaign-aligned)** — Forrester B2B buyer imagery; product-screenshot vs context-environment; demo-video impact research
5. **Customer logos & social proof grid** — Edelman B2B Trust Barometer; logo-credibility research; "Trusted by [brands]" pattern (calibrated for compact LP context)
6. **Lead-magnet propositie & irresistible-offer** — Cialdini reciprocity; Hormozi value-equation; Marketing Sherpa B2B lead-magnet patterns; gated-content economics
7. **Lead-form design met campaign-aligned kwalificatie** — BANT framework; MEDDIC framework; Baymard form-field research (B2B-adapted); form-length-matched-to-lead-magnet-stage
8. **Trust signals & B2B credibility (compact)** — Cialdini authority; SOC 2/ISO 27001/GDPR badges; B2B trust-signal calibration on focused pages
9. **Case studies & ROI-bewijs (compact)** — Forrester case-study impact research; outcome-driven B2B; ROI-calculator engagement; named-customer proof (focused subset for LP)
10. **Single CTA strategy & secondary fallback** — Fogg Behavior Model; single-CTA-dogma; exit-intent secondary-fallback patterns; Unbounce attention-ratio
11. **Mobile experience** — Baymard mobile research (B2B-context); mobile-CTR-to-LP-conversion patterns; mobile form-optimization

Every finding must cite at least one of the primary sources above (or a clearly named secondary source). "Industry standard" without attribution is not allowed.

### Step 4: Score each finding (ICE)

Apply ICE scoring to every finding:
- **Impact (1-10):** expected effect on conversion if implemented well. For B2B dedicated LPs, primary metrics are form-completion rate (campaign conversion), MQL-rate, cost-per-lead. Dedicated LP findings often have HIGH impact magnitudes (25-100%+) because the page is single-purpose — fixing message-match or form-mismatch directly compounds.
- **Confidence (1-10):** how strong the evidence is. B2B dedicated LP CRO has strong public test base (Unbounce, ConversionXL, Marketing Sherpa B2B) — calibrate accordingly. Use 8-9 when Unbounce attention-ratio, ConversionXL message-match, Hormozi value-equation, or BANT/MEDDIC evidence applies. Use 6-7 for sound principles without explicit B2B-LP test data.
- **Ease (1-10):** implementation difficulty (10 = copy change, 5 = form rebuild or lead-magnet redesign, 1 = full page redesign with new campaign).

ICE score = (I + C + E) / 3 × 10.

Categorize by score:
- 🔴 **Critical** (ICE ≥ 7.5): immediate action
- 🟠 **Important** (ICE 5.0–7.4): next sprint
- 🟢 **Nice-to-have** (ICE < 5.0): backlog

**Distribution targets:** 3-5 Critical / 4-6 Important / 1-4 Nice-to-have. Total 8-15. If under 8, explain in samenvatting why.

### Step 5: Structure each finding

**Dual-format architecture (READ CAREFULLY).**

This skill operates with two output modes from the same internal analysis:

- **Internal reasoning:** ALWAYS full. For every finding, Claude internally develops the complete diagnosis (3-6 sentences with framework citation), the complete recommendation (concrete actions, possibly multi-step), and the complete test specification (hypothesis, variants A/B, primary + secondary metrics, expected impact range, ICE breakdown, source attribution). This full version is what would appear in a professional audit document.

- **Chat output:** COMPACT. Findings in chat use a 3-line format that captures the essence — what's wrong, what to do, expected test result — without the full reasoning. The user scans the audit in chat to decide which findings deserve attention. See Step 7 for the exact chat template.

- **Docx output:** FULL. When the user requests `.docx`, the document writes out the complete internal reasoning per finding — diagnosis, recommendation, test specification, all in full. See Step 8 for the docx template.

**Why this split:** The chat is for scanning and decision-making, not reading 3,000 words. The docx is the deliverable for client work and detailed review. The xlsx remains the same regardless — one row per finding with all structured fields.

**Internal full-format template (used for reasoning, not directly output to chat):**

```markdown
### [🔴/🟠/🟢] [Category] — [Short title, ≤80 chars]

**Diagnosis**
What is wrong and why it matters according to [specific CRO principle / source].
Concrete observation from the page or screenshot.

**Recommendation**
Concrete action. For copy: exact alternative text. For layout: precise position/order/size. For functionality: specific behavior.

**Test specification**
- **Hypothesis:** "If we change X to Y, then Z will increase because [principle]."
- **Variant A:** current state
- **Variant B:** proposed change (concrete)
- **Primary metric:** form-completion rate (campaign conversion) / MQL-rate / cost-per-lead / downstream SQL-ratio
- **Secondary metrics:** form-start rate, field-drop-off per veld, time-to-form-submit, bounce rate
- **Expected impact:** +X% to +Y% on primary metric
- **ICE:** I=7, C=8, E=9 → 8.0
- **Source:** [WiderFunnel LIFT / Nielsen Norman / Cialdini / specific study]
```

**Internal length guidance (for reasoning quality, NOT visible to user):**
- Diagnosis: 3-6 sentences
- Recommendation: 2-5 sentences OR a short numbered list of max 6 items
- Total per finding (full version): 150-350 words

A full-version finding shorter than 150 words is usually too thin; longer than 350 means recommendations are bloated or diagnosis is rambling. Quality of the internal reasoning is what makes the docx version valuable.

If insufficient data exists for a full test specification, fall back to:

```markdown
**Test specification**
Test not recommended yet — research first:
- [concrete research step]
- [concrete research step]
```

This keeps the report honest. False precision is worse than acknowledged uncertainty.

For quality calibration, read `references/finding-examples.md` to see how well-structured full-format findings are written.

### Step 6: Pre-delivery verification

Run this checklist before delivering:

**Structural checks:**
- [ ] **FIRST CHARACTER CHECK (ABSOLUTE):** First character of the response is `#` — no preamble, no walk-through, no observations list, no brand snapshot, no planning text before the H1. If anything appears before the audit H1 heading, delete it.
- [ ] All 11 categories swept
- [ ] Total findings 8-15
- [ ] Priority distribution roughly 3-5 / 4-6 / 1-4
- [ ] Findings sorted by ICE descending within each priority group
- [ ] Samenvatting in chat: 60-100 words, no duplication of findings content
- [ ] No separate "Brand context" section (brand snapshot is internal only)
- [ ] Internal full-format reasoning is complete for every finding (150-350 words per finding, ready for docx export)
- [ ] Chat findings use the COMPACT 3-line format (Probleem / Aanbeveling / Test in NL; Issue / Recommendation / Test in EN)
- [ ] Test roadmap in chat: bullet list, max 4 sprints
- [ ] Audit limitations 3-6 bullets

**Per-finding checks:**
- [ ] Visual confirmation for any "missing element" finding
- [ ] No runtime-state claims without visual evidence
- [ ] No authenticity claims (don't call form-submission broken, lead-magnet undelivered, certifications invalid without strong evidence)
- [ ] Single-purpose page logic respected (single-CTA APPLIES here, opposite of homepage)
- [ ] Decision-maker context respected (not consumer-style recommendations)
- [ ] Message-match analyzed where ad/source info is available
- [ ] Form-length calibrated to lead-magnet stage + deal-size + CAC + sales-capacity
- [ ] Lead-quality vs lead-volume tradeoff explicit in form recommendations
- [ ] Campaign-type calibration explicit (download-LP vs demo-LP vs audit-LP)
- [ ] Traffic-source calibration where relevant (LinkedIn Ads vs Google Ads vs email)
- [ ] B2B-service-type calibration explicit
- [ ] Scarcity/urgency recommendations carefully calibrated (counterproductive in much of B2B)
- [ ] No length labels in output
- [ ] Translated jargon check (no "huren" in Dutch JTBD)
- [ ] Diagnosis cites a specific principle, study, or source
- [ ] Recommendation matches the brand snapshot AND B2B-service-type AND deal-size AND campaign-type
- [ ] ICE justified by I/C/E breakdown

**Language check (HARD):**
- [ ] Entire audit in ONE committed language (no mixed NL/EN, DE/EN, FR/EN, etc.)
- [ ] `.nl` TLD + Dutch content → audit fully in Dutch (not English with Dutch quotes)
- [ ] `.de` TLD + German content → audit fully in German
- [ ] B2B sites in English regardless of TLD → audit in English (match dominant content language)
- [ ] All section headings, all findings, all hypotheses, all CTA suggestions in committed language

**High-risk claim verification (HARD).** Some findings have a history of being wrong when based on HTML interpretation. For these specific claim types, the finding may only be included if you can quote or describe the exact visual evidence from the screenshot in the diagnosis itself.

**High-risk claim categories:**
- CTA text or button state ("the page shows 'X' as primary CTA")
- Form-field count, labels, or validation states ("the form has N fields including X")
- Customer-logos visible (which logos, how many, where positioned)
- Case-study presence and metrics
- Trust badges or certifications visible (SOC 2, ISO 27001, GDPR icons)
- Lead-magnet preview imagery and content-promise
- Navigation presence/absence (single-purpose LPs often have nav stripped — verify)
- Sticky CTA, exit-intent, chat widget presence
- Demo-video or product-screenshot in hero

**Verification format in diagnosis:** "Visible in screenshot: [specific element described]." If you cannot write that sentence based on what's in the screenshot, the finding is removed.

Hypothetical example: do NOT write *"De LP toont een 12-velden BANT-form"* unless you can write *"Visible in screenshot: het form toont 12 velden: naam, e-mail, bedrijfsnaam, role, bedrijfsgrootte, industry, budget-range, timeline, current-vendor, pain-point textarea, AVG-checkbox, GDPR-consent."*

**Message-match verification (HARD).** If user has provided ad/email/source context: cross-reference the LP-headline AND lead-magnet promise AND CTA against the source-promise. Mismatch is the #1 finding-priority for dedicated LPs. If user has NOT provided ad/source: note in audit limitations that message-match couldn't be fully assessed, but assess internal-coherence of the LP itself (headline matches CTA matches form-button matches lead-magnet promise).

If any box is unchecked, rework or remove the finding before delivering. False findings (claiming missing elements that are visually present) destroy audit credibility. One verified finding beats three unverified ones.

**Stock-state verification check (HARD).** Before delivering, scan every finding for these forbidden patterns:

- Any claim that product is "out of stock", "uitverkocht", "sold out", "uitgesloten", "niet leverbaar"
- Any claim about pre-order, "Houd me op de hoogte", "Notify me", "available from [date]", "beschikbaar vanaf [datum]"
- Any reference to release-dates, drop-dates, coming-soon states
- Any "ambiguous state" or "conflicting CTA" finding suggesting the page is in a non-buyable state
- Any inferred pre-order behavior or notify-flow

**For each such finding, ask: "Did I literally see this state in a screenshot?"**

- ❌ NO → DELETE the finding. Do not soften, do not downgrade, do not "research first". Delete entirely. The HTML lied; the screenshot tells the truth.
- ✓ YES → Keep only if you can write "Visible in screenshot: [describe the exact pixel-element]" in the diagnosis.

This check has the highest priority. A single fabricated stock-state finding can destroy audit credibility for the entire deliverable. Better to deliver 8 verified findings than 11 findings with 3 fabrications.

### Step 7: Deliver the report in chat (COMPACT format)

The chat output is the **scan-version** of the audit. Total readable in under 60 seconds. Findings use the compact 3-line format below. The full reasoning lives internally and surfaces in the docx export if requested.

**Use this exact structure:**

```markdown
# B2B Dedicated LP CRO Audit — [Brand]

## Samenvatting
[60-100 words. Structure:
- One-sentence overall verdict (what is the page doing well/badly at the highest level)
- Three Critical issues as bullets — title only, NO explanation (each gets its own full finding below)
- One closing sentence with campaign-type + B2B-service-type + deal-size detection + account-state of screenshots
No duplication with content that appears in findings. No "combined directional impact" lines. No marketing prose.]

## Category sweep
[One-line status per category: Findings (critical/important/nice) / No findings — [brief reason] / Not assessable — [reason].]

## Findings
[All findings sorted by ICE score, descending, within each priority group. Use the COMPACT format below.]

### 🔴 Critical findings
[3-5 findings]

### 🟠 Important findings
[4-6 findings]

### 🟢 Nice-to-have findings
[1-4 findings]

## Test roadmap
[Compact bullet list. Max 4 sprints. One line per test: "Test name — primary metric — ICE score". Note dependencies inline if relevant. Note that B2B dedicated LP test-windows depend on campaign traffic volume — paid campaigns with high traffic enable fast iteration (1-2 weken per test), low-volume campaigns may need 3-6 weken. Downstream MQL-to-SQL signal takes longer to attribute.]

## Audit limitations
[3-6 bullets. Explicit list of what was NOT assessed.]

---

**Export options — choose what you'd like:**

📄 **Client report (.docx)** — Word document with full audit content.

📊 **Sprint planning (.xlsx)** — Spreadsheet with one row per finding.

You can request **one, both, or neither**. Just let me know.
```

**COMPACT finding template (use exactly this in chat):**

```markdown
### [🔴/🟠/🟢] [N]. [Short title, ≤80 chars]
**Probleem:** [One sentence — what's wrong, observable from screenshot]
**Aanbeveling:** [One sentence — concrete action, specific copy/position/behavior]
**Test:** [Primary metric], verwacht [+X% tot +Y%]. ICE [score]. Bron: [source].
```

(In English audits: use **Issue:**, **Recommendation:**, **Test:** as labels.)

**Example of correct compact format:**

```markdown
### 🔴 1. [Concrete issue title — page-specific]
**Probleem:** [What's visibly wrong, specific to the page-type being audited]
**Aanbeveling:** [Concrete action with specific copy/position/behavior]
**Test:** [primary metric], verwacht +X% tot +Y%. ICE [score]. Bron: [framework].

### 🟠 4. [Another concrete issue]
**Probleem:** Visible in screenshot — [specific observation].
**Aanbeveling:** [Specific action] volgens [framework principle].
**Test:** [metric], verwacht [range]. ICE [score]. Bron: [source].
```

**What COMPACT mode does NOT include in chat:**
- Full diagnosis prose (3-6 sentences) — lives internally, written to docx
- Variant A / Variant B descriptions — lives internally, written to docx
- Secondary metrics — lives internally, written to docx
- ICE breakdown (I=X, C=Y, E=Z) — only composite score in chat; full breakdown in docx + xlsx
- Multi-step recommendation lists — collapsed to one-line summary in chat; full list in docx

**Critical:** the internal reasoning must remain complete during analysis. The compact chat output is a presentation layer over a full internal audit. If the user requests docx, the full version is written to the document directly from the internal reasoning — not reconstructed from the compact chat version.

### Step 8: Generate exports on request

**Communication rule:** the user sees only `Exports worden gegenereerd...` during generation. No process narration. No XML-error commentary.

**Use the official skills.** Always read `/mnt/skills/public/docx/SKILL.md` and `/mnt/skills/public/xlsx/SKILL.md` before generating.

**.docx structure:**

The docx contains the **FULL audit content** — NOT the compact chat version. Use the internal full-format reasoning developed in Step 5 (full diagnosis, full recommendation, full test specification with all fields). The chat output was compact for scanning purposes; the docx is the professional deliverable and must include the complete analysis.

Document structure: cover page (with campaign-type + B2B-service-type + deal-size), samenvatting (extended 150-200 words), category sweep, findings by priority (each in FULL format with full diagnosis 3-6 sentences + recommendation + test specification including hypothesis, Variant A/B, primary + secondary metrics, expected impact, ICE breakdown, source), extended test roadmap with dependencies, audit limitations.

**Critical:** every finding in the docx must be 150-350 words. If a finding in chat was compact (3 lines), the docx version expands it back to the full internal reasoning. The compact format is presentation-only; the underlying analysis is always complete.

Common XML pitfall: `children: [cell1, cell2]`, not `children: [[cell1, cell2]]`.

**.xlsx columns (exact order):** ID | Priority | Category | Short title | Hypothesis | Primary metric | Expected impact | ICE score | Impact | Confidence | Ease | Source | Status

Findings sorted by ICE descending. Auto-filter on all columns. Header row bold. Freeze top row.

**Both:** docx first, then xlsx. Brief closing confirmation only.

**Neither:** end audit without generating exports.

## What this skill explicitly does NOT do

- **No SEO audit** (schema, sitemap — out of scope; dedicated LPs are often non-indexed paid-traffic-only)
- **No full accessibility audit** — only where it impacts conversion
- **No paid-traffic audit** (ad-creative, audience targeting, bid strategy) — only the page itself; if user mentions ads, flag as adjacent scope
- **No CRM/marketing-automation integration audit** — only the UX of the lead-form, not the backend flow
- **No nurture-sequence audit** — only the LP, not the post-conversion email-flow
- **No competitor audit** — only the page provided
- **No B2C dedicated LP audit** (use landingpage-b2c-leadgen-dedicatedlp)
- **No B2B servicepage audit** (use landingpage-b2b-leadgen-servicepage — multi-purpose evaluation page)
- **No B2B homepage, contactpage, or aboutus audit** (use respective skills when available)
- **No B2B ecom page audit** (use landingpage-b2b-ecom-* skills)
- **No assumptions about invisible functionality** — check first

## Audit tone

- Direct and concrete
- Source-backed for every claim
- No assumptions about non-visible context (especially ad-source and campaign-type)
- Calls out campaign-type-specific exceptions (download-LP vs demo-LP vs audit-LP)
- Avoids unexplained CRO or B2B jargon
- Respects decision-maker context (no consumer-style recommendations)
- Respects single-purpose page logic (single-CTA dogma APPLIES, opposite of homepage)
- Calibrates scarcity/urgency carefully (often counterproductive in B2B context)
- Acknowledges lead-quality vs lead-volume tradeoffs in form-recommendations

## Reference files

- `references/frameworks-b2b-leadgen-dedicatedlp.md` — detailed B2B dedicated-LP frameworks and per-category guidance
- `references/finding-examples.md` — worked examples for quality calibration
