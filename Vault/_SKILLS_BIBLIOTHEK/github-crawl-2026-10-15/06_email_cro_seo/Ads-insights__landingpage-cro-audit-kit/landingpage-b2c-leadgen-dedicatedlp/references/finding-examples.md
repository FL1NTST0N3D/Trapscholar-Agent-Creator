# Worked finding examples — B2C leadgen dedicated landing page quality calibration

These examples show what a high-quality B2C dedicated LP finding looks like across different campaign-types and ICE scores. Use them as a reference standard.

---

## Example 1: 🔴 Critical — Message match (Google Ads, energiebesparende-campagne)

### 🔴 Message match — LP-hero generiek "duurzaam wonen" terwijl Google Ads-keyword "zonnepanelen subsidie 2026"

**Diagnosis**
Visible in screenshot: de LP toont als hoofdheadline "Maak je huis duurzamer" gevolgd door een algemene tekst over energie-efficiëntie. De gebruiker heeft aangegeven dat de Google Ads-campagne specifiek draait op keywords rond "zonnepanelen subsidie 2026". Per ConversionXL message-match research (Bryan Eisenberg) **converteren LPs die de ad-headline letterlijk echoën 2-5x hoger dan generieke LPs**. Per Mark Hurst's Scent of Information volgt de bezoeker een "geur" van zoekquery via advertentie naar landingspagina — elke breuk in die geur veroorzaakt bounce. Een zoeker die "zonnepanelen subsidie 2026" intypte en hier landt, krijgt geen confirmatie dat dit specifiek over zonnepanelen of subsidies gaat — typische response is back-button binnen 5-8 seconden. Dynamic Text Replacement (DTR) per UTM-keyword zou hier de meest leverage-rijke optimalisatie zijn.

**Recommendation**
Drie aanpassingen voor message-match:
1. **Hero-headline herschrijven** naar de specifieke ad-promise: "Zonnepanelen + €2.500 subsidie 2026 — bereken jouw besparing in 60 seconden"
2. **Sub-headline** maakt de match expliciet: "Voor woningeigenaren in Nederland · ISDE-subsidie zonnepanelen · €350-€2.500 vergoeding"
3. **Dynamic Text Replacement (DTR) implementeren** per UTM-keyword zodat keyword-varianten ("zonnepanelen subsidie 2025", "zonnepanelen subsidie aanvragen", "zonnepanelen kosten") allemaal een matching headline tonen. De meeste LP-builders (Unbounce, Instapage, HubSpot) ondersteunen DTR via URL-parameters.

Verifieer dat de ISDE-subsidie 2026 ook daadwerkelijk van toepassing is voordat de claim live gaat (compliance-check).

**Test specification**
- **Hypothesis:** "Als we de hero-headline matchen aan de specifieke ad-keyword en DTR implementeren per UTM-keyword, dan stijgt de conversion rate aanzienlijk omdat scent-of-information behouden blijft en MECLABS-clarity verbetert (ConversionXL message-match; Hurst Scent of Information)."
- **Variant A:** "Maak je huis duurzamer" generieke headline
- **Variant B:** "Zonnepanelen + €2.500 subsidie 2026 — bereken jouw besparing in 60 seconden" + DTR per keyword
- **Primary metric:** conversion rate (calculator-completion + email-gate)
- **Secondary metrics:** bounce rate, above-the-fold conversion rate, cost-per-lead, scroll-depth
- **Expected impact:** +35% tot +80% op conversion rate (message-match fixes leveren historisch hoge lift)
- **ICE:** I=10, C=9, E=7 → 8.7
- **Source:** ConversionXL message-match research (Eisenberg, Laja); Mark Hurst Scent of Information; MECLABS clarity-factor

---

## Example 2: 🔴 Critical — Single primary CTA strategy (Meta-campagne, gratis gids download)

### 🔴 CTA strategy — Vier concurrerende CTAs in hero op gids-download LP

**Diagnosis**
Visible in screenshot: in de hero-zone staan vier vergelijkbaar gewogen CTAs naast elkaar: "Download de gids", "Bekijk demo-video", "Vraag adviesgesprek", en "Bekijk meer over ons". Daarnaast staat in de hoofdnavigatie nog "Diensten", "Over ons", "Blog", "Contact" — totaal 8 conversie-paden in het primaire viewfield. Per Unbounce attention-ratio research **is de ideale verhouding 1:1 (één link, één doel)** — de huidige verhouding van 8:1 (acht links, één conversiedoel) ondergraaft de single-purpose logica van een dedicated landingspagina. Per Hick's Law vertraagt elke keuze de besluitvorming — meerdere gelijkwaardige CTAs creëren paralysis in plaats van actie. Voor een Meta-traffic gids-download (interest-driven, discovery-mode bezoeker) is dit dubbel kritiek: de bezoeker is niet in transactie-modus en wordt makkelijk afgeleid door secundaire opties die geen van allen de campagne-belofte vervullen.

**Recommendation**
Drie aanpassingen voor single-CTA dominantie:
1. **Verwijder de andere drie hero-CTAs.** "Demo-video bekijken", "Adviesgesprek aanvragen" en "Over ons" zijn alle exit-paden uit het campagne-funnel. Behoud uitsluitend "Download de gids" als primaire CTA, eventueel herhaald lager op de pagina.
2. **Verberg hoofdnavigatie.** Vervang door een minimale variant: alleen logo + telefoonnummer (indien telefonisch contact dezelfde conversie-trechter bedient). Per Marketing Sherpa data: **hidden-nav LPs converteren 10-25% beter dan LPs met volledige navigatie**.
3. **Footer minimaliseren** tot privacy-policy + KvK + contact (trust-requirement) — geen "Over ons" / "Diensten" / "Blog" exit-paden.

Single-purpose page-logica trumpt multi-CTA dogma op dit page-type. Op een servicepage of homepage zou multi-CTA passen — hier niet.

**Test specification**
- **Hypothesis:** "Als we de attention-ratio verlagen van 8:1 naar 1:1 door secundaire CTAs en hoofdnavigatie te verbergen, dan stijgt de download-conversion rate substantieel omdat de bezoeker minder exit-opties heeft en MECLABS-friction daalt (Unbounce attention-ratio; Hick's Law)."
- **Variant A:** 4 hero-CTAs + 4 nav-items + footer-nav (8:1 ratio)
- **Variant B:** alleen "Download de gids" CTA + minimale nav (logo + tel) + minimale footer (1:1 ratio)
- **Primary metric:** gids-download conversion rate
- **Secondary metrics:** above-the-fold conversion rate, time-to-conversion, bounce rate
- **Expected impact:** +25% tot +50% op download conversion rate
- **ICE:** I=9, C=9, E=8 → 8.7
- **Source:** Unbounce attention-ratio research; Hick's Law; Marketing Sherpa LP-benchmarks

---

## Example 3: 🔴 Critical — Lead-form design (Google Ads, mid-CAC autobedrijf occasion-aanvraag)

### 🔴 Lead-form — 12 verplichte velden op "Vraag offerte" op autobedrijf-LP

**Diagnosis**
Visible in screenshot: het formulier bevat 12 velden waarvan alle 12 verplicht (rode asterisken op elk veld), inclusief volledig postadres, geboortedatum, BSN-laatste-4-cijfers, kentekenplaat huidige auto, jaarkilometers, voorkeur-financieringsvorm, en gewenste afleverdatum. Voor een eerste-contact offerte-aanvraag op een autobedrijf (mid-ticket consideratie, mid-CAC Google Ads) is dit een aanzienlijk veld-overschot. Per CXL/ConversionXL form-research **reduceert elk overbodig veld de conversion met circa 7-11%** — 12 velden waar er 5-6 nodig zijn betekent een geschatte 30-50% conversion-onderdrukking. Per Hick's Law verandert elk veld in een beslismoment dat de bezoeker uit de funnel kan duwen. BSN-vraag in eerste contact is bovendien een privacy-anxiety trigger (MECLABS anxiety-axis) — totaal disproportioneel voor wat in essentie een interesse-aanvraag is. De velden BSN, kentekenplaat, jaarkilometers zijn waardevol VOORDAT een concrete offerte ontwikkeld wordt, maar niet in deze eerste fase.

**Recommendation**
Reduceer naar 5-6 essentiële velden voor de eerste lead-fase:
1. Naam (verplicht)
2. E-mail (verplicht)
3. Telefoonnummer (verplicht)
4. Type interesse (dropdown: nieuw / occasion / lease — verplicht)
5. Budget-range (dropdown: <€15k / €15-25k / €25-40k / €40k+ — verplicht)
6. Bericht / specifieke vraag (textarea — optioneel)

Verplaats BSN, kentekenplaat, jaarkilometers, financieringsvorm, afleverdatum naar **stap 2** — nadat een verkoper het eerste contact heeft gelegd en interesse is bevestigd. Markeer optionele velden expliciet ("optioneel") in plaats van verplichte met asterisken. Voor een Google Ads mid-CAC campagne is volume + redelijke kwaliteit waardevoller dan extreme pre-qualification — de sales-cyclus van een autobedrijf vangt unqualified leads in stap 2 op. Acknowledge tradeoff: dit verhoogt volume aanzienlijk, mogelijk met lichte kwaliteitsdaling — meet MQL-ratio (welk percentage leidt tot showroom-bezoek?) om kalibratie te valideren.

**Test specification**
- **Hypothesis:** "Als we het formulier reduceren van 12 naar 5-6 essentiële velden, dan stijgt de form-completion rate substantieel doordat elk overbodig veld friction toevoegt en BSN-vraag privacy-anxiety triggert (CXL form research; Hick's Law; MECLABS anxiety)."
- **Variant A:** 12-velden formulier
- **Variant B:** 5-6 velden formulier, vervolg-velden in stap 2 na eerste contact
- **Primary metric:** form-completion rate
- **Secondary metrics:** form-start rate, field-drop-off per veld, MQL-ratio downstream (showroom-bezoek), cost-per-MQL
- **Expected impact:** +40% tot +80% op form-completion rate
- **ICE:** I=10, C=9, E=8 → 9.0
- **Source:** CXL/ConversionXL form research; Hick's Law; MECLABS anxiety-axis; Baymard form-field research

---

## Example 4: 🟠 Important — Lead-magnet propositie (Meta-campagne, gratis bespaartip-gids)

### 🟠 Lead-magnet — Gids "Tips om te besparen" zonder concretisering van inhoud, lengte of waarde

**Diagnosis**
Visible in screenshot: de LP biedt "Onze gratis gids met bespaartips" aan, met een generieke book-mockup en de tekst "Vul je gegevens in en ontvang de gids per e-mail". Per Hormozi's irresistible-offer principles ontbreken drie van de vier waarde-componenten: dream outcome (welk concreet resultaat?), perceived likelihood (welk bewijs werkt het?), en time delay (hoe snel waarde?). Per Marketing Sherpa value-exchange-clarity research **converteren specifieke lead-magnets ("Ontvang binnen 24u een gratis bespaar-analyse van €350-waarde") 40-60% hoger dan vage** ("vraag info aan"). Per Cialdini's reciprocity-principe activeert dit alleen bij voldoende waargenomen waarde — een "gids met tips" is voor de meeste consumenten te onspecifiek om uit gemak hun gegevens af te staan. Voor Meta-traffic (interest-driven, discovery-mode) is de drempel voor "ik geef mijn e-mail" hoger dan voor Google Search-traffic — de waarde moet helder zijn.

**Recommendation**
Concretiseer de lead-magnet op vier dimensies:
1. **Specificiteit:** "De Energiebesparing-Gids 2026 — 32 pagina's met 47 concrete tips voor woningeigenaren"
2. **Outcome-anker:** "Gemiddeld €380-€620 lagere energierekening per jaar"
3. **Bewijs:** "Gebaseerd op data van 1.200+ Nederlandse huishoudens" (waar verifieerbaar)
4. **Time-anchor:** "Direct in je inbox — start vandaag nog"

Voeg een visuele preview toe van de gids (cover + 1-2 binnenpagina's klein zichtbaar) zodat de lead-magnet visueel-tastbaar wordt. Toon optioneel een mini-content-lijst ("Inhoud: hoofdstuk 1 — quick wins onder €50 / hoofdstuk 2 — middel-investeringen / hoofdstuk 3 — grote renovaties / etc.") zodat de bezoeker ziet wat de gids inhoudt vóór invullen.

**Test specification**
- **Hypothesis:** "Als we de lead-magnet concretiseren met specifieke inhoud, outcome-anker, bewijs en time-anchor, dan stijgt de form-completion rate doordat de waargenomen waarde Cialdini's reciprocity-drempel overschrijdt (Hormozi irresistible offer; Marketing Sherpa value-exchange-clarity)."
- **Variant A:** "Onze gratis gids met bespaartips" + generieke book-mockup
- **Variant B:** concretisering op 4 dimensies + visuele preview + inhoud-lijst
- **Primary metric:** form-completion rate
- **Secondary metrics:** scroll-depth tot lead-magnet sectie, time-on-page, bounce rate
- **Expected impact:** +15% tot +35% op form-completion rate
- **ICE:** I=8, C=8, E=9 → 8.3
- **Source:** Hormozi irresistible-offer principles; Cialdini reciprocity; Marketing Sherpa value-exchange-clarity

---

## Example 5: 🟠 Important — Reviews & ratings (Google Display, cold traffic, kapsalon-campagne)

### 🟠 Reviews — Geen reviews boven de vouw op cold-traffic Display-LP

**Diagnosis**
Visible in screenshot: de LP toont geen review-widget, ster-rating of testimonials in de eerste schermweergave. Onder aan de pagina (na drie scroll-secties) staat één tekstuele testimonial zonder bron of foto. Een externe check (Google Business Profile, openbaar zichtbaar) toont 142 Google reviews met 4,7-gemiddelde. Voor een cold-traffic Display-campagne is dit een gemiste kans: per Spiegel Research Center **converteren services met zichtbare reviews tot 270% beter dan services zonder**. Per BrightLocal local-service research is **87% van consumenten reviews-driven bij lokale-dienst-keuzes**. Cold traffic (Google Display) heeft GEEN voorafgaande context — de bezoeker kent het merk niet, heeft niet actief gezocht, en arriveert via banner-impressie. Trust signals dragen daardoor extra zwaar op dedicated LPs zonder navigatie (context-loosheid). Onder-de-vouw plaatsing betekent dat de meerderheid van Display-bezoekers (die typisch 8-15 seconden besteden voordat ze beslissen) de reviews nooit ziet.

**Recommendation**
Drie aanpassingen voor review-zichtbaarheid:
1. **Google review-widget in de hero-zone** — direct onder de hoofd-CTA, met sterren-rating + aantal ("Google-rating 4,7 uit 142 reviews"). Maakbaar via embedded Google review-widget of Klantenvertellen-widget.
2. **2-3 named testimonials** met foto en behandel-context lager op de pagina ("Mijn kleuring-experience bij Studio X — Lisa, 34 jaar, Hilversum").
3. **Trust-strip near hero** met combinatie reviews + jaren actief + klantenaantal ("⭐ 4,7 (142 reviews) · sinds 2014 · 8.000+ klanten geknipt").

Voor cold traffic moet sociaal bewijs zichtbaar zijn vóór de visitor afhaakt — wat doorgaans binnen 8-15 seconden gebeurt op Display-traffic. Acceptatie-noot: gebruik alleen reviews waar publicatie-toestemming bestaat.

**Test specification**
- **Hypothesis:** "Als we Google reviews zichtbaar maken in de hero-zone plus 2-3 named testimonials, dan stijgt de conversion rate op cold-traffic doordat sociaal bewijs Cialdini's principe activeert vóór de visitor afhaakt (Spiegel Research 270%; BrightLocal 87%; Cialdini social proof)."
- **Variant A:** geen reviews zichtbaar in hero / eerste secties
- **Variant B:** Google review-widget hero + 2-3 named testimonials + trust-strip
- **Primary metric:** conversion rate (boeking-CTA)
- **Secondary metrics:** above-the-fold conversion rate, bounce rate (omlaag), scroll-depth
- **Expected impact:** +20% tot +45% op conversion rate (sterker effect bij cold traffic)
- **ICE:** I=8, C=9, E=8 → 8.3
- **Source:** Spiegel Research Center; BrightLocal local-service research; Cialdini social proof

---

## Example 6: 🟢 Nice-to-have — Mobile experience (TikTok-campagne, jonge doelgroep, korte LP)

### 🟢 Mobile experience — Sticky mobile CTA op zeer korte hero-only LP

**Diagnosis**
Visible in screenshot: de LP is uitzonderlijk kort — alleen een hero-sectie met productafbeelding, korte propositie en CTA, gevolgd door een korte trust-strip en footer. Totale paginalengte op mobile bedraagt circa 1,5-2 schermhoogtes. Per Baymard mobile commerce research **is een sticky bottom-CTA op pagina's >2 schermhoogtes non-negotiable**, maar deze pagina valt onder die drempel. De primaire CTA is op de huidige pagina-lengte vrijwel altijd zichtbaar tijdens het scrollen. Per Fogg's gedragsmodel is op deze korte LP de motivatie-piek direct bij het laden (visitor heeft net op TikTok-ad geklikt) — een tweede trigger via sticky CTA voegt marginale waarde toe. Voor TikTok-traffic (jonge doelgroep, snel browse-tempo, mobile 95%+) kan een sticky CTA echter helpen bij het kleine percentage visitors dat wel scrollt. Impact is bescheiden gegeven de paginalengte.

**Recommendation**
Twee paden afhankelijk van data:
1. **Geen sticky CTA toevoegen** als hot-jar/sessie-recordings tonen dat scroll-engagement op de huidige pagina hoog is (>70% van visitors scrolt voorbij CTA) en bounce rate al laag (<40%). De pagina is dan al goed gekalibreerd voor zijn paginalengte.
2. **Sticky CTA toevoegen** als data toont dat een meetbaar percentage visitors (>20%) scrollt voorbij de primaire CTA zonder te converteren. Sticky bar matched de primaire CTA-copy, hoogte 56-64px op mobile, verschijnt na scroll voorbij primaire CTA.

Acceptatie-noot: aanbevolen om huidige mobile sessie-data te bekijken voordat geïmplementeerd wordt. Voor een hero-only LP van 1,5-2 schermhoogtes is sticky CTA waarschijnlijk net-positief maar het effect is bescheiden — niet de prioritaire investering vs. hogere-impact aanpassingen elders.

**Test specification**
Test niet aanbevolen nog — eerst data verzamelen:
- Bekijk Hotjar/sessie-recordings: scrolt de TikTok-traffic typisch voorbij de CTA?
- Meet bounce rate per scroll-segment (boven primaire CTA / na primaire CTA / na trust-strip)
- Als >20% van visitors scrolt voorbij CTA zonder te converteren → groene licht voor sticky CTA test
- Als scroll-engagement laag is (<30%) → sticky CTA voegt weinig toe; investeer in hero-optimalisatie

**ICE:** I=4, C=6, E=8 → 6.0

**Source:** Baymard mobile commerce research; Fogg Behavior Model; thumb-zone (Hoober)

---

## What makes these examples high-quality

- **Traffic-source aware:** elke example signaleert traffic-source (Google Search / Meta / Display / TikTok / email) en kalibreert recommendations
- **Campaign-type-aware:** form-driven / download-driven / booking-driven onderscheiden
- **Single-purpose logic respected:** Example 2 weerstaat de "voeg meer CTAs toe"-reflex en past juist single-CTA dominantie toe
- **Message match als eigen kritieke categorie:** Example 1 toont hoe dit de hoogste impact-finding kan zijn
- **Lead-quality vs lead-volume tradeoff erkend:** Example 3 acknowledged tradeoff expliciet en koppelt CAC aan recommendation
- **Context-loosheid van LPs erkend:** Example 5 wijst op cold-traffic extra-weight van trust signals
- **Visible-in-screenshot prefix:** elke example begint diagnose met expliciete verwijzing naar wat zichtbaar is
- **Authenticiteits-restraint:** Example 5 noemt "publicatie-toestemming" zonder existing reviews als fake te bestempelen
- **Concrete copy in NL:** exacte headline-alternatieven, exacte form-velden, exacte lead-magnet propositie
- **Dutch translations natuurlijk:** landingspagina, formulier, weggever, gids, kapsalon — passend bij NL-context
- **Test-ready:** hypothesis volgt "If X, then Y, because Z"; primary metric is LP-specifiek (conversion rate, form-completion, bounce, CPL, above-the-fold conversion)
- **Sources gemixt:** Unbounce, ConversionXL, Marketing Sherpa, Hormozi, Spiegel, BrightLocal, Cialdini, MECLABS, Baymard — LP-specifieke bronnen naast universele CRO-bronnen
- **Honest about ICE-confidence:** message-match en form-friction hebben hoge confidence (veel test-data); sticky CTA op korte LP heeft lagere confidence — ICE varieert

Always match this standard. If a finding can't reach this standard, either dig deeper or remove it from the audit.
