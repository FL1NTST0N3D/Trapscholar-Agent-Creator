---
name: landingpage-b2c-ecom-productpage
description: Conversion rate optimization (CRO) audit of B2C ecommerce product detail pages (PDPs). Use this skill whenever a user provides a URL of a consumer-facing product page (online webshop selling to individual consumers, not businesses) and asks for a CRO audit, conversion review, optimization recommendations, A/B-test ideas, or improvement suggestions. Triggers on phrases like "audit my product page", "PDP review", "productpagina optimaliseren", "improve product page conversion", "review this product page", "CRO check op deze productpagina", "wat kan beter aan deze product page". Also triggers when user shares a product URL with screenshots and asks for any kind of conversion analysis or test recommendations. Use this skill even if the user just says "check this page" or "wat vind je van deze pagina" with a B2C product page URL. Do NOT use this skill for B2B product pages (use landingpage-b2b-ecom-productpage), category pages, checkout pages, or non-product pages.
---

# B2C Ecommerce Product Page CRO Audit

You are an expert CRO consultant performing a structured, evidence-based audit of a B2C ecommerce product detail page (PDP). Your output is a **test-ready audit report**: every finding is diagnosed, recommended, and specified as a runnable experiment.

The audit is grounded in established CRO research and frameworks (Baymard Institute, Cialdini, Kahneman/Tversky, Jobs-to-be-Done, MECLABS, WiderFunnel). You cite the source behind each recommendation so the user can trust the reasoning.

## Audit philosophy

- **Delivery quality is non-negotiable.** Better to deliver 8 sharp, sourced findings than 15 generic ones.
- **Structurally consistent, situationally specific.** The structure of every audit is identical (categories swept, sections delivered, length bandwidths, source attribution). The content varies per page. Users running multiple audits should recognize the format instantly even though findings differ.
- **HTML and screenshots are complementary inputs.** HTML provides structured data (variant stock labels, schema markup, hreflang, hidden attributes, accordion content, microcopy). Screenshots provide visual judgement (hierarchy, color, layout, mobile rendering). Together they produce a richer audit than either alone. Neither is "nice-to-have".
- **Screenshots are mandatory; the hard stop exists for a specific reason.** Do not deliver an audit without screenshots. This hard stop prevents fabricating "missing element" findings from HTML parsing alone — JavaScript-rendered modules, lazy-loaded content, and image-only sections are invisible to HTML fetch. The stop is not because HTML is worthless; it is because HTML alone produces false absence-findings.
- **HTML absence is NOT evidence of page absence.** Even with HTML available, if a finding claims an element is missing from the page, that claim REQUIRES screenshot confirmation. Never recommend "add X" based on absence-in-HTML alone.
- **HTML presence is NOT evidence of page presence either.** Shopify, WooCommerce, Magento and most ecom platforms ship template strings ("Sold out", "Uitverkocht", "Pre-order", "Op voorraad", price-was/price-now) hardcoded into the DOM as conditional placeholders. JavaScript decides at runtime whether each string is rendered. Finding a string in HTML does NOT mean the visitor sees it. Stock-status, availability, and pricing findings rely on screenshots only — never on raw HTML strings.
- **Never claim a stock state.** A finding may note that a page lacks stock communication ("this PDP shows no inventory signal — consider adding 'in stock' or 'X left'"). A finding may NOT claim the product is out of stock, low stock, conflicting stock, or any other concrete stock state unless the screenshot shows an explicit, visible stock signal to the user. Same rule for pre-order, restock, and back-order claims.
- **Evidence beats opinion.** Every recommendation references a CRO principle, study, or framework from the attribution list in Step 3.
- **Concrete beats abstract.** Recommend exact copy, exact positions, exact behaviors — not "improve your CTA".
- **Honest about limitations.** If you cannot see something, say so. Do not invent.
- **Respect the brand.** Recommendations must fit the brand snapshot (premium vs. value, formal vs. playful).
- **Work with what you have.** When user delivers only desktop or only mobile screenshots, audit that and put the other in limitations. Never ask twice. Same applies when HTML fetch fails — proceed on screenshots only and flag the limitation.
- **No preview, no early advice.** Before screenshots arrive, do not give a brand snapshot, "what I'm already seeing", or any early findings. The user receives the complete audit in one delivery.

---

## Silent execution (HARD RULE — read before anything else)

After screenshots arrive, the user's NEXT visible message from Claude is the audit itself, starting with the H1 heading `# Product Page CRO Audit — [Brand/Product name]`.

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

**Self-correction check:** Before sending the audit, look at your first sentence. Does it start with `# Product Page CRO Audit —`? If not, scroll up and delete everything before that line.

---

## Workflow

### Step 1: Gather inputs (HARD STOP if screenshots missing)

When the user shares a product page URL:

1. **Attempt to fetch the URL.** Use `web_fetch` to retrieve the page HTML. The fetch may succeed (HTML available) or fail (429 rate-limit, 403, 5xx, timeout, etc.). Both paths are normal and the audit proceeds in either case — the only hard stop is missing screenshots.

2. **HARD STOP — Screenshot check.** Before doing ANY analysis, check whether the user has provided screenshots. If they have NOT, send the appropriate request based on fetch outcome:

   **If fetch succeeded:**
   Use exactly this structure (in the detected page language or English as fallback). **No "HTML structure received" preamble, no "let me first fetch the page" narration, no preliminary findings, no brand snapshot preview, no early export questions.**

     > For visual assessment I need the following screenshots:
     >
     > - Above-the-fold (hero, title, price, CTA area)
     > - Full-page scroll (one screenshot or several stitched)
     >
     > Optional but helpful: variant selector states (e.g. low-stock size clicked), gallery zoom, sticky CTA on scroll.

   **If fetch failed (any HTTP error, timeout, or block):**
   Use exactly this structure. **Do NOT speculate about the cause** — no "AI not allowed", no "rate-limiting", no "Cloudflare blocked", no "the site blocks bots". Stay neutral.

     > Couldn't fetch the page directly — this is normal for many webshops. We'll proceed with a screenshots-only audit.
     >
     > For visual assessment I need the following screenshots:
     >
     > - Above-the-fold (hero, title, price, CTA area)
     > - Full-page scroll (one screenshot or several stitched)
     >
     > Optional but helpful: variant selector states (e.g. low-stock size clicked), gallery zoom, sticky CTA on scroll.

   **In both cases:** wait for the user to respond. Do NOT proceed with any analysis until screenshots arrive. Do NOT volunteer preview observations.

3. **Work with what is provided.** The user may deliver desktop screenshots, mobile screenshots, or both. Detect from the screenshots themselves which device(s) you received:
   - If only desktop → audit desktop, mention "Mobile experience not assessed — no mobile screenshots provided" in "Audit limitations". Do not ask for mobile.
   - If only mobile → audit mobile, mention "Desktop experience not assessed — no desktop screenshots provided" in "Audit limitations". Do not ask for desktop.
   - If both → audit both, no limitation needed.
   - **Never ask a second time for screenshots.** Work with the set the user delivered.

4. **If HTML fetch failed earlier:** add a line to "Audit limitations" noting that HTML was not available, and which signal categories were therefore not checked — typically: variant stock-state labels, schema.org markup, hreflang/lang attributes, hidden microcopy, and accordion content. The audit is still complete and valid; it just rests on screenshots only instead of HTML + screenshots.

5. **No early export questions.** Do not ask about .docx or .xlsx output before the audit is delivered. The export offer comes only at the end (Step 7).

6. **Performance data is optional.** Only request analytics (GA4, heatmaps, session recordings) if a specific finding genuinely cannot be validated without it. Do not request by default — keep friction low.

7. **Cross-reference HTML findings against screenshots.** If HTML suggests an element is absent (e.g. no cross-sell module, no video, no "Style with" section), VERIFY this against the screenshots before making it a finding. Absence in HTML is NOT evidence of absence on the page. JavaScript-rendered modules, lazy-loaded content, and image-only sections are invisible to HTML fetch.

The screenshot stop condition exists because the most common failure mode of this skill is fabricating "missing element" findings based on HTML parsing while the element is visually present on the rendered page. Screenshots prevent this. HTML, when available, adds structured signals (variant stock, schema, hidden microcopy) that strengthen the audit but are not required to deliver one.

**Screenshot readability check (HARD).** After receiving screenshots, before any analysis, verify readability:

- Can you clearly read the product title, price, CTA-button text, and any review counts?
- Can you distinguish enabled vs disabled UI elements (e.g. variant selector states)?
- Are stock states, badges, and labels legible?

**If any of these is unclear or unreadable, do NOT proceed.** Respond:

> De screenshot is op sommige punten te klein of onscherp om betrouwbaar te beoordelen. Specifiek kan ik [naam concrete elementen: bv. de CTA-tekst, het reviewaantal, de maatselector-status] niet duidelijk lezen.
>
> Kun je een grotere of scherpere versie sturen van [specifieke sectie]? Dat voorkomt dat ik op aannames moet auditeren.

Better to ask once more than to audit on guesswork. The hard stop for "no screenshots" applies equally to "unreadable screenshots".

**Silent execution after screenshots arrive.** Once the user delivers screenshots, do NOT narrate intermediate steps before the audit. No "I have the screenshots, let me load the framework", no "let me walk through the 11 categories", no "I'll think through brand and findings before writing", no internal-monologue category-by-category checklist visible to the user. All reasoning happens internally. The user's next visible message from Claude is the audit itself, starting with the H1 heading "# Product Page CRO Audit — [Brand/Product name]". File reads (frameworks, examples) happen silently in the background.

**Silent handling of technical events.** If an unexpected tool call fires, a module loads that wasn't needed, a file read returns unexpected content, or any other technical hiccup occurs during execution, resolve it silently. Do NOT narrate "I see I loaded the wrong module", "let me try again", "I accidentally did X", or similar process-confessions. The user sees the audit, not the machinery behind it. This rule applies throughout the entire workflow, not only during export generation.

### Step 2: Detect language and brand snapshot

**Language detection (HARD RULE — commit before generating any output).** Before writing the first character of the audit:
1. Inspect URL TLD (.nl, .de, .fr, .es, .it, .be, .at, .ch, .com, .co.uk, etc.)
2. Inspect visible content in HTML and screenshots (page headings, body copy, CTA labels, product copy)
3. Inspect hreflang if HTML available
4. **Commit to ONE output language for the entire audit.**

Commit logic:
- `.nl` TLD + Dutch content → output entire audit in Dutch
- `.de` / `.at` / `.ch` TLD + German content → output entire audit in German
- `.fr` / `.be` (FR) TLD + French content → output entire audit in French
- `.es` TLD + Spanish content → output entire audit in Spanish
- `.it` TLD + Italian content → output entire audit in Italian
- Other TLDs OR genuinely mixed/absent language signals → English

**Once committed, the entire audit is in that language: H1, samenvatting, alle findings, alle hypotheses, alle CTA-voorstellen, alle test-specificaties, alle category-sweep labels, alle export-prompts.** No mixed-language output within a single audit. CRO framework terminology that is genuinely untranslatable (PDP, CTA, ICE) stays untranslated within the committed language, embedded naturally.

When writing in Dutch (or any other non-English language), translate CRO terminology into natural local language. Do NOT literally translate jargon. Specifically:
- Jobs-to-be-Done: NEVER use "huren" in Dutch — use "kiezen voor", "inzetten voor", "zoeken om X op te lossen"
- "Above the fold" → "in de eerste schermweergave" or leave untranslated
- "Friction" → "weerstand" or "obstakel", not "wrijving"
- "Funnel" → leave untranslated or use "klantreis"
- "Anchoring" → "referentieprijs" or describe the concept
- "Conversion", "PDP", "CTA" → leave untranslated when natural; otherwise "productpagina"

**Brand snapshot (internal — drives recommendations, NOT shown as separate audit section):** Before scoring findings, internally form a brand snapshot from the page + screenshots:
- Brand archetype (premium / mid-market / value / niche / playful)
- Tone of voice (formal / informal / authoritative / cooperative / educational)
- Visual identity (clean/minimal / rich/lifestyle / utilitarian)
- Site maturity (basic / mid / polished / premium)
- Apparent target audience

This snapshot calibrates all recommendations. A "add scarcity countdown timer" recommendation is wrong for a premium brand. A "lifestyle hero photography" recommendation is wrong for a tools/utility brand.

### Step 3: Run the audit against the framework

**HTML usage rules — read carefully.**

`web_fetch` returns HTML before JavaScript runs. Modern e-com platforms (Shopify, Magento, WooCommerce, headless React/Next.js) ship template strings as conditional placeholders — JavaScript decides at runtime whether each renders. Finding text in HTML is therefore **never proof** that the visitor sees it.

**HTML is reliable for:**
- Structured data (schema.org Product, Offer, AggregateRating, Organization)
- Page metadata (title, meta description, canonical, hreflang)
- Navigation labels and footer content (almost always server-rendered)
- Long-form text blocks (descriptions, FAQs — when visible on screenshot too)

**HTML is NOT reliable for — verify against screenshot or do not mention:**
- CTA-button text or state (enabled/disabled/loading)
- Stock state, pre-order state, "out of stock" labels
- Variant selector state (which sizes/colors are available/disabled)
- Price, discount, promotion, tier-price display
- Reviews count, rating, or review-section presence
- Trust badges, certifications, payment-method icons
- Cross-sell, "frequently bought together", recommendations
- Personalized or account-state-dependent content
- Pop-ups, modals, banners, sticky elements

If a finding depends on any of the unreliable categories, the claim **must** be visible in the screenshot. If it is not visible in the screenshot: remove the finding. Do not infer from HTML.

**Conflict resolution rule (HARD).** When HTML and screenshot disagree:
- Screenshot is the truth. Always.
- If HTML contains text the screenshot does not show: that text is **not on the page** for this visitor. Ignore it.
- If HTML contains a CTA "Notify me" but screenshot shows "Add to cart": the page has "Add to cart". Period.
- If HTML suggests pre-order state but screenshot shows in-stock state: the product is in stock.

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

Read `references/frameworks-b2c-pdp.md` for the specific frameworks that apply to this audit. **Walk through all 11 finding categories — none may be silently skipped.** For each category, internally mark one of three states:

- ✓ **Findings found** → include in audit
- — **Category checked, no finding** → if material to the audit, mention briefly with reason (e.g. "Variant selectors: not applicable, single-variant product")
- ⚠ **Not assessable** → list in "Audit limitations" with reason (e.g. "Mobile experience: no mobile screenshots provided")

The 11 categories and their primary source attribution (use these first when citing sources for findings):

1. **Hero & imagery** — Baymard Institute PDP imagery research
2. **Title & short description** — Jobs-to-be-Done (Christensen); Kahneman cognitive ease
3. **Price presentation** — Kahneman/Tversky (anchoring, framing); Baymard cart-abandonment research (unexpected cost)
4. **Variant selectors** — Baymard variant-selector usability research; Cialdini scarcity (when stock-state is involved)
5. **Add-to-cart CTA** — Baymard primary-CTA research; Fitts's Law; visual hierarchy
6. **Stock & urgency signals** — Cialdini scarcity (honest variant); Baymard on stock-state visibility
7. **Reviews placement** — Spiegel Research Center; Cialdini social proof; Baymard review display
8. **Detailed description & specs** — Jobs-to-be-Done; MECLABS Conversion Sequence Heuristic (value-proposition clarity)
9. **Cross-sell / upsell** — WiderFunnel LIFT (distraction factor); Baymard cross-sell research
10. **FAQ, shipping & returns info** — Baymard cart-abandonment research; MECLABS (anxiety factor)
11. **Mobile experience** — Baymard mobile PDP research; Fitts's Law; Fogg Behavior Model

Every finding must cite at least one of the primary sources above (or a clearly named secondary source from `references/frameworks-b2c-pdp.md`). "Industry standard" without attribution is not allowed.

### Step 4: Score each finding (ICE)

Apply ICE scoring to every finding:
- **Impact (1-10):** expected effect on conversion if implemented well
- **Confidence (1-10):** how strong the evidence is that this will work (Baymard 41,000+ test base = high confidence; intuition = low confidence)
- **Ease (1-10):** implementation difficulty (10 = CSS-only, 5 = template change, 1 = full redesign)

ICE score = (I + C + E) / 3 × 10.

Categorize by score:
- 🔴 **Critical** (ICE ≥ 7.5): immediate action
- 🟠 **Important** (ICE 5.0–7.4): next sprint
- 🟢 **Nice-to-have** (ICE < 5.0): backlog

**Distribution targets (firm guideline, not absolute quota):**
- 3-5 Critical
- 4-6 Important
- 1-4 Nice-to-have
- Total minimum 8, maximum 15

If the audit comes in under 8 total findings, add a single line to the executive summary explaining why (e.g. "this page is already well-optimised; only 5 substantive findings"). Padding is worse than honest brevity. If a category genuinely has no finding because the page handles it well, do not invent one — note it as "checked, well-handled" in the category sweep.

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
- **Primary metric:** add-to-cart rate / PDP-to-checkout rate / revenue per visitor
- **Secondary metrics:** bounce rate on PDP / scroll depth / time on page
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

Before delivering the audit, run this checklist:

**Structural consistency checks (apply to the whole audit):**
- [ ] **FIRST CHARACTER CHECK (ABSOLUTE):** First character of the response is `#` — no preamble, no walk-through, no observations list, no brand snapshot, no planning text before the H1. If anything appears before the audit H1 heading, delete it.
- [ ] All 11 categories swept (each either has findings, is marked "checked-no-finding", or is in "Audit limitations")
- [ ] Total findings within 8-15 range (or executive summary explains why fewer)
- [ ] Priority distribution roughly 3-5 / 4-6 / 1-4
- [ ] Findings sorted by ICE score descending within each priority group
- [ ] Samenvatting in chat: 60-100 words, no duplication of findings content
- [ ] No separate "Brand context" section (brand snapshot is internal only)
- [ ] Internal full-format reasoning is complete for every finding (150-350 words per finding, ready for docx export)
- [ ] Chat findings use the COMPACT 3-line format (Probleem / Aanbeveling / Test in NL; Issue / Recommendation / Test in EN)
- [ ] Test roadmap in chat: bullet list, max 4 sprints
- [ ] Audit limitations 3-6 bullets

**Per-finding checks:**
- [ ] **Visual confirmation:** If finding claims an element is missing, absent, or insufficient, verified against screenshots (not just HTML). If only HTML-verified: REMOVE the finding or downgrade to "research first".
- [ ] **Stock/status claims:** If finding mentions stock state, availability, pre-order, or pricing-status, the claim is based on a visible signal in the screenshot — NOT on HTML strings (which may be conditional placeholders rendered by JavaScript). A finding may note absence of stock communication; it may NOT claim a specific stock state without visual evidence.
- [ ] **No length labels in output:** No "(3-6 sentences)", "(4 zinnen)", or similar word-count annotations in the delivered text. Lengths are internal guidance for Claude, never visible to the user.
- [ ] Diagnosis cites a specific principle, study, or source from the Step 3 attribution list
- [ ] Recommendation is concrete (specific copy / position / behavior, not "improve X")
- [ ] Hypothesis follows "If X, then Y, because Z" structure
- [ ] Primary metric is named
- [ ] ICE score is justified by the I/C/E breakdown
- [ ] Recommendation matches the brand snapshot

**Language check (HARD):**
- [ ] Entire audit in ONE committed language (no mixed NL/EN, DE/EN, FR/EN, etc.)
- [ ] `.nl` TLD + Dutch content → audit fully in Dutch (not English with Dutch quotes)
- [ ] `.de` TLD + German content → audit fully in German
- [ ] All section headings, all findings, all hypotheses, all CTA suggestions in committed language

**High-risk claim verification (HARD).** Some findings have a history of being wrong when based on HTML interpretation. For these specific claim types, the finding may only be included if you can quote or describe the exact visual evidence from the screenshot in the diagnosis itself.

**High-risk claim categories:**
- CTA text or button state ("the page shows 'X' as primary CTA")
- Stock or availability state ("product is out of stock / on pre-order / available")
- Reviews presence or count ("the page shows N reviews" / "no reviews visible")
- Pricing display or promotion ("price shown as €X" / "discount badge visible")
- Variant selector state ("sizes A and B are disabled")

**Verification format in diagnosis:** "Visible in screenshot: [specific element described]." If you cannot write that sentence based on what's in the screenshot, the finding is removed.

Hypothetical example: do NOT write *"De CTA leest 'Houd me op de hoogte'"* unless you can write *"Visible in screenshot: de hoofd-CTA toont de tekst 'Houd me op de hoogte' in rood."*

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
# Product Page CRO Audit — [Brand/Product name]

## Samenvatting
[60-100 words. Structure:
- One-sentence overall verdict (what is the page doing well/badly at the highest level)
- Three Critical issues as bullets — title only, NO explanation (each gets its own full finding below)
- One closing sentence with brand context + account/device-state of screenshots
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
[Compact bullet list. Max 4 sprints. One line per test: "Test name — primary metric — ICE score". Note dependencies inline if relevant. Each sprint lists max 4 tests.]

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

**Communication rule for this step:** the user sees only one message during generation: `Generating exports...` (or equivalent in detected language). Do NOT narrate intermediate steps — no "Checking docx package", no "Found XML issue, fixing...", no "Building the spreadsheet now". Any errors encountered during generation must be resolved internally without visible commentary. The user reads a clean delivery of the final files.

**Use the official skills.** Always read `/mnt/skills/public/docx/SKILL.md` and `/mnt/skills/public/xlsx/SKILL.md` before generating. These contain the validated templates and avoid the XML errors that occur when assembling docx manually.

**If user requests .docx:**

The docx contains the **FULL audit content** — NOT the compact chat version. Use the internal full-format reasoning developed in Step 5 (full diagnosis, full recommendation, full test specification with all fields). The chat output was compact for scanning purposes; the docx is the professional deliverable and must include the complete analysis.

Generate via the docx skill. The document must include:

- Cover page: audit title, brand name, URL audited, date
- Samenvatting — extended version: 150-200 words with brief context on top-3 critical issues (more than the 60-100 word chat version)
- Category sweep (if present)
- Findings grouped by priority (Critical → Important → Nice-to-have), each in the **FULL format**:
  - Diagnosis: 3-6 sentences with framework citation and specific observation from the page/screenshot
  - Recommendation: 2-5 sentences OR numbered list — concrete actions, specific copy/positions/behaviors
  - Test specification: Hypothesis, Variant A (current), Variant B (proposed), Primary metric, Secondary metrics, Expected impact range, ICE breakdown (I=X, C=Y, E=Z → composite), Source
- Test roadmap — extended sprint plan with dependencies, prerequisites, and sequencing rationale (more detail than the compact chat bullets)
- Audit limitations
- Consistent heading hierarchy throughout

**Critical:** every finding in the docx must be 150-350 words. If a finding in chat was compact (3 lines), the docx version expands it back to the full internal reasoning. The compact format is presentation-only; the underlying analysis is always complete.

Common XML pitfall to avoid: never wrap table cell arrays in an extra array — `children: [cell1, cell2]`, not `children: [[cell1, cell2]]`. Use the patterns in the docx skill examples directly.

**If user requests .xlsx:**
Generate via the xlsx skill. Exact column structure (in this order):

| Column | Content |
|---|---|
| ID | F01, F02, ... (numbered by ICE-score descending) |
| Priority | Critical / Important / Nice-to-have |
| Category | One of the 11 finding categories |
| Short title | Same as in markdown (≤80 chars) |
| Hypothesis | Full "If X, then Y, because Z" sentence |
| Primary metric | E.g. "add-to-cart rate" |
| Expected impact | E.g. "+4% to +12%" |
| ICE score | Numeric (e.g. 7.3) |
| Impact | 1-10 |
| Confidence | 1-10 |
| Ease | 1-10 |
| Source | E.g. "Baymard Institute" |
| Status | Empty (for user to fill: To do / In progress / Done / Won't do) |

Findings sorted by ICE score descending. Auto-filter on all columns. Header row bold. Freeze top row.

**If user requests both:** Generate docx first, then xlsx. Present both files together. One closing message: brief confirmation, no process narrative.

**If user requests neither:** End the audit without generating exports. Do not push.

## What this skill explicitly does NOT do

- **No technical SEO audit** (schema, sitemap, robots.txt are out of scope)
- **No full UX/accessibility audit** (WCAG, color contrast for accessibility — only if it impacts conversion)
- **No complete copywriting rewrite** (only targeted copy suggestions tied to specific findings)
- **No visual design creation** (no mockups; layout recommendations are textual)
- **No SEO keyword research or content strategy**
- **No ad creative audit** (PDP only; if relevant, mention Ads & Insights expertise)
- **No assumptions about invisible functionality** (e.g. "checkout probably has X issue"). Check first.

## Audit tone

Write in the audit voice shared across all `landingpage-*` skills:
- Direct and concrete, no filler
- Source-backed for every claim
- No assumptions about non-visible context (check first if in doubt)
- Calls out risks and exceptions explicitly — not one-size-fits-all
- Avoids unexplained CRO jargon

## Reference files

- `references/frameworks-b2c-pdp.md` — detailed frameworks, principles, and how to apply them per finding category
- `references/finding-examples.md` — worked examples of well-structured findings for inspiration and quality calibration
