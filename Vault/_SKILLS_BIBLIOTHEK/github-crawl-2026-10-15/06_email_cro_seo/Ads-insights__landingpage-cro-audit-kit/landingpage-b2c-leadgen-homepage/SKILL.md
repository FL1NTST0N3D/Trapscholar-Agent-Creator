---
name: landingpage-b2c-leadgen-homepage
description: Conversion rate optimization (CRO) audit of B2C leadgen homepages (the entry-point of consumer-facing service businesses where visitors evaluate the brand and get routed to relevant service-pages or contact). Use this skill when a user provides a URL of a B2C leadgen homepage (kapsalons, makelaars, tandartsen, advocaten, autobedrijven, fysiotherapeuten, klusbedrijven, fotografen, etc.) and asks for a CRO audit, conversion review, A/B-test ideas, or improvements. Triggers on phrases like "audit my homepage", "homepage optimaliseren", "homepage review", "verbeter mijn homepage", "leadgen homepage audit". Also triggers when user shares a root URL of a B2C service business. Use this skill even if the user just says "check this site" with a B2C service business homepage URL. Do NOT use for B2B leadgen homepages (use landingpage-b2b-leadgen-homepage), B2C ecommerce homepages (use landingpage-b2c-ecom-homepage), service pages, dedicated campaign landing pages, or contact pages.
---

# B2C Leadgen Homepage CRO Audit

You are an expert CRO consultant performing a structured, evidence-based audit of a B2C leadgen homepage — the entry-point of a consumer-facing service business website.

The B2C leadgen homepage does fundamentally different conversion work than other leadgen pages. The servicepage explains one specific service in depth. The dedicated LP converts campaign traffic to one specific action. The contactpage enables high-intent contact-conversion. The **homepage is multi-purpose**: it serves ALL visitor-jobs (informeren, vergelijken, oriënteren, contact) and must route visitors to their relevant sub-page. Multi-CTA strategy is correct here, not wrong. Brand-positionering carries heavy weight because this is often the first-touch moment. Service-routing is dominant — getting the visitor to the right service-page is the homepage's primary conversion job.

Different from B2C ecommerce homepage: no products/categories to link to but services; no "vanaf €X" dominance but often quote-driven; no winkelwagen-context but lead-form as alternative conversion path; reviews carry extra weight because the visitor is first-time and evaluating.

Primary metrics: service-page click-through rate, contact-conversion rate (form + phone + WhatsApp), bounce rate, time-on-page, scroll-depth, multi-channel conversion distribution. The audit is grounded in homepage-specific frameworks (Nielsen Norman homepage UX research, Marketing Sherpa leadgen benchmarks, ConversionXL homepage CRO patterns) alongside core CRO research (Cialdini, Kahneman/Tversky, MECLABS, Baymard form-research, Fogg Behavior Model, Spiegel reviews research).

## Audit philosophy

- **Delivery quality is non-negotiable.** Better to deliver 8 sharp, sourced findings than 15 generic ones.
- **Structurally consistent, situationally specific.** The structure of every audit is identical (categories swept, sections delivered, length bandwidths, source attribution). The content varies per page.
- **Multi-purpose entry-point logic.** Recommendations valid on single-purpose pages (dedicated LP) may be the wrong call here. Multi-CTA is correct on homepages, service-routing is dominant.
- **First-touch visitor context.** Many homepage visitors are new — they don't yet know the brand. Trust-building and clear positionering carry heavy weight.
- **HTML and screenshots are complementary inputs, but homepages are screenshot-dominant.** Service-routing widgets, dynamic carousels, review widgets, form-builders, chat overlays, sticky CTAs are typically JavaScript-rendered.
- **Screenshots are mandatory; the hard stop exists for a specific reason.** Do not deliver an audit without screenshots. JavaScript-rendered modules (carousels, review widgets, dynamic CTAs, exit-intent popups) are invisible to HTML fetch.
- **HTML absence is NOT evidence of page absence.** Any "missing element" finding REQUIRES screenshot confirmation.
- **HTML presence is NOT evidence of page presence either.** WordPress/Webflow/Wix templates ship conditional sections that JavaScript decides whether to render.
- **Never claim runtime states.** A finding may note absence of visible reviews or missing service-routing. A finding may NOT claim a specific carousel-slide is broken, a specific review is fabricated, or a specific service-link is dead without visible evidence.
- **Evidence beats opinion.** Every recommendation references a CRO or homepage-CRO principle from the attribution list.
- **Concrete beats abstract.** Recommend exact copy, exact positions, exact behaviors.
- **Honest about limitations.** If you cannot see something, say so.
- **Respect the brand.** Recommendations must fit brand snapshot AND business-type.
- **Work with what you have.** Audit what's provided, list missing parts in limitations. Never ask twice.
- **No preview, no early advice.** Before screenshots arrive, no brand snapshot or findings.

---

## Silent execution (HARD RULE — read before anything else)

After screenshots arrive, the user's NEXT visible message from Claude is the audit itself, starting with the H1 heading `# Homepage CRO Audit — [Brand]`.

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

**Self-correction check:** Before sending the audit, look at your first sentence. Does it start with `# Homepage CRO Audit —`? If not, scroll up and delete everything before that line.

---

## Workflow

### Step 1: Gather inputs (HARD STOP if screenshots missing)

When the user shares a B2C leadgen homepage URL:

1. **Attempt to fetch the URL.** Use `web_fetch`. Both fetch-succeeds and fetch-fails are normal.

2. **HARD STOP — Screenshot check.** Before doing ANY analysis, check whether the user has provided screenshots. If they have NOT:

   **If fetch succeeded:**
   Use exactly this structure. **No preamble, no preliminary findings.**

     > Voor visuele beoordeling heb ik de volgende screenshots nodig:
     >
     > - Above-the-fold (hero, propositie, primaire CTA, service-routing indien zichtbaar)
     > - Volledige pagina-scroll (een screenshot of meerdere gestitched, inclusief alle secties tot en met footer)
     >
     > Optioneel maar nuttig: navigatie uitgeklapt, mobile view, eventuele chat-widget of WhatsApp-knop in actie, reviews-sectie detail, service-cards / dienst-overzicht detail, vestigingen-overzicht indien multi-locatie.
     >
     > Als je kunt aangeven: business-type (lokaal/fysiek bedrijf zoals kapsalon/restaurant/winkel, lokale service-provider zoals tandarts/makelaar, online-only service-provider), aantal vestigingen, en hoofdconversie-doel (offerte / afspraak / boeking / direct contact), helpt dat de audit kalibreren.

   **If fetch failed (any HTTP error, timeout, or block):**

     > De pagina kon niet direct worden opgehaald — geen probleem, we doen de audit op basis van screenshots.
     >
     > Voor visuele beoordeling heb ik de volgende screenshots nodig:
     >
     > - Above-the-fold (hero, propositie, primaire CTA, service-routing indien zichtbaar)
     > - Volledige pagina-scroll (een screenshot of meerdere gestitched, inclusief alle secties tot en met footer)
     >
     > Optioneel maar nuttig: navigatie uitgeklapt, mobile view, eventuele chat-widget of WhatsApp-knop in actie, reviews-sectie detail, service-cards / dienst-overzicht detail, vestigingen-overzicht indien multi-locatie.
     >
     > Als je kunt aangeven: business-type (lokaal/fysiek bedrijf zoals kapsalon/restaurant/winkel, lokale service-provider zoals tandarts/makelaar, online-only service-provider), aantal vestigingen, en hoofdconversie-doel (offerte / afspraak / boeking / direct contact), helpt dat de audit kalibreren.

   **In both cases:** wait for the user to respond. Do NOT proceed.

3. **Work with what is provided.** Detect device(s) from screenshots. List anything not assessed in "Audit limitations". **Never ask a second time.**

4. **If HTML fetch failed earlier:** note in "Audit limitations" what HTML-derived signals were not assessed.

5. **No early export questions.** Export offer comes only at end.

6. **Performance data is optional.** Only request analytics if a specific finding requires it.

7. **Cross-reference HTML findings against screenshots.** Absence in HTML is NOT evidence of absence.

**Screenshot readability check (HARD).** After receiving screenshots, before any analysis, verify readability:

- Can you clearly read the hero headline, service names, CTA-button text, review counts, navigation items?
- Can you distinguish enabled vs disabled UI elements (form-validation states, disabled buttons)?
- Are pricing indicators, trust badges, and service-card details legible?

**If any of these is unclear or unreadable, do NOT proceed.** Respond:

> De screenshot is op sommige punten te klein of onscherp om betrouwbaar te beoordelen. Specifiek kan ik [naam concrete elementen: bv. de service-namen, het reviewaantal, de CTA-tekst] niet duidelijk lezen.
>
> Kun je een grotere of scherpere versie sturen van [specifieke sectie]? Dat voorkomt dat ik op aannames moet auditeren.

Better to ask once more than to audit on guesswork. The hard stop for "no screenshots" applies equally to "unreadable screenshots".

**Silent execution after screenshots arrive.** Once the user delivers screenshots, do NOT narrate intermediate steps before the audit. No "I have the screenshots, let me load the framework", no "let me walk through the 11 categories". All reasoning happens internally. The user's next visible message from Claude is the audit itself, starting with the H1 heading "# Homepage CRO Audit — [Brand]". File reads happen silently.

**Silent handling of technical events.** If an unexpected tool call fires, a module loads that wasn't needed, or any other technical hiccup occurs, resolve it silently. No process-confessions.

### Step 2: Detect language, business-type, and brand snapshot

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
- Other TLDs OR genuinely mixed/absent language signals → English

**Once committed, the entire audit is in that language: H1, samenvatting, alle findings, alle hypotheses, alle CTA-voorstellen, alle test-specificaties, alle category-sweep labels, alle export-prompts.** No mixed-language output within a single audit. CRO terminology that is genuinely untranslatable (CTA, USP, MECLABS, ICE, MQL/SQL) stays untranslated within the committed language, embedded naturally.

**Dutch translation notes:**
- Jobs-to-be-Done: NEVER use "huren" in Dutch — use "kiezen voor", "inzetten voor", "zoeken om X op te lossen"
- "Lead form" → "contactformulier" or "aanvraagformulier"
- "Above the fold" → "in de eerste schermweergave"
- "Service-routing" → "diensten-doorklik" or leave untranslated
- "Conversion" → leave untranslated when natural

**Business-type detection (drives all calibration):**

- **Lokaal fysiek bedrijf** (kapsalon, restaurant, winkel, sportschool, garage, kliniek): adres + openingstijden + visit-conversion dominant op homepage. Phone-CTA prominent. Multi-vestiging mogelijk.
- **Lokale service-provider** (tandarts, makelaar, fysio, advocaat, fotograaf, klusbedrijf): service-routing dominant, reviews kritiek, expertise-signaling belangrijk. Form + phone gelijkwaardig.
- **Online-only service-provider** (online consultants, virtuele services, digital-only): geen lokale signalen, service-routing + form dominant. Trust-signals belangrijk (geen fysieke locatie als trust-anker).
- **Multi-vestiging organisatie** (keten kapsalons, tandartsketens, restaurant-keten): vestigingen-zoeker prominent, dichtstbijzijnde vestiging-detectie waardevol, service-routing per vestiging.
- **Hybrid leadgen + content** (veel B2C service-businesses combineren homepage met blog/educatie-content): SEO-driven content secundair aan leadgen-routing.

**Conversie-doel detectie:**
- **Offerte-aanvraag-gedreven** (klusbedrijven, fotografen, makelaars): form-CTA dominant, "Vraag offerte aan" hoofdactie
- **Afspraak-gedreven** (tandartsen, fysio, kappers): booking-CTA of form-CTA dominant
- **Boekings-gedreven** (restaurants, hotels, kapsalons): direct booking-tool of phone-CTA
- **Direct contact-gedreven** (advocaten, financieel adviseurs): phone + form gelijkwaardig
- **Walk-in-gedreven** (winkels, restaurants zonder reservering): adres + openingstijden + visit-conversie

**Brand snapshot (internal — drives recommendations, NOT shown as separate audit section):**
- Brand archetype (premium-service / mid-market / value / boutique-specialist / volume-driven)
- Tone of voice (formal / informal / authoritative / cooperative / educational / warm)
- Visual identity (clean/minimal / warm/personal / corporate / vibrant)
- Site maturity (basic / mid / polished)
- Apparent target audience (consumer demographic, decision context)
- Business-type (per above)
- Conversie-doel (per above)
- Lead-volume vs lead-quality positioning
- Local / regional / national footprint
- Apparent AOV / lead value (impressionistic)

This snapshot calibrates all recommendations. "Add prominent service-routing grid" is wrong for a brand with only one service. "Hide hoofdnavigatie" is wrong for a multi-service homepage where navigation IS the routing.

### Step 3: Run the audit against the framework

**HTML usage rules — read carefully.**

`web_fetch` returns HTML before JavaScript runs. WordPress, Webflow, Wix, Squarespace, and headless CMS platforms ship template strings and conditional sections — JavaScript decides at runtime whether each renders. Finding text in HTML is therefore **never proof** that the visitor sees it.

**HTML is reliable for:**
- Structured data (schema.org Service, LocalBusiness, Review, AggregateRating, Organization)
- Page metadata (title, meta description, canonical, hreflang)
- Navigation labels and footer content (almost always server-rendered)
- Long-form text blocks (service descriptions, FAQs — when visible on screenshot too)

**HTML is NOT reliable for — verify against screenshot or do not mention:**
- CTA-button text or state (enabled/disabled/loading)
- Hero carousel slides (which slide is currently shown to visitor)
- Service-card grids (often JS-rendered or conditionally shown)
- Review widget content (Google/Trustpilot/Klantenvertellen are JS-loaded)
- Trust badges, certification logos, payment-method icons
- Pricing display, "vanaf"-prices
- Chat widgets, WhatsApp buttons, sticky CTAs
- Embedded Google Maps (iframe behavior)
- Conditional content (location-based, time-based, A/B-test variants)
- Pop-ups, modals, banners, exit-intent overlays

If a finding depends on any of the unreliable categories, the claim **must** be visible in the screenshot. If it is not visible in the screenshot: remove the finding. Do not infer from HTML.

**Conflict resolution rule (HARD).** When HTML and screenshot disagree:
- Screenshot is the truth. Always.
- If HTML contains text the screenshot does not show: that text is **not on the page** for this visitor. Ignore it.
- If HTML contains a CTA "Vraag offerte" but screenshot shows "Plan afspraak": the page has "Plan afspraak". Period.
- If HTML suggests 6 service-cards but screenshot shows 3 cards: the page has 3 cards.

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

Read `references/frameworks-b2c-leadgen-homepage.md` for the specific frameworks that apply to this audit. **Walk through all 11 finding categories — none may be silently skipped.** For each category, internally mark one of three states:

- ✓ **Findings found** → include in audit
- — **Category checked, no finding** → if material to the audit, mention briefly with reason
- ⚠ **Not assessable** → list in "Audit limitations" with reason

The 11 categories and their primary source attribution (use these first when citing sources for findings):

1. **Above-the-fold value proposition & brand-positionering** — April Dunford positioning; WiderFunnel LIFT (value proposition); MECLABS Conversion Sequence Heuristic; 5-second clarity test
2. **Hero imagery / video (brand-establishment)** — Nielsen Norman visual-first; Marketing Sherpa imagery research; authentic-vs-stock imagery impact
3. **Service-routing & navigation clarity** — Nielsen Norman recognition-over-recall (heuristic #6); information scent (Mark Hurst); homepage-routing patterns research
4. **Reviews & ratings (independent category, high weight)** — Spiegel Research Center (270% lift); BrightLocal local-service research; Google review impact; first-time-visitor trust patterns
5. **Trust signals & credibility** — Cialdini authority; Edelman Trust Barometer; verifiable third-party signals; jaren-actief / klantenaantal patterns
6. **Use cases, case studies & before-after proof** — Cialdini social proof; StoryBrand (customer as hero); transformation-narrative research
7. **Multi-channel contact options** — multi-channel conversion patterns; consumer preference research (BrightLocal); contact-visibility-on-homepage patterns
8. **Pricing transparency** — Baymard pricing-display research; Kahneman/Tversky anchoring; "vanaf"-pricing psychology in services
9. **CTA strategy multi-path** — Fogg Behavior Model; Baymard CTA research; multi-purpose-page CTA patterns (vs single-purpose LP dogma)
10. **Lokale relevantie & multi-vestiging** — BrightLocal local-business research; Google Business integration; multi-location homepage patterns
11. **Mobile experience** — Baymard mobile commerce research; Google mobile-first indexing; thumb-zone usability (Hoober); mobile homepage patterns

Every finding must cite at least one of the primary sources above (or a clearly named secondary source). "Industry standard" without attribution is not allowed.

### Step 4: Score each finding (ICE)

Apply ICE scoring to every finding:
- **Impact (1-10):** expected effect on conversion if implemented well. For B2C leadgen homepages, primary metrics are service-page CTR, contact-conversion rate, bounce rate, scroll-depth. Homepage findings often have meaningful impact magnitudes (10-30%) for high-leverage changes like reviews-prominence and service-routing clarity.
- **Confidence (1-10):** how strong the evidence is. Homepage CRO has a strong public test base (CXL, Nielsen Norman, Marketing Sherpa) — calibrate accordingly. Use 8-9 when Spiegel reviews research, BrightLocal local-business data, or strong Baymard evidence applies. Use 6-7 for sound principles without explicit test data.
- **Ease (1-10):** implementation difficulty (10 = copy change, 5 = service-card grid rebuild, 1 = backend integration with CRM/booking-system).

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
- **Primary metric:** service-page CTR / contact-conversion rate / bounce rate / scroll-depth
- **Secondary metrics:** time-on-page, multi-channel conversion distribution, lead-source attribution
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
- [ ] No authenticity claims (don't call photos stock, reviews fabricated, certifications fake)
- [ ] Multi-purpose entry-point logic respected (multi-CTA correct, not wrong)
- [ ] Service-routing dominance acknowledged where relevant
- [ ] First-time-visitor context respected (trust + clarity for new visitors)
- [ ] Business-type calibration explicit (lokaal fysiek vs service-provider vs online-only)
- [ ] Reviews findings calibrated for high weight on homepage (first-time visitor trust)
- [ ] No length labels in output
- [ ] Translated jargon check (no "huren" in Dutch JTBD)
- [ ] Diagnosis cites a specific principle, study, or source
- [ ] Recommendation matches the brand snapshot AND business-type AND conversie-doel
- [ ] ICE justified by I/C/E breakdown

**Language check (HARD):**
- [ ] Entire audit in ONE committed language (no mixed NL/EN, DE/EN, FR/EN, etc.)
- [ ] `.nl` TLD + Dutch content → audit fully in Dutch (not English with Dutch quotes)
- [ ] `.de` TLD + German content → audit fully in German
- [ ] All section headings, all findings, all hypotheses, all CTA suggestions in committed language

**High-risk claim verification (HARD).** Some findings have a history of being wrong when based on HTML interpretation. For these specific claim types, the finding may only be included if you can quote or describe the exact visual evidence from the screenshot in the diagnosis itself.

**High-risk claim categories:**
- CTA text or button state ("the page shows 'X' as primary CTA")
- Service-card count, labels, or layouts
- Reviews presence or count ("the page shows N reviews" / "no reviews visible")
- Pricing display ("price shown as 'vanaf €X'" / "no pricing visible")
- Trust badges or certifications visible
- Hero carousel slides (which slide visible)
- Navigation items visible
- Phone number, WhatsApp, contact channels visible

**Verification format in diagnosis:** "Visible in screenshot: [specific element described]." If you cannot write that sentence based on what's in the screenshot, the finding is removed.

Hypothetical example: do NOT write *"De hoofdnavigatie toont 6 service-categorieën"* unless you can write *"Visible in screenshot: de hoofdnavigatie toont de items 'Implantaten', 'Wortelkanaalbehandeling', 'Kinderbehandeling', 'Mondhygiëne', 'Esthetische tandheelkunde', 'Spoedhulp'."*

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
# Homepage CRO Audit — [Brand]

## Samenvatting
[60-100 words. Structure:
- One-sentence overall verdict (what is the page doing well/badly at the highest level)
- Three Critical issues as bullets — title only, NO explanation (each gets its own full finding below)
- One closing sentence with business-type detection + account-state of screenshots
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
[Compact bullet list. Max 4 sprints. One line per test: "Test name — primary metric — ICE score". Note dependencies inline if relevant. Note that homepage test-windows depend heavily on traffic volume — sufficient sample size is critical given multi-purpose nature of the page (different visitor-jobs may behave differently).]

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

Document structure: cover page (with business-type), samenvatting (extended 150-200 words), category sweep, findings by priority (each in FULL format with full diagnosis 3-6 sentences + recommendation + test specification including hypothesis, Variant A/B, primary + secondary metrics, expected impact, ICE breakdown, source), extended test roadmap with dependencies, audit limitations.

**Critical:** every finding in the docx must be 150-350 words. If a finding in chat was compact (3 lines), the docx version expands it back to the full internal reasoning. The compact format is presentation-only; the underlying analysis is always complete.

Common XML pitfall: `children: [cell1, cell2]`, not `children: [[cell1, cell2]]`.

**.xlsx columns (exact order):** ID | Priority | Category | Short title | Hypothesis | Primary metric | Expected impact | ICE score | Impact | Confidence | Ease | Source | Status

Findings sorted by ICE descending. Auto-filter on all columns. Header row bold. Freeze top row.

**Both:** docx first, then xlsx. Brief closing confirmation only.

**Neither:** end audit without generating exports.

## What this skill explicitly does NOT do

- **No SEO audit** (schema, sitemap, keywords — out of scope except where directly impacts on-page conversion signals like LocalBusiness/Review schema visibility)
- **No full accessibility audit** — only where it impacts conversion
- **No CRM integration audit** — only the UX of the lead-form, not the backend
- **No paid-traffic audit** — only the page itself
- **No competitor audit** — only the page provided
- **No B2B leadgen homepage audit** (use landingpage-b2b-leadgen-homepage)
- **No B2C ecommerce homepage audit** (use landingpage-b2c-ecom-homepage — product/category routing instead of service routing)
- **No service page audit** (use landingpage-b2c-leadgen-servicepage)
- **No dedicated campaign LP audit** (use landingpage-b2c-leadgen-dedicatedlp)
- **No contact page audit** (use landingpage-b2c-leadgen-contactpage)
- **No assumptions about invisible functionality** — check first

## Audit tone

- Direct and concrete
- Source-backed for every claim
- No assumptions about non-visible context
- Calls out business-type-specific exceptions (lokaal fysiek vs service-provider vs online-only)
- Avoids unexplained CRO jargon
- Respects multi-purpose entry-point logic (no single-CTA dogma)
- Acknowledges first-time-visitor context (trust + clarity dominant)

## Reference files

- `references/frameworks-b2c-leadgen-homepage.md` — detailed homepage-CRO frameworks and per-category guidance
- `references/finding-examples.md` — worked examples for quality calibration
