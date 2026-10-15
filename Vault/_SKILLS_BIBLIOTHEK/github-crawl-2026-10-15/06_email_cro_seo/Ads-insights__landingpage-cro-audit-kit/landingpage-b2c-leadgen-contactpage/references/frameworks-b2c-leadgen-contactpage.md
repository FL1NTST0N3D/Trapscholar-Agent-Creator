# Frameworks for B2C Leadgen Contact Page Audits

This reference file contains the CRO and contact-page-specific frameworks, principles, and applied research. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

B2C contact pages are uniquely prone to fabricated findings because so much is JavaScript-rendered:
- "We zijn nu open / gesloten"-status widgets (real-time JavaScript)
- WhatsApp click-to-chat buttons (often dynamic, sometimes substituted)
- Google Maps embed (iframe with conditional loading)
- Form builders (Gravity Forms, Formidable, Typeform, HubSpot, custom)
- Sticky CTAs on mobile (conditional rendering)
- Chat widgets (Intercom, Drift, Zendesk, native chat)
- Phone-click tracking (numbers that look static but route via dynamic substitution per source)
- Multi-vestiging zoekers / store locators
- Location-based conditional content

**For every finding, verify against screenshots before delivering.**

---

## CRITICAL — High-intent visitor logic

The contact-page visitor is DIFFERENT from service-page or dedicated-LP visitor. They've already evaluated the brand. The job is NOT to convince — it's to **remove friction from their preferred conversion path.**

**Do NOT automatically recommend on contact pages:**
- "Add more proof / testimonials / case studies" — visitor already convinced, this adds noise
- "Strengthen value proposition" — too late, decision already made
- "Add lead-magnet" — wrong page type, visitor wants direct contact
- "Add sales-style copy" — visitor wants practical info, not pitch

**DO recommend (when appropriate):**
- Friction-removal on preferred channel (tap-to-call, WhatsApp button, sticky form-CTA)
- Multi-channel parallel CTAs matched to consumer preferences
- Bereikbaarheid/openingstijden as primary content
- Response-time clarity ("we bellen binnen 4 uur terug")
- Lokale info (route, parkeren, OV) for fysiek bedrijven

The high-intent rule trumps the conviction-needed best-practice on this page-type.

---

## CRITICAL — Multi-channel parallel, not multi-CTA competing

On service pages and dedicated LPs, multiple CTAs can confuse. On contact pages, multiple CHANNELS are correct — different consumers prefer different channels:

- **Phone-preferential consumers** (often older, urgency-driven, conversation-preference) — phone primary
- **WhatsApp-preferential consumers** (often younger, mobile-dominant, low-friction-preference) — WhatsApp primary
- **Form-preferential consumers** (deliberation-driven, asynchronous-comfort, detail-oriented) — form primary
- **Email-preferential consumers** (formal-preference, audit-trail-need, detail-oriented) — email primary
- **Visit-preferential consumers** (touch-and-feel, decisive, local) — fysiek bezoek primair

A contact page that hides channels in favor of a "single CTA" is conversion-killer. The visitor's preferred channel may be the one you hid.

**Recommendation pattern:** show all relevant channels with clear hierarchy, but don't force one path.

---

## CRITICAL — Business-type calibration

Recommendations valid for one business-type are often wrong for another:

**Lokaal fysiek bedrijf** (kapsalon, restaurant, winkel, café, sportschool, garage, kliniek):
- Adres + route + parkeren + OV dominant
- "We zijn nu open"-status critical (real-time)
- Openingstijden prominent zichtbaar
- Telefoon vaak primair
- Multi-vestiging: zoeker bovenaan
- Google Maps embed essential

**Lokale service-provider** (tandarts, makelaar, fysio, advocaat, fotograaf, klusbedrijf):
- Adres + openingstijden + telefoon + form gelijkwaardig
- Vestigingen tellen
- Response-tijd belangrijk
- WhatsApp afhankelijk van doelgroep
- Google Maps embed nuttig

**Service-provider zonder fysieke ontmoeting** (online consultants, virtuele services):
- Adres minder relevant (alleen postcode of regio voor trust)
- Response-tijd EN kanaal-diversiteit dominant
- Geen kaart nodig (kan zelfs verwarrend zijn)
- Form vaak primair kanaal
- E-mail visibility belangrijk

**Multi-vestiging organisatie** (kapsalon-keten, tandartsketens, restaurant-keten):
- Vestigingen-zoeker dominant
- Dichtstbijzijnde vestiging-detectie waardevol (geolocation of postcode)
- Per-vestiging openingstijden, telefoon, route
- Algemene contact-info als fallback

---

## Core frameworks (apply across the entire audit)

### Nielsen Norman contact-page research
The leading authority on contact-page UX. Key principles:
- Recognition-over-recall: visitors should not have to remember what they need; show all channels visibly
- Visibility of system status: "we zijn nu open" status real-time
- Match between system and real world: openingstijden in local format (Ma t/m Vr)
- Heuristic #6 (recognition over recall) applies heavily: contact-info should be SEEN, not searched-for

### Baymard mobile and CTA research
- Tap-to-call phone numbers on mobile lift contact-conversion 15-30%
- Sticky bottom CTA on mobile is non-negotiable for long contact pages
- Embedded Google Maps mobile-friendly variants improve in-person-visit conversion
- Form-field reduction applies but less aggressive than lead-form context

### BrightLocal local-business research
For lokaal fysiek bedrijven and local-service providers:
- 87% of consumers research local businesses online before contact
- NAP (Name-Address-Phone) consistency between site and Google Business critical
- 78% of mobile local searches result in offline conversion within 24 hours
- "Nu open / gesloten"-status increases trust signals significantly

### Marketing Sherpa response-time-promise research
- Response-time commitment ("binnen 4 uur reactie") lifts form-completion 10-20%
- Lack of response-time creates anxiety (MECLABS anxiety-axis)
- Specific time-anchors outperform vague ones ("binnen 4 uur" beats "snel")

### MECLABS Conversion Sequence Heuristic on contact pages
C = 4m + 3v + 2(i−f) − 2a

On contact pages:
- **m (motivation):** already high (visitor chose contact-action)
- **v (value):** less important than other pages (already convinced)
- **i (incentive):** response-time clarity, channel-preference accommodation
- **f (friction):** missing tap-to-call, missing channels, unclear hours, long forms
- **a (anxiety):** "ben ik nu open?", "krijg ik een sales-call?", "wanneer reactie?", privacy

### Cialdini's principles on contact pages (calibrated lighter)
On contact pages, Cialdini-principles are reinforcement, not conviction:
- **Authority** — light touch (KvK, BIG-registratie, certifications already established elsewhere)
- **Social proof** — reviews as reassurance, not conviction
- **Reciprocity** — response-time promise as small reciprocity
- **Liking** — warm tone, friendly photos of staff if visible
- **Scarcity** — typically NOT applicable on contact pages

### Fogg Behavior Model (B = MAT) on contact pages
Visitor's MOTIVATION is high — they're on the contact page. The job is to:
- Maximize ABILITY (easy tap-to-call, easy form, easy WhatsApp)
- Make TRIGGER available across motivation-pieken (above-the-fold + sticky mobile)
- Remove ABILITY-blockers (broken links, hidden numbers, unmounted maps)

### Nielsen Norman heuristics applied to contact pages
- **#1 Visibility of system status** — "we zijn nu open / gesloten" status
- **#2 Match real world** — openingstijden in local format
- **#5 Error prevention** — inline form validation
- **#6 Recognition over recall** — all channels visible, no hidden info
- **#9 Help users recover from errors** — clear form-error messages

### Jobs-to-be-Done on B2C contact pages
B2C consumers on a contact page are doing ONE of:
1. **Direct contact-initiation** — "I want to reach them NOW" (urgency-driven)
2. **Bereikbaarheid checking** — "Are they open? Can they help me?" (verification)
3. **Lokatie/route lookup** — "Where are they? How do I get there?" (pre-visit)
4. **Kanaal-keuze** — "What's the best way to contact them?" (multi-channel exploration)
5. **Form-submission preparation** — "Let me ask my question via form" (asynchronous)

Each job needs different page support. A high-converting contact page serves multiple jobs without forcing one path.

**Important Dutch translation:** never use "huren" for JTBD framing. Use "kiezen voor", "consumenten die X willen".

---

## Category 1: Above-the-fold contact-clarity

### Nielsen Norman contact-page usability
Above-the-fold on contact pages should answer in 5 seconds:
- "How do I contact them?" — primary channel(s) visible
- "Are they available now?" — status indicator if applicable
- "Where are they?" — adres if applicable

### High-intent visitor patterns
Unlike service/dedicated LPs, the contact-page visitor is not skeptical — they've decided. Above-the-fold work is about REMOVING friction, not BUILDING conviction.

### Best practices
- Primary contact channel(s) visible in hero zone (phone, WhatsApp, form-anchor)
- "We zijn nu open" status if applicable
- Adres if fysiek bedrijf
- Response-time commitment near form
- Multi-vestiging zoeker if applicable

### Common failures
- Hero with brand-mission statement, not contact info
- Phone number below the fold
- No status indicator on fysiek bedrijf
- Form taking 100% of above-the-fold while phone is hidden
- Hero text-only with no channel-CTAs

### Business-type calibration
- Lokaal fysiek: adres + telefoon + openingstijden-status hero
- Service-provider: telefoon + form-anchor + response-time hero
- Multi-vestiging: vestigingen-zoeker hero
- Online-only service: form + response-time + email hero

---

## Category 2: Multi-channel CTA strategy

### Multi-channel conversion patterns
B2C consumers convert through different channels by preference:
- Phone: urgency-driven, conversation-preference, older demographics
- WhatsApp: low-friction-preference, younger demographics, mobile-dominant
- Email: formal-preference, audit-trail-need, detail-oriented
- Form: deliberation-driven, asynchronous-comfortable
- Chat: question-driven, browse-mode, immediate-response expectation
- In-person visit: touch-and-feel, decisive, local

### Fogg Behavior Model — multiple triggers
Multiple channel-CTAs catch different motivation-states. Visitor with phone-preference and visitor with WhatsApp-preference need different triggers.

### Best practices
- All relevant channels visible (phone, email, WhatsApp, form, chat, visit)
- Clear hierarchy: primary > secondary > tertiary
- Channel-specific microcopy ("Bel ons direct" / "WhatsApp ons" / "Stuur bericht")
- Mobile: tap-to-call live, WhatsApp click-to-chat live
- Channels matched to brand demographic (WhatsApp for younger; phone for older)

### Common failures
- Single-CTA dogma (form-only, hiding phone/WhatsApp)
- All channels equal weight without hierarchy
- Phone visible but not tappable on mobile
- WhatsApp absent despite mobile-dominant audience
- Email-only contact (too high-friction for most consumers)

### Business-type calibration
- Lokaal fysiek: phone primair, visit secundair, WhatsApp tertiair, form fallback
- Service-provider mid-ticket: phone + form balanced, WhatsApp + email secundair
- Service-provider high-ticket: phone + form balanced, email secundair, WhatsApp NEE als professional/legal context
- Online-only: form primair, email secundair, chat indien capaciteit

---

## Category 3: Telefonische bereikbaarheid & response-belofte

### Baymard tap-to-call research
On mobile contact pages, tap-to-call lifts phone-conversion 15-30%. The phone number must be:
- Clickable as `tel:` link on mobile
- Large enough for thumb (Hoober thumb-zone)
- Visually distinct from surrounding text

### Response-time-promise research (Marketing Sherpa)
- "Binnen 4 uur reactie" lifts form-completion 10-20% vs no time-anchor
- "Binnen 1 werkdag" outperforms "snel" or "z.s.m."
- "We bellen je binnen 30 minuten terug" creates strong reciprocity-pull

### Best practices
- Phone number prominent (hero or directly below)
- Phone number ALWAYS tap-to-call on mobile
- Response-time promise specific ("Telefonisch direct bereikbaar Ma-Vr 9-17 uur" / "We bellen binnen 4 uur terug")
- Voicemail-belofte expliciet ("Inspreken? We bellen binnen 24u terug")
- Alternative number voor noodgevallen if applicable

### Common failures
- Phone visible but plain text on mobile
- No response-time commitment
- Vague "snel beschikbaar" without time-anchor
- Phone hidden in footer only
- Single phone number for multi-vestiging without context

### Business-type calibration
- Lokaal fysiek: phone hoofdkanaal, openingstijden prominent
- Service-provider: phone + form, response-time commitment beide
- Online-only: phone optioneel, soms alleen geplande call

---

## Category 4: WhatsApp & messaging kanalen

### Consumer-messaging-preference research
- 78% of NL/BE consumers prefer WhatsApp over phone for low-stakes contact (2023 data)
- WhatsApp click-to-chat lifts mobile contact-conversion 2-3x over phone-click for younger audiences
- WhatsApp Business with "we reageren binnen X" automation outperforms plain WhatsApp links

### Low-friction conversion patterns
WhatsApp specifically wins because:
- No commitment of voice call
- Async (visitor sets pace)
- Familiar UI (WhatsApp app native)
- Conversation history preserved
- File-sharing easy (foto van probleem, document)

### Best practices
- WhatsApp Business met click-to-chat URL (`wa.me/31...`)
- WhatsApp icoon + tekst CTA ("WhatsApp ons direct")
- Voorbeeld-bericht-tekst pre-filled waar relevant
- Mobiel: directe app-deep-link
- Desktop: WhatsApp Web fallback
- Response-time-promise specifiek voor WhatsApp ("we reageren binnen 1 uur op werkdagen")

### Common failures
- WhatsApp ontbreekt despite mobile-dominant audience
- WhatsApp icoon zonder click-functionaliteit
- Geen pre-filled bericht (visitor moet alles zelf typen)
- Geen response-time-belofte op WhatsApp specifiek
- WhatsApp-knop op een non-mobile-friendly position

### Business-type calibration
- Lokaal fysiek + jong publiek: WhatsApp primair na phone
- Lokaal fysiek + ouder publiek: WhatsApp tertiair
- Service-provider mid-ticket: WhatsApp gelijkwaardig aan phone afhankelijk van doelgroep
- Service-provider high-ticket (juridisch, financieel): WhatsApp vaak ongepast (formaliteit)
- Online-only: WhatsApp afhankelijk van service-aard

### Capaciteit-acceptatie
Aanbevelen om WhatsApp toe te voegen vereist response-capaciteit. Onbeantwoorde WhatsApps ondergraven vertrouwen meer dan WhatsApp-afwezigheid.

---

## Category 5: Lokatie, route, parkeren, OV

### BrightLocal local-business research
For lokaal fysiek bedrijven, location-related content is dominant:
- 78% of mobile local searches result in offline conversion within 24 hours
- Visitors check route/parkeren/OV BEFORE deciding to visit
- Missing or incorrect info on these elements is direct conversion-killer

### Physical-visit conversion drivers
- Embedded Google Maps (zichtbare locatie)
- Adres met format dat lokaal werkt (NL: "Hoofdstraat 12, 1234 AB Amsterdam")
- Route-link naar Google Maps / Apple Maps (one-click directions)
- Parkeer-info specifiek ("Gratis parkeren voor de deur" / "Betaald parkeren P+R")
- OV-info specifiek ("3 min lopen vanaf station Centraal")
- Toegankelijkheid-info (rolstoel, lift) waar relevant

### Best practices
- Embedded Google Maps op locatie van bedrijf
- Adres in NAP-format (Name-Address-Phone) consistent met Google Business
- "Route plannen"-knop met deep-link naar Maps-app
- Parkeer-info concreet
- OV-info concreet
- Optioneel: foto van gevel / entree (vindbaarheid)

### Common failures
- Geen embedded map (alleen adres)
- Adres in inconsistent format met Google Business (NAP-inconsistentie)
- Geen route-knop (visitor moet copy-paste adres)
- Geen parkeer-info ("ja maar elke buurman weet het")
- Geen OV-info despite urban location
- Multi-vestiging zonder duidelijke locatie-zoeker

### Business-type calibration
- Lokaal fysiek: alles bovenstaand dominant
- Service-provider mid-ticket met spreekuur: adres + route + parkeren
- Service-provider zonder fysieke ontmoeting: adres optioneel (alleen voor trust), GEEN map
- Multi-vestiging: locatie-zoeker primair, per-vestiging details secundair

---

## Category 6: Openingstijden & beschikbaarheid

### Nielsen Norman recognition-over-recall (heuristic #6)
Openingstijden moeten ZICHTBAAR zijn, niet doorgaans-bekend-verondersteld. Bezoekers willen weten:
- "Are they open NOW?"
- "When can I visit / call?"
- "What about holidays?"

### Real-time-status patterns
Google Business toont "Open / Closes at X / Closed / Opens at Y" — zelfde patroon werkt op contact pages:
- **Real-time status widget:** "We zijn nu open · sluit om 17:30"
- **Tijden-tabel:** weekoverzicht met huidige dag gehighlight
- **Uitzonderingen:** feestdagen, vakanties expliciet

### Google Business hours-display research
Inconsistentie tussen Google Business hours en site-hours veroorzaakt:
- Verwarring (bezoeker komt op gesloten tijd)
- Trust-loss (bedrijf lijkt niet professioneel)
- Direct conversion-loss

### Best practices
- "We zijn nu open / gesloten"-status real-time (boven of in de buurt van openingstijden)
- Volledige weekoverzicht met huidige dag gehighlight
- Uitzonderingen specifiek (feestdagen, vakanties, gewijzigde tijden)
- Consistentie met Google Business
- Voor telefoon: aparte telefonische bereikbaarheid indien anders dan winkel/praktijk-tijden

### Common failures
- Openingstijden in footer-tekst zonder visuele structuur
- Geen real-time status (bezoeker moet zelf rekenen)
- Inconsistentie met Google Business
- Uitzonderingen ontbreken (feestdagen, vakanties)
- "Op afspraak"-tijden zonder context (wanneer is afspraak mogelijk?)
- Multi-vestiging met algemene tijden zonder per-vestiging variatie

### Business-type calibration
- Lokaal fysiek: openingstijden hero-zichtbaar of direct daaronder, status real-time
- Service-provider met spreekuur: telefonische bereikbaarheid + afspraak-tijden duidelijk gescheiden
- Service-provider 24/7 (digital): "Reactie binnen X uur" in plaats van openingstijden
- Multi-vestiging: per vestiging eigen tijden

---

## Category 7: Contact-form design & field optimization

### Baymard form-field research
Contact-form vs lead-form distinction:
- **Lead-form:** vraagt offerte/aanvraag, 5-7 velden acceptabel, kwalificatie belangrijk
- **Contact-form:** open bericht-form, 3-5 velden max, asynchrone vraag-functie

### CXL form-friction research
Op contact-form geldt nog harder dat elk veld friction toevoegt. Contact-form is geen kwalificatie-tool — het is een bericht-doorgeefluik.

### Standard contact-form best practice
Minimaal velden-set voor contact-form:
1. Naam (verplicht)
2. E-mail of telefoonnummer (verplicht, met keuze)
3. Onderwerp / type vraag (dropdown, optioneel)
4. Bericht (textarea, verplicht)

Extra velden alleen als compliance vereist (AVG-checkbox) of als specifieke routing essentieel is.

### Best practices
- 3-5 velden max
- Labels boven velden
- Required-only marking (markeer optioneel, niet verplicht)
- Real-time validation
- Mobile-optimized keyboards
- Single-column op mobile
- AVG-checkbox compact en duidelijk
- Submit-CTA actie-gericht ("Stuur bericht" beats "Verzenden")
- Privacy-microcopy bij submit ("We gebruiken je gegevens alleen voor antwoord op deze vraag")

### Common failures
- 8+ velden op contact-form (verkeerd page-type)
- Multi-step form op simpel contact-form (overengineered)
- Placeholder-only labels
- Verplicht-asterisken op elk veld
- "Welk product?" dropdown op een non-ecom contact-page
- AVG-checkbox in juridisch-jargon zonder uitleg
- Generieke "Verzenden" submit-CTA

### Business-type calibration
- Lokaal fysiek: contact-form als fallback, kort (3-4 velden)
- Service-provider: contact-form gelijkwaardig aan phone, 4-5 velden acceptable
- Online-only: contact-form vaak primair, 4-6 velden acceptable
- Multi-vestiging: optioneel veld "voor welke vestiging?"

---

## Category 8: Trust signals & credibility (lichter dan andere LPs)

### Lighter calibration than service/dedicated LP
De contact-page bezoeker is al overtuigd. Trust signals zijn:
- **Reinforcement** (bevestig wat ze al geloven)
- NIET **conviction** (overtuig ze opnieuw)

### Acceptable trust signals on contact pages
- KvK-nummer (Nederlandse context, verplicht voor commerciële sites)
- BTW-nummer (waar relevant)
- BIG-registratie (zorgverleners)
- Branche-certificeringen kort vermeld
- AVG-compliance microcopy bij form
- Privacybeleid-link

### What NOT to add
- Lange testimonial-secties (verkeerd page-type)
- Case studies (verkeerd page-type)
- Award-walls (overkill)
- Pers-logos (overkill)
- Klant-logo-grids (overkill)

### Best practices
- Footer-strip met KvK + BTW + privacy-link
- AVG-microcopy bij form
- Eventueel: 1-2 line "10+ jaar ervaring" of "8.000+ klanten" als rustige reinforcement
- Branche-certificering klein zichtbaar

### Common failures
- Geen KvK / BTW (vereist voor NL commerciële sites)
- Geen privacy-link bij form
- Te zware trust-walls (hoort op homepage of about, niet contact)
- Generic trust-zonder-context ("jarenlange ervaring")

---

## Category 9: Reviews & ratings (independent category, lichter gewicht)

### Spiegel Research Center on reviews (baseline-context)
- Producten/diensten met zichtbare reviews converteren tot 270% beter
- Op contact-pages is dit effect MINDER sterk dan op service/dedicated LPs
- Maar: voor first-time visitors die direct landen op contact-page (search "kapsalon contact"), kan reviews-zichtbaarheid wel impact hebben

### BrightLocal local-service research
Voor lokaal fysiek bedrijven specifiek:
- 87% van consumenten leest reviews voor lokale bedrijven
- Sommige consumers landen direct op contact-page via Google Business / branded search
- Voor deze subgroep: reviews zichtbaar op contact-page = reinforcement

### Reinforcement-not-conviction role
Op contact-page reviews dienen als:
- Bevestiging dat keuze juist was ("ik twijfelde nog, maar zie deze rating")
- Last-minute trust-boost vóór contact-actie
- NIET als overtuigingsmiddel

### Best practices
- Klein review-element (rating + count) bij contact-zone
- Embedded Google review-widget compact (niet full-section zoals op homepage)
- Geen full review-feed (overkill voor page-type)
- Multi-vestiging: per-vestiging rating als mogelijk

### Common failures
- Volledige review-sectie op contact-page (verkeerd page-type)
- Geen reviews terwijl Google Business 4.8 toont (gemist signaal)
- Generic "Onze klanten zijn tevreden" zonder bron
- 5/5 perfect rating (skepticism-trigger)

### Calibration logic
- Lokaal fysiek met sterke Google reviews: klein widget bij contact-zone, ICE doorgaans 5-7
- Service-provider: optioneel klein widget, ICE doorgaans 4-6
- Online-only zonder lokale-search-context: minimal of geen reviews op contact-page

### Authenticity restraint
A finding may recommend verifying review authenticity. A finding may NOT claim displayed reviews are fabricated without strong evidence.

---

## Category 10: FAQ & contact-specifieke objection handling

### MECLABS anxiety axis on contact pages
Contact-specifieke anxieties:
- "Krijg ik direct een sales-call?" (sales-call fear)
- "Hoe lang duurt het voor reactie?" (response-time uncertainty)
- "Word ik wel teruggebeld?" (commitment fear)
- "Wat doen ze met mijn gegevens?" (privacy anxiety)
- "Worden ze niet duur als ik bel?" (cost fear voor sommige services)

### Pre-emptive objection handling
Op contact-pages werken FAQ's en microcopy heel anders dan op service/dedicated LPs:
- Microcopy direct bij form/CTA ("We bellen alleen na jouw verzoek")
- Korte FAQ-strip met top 3-5 contact-vragen
- Privacy-reassurance compact

### Best practices
- Microcopy bij form: "We gebruiken je gegevens alleen voor antwoord op deze vraag"
- Korte FAQ: "Wat gebeurt er na ik dit invul?" / "Hoe lang duurt het voor reactie?" / "Krijg ik een sales-call?"
- Response-time-commitment expliciet
- Eventuele kosten-clarity (voor services waar bellen kan kosten of premium nummers worden gebruikt)

### Common failures
- Geen microcopy bij form (anxiety blijft)
- Geen response-time-commitment
- Generic FAQ (algemene service-vragen i.p.v. contact-specifieke)
- Geen privacy-reassurance bij form

---

## Category 11: Mobile experience

### Baymard mobile commerce research
B2C contact-pages zijn mobile-dominant:
- 65-85% van contact-page traffic is mobile
- Mobile conversie op contact-pages is doorgaans HOGER dan desktop (tap-to-call factor)
- Sticky bottom CTA op mobiel verhoogt phone-conversie 15-30%

### Google mobile-first indexing
Mobile experience drijft ranking AND conversie. Mobile audit is core.

### Thumb-zone usability (Hoober)
Mobile tap-targets in thumb-bereik:
- Sticky CTA bottom (primair thumb-zone)
- Phone number prominent in hero
- WhatsApp button prominent

### Mobile contact-page patterns
- **Sticky bottom action bar:** "Bel | WhatsApp | Route" (drie iconen + label)
- **Tap-to-call dominant:** elk telefoonnummer als `tel:` link
- **WhatsApp click-to-chat:** native deep-link naar app
- **Map mobile-optimized:** lightweight Maps embed of statische kaart met "Route plannen"-knop
- **Form mobile-optimized:** single column, large fields, mobile keyboards

### Best practices
- Sticky bottom CTA bar op mobile met meest relevante kanalen
- Alle phone numbers tap-to-call
- WhatsApp click-to-chat live
- Map mobile-optimized (geen heavy desktop-iframe)
- Form mobile-optimized (single column, mobile keyboards)
- Geen scroll-blocking elementen (chat-overlay die CTA bedekt)

### Common failures
- Geen sticky mobile CTA
- Phone zichtbaar maar plain text
- WhatsApp afwezig despite mobile-dominant audience
- Heavy Google Maps embed slows page load
- Form desktop-ported (multi-column, kleine velden)
- Chat-overlay blokkeert primaire CTA

---

## Brand calibration notes

Always recalibrate by brand snapshot AND business-type:

**Example: Hero CTA**
- Lokaal kapsalon: phone + adres + openingstijden status hero
- Tandartspraktijk: phone + afspraak-form + openingstijden hero
- Online financieel adviseur: form + email + response-time hero
- Restaurant-keten: vestigingen-zoeker + reservering-CTA hero

**Example: WhatsApp emphasis**
- Kapsalon met jonge doelgroep (18-35): WhatsApp primair na phone
- Advocatenkantoor: WhatsApp NEE (formaliteit)
- Klusbedrijf: WhatsApp dominant (visuele info-deling, foto van probleem)

**Example: Map prominence**
- Lokaal fysiek: embedded map prominent
- Service-provider met spreekuur: map nuttig maar secundair
- Online-only: geen map (kan verwarrend zijn)

Recommendations that don't match brand AND business-type zijn fout.

---

## Test-readiness check

Before finalizing each finding:
- [ ] Diagnosis cites a specific principle, study, or source
- [ ] Recommendation is concrete (exact copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z"
- [ ] Primary metric is named (contact-conversion rate / phone-click / form-completion / WhatsApp-click)
- [ ] ICE justified by I/C/E breakdown
- [ ] Recommendation matches brand snapshot AND business-type
- [ ] High-intent visitor logic respected (no automatic "add conviction" recommendations)
- [ ] Multi-channel parallel logic respected (no automatic "consolidate" recommendations)
- [ ] Reviews findings calibrated lighter (reinforcement, not conviction)
- [ ] Dutch output: no "huren" check
- [ ] No authenticity claims about phone/hours/email functionality

If any box unchecked, rework or remove the finding before delivering.
