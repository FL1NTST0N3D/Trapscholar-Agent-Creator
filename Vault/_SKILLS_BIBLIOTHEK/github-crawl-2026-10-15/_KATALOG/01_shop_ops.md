# Shopify Store Operations (Lil Snouts, lilsnouts.de)

Domäne: Produkt-/Listing-Management, Katalog, Inventar, Bestell-Triage, Fulfillment, Retouren/Erstattungen, Kundenservice/Helpdesk, Reviews, Richtlinien/Rechtstexte (DE/EU), Theme/Liquid, Shopify Flow, POD-Integrationen (Printful, Printify, Gelato, TeeInBlue, Printy6, Spreadconnect), Versand/Tracking, Rabatte, Scheduled Routines.

Methode: 18 WebSearch-Abfragen (extended), 46 neue Clones, Sichtung der bereits vorhandenen Clones. Alle Angaben unten stammen aus gelesenen Dateien (README, SKILL.md, Tool-Tabellen, Quellbäume). Repos ohne LICENSE-Datei sind als "keine Lizenzdatei" markiert. Alle Pfade sind relativ zu `scratchpad/crawl/repos/`.

Hinweis zur Suche: Das WebSearch-Budget der Session war nach 18 Abfragen erschöpft; zwei geplante Nachsuchen (POD-SKILL.md-Skills jenseits der MCP-Server; "alex-brecher/shopify-multi-store") konnten nicht mehr ausgeführt werden.

## Gecrawlte Repos

Legende Relevanz: 5 = direkt einsetzbar für Vollautomatik, 1 = nur Hintergrund. "Automatisierbar?" = läuft der Inhalt gegen eine API/MCP (ja) oder ist er reine Beratung/Prosa (nein).

| Repo | URL | Lizenz | Inhalt kurz | Anzahl SKILL.md / Agents | Relevanz | Automatisierbar? |
|---|---|---|---|---|---|---|
| 40rty-ai_shopify-admin-skills (vorhanden) | https://github.com/40RTY-ai/shopify-admin-skills | MIT | 116 Skills in 11 Kategorien (customer-support, fulfillment-ops, returns, merchandising, order-intelligence, store-management, finance ...) + 21 Scheduled-Routine-Definitionen (cron + Prompt + genutzte Skills). Jeder Skill: Frontmatter mit `graphql_operations`, `api_version 2025-01`, Parameter-Tabelle inkl. `dry_run`, fertige validierte GraphQL-Queries/Mutationen. Läuft über Shopify CLI `shopify store execute` (AI-Toolkit-Plugin). | 117 SKILL.md, 21 Routines (.md), 0 Agents | 5 | ja (Admin GraphQL via Shopify CLI; 56 Skills mit dry_run) |
| vinceservidad_Shopify-Expert-AI-Skills (vorhanden) | https://github.com/vinceservidad/Shopify-Expert-AI-Skills | MIT | 19 Rollen-Skills (shopify-order-operations, shopify-support, shopify-flow-automation, shopify-catalog-operations, shopify-product-listing, shopify-store-audit, shopify-seo, shopify-cro ...). Reine Arbeitsverträge/Workflows ("Operating contract", "Required inputs", 8-Schritt-Workflow, "Output contract") mit references/ (order-workflows.md, exception-handling.md, automation-patterns.md). Keine GraphQL-Queries, tool-agnostisch. | 19 SKILL.md | 4 | teilweise (Prozessrahmen, braucht MCP/CLI daneben) |
| Shopify__Shopify-AI-Toolkit (neu) | https://github.com/Shopify/Shopify-AI-Toolkit | MIT | Offizielles Plugin: ein konsolidierter Skill `shopify` mit Routing-Tabelle (admin, shopifyql, liquid, custom-data, use-shopify-cli, functions, onboarding-merchant ...), `scripts/search_docs.mjs`, `scripts/validate.mjs` (GraphQL/Liquid/Functions-Validator), `references/use-shopify-cli.md` beschreibt `shopify store auth` / `shopify store execute` (lesend und mit `--allow-mutations`). Telemetrie an shopify.dev, Opt-out per Datei. Ältere Einzel-Skills unter `deprecated/`. | 2 aktive + 21 deprecated SKILL.md | 5 | ja (CLI store execute, Validator) |
| Shopify_agent-skills (vorhanden) | https://github.com/Shopify/agent-skills | keine Lizenzdatei | Ältere, auto-generierte Einzel-Skills (shopify-admin, shopify-liquid, shopify-custom-data, shopify-functions, ...). Pflicht: `/scripts/search_docs.js` vor jeder Antwort. Durch AI-Toolkit abgelöst. | 15 SKILL.md | 3 | ja (Doku-Suche) |
| Shopify__liquid-skills (neu) | https://github.com/Shopify/liquid-skills | keine Lizenzdatei | Claude-Code-Marketplace mit Plugin `liquid-skills`: shopify-liquid-themes, liquid-theme-standards, liquid-theme-a11y (identisch mit benjaminsehl). | 3 SKILL.md | 4 | ja (Theme-Code) |
| benjaminsehl__liquid-skills (neu) | https://github.com/benjaminsehl/liquid-skills | keine Lizenzdatei | Dieselben drei Liquid-Skills (Schema-JSON, LiquidDoc, Filter/Tags/Objects, Standards, A11y). | 3 SKILL.md | 4 | ja |
| baslefeber__shopify-skills (vorhanden, nicht in cloned_list) | https://github.com/baslefeber/shopify-skills | MIT | 8 Theme-Skills: section-builder, seo-structured-data, cro-audit, review-ai-shopify-liquid, accessibility-audit, performance-audit, theme-best-practices, metafields-architect. | 8 SKILL.md | 4 | ja (Theme) |
| tanujrajputdev__shopify-theme-audit-skill (vorhanden, nicht in cloned_list) | https://github.com/tanujrajputdev/shopify-theme-audit-skill | MIT | Theme-Audit mit 80+ Checks (Performance, SEO/AEO/GEO, App-Overhead inkl. Judge.me/Loox), Scoring-Report, Liquid-Fixes. | 1 SKILL.md (+8 Dateien) | 3 | ja (liest Theme-Dateien) |
| kgelster_awesome-ecom-skills (vorhanden) | https://github.com/kgelster/awesome-ecom-skills | MIT | 9 Katalog-Skills: shopify-catalog-audit (read-only FIND), shopify-catalog-cleanup, shopify-seo-metadata, shopify-alt-text, shopify-category-taxonomy, shopify-matrixify (Blank-Cell-Falle, MERGE/REPLACE), shopify-redirect-mapping, shopify-json-ld, ecom-landing-pages. GraphQL gegen Admin API 2025-07, references/queries.md. | 10 SKILL.md | 5 | ja (Admin API / Matrixify) |
| proskillpacks_shopify-store-skills (vorhanden) | https://github.com/proskillpacks/shopify-store-skills | MIT | 5 Skills: review-reply-drafter (eine spezifische Antwort je Review, Flag-Codes SAFETY/LEGAL/MONEY), shopify-policy-checker (holt `/policies/*.json` per `scripts/fetch_policies.py`, prüft Widersprüche), product-title-cleaner, shopify-alt-text-writer, agent-ready-quick-check. | 5 SKILL.md | 4 | teilweise (Policy-Fetch per Script; Review-Antworten sind Entwürfe) |
| finsilabs_awesome-ecommerce-skills (vorhanden) | https://github.com/finsilabs/awesome-ecommerce-skills | MIT | 178 generische E-Commerce-Skills (returns-management, order-fulfillment-workflow, shipment-tracking, customer-support-integration (Gorgias/Zendesk), gdpr-ecommerce, shopify-admin-api, shopify-webhooks, discount-engine, coupon-management ...). Prosa-Playbooks mit Tool-Empfehlungen (Loop Returns, ShipStation), jeweils mit evals/ und tile.json; kaum ausführbare Queries. | 178 SKILL.md | 3 | nein (Beratungstexte), shopify-admin-api-Skill mit Code |
| mardab96_ecommerce-claude-skills (vorhanden) | https://github.com/mardab96/ecommerce-claude-skills | MIT | 20 Analyse-Skills über Exporte: returns-reason-miner, support-ticket-theme-miner, shipping-economics-review, catalog-content-audit, product-feed-qa, weekly-ecommerce-growth-readout. | 20 SKILL.md | 3 | nein (arbeitet auf CSV/Text-Exports) |
| nexscope-ai_eCommerce-Skills (vorhanden) | https://github.com/nexscope-ai/eCommerce-Skills | MIT | 162 kurze "Beta"-Skills (ca. 50-60 Zeilen, Capabilities + Install + Usage-Prompt), u. a. etsy-print-on-demand, ecommerce-returns-management, shopify-inventory-management, review-monitoring. Inhaltlich dünn. | 162 SKILL.md | 2 | nein |
| claude-office-skills_skills / aiLab-2030 (vorhanden, identisch) | https://github.com/claude-office-skills/skills | MIT | 137 Office-Skills; relevant: shopify-automation (519 Zeilen, Frontmatter verweist auf MCP-Server `shopify-mcp` mit Tools shopify_orders/inventory/customers/products), customer-success. | 137 SKILL.md, 7 Agents | 2 | teilweise (setzt eigenen MCP voraus) |
| jezweb_claude-skills (vorhanden) | https://github.com/jezweb/claude-skills | MIT | Plugin `shopify`: shopify-setup (CLI-Auth, api-scopes.md), shopify-products (458 Zeilen: Create/Update/Bulk-CSV, Varianten, Inventar via Admin GraphQL), shopify-content (Pages/Blog/SEO-Meta); 3 Commands. | 63 SKILL.md (3 Shopify), 6 Agents | 4 | ja |
| Jeffallan_claude-skills (vorhanden) | https://github.com/Jeffallan/claude-skills | MIT | shopify-expert (Theme/App/Storefront, references liquid-templating.md, checkout-customization.md). | 67 SKILL.md (1 Shopify) | 2 | ja (Code) |
| Microck_ordinary-claude-skills (vorhanden) | https://github.com/Microck/ordinary-claude-skills | (Sammlung) | shopify-api (837 Zeilen API-Referenz GraphQL/REST/Storefront/Webhooks/Rate-Limits, Version 2025-10), shopify, shopify-debugging, shopify-app-dev. | 4 Shopify-SKILL.md | 3 | ja (Referenz) |
| thatrebeccarae_claude-marketing (vorhanden) | https://github.com/thatrebeccarae/claude-marketing | MIT | shopify (Store-Audit/Conversion/Tracking/Feeds, Marketing-Sicht), klaviyo-analyst, klaviyo-developer. | 56 SKILL.md (1 Shopify) | 2 | teilweise |
| wiebekaai_ecommerce-skills (vorhanden) | https://github.com/wiebekaai/ecommerce-skills | keine Lizenzdatei | shopify-Skill mit `scripts/query.js` / `storefront-query.js` (bun, .env) für beliebige Admin/Storefront-GraphQL-Queries. | 3 SKILL.md | 3 | ja (Script) |
| dainostore_shopify-ai-skills (vorhanden) | https://github.com/dainostore/shopify-ai-skills | keine Lizenzdatei | README verspricht 15 Slash-Commands (/order-autopilot, /bulk-price-update, /margin-analyzer); im Clone liegen nur CLAUDE.md, README.md, setup.cjs – keine SKILL.md, keine commands/. Platzhalter. | 0 | 1 | nein |
| devkindhq__shopifyql-skill (vorhanden, nicht in cloned_list) | https://github.com/devkindhq/shopifyql-skill | MIT | ShopifyQL-Skill + Agent `shopifyql-executor` + Command `shopifyql-setup` (Analytics-Queries, Segment-Filter). | 1 SKILL.md, 1 Agent | 3 | ja |
| simpleproductfeeds__skills (neu) | https://github.com/simpleproductfeeds/skills | MIT | feed-ops Skill für die App "Simple Product Feeds" (Google Merchant Center/CJ-Feeds, Preview-first Writes). App-gebunden. | 1 SKILL.md | 2 | ja (nur mit dieser App) |
| takechanman1228__claude-ecom (neu) | https://github.com/takechanman1228/claude-ecom | (siehe Repo) | Skill `ecom`: Business-Review aus Order-CSV mit gebündelter Python-Engine (KPI-Baum, ~30 Health-Checks). 18 MB wegen assets/. | 1 SKILL.md | 2 | teilweise (CSV-Export) |
| A1-x-Tech__mcp-shopify-admin (neu) | https://github.com/A1-x-Tech/mcp-shopify-admin | MIT | MCP-Server, 16 Tools (get_shop, list/get/create/update_product, update_variant, list/get_orders, cancel_order, list/get_customer, list_locations, set_inventory, Discounts, graphql_request als Escape-Hatch), ein Store pro Server, mintet Token aus Dev-Dashboard Client-ID/Secret (Pflicht für Apps ab 2026-01). Keine Fulfillment-/Refund-Tools. Telemetrie abschaltbar. | MCP (docs/TOOLS.md, docs/capabilities/) | 4 | ja |
| Cesarjoquin__shopify-mcp (neu) | https://github.com/Cesarjoquin/shopify-mcp | MIT | MCP-Server, 40+ Tools laut src/tools: Orders (getOrders, orderCancel, createRefund, getOrderRefundDetails, orderMarkAsPaid, updateOrder, createFulfillment, getFulfillmentOrders), Draft Orders, Inventory (setInventoryQuantities), Products/Variants/Options, Metafields, Customers (merge, addresses), Tags, Markets, PriceLists. Token oder Client-Credentials, API 2026-01, optional Redis. | MCP | 5 | ja (breiteste Abdeckung inkl. Refund/Fulfillment) |
| miller-joe__shopify-mcp (neu) | https://github.com/miller-joe/shopify-mcp | MIT | MCP-Server: Products, Orders, Draft Orders, Inventory, Metafields/Metaobjects, Webhooks, Collections, Variants (bulk), Fulfillment (list/get fulfillment orders, create_fulfillment mit Tracking + notify, update_fulfillment_tracking, cancel_fulfillment), run_shopifyql_query, ComfyUI-Bildbrücke. | MCP | 4 | ja |
| Nextboom-Inc__Shopify-MCP-Server (neu) | https://github.com/Nextboom-Inc/Shopify-MCP-Server | MIT (package.json) | MCP-Server mit Shipping-Profiles (create/update_shipping_rate), Product-Taxonomy, Menus, Publications, Orders (create/update/cancel_order, fulfill_order, create_refund), Files. Client-Credentials-Flow. | MCP | 4 | ja |
| antoineschaller__shopify-mcp-server (neu) | https://github.com/antoineschaller/shopify-mcp-server | MIT | 22 Tools (products, orders inkl. fulfill_order/cancel_order/create_order_note, customers, analytics, create_discount). Älter. | MCP | 3 | ja |
| daanjonk__shopify-mcp (neu) | https://github.com/daanjonk/shopify-mcp | keine Lizenzdatei | Python-MCP (Railway-Deploy), 27 Tools inkl. shopify_create_fulfillment, cancel/close_order, inventory, webhooks. API 2024-10. | MCP | 3 | ja |
| tanush-yadav__shopify-mcp (neu) | https://github.com/tanush-yadav/shopify-mcp | MIT | Kleiner MCP (Products/Orders/Customers Lesen, einfache Filter). | MCP | 2 | ja (lesend) |
| buildwithabid__shopify-mcp (neu) | https://github.com/buildwithabid/shopify-mcp | MIT | Read-only HTTP-MCP: search_orders, get_sales_summary, Inventar, Kunden. Client-Credentials. | MCP | 2 | ja (lesend) |
| krunalp2801__shopify-mcp-server (neu) | https://github.com/krunalp2801/shopify-mcp-server | MIT | Read-only, 5 Tools (shop_info, list/get_orders, list_products, inventory_levels mit belowQuantity), Demo-Fixtures ohne Token. | MCP | 2 | ja (lesend) |
| rushikeshmore__admin-agent (neu) | https://github.com/rushikeshmore/admin-agent | keine Lizenzdatei | Python-MCP "21 Tools": Products, Collections, ShopifyQL-Analytics, Bulk-Operations (submit/status/cancel), safety.py. Keine Order-Tools. | MCP | 2 | ja |
| charlesemarsh__ask-ai-mcp (neu) | https://github.com/charlesemarsh/ask-ai-mcp | keine Lizenzdatei | Nur README + tools.json für gehosteten Dienst (Shopify/Klaviyo/GA4/Gorgias-Daten). Kein Code. | – | 1 | nur über Fremddienst |
| Shopify__claude-for-commerce-examples (neu) | https://github.com/Shopify/claude-for-commerce-examples | Apache-2.0 | Offiziell: `merchant/` = Merchant-Agent über Admin GraphQL (MerchantBackend mit 16 Methoden, stage/approve/apply-Gate, idempotente Inventory-Mutationen, lokaler Stand-in-Store), `storefront/` = Shopping-Agent über UCP. Referenzarchitektur für Freigabe-Gates. | 0 SKILL.md (Python-App) | 4 | ja (Admin API) |
| Shopify__shop-chat-agent (neu) | https://github.com/Shopify/shop-chat-agent | MIT (LICENSE.md) | ARCHIVIERT: Storefront-MCP Catalog/Cart-Tools wurden entfernt; nur noch Referenz. Verweist auf UCP und Customer-Accounts-MCP. | 0 | 1 | nein |
| akallam04__shopify-support-agent (neu) | https://github.com/akallam04/shopify-support-agent | MIT | LangGraph-Support-Agent über eigenen MCP-Server (Admin GraphQL): Cancel, Adresse ändern, Retoure starten; Policy in Code (`mcp_server/policy.py`), Confirmation-Gate (`app/agent/nodes/gate.py`), Fakten-Verifikation, Eval-Harness (gate on: 0/200 ungewollte Änderungen). 28 MB (evals/). | 0 SKILL.md (App) | 4 | ja (Muster + MCP-Code) |
| sengoku-samurai__ecommerce-return-triage-agent (neu) | https://github.com/sengoku-samurai/ecommerce-return-triage-agent | keine Lizenzdatei | n8n-Workflow (workflow.json): Retourenantrag -> LLM-Urteil gegen Policy (approve/escalate + confidence) -> bei <70 Slack-Freigabe -> Shopify-POST; Fehlerzweig mit Reasoning. | 0 (n8n JSON) | 3 | ja (n8n) |
| vinceservidad (s. o.) shopify-flow-automation | – | – | Einzig gefundenes Flow-spezifisches Skill (Spezifikation, Tests, Rollback, keine Flow-Templates). | – | – | – |
| rudberga__printful-mcp (neu) | https://github.com/rudberga/printful-mcp | MIT | Read-only Printful-MCP (GET-only by design): list/get_orders, list/get_store_products, get_catalog_product, generischer `printful_get`; Redaction. Kann keine Bestellung freigeben. | MCP | 4 | ja (lesend, sicher für Monitoring) |
| Purple-Horizons__printful-mcp (neu) | https://github.com/Purple-Horizons/printful-mcp | MIT | Python-MCP, 17 Tools: Katalog/Varianten/Preise/Verfügbarkeit, create_order, confirm_order, list/get_orders, calculate_shipping, create/get_mockup_task, get_file, stores, store_stats, sync_products; enthält `.cursor/skills/printful-mcp/SKILL.md`. | MCP + 1 SKILL.md | 5 | ja (schreibend inkl. Produktion) |
| jeffkimble__printify-mcp-server (neu) | https://github.com/jeffkimble/printify-mcp-server | MIT | TypeScript-MCP: get_shops, get_blueprints/print_providers/variants, upload_image, create_product, publish_product, get_products, get_orders, create_order (laut src/index.ts). | MCP | 4 | ja |
| TSavo__printify-mcp (vorhanden, nicht in cloned_list) | https://github.com/TSavo/printify-mcp | ISC | Printify-MCP mit Produkt-/Katalog-Tools, upload-image, plus Replicate-Bildgenerierung. | MCP | 3 | ja |
| kylemillerbuilds_printify-publish-queue (vorhanden) | https://github.com/kylemillerbuilds/printify-publish-queue | MIT | Python-State-Machine für Printify-Publish (Warten >=5 min, nie re-publish bei locked, DELETE+recreate bei Silent Failure, Cooldown, Verifikation am Zielkanal). Kein Skill, aber Regelwerk. | 0 | 4 | ja (Python) |
| altetsa__gelato-mcp-server (neu) | https://github.com/altetsa/gelato-mcp-server | ISC (package.json) | Gelato-MCP: stores, create_product_from_template (publish zu Shopify), templates, catalog, create/quote/get/search_order. | MCP | 3 | ja |
| madzarm__mcp-server-gelato (neu) | https://github.com/madzarm/mcp-server-gelato | MIT | Python-MCP: search_orders, get_order_summary, Katalog-Ressourcen. Lesend. | MCP | 2 | ja (lesend) |
| 1nc0gn30__gelato-connector (neu) | https://github.com/1nc0gn30/gelato-connector | MIT (package.json) | Gelato Open API v2 Connector + 6 MCP-Tools, Multi-Country-Routing. | MCP | 2 | ja |
| pizzzzzza_printkk-agent-skill / adrianohenriqueuna-pixel (vorhanden) | https://github.com/pizzzzzza/printkk-agent-skill | MIT | 1 SKILL.md für PrintKK-API (Designs, Orders, Images; kein Publishing nach Shopify). Nicht im Lil-Snouts-Stack. | 1 SKILL.md | 1 | ja (nur PrintKK) |
| AfterShip__tracking-and-returns-mcp (neu) | https://github.com/AfterShip/tracking-and-returns-mcp | MIT | Offizieller Remote-MCP + SKILL.md: track_shipment (1.200+ Carrier, Auto-Erkennung, ohne API-Key), get_returns_demo. | MCP + 1 SKILL.md | 4 | ja |
| pocharlies__mcp-17track (neu) | https://github.com/pocharlies/mcp-17track | MIT (package.json) | 17Track-MCP (Free-Tier), DHL/DPD/GLS/Hermes-fähig laut Beschreibung; nur ARCHITECTURE.md, kein README. | MCP | 3 | ja |
| benbonn__utapimcp (neu) | https://github.com/benbonn/utapimcp | MIT | DHL Unified Tracking API MCP (track-shipment, API-Key), Azure/Copilot-Template, 8 MB. | MCP | 3 | ja (DHL-direkt) |
| mattcoatsworth__Gorgias-MCP-Server (neu) | https://github.com/mattcoatsworth/Gorgias-MCP-Server | keine Lizenzdatei | Gorgias-MCP: list/get/create_ticket, add_message_to_ticket, list/get_customer (API-Key/OAuth). | MCP | 3 | ja |
| fabiogermann__zendesk-mcp-server (neu) | https://github.com/fabiogermann/zendesk-mcp-server | MIT | Zendesk-MCP: Tickets end-to-end (create/update, public reply, internal note, triage, Attachments), Help-Center-Artikel drafting/translate, Remote-HTTP-Modus. | MCP | 3 | ja |
| wlaubernds__zendesk-mcp-server (neu) | https://github.com/wlaubernds/zendesk-mcp-server | MIT | Zendesk-MCP: search_tickets, get_ticket, search/get_article, get_tickets_by_tag. | MCP | 2 | ja (überwiegend lesend) |
| lxhelili__dsgvo-audit (neu) | https://github.com/lxhelili/dsgvo-audit | MIT | Skill `dsgvo-audit` (Law-Stand 2026-09) + Agent `dsgvo-auditor` (model: opus): DSGVO/TDDDG/DDG-Audit mit Scannern (`scripts/lint-origins.mjs`, `scan-origins.mjs`), references (checklist, patterns, services, recht, gesundheit), Templates für Datenschutzerklärung/Impressum/Consent, deutscher Report mit RDG-Hinweis; evals/. | 1 SKILL.md, 1 Agent | 4 | teilweise (Scanner ja, Texte = Entwurf) |
| waldo-van-der-code__gdpr-dsgvo-audit (neu) | https://github.com/waldo-van-der-code/gdpr-dsgvo-audit | MIT | 4 Skills: gdpr-dsgvo (Audit + document-templates.md), shop-check (Impressum DDG §5, Button-Lösung §312j, PAngV, Widerrufsbelehrung, AGB; Modi scan/audit/draft), widerruf (Art. 7(3) Consent-Widerruf, nicht Waren-Widerruf), bfsg. Nutzt `rechtsinformationen-bund-de`-MCP wenn vorhanden. | 4 SKILL.md | 4 | teilweise (WebFetch-Scan; Texte = Entwurf) |
| patrickstigler__claude-skill-it-recht-dsgvo (neu) | https://github.com/patrickstigler/claude-skill-it-recht-dsgvo | MIT + Commons Clause | Skill `anwalt-de`: Ersteinschätzung IT-Recht/DSGVO/AGB/Impressum/UWG, references (checklisten, dsgvo, it-recht, vertragsrecht). Keine Textgenerierung als Kernfunktion. | 1 SKILL.md | 2 | nein |
| Klotzkette__claude-fuer-deutsches-recht__trimmed (neu, auf 13 MB getrimmt; Original 2,4 GB gelöscht) | https://github.com/Klotzkette/claude-fuer-deutsches-recht | Apache-2.0 / MIT (dual) | Behalten: Plugins `ecommerce-recht` (ca. 80 Skills: widerrufsrecht-verbraucher-355-312g-bgb, widerrufsbelehrung-digitale-waren-dienstleistungen, retourenmanagement-wertersatz, textilkennzeichnung-lmiv-trusted-flagger, preisangaben-pangv-produktbewertungen-ranking, rabatte-streichpreise, newsletter-double-opt-in, impressum-ddg-influencer-affiliate, button-loesung-312j-bgb, odr-verbraucherstreitbeilegung-hinweis, produktsicherheit-gpsr-onlinehandel, kundenservice-chatbot-lieferzeiten, livecheck-bgb-uwg-ddg-dsa-pangv, red-team-shop-vor-launch ...), `verbraucherschutzrecht-pruefer`, `agb-recht-pruefer`, `datenschutzrecht` (285 Skills), `produktrecht`, `influencer-recht`, `fashion-law-moderecht`. Skills sind kurz (ca. 50-110 Zeilen), Normenanker + generischer "Arbeitsweg" (Live-Prüfung auf gesetze-im-internet.de), Prüfprodukt mit Risiko. Experimentell, keine Rechtsberatung. | >900 SKILL.md im Trim (Gesamt-Repo 23.278) | 3 | nein (Prüfraster; keine API) |
| rdwz__dsgvo-generator (neu) | https://github.com/rdwz/dsgvo-generator | licence.txt (siehe Repo) | Web-Generator (JS) für Datenschutzerklärungs-Text AT/DE; Textbausteine in src/. Kein Skill. | 0 | 2 | nein (Textquelle) |
| domocarroll__shopify-builds (neu) | https://github.com/domocarroll/shopify-builds | keine Lizenzdatei | 6 Claude-Code-Agents (shopify-liquid-dev, shopify-api-dev (model: sonnet), shopify-content-dev, shopify-functions-dev, shopify-hydrogen-dev, shopify-qa). | 6 Agents | 3 | ja (Dev) |
| sarojpunde__shopify-dev-toolkit-claude-plugins (neu) | https://github.com/sarojpunde/shopify-dev-toolkit-claude-plugins | keine Lizenzdatei | Marketplace: shopify-theme-development (6 Skills, 5 Agents: liquid-specialist, section-builder, translation-manager ...), shopify-polaris, shopify-app-development. | 11 SKILL.md, 16 Agents | 3 | ja (Dev) |
| henkisdabro__wookstar-claude-plugins (neu) | https://github.com/henkisdabro/wookstar-claude-plugins | MIT | 33 Plugins; relevant shopify-developer (Branch-Tabelle, Pin API-Version, Validierung über AI-Toolkit/dev-mcp), google-analytics, google-tagmanager, humanise, message. | 25 SKILL.md (1 Shopify) | 2 | ja (Dev) |
| moVictor99__shopify-theme-builder (neu) | https://github.com/moVictor99/shopify-theme-builder | MIT | Interview-first Skill: komplettes OS-2.0-Theme bauen (theme-check-clean, bilingual/RTL). | 1 SKILL.md | 2 | ja (Theme-Neubau; für Live-Pflege unnötig) |
| SaadBenhmid__shopify-store-builder-skill (neu) | https://github.com/SaadBenhmid/shopify-store-builder-skill | keine Lizenzdatei | Store-Builder über proprietären "StorePipe MCP"; 17 Shopify-Gotchas, Pre-Deploy-Checkliste. | 1 SKILL.md | 2 | nur mit StorePipe |
| HemeraOne__awesome-agentic-commerce (neu) | https://github.com/HemeraOne/awesome-agentic-commerce | CC0 | Linkliste (UCP, ACP, AP2, Shopify-Repos, paypal/agent-toolkit, punkpeye/awesome-mcp-servers). Keine neuen POD/Shop-Ops-Skill-Repos. | 0 | 1 | – |
| efegokdemir__awesome-shopify (neu) | https://github.com/efegokdemir/awesome-shopify | CC0 | Linkliste; Abschnitt "AI, MCP & Agents" nur offizielle Shopify-Doku-Links. | 0 | 1 | – |
| ylnhari__openclaw-skills (neu) | https://github.com/ylnhari/openclaw-skills | MIT | Nur ein Skill (medium-blog-post-creator). Irrelevant. | 1 | 1 | – |
| claude-market__marketplace (neu) | https://github.com/claude-market/marketplace | (siehe Repo) | Kein Shopify-/E-Commerce-Inhalt (nur ein DB-Plan erwähnt e-commerce-schema). | 0 relevant | 1 | – |

Nicht erreichbar (Clone fehlgeschlagen, vermutlich gelöscht/privat): apexradius/shopify-admin-mcp, Jasuni69/printful-mcp-server, amanamabasiakpan/ecommerce-skills, amir-bengherbi/shopify-mcp.
Nicht gefunden (kein GitHub-Treffer in 18 Suchen): TeeInBlue-API/-MCP (TeeInBlue hat keine öffentliche API-Doku; Orders aus Shopify-Produkten bekommen laut teeinblue.com nur eine Design-URL angehängt), Spreadconnect/Spreadshirt-MCP, Printy6-Integration, Judge.me-/Loox-Review-Reply-Automation als Skill, Shopify-Flow-Template-Sammlung als Skill.

## Top-Skills zum Übernehmen

Modell-Stufen: haiku = Grundarbeit (lesende Reports, Datenabzug, Formatierung), sonnet = Standard (Entwürfe, Katalog-Pflege mit dry_run, Routing), opus = Entscheidung (Geld, Recht, irreversible Mutationen, Kundenfreigaben).

1. `40rty-ai_shopify-admin-skills/skills/customer-support/shopify-admin-order-lookup-and-summary/SKILL.md` – vollständige Bestell-Zusammenfassung (Status, Tracking, Refunds) per validierter GraphQL-Query; Basis jeder WISMO-Antwort. Warum: fertige Query, read-only, Scopes read_orders/read_customers. Stufe: haiku.
2. `40rty-ai_shopify-admin-skills/skills/customer-support/shopify-admin-wismo-bulk-status-report/SKILL.md` – findet Bestellungen mit stalem Tracking (>5 Tage) und unfulfilled > SLA (3 Tage). Warum: proaktive Ticket-Vermeidung, direkt als Routine nutzbar. Stufe: haiku.
3. `40rty-ai_shopify-admin-skills/skills/fulfillment-ops/shopify-admin-fulfillment-status-digest/SKILL.md` – tägliche Fulfillment-Triage mit Alters-Buckets und ON_HOLD-Erkennung über fulfillmentOrders. Warum: zeigt POD-Verzögerungen (TeeInBlue/Printful) ohne Admin-UI. Stufe: haiku.
4. `40rty-ai_shopify-admin-skills/skills/customer-support/shopify-admin-refund-and-reorder/SKILL.md` – refundCreate (voll/teil) + optional draftOrderCreate als Ersatzbestellung, dry_run, Safety-Block ("refundCreate cannot be undone"). Warum: einziger gefundener Skill mit kompletter Refund-Mutation + Ersatzlogik. Stufe: opus (Freigabe), Ausführung danach sonnet.
5. `40rty-ai_shopify-admin-skills/skills/customer-support/shopify-admin-return-initiation/SKILL.md` – returnCreate mit Return-Reasons (SIZE_TOO_SMALL, WRONG_ITEM, DEFECTIVE ...), prüft FULFILLED, notify_customer-Schalter. Warum: nativer Retourenprozess für Widerrufe. Stufe: opus (Entscheidung ob Retoure/Wertersatz), sonnet für Ausführung.
6. `40rty-ai_shopify-admin-skills/skills/fulfillment-ops/shopify-admin-tracking-update-bulk/SKILL.md` und `.../shopify-admin-bulk-fulfillment-creation/SKILL.md` – fulfillmentUpdate/Tracking in Masse, Fulfillment anlegen. Warum: wenn TeeInBlue/Printful Tracking nicht zurückschreibt. Stufe: sonnet.
7. `40rty-ai_shopify-admin-skills/skills/customer-support/shopify-admin-address-correction/SKILL.md` – Adresskorrektur vor Produktion. Stufe: sonnet.
8. `40rty-ai_shopify-admin-skills/routines/fulfillment-sla-watchdog.md`, `.../morning-store-briefing.md`, `.../low-stock-watchdog.md`, `.../catalog-health-weekly.md`, `.../return-fraud-watch.md`, `.../fraud-sentinel.md`, `.../price-anomaly-scanner.md` – fertige Cron+Prompt-Definitionen (Frontmatter routine_id/cron/skills_used/notify) für Claude-Code-Scheduled-Tasks. Warum: 1:1 als Scheduled-Routine-Prompts übernehmbar (Store-Domain und Slack->Gmail/Notiz tauschen). Stufe: haiku für Reports, sonnet für Routinen mit Mutationen.
9. `40rty-ai_shopify-admin-skills/skills/merchandising/shopify-admin-product-data-completeness-score`, `.../shopify-admin-seo-metadata-audit`, `.../shopify-admin-product-image-audit`, `.../shopify-admin-collection-membership-audit`, `.../shopify-admin-product-tag-bulk-update`, `.../shopify-admin-variant-option-normalizer` – Katalog-Hygiene mit GraphQL. Warum: ergänzt den vorhandenen shopify-manager-Skill mit konkreten Queries. Stufe: haiku (Audit), sonnet (Bulk-Update mit dry_run).
10. `40rty-ai_shopify-admin-skills/skills/store-management/shopify-admin-url-redirect-audit`, `.../shopify-admin-discount-hygiene-cleanup`, `.../shopify-admin-page-content-audit`, `.../shopify-admin-staff-account-audit` – Redirects nach Handle-Änderung, abgelaufene Rabattcodes, Seiteninhalte. Stufe: haiku/sonnet.
11. `40rty-ai_shopify-admin-skills/docs/skill-template.md` + `docs/graphql-operations-index.md` – Vorlage/Index zum Schreiben eigener Skills im gleichen Format (graphql_operations, Parameter, Safety). Stufe: –.
12. `vinceservidad_Shopify-Expert-AI-Skills/skills/shopify-order-operations/SKILL.md` + `references/order-workflows.md`, `references/exception-handling.md` – Operating-Contract für Bestelländerungen (read-only Start, Re-Read vor Ausführung, Timeout = Outcome unknown, kein "resolved" ohne Verifikation). Warum: als Leitplanken-Text für den Order-Agenten über die 40rty-Skills legen. Stufe: opus für Entscheidungsschritte.
13. `vinceservidad_Shopify-Expert-AI-Skills/skills/shopify-support/SKILL.md` + `references/response-guidelines.md`, `references/faq-framework.md` – Support-Antworten nur aus verifizierten Fakten, Holding-Reply bei fehlender Evidenz, Eskalationsliste (Chargeback, Fraud, Privacy). Stufe: sonnet (Entwurf), haiku (Makro-Fälle).
14. `vinceservidad_Shopify-Expert-AI-Skills/skills/shopify-flow-automation/SKILL.md` + `references/automation-patterns.md`, `references/examples.md` – Trigger-Condition-Action-Spezifikation, Duplikat-/Retry-/Rollback-Design, Testmatrix. Warum: einziges Flow-Skill; dient zum Entwerfen der Shopify-Flow-Automationen (Tagging, Benachrichtigung), die Claude nicht selbst anlegen kann. Stufe: sonnet.
15. `vinceservidad_Shopify-Expert-AI-Skills/skills/shopify-catalog-operations/SKILL.md` (+ references/bulk-operations.md, worked-example.md) – Bulk-Katalog-Governance (Backup-Export, Pilot-Batch, Dry-Run-Diff, Reconciliation). Stufe: sonnet.
16. `kgelster_awesome-ecom-skills/skills/shopify-catalog-audit/SKILL.md` (+ references/triage-method.md, queries.md) – read-only Katalog-Audit mit deterministischem Index statt PDP-Lesen. Stufe: haiku.
17. `kgelster_awesome-ecom-skills/skills/shopify-redirect-mapping/SKILL.md` – 301-Mapping nach Handle-/URL-Änderung (passt zu shopify-live-pflege "Titel/Handle mit Redirect"). Stufe: sonnet.
18. `kgelster_awesome-ecom-skills/skills/shopify-seo-metadata/SKILL.md`, `.../shopify-alt-text/SKILL.md`, `.../shopify-category-taxonomy/SKILL.md`, `.../shopify-matrixify/SKILL.md` – SEO-Backfill ohne Überschreiben menschlicher Texte, Taxonomie-IDs, Matrixify-Sicherheitsdoktrin. Stufe: sonnet.
19. `proskillpacks_shopify-store-skills/skills/review-reply-drafter/SKILL.md` + `references/flags-and-patterns.md` – je Review eine spezifische Antwort, Flags SAFETY/LEGAL/MONEY-dispute -> Holding-Reply + interne Notiz, Banned-Phrases. Warum: Judge.me/Loox-Antworten vorbereiten (Posten bleibt manuell/API). Stufe: sonnet.
20. `proskillpacks_shopify-store-skills/skills/shopify-policy-checker/SKILL.md` + `scripts/fetch_policies.py` – holt `/policies/*.json` + FAQ/Versand-Seiten, findet Lücken/Widersprüche zu Banner-Claims ("kostenloser Versand", "30 Tage"). Warum: wöchentlicher Konsistenz-Check der Richtlinien auf lilsnouts.de. Stufe: haiku (Fetch), sonnet (Bewertung).
21. `jezweb_claude-skills/plugins/shopify/skills/shopify-products/SKILL.md` + `shopify-setup/references/api-scopes.md` – Produkt-Create/Update/Bulk-CSV mit Varianten/Inventar via Admin GraphQL, Scope-Liste. Stufe: sonnet.
22. `Shopify__Shopify-AI-Toolkit/skills/shopify/SKILL.md` + `references/use-shopify-cli.md`, `references/admin.md`, `references/shopifyql.md`, `references/liquid.md` + `scripts/validate.mjs` – offizieller Weg: GraphQL validieren, dann `shopify store execute --store ... --query ...` (Mutationen nur mit `--allow-mutations`). Warum: Laufzeit-Basis für alle 40rty-Skills; Liquid-Validator für Theme-Änderungen. Hinweis: Telemetrie an shopify.dev (Opt-out-Datei setzen). Stufe: haiku (Lookup/Validate), sonnet (Code).
23. `Shopify__liquid-skills/plugins/liquid-skills/skills/shopify-liquid-themes/SKILL.md`, `liquid-theme-standards`, `liquid-theme-a11y` – Liquid-Sprache, Schema-JSON, Standards, A11y. Warum: für Theme-Code-Änderungen in shopify-live-pflege. Stufe: sonnet.
24. `baslefeber__shopify-skills/skills/review-ai-shopify-liquid/SKILL.md`, `shopify-cro-audit`, `shopify-section-builder`, `shopify-metafields-architect` – Review von KI-generiertem Liquid (Money-Filter, Inline-Style-Falle), CRO-Audit. Stufe: sonnet.
25. `Cesarjoquin__shopify-mcp` (MCP-Server) – breitester Community-MCP inkl. createRefund, createFulfillment, getFulfillmentOrders, orderCancel, setInventoryQuantities, mergeCustomers; Alternative zum CLI-Weg, wenn Admin-GraphQL als MCP gewünscht ist (das Session-interne Shopify-MCP hat bereits graphql_query/graphql_mutation). Stufe: –.
26. `Purple-Horizons__printful-mcp/.cursor/skills/printful-mcp/SKILL.md` + Server – Printful-Katalog, Preise in EUR, calculate_shipping, create/confirm_order, Mockup-Tasks. Warum: Fallback-Fulfillment/Mockups, falls Lil Snouts Printful direkt nutzt. Für reines Monitoring sicherer: `rudberga__printful-mcp` (GET-only). Stufe: sonnet (Mockup/Quote), opus (confirm_order).
27. `jeffkimble__printify-mcp-server` (upload_image, create_product, publish_product, create_order) + `kylemillerbuilds_printify-publish-queue/README.md` (Publish-State-Machine: 5 Minuten warten, nie re-publish bei locked, DELETE+recreate, Cooldown) – Regeln beim Printify-Publish nach Shopify übernehmen. Stufe: sonnet, Regeln als Hard-Gates.
28. `AfterShip__tracking-and-returns-mcp/skills/tracking-and-returns/SKILL.md` – track_shipment ohne API-Key, Fallback-URL `aftership.com/track/{nr}`. Warum: Tracking-Status für WISMO-Antworten. Alternativ `benbonn__utapimcp` (DHL-direkt, API-Key) oder `pocharlies__mcp-17track`. Stufe: haiku.
29. `waldo-van-der-code__gdpr-dsgvo-audit/skills/shop-check/SKILL.md` – Prüfmatrix Impressum (DDG §5), Button-Lösung (§312j), PAngV, Widerrufsbelehrung, AGB mit Modi `scan <url>` / `draft <typ>`; `skills/gdpr-dsgvo/references/document-templates.md` für Datenschutz-Textbausteine. Warum: deutschsprachige Shop-Rechtsprüfung, auf lilsnouts.de direkt anwendbar. Stufe: opus (Rechtstexte), haiku (Scan).
30. `lxhelili__dsgvo-audit/skills/dsgvo-audit/SKILL.md` + `agents/dsgvo-auditor.md` + `references/checklist.md`, `services.md`, `patterns.md`, `scripts/scan-origins.mjs` – technischer DSGVO/TDDDG-Audit (Klaviyo, Meta-Pixel, Fonts, Consent-Gating), Report in Deutsch, Templates Datenschutzerklärung/Impressum. Stufe: opus (Agent ist bereits `model: opus`).
31. `Klotzkette__claude-fuer-deutsches-recht__trimmed/ecommerce-recht/skills/widerrufsrecht-verbraucher-355-312g-bgb/SKILL.md`, `retourenmanagement-wertersatz`, `textilkennzeichnung-lmiv-trusted-flagger` (Textilkennzeichnungs-Pflicht für Apparel), `preisangaben-pangv-produktbewertungen-ranking`, `rabatte-streichpreise-rechtsabteilung-cross` (Streichpreise/Omnibus), `newsletter-double-opt-in-einwilligung`, `odr-verbraucherstreitbeilegung-hinweis`, `produktsicherheit-gpsr-onlinehandel`, `livecheck-bgb-uwg-ddg-dsa-pangv`, `red-team-shop-vor-launch` – deutsche Normenanker + Prüfraster je Thema. Warum: Checklisten-Basis für Rechtstexte und Rabatt-Kommunikation; Skills sind kurz und generisch, liefern aber die richtigen Paragraphen. Stufe: opus.
32. `akallam04__shopify-support-agent/mcp_server/policy.py`, `app/agent/nodes/gate.py`, `app/agent/nodes/verify.py` (nur lesen, nicht ausführen) – Muster: Policy in Code, Confirmation-Gate, Fakten-Verifikation gegen Store-Daten; Eval zeigt Gate-off 42/200 ungewollte Änderungen vs. Gate-on 0/200. Warum: Architekturvorlage für den Support-Agenten (Haiku für Routing/Antworten reicht laut Repo). Stufe: Design-Referenz.
33. `Shopify__claude-for-commerce-examples/merchant/README.md` + `merchant/api/` – offizielles stage/approve/apply-Gate über Admin GraphQL (Staging schreibt nichts, Apply genau eine Mutation, idempotente Inventory-Mutationen auf API 2026-07). Stufe: Design-Referenz.
34. `sengoku-samurai__ecommerce-return-triage-agent/workflow.json` + README – Retouren-Triage-Muster: Urteil + Confidence, <70 -> menschliche Freigabe, Fehlerzweig mit Reasoning. Stufe: Muster für opus-Entscheidungsschritt.
35. `mardab96_ecommerce-claude-skills/returns-reason-miner-ecommerce/SKILL.md`, `support-ticket-theme-miner-ecommerce/SKILL.md` – wöchentliche Auswertung von Retouren-/Ticket-Exports zu Produktseiten-Fixes (Größentabelle, Erwartungen). Stufe: sonnet.
36. `finsilabs_awesome-ecommerce-skills/skills/customer-crm/customer-support-integration/SKILL.md`, `fulfillment-shipping/returns-management`, `shipment-tracking`, `security-compliance/gdpr-ecommerce`, `platform-shopify/shopify-webhooks` – Hintergrund-Playbooks (Gorgias-Makros, RMA-Logik, Art. 17/20-Workflows, Webhook-Themen). Stufe: haiku als Nachschlagewerk.

## Lücken (muss selbst geschrieben werden)

1. **TeeInBlue-Operations-Skill**: Kein Repo, kein MCP, keine API-Doku auf GitHub. TeeInBlue-Bestellungen aus Shopify-Produkten erhalten nur eine Design-URL; Fulfillment-Status, Druckdatei-Prüfung, Kampagnen-/Artwork-Pflege müssen per Browser/Export (eigener `teeinblue-ops`-Skill existiert bereits lokal) abgebildet werden. Fehlt: Abgleich Shopify-Order <-> TeeInBlue-Produktionsstatus <-> Tracking.
2. **Spreadconnect/Spreadshirt und Printy6**: keine MCP-Server, keine Skills gefunden. Falls genutzt: REST-Wrapper + Skill selbst schreiben.
3. **Deutsche Rechtstexte als fertige Generatoren**: Es gibt Prüfraster (waldo shop-check, Klotzkette, lxhelili) und Datenschutz-Templates, aber keinen Skill, der ein komplettes DE-Shop-Paket (Impressum, Widerrufsbelehrung inkl. Muster-Widerrufsformular, AGB für POD-Personalisierung mit §312g Abs. 2 Nr. 1 BGB-Ausnahme für personalisierte Ware, Versand-/Zahlungsinfos, ODR/VSBG-Hinweis, Textilkennzeichnung) erzeugt und in Shopify `shopPolicyUpdate` schreibt. Für Lil Snouts besonders: Personalisierte Hunde-Shirts -> Ausnahme vom Widerrufsrecht sauber formulieren.
4. **Review-Automation Judge.me/Loox**: nur Entwurfs-Skill (proskillpacks). Fehlt: Abruf neuer Reviews über Judge.me-API, Antwort posten, Bewertungsanfragen auslösen.
5. **Gmail-basierter Helpdesk-Flow**: Gorgias/Zendesk-MCPs existieren, für Gmail (Lil Snouts) gibt es nur das Session-MCP. Fehlt: Skill "Support-Inbox-Triage" = Gmail-Thread lesen -> Order-Lookup (40rty) -> Tracking (AfterShip) -> Antwort-Entwurf (vinceservidad shopify-support) -> Label/Draft; Identitätsprüfung (E-Mail = Order-E-Mail); Eskalationsregeln (Chargeback, Rechtliches).
6. **Retouren-/Erstattungs-Policy-Engine für POD**: Entscheidungslogik (Druckfehler/Beschädigung -> Ersatz ohne Rücksendung; falsche Größe bei personalisierter Ware -> Kulanz-Rabatt statt Widerruf; Nichtzustellung -> Carrier-Nachforschung) als Policy-in-Code (Muster akallam04) + Shopify-Mutationen (40rty refund/return) + TeeInBlue-Nachproduktion.
7. **Shopify-Flow-Vorlagen**: nur Design-Skill (vinceservidad). Fehlt: konkrete Flow-Rezepte für Lil Snouts (Order-Tagging nach POD-Partner, Hold bei Adressfehlern, Benachrichtigung bei >48h unfulfilled), als Liquid/Flow-JSON-Spezifikation.
8. **Routinen-Adapter**: 40rty-Routinen notifizieren nach Slack und setzen eine 40rty-Demo-Domain; Anpassung auf Gmail/Artifact-Log, lilsnouts.de, EUR/DE-Carrier (DHL, Hermes, DPD) und DE-Feiertage nötig.
9. **Discount-/Preis-Routine mit Omnibus-/PAngV-Regel**: 40rty hat Discount-ROI und Promo-Code-Generator, aber keine Prüfung "30-Tage-Niedrigstpreis bei Streichpreisen" (PAngV §11). Muss mit Klotzkette-Normenanker selbst gebaut werden.
10. **Tracking-Rückschreibung von POD nach Shopify**: 40rty tracking-update-bulk kann Tracking setzen; fehlt die Quelle (TeeInBlue/Printful-Export -> Mapping -> fulfillmentUpdate) als End-to-End-Skill.
11. **Inventory bei POD**: Shopify-Inventory-Skills sind für Lagerware; für POD braucht es "Verfügbarkeit beim Drucker" (Printful get_product_availability existiert) als Routine, die Varianten bei Blank-Out-of-Stock auf Draft setzt.

## Quellen

GitHub-Repos (gecrawlt):
- https://github.com/40RTY-ai/shopify-admin-skills
- https://github.com/vinceservidad/Shopify-Expert-AI-Skills
- https://github.com/Shopify/Shopify-AI-Toolkit
- https://github.com/Shopify/agent-skills
- https://github.com/Shopify/liquid-skills
- https://github.com/benjaminsehl/liquid-skills
- https://github.com/baslefeber/shopify-skills
- https://github.com/tanujrajputdev/shopify-theme-audit-skill
- https://github.com/kgelster/awesome-ecom-skills
- https://github.com/proskillpacks/shopify-store-skills
- https://github.com/finsilabs/awesome-ecommerce-skills
- https://github.com/mardab96/ecommerce-claude-skills
- https://github.com/nexscope-ai/eCommerce-Skills
- https://github.com/claude-office-skills/skills
- https://github.com/jezweb/claude-skills
- https://github.com/Jeffallan/claude-skills
- https://github.com/Microck/ordinary-claude-skills
- https://github.com/thatrebeccarae/claude-marketing
- https://github.com/wiebekaai/ecommerce-skills
- https://github.com/dainostore/shopify-ai-skills
- https://github.com/devkindhq/shopifyql-skill
- https://github.com/simpleproductfeeds/skills
- https://github.com/takechanman1228/claude-ecom
- https://github.com/A1-x-Tech/mcp-shopify-admin
- https://github.com/Cesarjoquin/shopify-mcp
- https://github.com/miller-joe/shopify-mcp
- https://github.com/Nextboom-Inc/Shopify-MCP-Server
- https://github.com/antoineschaller/shopify-mcp-server
- https://github.com/daanjonk/shopify-mcp
- https://github.com/tanush-yadav/shopify-mcp
- https://github.com/buildwithabid/shopify-mcp
- https://github.com/krunalp2801/shopify-mcp-server
- https://github.com/rushikeshmore/admin-agent
- https://github.com/charlesemarsh/ask-ai-mcp
- https://github.com/Shopify/claude-for-commerce-examples
- https://github.com/Shopify/shop-chat-agent
- https://github.com/akallam04/shopify-support-agent
- https://github.com/sengoku-samurai/ecommerce-return-triage-agent
- https://github.com/rudberga/printful-mcp
- https://github.com/Purple-Horizons/printful-mcp
- https://github.com/jeffkimble/printify-mcp-server
- https://github.com/TSavo/printify-mcp
- https://github.com/kylemillerbuilds/printify-publish-queue
- https://github.com/altetsa/gelato-mcp-server
- https://github.com/madzarm/mcp-server-gelato
- https://github.com/1nc0gn30/gelato-connector
- https://github.com/pizzzzzza/printkk-agent-skill
- https://github.com/AfterShip/tracking-and-returns-mcp
- https://github.com/pocharlies/mcp-17track
- https://github.com/benbonn/utapimcp
- https://github.com/mattcoatsworth/Gorgias-MCP-Server
- https://github.com/fabiogermann/zendesk-mcp-server
- https://github.com/wlaubernds/zendesk-mcp-server
- https://github.com/lxhelili/dsgvo-audit
- https://github.com/waldo-van-der-code/gdpr-dsgvo-audit
- https://github.com/patrickstigler/claude-skill-it-recht-dsgvo
- https://github.com/Klotzkette/claude-fuer-deutsches-recht
- https://github.com/rdwz/dsgvo-generator
- https://github.com/domocarroll/shopify-builds
- https://github.com/sarojpunde/shopify-dev-toolkit-claude-plugins
- https://github.com/henkisdabro/wookstar-claude-plugins
- https://github.com/moVictor99/shopify-theme-builder
- https://github.com/SaadBenhmid/shopify-store-builder-skill
- https://github.com/HemeraOne/awesome-agentic-commerce
- https://github.com/efegokdemir/awesome-shopify
- https://github.com/ylnhari/openclaw-skills
- https://github.com/claude-market/marketplace

Suchtreffer/Sekundärquellen (nicht geklont, nur zur Einordnung):
- https://www.get-ryze.ai/blog/claude-shopify-skills
- https://www.get-ryze.ai/blog/claude-skills-every-shopify-merchant-should-set-up
- https://www.skillsdirectory.com/skills/alex-brecher-shopify-multi-store-shopify-multi-store
- https://ecosire.com/blog/openclaw-shopify-store-skill-build-tutorial
- https://lobehub.com/skills/openclaw-skills-clawver-print-on-demand
- https://lobehub.com/skills/openclaw-skills-openclaw-commerce-shopify
- https://www.sarasanalytics.com/blog/zendesk-mcp-gorgias-mcp
- https://github.com/activepieces/activepieces/pull/16087
- https://github.com/majiayu000/claude-skill-registry (nicht geklont: Registry mit shopify-theme-dev-Skill)
- https://teeinblue.com/pages/integrations, https://teeinblue.com/pages/shopify (keine öffentliche API-Doku)
- https://www.shopify.com/de/tools/richtlinien-generator
- https://code.claude.com/docs/en/sub-agents
