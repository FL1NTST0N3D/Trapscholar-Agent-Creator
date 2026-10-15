# Print-on-Demand & Marktplätze (Merch by Amazon, KDP, Amazon Seller/PPC, Etsy, Redbubble/Spreadshirt/Teepublic, Printful/Printify/Gelato/PrintKK, Mockups, Trend- & Markenrecherche)

Stand: 2026-10-15. Crawl für Lil Snouts (Hunde-/Katzen-Apparel, DE). Alle Pfade relativ zu `scratchpad/crawl/repos/`. Verzeichnisse mit `__` wurden in diesem Crawl neu geklont (bzw. von parallelen Crawlern), Verzeichnisse mit `_` lagen bereits vor. Kein Code wurde ausgeführt, nur gelesen. 24 WebSearch-Abfragen (extended) durchgeführt.

Hinweis zu Amazon-Richtlinien: Die Merch-on-Demand-FAQ (im README von `benpearson2003__amathon` zitiert) verneint ausdrücklich „scripting for bulk upload of designs". Alle Selenium-Uploader für Merch sind deshalb nur als Referenz für Feld-Mapping/CSV-Struktur zu verstehen, nicht als Produktivwerkzeug.

## Gecrawlte Repos

| Repo | URL | Lizenz | Inhalt kurz | Anzahl SKILL.md / Agents / Scripts | Relevanz 1-5 | Automatisierbar? |
|---|---|---|---|---|---|---|
| **Merch by Amazon** | | | | | | |
| AffiliateCoaches__MerchPy | https://github.com/AffiliateCoaches/MerchPy | GPL | Selenium-Uploader für Merch by Amazon; `merchpy.csv` mit Spalten Shirt Type, Brand Name, Title, Desc 1/2, Colors, Fits, Price, File; `daily_limit = 10` | 0 / 0 / 1 (merch.py) | 2 | Nein (Policy-Verstoß); CSV-Schema als Vorlage nutzbar |
| benpearson2003__amathon | https://github.com/benpearson2003/amathon | BSD-3 | `merchify.py` (PIL: Art auf 4500x5400-Shirt-Canvas zentrieren), `upload.py` (Selenium mit Merch-DOM-IDs wie `data-draft-brand-name`, Fit-Type-Checkboxen, Farb-Checkboxen), `scrapeImages.py` | 0 / 0 / 4 | 2 | Nur Canvas-Script (merchify) unbedenklich; Upload nein |
| **Amazon KDP** | | | | | | |
| AILabs-official__aws-kdp | https://github.com/AILabs-official/aws-kdp | keine Lizenzdatei | Vollständige KDP-Pipeline (Vietnamesisch/Englisch): `.claude/skills/` mit niche-hunter (676 Zeilen, 9 Datenquellen, Opportunity Score), kdp-category-finder (19k Kategorien crawlen, #1-Bestseller schwach?), ads-manager (Sponsored Products), kdp-cover-creator/checker, image-generator, quality-reviewer; `scripts/trademark_check.py` (USPTO Class 016 + Trademarkia + EUIPO-URLs, Verdict CLEAR/WARNING/FAIL/MANUAL_CHECK), `amazon_research.py` (Autocomplete-Seeds, Kategorie-URLs), `apify_research.py` (junglee/Amazon-crawler), `niche_criteria.py` (versionierte Scoring-Gewichte) | 21 / 0 / 35 | 5 (als Blaupause) | Ja, nach Umbau auf Class 025 (Bekleidung) |
| semrebayrak__tomescout-claude-plugin | https://github.com/semrebayrak/tomescout-claude-plugin | MIT | Claude-Plugin + gehosteter MCP (tomescout.com): keyword_boxes, check_listing, royalty_calculator, bsr_to_sales; Skills kdp-listing-prep, kdp-niche-sizing-by-rank | 4 / 0 / 0 | 2 | Ja (MCP, extern gehostet) |
| ainjection__kdp-niche-scorer-mcp | https://github.com/ainjection/kdp-niche-scorer-mcp | keine | Gehosteter MCP (mcpize.run): Keyword → 0-100 Score aus BSR, Konkurrenzzahl, Seitenzahl, Review-Velocity | 0 / 0 / 9 | 2 | Ja (extern) |
| zakaryabelleboukh_amazon-kdp-skill (vorhanden) | https://github.com/zakaryabelleboukh/amazon-kdp-skill | MIT | Ein SKILL.md: Manuskript/Cover/Metadaten-Workflow, QC-Gates | 1 / 0 / 0 | 1 | Prompt-only |
| joshyattridge_amazon-kdp-skill (vorhanden) | https://github.com/joshyattridge/amazon-kdp-skill | keine | KDP-Dashboard-Automation per Playwright: skills connect-session, publish-book, update-metadata, update-pricing, download-reports, parse-reports; 40+ TS-Scripts mit DOM-Probes | 12 / 0 / 70 | 2 | Ja (Browser-Automation, fragil) |
| **Amazon Seller / SP-API / PPC** | | | | | | |
| nexscope-ai_Amazon-Skills (vorhanden) | https://github.com/nexscope-ai/Amazon-Skills | MIT | 52 Prompt-Skills: amazon-keyword-research (200 Z.), amazon-listing-optimization (428 Z.), amazon-niche-finder (321 Z., 1-10 Scoring), amazon-trending-products (252 Z., BSR-Muster), amazon-backend-keywords, amazon-ppc-campaign, amazon-negative-keywords, amazon-product-compliance, amazon-global-selling, amazon-international-listings; Scripts nur fba-calculator & tariff | 52 / 0 / 6 | 4 | Prompt-Frameworks, kein API-Zugriff |
| brianmoney_amazon-marketing-skill (vorhanden) | https://github.com/brianmoney/amazon-marketing-skill | MIT | Router-Skill + 6 Sub-Skills (keyword-research, listing-optimizer, listing-audit, a-plus-content, competitor-analysis, product-onboarding), Templates, `asins.csv` | 7 / 0 / 0 | 3 | Prompt-only |
| ferrants_amazon-seller-agent-claude-code (vorhanden) | https://github.com/ferrants/amazon-seller-agent-claude-code | MIT | 10 Skills an den Marketplace-Ad-Pros-MCP gebunden: amazon-listing-audit (RUFUS-Score, Hijacking, Suppressed), amazon-ads-optimization, search-term-harvest-dashboard, wasted-ad-spend-dashboard, fba-inventory-risk | 10 / 0 / 1 | 3 | Ja, mit externem MCP |
| nospicyplease__amazon-ppc-advanced-skills | https://github.com/nospicyplease/amazon-ppc-advanced-skills | MIT | 7 PPC-Skills: search-term-harvest-planner (294 Z.), ads-performance-drop-diagnosis (205 Z.), growth-opportunity-finder, account-growth-operating-system, rocketcart-live-review; Safety-Invariante: nie selbst schreiben | 7 / 0 / 19 | 3 | Analyse ja, Writes nur mit Freigabe |
| bhavykhatri__amazon-seller-mcp | https://github.com/bhavykhatri/amazon-seller-mcp | MIT | Self-hosted SP-API-MCP (`npx seller-central-mcp`): Listings, Orders, Reports, Feeds, Pricing; LWA-only Auth; jede Region/Marktplatz (DE setzbar) | 0 / 0 / 14 | 4 | Ja (eigener SP-API-Developer-Account nötig) |
| coaxon__amazon-mcp | https://github.com/coaxon/amazon-mcp | MIT | Self-hosted Python-MCP für SP-API + Ads API (read-orientiert): Orders, Inventory, Pricing, Ads, Reports | 0 / 0 / 126 | 3 | Ja |
| KuudoAI__amazon-selling-partner-mcp | https://github.com/KuudoAI/amazon-selling-partner-mcp | MIT | Registry-Stub; 304 SP-API-Operationen, läuft in eigener Cloud (Kuudo) | 0 / 0 / 0 | 2 | Ja (Hosted) |
| ppcprophet__amazon-ads-mcp | https://github.com/ppcprophet/amazon-ads-mcp | MIT | Gehosteter Amazon-Ads-MCP: Wasted Spend, Metrik-Diagnose, Automationsregeln | 0 / 0 / 11 | 2 | Ja (SaaS) |
| TheBurdz__amz-vault-mcp | https://github.com/TheBurdz/amz-vault-mcp | MIT | Nur Registry-Listing für gehosteten MCP (Seller Central + Ads, PPC/SQP) | 0 / 0 / 0 | 1 | SaaS |
| agentcentral-to__agent-central-mcp | https://github.com/agentcentral-to/agent-central-mcp | MIT | Registry-Stub, Hosted MCP für Ads + Seller Central, 23 Marktplätze inkl. DE | 0 / 0 / 1 | 2 | SaaS |
| pangolinfoapi__amazon-niche-finder | https://github.com/pangolinfoapi/amazon-niche-finder | MIT | `niche_finder.py` (stdlib): Blue-Ocean-Score = Suchvolumen ÷ Markenanzahl via Pangolinfo-API, GitHub-Actions-Tracking, `niches.json` | 0 / 0 / 1 | 3 | Ja (API-Key Pangolinfo) |
| Umair706__amazon-omniscient | https://github.com/Umair706/amazon-omniscient | proprietär („All Rights Reserved") | FBA-Research-Engine (FastAPI+Next.js, Playwright): BSR-Tracker, Niche Finder, Profit | 0 / 0 / 224 | 2 | Lizenz blockiert Übernahme |
| data-scrape__amazon-product-scraper | https://github.com/data-scrape/amazon-product-scraper | MIT | Ein Python-Script (CoreClaw-Werbung), BSR/Preis/Bilder → JSON/CSV | 0 / 0 / 1 | 1 | Bedingt |
| eaintkyawthmu__Amazon-Bestseller-Scraper | https://github.com/eaintkyawthmu/Amazon-Bestseller-Scraper | keine | Tutorial-Scraper für Amazon Fashion Bestsellers (BS4+Selenium) | 0 / 0 / 1 | 2 | Bedingt (Fashion-BSR-Seite = Merch-relevant) |
| m-murasovs__amazon-bestsellers-scraper (Sibling) | https://github.com/m-murasovs/amazon-bestsellers-scraper | Apache-2.0 | Apify-Actor: Top-100-Bestseller für .com/.co.uk/.de/.fr/.es/.it | 0 / 0 / 5 | 3 | Ja (Apify) |
| omkarcloud__amazon-scraper (Sibling) | https://github.com/omkarcloud/amazon-scraper | MIT | Open-Source-Scraper-API: Produktdetails, Suche, Bestseller-Endpoint | 0 / 0 / 21 | 3 | Ja |
| **Etsy** | | | | | | |
| amirjahfar1__Etsy-MCP-Server | https://github.com/amirjahfar1/Etsy-MCP-Server | keine Lizenzdatei | Node/TS-MCP ~90 Tools (Etsy API v3, Multi-Account, Confirm-before-write) + 29 Skills in `.claude/skills/` (doppelt im Repo): etsy-niche-scanner, etsy-keyword-research (Tag-DB), etsy-product-ideation, etsy-new-listing-copywriter, etsy-optimize-listing, etsy-competitor-research, etsy-pricing-audit, etsy-seasonal-keywords, etsy-risk-scan, etsy-fee-watchdog, etsy-financial-report, etsy-morning-briefing | 58 / 0 / ~40 | 5 | Ja (Etsy-Developer-App nötig) |
| aserper__etsy-mcp | https://github.com/aserper/etsy-mcp | MIT | TS-MCP, 37 Tools (~70 Endpunkte): create_draft_listing, update_listing, upload_listing_image/video, inventory, shipping profiles, receipts, taxonomy; OAuth-PKCE, Rate-Limiter, Docker | 0 / 0 / 30 | 5 | Ja |
| BusyBee3333__etsy-mcp-2026-complete | https://github.com/BusyBee3333/etsy-mcp-2026-complete | keine | TS-MCP „50+ Module", Zod-Schemas, readOnly/destructive-Hints | 0 / 0 / 50 | 3 | Ja |
| georgejeffers__etsy-mcp-server | https://github.com/georgejeffers/etsy-mcp-server | keine | Kleiner TS-MCP: Listings anlegen, Shop, Shipping Profiles, Bild-Upload | 0 / 0 / 10 | 2 | Ja |
| moiz-za_etsy-seller-seo-system (vorhanden) | https://github.com/moiz-za/etsy-seller-seo-system | MIT | 450-Zeilen-Skill „etsy-seller": REWRITE/CREATE-Modus, Live-Autocomplete-Research, 13-Tag-Optimierung, Indexing-Spread-Check, Policy-Sync-Script | 1 / 0 / 3 | 5 | Ja (Prompt + Web-Research) |
| silennsong_etsy-listing-helper (vorhanden) | https://github.com/silennsong/etsy-listing-helper | MIT | POD-Spezifikation + Produktfoto → Titel (≤140), 13 Tags (≤20 Z.), Beschreibung, Materialien, Kategorie-Pfad, Attribute, Alt-Text, Varianten; mehrsprachig | 1 / 0 / 0 | 5 | Ja (Prompt-only) |
| nexscope-ai_eCommerce-Skills (vorhanden) | https://github.com/nexscope-ai/eCommerce-Skills | MIT | 162 Skills; vollwertig: etsy-seo (174 Z. + `analyzer.py` 0-100-Score); **Stubs (56 Zeilen, generischer Text)**: etsy-print-on-demand, etsy-seo-tags, etsy-keyword-research, etsy-competitor-analysis, etsy-advertising, etsy-pricing-strategy u.a.; zusätzlich ebay-*, tiktok-shop-*, walmart-listing | 162 / 0 / 42 | 3 | etsy-seo ja; Rest Platzhalter |
| ghosttown123_etsy-ugc-compliance-harvester (vorhanden) | https://github.com/ghosttown123/etsy-ugc-compliance-harvester | – | Etsy-Seller-Ops/Compliance-Suite (von anderem Crawler bewertet) | – | 2 | – |
| robomello__claude-code-setup | https://github.com/robomello/claude-code-setup | keine | `skills/etsy-browser/SKILL.md` (201 Z.): Etsy-Shop-Management über interne API (httpx) + Playwright-Fallback, Batch-Update, 4 Shops | 14 / 30 / 27 | 3 | Ja, aber inoffizielle API (ToS-Risiko) |
| 2scraper__etsy-scraper (Sibling) | https://github.com/2scraper/etsy-scraper | MIT | Etsy-Scraper (Suche, Kategorie, Shop, Listing), 3 Browser-Engines, DataDome-aware, JSON/CSV | 0 / 0 / 15 | 4 | Ja (Konkurrenz-Research) |
| scraper-bank__Etsy.com-Scrapers (Sibling) | https://github.com/scraper-bank/Etsy.com-Scrapers | MIT | Python+Node Etsy-Scraper (Playwright/Puppeteer) | 0 / 0 / 18 | 3 | Ja |
| **POD-Anbieter-APIs** | | | | | | |
| Purple-Horizons__printful-mcp (vorhanden) | https://github.com/Purple-Horizons/printful-mcp | MIT | Python-MCP, 19 Tools: catalog, variants, variant_prices (EUR), availability, create/confirm order, calculate_shipping, **create_mockup_task/get_mockup_task**, add_file, store_stats; Cursor-SKILL.md | 1 / 0 / 20 | 4 | Ja |
| rudberga__printful-mcp (Sibling) | https://github.com/rudberga/printful-mcp | MIT | Read-only Printful-MCP (bewusst ohne Order-Writes) | 0 / 0 / 3 | 2 | Ja |
| five59__pyPrintful | https://github.com/five59/pyPrintful | Apache-2.0 | Python-Wrapper Printful (pip `pyprintful`) | 0 / 0 / 3 | 2 | Ja |
| mdn522__printful-api-python | https://github.com/mdn522/printful-api-python | keine | Inoffizieller Python-Wrapper (alt) | 0 / 0 / 5 | 1 | Bedingt |
| TSavo__printify-mcp | https://github.com/TSavo/printify-mcp | ISC | Printify-MCP (TS, Docker): Shops, Products, Blueprints/Variants, Image-Upload, AI-Design-Workflow „T-Shirt mit KI-Design" | 0 / 0 / 20 | 4 | Ja |
| jeffkimble__printify-mcp-server (Sibling) | https://github.com/jeffkimble/printify-mcp-server | MIT | Kleiner Printify-MCP (1 Datei) | 0 / 0 / 1 | 2 | Ja |
| lawrencemq__printipy | https://github.com/lawrencemq/printipy | MIT | Python-Wrapper Printify REST v1 (PyPI `printipy`, Py 3.9-3.12) | 0 / 0 / 7 | 4 | Ja |
| clintmcmahon__printify-uploader | https://github.com/clintmcmahon/printify-uploader | keine | Ordner-getriebenes Bulk-Anlegen von Printify-Produkten (mehrere Produkttypen, Dry-Run) | 0 / 0 / 2 | 4 | Ja |
| kylemillerbuilds_printify-publish-queue (vorhanden) | https://github.com/kylemillerbuilds/printify-publish-queue | MIT | Gehärteter Publish-Flow Printify→Shopify/Etsy: State-Machine, 3 Fehlermodi (Queued/Silent-Fail/Duplikat), Tests | 0 / 0 / 2 | 4 | Ja |
| GitStudying__PrintifyProfitCalculator (Sibling) | https://github.com/GitStudying/PrintifyProfitCalculator | keine | Web-Rechner: Produktion+Versand+VAT → Netto-Marge | 0 / 0 / 0 | 2 | Formel übernehmbar |
| denkan__gelato-api | https://github.com/denkan/gelato-api | MIT | TS/JS-Client Gelato (Orders create/get/search/patch/cancel, Products) | 0 / 0 / 13 | 3 | Ja |
| ekkolon__gelato-admin-node | https://github.com/ekkolon/gelato-admin-node | Apache-2.0 | Zero-dependency Node-SDK Gelato: orders, products, shipment, ecommerce; Multi-Account | 0 / 0 / 37 | 3 | Ja |
| 1nc0gn30__gelato-connector (Sibling) | https://github.com/1nc0gn30/gelato-connector | keine | Python-stdlib Gelato-v2-Connector, 32-Länder-Routing, Multi-Currency-Margin-Engine, MCP-Suite | 0 / 0 / 14 | 3 | Ja |
| altetsa__gelato-mcp-server / madzarm__mcp-server-gelato (Sibling) | https://github.com/altetsa/gelato-mcp-server , https://github.com/madzarm/mcp-server-gelato | keine / MIT | Gelato-MCPs: Produktanlage aus Design-URL bzw. Orders/Katalog | 0 / 0 / 1 bzw. 48 | 3 | Ja |
| pizzzzzza_printkk-agent-skill (vorhanden) | https://github.com/pizzzzzza/printkk-agent-skill | MIT | 234-Zeilen-SKILL.md PrintKK-API: Design anlegen (async), Brand-Flow, Bildverwaltung, Gotchas (isWhole, imageFillingMode, Shipping-Prioritätsliste) | 1 / 0 / 0 | 3 | Ja (mit PrintKK-MCP) |
| runjak__sprd-design-upload | https://github.com/runjak/sprd-design-upload | MIT | Node-Tool Spreadshirt-Design-Upload + Metadaten + Veröffentlichen; **archiviert 01/2026**, Image-Pointer-Upload laut Autor nicht mehr möglich | 0 / 0 / 7 | 2 | Nein (veraltet) |
| ChristianKnedel__spreadshirt_api_client | https://github.com/ChristianKnedel/spreadshirt_api_client | keine | Minimal-Python-Client Spreadshirt (Shop-Lesen) | 0 / 0 / 1 | 1 | Kein Upload (offiziell nicht vorgesehen) |
| **Redbubble / Teepublic** | | | | | | |
| jalbrekt85__Redbubble-Bot | https://github.com/jalbrekt85/Redbubble-Bot | MIT | Tkinter-GUI + Selenium: Ordner → Redbubble-Upload, Tags aus tags.txt/Dateiname | 0 / 0 / 1 | 2 | Fragil (DOM), ToS-Risiko |
| dhia10__redbubble | https://github.com/dhia10/redbubble | keine | Modulare POD-Pipeline: `trend_detector.py` (Google Trends via pytrends + Redbubble /trending + Pinterest /ideas per httpx/BS4), `niche_scorer.py` (GPT), `idea_generator.py`, `seo_generator.py` (Titel/Beschreibung/50 Tags), `redbubble_uploader.py` (Playwright), SQLite, Streamlit-Dashboard, `config/prompts.yaml` (Prompts mit IP-Vermeidung) | 0 / 0 / 20 | 4 | Pipeline-Architektur + Prompts übernehmbar |
| winsomeautomation__teepublic-automation-tool | https://github.com/winsomeautomation/teepublic-automation-tool | keine | Tkinter+Selenium Bulk-Uploader Teepublic; enthält chromedriver.exe (25 MB) | 0 / 0 / 2 | 1 | Nein |
| **Mockups** | | | | | | |
| thieuhoang2002__mockup-forge | https://github.com/thieuhoang2002/mockup-forge | (Lizenzdatei vorhanden) | CPU-only fotorealistischer POD-Mockup-Generator (OpenCV/NumPy/Pillow): Displacement-Map für Stofffalten, Shadow-Map, Flask-Web-Studio, `engine.py`, `validator.py`, Abschnitt „Etsy & Ecommerce Listing Standards" | 0 / 0 / 5 | 5 | Ja (wrap als Skill-Script) |
| CTDave001__automated_mockups | https://github.com/CTDave001/automated_mockups | MIT | PyPI `mockup-generator`: Batch Design×Template, Platzhalter-Erkennung per Farbe, Rotation, 9 Alignments | 0 / 0 / ~5 | 4 | Ja |
| kashifulhaque__product-mockup-node-python | https://github.com/kashifulhaque/product-mockup-node-python | keine | ImageMagick-Displacement/Lighting-Maps, Python/Node/Shell-Entry | 0 / 0 / 3 | 3 | Ja (ImageMagick) |
| motiful__product-shots (Sibling) | https://github.com/motiful/product-shots | MIT | 7 Skills für Produktfotos (von anderem Crawler bewertet) | 7 / 0 / 1 | 2 | – |
| **Marken-/IP-Prüfung** | | | | | | |
| pipeworx-io__mcp-trademarks | https://github.com/pipeworx-io/mcp-trademarks | MIT | Hosted MCP: `search_trademarks` (Wortmarken-Volltext, keyless, tmsearch-Backend = TESS-Nachfolger), get_by_serial/registration, documents (USPTO-Key) | 0 / 0 / 5 | 5 | Ja |
| jordanburke__trademark-mcp-server | https://github.com/jordanburke/trademark-mcp-server | MIT | TS-MCP TSDR: search_by_serial/registration, status, image, documents; USPTO-API-Key Pflicht; Docker | 0 / 0 / 15 | 3 | Ja (nur Status, keine Wortsuche) |
| riemannzeta__patent_mcp_server | https://github.com/riemannzeta/patent_mcp_server | MIT | Python-MCP, 42 Tools über 6 USPTO-Quellen inkl. Trademark-Search, TSDR, Assignments | 0 / 0 / 75 | 4 | Ja |
| parkerhancock__patent-client-agents | https://github.com/parkerhancock/patent-client-agents | Apache-2.0 | `skills/ip_research/SKILL.md` (275 Z.) + TsdrClient (Python), Public-Demo-MCP, Routing-Logik | 1 / 0 / 839 | 3 | Ja |
| apifyforge__euipo-trademark-search | https://github.com/apifyforge/euipo-trademark-search | MIT | Nur README für Apify-Actor: EUIPO-API mit OAuth2, RSQL-Queries, Nizza-Klassen, Pagination | 0 / 0 / 0 | 3 | Ja (Apify, kostenpflichtig) |
| mvanhorn__printing-press-library (getrimmt: `library/` + `.git` gelöscht, 2,0 GB → 21 MB) | https://github.com/mvanhorn/printing-press-library | Apache-2.0 | 589 generierte `pp-*`-CLI-Skills (Go-Binaries via npx/go install). Relevant: **pp-uspto-tsdr** (status, timeline, docs, deadlines, watch, batch), **pp-google-trends** (pytrends-Ersatz mit SQLite-Cache, interest-over-time, related/rising), **pp-printify** (manifest-driven Create, placement-matrix, product-drift, catalog-margin-matrix, personalization-batch, fulfillment-risk), **pp-amazon-ads** (break-even-acos, true-profit, acos-vs-tacos, portfolio-dashboard), **pp-amazon-seller** (catalog, listings, fba-inventory), **pp-etsy-seller-dashboard** (read-only Marketplace Insights/Ads/Offsite), pp-kdpnichefinder, pp-trendhunter, pp-ebay, pp-tiktok-shop | 589 / 0 / 0 (Binaries extern) | 5 | Ja (Go-Toolchain oder npx) |
| **Trend-Research** | | | | | | |
| flack0x__trendspyg | https://github.com/flack0x/trendspyg | MIT | Python-Lib Google Trends (pytrends-kompatibel `TrendReq`): Trending Now, Interest over Time, Related, Region, 2-5-Keyword-Vergleich | 0 / 0 / 68 | 4 | Ja |
| yiromo__pytrends-modern | https://github.com/yiromo/pytrends-modern | MIT | pip `pytrends-modern`: HTTP-API, RSS, Camoufox-Browser, Selenium, CLI | 0 / 0 / 24 | 3 | Ja |
| HasData__google-trends-mcp / cryptoken__GoogleTrendsMCP / pipeworx-io__mcp-google-trends (Sibling) | github.com/HasData/google-trends-mcp u.a. | MIT | Google-Trends-MCPs (hosted mit 1.000 Credits/Monat; lokal; Daily-Trending-RSS) | 0 | 3 | Ja |
| N-Graves__pinterest-mcp-server / aymandakirgh__pinterest-mcp / what-name__pinterest-mcp (Sibling) | github.com/N-Graves/pinterest-mcp-server u.a. | MIT | Pinterest-API-v5-MCPs (263 Ops; 35 Tools; Keyword-Research+Analytics) – **kein** trends.pinterest.com-Zugriff | 0 | 3 | Ja |
| trendsmcp-ai__Trends-MCP (Sibling) | https://github.com/trendsmcp-ai/Trends-MCP | MIT | Hosted Multi-Source-Trend-MCP (Google, TikTok, YouTube, Amazon, Reddit) | 0 / 0 / 3 | 3 | SaaS |
| **Komplett-Pipelines (Sibling-Clones, POD-relevant)** | | | | | | |
| 626Labs-LLC__626labs-pod-pipeline | https://github.com/626Labs-LLC/626labs-pod-pipeline | eigene Lizenz | Konzept → KI-Art → QA → BG-Removal → Text-Compositing → Varianten-Matrix → Printify → Etsy-Listing; Python + JSON-Katalog; 1 Skill (`remy`) | 1 / 0 / 16 | 4 | Lizenz prüfen |
| carlosfrias__presswork-pod | https://github.com/carlosfrias/presswork-pod | keine | 4-Agenten-System Scout→Design→Listing→Ledger für Etsy-POD; PLAN_MOCKUP_RENDERER, PLAN_birefnet_bg_removal, PLAN_shirt_color_size_variants, PLAN_listing_etsy_mock_mode | 0 / 4 (AGENTS.md) / 221 | 4 | Architektur-Referenz |
| booleandifference__art-factory | https://github.com/booleandifference/art-factory | MIT | React-Dashboard: Konzept → KI-Bild → Upscale → Claude-Listing-Copy → Gelato-Publish (Etsy) | 0 / 0 / 34 | 3 | Teile übernehmbar |
| kangise__ecommerce-ai-skills | https://github.com/kangise/ecommerce-ai-skills | CC0 | 29 Skills, u.a. `ecom-listing`; jede Zahl mit Quelle, CI-geprüft | 29 / 0 / 95 | 2 | Prompt-only |

Nicht klonbar (404/privat): `DynamicEndpoints/etsy-mcp`, `zhisanhang-droid/amazon-product-research-skill`, `keysersoft/amazon-seller-mcp-server`. Nicht geklont, da nur SaaS-Listings ohne Code: Niche Scout for KDP (mcpmarket), eRank-Skill (pp-erank in printing-press, nicht im Katalogordner gefunden), MerchGhost/Merch Titans (kommerzielle Browser-Extensions).

## Top-Skills/Tools zum Übernehmen

| # | Pfad (unter repos/) | Was es tut | Modell-Tier | Anmerkung für Lil Snouts |
|---|---|---|---|---|
| 1 | `AILabs-official__aws-kdp/scripts/trademark_check.py` | Keyword gegen USPTO-Suche + Trademarkia prüfen, Verdict CLEAR/WARNING/FAIL/MANUAL_CHECK als JSON, Exit-Codes für Agent-Gating; erzeugt zusätzlich manuelle Prüf-URLs (USPTO, Trademarkia, EUIPO) | haiku (Script-Aufruf) | Class 016 → **Class 025 (Bekleidung) + 018 (Hundezubehör)** umstellen; EUIPO/DPMA-URLs sind bereits generiert |
| 2 | `AILabs-official__aws-kdp/.claude/skills/niche-hunter/SKILL.md` + `scripts/niche_criteria.py`, `amazon_research.py` | 9-Schritte-Blue-Ocean-Framework, Opportunity-Score mit versionierten Gewichten, Hard-Elimination (inkl. Trademark), Autocomplete-Seeds, Kategorie-Bestseller-URLs | sonnet (Research), haiku (Scoring-Script) | Als Vorlage für „merch-niche-hunter" (Hund/Katze × Spruch × Anlass) |
| 3 | `AILabs-official__aws-kdp/.claude/skills/kdp-category-finder/SKILL.md` + `scripts/category_finder.py` | Kategorie-Baum crawlen, #1-Bestseller je Blatt holen, BSR→Verkäufe, schwächste zuerst, SQLite-Persistenz | sonnet | Übertragbar auf Amazon-Fashion-/Novelty-T-Shirt-Kategorien (.de) |
| 4 | `mvanhorn__printing-press-library/cli-skills/pp-uspto-tsdr/SKILL.md` | CLI: trademark status/timeline/docs/deadlines/**watch**/batch (TSDR, API-Key) | haiku | Monitoring eigener Marke „Lil Snouts" + Batch-Status fremder Marken |
| 5 | `pipeworx-io__mcp-trademarks` (hosted MCP) | `search_trademarks` Wortmarken-Volltextsuche ohne Key (TESS-Nachfolger) → Knockout-Search für Sprüche | haiku | Einzige gefundene keylose Wortmarken-Suche; EU-Pendant fehlt (siehe Lücken) |
| 6 | `riemannzeta__patent_mcp_server` | Self-hosted Python-MCP mit Trademark-Search + TSDR (42 Tools) | haiku | Alternative zu #5 ohne Drittanbieter-Gateway |
| 7 | `amirjahfar1__Etsy-MCP-Server/.claude/skills/etsy-niche-scanner`, `etsy-keyword-research`, `etsy-new-listing-copywriter`, `etsy-optimize-listing`, `etsy-seasonal-keywords`, `etsy-risk-scan`, `etsy-pricing-audit` | Komplettes Etsy-Agency-Skillset auf eigenem ~90-Tool-MCP; jede Schreibaktion mit Diff+Bestätigung; Tag-Datenbank | sonnet (Research/Copy), haiku (Audits) | Bestes Etsy-Paket; DE-Shop über Multi-Account |
| 8 | `aserper__etsy-mcp` | Schlanker, getesteter Etsy-v3-MCP (37 Tools, OAuth-PKCE, Rate-Limit, Docker) | – (Infrastruktur) | Wenn nur API-Zugriff ohne Skill-Overhead gewünscht |
| 9 | `moiz-za_etsy-seller-seo-system/skill/SKILL.md` | Etsy-SEO REWRITE/CREATE mit Live-Autocomplete, 13 Tags, Indexing-Spread, ehrliche Diagnose, Policy-Freshness | sonnet | Direkt nutzbar; Tags ≤20 Zeichen, DE-Keywords einspeisen |
| 10 | `silennsong_etsy-listing-helper/SKILL.md` + `references/` | POD-Spec + Foto → fertiges Etsy-Listing (Titel/Tags/Beschreibung/Kategorie/Attribute/Alt-Text/Varianten) | sonnet | Für Shirt-/Hoodie-Listings mit TeeInBlue-Spezifikation; mehrsprachig |
| 11 | `nexscope-ai_eCommerce-Skills/etsy-seo/` (+ `scripts/analyzer.py`) | 0-100-Listing-Score über Titel/Tags/Beschreibung/Attribute/Bilder | haiku | Als QA-Gate vor Veröffentlichung |
| 12 | `nexscope-ai_Amazon-Skills/amazon-niche-finder`, `amazon-trending-products`, `amazon-keyword-research`, `amazon-listing-optimization`, `amazon-backend-keywords`, `amazon-product-compliance` | Strukturierte Prompt-Frameworks mit Scoring-Systemen und Report-Formaten | sonnet | Für Merch/Seller-Listing-Texte (Brand, Titel, 2 Bullets, Beschreibung) anpassen |
| 13 | `nospicyplease__amazon-ppc-advanced-skills/amazon-search-term-harvest-planner`, `amazon-ads-performance-drop-diagnosis` | Search-Term-Harvesting mit Evidenz-Schwellen, Drop-Diagnose-Gates, Approval-Queue | sonnet | Für Sponsored-Products auf Merch/Seller-Listings |
| 14 | `mvanhorn__printing-press-library/cli-skills/pp-amazon-ads/SKILL.md` | break-even-acos, true-profit, acos-vs-tacos, portfolio-dashboard aus CSV-Exports | haiku | Royalty-basierte ACOS-Grenze für Merch |
| 15 | `bhavykhatri__amazon-seller-mcp` | Self-hosted SP-API-MCP (Listings/Orders/Reports/Feeds/Pricing), Marktplatz DE konfigurierbar | – | Für FBA/FBM-Hundekleidung neben Merch |
| 16 | `mvanhorn__printing-press-library/cli-skills/pp-printify/SKILL.md` | Manifest-getriebenes Produkt-Anlegen, placement-matrix, product-drift, catalog-margin-matrix, personalization-batch (CSV) | haiku | Bulk-Anlage von Varianten + Margen-Check |
| 17 | `lawrencemq__printipy` + `clintmcmahon__printify-uploader` + `kylemillerbuilds_printify-publish-queue/printify_publish_queue.py` | Python-Client, Ordner→Produkte, gehärteter Publish nach Etsy/Shopify (keine Duplikate) | haiku | Kette für Printify-Pfad |
| 18 | `Purple-Horizons__printful-mcp` (`printful_create_mockup_task`, `printful_get_variant_prices`, `printful_calculate_shipping`) | Printful-Mockups per API, EUR-Preise, Versand nach DE | haiku | Mockup-Generator ohne eigene Rendering-Pipeline |
| 19 | `thieuhoang2002__mockup-forge/engine.py` | Fotorealistische Mockups mit Displacement-/Shadow-Map, CPU-only, Etsy-Bildstandards | haiku (Script) | Ergänzung zu ls-mockup-pipeline für Flatlay-Fotos |
| 20 | `CTDave001__automated_mockups` | Batch Design×Template per Farbplatzhalter, Rotation | haiku | Schnelle Massenmockups |
| 21 | `dhia10__redbubble/modules/trend_detector.py`, `niche_scorer.py`, `seo_generator.py`, `config/prompts.yaml` | Trend-Signale (Google Trends + Redbubble-Trending + Pinterest-Ideas), GPT-Niche-Scoring, 50-Tag-SEO, Prompts mit IP-Vermeidung | sonnet (Scoring), haiku (Scraper) | Pipeline-Skelett für „Trend→Idee→Design→Listing"; Uploader nicht nutzen |
| 22 | `flack0x__trendspyg` bzw. `mvanhorn__printing-press-library/cli-skills/pp-google-trends` | Google-Trends-Daten (Interest, Related/Rising, Region DE) mit Cache | haiku | Saisonale Hunde-/Katzen-Nischen (Weihnachten, Oktoberfest, Halloween) |
| 23 | `ekkolon__gelato-admin-node` / `1nc0gn30__gelato-connector` | Gelato-SDKs (Node/Python) inkl. Länder-Routing und Margen-Engine | – | Nur falls Gelato über TeeInBlue angebunden wird |
| 24 | `semrebayrak__tomescout-claude-plugin/skills/kdp-niche-sizing-by-rank/SKILL.md` | BSR → Tages-/Monatsverkäufe (zwei öffentliche Modelle) | haiku | BSR-zu-Sales-Logik auf Apparel-Kategorie adaptieren |
| 25 | `2scraper__etsy-scraper` | Etsy-Such-/Shop-/Listing-Scraper mit DataDome-Handling | haiku | Konkurrenz-Bestseller-Ledger für Hunde-Apparel |

## Merch by Amazon: alles Gefundene — und was fehlt

**Gefunden (Merch-spezifisch):**
- `AffiliateCoaches__MerchPy` (GPL, Selenium-Uploader, CSV-Schema: Shirt Type, Brand Name, Title, Desc 1, Desc 2, Colors, Fits, Price, File) und `benpearson2003__amathon` (BSD, Selenium-Uploader mit Merch-DOM-IDs, plus `merchify.py` für 4500x5400-Canvas). Beide alt (Selenium-API `find_element_by_id`), beide widersprechen der Merch-FAQ („scripting for bulk upload: No"). Nutzen: nur Feldliste, Canvas-Vorbereitung und als Dokumentation der Upload-Maske.
- Kein einziges SKILL.md, kein Claude-Subagent, kein MCP speziell für Merch on Demand existiert auf GitHub (6 Suchvarianten). Kommerzielle Lösungen (Merch Informer, Merch Titans, MerchGhost, Merch-Check-Extension) sind closed-source.
- `AILabs-official__aws-kdp/.claude/skills/ads-manager/SKILL.md` grenzt sich explizit ab: „You are NOT running Merch on Demand ads — economics and product type are different."

**Gefunden (übertragbar auf Merch):**
- *Research:* nexscope `amazon-niche-finder`/`amazon-trending-products`/`amazon-keyword-research` (Prompt-Frameworks), `pangolinfoapi__amazon-niche-finder` (Blue-Ocean-Score), AILabs `niche-hunter` + `kdp-category-finder` (Datenquellen, Scoring, BSR-Mathematik), `m-murasovs__amazon-bestsellers-scraper` (.de-Bestseller), `eaintkyawthmu__Amazon-Bestseller-Scraper` (Fashion-Bestseller-Seite), Google-Trends-Tools (`trendspyg`, `pp-google-trends`), `dhia10__redbubble/trend_detector.py`.
- *Trademark:* `AILabs-official__aws-kdp/scripts/trademark_check.py` (einziges fertiges „Phrase → Verdict"-Script), `pipeworx-io__mcp-trademarks` (Wortmarken-Suche ohne Key), `riemannzeta__patent_mcp_server`, `pp-uspto-tsdr` (Status/Watch), `jordanburke__trademark-mcp-server` (nur Serial/Reg-Nr.), `apifyforge__euipo-trademark-search` (EUIPO via Apify).
- *Listing/Keywords:* nexscope `amazon-listing-optimization` (428 Z.) und `amazon-backend-keywords`, brianmoney `listing-optimizer`/`keyword-research`, tomescout `keyword_boxes` (Packlogik für Zeichenlimits, Markennamen-Filter — Prinzip identisch mit Merch-Titel 60 Z./Bullets 256 Z.).
- *Ads auf Merch-Listings:* `nospicyplease__amazon-ppc-advanced-skills`, `pp-amazon-ads` (break-even-ACOS), ferrants `amazon-ads-optimization`.
- *Design-Vorbereitung:* `amathon/merchify.py` (Canvas), mockup-forge/automated_mockups (Mockups für Social/Shop, Merch selbst rendert eigene Mockups).

**Was fehlt (nirgends gefunden):**
1. Merch-Tier-Logik (Tier 10/25/100/500…, Slot-Belegung ≥80 %, Batch-Promotion, Upload-Limits pro Tag) — nur Blogartikel, keine Repos/Skills.
2. Merch-Listing-Validator (Titel 60, Brand 50, Bullets 2×256, Beschreibung 2000, verbotene Wörter/Markenwörter, Preis-Royalty-Tabelle nach Marktplatz DE/US/UK) — muss selbst gebaut werden; Vorlage: tomescout `check_listing`/`keyword_boxes`.
3. Merch-Dashboard-Reader (Verkäufe/Royalties/Slots per Browser-Session, wie joshyattridge für KDP) — nicht vorhanden; joshyattridge-Architektur (Playwright-Session + Report-Parser) wäre übertragbar, Policy-Risiko bleibt.
4. Merch-Research-Scraper für amazon.de Novelty-T-Shirt-Suche (BSR, „Lightweight, Classic fit"-Erkennung von Merch-Listings, Brand-Zählung) — nur generische Amazon-Scraper vorhanden.
5. Amazon-Brand-Analytics/Search-Query-Performance für Merch-Accounts — nicht verfügbar (nur Seller-Central-MCPs).
6. EU-/DE-Markenprüfung ohne Apify (EUIPO-API-Client Python, DPMAregister) — nicht gefunden; nur URL-Generierung in `trademark_check.py`.

## Lücken

- **Merch by Amazon:** kein Skill, kein MCP, keine offizielle API; Upload nur manuell oder über riskante Browser-Automation. Tier-Strategie, Listing-Validator und Royalty-Rechner müssen als eigene Skills geschrieben werden.
- **EUIPO/DPMA:** kein Open-Source-Client (nur Apify-Actors, kostenpflichtig). Für eine Deutschland-Marke ist USPTO allein unzureichend; `trademark_check.py` liefert nur manuelle EUIPO-URLs.
- **Spreadshirt/SPOD:** offiziell kein Design-Upload per API; einziges Tool (`runjak__sprd-design-upload`) archiviert. Teepublic/Redbubble nur Selenium-Bots (fragil, ToS).
- **TeeInBlue:** kein öffentlicher API-Client/Skill auf GitHub; Anbindung an Gelato/Printful nur per Dashboard-Key dokumentiert.
- **Pinterest Trends:** kein Open-Source-Zugriff auf trends.pinterest.com; Pinterest-MCPs decken nur API v5 (Pins/Boards/Analytics/Keyword-Suche); `dhia10` scrapt nur /ideas.
- **Etsy-Research ohne eigenen Shop:** eRank-/Marmalead-ähnliche Daten nur über pp-erank-CLI (Katalog, nicht gefunden) oder Scraper (`2scraper__etsy-scraper`).
- **nexscope eCommerce-Skills:** die meisten Etsy-Skills (etsy-print-on-demand, etsy-seo-tags, etsy-keyword-research, etsy-competitor-analysis u.a.) sind 56-Zeilen-Platzhalter ohne Fachinhalt — nicht übernehmen.
- **Hosted-only MCPs:** amz-vault, agentcentral, Kuudo, PPC Prophet, tomescout, kdp-niche-scorer, pipeworx liefern keinen lauffähigen Code; Abhängigkeit von Drittanbietern und Credential-Weitergabe.
- **Mockups auf Hunde-/Katzen-Kleidung:** alle Generatoren sind auf menschliche T-Shirts ausgelegt; Displacement-Maps für Hundeshirts müssten selbst erstellt werden (mockup-forge `generate_assets.py` als Ausgangspunkt).
- **Lizenzlücken:** AILabs aws-kdp, amirjahfar1 Etsy-MCP-Server, BusyBee3333, dhia10, clintmcmahon, winsomeautomation, 1nc0gn30 ohne Lizenzdatei; Umair706 proprietär.

## Quellen

- https://github.com/AffiliateCoaches/MerchPy
- https://github.com/benpearson2003/amathon
- https://github.com/AILabs-official/aws-kdp
- https://github.com/semrebayrak/tomescout-claude-plugin
- https://github.com/ainjection/kdp-niche-scorer-mcp
- https://github.com/nexscope-ai/Amazon-Skills
- https://github.com/nexscope-ai/eCommerce-Skills
- https://github.com/brianmoney/amazon-marketing-skill
- https://github.com/ferrants/amazon-seller-agent-claude-code
- https://github.com/nospicyplease/amazon-ppc-advanced-skills
- https://github.com/bhavykhatri/amazon-seller-mcp
- https://github.com/coaxon/amazon-mcp
- https://github.com/KuudoAI/amazon-selling-partner-mcp
- https://github.com/ppcprophet/amazon-ads-mcp
- https://github.com/TheBurdz/amz-vault-mcp
- https://github.com/agentcentral-to/agent-central-mcp
- https://github.com/pangolinfoapi/amazon-niche-finder
- https://github.com/Umair706/amazon-omniscient
- https://github.com/data-scrape/amazon-product-scraper
- https://github.com/eaintkyawthmu/Amazon-Bestseller-Scraper
- https://github.com/amirjahfar1/Etsy-MCP-Server
- https://github.com/aserper/etsy-mcp
- https://github.com/BusyBee3333/etsy-mcp-2026-complete
- https://github.com/georgejeffers/etsy-mcp-server
- https://github.com/moiz-za/etsy-seller-seo-system
- https://github.com/silennsong/etsy-listing-helper
- https://github.com/robomello/claude-code-setup
- https://github.com/Purple-Horizons/printful-mcp
- https://github.com/five59/pyPrintful
- https://github.com/mdn522/printful-api-python
- https://github.com/TSavo/printify-mcp
- https://github.com/lawrencemq/printipy
- https://github.com/clintmcmahon/printify-uploader
- https://github.com/kylemillerbuilds/printify-publish-queue
- https://github.com/denkan/gelato-api
- https://github.com/ekkolon/gelato-admin-node
- https://github.com/pizzzzzza/printkk-agent-skill
- https://github.com/runjak/sprd-design-upload
- https://github.com/ChristianKnedel/spreadshirt_api_client
- https://github.com/jalbrekt85/Redbubble-Bot
- https://github.com/dhia10/redbubble
- https://github.com/winsomeautomation/teepublic-automation-tool
- https://github.com/thieuhoang2002/mockup-forge
- https://github.com/CTDave001/automated_mockups
- https://github.com/kashifulhaque/product-mockup-node-python
- https://github.com/pipeworx-io/mcp-trademarks
- https://github.com/jordanburke/trademark-mcp-server
- https://github.com/riemannzeta/patent_mcp_server
- https://github.com/parkerhancock/patent-client-agents
- https://github.com/apifyforge/euipo-trademark-search
- https://github.com/mvanhorn/printing-press-library
- https://github.com/flack0x/trendspyg
- https://github.com/yiromo/pytrends-modern
- Sibling-Clones: https://github.com/626Labs-LLC/626labs-pod-pipeline , https://github.com/carlosfrias/presswork-pod , https://github.com/booleandifference/art-factory , https://github.com/1nc0gn30/gelato-connector , https://github.com/altetsa/gelato-mcp-server , https://github.com/madzarm/mcp-server-gelato , https://github.com/rudberga/printful-mcp , https://github.com/jeffkimble/printify-mcp-server , https://github.com/GitStudying/PrintifyProfitCalculator , https://github.com/2scraper/etsy-scraper , https://github.com/scraper-bank/Etsy.com-Scrapers , https://github.com/m-murasovs/amazon-bestsellers-scraper , https://github.com/omkarcloud/amazon-scraper , https://github.com/HasData/google-trends-mcp , https://github.com/cryptoken/GoogleTrendsMCP , https://github.com/pipeworx-io/mcp-google-trends , https://github.com/N-Graves/pinterest-mcp-server , https://github.com/aymandakirgh/pinterest-mcp , https://github.com/what-name/pinterest-mcp , https://github.com/trendsmcp-ai/Trends-MCP , https://github.com/kangise/ecommerce-ai-skills
- Policy-Quelle Merch-Bulk-Upload: Amazon Merch FAQ, zitiert in https://github.com/benpearson2003/amathon (README)
- Nicht-Repo-Quellen aus der Suche (nur zur Einordnung, nicht geklont): https://mcpmarket.com/tools/skills/printify-rest-api-integration , https://mcpmarket.com/tools/skills/niche-scout-for-kdp , https://merchinformer.com/uspto-merch-by-amazon-trademark-tutorial-guide/ , https://developer.spreadshirt.net/ (Public Shop API: kein Design-Upload) , https://merchtitans.com/blog/amazon-merch-tier-10-escape-plan-2026 , https://merchpursuits.com/how-to-tier-up-quickly-with-merch-by-amazon/
