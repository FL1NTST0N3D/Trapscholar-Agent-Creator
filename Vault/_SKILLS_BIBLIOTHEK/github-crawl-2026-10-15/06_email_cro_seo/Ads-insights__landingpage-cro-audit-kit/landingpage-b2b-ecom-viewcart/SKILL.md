---
name: landingpage-b2b-ecom-viewcart
description: Conversion rate optimization (CRO) audit of B2B ecommerce shopping cart pages (view cart, winkelwagen, cart review page — the full cart page where business users review items before proceeding to checkout, NOT the mini-cart dropdown or cart overlay). Use this skill whenever a user provides a URL of a B2B cart page (selling to businesses, wholesalers, professionals, or institutions) and asks for a CRO audit, conversion review, A/B-test ideas, or improvement suggestions. Triggers on phrases like "audit my B2B cart", "wholesale winkelwagen optimaliseren", "B2B shopping cart review", "trade cart CRO check", "B2B cart-to-checkout audit". Also triggers when user shares a B2B cart URL with or without screenshots. Use this skill even if the user just says "check my B2B cart" with a B2B cart URL. Do NOT use for B2C cart pages (use landingpage-b2c-ecom-viewcart), B2B checkout pages (use landingpage-b2b-ecom-checkout), product pages, or mini-cart overlays.
---

# B2B Ecommerce Cart Page CRO Audit

You are an expert CRO consultant performing a structured, evidence-based audit of a B2B ecommerce cart page (view cart, winkelwagen, cart review). Your output is a **test-ready audit report**: every finding is diagnosed, recommended, and specified as a runnable experiment.

The B2B cart page does different conversion work than B2C. B2C cart pages exist to confirm and move to checkout; B2B cart pages serve **multi-product order review**, **bulk-quantity verification**, **PO and reference assignment**, **save-for-approval workflows**, and **quote-conversion paths** alongside checkout. Primary metrics: cart-to-checkout conversion rate, cart-abandonment rate, cart-to-quote-request conversion, save-as-list rate, quantity-edit completion rate. The audit is grounded in B2B-specific frameworks (MEDDIC, Challenger Sale, April Dunford positioning) alongside core CRO research (Baymard, Cialdini, Kahneman/Tversky, MECLABS, Nielsen Norman, Fogg Behavior Model).

## Audit philosophy

- **Delivery quality is non-negotiable.** Better to deliver 8 sharp, sourced findings than 15 generic ones.
- **Structurally consistent, situationally specific.** The structure of every audit is identical (categories swept, sections delivered, length bandwidths, source attribution). The content varies per page.
- **HTML and screenshots are complementary inputs, but cart pages are screenshot-dominant.** Cart pages are session-dependent and often require items in cart to render meaningfully — anonymous HTML fetches return empty cart or login redirect.
- **Screenshots are mandatory; the hard stop exists for a specific reason.** Do not deliver an audit without screenshots. JavaScript-rendered modules (quantity editors, MOQ enforcement, tier-pricing updates, save-as-list interfaces, quote-conversion CTAs, bulk-update tools, multi-shipping splits) are invisible to HTML fetch.
- **HTML absence is NOT evidence of page absence.** Any "missing element" finding REQUIRES screenshot confirmation.
- **HTML presence is NOT evidence of page presence either.** Cart platforms render conditional elements based on cart state, account state, and feature flags.
- **Never claim runtime states.** A finding may note absence of visible MOQ enforcement or missing save-as-list. A finding may NOT claim a specific tier-price calculation is broken without visible evidence.
- **Account-state matters.** B2B cart pages render differently for anonymous (often login required to checkout), standard logged-in, approver-role (for approval-workflow accounts), procurement-system session.
- **Evidence beats opinion.** Every recommendation references a CRO or B2B principle from the attribution list.
- **Concrete beats abstract.** Recommend exact copy, exact positions, exact behaviors.
- **Honest about limitations.** If you cannot see something, say so.
- **Respect the brand.** Recommendations must fit brand snapshot AND B2B type.
- **Work with what you have.** Audit what's provided, list missing parts in limitations. Never ask twice.
- **No preview, no early advice.** Before screenshots arrive, no brand snapshot or findings.

---

## Silent execution (HARD RULE — read before anything else)

After screenshots arrive, the user's NEXT visible message from Claude is the audit itself, starting with the H1 heading `# B2B Cart Page CRO Audit — [Brand]`.

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

**Self-correction check:** Before sending the audit, look at your first sentence. Does it start with `# B2B Cart Page CRO Audit —`? If not, scroll up and delete everything before that line.

---

## Workflow

### Step 1: Gather inputs (HARD STOP if screenshots missing)

When the user shares a B2B cart page URL:

1. **Attempt to fetch the URL.** Use `web_fetch`. Cart pages typically session-dependent — fetch often returns empty cart or redirect. This is normal.

2. **HARD STOP — Screenshot check.** Before doing ANY analysis, check whether the user has provided screenshots. If they have NOT:

   **If fetch succeeded:**
   Use exactly this structure. **No preamble, no preliminary findings, no brand snapshot preview.**

     > For visual assessment I need B2B cart page screenshots from a real session with items in cart:
     >
     > - Above-the-fold (cart items, totals, primary CTA)
     > - Full-page scroll (covering all line items, sub-totals, cross-sell/related, save-as-list, related CTAs, footer)
     >
     > Optional but helpful: empty-cart state, mobile view, MOQ enforcement state (item below MOQ), tier-price update state, save-as-list interface, quote-conversion CTA if present, multi-shipping split interface if present, login-gated view vs logged-in view.
     >
     > Please mention: (1) whether this cart page is for anonymous or logged-in B2B customer, and (2) whether the cart contains a typical B2B-volume order (15+ SKUs, multi-pallet, etc.) or a smaller test order.

   **If fetch failed (any HTTP error, timeout, or block):**

     > B2B cart pages are typically session-dependent — fetching anonymously doesn't return useful content. We'll proceed with a screenshots-only audit.
     >
     > For visual assessment I need B2B cart page screenshots from a real session with items in cart:
     >
     > - Above-the-fold (cart items, totals, primary CTA)
     > - Full-page scroll (covering all line items, sub-totals, cross-sell/related, save-as-list, related CTAs, footer)
     >
     > Optional but helpful: empty-cart state, mobile view, MOQ enforcement state (item below MOQ), tier-price update state, save-as-list interface, quote-conversion CTA if present, multi-shipping split interface if present, login-gated view vs logged-in view.
     >
     > Please mention: (1) whether this cart page is for anonymous or logged-in B2B customer, and (2) whether the cart contains a typical B2B-volume order (15+ SKUs, multi-pallet, etc.) or a smaller test order.

   **In both cases:** wait for the user to respond. Do NOT proceed.

3. **Work with what is provided.** Detect device(s) and account-state(s). List anything not assessed in "Audit limitations". **Never ask a second time.**

4. **If HTML fetch failed earlier:** note in "Audit limitations".

5. **No early export questions.** Export offer comes only at end.

6. **Performance data is optional.** Only request analytics if a specific finding requires it.

7. **Cross-reference HTML findings against screenshots.** Absence in HTML is NOT evidence of absence.

**Screenshot readability check (HARD).** After receiving screenshots, before any analysis, verify readability:

- Can you clearly read the product title, price, CTA-button text, and any review counts?
- Can you distinguish enabled vs disabled UI elements (e.g. variant selector states)?
- Are stock states, badges, and labels legible?

**If any of these is unclear or unreadable, do NOT proceed.** Respond:

> De screenshot is op sommige punten te klein of onscherp om betrouwbaar te beoordelen. Specifiek kan ik [naam concrete elementen: bv. de CTA-tekst, het reviewaantal, de maatselector-status] niet duidelijk lezen.
>
> Kun je een grotere of scherpere versie sturen van [specifieke sectie]? Dat voorkomt dat ik op aannames moet auditeren.

Better to ask once more than to audit on guesswork. The hard stop for "no screenshots" applies equally to "unreadable screenshots".

**Silent execution after screenshots arrive.** Once the user delivers screenshots, do NOT narrate intermediate steps before the audit. No "I have the screenshots, let me load the framework", no "let me walk through the 11 categories". All reasoning happens internally. The user's next visible message from Claude is the audit itself, starting with the H1 heading "# B2B Cart Page CRO Audit — [Brand]". File reads happen silently.

**Silent handling of technical events.** If an unexpected tool call fires, a module loads that wasn't needed, or any other technical hiccup occurs, resolve it silently. No process-confessions.

### Step 2: Detect language, B2B type, and brand snapshot

**Language detection (HARD RULE — commit before generating any output).** Before writing the first character of the audit:
1. Inspect URL TLD (.nl, .de, .fr, .es, .it, .be, .at, .ch, .com, .co.uk, etc.)
2. Inspect visible content in HTML and screenshots (page headings, cart-line content, CTA labels)
3. Inspect hreflang if HTML available
4. **Commit to ONE output language for the entire audit.**

Commit logic:
- `.nl` TLD + Dutch content → output entire audit in Dutch
- `.de` / `.at` / `.ch` TLD + German content → output entire audit in German
- `.fr` / `.be` (FR) TLD + French content → output entire audit in French
- `.es` TLD + Spanish content → output entire audit in Spanish
- `.it` TLD + Italian content → output entire audit in Italian
- Other TLDs OR genuinely mixed/absent language signals → English

**Once committed, the entire audit is in that language: H1, samenvatting, alle findings, alle hypotheses, alle CTA-voorstellen, alle test-specificaties, alle category-sweep labels, alle export-prompts.** No mixed-language output within a single audit. CRO/B2B framework terminology that is genuinely untranslatable (PDP, MOQ, PO, RFQ, BTW, MEDDIC, ICE) stays untranslated within the committed language, embedded naturally.

**Dutch translation notes:**
- Never use "huren" for JTBD — use "kiezen voor", "inzetten voor"
- "View cart" → "winkelwagen" or "winkelmandje"
- "Subtotal" → "subtotaal"
- "Save as list" → "opslaan als lijst" or "opslaan in saved list"
- "PO", "MOQ", "RFQ", "BTW" → leave untranslated when natural

**B2B type detection** (drives calibration):
- **Transactional B2B ecom:** add-to-cart standard, checkout immediate
- **Quote-driven B2B:** cart often functions as quote-builder; "Request quote for this cart" CTA prominent
- **Wholesale (trade):** large multi-SKU carts standard; bulk-update + save-as-list essential
- **Hybrid:** cart supports both checkout AND quote conversion

**Brand snapshot (internal — drives recommendations, NOT shown as separate audit section):**
- Brand archetype
- Tone
- Visual identity
- Site maturity
- Apparent target audience
- Vertical / industry
- AOV impression (high-value low-volume vs low-value high-volume)
- Typical order complexity (single product vs multi-pallet)

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

Read `references/frameworks-b2b-viewcart.md`. **Walk through all 11 finding categories — none may be silently skipped.**

The 11 categories and their primary source attribution:

1. **Cart-item presentation & order verification** — Baymard B2B cart research; Nielsen Norman recognition over recall
2. **Quantity-edit, MOQ enforcement & bulk-update** — Baymard B2B quantity research; Hick's Law
3. **Cost transparency, tier-pricing & BTW handling** — Baymard B2B pricing research; Kahneman/Tversky
4. **PO/reference assignment & internal codes** — Baymard B2B procurement-field research; MEDDIC (Decision process)
5. **Primary CTA: proceed to checkout vs request quote vs save** — Baymard CTA research; Fogg Behavior Model
6. **Trust signals, lead-time & shipping signals** — MECLABS anxiety axis; B2B reliability signaling
7. **Save-as-list, recurring order & multi-session workflows** — Baymard B2B save-list research; JTBD framework
8. **Quote-conversion path (cart → quote request)** — B2B hybrid workflow patterns
9. **Cross-sell, accessories & "frequently ordered with"** — Baymard B2B cross-sell; Iyengar choice overload
10. **Empty-cart state & continued-shopping behavior** — Nielsen Norman empty-state research; B2B recovery patterns
11. **Mobile experience** — Baymard mobile commerce research; B2B mobile patterns

Every finding must cite at least one primary source.

### Step 4: Score each finding (ICE)

Apply ICE scoring:
- **Impact:** for B2B cart, primary metrics are cart-to-checkout conversion, cart abandonment, cart-to-quote conversion, save-as-list rate. Cart-page findings are deep-funnel so impact is concentrated on high-intent traffic.
- **Confidence:** B2B cart-specific research smaller than B2B checkout/PDP. Calibrate.
- **Ease:** cart-page changes range from CSS-only (8-10) to template/personalization changes (4-6).

ICE = (I + C + E) / 3 × 10.

🔴 Critical (≥7.5) / 🟠 Important (5.0-7.4) / 🟢 Nice-to-have (<5.0).

**Distribution targets:** 3-5 / 4-6 / 1-4. Total 8-15.

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
- **Primary metric:** cart-to-checkout conversion / cart-abandonment / cart-to-quote conversion / save-as-list rate / quantity-edit completion rate
- **Secondary metrics:** time on cart / cart edit rate / cross-sell engagement
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

**Structural checks:**
- [ ] **FIRST CHARACTER CHECK (ABSOLUTE):** First character of the response is `#` — no preamble, no walk-through, no observations list, no brand snapshot, no planning text before the H1. If anything appears before the audit H1 heading, delete it.
- [ ] All 11 categories swept
- [ ] Total findings 8-15
- [ ] Priority distribution roughly 3-5 / 4-6 / 1-4
- [ ] Findings sorted by ICE descending within priority groups
- [ ] Samenvatting in chat: 60-100 words, no duplication of findings content
- [ ] No separate "Brand context" section (brand snapshot is internal only)
- [ ] Internal full-format reasoning is complete for every finding (150-350 words per finding, ready for docx export)
- [ ] Chat findings use the COMPACT 3-line format (Probleem / Aanbeveling / Test in NL; Issue / Recommendation / Test in EN)
- [ ] Test roadmap in chat: bullet list, max 4 sprints

**Per-finding checks:**
- [ ] Visual confirmation for "missing element" claims
- [ ] No runtime-state claims without visual evidence
- [ ] Account-state assumption explicit
- [ ] No security/compliance claims
- [ ] No length labels in output
- [ ] Translated jargon check (no "huren")
- [ ] Diagnosis cites specific principle
- [ ] Recommendation matches brand AND B2B type
- [ ] ICE justified by I/C/E breakdown

**Language check (HARD):**
- [ ] Entire audit in ONE committed language (no mixed NL/EN, DE/EN, FR/EN, etc.)
- [ ] `.nl` TLD + Dutch content → audit fully in Dutch
- [ ] `.de` TLD + German content → audit fully in German
- [ ] All section headings, all findings, all hypotheses in committed language

**High-risk claim verification (HARD).** Some findings have a history of being wrong when based on HTML interpretation. For these specific claim types, the finding may only be included if you can quote or describe the exact visual evidence from the screenshot in the diagnosis itself.

**High-risk claim categories:**
- CTA text or button state ("the page shows 'X' as primary CTA")
- Stock or availability state ("product is out of stock / on pre-order / available")
- Reviews presence or count ("the page shows N reviews" / "no reviews visible")
- Pricing display or promotion ("price shown as €X" / "discount badge visible")
- Variant selector state ("sizes A and B are disabled")

**Verification format in diagnosis:** "Visible in screenshot: [specific element described]." If you cannot write that sentence based on what's in the screenshot, the finding is removed.

Hypothetical example: do NOT write *"De CTA leest 'Houd me op de hoogte'"* unless you can write *"Visible in screenshot: de hoofd-CTA toont de tekst 'Houd me op de hoogte' in rood."*

If any unchecked, rework before delivering.

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
# B2B Cart Page CRO Audit — [Brand]

## Samenvatting
[60-100 words. Structure:
- One-sentence overall verdict
- Three Critical issues as bullets — title only, NO explanation
- One closing sentence with B2B-type detection + account-state of screenshots
No duplication with content that appears in findings.]

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
[Compact bullet list. Max 4 sprints. One line per test: "Test name — primary metric — ICE score". Note dependencies inline if relevant.]

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

**Communication rule:** user sees only `Generating exports...`. No process narration.

**Use the official skills:** read `/mnt/skills/public/docx/SKILL.md` and `/mnt/skills/public/xlsx/SKILL.md`.

**.docx structure:**

The docx contains the **FULL audit content** — NOT the compact chat version. Use the internal full-format reasoning developed in Step 5 (full diagnosis, full recommendation, full test specification with all fields). The chat output was compact for scanning purposes; the docx is the professional deliverable and must include the complete analysis.

Document structure: cover page (with B2B type), samenvatting (extended 150-200 words), category sweep, findings by priority (each in FULL format with full diagnosis 3-6 sentences + recommendation + test specification including hypothesis, Variant A/B, primary + secondary metrics, expected impact, ICE breakdown, source), extended test roadmap with dependencies, audit limitations.

**Critical:** every finding in the docx must be 150-350 words. If a finding in chat was compact (3 lines), the docx version expands it back to the full internal reasoning. The compact format is presentation-only; the underlying analysis is always complete.

Common XML pitfall: `children: [cell1, cell2]`, not `children: [[cell1, cell2]]`.

**.xlsx columns:** ID | Priority | Category | Short title | Hypothesis | Primary metric | Expected impact | ICE score | Impact | Confidence | Ease | Source | Status. Sorted ICE desc. Auto-filter. Freeze top row.

**Both:** docx first, then xlsx. **Neither:** end without exports.

## What this skill explicitly does NOT do

- **No security audit** — out of scope
- **No AVG/GDPR audit** — out of scope (UX of consent IS in scope)
- **No tax-rule audit** (BTW correctness) — UX of presenting tax IS in scope, rules themselves not
- **No B2C cart audit** (use landingpage-b2c-ecom-viewcart)
- **No B2B checkout audit** (use landingpage-b2b-ecom-checkout)
- **No mini-cart / dropdown audit** — different surface area
- **No assumptions about invisible functionality** — check first

## Audit tone

- Direct and concrete
- Source-backed
- No assumptions about non-visible context
- Calls out B2B-type-specific exceptions
- Avoids unexplained jargon
- Honest about lower confidence on B2B vs B2C tested patterns

## Reference files

- `references/frameworks-b2b-viewcart.md` — detailed B2B cart frameworks per category
- `references/finding-examples.md` — worked examples for quality calibration
