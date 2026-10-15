# Worked finding examples — B2B leadgen dedicated LP quality calibration

These examples show what a high-quality B2B dedicated-LP finding looks like across different campaign-types, B2B-service-types, and ICE scores. Use them as a reference standard.

---

## Example 1: 🔴 Critical — Message match (LinkedIn Ads → SaaS demo LP)

### 🔴 Message match — LinkedIn Ad belooft "marketing ROI calculator", LP toont algemene demo-CTA

**Diagnosis**
Visible in screenshot: de LP toont als headline "Schedule a personalized demo of [Brand Platform]" met een demo-CTA. De gebruiker heeft de LinkedIn-ad-copy meegestuurd: "Calculate your marketing ROI in 2 minutes — free interactive calculator". Per ConversionXL message-match research **is mismatch tussen ad-promise en LP-content de #1 oorzaak van LP-bounce** — 73% van B2B visitors verlaat een LP binnen 8 seconden als ze de beloofde content niet direct herkennen. Per Hurst's Scent of Information: visitor arrived met declaratieve verwachting ("ik klikte voor calculator"), en de LP toont een fundamenteel andere offer (demo). Voor mid-market B2B SaaS (€500-5k/m, marketing director doelgroep) is dit een catastrofale mismatch — visitor moet cognitief bridgen ("de ad zei calculator, de page zegt demo, doen ze hetzelfde?") wat 5-8 seconden duurt; binnen die tijd bouncet 73%. Per declarative-thinking patterns: campagne-traffic verwacht VERBATIM-recall, niet alternative-but-related. De CPL voor LinkedIn Ads (typisch €30-€80 per click voor marketing-director targeting) wordt hier verbrand zonder conversion-opportunity.

**Recommendation**
Drie aanpassingen voor message-match herstel:

1. **Headline match verbatim aan ad-copy:**
   - Vervang "Schedule a personalized demo" door "Calculate Your Marketing ROI in 2 Minutes — Free Interactive Calculator"
   - Exact-match versterkt scent en bouwt declarative-confirmation

2. **Pivot LP-content naar calculator-as-offer:**
   - Calculator-widget prominent above-the-fold (waar nu demo-CTA staat)
   - Optionele secondary: "After calculating, schedule a demo to discuss results" (als bottom-of-funnel optie NA calculator-engagement)

3. **Visual style match aan ad-creative:**
   - Calculator-screenshot of preview-image in hero
   - Maintain ad-color-palette en visual-tone op LP voor visuele continuïteit

**Acceptatie-noot:** dit vereist mogelijk een nieuwe LP-build of een major-rebuild van bestaande LP. Alternatief: pas de ad-copy aan om met de LP te matchen ("Schedule a marketing platform demo"). Welke kant gekozen wordt hangt af van bestaande performance — calculator-LPs converteren typisch 15-25% (top-funnel volume), demo-LPs 3-10% (decision-stage quality). Voor dezelfde LinkedIn-budget levert calculator-LP doorgaans 2-3x meer leads (lager-funnel kwaliteit), maar minder direct-sales-routable.

**Test specification**
- **Hypothesis:** "Als we de LP-headline en het primaire aanbod aanpassen om verbatim te matchen met de LinkedIn-ad-promise (calculator), dan stijgt de form-completion rate dramatisch doordat message-match mismatch — de #1 oorzaak van LP-bounce — wordt opgelost (ConversionXL message-match research; Hurst Scent of Information; declarative-thinking patterns)."
- **Variant A:** LP toont demo-CTA terwijl ad calculator beloofde
- **Variant B:** LP-headline en hero match verbatim aan ad-promise (calculator)
- **Primary metric:** form-completion rate
- **Secondary metrics:** bounce rate, time-to-form-fill, cost-per-lead, downstream MQL→SQL ratio
- **Expected impact:** +60% tot +200% op form-completion rate (message-match impact is enorm)
- **ICE:** I=10, C=9, E=7 → 8.7
- **Source:** ConversionXL message-match research; Hurst Scent of Information; declarative-thinking patterns

---

## Example 2: 🔴 Critical — Friction reduction & distraction management (B2B consultancy LP)

### 🔴 Friction reduction — Volledige hoofdnavigatie + sidebar op B2B consultancy demo-LP

**Diagnosis**
Visible in screenshot: de dedicated LP voor een B2B operations-consultancy demo-aanvraag toont een volledige hoofdnavigatie (8 menu-items inclusief Home, Diensten, Branches, Blog, Cases, Over Ons, Contact, Login), een rechtse sidebar met "Latest articles" en "Related services", en een footer met mega-menu (12+ links). Voor een dedicated paid-traffic LP (consultancy mid-ticket €25k-100k) is dit een fundamentele schending van single-purpose page logic. Per Unbounce 1:1 attention ratio **moet een dedicated LP idealiter één link naar één conversie-doel hebben**; deze LP heeft een attention-ratio van naar schatting 25:1 of hoger. Per distraction-to-reaction ratio research **reduceert elke non-conversie-link de conversie met gemiddeld 5-15%** — met 20+ navigatie-links is de cumulatieve impact catastrofaal. Per ConversionXL paid-traffic research lift navigation-removal op B2B dedicated LPs de conversie 10-25%. Visitor kreeg een ad-promise, klikte met intent, en wordt nu uitgenodigd om naar 20 andere pagina's te navigeren in plaats van te converteren — paid-spend wordt direct verbrand naar non-converting page-visits.

**Recommendation**
Drie aanpassingen voor distraction-removal:

1. **Hoofdnavigatie strippen** of minimaliseren tot logo + optionele "Contact" link:
   - Verwijder: Home, Diensten, Branches, Blog, Cases, Over Ons (alle exit-paths)
   - Behoud: alleen brand-logo (klikbaar of inert)
   - Optioneel: minimaal "Bel ons" alternative-CTA in nav-positie

2. **Sidebar volledig verwijderen:**
   - "Latest articles" sectie weg
   - "Related services" sectie weg
   - LP wordt single-column, fokus op offer

3. **Footer compact maken:**
   - Verwijder mega-menu
   - Behoud alleen: legal-links (Privacy, Voorwaarden, Cookies), KvK-nummer, copyright
   - Maximaal 4-5 footer-links totaal

**Acceptatie-noot:** sommige brands prefereren light-navigatie voor "we hebben niets te verbergen"-trust. Voor enterprise-targeting kan stripped-navigatie soms onnatuurlijk aanvoelen ("dit is een landings-truc"). Mitigatie: behoud licht-grijze, kleine "Contact ons direct: 020-123456" of logo in plaats van volledige nav, wat single-purpose feel behoudt zonder hard-stripped-navigation suggestie. Voor MKB-targeting is volledig strippen meestal acceptabel.

**Test specification**
- **Hypothesis:** "Als we de hoofdnavigatie en sidebar strippen en de footer compact maken, dan stijgt de form-completion rate aanzienlijk doordat de attention-ratio van naar schatting 25:1 verbetert naar 1:1 of 2:1, conform Unbounce dedicated-LP-principes (Unbounce 1:1 attention ratio; distraction-to-reaction ratio research; ConversionXL paid-traffic research)."
- **Variant A:** volledige nav + sidebar + footer-mega-menu
- **Variant B:** logo-only nav + geen sidebar + compact footer
- **Primary metric:** form-completion rate
- **Secondary metrics:** bounce rate, time-on-page, scroll-depth, exit-via-nav-clicks
- **Expected impact:** +15% tot +30% op form-completion rate
- **ICE:** I=8, C=9, E=9 → 8.7
- **Source:** Unbounce 1:1 attention ratio; distraction-to-reaction ratio research; ConversionXL paid-traffic LP research

---

## Example 3: 🔴 Critical — Lead-magnet propositie (B2B managed-IT audit LP)

### 🔴 Lead-magnet — Vage "Vraag een gratis audit aan" zonder Hormozi-value-elementen

**Diagnosis**
Visible in screenshot: de LP voor een B2B managed-IT-services audit-offer toont als hero "Vraag een gratis IT-audit aan" en als sub-headline "Onze experts kijken graag met je mee". Geen specificiteit over scope, geen time-anchor, geen proof-backing, geen preview van wat de visitor ontvangt. Voor een mid-ticket managed-IT-services aanbieder (€10k-50k/jaar contracts, doelgroep IT-managers en CFOs) is dit een fundamenteel onder-ontwikkelde lead-magnet. Per Hormozi's value-equation **mist deze offer alle vier de waarde-componenten**: dream outcome is vaag ("kijken graag met je mee"), perceived likelihood is nul (geen customer-count of proof), time delay is onbepaald, effort and sacrifice onduidelijk (welke gegevens nodig?). Per Marketing Sherpa B2B lead-magnet patterns **converteren specifieke audit-offers ("Free 30-min infrastructure audit + 47-page rapport") 2-4x beter dan algemene "audit"-offers**. Per Cialdini reciprocity: vage offers triggeren GEEN reciprocity-respons; visitor geeft contact-info pas in ruil voor concrete waarde. Op een dedicated LP waar lead-magnet IS het hele bestaansrecht, ondergraaft dit het volledige conversion-doel.

**Recommendation**
Vervang de generieke audit-offer door een Hormozi-aligned irresistible-offer:

**Specifieke offer-structuur:**

```
**Free 30-min Infrastructure Security Audit**

✓ 12-punts assessment van je huidige IT-omgeving
✓ Concrete kwetsbaarheden geïdentificeerd
✓ 47-page rapport met aanbevelingen
✓ Uitgevoerd door CISSP-gecertificeerde auditeurs
✓ Gemiddeld 5 critical-vulnerability-fixes per audit

**Rapport in je inbox binnen 5 werkdagen.**

Gebruikt door 200+ Nederlandse MKB-bedrijven.
```

**Component-breakdown (Hormozi value-equation):**
- **Dream outcome:** infrastructure security, identified vulnerabilities, fixes
- **Perceived likelihood:** "200+ MKB-bedrijven", CISSP-certificering, "gem. 5 fixes"
- **Time delay:** "5 werkdagen" specifiek
- **Effort and sacrifice:** "30 minuten" + simple form

**Visuele preview** van het rapport (cover-image + table-of-contents) naast form. **Voeg klantlogos** toe direct onder offer (5-6 herkenbare MKB-bedrijfslogos) als peer-validation.

**Test specification**
- **Hypothesis:** "Als we de generieke audit-offer vervangen door een Hormozi-aligned irresistible-offer met specifiek scope, customer-count proof, time-anchor en preview, dan stijgt form-completion rate aanzienlijk doordat alle vier value-componenten worden geactiveerd (Hormozi value-equation; Marketing Sherpa B2B lead-magnet patterns; Cialdini reciprocity)."
- **Variant A:** "Vraag een gratis IT-audit aan / Onze experts kijken graag met je mee"
- **Variant B:** specifieke offer met scope + customer-count + time-anchor + preview
- **Primary metric:** form-completion rate
- **Secondary metrics:** form-start rate, scroll-to-offer, time-on-page, downstream MQL-quality
- **Expected impact:** +80% tot +150% op form-completion rate
- **ICE:** I=9, C=8, E=7 → 8.0
- **Source:** Hormozi "$100M Offers" (value-equation); Marketing Sherpa B2B lead-magnet research; Cialdini reciprocity

---

## Example 4: 🔴 Critical — Lead-form design (whitepaper download-LP met BANT-form)

### 🔴 Lead-form — 11-velden BANT-form op top-funnel whitepaper download

**Diagnosis**
Visible in screenshot: de LP voor een gratis whitepaper download ("State of B2B Marketing Automation 2025") toont een form met 11 velden waarvan 10 verplicht: naam, achternaam, work-email, bedrijfsnaam, role, bedrijfsgrootte, industry, current-marketing-platform, jaarlijks-marketing-budget, implementatie-timeline, en use-case-textarea. Voor een top-funnel research-stage lead-magnet (whitepaper download — visitor wil research-content, niet sales-conversatie) is dit een fundamentele over-qualification. Per CXL/ConversionXL form-research **reduceert elke veld de form-completion met gemiddeld 7-11%** — met 11 velden waar 3-4 nodig zijn, betekent dit naar schatting 50-70% form-completion-onderdrukking. Per Forrester B2B buyer research **doen B2B-decision-makers 70%+ van research zelf-bedienbaar** vóór ze sales-contact toelaten; een whitepaper download is bij definitie research-stage, niet decision-stage. Per Hormozi value-equation: een 11-velden form maakt "effort and sacrifice" disproportioneel hoog voor de geleverde waarde (een rapport). Per gated-content economics: heavy-gating op top-funnel content kills lead-volume zonder lead-quality te verhogen — research-stage visitors die afhaken vullen geen form-velden eerlijk in.

**Recommendation**
Reduceer naar 3 velden voor top-funnel whitepaper download:

**Minimaal form-set:**
1. **Work-email** (verplicht) — voor whitepaper-delivery + nurture-sequence
2. **Naam** (verplicht) — personalization voor nurture
3. **Bedrijfsnaam** (verplicht) — minimal qualification context

**Optioneel:** role (dropdown) — als marketing-team specifieke nurture-tracks wil

**Verplaats BANT-velden naar fase 2:**
- BANT-qualificatie hoort op demo-aanvraag of audit-aanvraag, niet op whitepaper download
- Verzamel BANT later in nurture-sequence (progressive profiling)
- Bij volgende form-fill (mid-funnel) vraag company-size en use-case
- Bij decision-stage form (demo/audit) vraag budget + timeline + decision-maker

**Acceptatie-noot:** dit verlaagt mogelijk de gemiddelde MQL→SQL ratio op deze specifieke lead-magnet (geen BANT-voorqualificatie). VOORDEEL: form-completion 3-5x hoger, lead-volume dramatisch op, nurture-pipeline gevuld. Per Forrester research scheidt 80%+ van B2B buyers self-research-stage van decision-stage; deze LP behoort op research-pipeline-vulling te focussen, niet op pre-qualificatie.

**Test specification**
- **Hypothesis:** "Als we het 11-velden BANT-form reduceren naar 3 essentiële velden (email, naam, bedrijf) op een top-funnel whitepaper download, dan stijgt form-completion rate dramatisch doordat over-qualification wordt verwijderd voor research-stage visitors (CXL form-research; Forrester self-research patterns; gated-content economics; Hormozi effort-and-sacrifice)."
- **Variant A:** 11-velden BANT-form
- **Variant B:** 3-velden minimal form (email, naam, bedrijf)
- **Primary metric:** form-completion rate
- **Secondary metrics:** form-start rate, lead-volume per maand, downstream nurture-engagement, MQL-volume vs MQL-quality
- **Expected impact:** +200% tot +400% op form-completion rate (form-shortening op heavy-gated content levert disproportionate volume)
- **ICE:** I=9, C=9, E=9 → 9.0
- **Source:** CXL/ConversionXL form-research; Forrester B2B self-research patterns; gated-content economics research; Hormozi value-equation

---

## Example 5: 🟠 Important — Above-the-fold (B2B consultancy demo-LP)

### 🟠 Above-the-fold — Feature-list hero op Operations Consultancy demo-LP zonder business-outcome

**Diagnosis**
Visible in screenshot: de demo-LP voor een operations-consultancy toont als hero "End-to-end operational excellence: process optimization, supply chain consulting, digital transformation, change management." Sub-headline: "Trusted partner for your business needs." Voor een B2B consultancy demo-aanvraag (deal-size €25k-100k, doelgroep COO/Operations Directors) is dit een fundamenteel oncommuniceerde positie. Per April Dunford's B2B positioning **moet een dedicated LP voor specifieke campagne-traffic in 5 seconden communiceren WAT outcome de visitor krijgt, NIET welke services het bedrijf aanbiedt**. Per Challenger Sale reageren B2B-decision-makers op insight-led messaging dat hun probleem herframet — de huidige hero feature-stacking levert geen insight, geen herframing, geen differentiatie. Per MECLABS Conversion Sequence: de v-factor (perceived value) is laag omdat geen concreet outcome wordt gecommuniceerd. Per Forrester B2B buyer research: COO/Operations-Directors evalueren consultancy-vendors specifiek op "verstaat dit bedrijf MIJN industry-pain?" — generieke service-listing scoort daar nul op. De campagne-traffic gevoeligheid is hoog: visitor heeft op een specifieke ad geklikt; vague LP-positionering ondergraaft alle vooraf opgebouwde scent.

**Recommendation**
Vervang feature-stacking door outcome-led headline met Challenger-insight. Pas op B2B-consultancy:

**Headline-structuur:** "[Specific outcome] voor [specifieke doelgroep]. [Industry-insight of differentiator]."

Voorbeeld toepassingen:

**Optie A — Outcome-led:**
- ✅ "Manufacturing COOs: Cut operational waste with 23-47% within 6 months."

**Optie B — Challenger-insight-led:**
- ✅ "Most operations consultants find waste. Few help you eliminate it. Here's what we do differently."

**Sub-headline:** specificeer audience + credibility-anchor
- "Voor manufacturing companies €10-100M omzet. 47+ implementaties bij Nederlandse industrial-bedrijven."

**Primary CTA:** matched aan demo-LP doel:
- "Plan 30-min discovery call →" met onder kleine "Of bekijk 3 sector-cases"

**Optioneel:** customer-quote met sector-context onder hero: "We've worked with [Brand] across two transformation programs. Their pragmatic approach saved us 18 months on our digital transformation." — Sector-relevante CFO-quote bouwt instant peer-validation.

**Test specification**
- **Hypothesis:** "Als we de generieke feature-stacking hero vervangen door outcome-led messaging met sector-specifieke positioning en insight-led framing, dan stijgt de demo-request rate aanzienlijk doordat decision-makers direct herkennen of dit voor hen relevant is (April Dunford B2B positioning; Challenger Sale; MECLABS; Forrester B2B buyer research)."
- **Variant A:** "End-to-end operational excellence: [feature-list]. Trusted partner for your business needs."
- **Variant B:** outcome-led headline + sector-specificity + customer-quote
- **Primary metric:** demo-request rate
- **Secondary metrics:** bounce rate, time-on-page, scroll-depth, downstream sales-cycle progression
- **Expected impact:** +30% tot +60% op demo-request rate
- **ICE:** I=8, C=8, E=8 → 8.0
- **Source:** April Dunford "Obviously Awesome"; Challenger Sale (Dixon & Adamson); MECLABS Conversion Sequence Heuristic; Forrester B2B buyer research

---

## Example 6: 🟢 Nice-to-have — Customer logos & social proof (calculator-LP)

### 🟢 Customer logos — Generieke "Trusted by industry leaders" zonder concrete logos op ROI-calculator-LP

**Diagnosis**
Visible in screenshot: de ROI-calculator-LP voor een marketing-automation SaaS toont een sectie met de tekst "Trusted by industry leaders worldwide" zonder concrete klantlogos eronder — alleen een algemeen tekst-statement. Voor een mid-funnel calculator-LP (waar lead-magnet — de calculator zelf — de hoofdaanbod is) is dit een gemiste kans, maar genuanceerd vs. bv. een demo-LP waar logos kritisch zijn. Per Edelman B2B Trust Barometer **dragen visible-customer-logos significant meer trust dan tekst-claims over customer-aantallen**. Echter, op een calculator-LP is de calculator zelf het primaire conversion-driver; logos zijn supporting trust-element, niet dominant. Per logo-credibility research lift een logo-strip op B2B LPs de conversie met 10-25%, met effect aan de lagere kant op calculator-LPs vs. demo-LPs. Voor mid-market SaaS targeting marketing-teams: peer-validation via herkenbare brand-logos versterkt de "deze tool is voor mij"-feeling tijdens calculator-engagement. De impact is bescheiden vergeleken met message-match of form-shortening, daarom nice-to-have.

**Recommendation**
Twee paden afhankelijk van logo-permissions en strategy:

**Optie A — Echte logos toevoegen:**
- Vervang tekst-claim door logo-strip met 5-8 herkenbare customer-logos
- Monochrome treatment voor visuele coherentie
- Geplaatst: direct onder calculator-interface OF in trust-strip onder hero
- Optioneel: "Used by marketing teams at:" framing-tekst voor concrete context

**Optie B — Customer-count-aggregate als alternatief:**
- Als logo-permissions ontbreken: "Trusted by 500+ marketing teams" met visuele icon-grid (industries served)
- Concrete metric beats generic "industry leaders"-tekst
- Toon optioneel bedrijfsgrootte-mix: "From 50-person startups to 5,000-person enterprises"

**Acceptatie-noot:** logo-toevoeging vereist permissions van klanten — typisch contractueel geregeld voor enterprise-klanten, vraag het. Logo-strip op calculator-LP is minder kritisch dan op demo-LP (waar peer-validation directere conversion-impact heeft). Eerst zwaardere findings adresseren; deze als latere optimization-iteratie.

**Test specification**
Test optioneel — eerst onderzoek aanbevolen:
- Verzamel customer-logo-permissions (typisch 1-2 dagen werk)
- Welke 5-8 logos zijn meest herkenbaar voor target-audience (marketing teams)?
- Industry-mix relevant voor calculator-audience?

Bij implementatie: A/B-test "Trusted by industry leaders" generic-tekst vs. concrete logo-strip op calculator-completion-rate én downstream form-submission (email-gate na calculator).

**ICE:** I=5, C=7, E=8 → 6.7

**Source:** Edelman B2B Trust Barometer; logo-credibility research; B2B LP peer-validation patterns

---

## What makes these examples high-quality

- **Campaign-type aware:** elke example signaleert campaign-type (LinkedIn Ads → SaaS demo / consultancy demo-LP / managed-IT audit-LP / whitepaper download-LP / calculator-LP) en kalibreert recommendations
- **B2B-service-type calibratie expliciet:** SaaS mid-market, consultancy mid-ticket, managed services, marketing-automation SaaS — elk met service-type-specifieke proof- en form-keuze
- **Message-match als #1 priority:** Example 1 demonstreert hoe message-match mismatch de zwaarste finding is (ICE 8.7), met expected impact +60-200%
- **Single-purpose page logic respected:** Example 2 toont distraction-removal als kritiek vs. multi-purpose page (homepage) waar dit fout zou zijn
- **Lead-magnet stage matched to form-length:** Example 4 demonstreert catastrofale over-qualification (11 velden BANT op top-funnel whitepaper) en juist over-shortening risk wordt benoemd
- **Hormozi value-equation toegepast:** Example 3 expliciet structuur volgens dream outcome × perceived likelihood / time delay × effort and sacrifice
- **Decision-maker context respected:** geen consumer-style aanbevelingen; COO/CFO/Marketing-Director anxieties dominant
- **Scarcity/urgency carefully calibrated:** geen "Only 3 spots left" aanbevolen waar dit B2B-counterproductief zou zijn
- **Visible-in-screenshot prefix:** elke example begint diagnose met expliciete verwijzing
- **Authenticity restraint:** geen claims dat customer-logos unauthorized zijn of metrics inflated zonder bewijs
- **Concrete copy:** exacte headline-alternatieven, exacte form-velden-sets, exacte Hormozi-offer-structuren
- **Dutch/English mix natuurlijk:** B2B-jargon zoals MQL, SQL, BANT, SaaS, ROI, CISSP blijft Engels in NL-context; product-namen en CTAs aangepast aan audit-taal
- **Test-ready:** hypothesis volgt "If X, then Y, because Z"; primary metric is dedicated-LP-specifiek (form-completion rate, cost-per-lead, demo-request rate, MQL-volume)
- **Sources gemixt:** ConversionXL, Hurst, Unbounce, Hormozi, April Dunford, Challenger Sale, MECLABS, Forrester, Cialdini, BANT/MEDDIC, CXL — dedicated-LP-specifieke bronnen dominant
- **Honest about ICE-confidence:** message-match en form-length hoge confidence (sterke B2B-LP research base), customer-logos op calculator-LP lagere confidence (genuanceerde context) — ICE varieert dienovereenkomstig

Always match this standard. If a finding can't reach this standard, either dig deeper or remove it from the audit.
