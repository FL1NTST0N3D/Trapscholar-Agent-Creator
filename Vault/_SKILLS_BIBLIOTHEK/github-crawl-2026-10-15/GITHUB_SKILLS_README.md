# GitHub-Skill-Bibliothek fuer Lil Snouts Vollautomatik (Stand 2026-10-15)

Quelle: 10x-Deepcrawl ueber GitHub (8 Domaenen, 9 parallele Crawl-Agenten, ~520 Repos geklont, 5.809 Skills + 25 Agent-Definitionen aus 237 Repos uebernommen). Auftrag Phil 15.10.: "zieh dir mal skills aus github fuer e commerce ad scaling designing print on demand amazon MBA ... 10x deepcrawl", "voll automatisierbare skills + agents fuer alles was wir brauchen", "agenten architektur sehr wichtig ... passende modelle fuer grundwork ... bei entscheidungen das groesste", "alles durchscannen bevors losgeht".

## Aufbau
```
github-crawl-2026-10-15/
  GITHUB_SKILLS_README.md   <- diese Datei (Einstieg, Top-Picks)
  INDEX.md / _KATALOG/index.json  <- alle 5.809 Skills mit Pfad, Beschreibung, Lizenz (INDEX.md 1,4 MB: nur greppen, nie ganz lesen)
  _KATALOG/0[1-8]_*.md      <- je Domaene: Repo-Tabelle, Top-Skills, Zahlen/Regeln mit Quellpfad, Luecken, Quellen
  _KATALOG/SCAN_BERICHT.md  <- Sicherheits-Scan (REAL-Treffer, geloeschte Dateien, Lizenzliste)
  _KATALOG/scan_skills.py, index_skills.py, copy_to_vault.py  <- Werkzeuge fuer Nachcrawls
  01_shop_ops/ 02_paid_ads/ 03_pod_marketplaces/ 04_design/ 05_social/ 06_email_cro_seo/ 07_agent_arch/ 08_research_data/
      <owner>__<repo>/<skill-ordner>/SKILL.md (+ references, scripts)   README + LICENSE je Repo
```
Regeln fuer den Einsatz: `_SKILLS_BIBLIOTHEK/_eigene_entwuerfe/ls-skill-sicherheitsregeln/SKILL.md` (nur lesen, kein Skript blind, Rang Phil > Vault-Regeln > eigene Skills > Fremd-Skills). Modell je Aufgabe: `Vault/00_SYSTEM/agent-architektur/ARCHITEKTUR.md`.

## Top-Picks je Domaene (Relevanz 5, Details im jeweiligen Katalog)

### 01 Shop-Betrieb (`_KATALOG/01_shop_ops.md`)
- `40rty-ai__shopify-admin-skills` (MIT): 117 Skills mit validierten Admin-GraphQL-Operationen + dry_run, 21 Scheduled-Routinen (Fulfillment-SLA, Fraud, Customer Health). Grundlage fuer `ls-support`, Shopify-Manager.
- `vinceservidad__Shopify-Expert-AI-Skills`: Operating-Contracts fuer order-operations, support, flow-automation, catalog-operations.
- `kgelster__awesome-ecom-skills`: catalog-audit, redirect-mapping, seo-metadata, alt-text, Matrixify-Regeln.
- `akallam04__shopify-support-agent`, `Shopify__claude-for-commerce-examples`: Policy-in-Code + Confirmation-Gate (stage/approve/apply) = unser Dry-Run-Muster.
- DE-Recht: `waldo-van-der-code__gdpr-dsgvo-audit` (Impressum/Button-Loesung/PAngV/Widerruf), `lxhelili__dsgvo-audit`, `Klotzkette__claude-fuer-deutsches-recht__trimmed` (Widerruf 355/312g, Textilkennzeichnung, Streichpreise).
- Luecke: TeeInBlue hat keinen oeffentlichen Client -> bleibt `teeinblue-ops`.

### 02 Paid Ads (`_KATALOG/02_paid_ads.md`, Abschnitt "Skalierungsregeln mit Zahlen")
- `tenfoldmarc__meta-ads-launch-skill/optimizer.md`: Scheduled-Optimizer, Baender r = CPA/Target (WIN <= 1,0 / CLOSE <= 1,3 / OFF <= 1,5 / WAY_OFF > 1,5), Phasen nach Kampagnenalter, Strike-Logik, CUT (0 Conv & Spend >= 1x Target oder CPA > 1,5x & Spend >= 2x), +20 % Scale mit 3-Tage-Cooldown, Approval-JSON.
- `coreyhaines31_marketingskills/skills/ads/references/meta-decision-system.md` + `meta-andromeda-playbook.md` + `ad-creative/references/hook-system.md`: TCPL-Gate (3x Target), 80/20 Scaling/Testing-CBO, Frequency-Baender, Rollback > 1,5x.
- `sepivip__meta-ads-skill`: Tool-Vertraege fuer den offiziellen Meta-Ads-MCP (Cent-Budgets, Targeting-JSON, keine Budgetfelder unter CBO).
- `gushchinda__meta-ads-skills`: Cron-Loop (Poisson-Kill aus LTV, +/-15 %/Tag nach Predicted ROAS).
- `mardab96__tiktok-ads-claude-skills`, `marcelfelixbaur__tiktok-ad-compliance` (EU: 30-Tage-Preisregel, AI-Act).
- Fusion der widerspruechlichen Schwellen (10-15 %/48 h vs 20 %/3-5 d vs +/-15 %/Tag) steht im Katalog; unsere Vault-Fassung `ads-skalierung` bleibt massgeblich, Katalog liefert Belege.

### 03 POD & Marktplaetze (`_KATALOG/03_pod_marketplaces.md`)
- Merch by Amazon: KEIN Skill/MCP auf GitHub, Bulk-Upload verboten -> eigener Skill `_eigene_entwuerfe/ls-merch-by-amazon-de`. Bausteine: `AILabs-official__aws-kdp` (trademark_check.py USPTO+Trademarkia, niche-hunter mit 9 Datenquellen), `pipeworx-io__mcp-trademarks`.
- Etsy: `amirjahfar1__Etsy-MCP-Server` (~90 Tools + 29 Skills), `moiz-za__etsy-seller-seo-system`, `silennsong__etsy-listing-helper` (POD-Spec -> Listing). nexscope-Etsy-Skills sind grossteils Platzhalter.
- Printful `Purple-Horizons__printful-mcp` (Mockup-Tasks, EUR-Preise), Printify `TSavo__printify-mcp`, `kylemillerbuilds__printify-publish-queue`, Gelato-SDKs; `thieuhoang2002__mockup-forge` (Displacement-Mockups CPU-only).
- Amazon: `nexscope-ai__Amazon-Skills` (53), `nospicyplease__amazon-ppc-advanced-skills` (Approval-Queue), `bhavykhatri__amazon-seller-mcp` (SP-API DE).

### 04 Design & Aesthetik (`_KATALOG/04_design_aesthetik.md`, "Master-Designer: die besten 10")
- `anthropics__skills/skills/frontend-design` + `canvas-design` (Zwei-Pass, Tells-Liste), `Leonxlnx__taste-skill` (Studie 247 Sites, datiertes Tells-Register, brandkit-Bildprompt), `MengTo__skills` (no-ai-design-slop + illustration-* inkl. vintage-emblem mit 7-Farben-Lint), `jiji262__claude-design-skill/references/design-principles.md`, `crizex__art-director` (persistentes taste.md), `Nutlope__hallmark` (study = DNA-Extraktion aus Screenshots), `miqdadbadjuber__anti-slop`, `b1rdmania__claude-brand-skills`, `pbakaus__impeccable`, `designrique__ai-graphic-design-skill`.
- POD-Pipeline-Muster: `626Labs-LLC__626labs-pod-pipeline` (Gemini ohne Text -> qa.py Slop-Gate -> CV-Freistellung -> PIL-Typo -> Varianten -> Printify, human-gated), `carlosfrias__presswork-pod`.
- Bildgen-Prompting: `kingbootoshi__nano-banana-2-skill`, `jlouage__Nano-Banana-Pro-Claude-Skills`, `devkindhq__ideogram-ai-toolkit`, `justinperea__midjourney-cc-skill`; Farbe `meodai__skill.color-expert`.
- Referenz-Analyse: `Manavarya09__design-extract`, `kalilfagundes__design-system-extractor-skill`, `bubucilo__social-audit`.
- Kein GitHub-Skill kodiert DTG/DTF/AOP-Regeln fuer Apparel -> `_eigene_entwuerfe/ls-master-designer-aesthetik` Abschnitt 8 + `omd-bauweise`.

### 05 Social (`_KATALOG/05_social_media.md`, "Vollautomatik-Pipeline")
- `social-media-skills__skills` (106, MIT), `sergebulaev__instagram/tiktok/youtube/facebook-skills` (Publora-Publish, Apify-Research, Approval-Gate in lib/approval.py), `ScrapeCreators__social-media-research-skills` (Outlier/Comment-Mining/Teardown), `gitroomhq__postiz-agent` (offizielle CLI+MCP, 28 Kanaele; Plugin postiz:postiz ist im Konto).
- Video: `johannships__reels-engine` (Cron-Pipeline mit QA-Gates), `retrogtx__ai-marketing-videos` (Remotion-Produkt-Ads), `kajisho5__ffmpeg-skill`, `heygen-com__skills` (DE/EN-Dubbing).
- Luecken: kein DACH-Skill, Comment/DM-Automation nur als Apps, Pinterest/TikTok-Direktpublish braucht eigene App.

### 06 E-Mail, CRO, SEO (`_KATALOG/06_email_cro_seo.md`, "Benchmarks")
- `CosmoBlk__email-marketing-bible` (Send-Gates, Thresholds: Complaint >= 0,1 % blockt; Klaviyo-2026-RPR je Flow), `thatrebeccarae__claude-marketing/skills/klaviyo-analyst` (Audit, analyze.py), `jasoncarrigan__ecom-klaviyo-email-skill` (Produktlink -> Klaviyo-Draft), `scalably-io__klaviyo-mcp` (read-only Reporting).
- CRO mit DOI-Belegen: `checkout-page__ecommerce-skills` (Guest-Checkout +45 %, Quantity-CTA +14 % CVR, Cart-Mail 24-72 h), `llizell__pdp-audit`, `Ads-insights__landingpage-cro-audit-kit`.
- SEO/GEO: `AgriciDaniel__claude-seo`, `aretenia__geo-skills`, `seranking__seo-skills`, `kgelster` shopify-seo-metadata/json-ld.
- Luecken: nichts DE/DE-Recht, kein getesteter Klaviyo-Flow-JSON-Skill, MER wird nirgends berechnet (-> `ads-roas-rechner`, `ls-finance`).

### 07 Agenten-Architektur & Token (`_KATALOG/07_agent_architektur_tokens.md`, [DOC]/[REPO]/[BLOG] markiert)
- Docs (verifiziert): `model:` Frontmatter sonnet|opus|haiku|fable|ID|inherit; Aufloesung Invocation > Frontmatter > CLAUDE_CODE_SUBAGENT_MODEL > Hauptmodell; Sparfelder effort/maxTurns/omitClaudeMd/autoCompactWindow; Agent Teams ~7x Token; Scheduled Tasks senden vollen Kontext; CLAUDE.md < 200 Zeilen.
- Muster: `michael-harris__claude-code-multi-agent-dev-system` (Escalation haiku->sonnet->opus), `TurboKach__claude-code-setup` (Rolle->Modell), `pejmanjohn__slot-machine` (Best-of-N + Judge), `fltman__loop-engineer` (Cost-Gating), `anthropics__commerce-agents` (Staged Changes + Approval), `affaan-m__everything-claude-code` (token-optimization, strategic-compact, council).
- Token: `juliusbrussee__caveman` (einzige mit externem A/B: -33 % Input), `rtk-ai__rtk`, `egorfedorov__claude-context-optimizer`, `ryoppippi__ccusage`, Hooks `karanb192__claude-code-hooks`, `kenryu42__cc-safety-net`.

### 08 Research, Daten, Finance (`_KATALOG/08_research_data_finance.md`)
- Competitor-Komplettabzug in 9 Ebenen: `zhaoheng588-tech__shopify-scout` (products.json), `dembrandt__dembrandt`/`yuvrajangadsingh__brandmd`/`arvindrk__extract-design-system` (Design-System), `RamsesAguirre777__facebook-ads-library-mcp` (EU liefert alle Ads, ohne Token), ScrapeCreators/Apify (IG/TikTok/Reviews), `0-shiv__secondstep-claude-skills` competitor-analysis (9 Sub-Skills).
- Finance: `mardab96__ecommerce-claude-skills` (margin_stack.py CM2/CM3 + BE-ROAS je SKU, cohort_read.py), `Jakeschincariol__founder-skill` (unit_economics.py), `EveryInc__charlie-cfo-skill` (LTV >= 3x CAC, Payback < 12 Mo), `deanpeters` finance-metrics-quickref (CM < 40 % kritisch).
- Offers: `itsfromgaurav__grand-slam-offer-skill`, `alexsmedile__hormozi-skills`. Scraping: `firecrawl__skills`, `lancelin111__crawl4ai-skill`, `apify__awesome-skills`, `lackeyjb__playwright-skill`.
- Luecken: Pinterest-Trends/TikTok Creative Center nur bezahlt (Apify), Etsy blockt Datacenter-IPs, kein POD-Unit-Economics-Modell (TeeInBlue/Marketprint, USt, Textil-Retouren) -> `ls-finance` parametrisiert.

## Eigene Skills aus dem Crawl (`_SKILLS_BIBLIOTHEK/_eigene_entwuerfe/`)
ls-shop-vollautomatik-leitstand, ls-skill-sicherheitsregeln, ls-master-designer-aesthetik, ls-design-referenz-crawl, ls-merch-by-amazon-de. Agenten: `Vault/.claude/agents/ls-*.md` (15, mit model-Frontmatter).

## Nachcrawl
`_KATALOG/copy_to_vault.py` + `scan_skills.py` + `index_skills.py`; Ablauf: clone --depth 1 -> scan -> selection.json -> copy -> index -> SKILL_ZUORDNUNG-Zeile. Vollstaendige Repo-Liste des Crawls (520) in `_KATALOG/cloned_list.txt`.
