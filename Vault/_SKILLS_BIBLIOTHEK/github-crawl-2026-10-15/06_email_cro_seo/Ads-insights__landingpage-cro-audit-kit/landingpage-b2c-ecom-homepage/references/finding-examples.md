# Worked finding examples — homepage quality calibration

These examples show what a high-quality homepage finding looks like across different categories, brand snapshots, and ICE scores. Use them as a reference standard. Findings should match this depth and specificity — not be vaguer, not be more generic.

---

## Example 1: 🔴 Critical — Above-the-fold value proposition (mid-market specialty retailer)

### 🔴 Above-the-fold clarity — Brand-only headline forces visitors to derive category from imagery

**Diagnosis**
The above-the-fold area shows only the brand logo "TradingCardsCo" and a hero image of a Pokémon booster box. There is no headline explaining what the site sells, who it's for, or what makes it different. A first-time visitor arriving from a Google search or ad has to derive the category from a single product image. Per WiderFunnel LIFT's value proposition factor and Nielsen Norman's 5-second test, this fails the most basic clarity check — a visitor should be able to answer "what does this site sell, who is it for, and why this site" within five seconds, without scrolling. Currently they can guess "trading cards" from the visual, but the visitor segment (collectors? players? gift-buyers?) and the brand positioning (specialist? generalist? authentic source?) are invisible.

**Recommendation**
Add a clear text headline above or next to the hero image. Recommended structure: "[Category] — [Differentiator] — [Audience signal]". Example: "Trading Card Games — Officieel & op voorraad — Voor verzamelaars en spelers". Pair it with a sub-headline naming the brands carried (Pokémon, Magic, Yu-Gi-Oh) and one trust anchor ("Vertrouwd door 12.000+ Nederlandse fans"). Keep the existing hero image; add the text overlay or place it adjacent. Test layouts both with text-over-image and text-beside-image.

**Test specification**
- **Hypothesis:** If we add a category headline + sub-headline + trust anchor above the fold, then bounce rate will decrease and click-to-category rate will increase because first-time visitors immediately understand what the site sells and why this site (WiderFunnel LIFT value proposition).
- **Variant A:** current brand-logo-only hero
- **Variant B:** hero with category headline, sub-headline naming brands carried, and one trust anchor
- **Primary metric:** bounce rate on homepage (sessions with single pageview)
- **Secondary metrics:** click-to-category rate, time on homepage, search-bar usage
- **Expected impact:** -8% to -15% on bounce rate
- **ICE:** I=9, C=8, E=9 → 8.7
- **Source:** WiderFunnel LIFT (value proposition); Nielsen Norman Group 5-second test research

---

## Example 2: 🔴 Critical — Primary navigation (mid-market apparel retailer)

### 🔴 Primary navigation — Search bar hidden behind icon, category labels mirror internal taxonomy

**Diagnosis**
The top navigation hides search behind a magnifying-glass icon (one click to reveal) and uses category labels "S/S 25", "F/W 24", and "PRE-FALL" — internal seasonal taxonomy that means little to most visitors. Baymard's navigation research shows search-bar usage drops 2-3x when hidden behind an icon on retailers with 100+ SKUs. The visible-input search bar is the format that drives meaningful engagement. Separately, category labels that use industry shorthand fail Nielsen Norman's information-scent principle — visitors don't follow scent when labels don't match their mental model. A visitor looking for "linen shirts" has no idea whether to click "S/S 25" or "F/W 24".

**Recommendation**
Two changes. First, expose the search input directly in the top bar with placeholder "Zoek op merk, type, …" and autocomplete enabled. Position it center-right of the navigation, between category labels and the cart icon. Second, replace internal-taxonomy labels with customer-language equivalents: "Nieuw" or "Lente/Zomer 2025" instead of "S/S 25". Keep brand-savvy labels like "Designers" and "Bestsellers". The internal seasonal codes can remain accessible via a sub-menu for power users.

**Test specification**
- **Hypothesis:** If we expose the search input directly and replace internal-taxonomy navigation labels with customer-language equivalents, then click-to-PDP rate will increase and search-usage will rise because visitors can follow clearer information scent (Baymard navigation research; Nielsen Norman information scent).
- **Variant A:** search behind icon, internal-taxonomy labels
- **Variant B:** visible search input + customer-language labels
- **Primary metric:** click-to-PDP rate (sessions reaching a product page)
- **Secondary metrics:** search-bar usage rate, navigation menu interaction rate, bounce rate
- **Expected impact:** +6% to +12% on click-to-PDP rate
- **ICE:** I=8, C=8, E=8 → 8.0
- **Source:** Baymard Institute navigation research; Nielsen Norman Group information scent research

---

## Example 3: 🔴 Critical — Social proof (Dutch consumer webshop, mid-market)

### 🔴 Social proof — "9,9" badge present but uncontextualised; no review widget on homepage

**Diagnosis**
The site shows a small "9,9" badge in the top-right corner, but with no platform label (Kiyoh? WebwinkelKeur? Google?), no review count, and no link to the review source. For Dutch visitors, the platform matters: Kiyoh, WebwinkelKeur, and Trustpilot all carry different weight. Per Cialdini's social proof principle and Spiegel Research Center data, sites displaying contextualised reviews convert ~270% better than sites with absent or unverifiable proof. The current badge gives the visitor no reason to trust it — it could be self-applied. Additionally, no aggregate review widget or testimonial appears anywhere on the homepage, leaving the social-proof signal weak for a webshop at this price tier.

**Recommendation**
Two layered changes. First, expand the existing "9,9" badge: add the platform name and review count ("9,9/10 op Kiyoh — gebaseerd op 1.247 reviews"), make the badge clickable to the review source. Second, add an embedded Kiyoh/Trustpilot widget below the hero with 3-4 visible review quotes that rotate. Place it before the featured-products section so visitors encounter social proof early in the scroll. For Dutch market: pair this with a Thuiswinkel Waarborg or WebwinkelKeurmerk badge if applicable.

**Test specification**
- **Hypothesis:** If we contextualise the "9,9" badge and add an embedded review widget with rotating quotes, then click-to-PDP rate will increase because verifiable social proof reduces first-visit anxiety (Cialdini social proof; Spiegel Research Center).
- **Variant A:** uncontextualised "9,9" badge, no review widget
- **Variant B:** expanded badge with platform + count + click-through, plus review widget below hero
- **Primary metric:** click-to-PDP rate
- **Secondary metrics:** time on homepage, scroll depth past hero, return-visitor rate
- **Expected impact:** +5% to +12% on click-to-PDP rate
- **ICE:** I=8, C=8, E=9 → 8.3
- **Source:** Cialdini (social proof principle); Spiegel Research Center on reviews and conversion; Baymard Institute trust-element placement

---

## Example 4: 🟠 Important — Hero imagery (premium brand)

### 🟠 Hero imagery & messaging — Single-product hero misses brand-discovery and broader category framing

**Diagnosis**
The homepage hero shows a single product (a specific overshirt) with the product name as headline. For a premium multi-brand retailer with thousands of SKUs, anchoring the hero to one product narrows the entry experience for visitors who arrived without intent for that specific item. Per Eisenberg's buyer modalities, the hero currently addresses only the "competitive" modality (here is a specific product, decide). It fails to address "spontaneous" (lifestyle inspiration), "humanistic" (brand story, editorial framing), or "methodical" (category/brand overview). Nielsen Norman F-pattern research confirms visitors scan the hero horizontally before committing to scroll; a hero serving multiple modalities outperforms a single-product anchor for sites with broad assortments.

**Recommendation**
Replace the single-product hero with a layered structure that addresses three modalities at once: editorial lifestyle imagery (humanistic + spontaneous), a category/edit headline ("Spring Essentials" / "New Designers — Summer 2025") as opposed to a product name (competitive), and two CTAs — primary "Shop the edit", secondary "Bekijk alle nieuwe arrivals". Keep premium photography style — single editorial image, generous whitespace, no badge clutter. The single-product hero pattern can return as a sub-hero one section down for visitors interested in that specific item.

**Test specification**
- **Hypothesis:** If we replace the single-product hero with an editorial category-edit hero, then bounce rate will decrease and click-to-category rate will increase because the hero addresses more buyer modalities and matches premium-retailer conventions (Eisenberg buyer modalities; Nielsen Norman F-pattern).
- **Variant A:** single-product hero with product name as headline
- **Variant B:** editorial category-edit hero with lifestyle imagery and dual CTAs
- **Primary metric:** click-to-category rate (any non-PDP next click)
- **Secondary metrics:** bounce rate, scroll depth, click-to-PDP rate (may slightly decrease, acceptable trade-off)
- **Expected impact:** +4% to +10% on click-to-category rate
- **ICE:** I=7, C=7, E=7 → 7.0
- **Source:** Eisenberg buyer modalities; Nielsen Norman Group F-pattern eye-tracking research

---

## Example 5: 🟠 Important — USP-banner (mid-market Dutch retailer)

### 🟠 USP-banner — Highest-anxiety USP buried below shipping-threshold message

**Diagnosis**
The trust strip below the header shows three USPs in this order: "Gratis verzending vanaf €50", "Veilig betalen met iDEAL", "Snelle levering". The most anxiety-reducing element for first-time Dutch ecom visitors — return policy — is absent. Baymard's cart-abandonment research consistently places return-policy uncertainty in the top-5 abandonment reasons. MECLABS Conversion Sequence Heuristic identifies the "a" (anxiety) factor as a directly controllable conversion lever — and the strongest anxiety on a first homepage visit is typically "what if I don't like it". The current USP strip addresses payment safety (low anxiety for established iDEAL users) and shipping cost (moderate anxiety) but skips the bigger lever.

**Recommendation**
Reorder and expand the USP strip to four items with the highest-anxiety USP first: "14 dagen gratis retour", "Voor 22:00 besteld = morgen geleverd", "Gratis verzending vanaf €50", "Veilig betalen met iDEAL, PayPal, Apple Pay". Add a Thuiswinkel Waarborg badge at the end of the row for additional trust anchoring. Keep the strip visually consistent with the brand — no aggressive icons, no color-coded alerts — just text with subtle dividers.

**Test specification**
- **Hypothesis:** If we add a return-policy USP and place it first in the trust strip, then bounce rate will decrease and click-to-PDP rate will increase because the highest-anxiety question is answered before the visitor decides whether to engage further (MECLABS anxiety reduction; Baymard cart-abandonment).
- **Variant A:** current three-USP strip without return policy
- **Variant B:** four-USP strip with "14 dagen gratis retour" first
- **Primary metric:** bounce rate
- **Secondary metrics:** click-to-PDP rate, scroll depth, time on homepage
- **Expected impact:** -3% to -7% on bounce rate
- **ICE:** I=6, C=8, E=10 → 8.0
- **Source:** MECLABS Conversion Sequence Heuristic (anxiety factor); Baymard Institute cart-abandonment research

---

## Example 6: 🟢 Nice-to-have — Email capture (premium brand)

### 🟢 Email capture — Newsletter signup buried in footer; no incentive

**Diagnosis**
The newsletter signup appears only in the footer with the label "Subscribe to our newsletter" and no incentive offered. Per Fogg's Behavior Model, this fails the trigger condition: the visitor reaches the footer only after engagement, when the trigger arrives too late and without motivation. Cialdini's reciprocity principle suggests email capture works dramatically better when paired with a tangible incentive (early access, lookbook, welcome offer). Industry conversion benchmarks: footer signups without incentive convert <1% of homepage visitors; well-timed popups with relevant incentives convert 3-8%. However, for a premium brand a full-screen popup is brand-damaging. A subtle bottom-bar opt-in after scroll, with a brand-appropriate incentive, is the right pattern.

**Recommendation**
Add a subtle bottom-bar email opt-in that appears after 40% scroll depth, with copy: "Inside access — first to know about new collections and exclusive editorial. [email] [Sign up]". Skip the discount framing (off-brand for premium); use editorial-access framing. Cap frequency at one impression per session, dismissable, remembered for 30 days. Keep the footer signup as the secondary route for visitors who scroll all the way. Optional: add a returning-visitor variant ("Welcome back — what's new since you last visited").

**Test specification**
- **Hypothesis:** If we add a subtle scroll-triggered email opt-in with editorial-access framing, then newsletter signups per homepage visit will increase materially with no negative impact on bounce rate (Fogg trigger timing; Cialdini reciprocity).
- **Variant A:** footer-only newsletter signup, no incentive
- **Variant B:** scroll-triggered bottom-bar opt-in with editorial-access incentive, plus footer signup
- **Primary metric:** newsletter signups per homepage visit
- **Secondary metrics:** bounce rate (must not increase), opt-in dismissal rate
- **Expected impact:** +200% to +400% on newsletter signups (low base rate)
- **ICE:** I=4, C=7, E=6 → 5.7 (nice-to-have because direct revenue impact is delayed via email channel)
- **Source:** Fogg Behavior Model (trigger timing); Cialdini's reciprocity principle

---

## What makes these examples high-quality

- **Specific:** every observation names an exact element with position and behavior
- **Sourced:** every claim references a specific principle, study, or institution
- **Brand-aware:** recommendations consider whether they fit the brand snapshot (premium vs mid-market vs value)
- **Honest about uncertainty:** when data is missing, the finding says so and recommends research, not action
- **Test-ready:** hypothesis follows "If X, then Y, because Z"; primary metric is named (homepage-appropriate: bounce, scroll, click-to-PDP, etc.); ICE is justified by the breakdown
- **Concrete copy and behavior:** not "improve the hero" — actual headline copy, exact placement, specific incentive type
- **Dutch translations natural:** when output is Dutch, JTBD framing avoids "huren"; terms like "klantreis" or untranslated "funnel" used appropriately

Always match this standard. If a finding can't reach this standard, either dig deeper or remove it from the audit.
