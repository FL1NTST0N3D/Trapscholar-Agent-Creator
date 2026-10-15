# Cannabis-Breeding – Wissensreferenz kompakt (Stand 2026-10-15)

Lade-Referenz fuer den Breeding-Agenten. Jede Sektion nennt ihre Quellen (Repo-Pfad unter `scratchpad/crawl/repos_breeding/`, Peer-Review-Zitat in Klammern; (S) = Sekundaerbeleg ueber Repo-Fussnote, nicht live verifiziert). Zahlen ohne Quelle gibt es hier nicht. Rechtlicher Rahmen: KCanG (Erwachsene, § 9 max. 3 Pflanzen gleichzeitig, § 10 Vermehrungsmaterial sichern, § 4 Abs. 2 Samen nur aus EU) – `legalize-dev__legalize-de/de/KCANG.md`.

## 1. Genetik-Grundlagen Cannabis

- Art: *Cannabis sativa* L., Cannabaceae (mit Hopfen). Einjaehrig, **dioezisch** (meist getrennte Geschlechter), **windbestaeubt**, Bluete durch **Nachtlaenge** (Kurztagpflanze). (plant-biology.md, Small 2015; McPartland 2018) (S)
- Chromosomen: **2n = 20** = 9 Autosomenpaare + **XY** (Maennchen XY, Weibchen XX). (plant-biology.md, Divashuk 2014) (S)
- Genom ca. 818 Mb; Referenz **cs10 / CBDRx** (NCBI GCF_900626175.2, Grassa 2021); Chromosomen seit 2020 neu nummeriert – alte Daten (z. B. MylesLab-PLINK) muessen umkodiert werden. (Reviews-Maker §3; MylesLab README)
- Cannabinoid-Synthase-Gene (THCAS/CBDAS/CBCAS) liegen geclustert am **B-Locus** (Chr. 6 nach alter Zaehlung, Laverty 2019); daher einfache mendelsche Vererbung des Chemotyps, waehrend Morphologie ("Indica/Sativa") polygen ist und schnell verduennt. (Reviews-Maker §3) (S)
- Terpenprofil wird ueberwiegend durch Terpen-Synthase-Gene bestimmt; Mono-TPS-Cluster Chr. 5, Sesqui-TPS Chr. 6; Label-Chemie korreliert mit TPS-Varianten. (MylesLab/cannabis-labelling; Booth 2019 via cannabinoids-terpenes.md) (S)
- Begriffe: **Genotyp** = DNA (fix ab Samen, in jeder Zelle gleich); **Phaenotyp** = Genotyp × Umwelt (sichtbar/messbar); **Chemotyp** = Synthase-Allele → Cannabinoid-Verhaeltnis; keine Umweltaenderung macht aus THC CBD. CBN ist Lagerprodukt, kein Zuchtmerkmal. (genetics-phenohunting.md; cannabinoids-terpenes.md Z. 95)
- "Sativa/Indica"-Etiketten: > 35 % der kommerziellen "Sativas" genetisch von Indica-Linien nicht unterscheidbar (Sawler 2015, 81 Individuen, 13 SSR); gleicher Name ≠ gleiche Genetik (Schwabe & McGlaughlin 2019). → Chemotyp/Genotyp vor Name. (Reviews-Maker §3; genetics-phenohunting.md) (S)
- Quantitative Genetik (Pflanzenzuechter-Denkrahmen): Selektionsantwort **R = h² · S**; genetischer Gewinn = Selektionsintensitaet × Genauigkeit × additive Varianz / Generationszeit; niedrig-heritable Merkmale (Ertrag) brauchen Wiederholung, hoch-heritable (Chemotyp, viele Qualitaetsmerkmale) erlauben fruehes Cullen; Indexselektion statt unabhaengiger Cull-Schwellen bei Zielkonflikten; G×E kann Rangfolgen umkehren → unter Zielbedingungen testen. (K-Dense-AI__scientific-agents/.../plant-breeder/SKILL.md; zankrut20/selection.index)

## 2. Chemotyp-Allele (B-Locus) und Vererbung

| Typ | Definition | Genotyp (B-Locus) |
|---|---|---|
| I | THC-dominant (CBD < 0,5 %) | B_T/B_T |
| II | THC ≈ CBD | B_T/B_D (kodominant) |
| III | CBD-dominant (THC < 0,3 %) | B_D/B_D |
| IV | CBG-dominant | nachgeschaltete Synthasen defekt, CBGA staut sich |
| V | cannabinoidfrei | rezessiv o/o (Pathway blockiert) |

- **Kreuzung I × III → F1 alle Typ II; F2 spaltet 1 : 2 : 1 (I : II : III).** Kodominanz: Heterozygote zeigen beide Enzyme. (de Meijer 2003 Genetics 163:335; cannabinoids-terpenes.md Z. 159, 382) (S)
- Typ V: ein rezessives Allel (o) stoppt den Pathway voellig; Kreuzungen wieder 1 : 2 : 1. (de Meijer 2009 Euphytica 168:95) (S)
- **Locus steuert das Verhaeltnis, nicht die Menge**: Gesamtgehalt = viele Gene + Umwelt (Licht, Reife, Kronendach). Zucht/Saatgut bestimmt Ratio, Kultur bestimmt Menge. (cannabinoids-terpenes.md Z. 163; Small 1979 via Farming-KB) (S)
- "CBD-Sorte" mit hohem THC = Typ II – der Locus erklaert es, nicht der Grower. (cannabinoids-terpenes.md Z. 300)
- **Chemotyp vor Bluete bestimmbar**: Blattprobe (Labor) oder DNA-Marker THCAS/CBDAS (Toth 2020). Nutzen: THC-/CBD-Arbeit frueh trennen, Bankplatz sparen. Marker sagt **nicht** THC-%, Terpene oder Ertrag voraus. (genetics-phenohunting.md Tabelle Gentests) (S)
- Maennchen zeigen dieselben Cannabinoid-Verhaeltnisse wie Weibchen, nur in geringerer Menge → Chemotyp-Marker/Analytik auch am Pollenelter einsetzen; ohne Analytik ist Selektion auf Cannabinoide "subjektives Raten". (Farming-KB cannabis-chemotype-classification-cannabinoid-breeding.md, Clarke/Small)
- THC-Gesamt auf COAs: THC_total = THC + 0,877 × THCA (Decarboxylierungs-Massenverlust). Datenschema soll `thcSource = breeder_claim | lab_tested` fuehren. (Reviews-Maker §2)

## 3. Geschlecht, Autoflower, weitere Einzelgene

- Vorblueten: Maennchen ~3–4 Wochen nach Keimung (1–2 Wochen vor Weibchen), Node 4–6, Lupe 60×; maennlich = eifoermig am Stielchen, weiblich = Tropfen mit weissem Pistill; nach Bestaetigung **7–10 Tage bis zur ersten Pollenfreisetzung** → sofort isolieren. (akravetz__dirt/wiki/breeding/male-evaluation.md)
- Photoperiod-Pflanzen zeigen Vorblueten Woche 4–6 Veg; PCR-Geschlechtsmarker im Keimlingsstadium (Toth 2020). (genetics-phenohunting.md Schritt 3) (S)
- **Autoflower1 = rezessiver Haupt-Locus** (+ Early1 fuer Fruehbluete). Auto × Photo → F1 alle photoperiodisch (Traeger); Auto erscheint erst in F2 (¼) oder nach Rueckkreuzung auf Auto. Autos: kleiner, nicht als Mutter haltbar, kein Umtopf-Stress. (Toth 2022 Front Plant Sci 13:991680; genetics-phenohunting.md; Farming-KB autoflowering-breeding.md) (S)
- Hermaphroditismus/Intersex ist erblich und wird durch Stress-Selbstung (Rodelization) in Linien angereichert; Nachkommen von stressinduzierten Bananen erben die Neigung. (Punja & Holmes 2020; genetics-phenohunting.md) (S)
- Polyploidie: Tetraploide (Colchicin/Oryzalin) × Diploide → sterile Triploide (samenlos); Zuchtwerkzeug, kein Standard. (Medcan-Agent advanced_breeding.md)

## 4. Feminisierung (STS/kolloidales Silber) – publizierte Grundlagen

- Mechanismus: **Silberionen blockieren Ethylen-Rezeptoren**; Ethylen haelt die Pflanze weiblich → ohne Signal bildet ein XX-Weibchen fertile maennliche Blueten; Pollen traegt nur X → Nachkommen XX. Keine DNA-Veraenderung, hormonell/epigenetisch, zeitlich begrenzt. (Mohan Ram & Sett 1982 TAG 62:369; genetics-phenohunting.md; Reviews-Maker §4) (S)
- Protokoll (publiziert, Hanf/Cannabis): **STS-Blattspray in niedriger Konzentration, wenige Anwendungen um den 12/12-Flip**, Pollen einige Wochen spaeter; Lubell & Brand 2018 (HortTechnology 28:743), Flajsman 2021 (Front Plant Sci 12:718092: fem. Saatgut praktisch 100 % weiblich), 2024 "Optimized guidelines for feminized seed production in high-THC cultivars" (Front Plant Sci 15:1384286). Konkrete mM-Werte/Spruehintervalle **in den Originalen nachschlagen** – in diesem Crawl nicht live lesbar; Community-Rezepte (AgNO3 + Na-Thiosulfat-Stammloesung, 1:9 verduennt) sind nicht peer-reviewed. (S)
- Praxisregeln (dirt/feminized-production.md): Reversion **in Isolation**; behandelte Pflanze **nicht konsumieren**; Pollen getrennt sammeln/trocknen/aliquotieren; Seed-Mutter und Reversions-Donor = zwei elite Klone derselben gepruften Familie (oder derselbe Klon fuer S1); kein dauerhafter "Vater" noetig.
- **Feminisiertes Saatgut ist nicht schwaecher**; Hermie-Risiko kommt aus der Elternwahl. Frage an Breeder: STS auf stabiler Mutter oder Rodelization? (genetics-phenohunting.md) (S)
- S1 (Selbstung ueber Reversion) ≈ 99 % weiblich, "viele Merkmale der Mutter, aber **keine Kopie**" – jeder heterozygote Locus spaltet. S1 eines Elite-Cuts = verwandte Population. (genetics-phenohunting.md)
- Saatguttypen-Tabelle: regular ~50/50, geringe Uniformitaet, einzige Quelle fuer Maennchen; feminisiert ≥ 99 % ♀, low–moderate Uniformitaet; auto regular/fem; S1 moderate; clone-only = exakte Kopie, Krankheit reist mit. (genetics-phenohunting.md)

## 5. Selektion / Pheno-Hunt

1. **Samenzahl vorab festlegen**; Scoring-Tabelle (Kriterien, Gewichte, Cull-Schwellen) **vor der Keimung** schreiben (Halo-Effekt). (genetics-phenohunting.md Schritt 1 + TIP)
2. Alle Samen gleichzeitig keimen, **permanente ID = Packungscode + Samen-Nr.** am ersten echten Blattpaar; ID wandert bei jedem Umtopfen mit. (Schritt 2)
3. Geschlecht so frueh wie moeglich; Maennchen raus, bevor ein Sack oeffnet (ausser Zucht). (Schritt 3)
4. Gleiche Toepfe/Medium/Feed/Topping fuer alle; Veg-Vigor und Bewurzelungszeit loggen, aber **nicht** danach selektieren. (Schritt 4)
5. **2–3 bewurzelte Backup-Stecklinge je Pflanze VOR dem 12/12-Flip** – ohne Steckling ist die Pflanze nicht im Hunt. (Schritt 5; dirt/pheno-hunt-protocol.md)
6. Ein Raum, gleicher Flip-Tag, **woechentliche Positionsrotation** (Rand/Hotspot-Effekte mitteln). (Schritt 6)
7. Woechentlich Zahlen: Stretch, Struktur, Bluetebeginn, Pest/Schimmel, Aromawandel; **nie in Woche 3 selektieren**. (Schritt 7)
8. Je Pflanze: Trockengewicht, getrennt trocknen/curen, wenn moeglich Labor, Wasch-/Presstest fuer Hash. (Schritt 8)
9. **Runde 2**: beste 2–3 als Klone gemeinsam nachbauen; Keeper = Pflanze, die als Klon **wieder** liefert. "One crop is a test, two crops make a cultivar." (Schritt 9)

Kriterien-Set (Methode): Potenz/Chemotyp (Labor je Pflanze) · Terpene (riechen ab W6, nach Cure im Glas, Labor) · Ertrag (Trockengewicht bei gleichem Abstand) · Struktur (Internodien, Astwinkel, Selbsttragend, Larf-Anteil) · Bluetezeit (Tage Flip → Trichomreife) · Schimmel/Pest-Log · Trichomertrag (Waschtest) · Bewurzelungsrate/-tage der Backups · Stretch (Hoehe Peak / Hoehe Flip; Tag 21). (genetics-phenohunting.md Tabelle)
Gewichtungsbeispiel (Prime Cuts, 1–10 je Kategorie): Commercial/Personal – Ertrag 25/10 %, Bag Appeal 20/15, Terpene 15/30, Potenz 10/25, Anbau-Schwierigkeit 15/5, Finish-Zeit 15/15. Fehler: zu frueh, nur Ertrag, zu wenige Samen (min. 10, besser 20–50), Stabilitaet ignorieren, zu viele behalten. (cannabis-cultivation-resources/phenotype-selection-guide.md)
Stichprobe: Keeper (alle Mindestschwellen) ~1/20 → **10 Samen ≈ 40 %, 50 Samen > 90 % Chance**; bei regular N halbieren; "best of N" dokumentieren, N kennen. Kommerzielle Hunts: Hunderte–Tausende Samen, 1–2 Keeper. (genetics-phenohunting.md "Limits of the sample size")
Gate-basiert zuerst (dirt): Pflanzen ohne Zielsignal (z. B. kein frueher Anthocyan, Hermie, unsichere Labels) fliegen **vor** dem Scoring raus; Farbe an Kelchen scoren (W3/6/9 fotografieren), nicht nur Blatt. (pheno-hunt-protocol.md)
Maennchen-Score (2–4 Wochen zwischen Sexing und Sackschwellung): Stamm-/Petiolenfarbe, Vigor (Tage bis Vorbluete, Nodien/Woche, Stammdicke), Struktur, Blattform, **Stem-Rub-Aroma**, Sackdichte, **Hermie = Cull**. (male-evaluation.md)

## 6. Pollen- und Saatgut-Handling

Pollen (dirt/pollen-handling.md, Praxis; Clarke via Farming-KB):
- Sammeln bei **~33 % aufgeplatzten Saecken**, **3 Sessions im Abstand 2–3 Tage**, mittags bei **RH < 50 %**, Tuer zu, Luefter aus; Maske/Handschuhe; Pergament je Maennchen je Session; geschwollene, ungeoeffnete Saecke mit Pinzette abnehmen, 24 h nachreifen lassen. Clarke: frueh morgens vor Hitze, Werkzeuge zwischen Quellen reinigen, feucht = keimt/verdirbt.
- Ertrag: 0,5–2 g je kleinem Maennchen/Woche; 0,1–0,2 g genuegen fuer eine Kreuzung. **Lots nie mischen** (nur bei bewusst gemischtem Vaterlos).
- Trocknen 24–48 h bei RT mit Reis/Silica; **mit Mehl 4:1 strecken**, Einmal-Aliquots, vakuumieren.
- Haltbarkeit: offen 1–2 Wo · dicht RT 2–4 Wo · Kuehlschrank 4 °C + Trockenmittel 3–6 Mon · **Gefrierer −18 °C 18–24 Mon** · LN2 8+ J. Aliquot ~30–60 min vor Gebrauch auftauen, Rest verwerfen, nie wieder einfrieren.
- Dokumentation je Lot: Maennchen-ID (z. B. `TA-M1`), Herkunftspopulation, Sexing-Datum, Flip-Datum, erste Sackschwellung, Session/Datum, Score-Kurzfassung – gleiche ID auf Tag, Papier, Tube, Box, Kreuzungsbuch.

Bestaeubung (dirt/cross-procedure.md):
- Fenster: Stigmen **frisch, weiss, klebrig = Woche 2–3 (Tag 14–18 nach Flip)**; ab Woche 4 sinkende Rezeptivitaet, nach Woche 5 gering.
- **1–2 untere Aeste** (100–500 Samen/Ast; ~50 reichen fuer einen Hunt), Etikett sofort (Eltern × Datum × Position), optional 24 h Papier-/Organzabeutel; Pinsel #2 trocken; danach Rest der Pflanze und Handschuhe **mit Wasser nebeln** (denaturiert Pollen); Kleidung wechseln/duschen vor Rueckkehr zum Haupttent.
- Reziproke Kreuzungen getrennt fuehren (Mutter-Effekte, Samenvigor). (stabilization-strategy.md)

Saatgut (seeds-germination.md; s4ag-seeds):
- Reif = hart, dunkelbraun, Tigerstreifen; blass/gruen = unreif, schlechte Keimung. Lagern **kuehl, dunkel, trocken, dicht im Kuehlschrank**; jahrelang viabel, Keimrate sinkt mit Alter (Lipidoxidation; Cockson 2025) (S). Frische fem. Samen > 90 % Keimrate; 1–2 Ausfaelle normal; 1–2 Reserve keimen.
- Lot-Daten: Eltern, Methode (regular/STS-fem/S1/BX), Erntedatum, Anzahl, Keimtest (n, Datum, %), Lagerort.

## 7. Stabilisierungsplan F1 → F5 / IBL

Nomenklatur (dirt/nomenclature.md; Reviews-Maker §1): P = Elternlinien · F1 = P × P (uniform-ish, Heterosis) · F2 = F1 × F1 (**maximale Aufspaltung – hier jagen**) · F3+ = Geschwister-/Familienkreuzungen (Varianz sinkt bei konsequenter Selektion) · **BX** = Rueckkreuzung auf einen Elter · **S1** = Selbstung · **IBL** = 4–6+ Generationen Selbstung/Sibcross, "reproduziert wahr" · "feminisiert" ist **keine Generationsbezeichnung**. Generationszaehlung des Breeders fortsetzen (unsere erste Kreuzung aus F1-Samen ergibt **F2**).

Plan (dirt/family-selection.md, stabilization-strategy.md; Clarke):
1. **F1 → F2**: regulaere Maennchen nutzen (exponieren Variation). Beste F2-Familien aus bekannten Paaren (`TA-M1 × A → F2-A`, `TA-M1 × D → F2-D`), Test z. B. 8 + 8 Samen; Familie mit hoechster Trefferquote (z. B. 5/8 on-target, 0 Hermies) weiter.
2. **F2 → F3**: in der Siegerfamilie 2–3 Maennchen × 2–3 Weibchen bewerten; **2×2 = 4 F3-Familien** als Standardmaximum; Screening 4 Samen/Familie, Sieger 8–16.
3. **F3 → F4 → F5**: Schleife "Gewinnerfamilie anbauen → beste Paare → 1–4 bekannte Subfamilien → testen → eine weiter (+1 Backup bei Platz)". Keine volle 4×4-Matrix mit 16 Plaetzen.
4. Regel: **Individuen nach Phaenotyp selektieren, Familien nach Nachkommenleistung advancen.** Ein schoener F2 ist Kandidat, kein Beweis.
5. Fixierung: nach **5–6 Generationen** sind die meisten Merkmale fixiert (Clarke, Farming-KB); dabei unerwuenschte rezessive Allele konsequent entfernen, Inzuchtdepression (Fertilitaet/Vigor) beobachten, Populationsgroesse nicht zu klein (K-Dense; s4ag-seeds/Deppe).
6. **Produktionsendpunkt feminisiert**: erst wenn eine Familie wiederholt die Gates besteht (≈ F4/F5): Seed-Mutter-Klon × reversierter Donor-Klon → Progeny-Test. Schwellen: **< 70 % on-target = nicht stabil; 70–90 % = Selektionsmaterial; > 90 % on-target ♀, einmal wiederholt = Produktionslos.** Nenner loggen (gekeimt, gecullt + Grund, geblueht, on-target, Hermie/Intersex, off-target). (feminized-production.md)
7. Simulation vor dem Grow (jbancic_alphasimr_plants, meiosim): Samen je Generation fuer p(Ziel) bei 2–3 Zielloci; 1 : 2 : 1 je kodominantem Locus, 3 : 1 je dominant/rezessiv (Mendel; Clarke "Mendelian breeding system": 2 reine Linien → F1 → F2 → klassifizieren → statistisch pruefen).

## 8. Rueckkreuzungsplan (BX)

- Zweck: ein **einfach vererbtes, leicht bonitierbares** Merkmal (Schimmel-/Mehltau-Resistenz, Bluetezeit, Auto, Farbe) vom Donor in einen fast idealen rekurrenten Elter einbringen, ohne dessen Profil zu verlieren. (Farming-KB cannabis-backcrossing-breeding.md, Cervantes)
- Ablauf dominantes Merkmal: P_rec × Donor → F1 (alle tragen) → F1 × P_rec → **BC1** (50 % zeigen) → selektierte BC1 × P_rec → BC2 … ; rezessives Merkmal: nach jeder BX einmal selbsten/sibkreuzen oder Marker nutzen, um Traeger zu erkennen.
- Erwarteter Anteil rekurrentes Genom (Standardgenetik): F1 50 % · BC1 75 % · BC2 87,5 % · BC3 93,75 % · BC4 96,9 %; Szeneregel "BX3 = auf den Elter stabilisiert" (dirt/nomenclature.md). Real messbar per SNP (piercetaylor/backcross: Recurrent-Parent-Recovery, Donor-Segmente, Linkage Drag).
- Feminisierter BX-Pfad (dirt/stabilization-strategy.md): `F1-Maennchen × Elite-Klon A → F2; beste F2-♀ × reversierter A-Pollen → BX1 fem; beste BX1-♀ × rev. A → BX2 fem`; danach entscheiden: weiter BX, selbsten oder zurueck zur F-Linie. **BX engt Diversitaet ein und ersetzt keinen Progeny-Test.**
- Wann BX statt F-Linie: nur wenn ein Elter klar der Phaenotyp-Anker ist; sonst Familienselektion (Rekombinanten besser als beide Eltern). (stabilization-strategy.md)
- Linkage Drag: eingekreuzte QTL bringen Hintergrund mit; mehrere BX-Generationen + Rekombination noetig, nicht eine Markerselektion. (K-Dense plant-breeder SKILL)

## 9. Keeper-Erhalt, HLVd, Gewebekultur

- Redundanz: **≥ 2 Muetter** (getrennte Raeume), bewurzelte Backup-Stecklinge, Mutter-Verjuengung aus gesunden Stecklingen, **HpLVd-Test vor Mutterstatus**, Etikett (Sorte, Hunt-ID, Datum) auf jeder Pflanze/Schale. (genetics-phenohunting.md)
- HpLVd ("Dudding"): ~256-nt RNA-Viroid; CA 2021: **~90 % der Betriebe, ~30 % der Pflanzen** positiv; THC −50…70 %; meist symptomlos; Uebertragung mechanisch (Klinge, Saft ~7 Tage, Trockenmaterial ~4 Wochen infektioes), Wurzel-zu-Wurzel in gemeinsamer Naehrloesung ≤ 2 Wochen, Bench/Giesskanne positiv; nach Stichinfektion Wurzel 2–3 Wo, Blatt 4–6 Wo positiv → **Wurzelprobe, mehrere Stellen**; Test **alle 4–6 Wochen**, immer **vor** grosser Stecklingsernte; Quarantaene neuer Genetik + 2 Tests (Prime Cuts: 14 Tage, Tag 1 + Tag 14, Muetter alle 90 Tage); **neue Klinge je Pflanze oder 10 % Bleiche**, Isopropanol/Flamme-ohne-Bleiche unzuverlaessig; keine Rezirkulation fuer Muetter; infizierte Pflanze entsorgen; 12/12 beschleunigt Ausbreitung. (mother-plants.md; hlvd-prevention-protocol.md; Punja 2025; Adkar 2023) (S)
- Gewebekultur: Meristemdom 0,2–0,5 mm ohne Leitgewebe → einzige Methode, HpLVd zu entfernen (Erfolg ⌀ ~41 %, 0–100 % je Genotyp), Nachweis per RT-qPCR ("Indexing"); Zeit bis sauberer Klon 10–15 Wochen, bis getestete saubere Mutter 5–6+ Monate; Kontaminations-/Endophytenrisiko, Erstbatch als Methodentest; **Mutationslast ∝ Subkulturen (r > 0,92)** → Archivkopie frueh, wenige Subkulturen; Cryo (Droplet-Vitrifikation) als Langzeitversicherung. (tissue-culture.md; Adamek 2024; Monthony 2021) (S)
- Klon-"Drift" = meist Epigenetik + Virenlast + Alter, selten DNA; TC-Reset stellt Vigor wieder her. (Medcan-Agent genetic_stability.md)
- Stecklinge: 3 voll entfaltete Blaetter, keine Blattspitzen kuerzen, apikal/basal egal (Caplan 2018); Retip-Stecklinge bewurzeln 76–81 % ohne Hormon (Kurtz 2022). (mother-plants.md Refs) (S)
- Muetter: 18 h Licht (Bluete wird bei allen getesteten Sorten schon bei 14 h ausgeloest, Ahrens 2023); Feedback = Bewurzelungsrate der Stecklinge; Ersatz nach Daten, mit Ueberlappung. (mother-plants.md) (S)

## 10. Record-Keeping-Schema (fuer Vault/CSV)

Trust-Modell je Stammbaum-Kante (CRS-01): `VERIFIED` (menschlich kuratiert/Breeder-Original) · `COMMUNITY_CONSENSUS` (≥ 2 unabhaengige Domains) · `ANECDOTAL` (1 Quelle, z. B. nur SeedFinder) · `CONTRADICTED` (abweichende Elternsets – behalten, markieren, nie loeschen); jede Claim mit Quell-URL.

```text
lines.csv        line_id, name, breeder, generation(P|F1|F2|F3|F4|F5|BX1..3|S1|IBL), seed_type(regular|feminized|auto),
                 genetic_type(landrace|ibl|polyhybrid|auto), chemotype(I|II|III|IV|V|unknown), chemo_source(breeder_claim|lab_tested|marker),
                 auto1_status(auto|carrier|photo|unknown), herm_history, source_url, trust_tier
plants.csv       plant_id(=pack_code+seed_no), line_id, germ_date, sex(unknown|F|M|intersex), sex_method(preflower|pcr), flip_date,
                 clone_backup_n, hlvd_test_date, hlvd_result, status(hunt|mother|keeper|culled), cull_reason
scores.csv       plant_id, week, stretch_ratio, structure, flower_onset, pest_mold, aroma_note, aroma_score, trichome, color_calyx, yield_g_dry,
                 flower_days, root_rate_backup, hash_wash, lab_thc, lab_cbd, terpenes_json, total_weighted, gate_pass(bool)
crosses.csv      cross_id, mother_plant_id, father_plant_id_or_donor, pollination_method(open|manual|isolation|bag|brush|stored_pollen|
                 selfing_inversion|chemical_feminization), reversal_agent(STS|CS|none), branch_position, pollination_day_after_flip,
                 harvest_date, seeds_n, lot_id, notes
pollen_lots.csv  lot_id, male_plant_id, collection_sessions, dry_hours, flour_ratio, storage(-18C|4C|RT), stored_date, aliquots_n, aliquots_used, viability_check
seed_lots.csv    lot_id, cross_id, seed_type, harvest_date, seeds_n, storage, germ_tests(json: date,n,pct)
progeny_tests.csv lot_id, germinated, culled_pre_flip(json reasons), females_flowered, on_target, intersex, off_target, pct_on_target,
                 verdict(<70 unstable|70-90 selection|>90 production), repeat_no
```
Quellen: Reviews-Maker 05_GENETIQUE_GENEALOGIE.md (Felder/Enums), dirt feminized-production.md (Progeny-Nenner), dirt pollen-handling.md (Lot-IDs), cannabis-white-papers (ID-Regel, Kriterien), CRS-01 README (Trust-Tiers), isley/growforge (Journal-Tabellen).

## 11. KCanG-Randbedingungen fuer das Programm (nur Hinweis, keine Rechtsberatung)

- § 9 Abs. 1: Erwachsene duerfen am Wohnsitz **insgesamt nicht mehr als 3 Cannabispflanzen gleichzeitig** anbauen; Abs. 2: keine Weitergabe an Dritte. § 10: Cannabis **und Vermehrungsmaterial** (Samen, Stecklinge, Pollen-tragende Pflanzen) vor Dritten, insbesondere Kindern, sichern. § 4 Abs. 2: Samenimport fuer Eigenanbau nur aus EU-Mitgliedstaaten. (`legalize-dev__legalize-de/de/KCANG.md` Z. 183, 255–263)
- Konsequenz: Pheno-Hunts mit 10–50 Samen sind privat nicht abbildbar → Staffelung (max. 3 lebende Pflanzen: z. B. Mutter + Samentraegerin + Pollenelter), Pollen-Banking (18–24 Monate) entkoppelt Zeitpunkte; groessere Populationen nur im Rahmen einer Anbauvereinigung (§§ 11 ff.) – Details ueber die vorhandenen recht/-Skills pruefen.

## Quellen (Kurz)
Repos: JakeTheRabbit/cannabis-white-papers (CC BY-NC 4.0) · akravetz/dirt · HomunculusLabs/Farming-KB (Clarke/Cervantes/Small-Exzerpte) · Jack-MillionMedia/Medcan-Agent · johnhouston707/cannabis-cultivation-resources · RAFOUgg/Reviews-Maker · 0-CYBERDYNE-SYSTEMS-0/CRS-01 · K-Dense-AI/scientific-agents · human-avatar/skills-for-agriculture · MylesLab/cannabis-labelling · nickpalladino/kannapedia-data · piercetaylor/backcross · HighlanderLab/jbancic_alphasimr_plants · legalize-dev/legalize-de.
Papers (S): de Meijer 2003/2009 · Laverty 2019 · Grassa 2021 · Toth 2020/2022 · Mohan Ram & Sett 1982 · Lubell & Brand 2018 · Flajsman 2021 · Front Plant Sci 2024 (15:1384286) · Punja & Holmes 2020 · Punja 2025 · Adkar-Purushothama 2023 · Adamek 2024 · Monthony 2021 · Caplan 2018 · Kurtz 2022 · Ahrens 2023 · Cockson 2025 · Sawler 2015 · Schwabe 2019 · McPartland 2018 · Divashuk 2014 · Bancic 2024 · Gaynor 2021. Volle Zitate: `09_cannabis_breeding.md` → Quellen.
