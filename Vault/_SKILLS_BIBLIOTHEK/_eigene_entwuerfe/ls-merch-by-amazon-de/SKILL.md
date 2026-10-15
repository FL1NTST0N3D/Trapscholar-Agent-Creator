---
name: ls-merch-by-amazon-de
description: "Lil Snouts auf Merch by Amazon (Merch on Demand) bringen: Nischen-Research mit Zahlen, Markencheck (USPTO/EUIPO/DPMA), Listing-Validator (Zeichenlimits), Royalty-Rechnung, Tier-Strategie, manueller Upload-Ablauf (kein Bulk-Upload erlaubt). Laden bei jeder Merch-Aufgabe."
---
# Merch by Amazon fuer Lil Snouts (Entwurf 2026-10-15, aus GitHub-Crawl 03)

Befund Crawl: Es gibt auf GitHub KEINEN fertigen Merch-Skill, keinen MCP, keine erlaubte Upload-API. Amazon-FAQ: "scripting for bulk upload: No" (zitiert in `github-crawl-2026-10-15/03_pod_marketplaces/benpearson2003__amathon/README`). Selenium-Uploader (MerchPy, amathon) verstossen gegen die Merch-Regeln -> NICHT benutzen, Konto-Sperre. Alles bis zum Upload automatisieren, Upload = Phil-Klick (oder Claude-Browser mit Phils Wort je Design).

## 1. Modell-Routing
haiku: Research-Crawl, Trademark-Lookup, Zeichen-Validator, Royalty-Tabelle. sonnet: Listing-Texte (Titel/Brand/Bullets/Description EN+DE), Nischen-Score. opus: Go/No-Go je Design (Markenrisiko, Nische, Design-Niveau).

## 2. Nischen-Research (haiku -> sonnet)
Quellen: Amazon Suche `site:amazon.de "Merch on Demand"`-Listings via `ls-crawler` (Suchbegriff -> Treffer, BSR, Preis, Review-Anzahl), Autocomplete-Seeds (`AILabs-official__aws-kdp/scripts/amazon_research.py` nur als Muster lesen), Google Trends (`HasData__google-trends-mcp`), Bestseller-Crawls `Ops/_eingang/BESTSELLER_*`.
Score je Nische (0-100): Nachfrage (Autocomplete-Treffer, Trends-Index 12 Mon.), Wettbewerb (Anzahl Merch-Listings, BSR Top-10 Median), Preisband (>= 19,99 EUR), Markenrisiko (Schritt 3), Passung Lil Snouts (Hund/Katze, Parodie-Faehigkeit, DE-Humor). Gewichte 30/25/15/20/10. Ergebnis `Ops/MERCH/NISCHEN_<datum>.md`.

## 3. Markencheck (haiku, Pflicht vor jedem Listing)
- USPTO: `pipeworx-io__mcp-trademarks` (keylos) oder TESS-Nachfolger-Suche; EUIPO: eSearch-URL `https://euipo.europa.eu/eSearch/#basic/1+1+1+1/100+100+100+100/<begriff>`; DPMA: DPMAregister-URL je Begriff.
- Jedes Wort im Titel/Spruch + jede Bildmarke pruefen; Klasse 025 (Bekleidung) und 018. Verdict je Begriff: CLEAR / WARNING (aehnliche lebende Marke) / FAIL (identische lebende Marke in 025).
- Parodien: Marken-/Figurennamen nie woertlich (Phil-Regel KEIN STIL-KOPIEREN, nie 1:1-Logos/Fonts). Fassaden-Logik aus `bestseller-textildesign`.
- Logzeile: `MARKE | <begriff> | USPTO=<v> EUIPO=<v> DPMA=<v> | <quelle-url>`. FAIL = Design nicht einreichen.

## 4. Listing-Validator (haiku, hart)
Limits Merch: Brand 50 Zeichen, Titel 60, Bullet 1 und 2 je 256, Beschreibung 2000; keine Marken Dritter, keine URLs, kein "Amazon", keine Preis-/Versandangaben, kein "best seller". Sprache je Marktplatz (amazon.de = DE, .com = EN). Datei `Ops/MERCH/LISTING_<slug>.md` mit Feld, Text, Zeichenzahl, OK/FAIL.

## 5. Royalty-Rechnung (haiku)
Royalty = Listenpreis - USt - Amazon-Kosten (Druck + Service, Tabelle je Produkt/Marktplatz aus dem Merch-Dashboard "Royalty Calculator", Stand monatlich in `Ops/MERCH/ROYALTY_TABELLE.md` eintragen). Mindest-Royalty je Shirt: 3,00 EUR, sonst Preis rauf oder nicht listen.

## 6. Tier-Strategie
Tier 10 -> 25 -> 100 -> 500: Tier-Up nur durch verkaufte Stueck (je Tier alle Slots verkauft). Deshalb: Slots nur mit Nischen-Score >= 60 und Phil-OK-Design-Niveau fuellen; schlecht laufende Designs (0 Verkaeufe in 60 Tagen) loeschen und Slot neu belegen (Loeschung = Phil-Wort).

## 7. Datei-Specs
PNG, 4500 x 5400 px, 300 dpi, transparent, <= 25 MB, kein Rand-Kasten (Kasten-Gate aus `omd-bauweise`). Druckdatei aus TeeInBlue-Export (`teeinblue-ops` 7.6 lossless) oder Marketprint-Export, Readback: Groesse + Alpha-Rand messen (`omd-gate-messung`).

## 8. Upload-Ablauf (Phil oder Claude-Browser mit Phil-Wort)
Dashboard merch.amazon.com -> Create -> Produkt -> PNG hochladen -> Farben (max 10, nach STATION F) -> Marktplaetze -> Listing-Felder aus LISTING_<slug>.md einfuegen -> Preis aus Royalty-Tabelle -> Submit. Je Design eine Logzeile `MERCH | <slug> | eingereicht | <datum>`; Status (under review / live / rejected) in `Ops/MERCH/REGISTER.md` nachtragen (haiku, taeglich).

## Quellen (Bibliothek)
`github-crawl-2026-10-15/03_pod_marketplaces/`: AILabs-official__aws-kdp (trademark_check.py Muster, niche-hunter), nexscope-ai__Amazon-Skills (amazon-listing-optimization, amazon-niche-finder), pipeworx-io__mcp-trademarks, benpearson2003__amathon (nur CSV-Schema). Katalog `_KATALOG/03_pod_marketplaces.md`.
