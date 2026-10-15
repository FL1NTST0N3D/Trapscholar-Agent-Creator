---
name: ls-design-referenz-crawl
description: "Referenzmarken (OMD/omdwear, Heybalu, Petprinted, Ad-Library-Gewinner) komplett abziehen und als Designsprache auswerten: Shop-Katalog via products.json, Bestseller-Sortierung, Instagram-Grid, aktive Ads, Farbwelten, Kompositionsmuster, Preisband. haiku crawlt, sonnet wertet aus, opus urteilt. Laden vor jeder Designrunde und im Markt-Radar."
---
# Design-Research per Referenz (Entwurf 2026-10-15, aus GitHub-Crawl 04 + 08)

Ziel: nicht kopieren, sondern messbar wissen, WAS die Referenz besser macht (Phil: "die muessen wirklich auf das niveau von omd kommen"). Referenz-Niveau-Datei bleibt `Ops/_eingang/REFERENZ_OMDWEAR_2026-10-07/`.

## 1. Crawl (haiku, `ls-crawler`)
Je Marke in `Ops/_eingang/REFERENZ_<MARKE>_<datum>/`:
1. Katalog: `https://<shop>/products.json?limit=250&page=N` (Shopify) -> `katalog.csv` (handle, titel, typ, tags, preis, bilder[], created_at, varianten). Skill-Muster: `08_research_data/zhaoheng588-tech__shopify-scout`, `practical-data-science__ShopifyScraper`.
2. Bestseller: `/collections/all?sort_by=best-selling` Seite 1-3 -> Reihenfolge = `bestseller_rank`. Review-Zahlen aus Judge.me/Loox-Widget-JSON, falls sichtbar.
3. Instagram: Profil-Grid (letzte 30 Posts: Bild-URL, Caption, Likes, Datum) ueber ScrapeCreators-/Apify-Skill (`05_social/ScrapeCreators__social-media-research-skills`, `08_research_data/apify__agent-skills`) oder Claude-Browser-Rohlesen (`stammbaum-crawler`-Methode).
4. Ads: Meta Ad Library (EU zeigt alle aktiven Ads) via `08_research_data/RamsesAguirre777__facebook-ads-library-mcp` oder `logiover__meta-ad-library-scraper` -> `ads.csv` (start_date, format, text, bild/video-url, laufzeit_tage). Laufzeit >= 30 Tage = Gewinner-Signal.
5. Bilder der Top-30 (Bestseller + laengste Ads) lokal ablegen (`bilder/`), max 1 MB je Bild.

## 2. Auswertung (sonnet, `ls-design-researcher`)
`designsprache.md` je Marke:
- Motiv-Typen: Anteil Portrait / Szene / Typo-only / Parodie / Foto-Personalisierung (zaehlen aus Top-30).
- Komposition: Rand gestaltet oder Kasten? Pop-out? Mitte? Hochformat-Anteil? (`omd-bauweise` Kriterien 1-14 als Checkliste, je Bild 0/1).
- Farbwelt: 5 Hauptfarben je Bild per PIL k-means (k=5) -> Cluster ueber alle Top-30 -> Palette mit Haeufigkeit. Kontrast Motiv/Textil (Delta L*).
- Typografie: Schriftklassen (Serif/Sans/Display/Script), Anzahl Schriften je Design, Textanteil.
- Spruch-Logik: Wortspiel / Rolle (Hundemama) / Rasse / Anlass; Sprache.
- Preisband: Median, Min, Max je Produkttyp; Streichpreise ja/nein; Bundles.
- Bestseller-Signale: welche Motiv-Typen stehen vorne? Korrelation Typ x Rank.
- Instagram: Posting-Takt, Format-Mix (Reel/Carousel/Bild), UGC-Anteil, Hook-Muster der Top-5 nach Likes.
- Ads: Formate, Hook-Typen (Frage/Statement/Social Proof), Person-von-hinten + echter Hund? heller Hintergrund? (Lernsatz 15.10.)

## 3. Vergleich + Urteil (opus, `ls-master-designer`)
`Ops/_eingang/REFERENZ_VERGLEICH_<datum>.md`: Tabelle Marke x Kriterium + je Marke 3 Punkte "machen sie messbar besser" mit Bild-URL-Beleg + 3 Punkte "machen wir besser". Daraus Ueberbieten-Plan je neuem Design (`design-evaluation`).

## 4. Takt
Woechentlich im Markt-Radar (montags), Delta-Report gegen Vorwoche (neue Produkte, neue Ads, Preisaenderungen). Vor jeder Designrunde: Bestseller-Top-10 der Referenzmarke als Pflichtlektuere des Richters.

## Regeln
Kein 1:1-Nachbau, keine Logos/Fonts, keine Markennamen in Prompts (REGELN KEIN STIL-KOPIEREN). Referenzbilder duerfen fuer Komposition in Gemini hochgeladen werden (Regel 11 vom 15.10.).
