# Design & Ästhetik (Master-Designer, Brand, Textil-/Print-Design, Bildgenerierung, Design-Research)

Stand: 2026-10-15. Crawl-Agent Domäne 04. Basis: 26 WebSearch-Abfragen (extended), 46 neu geklonte Repos plus Inspektion von 15 bereits vorhandenen Repos. Alle Pfade unterhalb von
`/tmp/claude-0/-home-user-Trapscholar-Agent-Creator/565203ac-a19a-5fc6-82c5-f701b96a51c7/scratchpad/crawl/repos/` (im Folgenden `REPOS/`).

Hinweis zur Verifikation "OMD = Oh My Dog": konnte nicht verifiziert werden, das Suchbudget war vor der Prüfung aufgebraucht. In den gecrawlten Repos kommt weder "OMD" noch "Oh My Dog" vor; Heybalu und Petprinted ebenfalls nicht. Es gibt auf GitHub kein Skill/Agent, der speziell Pet-Portrait-Apparel-Marken analysiert.

## Gecrawlte Repos

Relevanz = 1-5 für Textildesign + Brand (Lil Snouts). Automatisierbar = kann headless in einer Pipeline laufen (Skripte/CLI/API) vs. reine Prompt-/Judgement-Skill.

| Repo | URL | Lizenz | Inhalt kurz | Anzahl Skills/Agents | Relevanz | Automatisierbar? |
|---|---|---|---|---|---|---|
| anthropics/skills (vorhanden) | https://github.com/anthropics/skills | Apache (README), Skill-LICENSE.txt je Skill | Offizielle Skills: frontend-design (Anti-Slop-Designleitung), canvas-design (Design-Philosophie -> visuelles Artefakt), brand-guidelines (Anthropic-Farben), algorithmic-art | 20 Skills | 4 | Nein (Judgement) |
| jiji262/claude-design-skill (vorhanden) | https://github.com/jiji262/claude-design-skill | MIT | Portierter Claude-Design-Systemprompt: Design-Direction-Advisor, Core-Asset-Protokoll, Anti-Slop-Regeln, Craft-/Content-Regeln | 1 Skill + references/ | 4 | Nein |
| designrique/ai-graphic-design-skill (vorhanden) | https://github.com/designrique/ai-graphic-design-skill | MIT | Logo/Brand mit KI: Tool-Matrix (Recraft/MJ/SD/Firefly), Prompt-Formeln, Vektorisierungs-Pipeline, Mockup (Displacement Maps), Lieferformate (DPI/CMYK), IP-Safety. Portugiesisch | 1 Skill (366 Zeilen) | 5 | Teilweise (Python-Pipeline Abschnitt 9) |
| b1rdmania/claude-brand-skills (vorhanden) | https://github.com/b1rdmania/claude-brand-skills | MIT (README, keine LICENSE-Datei) | 8-Phasen-Brand-System (Emotive Narrative -> DESIGN.md), Art-CLI (nano-banana-pro/flux/gpt-image, --remove-bg, --reference-image), Konvergenz-Essay ADDENDUM-4 | 4 Skills, 9 Workflows | 5 | Teilweise (Generate.ts CLI) |
| bergside/awesome-design-skills (vorhanden) | https://github.com/bergside/awesome-design-skills | MIT | 67 Stil-Skills (artistic, colorful, vintage, riso, retro, neobrutalism ...) je mit DESIGN.md | 67 Skills / 67 DESIGN.md | 3 | Nein |
| VoltAgent/awesome-design-md (vorhanden) | https://github.com/VoltAgent/awesome-design-md | MIT | 84 DESIGN.md realer Marken (nike, starbucks, airbnb, shopify, mydealz ...) im Stitch-Format | 84 DESIGN.md | 3 | Nein |
| VoltAgent/awesome-claude-design (NEU) | https://github.com/VoltAgent/awesome-claude-design | MIT | Nur README: Liste von 68 DESIGN.md-Inspirationen (verweist auf awesome-design-md) | 0 | 1 | Nein |
| Digiflex-solution/awesome-design-md (NEU) | https://github.com/Digiflex-solution/awesome-design-md | MIT | Fork/Mirror von VoltAgent (identische Lizenz), keine eigenen Skills | 0 | 1 | Nein |
| rohitg00/awesome-claude-design (vorhanden) | https://github.com/rohitg00/awesome-claude-design | MIT | Awesome-Liste: DESIGN.md nach Ästhetik-Familie, Video-Teardowns, Links zu externen Katalogen | 0 Skills (Linkliste) | 2 | Nein |
| pbakaus/impeccable (vorhanden) | https://github.com/pbakaus/impeccable | Apache-2.0 | 1 Skill, 24 Commands (critique, audit, polish, bolder, typeset, colorize ...), 59 deterministische Detektor-Regeln, Agents (asset-producer, finish-reviewer) | 25 SKILL.md-Kopien, 4 Agents | 3 | Ja (CLI-Detektor ohne LLM) |
| nextlevelbuilder/ui-ux-pro-max-skill (vorhanden) | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | MIT | UI/UX-Suite; relevant: banner-design (Safe-Zones, max 2 Fonts, 4.5:1 Kontrast), brand (Scripts: inject-brand-context, validate-asset, extract-colors) | 13 Skills | 3 | Teilweise (Node-Scripts) |
| MengTo/skills (vorhanden) | https://github.com/MengTo/skills | MIT | 176 Skills; relevant: no-ai-design-slop, audit-ai-design-slop, 14 illustration-* Stile als handgeschriebene SVG (vintage-emblem = Siebdruck-Badge), generate-reference-inspired-brand-worlds, daily-ui-inspiration-capture | 176 Skills | 4 | Teilweise (lint.mjs, wordmark.mjs) |
| contains-studio/agents (vorhanden) | https://github.com/contains-studio/agents | MIT (README) | 37 Subagents; design/: brand-guardian, visual-storyteller, ui-designer, whimsy-injector | 37 Agents | 2 | Nein |
| msitarzewski/agency-agents (vorhanden) | https://github.com/msitarzewski/agency-agents | MIT | 308 Agent-Personas; design/: brand-guardian, image-prompt-engineer (Foto-Terminologie), ui-finish-gate-reviewer | 308 Agents | 2 | Nein |
| transitive-bullshit/skills (vorhanden) | https://github.com/transitive-bullshit/skills | MIT | 96 kuratierte Skills (mit provenance/): unslop, better-typography, better-colors, midjourney-images (Web-App-Bedienung), branding-exercise (3 Richtungen + SVG-Poster) | 96 Skills | 3 | Teilweise |
| nidhinjs/prompt-master (vorhanden) | https://github.com/nidhinjs/prompt-master | MIT | Generischer Prompt-Schreiber mit Tool-Profilen (u. a. Midjourney) | 1 Skill | 2 | Nein |
| coreyhaines31/marketingskills (vorhanden) | https://github.com/coreyhaines31/marketingskills | MIT | skills/image: Modellvergleich (Nano Banana/Flux/Ideogram), Ansatzwahl (AI-Gen vs Canva vs Screenshot+Overlay); skills/ad-creative mit static-ad-templates | 50 Skills | 3 | Teilweise |
| crizex/art-director (NEU) | https://github.com/crizex/art-director | MIT | Persönlicher Art Director: taste.md/log.md/references/ außerhalb des Skills, Quellenrotation, Richtungen als Bilder, "measure against the bar", Slop-Detektor früh laufen lassen | 1 Skill + 2 Scripts | 4 | Teilweise |
| hcaiano/skills (NEU) | https://github.com/hcaiano/skills | MIT | art-director: 3-5 Richtungen mit je eigener Kompositionsregel, Breite -> Kuratieren -> 1 Trait pro Iteration ändern -> Systemboard beweisen; no-slop (deprecated) | 17 Skills | 3 | Nein |
| Leonxlnx/taste-skill (NEU) | https://github.com/Leonxlnx/taste-skill | MIT | tasteskill v2 (Studie von 247 Gallery-Sites, draw.mjs verteilt 3 von 20 Richtungen, inspect.mjs misst im Browser, tells.md datiertes Register), brandkit (Brand-Board-Bildgenerierung), imagegen-frontend-web, image-to-code, redesign, output | 14 Skills, 1 DESIGN.md | 4 | Ja (Node 22 + Chromium) |
| paulltalk/anti-slop (NEU) | https://github.com/paulltalk/anti-slop | MIT (Copyright Miqdad Badjuber) | Identischer Inhalt wie miqdadbadjuber/anti-slop (Mirror) | 6 Skills | 3 | Nein |
| miqdadbadjuber/anti-slop (NEU) | https://github.com/miqdadbadjuber/anti-slop | MIT | antislop core + ui + copywriting + layoutmobile + human + code; jede Regel als Tell/Why/Fix mit R-XX-Referenz, Delivery Gate | 6 Skills | 3 | Nein |
| Nutlope/hallmark (NEU) | https://github.com/Nutlope/hallmark | MIT | Anti-Slop-Skill mit Verben audit/redesign/study; 21 Makrostrukturen, 57 Slop-Gates, 6 Disziplinen (Pre-emit Self-Critique 1-5, Locked Tokens, keine italic Headlines), study = DNA-Extraktion aus URL/Screenshot | 1 Skill (558 Zeilen) + references | 4 | Nein |
| wwewtech/anti-slop-design (NEU) | https://github.com/wwewtech/anti-slop-design | MIT | Banned Matrix (12 Tropes), Axiome (1-zu-3-Regel, 85%-Priorisierung), 8 Cures inkl. Visual-DNA-Ingestion aus Screenshots, Physical-vs-Digital-Asset-Regel | 2 Skills | 3 | Nein |
| danielrosehill/Claude-Digital-Printing-Plugin (NEU) | https://github.com/danielrosehill/Claude-Digital-Printing-Plugin | MIT | PDF-Druckvorstufe: add-bleed (3 mm), verify-bleed-safe, downsample-images (300 DPI, Ghostscript), normalize-color-profile (sRGB/CMYK FOGRA39), embed-fonts, flatten-transparency, print-prep-orchestrator Agent. v1 nur PDF | 21 Skills, 1 Agent | 3 | Ja (gs/pdfimages) |
| danielrosehill/Claude-Image-Production-Plugin (NEU) | https://github.com/danielrosehill/Claude-Image-Production-Plugin | MIT | Bildproduktion: vectorize (vtracer), upscale-image, svg-to-raster, web-ready, auto-deskew, ai-graphics, scrub-metadata | 29 Skills | 4 | Ja |
| realproject7/svgsmith (NEU) | https://github.com/realproject7/svgsmith | FSL-1.1-MIT (Functional Source License, MIT nach 2 Jahren) | Selbstverifizierender Raster->SVG-Vektorisierer (VTracer/Potrace, --transparent-background, --flatten-shading, --detail poster) als CLI + Skill | 1 Skill | 4 | Ja |
| justinperea/midjourney-cc-skill (NEU) | https://github.com/justinperea/midjourney-cc-skill | MIT | Midjourney V7 Wissensbasis + lernende Session-DB (schema.sql), Übersetzungstabellen Qualität->Keyword, optionale Playwright-Automation. 75 MB (docs/) | 1 Skill | 3 | Teilweise |
| avienor/midjourney-prompts (NEU) | https://github.com/avienor/midjourney-prompts | KEINE Lizenzdatei | MJ V8.x / Niji 7 Prompts: Modellwahl-Tabelle, Charakter-Konsistenz (Edit Model, srefs), official.md vs community.md getrennt | 1 Skill | 3 | Nein |
| kingbootoshi/nano-banana-2-skill (NEU) | https://github.com/kingbootoshi/nano-banana-2-skill | MIT | Gemini-Image-CLI (Bun): 512-4K, `-t` Green-Screen -> FFmpeg colorkey+despill -> transparentes PNG, Referenzbilder, Style Transfer | 1 Skill | 4 | Ja |
| maciejdzierzek/nano-banana-prompt-generator (NEU) | https://github.com/maciejdzierzek/nano-banana-prompt-generator | MIT | Prompting-Guide Nano Banana 2 / 2 Lite / Pro (Modell-IDs, Deprecations, Formeln), kein Generator | 1 Skill (563 Zeilen) | 3 | Nein |
| devonjones/devon-claude-skills (NEU) | https://github.com/devonjones/devon-claude-skills | MIT | nano-banana Plugin: generate_image.py / compose_images.py (bis 14 Referenzen), Product-Mockup-Workflow; Rest unrelated | 11 Skills, 6 Agents | 3 | Ja |
| jlouage/Nano-Banana-Pro-Claude-Skills (NEU) | https://github.com/jlouage/Nano-Banana-Pro-Claude-Skills | MIT | Gemini-Image-Skill mit Presets (product 2K 1:1 Studio, social-story, banner, illustration), Cost-Controls | 1 Skill | 3 | Ja |
| damiansire/generate-nanobanana (NEU) | https://github.com/damiansire/generate-nanobanana | MIT | Nano Banana 2 Lite/Pro + Omni Flash Video, Cost-Gate vor bezahlten Runs, Prompt-Log neben jeder Datei | 1 Skill | 3 | Ja |
| 0-to-1-Labs/gemini (NEU) | https://github.com/0-to-1-Labs/gemini | MIT | Gemini-Suite: nanobanana (Prompt-Enhancement), veo, lyria, tts, understand, omni | 6 Skills | 2 | Ja |
| AbdulkareemKR/brand-identity-generator (NEU) | https://github.com/AbdulkareemKR/brand-identity-generator | MIT | Komplette Brand-Guideline als 16:9-HTML-Deck -> PDF, 3 Modi (from scratch / vom Logo / von Website), process_logo.py (Mark isolieren, Weißvariante, Palette samplen), KI-Mockups via OpenAI | 1 Skill | 4 | Teilweise |
| cofoundy/brand-skills (NEU) | https://github.com/cofoundy/brand-skills | MIT | 16 Brand-Skills um brand.yaml: brand-init, brand-strategy, brand-identity (Visual Brief), competitor-branding, naming, brand-voice, brand-guidelines, rebranding | 16 Skills | 4 | Nein |
| arnabbagxd/Brand-building-skills (NEU) | https://github.com/arnabbagxd/Brand-building-skills | MIT | 29 Brand-/Marketing-Skills (brand-identity, brand-packaging, d2c-marketing, competitor-branding, ugc-strategy); überlappt cofoundy | 29 Skills | 3 | Nein |
| fatihaydost/brand-identity-skill (NEU) | https://github.com/fatihaydost/brand-identity-skill | MIT | Brand-Sets (Logo+Type+Palette gemeinsam) mit Mess-Skripten (brand.py: Kontrast, Farbenblindheit, Glyph-Coverage, Font-Lizenzen, Kleinst-Logo-Render), `site extract` | 1 Skill + Scripts | 4 | Ja (Python/uv) |
| motiful/product-shots (NEU) | https://github.com/motiful/product-shots | MIT | 1 Produktfoto -> Main Image, A+ Detail, 9-Winkel-Lookbook (Fashion-on-Model), Social Post, Ad Creative (Plattformmaße, Safe Zones, Banned-Words-Filter für Bildprompts) | 7 Skills | 4 | Ja (Image-Gateway) |
| veryCoolTimo/imagegen-skills (NEU) | https://github.com/veryCoolTimo/imagegen-skills | MIT | image-prompt: 9-Block-Skelett (benannte Zonen, Hex-Palette, echte Fonts, IP-Safety), Archetypen (poster/product-ad/logo/illustration), Model-Adapter gpt-image-2/FLUX.2/Recraft V4/Ideogram v4 | 1 Skill | 4 | Nein |
| eachlabs/skills (NEU) | https://github.com/eachlabs/skills | MIT (README), keine LICENSE-Datei | 102 Skills um bezahlte each::sense API: tshirt-design-generation (Druckverfahren-Tabelle), pet-portrait-generation, sticker-design-generation, seamless-pattern-generation, product-photo, meta-ad-creative, logo-generation | 102 Skills | 4 (Inhalt) / 2 (API-Lock-in) | Ja (bezahlte API) |
| inference-sh/skills (vorhanden, anderer Agent) | https://github.com/inference-sh/skills | MIT (README) | guides/design: logo-design-guide, email-design, og-image, youtube-thumbnail, book-cover, character-design-sheet; API-gebunden | 86 Skills | 2 | Ja (API) |
| Manavarya09/design-extract (NEU) | https://github.com/Manavarya09/design-extract | MIT | `npx designlang <url> --screenshots`: 8 Output-Dateien (Design-Language-MD, Tailwind, shadcn, Figma-Variables, W3C-Tokens), /battle Vergleich, /remix, Gallery mit 24 vorextrahierten Sites | 25 SKILL.md (1 Haupt + 24 Gallery), 24 Agents | 4 | Ja (Playwright) |
| kalilfagundes/design-system-extractor-skill (NEU) | https://github.com/kalilfagundes/design-system-extractor-skill | MIT (README), keine LICENSE-Datei | Reverse-Engineering Design-System von URL: Python-Preprozessor (Token-Limit-sicher) -> HTML-Doku | 1 Skill (1223 Zeilen) | 3 | Ja (Python) |
| nhatmobile1/color-palette-skill (NEU) | https://github.com/nhatmobile1/color-palette-skill | MIT | Paletten gegen generische KI-Ästhetik: kuratierte Domänen-Paletten, WCAG-Validator, Harmonie-Scripts (komplementär/triadisch), 50-950-Skalen | 1 Skill + Scripts | 3 | Ja |
| OneWave-AI/claude-skills (NEU) | https://github.com/OneWave-AI/claude-skills | MIT | 232 Skills; relevant: color-palette-extractor (K-Means aus Bild/Website), brand-consistency-checker, claude-design-critic, design-system-generator, stock-photo-finder | 232 Skills | 2 | Teilweise |
| meodai/skill.color-expert (NEU) | https://github.com/meodai/skill.color-expert | CC-BY-4.0 | Farbwissen (180+ Referenzdateien): OKLCH-Rampen, APCA/WCAG, Pigmentmischung, Farbnamen, Print vs Screen | 1 Skill | 3 | Nein |
| devkindhq/ideogram-ai-toolkit (NEU) | https://github.com/devkindhq/ideogram-ai-toolkit | Apache-2.0 | 16 Ideogram-MCP-Skills: logo-prompting (Anti-Slop-Disziplin), seamless-pattern-texture-generator (Tile-Rezept + visuelle Verifikation), brand-identity-sheet, moodboard, concept-grid, character-model-sheet, custom-model-training | 16 Skills | 4 | Ja (Ideogram MCP) |
| han669669/meta-ads-static-creator (NEU) | https://github.com/han669669/meta-ads-static-creator | KEINE (README: Skill von Joey Mulcahy "ohne seine Erlaubnis" veröffentlicht) | Referenz-Ad -> textfreie Foto-Platte (fal/Replicate) + editierbare Text-/UI-Layer (compose-text.py, layers-to-html.py), 4:5 + 9:16; brand-Skill baut Markenprofil von Website | 2 Skills | 4 (Inhalt) / Lizenzrisiko | Ja |
| gushchinda/meta-ads-skills (NEU) | https://github.com/gushchinda/meta-ads-skills | MIT | generate-creatives (Nano Banana, Meta-Maße 9:16/4:5/1:1, Text-Verifikationspass), deploy-creatives, creative-testing, predict | 9 Skills | 3 | Ja |
| Creatify-AI/static-ad-concept-generator (NEU) | https://github.com/Creatify-AI/static-ad-concept-generator | MIT | 320+ Ad-Konzept-Templates (Angle/Headline/Visual/CTA), 16 universelle Angles; Produktion via Creatify-API | 1 Skill | 3 | Nein |
| alirezarezvani/claude-skills (NEU) | https://github.com/alirezarezvani/claude-skills | MIT | 846 SKILL.md (viele Harness-Kopien); design-relevant nur ad-creative, brand-guidelines, design-system, ui-design-system (generisch) | 846 Skills, 281 Agents | 1 | Nein |
| rampstackco/claude-skills (vorhanden, anderer Agent) | https://github.com/rampstackco/claude-skills | MIT | 309 Website-Lifecycle-Skills; brand-discovery, brand-ideation, brand-archetype-system, brand-style-guide, logo-design, design-standards | 309 Skills | 2 | Nein |
| sickn33/antigravity-awesome-skills (NEU, 484 MB, Bulk = Skill-Inhalt, behalten) | https://github.com/sickn33/antigravity-awesome-skills | MIT (Sammlung; Einzel-Skills mit eigener license-Angabe im Frontmatter) | 8294 SKILL.md Aggregator; relevant: high-end-visual-design (Kopie Leonxlnx), design-philosophy (connerkward), design-md (Google Stitch), design-it/* (30 Stil-Skills), canvas-design, competitor-ad-intelligence, ecommerce-listing-image-set (Beatra, bezahlt), photopea-embedded-editor | 8294 Skills | 2 (Aggregator, meist Kopien) | Nein |
| 626Labs-LLC/626labs-pod-pipeline (NEU) | https://github.com/626Labs-LLC/626labs-pod-pipeline | Code MIT / Artwork all rights reserved | Echte Merch-POD-Pipeline (Etsy "Conundrum by Este"): Gemini-Art ohne Text -> qa.py AI-Slop-Gate (Gemini Vision) -> bgremove.py (klassische CV, 6 Modi) -> PIL-Textkomposit -> Varianten-Matrix -> Printify -> human-gated Publish; remy/SKILL.md Designer-Persona; product_matrix.md mit Printify-Blueprint-IDs und Scale-Regeln | 1 Skill, 11 Commands, 15 Python-Scripts | 5 | Ja |
| carlosfrias/presswork-pod (NEU) | https://github.com/carlosfrias/presswork-pod | KEINE Lizenzdatei (Fork von brac/presswork; Original nicht mehr erreichbar) | 4-Agent-POD-Pipeline (Scout -> Design -> Listing -> Ledger), FLUX via fal.ai -> 300dpi PNG -> Printify -> Etsy, Supabase, AGENTS.md/AGENTS-DEEP.md, Pläne für Mockup-Renderer und BiRefNet-BG-Removal | 0 SKILL.md, 4 Agents (Code) | 4 | Ja |
| booleandifference/art-factory (NEU) | https://github.com/booleandifference/art-factory | MIT | Etsy-Wall-Art/Mugs via Gelato: fal.ai (Flux/SDXL/nano-banana) -> Kuratieren -> 4x Upscale (seedvr) -> Claude Vision schreibt Listing; Tabelle Pixel->Druckgröße (>=4961 px = A3+ bei 300 DPI) | React-App, Cloud Functions | 3 | Ja |
| elayadesign/ai-design-skills (NEU) | https://github.com/elayadesign/ai-design-skills | MIT | landing-page-design (403 Zeilen): Intake, Struktur, Conversion-Copy, visuelles System (Type/Spacing/Radius/Motion) | 1 Skill | 3 | Nein |
| bubucilo/social-audit (NEU) | https://github.com/bubucilo/social-audit | MIT | TikTok/IG-Profil-Audit via Apify MCP: alle Posts ziehen, paid/organic trennen, Winner kategorisieren, <=5 Content-Pillars; Scripts rechnen, Modell urteilt | 1 Skill + Scripts | 3 | Ja (Apify, kostenpflichtig) |
| klebertanide/instagram-agent-skill (NEU) | https://github.com/klebertanide/instagram-agent-skill | MIT | 13 IG-Skills: viral-research, Profil-Scoring (100 Punkte), 26 Hook-Formeln, Caption-Linter, Humanizer | 13 Skills | 2 | Teilweise |
| MastroMimmo/claude-photoshop-skill (NEU) | https://github.com/MastroMimmo/claude-photoshop-skill | MIT | Photoshop-Steuerung (90 Tools) via UXP-Plugin + Proxy (adb-mcp): Layer, Text, Masken, Generative Fill, batchPlay | 1 Skill | 3 | Ja (PS 26+, Desktop) |
| alisaitteke/photoshop-mcp (NEU) | https://github.com/alisaitteke/photoshop-mcp | MIT | Photoshop-MCP mit 118 Tools | MCP | 3 | Ja (Desktop) |
| sfkislev/flue (NEU, 74 MB docs/) | https://github.com/sfkislev/flue | MIT | Python-Bridge zu Adobe-Apps (Photoshop, Illustrator, InDesign) per ExtendScript ohne MCP; Skills-Ordner | Adapter + Skills | 3 | Ja (Desktop) |
| Purple-Horizons/printful-mcp (vorhanden, anderer Agent) | https://github.com/Purple-Horizons/printful-mcp | MIT | Printful-MCP: 17 Tools inkl. printful_create_mockup_task / get_mockup_task, Katalog, Files | MCP | 4 | Ja |
| pizzzzzza/printkk-agent-skill (vorhanden) | https://github.com/printkk/printkk-agent-skill | MIT | PrintKK-API-Skill: Bilder, Designs (async), Print Areas, Orders | 1 Skill | 3 | Ja |
| kylemillerbuilds/printify-publish-queue (vorhanden) | https://github.com/kylemillerbuilds/printify-publish-queue | MIT | State Machine für Printify-Publish (5 Regeln gegen Duplikate) | Python-Modul | 3 | Ja |
| lionelsimai/claude-skills-collection (vorhanden, anderer Agent) | https://github.com/lionelsimai/claude-skills-collection | (nicht geprüft) | Hunderte Template-Skills; apparel-quality-control, tech-pack-creator, size-guide-builder, garment-costing, print-on-demand-strategy, competitor-ad-spy, fashion-brand-identity. Inhalt = generisches 4-Schritt-Template, kaum Fachwissen | sehr viele | 1 | Nein |

Fehlgeschlagene Clones (Repo existiert nicht oder umbenannt): abdul7867/anti-slop bzw. /antislop, Legvan/pod-graphics-workflow, brac/presswork (nur Fork carlosfrias erreichbar, geklont).

## Master-Designer / Ästhetik-Agents: die besten 10 mit Begründung

Kriterien: kodierte Prinzipien statt Adjektiv-Salat, nachprüfbare Regeln, Übertragbarkeit auf Textil-/Markengrafik (nicht nur Web-UI), Anti-Slop-Disziplin.

### 1. anthropics/skills — frontend-design + canvas-design
Pfad: `REPOS/anthropics_skills/skills/frontend-design/SKILL.md`, `REPOS/anthropics_skills/skills/canvas-design/SKILL.md`
Warum: Die Referenz, von der fast alle anderen abschreiben (Hallmark, Impeccable, Leonxlnx nennen sie als Ursprung). Kodiert die Idee "Design aus dem Gegenstand ableiten", Zwei-Pass-Prozess (Token-Plan -> Review gegen Brief -> bauen -> Selbstkritik) und eine datierte Liste der aktuellen KI-Tells. canvas-design liefert das Muster "erst Design-Philosophie (Manifest in 4-6 Absätzen) schreiben, dann 90 % visuell / 10 % Text ausführen", das sich 1:1 auf Shirt-Grafiken übertragen lässt.
Stärkste Regeln:
- "Spend your boldness in one place. Let one element be the memorable thing, keep everything around it quiet and disciplined" (frontend-design, Abschnitt Restraint and self-critique)
- "For calibration, AI-generated design right now clusters around some traits: 1. a warm cream background (near #F4F1EA) with a high-contrast serif display and a terracotta ... accent (often near #D97757 ...) 2. a near-black background with a single bright acid-green or vermilion accent ..." (frontend-design, Process)
- "Emphasize craftsmanship REPEATEDLY: The philosophy MUST stress multiple times that the final work should appear as though it took countless hours to create" (canvas-design, Zeile 48)
Modell: Opus.

### 2. Leonxlnx/taste-skill — tasteskill v2 + brandkit + tells.md
Pfad: `REPOS/Leonxlnx__taste-skill/skills/taste-skill/SKILL.md`, `.../references/tells.md`, `.../skills/brandkit/SKILL.md`
Warum: Einziger Skill mit empirischer Basis (Studie von 247 kuratierten Sites, blinde Juroren), Bibliothek aus 20 Richtungen/Paletten/Typsystemen als JSON (`library/`), und einem Browser-Inspektor, der Regeln misst statt hofft. Das datierte Tells-Register erklärt, warum "use X instead"-Listen selbst zu Tells werden. brandkit ist ein Bildgenerierungs-Prompt für Brand-Boards (3x3-Grid, "one strong brand idea per board"), direkt für Lil-Snouts-Identity-Boards nutzbar.
Stärkste Regeln:
- "what separated the best sites from the forgettable ones was a concept taken from the thing itself, not the styling" (SKILL.md, Punkt 2)
- "inventory the subject ... eight to twelve things that belong to this client and to no competitor ... In blind tests, the page that won each brief was built from an item on such a list" (SKILL.md, Schritt 1)
- "Taking the ornaments away is only half the job; a page that has lost its labels, rules and cards and gained nothing in their place reads as thin" (SKILL.md, Warnung)
- brandkit: "A premium brand kit is not decoration. It is a visual argument for why the brand exists." (brandkit/SKILL.md, Core Principle)
Modell: Opus (Richtungswahl), Scripts laufen ohne LLM.

### 3. jiji262/claude-design-skill
Pfad: `REPOS/jiji262_claude-design-skill/SKILL.md`, `REPOS/jiji262_claude-design-skill/references/design-principles.md`
Warum: Adaptierter interner Claude-Design-Systemprompt; sauberste Liste von Anti-Slop- und Craft-Regeln, plus "Core Asset Protocol" (Marken-Assets wie Logos/Produktfotos sind Pflichtbestandteil, kein SVG-Nachzeichnen) und "Scale floors" (Druck >= 12 pt Body).
Stärkste Regeln:
- "No SVG-drawn imagery as a substitute for real assets. Don't try to SVG-draw a hero illustration, a product screenshot, a portrait, or a 3D object" (design-principles.md)
- "No decoration-by-dataviz. Fake stats, invented numbers, decorative charts that don't represent anything — these are slop" (design-principles.md)
- "Commit to a system before placing pixels. State ... your type scale, your 1–2 background colors, your layout rhythm ... Then hold" (design-principles.md, Craft rules)
Modell: Opus.

### 4. MengTo/skills — no-ai-design-slop + illustration-* (14 Stile, bes. vintage-emblem)
Pfad: `REPOS/MengTo_skills/agent-skills/ui/no-ai-design-slop/SKILL.md`, `REPOS/MengTo_skills/agent-skills/illustration/illustration-vintage-emblem/SKILL.md`, `.../illustration/*/references/craft.md`
Warum: no-ai-design-slop definiert Slop als Entscheidungsqualität ("a choice made by reflex rather than for the product") und liefert einen Removal-Test. Die Illustrations-Skills sind das einzige Fundstück, das Illustrations-Stil in messbare Zahlen gießt (Hex-Palette mit Pixelanteilen, Strichstärken, Keyline-Breite, Komposition) und mit `lint.mjs` prüft; vintage-emblem ist ein Siebdruck-Badge-Stil mit 7 Flachfarben ohne Gradienten, also drucktauglich (Screen/DTG). craft.md enthält Hände-/Handedness-Regeln, die bei Hundemotiven für Pfoten/Posen analog gelten.
Stärkste Regeln:
- "Slop is not a color, font, gradient, card, or animation. It is a choice made by reflex rather than for the product." (no-ai-design-slop, Core Judgment)
- "Never: gradients, opacity, textures, hatching, filters, pure black or white, a sixth hue." (illustration-vintage-emblem, Palette)
- "Never trace or recompose a reference image. Don't reuse its poses, props or layout ... ask 'would someone say this is that card redrawn?' If yes, recompose." (craft.md, Originality)
Modell: Opus für Stil-Entscheidungen; Sonnet für Lint-Durchläufe.

### 5. crizex/art-director
Pfad: `REPOS/crizex__art-director/skills/art-director/SKILL.md`, `.../sources.md`, `.../templates/taste.md`
Warum: Einziger Skill mit persistentem Geschmacksprofil außerhalb des Skills (taste.md, log.md, references/ mit Index), Quellen-Rotation gegen Monokultur und der Regel, jede Richtung neben die stärkste Referenz zu legen. Genau das Modell für einen Lil-Snouts-Art-Director, der Phils Geschmack und die Konkurrenz-Referenzen über Sessions hinweg behält.
Stärkste Regeln:
- "Galleries alone produce gallery averages. Also look at real products next to the category" (Schritt 2)
- "Measure against the bar. Put the strongest find from step 2 next to each direction, at the same size. If a sketch looks plainly weaker than the reference beside it, redo it before the user sees it." (Schritt 3)
- "If taste.md has a 'Patterns' section, let one direction follow it and at least one deliberately break it, so a known preference does not become the next monoculture." (Schritt 3)
Modell: Opus.

### 6. Nutlope/hallmark
Pfad: `REPOS/Nutlope__hallmark/skills/hallmark/SKILL.md`, `.../references/study.md`, `.../references/macrostructures.md`
Warum: Besteht auf struktureller Varianz (21 Makrostrukturen, Rotation), 57 Slop-Gates, sechs verbübergreifende Disziplinen inkl. Pre-emit-Self-Critique auf 6 Achsen und Locked Tokens. `study` ist die beste gefundene Vorlage für "DNA aus Screenshot/URL extrahieren, nicht Pixel kopieren".
Stärkste Regeln:
- "Pre-emit self-critique. Before handing back any output, score it 1–5 on six axes — Philosophy, Hierarchy, Execution, Specificity, Restraint, Variety. Anything < 3 triggers a revision pass" (Disziplin 1)
- "Locked tokens — no mid-render improvisation. Once a theme is selected ... every colour and every font-family declaration ... must reference a named token" (Disziplin 3)
- "study extracts structure, not pixels. It names the macrostructure, the archetypes, the type-pairing, the colour anchor" (hallmark study)
Modell: Opus.

### 7. miqdadbadjuber/anti-slop (antislop + antislop-ui)
Pfad: `REPOS/miqdadbadjuber__anti-slop/skills/antislop/SKILL.md`, `.../skills/antislop-ui/SKILL.md`
Warum: Jede Regel als Tell/Why/Fix mit Referenz auf eine Kernregel (R-01 ...), Dosis-Caps (Glass max 1-2 Elemente, Glow max 1-2), Delivery Gate. Als Filter vor jedem Mockup/Hero/Ad brauchbar, bewusst ohne eigenen Stil.
Stärkste Regeln:
- "Generic Blue-Purple Gradient ... It signals 'no brand identity', not 'our palette', and marks the design as AI-generated at a glance." (antislop-ui, Visual & Color)
- "Dark is a decision, not a default. Forcing it reads as following a trend, not serving the product." (antislop-ui, Dark Mode Default)
- "When every surface is glass, nothing is foreground. ... Dose cap: at most 1-2 elements (R-10)." (antislop-ui, Excessive Glassmorphism)
Modell: Sonnet reicht (Checklisten-Charakter).

### 8. b1rdmania/claude-brand-skills — brand-skill + ADDENDUM-4
Pfad: `REPOS/b1rdmania_claude-brand-skills/brand-skill/SKILL.md`, `.../Workflows/00-EmotiveNarrative.md`, `.../Workflows/03-MarkDevelopment.md`, `.../ADDENDUM-4-WEB-PRESENCE.md`, `REPOS/b1rdmania_claude-brand-skills/art/SKILL.md`
Warum: Vollständigster Brand-Workflow (Emotive Narrative -> Discovery -> Visual Direction mit generierten Referenzbildern -> Mark (Hand-SVG oder Bitmap-Tracing mit vtracer) -> Wordmark -> Design System -> DESIGN.md). ADDENDUM-4 ist der ehrlichste Text zum Konvergenzproblem (warum Vorschriften neue Mittelwerte erzeugen). Art-CLI deckt nano-banana-pro/flux/gpt-image mit --remove-bg und Referenzbildern ab.
Stärkste Regeln:
- "Start with emotive narrative before any visual work. This creates deep LLM memory that prevents generic drift." (SKILL.md)
- "LLMs struggle with mark development because they write SVG as text tokens without seeing the visual result ... if it's not converging we should switch to tracing from a reference image" (03-MarkDevelopment.md)
- "Any instruction specific enough to produce a distinctive result is specific enough to become a new center. 'Be bold' converges to the average of bold." (ADDENDUM-4)
Modell: Opus.

### 9. pbakaus/impeccable
Pfad: `REPOS/pbakaus_impeccable/.claude/skills/impeccable/SKILL.md`, `REPOS/pbakaus_impeccable/README.md`
Warum: Gemeinsame Design-Vokabel (critique, audit, polish, bolder, quieter, distill, typeset, colorize) plus 59 deterministische Detektorregeln, die ohne LLM laufen (CLI/Browser-Extension). Trennung von PRODUCT.md (dauerhafte Produktwahrheit) und DESIGN.md (visuelles System). Für Textil nur die Begriffe und die Anti-Patterns übertragbar.
Stärkste Regeln:
- "Don't use pure black/gray (always tint)" / "Don't wrap everything in cards or nest cards inside cards" / "Don't use bounce/elastic easing" (README, Anti-Patterns)
- "init records durable product truth in PRODUCT.md, so later commands know the audience, purpose, operating context, constraints, voice, and evidence without confusing those facts with surface-level visual direction" (README)
Modell: Sonnet für Commands, Detektor ohne LLM.

### 10. designrique/ai-graphic-design-skill
Pfad: `REPOS/designrique_ai-graphic-design-skill/SKILL.md`
Warum: Einziger Skill, der den kompletten Grafikdesign-Produktionsweg für Marken/Merch beschreibt: Tool-Matrix nach Szenario (Recraft für SVG, Midjourney für Moodboards, Firefly für IP-Safety, Nano Banana für Mockups, Vectorizer.ai, Upscayl), Prompt-Formeln je Tool, Vektorisierungs-Pipeline (Upscale -> Vektorisieren -> Bezier-Cleanup), Displacement-Map-Mockups, Lieferformat-Tabelle (PNG 300 DPI Druck, EPS CMYK), IP-Risiko-Matrix, Anti-Patterns. Portugiesisch, aber kompakt.
Stärkste Regeln:
- "Defina um unico arquetipo dominante antes de qualquer geracao visual. Misturar arquetipos conflitantes (ex: luxuoso + brincalhao + barato) e o erro #1" (Abschnitt 2)
- Recraft-Prompt-Struktur: "Restricoes (CRITICO) -> 'evite gradientes, texturas, sombras, linhas finas'" (Abschnitt 3.1)
- "Regra: sempre entregue o vetor original + rasterizacoes derivadas." (Abschnitt 8)
Modell: Sonnet (Nachschlagewerk), Opus für die Richtungsentscheidung.

Knapp dahinter (lohnende Ergänzungen):
- hcaiano/skills art-director (`REPOS/hcaiano__skills/skills/art-director/SKILL.md`): "Each direction needs a different underlying rule for composition, hierarchy, imagery, and mood. 'More options' is not a direction." und "Change one named trait at a time instead of remixing everything."
- wwewtech/anti-slop-design: Cure 3 "Physical Goods (Apparel, Food, Hardware): The interface must act as an invisible, silent frame. Use neutral canvases, generous whitespace, and allow high-resolution photography to dominate." (direkt für lilsnouts.de-Produktseiten)
- devkindhq logo-prompting: "specific about constraints (palette, type, mood, what to avoid), abstract about the mark itself (suggest, don't depict)"; "Honest specificity, not adjective soup".
- 626Labs remy: "Taste: Loves oversized edge-to-edge prints, bold type ... Hates tiny floating chest logos and generic clip-art." + "Print quality over cleverness ... A funny idea that prints muddy gets fixed or killed."
- transitive-bullshit better-typography: messbare Typo-Regeln (Line-height nach Rolle 1.1/1.2-1.3/1.5-1.6, Letter-spacing nach Größe, Measure 60-75 Zeichen).
- sickn33 design-philosophy (connerkward): "Name the movement (1–2 words) ... Articulate in 4–6 paragraphs"; Kurzfassung von canvas-design.

## Textil/Print-spezifisch: alles Gefundene

Ergebnis vorweg: Es gibt kein GitHub-Skill, das DTG/DTF/AOP-Druckdateiregeln (Druckfläche in Pixeln, 300 DPI auf Endgröße, transparente PNG, Halo-/Knockout-Regeln, Unterweiß) als Agent-Skill kodiert. Die nächsten Treffer:

1. 626Labs-LLC/626labs-pod-pipeline — `REPOS/626Labs-LLC__626labs-pod-pipeline/` (Relevanz 5)
   - README + `POD_DESIGN_PIPELINE.md`: 9 Stufen "CONCEPT -> GENERATE (Gemini, no text) -> QA (AI-slop filter) -> BG REMOVE -> TEXT COMPOSITE (PIL) -> VARIANT MATRIX (5-10 SKUs/base) -> UPLOAD -> CREATE PRODUCT -> PUBLISH (gated)".
   - Regel "The model never writes the words. Every generation prompt includes 'no text'; type is composited afterward with PIL."
   - `qa.py`: Gemini-Vision-Pass mit Prompt-Checkliste "extra or missing fingers/limbs, melted or asymmetric faces, garbled or gibberish text, uncanny over-smooth plastic gloss, nonsensical [objects]", Verdikt pass/regenerate, plus "untied_background" und "text_legible".
   - `bgremove.py`: klassische CV (Corner-Sampling-Color-Key, GrabCut, Contour-Matting, Alpha-Unmixing), 6 Modi, deterministisch.
   - `city_nickname_art.py`: "Auto-fits type to ~86% width, controlled shadow (no ghost), transparent RGBA at print res."
   - `remy/references/product_matrix.md`: Printify-Blueprint/Provider/Variant-IDs, Scale-Regeln (AOP Tote/Drawstring scale=2.5, "AOP Hoodie: ALL positions need images", "Keep solid bg for: AOP (hoodies, joggers), pattern-combo overlays"). Drop-Mathe: "A 'drop' = one concept x 3-10 SKUs minimum. Never ship a single SKU."
   - `remy/SKILL.md`: Designer-Persona mit Hard Rules (ask before live, legal safety, print quality over cleverness, SKU math).
   - `.claude/commands/`: gen, qa, cut, wordart, build, ship, draft, reassess, gallery, inventory, deploy.
   - Einschränkung: Artwork "all rights reserved"; Code MIT. Nutzung der Scripts/Regeln ja, der Designs nein.

2. eachlabs/skills tshirt-design-generation — `REPOS/eachlabs__skills/skills/tshirt-design-generation/SKILL.md` (362 Zeilen)
   - Tabelle Druckverfahren -> Format: Screen Print PNG transparent 1-6 Farben; DTG PNG transparent unlimitiert; Sublimation PNG/JPG All-over; Heat Transfer transparent; Vinyl Cut "1-3 colors, Simple shapes, no gradients".
   - Stil-Kategorien (Graphic, Typography, Vintage/Retro distressed, Minimalist, Band-Merch, Humor/Meme). Alle Beispiele sind curl-Aufrufe an die bezahlte each::sense-API; die Prompt-Formulierungen ("suitable for screen printing", "transparent background exports") sind als Prompt-Bausteine ohne API nutzbar.
   - Ebenfalls dort: pet-portrait-generation (Stile: Renaissance/Royal, Watercolor, Pop Art, Costume, Memorial, "Product Mockups: Pet portraits on mugs, canvas, and merchandise"; mit image_urls Referenzfoto), sticker-design-generation (Die-Cut-Größen, weißer Hintergrund zum Schneiden), seamless-pattern-generation (Repeat-Typen tile/half-drop/mirror/brick), product-photo-generation, meta-ad-creative-generation, logo-generation.

3. devkindhq/ideogram-ai-toolkit seamless-pattern-texture-generator — `REPOS/devkindhq__ideogram-ai-toolkit/skills/seamless-pattern-texture-generator/SKILL.md` + `references/tile-prompt-recipe.md`, `tiling-verification.md`, `anti-slop-discipline.md`
   - Ehrlich: "No generate_image ... call ... exposes a seamless/tileable boolean ... Seamlessness here is achieved entirely through prompt language plus a best-effort visual-verification step."
   - Default "straight repeat, and say so explicitly"; Prompt muss "flat top-down framing with no directional lighting, exclude any border or vignette" enthalten. Relevant für AOP-Muster (Hundemotiv-Repeat).

4. danielrosehill/Claude-Digital-Printing-Plugin — `REPOS/danielrosehill__Claude-Digital-Printing-Plugin/skills/{add-bleed,verify-bleed-safe,downsample-images,normalize-color-profile,embed-fonts,flatten-transparency}/SKILL.md`, Agent `agents/print-prep-orchestrator`
   - Nur PDF (v1): 3 mm Bleed, 300 DPI Ghostscript-Rezept, CMYK FOGRA39 vs sRGB. Für Poster-Karten/Beileger/Hangtags brauchbar, nicht für DTG-PNG. README: "Skills for image and banner prep ... will be added later."

5. danielrosehill/Claude-Image-Production-Plugin — `REPOS/danielrosehill__Claude-Image-Production-Plugin/skills/{vectorize,upscale-image,svg-to-raster,web-ready,scrub-metadata}/SKILL.md`
   - vectorize: vtracer (Farbe), Fallback Inkscape/potrace; Parameter color precision 1-8, filter speckle, "Stylize a photo into a flat-colour vector (large --filter-speckle + low --color-precision)". upscale-image für Druckauflösung.

6. realproject7/svgsmith — `REPOS/realproject7__svgsmith/skills/vectorize/SKILL.md`
   - Intent->Flags-Tabelle (binary 0.95 für Logos, color für Flat-Art, --transparent-background, --flatten-shading, --detail poster), Selbstverifikation per Re-Rasterisierung. Lizenz FSL-1.1 (kommerziell nutzbar, nicht als Konkurrenzprodukt).

7. designrique/ai-graphic-design-skill — Abschnitte 6 (Vektorisierungs-Pipeline: Upscaling -> Vectorizer.ai/Recraft -> manueller Bezier-Cleanup), 7 (Mockups: Photoshop Displacement Maps, Blend Options; KI-Alternativen), 8 (Formate: "PNG 72 PPI (tela) / 300 DPI (impressao)", "EPS: CMYK obrigatorio"), 10 (IP-Safety-Matrix je Tool).

8. MengTo illustration-vintage-emblem + illustration-halftone-line + illustration-two-colour-brush — handgeschriebene SVG-Stile mit festen Flachfarbpaletten; vintage-emblem ist explizit "A screen-printed badge on cream paper", Palette 7 Farben, "Never: gradients, opacity, textures". Scripts `wordmark.mjs` (Wordmark-Lockup A-Z, --max-width) und `lint.mjs`. Direkt als Vektor-Shirt-Grafik verwendbar (SVG -> Druck-PNG via svg-to-raster).

9. carlosfrias/presswork-pod — `REPOS/carlosfrias__presswork-pod/ARCHITECTURE.md`: "Design runs every 15 min, picks up approved briefs, generates FLUX prompts -> fal.ai -> 300dpi PNG -> design_packages table"; `PLAN_MOCKUP_RENDERER.md`, `PLAN_birefnet_bg_removal.md`, `PLAN_shirt_color_size_variants.md`, `docs/printify-integration.md` (Rate-Limits 200/30 min für publishing). AGENTS.md-Muster für 4 Agenten. Keine Lizenzdatei.

10. booleandifference/art-factory — `WORKFLOWS.md` Zeile 155: Tabelle Pixelbreite -> Druckgröße ("≥ 4961px | A3+ at 300 DPI"), "Gelato publishing refuses anything that isn't 4× upscaled" (seedvr). Wall Art/Mugs, nicht Apparel.

11. kingbootoshi/nano-banana-2-skill — `-t` Flag: "generate on green screen, remove background (FFmpeg colorkey + despill)" -> transparente PNG-Freisteller für Shirt-Grafiken ohne Remove.bg-Key. b1rdmania art/Generate.ts: `--remove-bg` (REMOVEBG_API_KEY), `--reference-image` (nano-banana-pro) für Stilkonsistenz über Hunderassen hinweg.

12. motiful/product-shots — `product-shots-multi-angle` (9-Winkel Fashion-on-Model-Lookbook), `product-shots-ad-creative` (Plattformmaße/Safe-Zones/Text-Overlay-Regeln, Banned-Words-Filter, "Required Positive Instruction protects native packaging text"). Apparel-Mockups via Image-Gateway, kein Printful.

13. Purple-Horizons/printful-mcp — `printful_create_mockup_task` / `printful_get_mockup_task`: echte Hersteller-Mockups per API (Alternative zu KI-Mockups). pizzzzzza/printkk-agent-skill: Print-Areas je Produkt abfragbar. kylemillerbuilds/printify-publish-queue: Publish-State-Machine ("Wait at least 5 minutes before judging a publish", "Never re-publish a product that is still locked").

14. Adobe-Automation: MastroMimmo/claude-photoshop-skill (90 Tools via UXP, Generative Fill, Masken, batchPlay), alisaitteke/photoshop-mcp (118 Tools), sfkislev/flue (ExtendScript-Bridge für Photoshop/Illustrator/InDesign). Damit wären Displacement-Map-Mockups und Smart-Object-Templates skriptbar (Desktop-Photoshop nötig).

15. lionelsimai/claude-skills-collection: tech-pack-creator, apparel-quality-control, size-guide-builder, garment-costing, print-on-demand-strategy. Inhalt ist ein generisches 4-Schritt-Template ohne Fachregeln (geprüft an apparel-quality-control). Nicht übernehmen.

16. wwewtech anti-slop-design Cure 3 (Physical Goods: Interface als stiller Rahmen, Fotografie dominiert) und nextlevelbuilder banner-design (Safe Zone: "critical content in the central 70–80%", "at most 2 typefaces, a single CTA, text contrast of at least 4.5:1") für Shop-/Ad-Flächen.

## Design-Research per Referenz: Tools/Skills, die Websites/IG/Ads einer Marke analysieren

Website -> Design-Sprache:
- Manavarya09/design-extract (`REPOS/Manavarya09__design-extract/skills/extract-design/SKILL.md`): `npx designlang <url> --screenshots [--depth 3] [--dark]` -> 8 Dateien (AI-Markdown mit Farben/Fonts/Spacing/Shadows/Components/Animations, Tailwind, shadcn, Figma-Variables, W3C-Tokens, Preview-HTML). `/battle` = benoteter Head-to-Head zweier Sites, `/remix` = Umstilen. Headless, MIT. Bester Startpunkt für heybalu.de / petprinted / OMD-Shop.
- Nutlope/hallmark `study <URL|Screenshot>` (`references/study.md`): 5-Schritt-Protokoll Surface -> Type -> Structure (21 Makrostrukturen + Komponenten-Archetypen mit Variation-Knobs) -> Motion -> Rhythm; URL-Modus liest DOM, Bild-Modus Vision-Pass. Ausgabe ist eine Diagnose, aus der gebaut wird ("extracts structure, not pixels"). Hat Refuse-Liste für Domains.
- kalilfagundes/design-system-extractor-skill: Python-Preprozessor (`tools/design_system_extractor.py <URL>`) gegen Token-Limits, Ausgabe Storybook-ähnliche HTML-Doku.
- Leonxlnx/taste-skill: `scripts/inspect.mjs` misst eine Seite im Browser gegen tells.md; `image-to-code-skill` (Bild -> Analyse -> Frontend); `library/sites.json` als Referenzdatenbank.
- wwewtech anti-slop-design Cure 1 "Visual DNA Ingestion & Style Extraction": aus Screenshot die 5 Foundation Tokens + Spacing Density extrahieren, "Do not blindly copy visual bugs from screenshots".
- OneWave-AI color-palette-extractor: K-Means-Dominanzfarben aus Bild/Website/Mockup, Harmonie-Analyse, Export als CSS/Tailwind. fatihaydost brand-identity `site extract`. nextlevelbuilder brand `extract-colors.cjs <image>`.
- VoltAgent/awesome-design-md als Vorlage, wie ein fertiges Konkurrenz-DESIGN.md aussieht (z. B. `design-md/nike/DESIGN.md`: "photography-first commerce system built on extreme typographic contrast", benannte Tokens inkl. sale/success/info).

Instagram / Social:
- bubucilo/social-audit (`REPOS/bubucilo__social-audit/SKILL.md`): zieht via Apify alle Posts eines öffentlichen IG/TikTok-Profils, trennt paid/organic, findet Winner, baut <=5 Content-Pillars. Laut Beschreibung für das eigene Profil gedacht, technisch läuft es auf jedem öffentlichen Account (Konkurrenz-IG ist damit auswertbar; IG liefert nur Likes/Kommentare).
- klebertanide/instagram-agent-skill: viral-research, Outlier-Ranking, Profil-Scoring-Rubrik (100 Punkte).
- ScrapeCreators/social-media-research-skills und apify/awesome-skills (bereits im Crawl vorhanden) als Datenquellen.

Ads (Meta Ad Library etc.):
- apify/awesome-skills apify-ads-intelligence (`REPOS/apify_awesome-skills/skills/apify-ads-intelligence/SKILL.md`): Meta/Google/TikTok/LinkedIn Ad Libraries via Apify-Actors, Kreativ-Daten inkl. Laufzeit.
- thatrebeccarae/claude-marketing competitor-ads-analyst: Formate, Message-Typen, Funnel-Stufe, Pain-Point-Frequenz-Scoring.
- lionelsimai competitor-ad-spy, Hainrixz/claude-ads ads-competitor, sickn33 competitor-ad-intelligence: Template-Teardowns (Hook/Offer/CTA/Why it works), keine Bildanalyse.
- han669669/meta-ads-static-creator: "studies a reference ad and identifies its format devices (ratings, testimonial cards, badges)", baut Brand-Profil aus Website (`/brand`), produziert Nachbau mit eigenen Produkten in 4:5 + 9:16. Lizenzproblem beachten.
- Hinweis: In dieser Session sind Motion_Creative_Analytics (get_inspo_creatives, get_inspo_brand_context) und FB_META_ADS ads_library_search als MCP-Tools vorhanden; das ist für Lil Snouts der direktere Weg als Apify.

Bestseller-/Trend-Analyse:
- 626Labs `ETSY_REASSESSMENT_2026-06.md` + `pod reassess` (Repricing/Cuts aus Verkaufsdaten), remy "Review the styles we have now" (Ordner sichten, Kritik, Lücken vs. Trend).
- carlosfrias/presswork-pod Scout-Agent (`PLAN_SCOUT_VISION.md`): Trend-Scouting mit Vision.
- MengTo daily-ui-inspiration-capture: Full-Page-Screenshot + Section-Crops je Referenz, Manifest gegen Wiederholung; Muster für einen "Konkurrenz-Bestseller-Capture"-Workflow.
- Kein Repo macht Bestseller-Analyse auf Shopify-/Etsy-Konkurrenzshops (Best-Selling-Collection-Sortierung, Review-Zählung). Muss gebaut werden.

## Top-Skills zum Übernehmen

Modell-Tier: Design-Urteil = Opus; Checklisten/Prompt-Formatierung = Sonnet; reine Skripte/Lints = Haiku oder ohne LLM.

| # | Pfad | Was übernehmen | Tier |
|---|---|---|---|
| 1 | `REPOS/anthropics_skills/skills/frontend-design/SKILL.md` + `skills/canvas-design/SKILL.md` | Zwei-Pass-Prozess (Token-Plan -> Review gegen Brief -> bauen -> Selbstkritik), datierte Tells-Liste, "Philosophie-Manifest zuerst" für Shirt-Motive | Opus |
| 2 | `REPOS/Leonxlnx__taste-skill/skills/taste-skill/SKILL.md`, `references/tells.md`, `references/critique.md`, `references/imagery.md` | Subjekt-Inventar (8-12 Dinge, die nur dieser Marke gehören), Richtungen verteilen statt erfinden, Juror-Rubrik, Tells-Register | Opus |
| 3 | `REPOS/Leonxlnx__taste-skill/skills/brandkit/SKILL.md` | Brand-Board-Bildprompt (3x3, Core Principle, Intake) für Lil-Snouts-Identity-Boards via Gemini | Sonnet (Prompt) / Opus (Auswahl) |
| 4 | `REPOS/jiji262_claude-design-skill/references/design-principles.md` + `SKILL.md` (Core Asset Protocol) | Anti-Slop-/Craft-/Content-Regeln, Scale floors, "Placeholders beat fakes" | Opus |
| 5 | `REPOS/crizex__art-director/skills/art-director/SKILL.md` + `templates/taste.md`, `templates/log.md`, `sources.md` | Persistentes Geschmacksprofil (taste.md) und Referenz-Index für Phils Vorlieben + Konkurrenzreferenzen; Quellenrotation; "measure against the bar" | Opus |
| 6 | `REPOS/Nutlope__hallmark/skills/hallmark/references/study.md` + `macrostructures.md` | DNA-Extraktion aus Konkurrenz-Screenshots (Struktur, Archetypen, Type-Pairing, Colour Anchor, Rhythm) für Website/Ads der Wettbewerber | Opus |
| 7 | `REPOS/MengTo_skills/agent-skills/ui/no-ai-design-slop/SKILL.md` | Removal-Test und Quality Gates als Gate vor jedem Mockup/Hero | Sonnet |
| 8 | `REPOS/MengTo_skills/agent-skills/illustration/illustration-vintage-emblem/SKILL.md` + `references/craft.md` + `scripts/wordmark.mjs`, `lint.mjs` | Siebdruck-Badge-Stil als messbares Regelwerk (Palette mit Pixelanteilen, Strichstärken, Keyline) als Vorlage für eigene Lil-Snouts-Stil-Skills (Crest/Bootleg/Xmas) | Opus (Stil) / ohne LLM (Lint) |
| 9 | `REPOS/626Labs-LLC__626labs-pod-pipeline/qa.py` (Prompt-Checkliste), `POD_DESIGN_PIPELINE.md` Stage 3, `remy/SKILL.md` Hard Rules, `remy/references/product_matrix.md` | AI-Slop-QA-Gate für generierte Motive (Gliedmaßen, Gesichter, Gibberish, Plastik-Glanz, lose Hintergrundelemente), "no text in generation, type via PIL", SKU-/Drop-Mathe, AOP-Scale-Regeln | Sonnet (Vision-QA) |
| 10 | `REPOS/b1rdmania_claude-brand-skills/brand-skill/Workflows/00-EmotiveNarrative.md`, `03-MarkDevelopment.md`, `ADDENDUM-4-WEB-PRESENCE.md`, `art/Tools/Generate.ts` | Emotive Narrative als Gedächtnisanker, Mark-Tracing-Pfad (vtracer), Konvergenz-Warnung, Multi-Model-Image-CLI mit --reference-image | Opus / CLI |
| 11 | `REPOS/designrique_ai-graphic-design-skill/SKILL.md` Abschnitte 1, 3.1, 3.5, 6, 8, 10 | Tool-Matrix, Recraft-Prompt-Struktur mit Restriktionen, Mockup-Formel, Vektorisierungs-Pipeline, Formattabelle, IP-Matrix | Sonnet |
| 12 | `REPOS/veryCoolTimo__imagegen-skills/skills/image-prompt/SKILL.md` + `references/anatomy.md`, `archetypes.md`, `fonts-palettes.md`, `models/` | 9-Block-Prompt-Skelett mit benannten Zonen/Hex/Fonts; Archetyp product-ad/poster/illustration; Adapter für gpt-image-2/FLUX.2/Recraft/Ideogram | Sonnet |
| 13 | `REPOS/maciejdzierzek__nano-banana-prompt-generator/skills/nano-banana/SKILL.md` | Modell-IDs/Deprecations/Prompt-Formeln für Gemini-Image (Nano Banana 2 / Pro), konversationelles Editieren | Sonnet |
| 14 | `REPOS/kingbootoshi__nano-banana-2-skill/plugins/nano-banana/skills/nano-banana/SKILL.md` | Green-Screen -> FFmpeg colorkey+despill Freisteller-Rezept ohne Remove.bg | ohne LLM |
| 15 | `REPOS/devkindhq__ideogram-ai-toolkit/skills/logo-prompting/SKILL.md` + `references/anti-slop-discipline.md`; `skills/seamless-pattern-texture-generator/` | Logo-Prompt-Struktur (suggest, don't depict; strukturelle Varianz statt Palette-Swaps); Tile-Rezept + Tiling-Verifikation für AOP-Muster | Opus (Richtung) / Sonnet (Prompt) |
| 16 | `REPOS/realproject7__svgsmith/skills/vectorize/SKILL.md` und `REPOS/danielrosehill__Claude-Image-Production-Plugin/skills/{vectorize,upscale-image,svg-to-raster}/SKILL.md` | Vektorisierung/Upscaling als deterministische Pipeline-Schritte | ohne LLM / Haiku |
| 17 | `REPOS/Manavarya09__design-extract/skills/extract-design/SKILL.md` | Konkurrenz-Website -> Design-Language-MD + Screenshots, /battle | Haiku (Ausführung) / Opus (Interpretation) |
| 18 | `REPOS/motiful__product-shots/skills/product-shots-ad-creative/references/hard-constraints.md`, `banned-words.md`; `product-shots-multi-angle/SKILL.md` | Plattformmaße/Safe-Zones/Text-Overlay-Regeln, Banned-Words-Filter für Bildprompts, 9-Winkel-Lookbook-Prompts | Sonnet |
| 19 | `REPOS/miqdadbadjuber__anti-slop/skills/antislop-ui/SKILL.md` + `antislop/SKILL.md` | Tell/Why/Fix-Filter mit Dosis-Caps für Shop-Seiten, Ads, E-Mails | Sonnet |
| 20 | `REPOS/cofoundy__brand-skills/skills/{brand-identity,competitor-branding,brand-guidelines}/SKILL.md` | brand.yaml-Konvention, Visual-Identity-Brief-Struktur, Competitor-Brand-Map (Positionierung, Voice, visueller Ansatz, Territory) | Sonnet (Struktur) / Opus (Urteil) |
| 21 | `REPOS/fatihaydost__brand-identity-skill/scripts/brand.py` + `references/{cohesion,type,logo,color,ai-defaults}.md` | Messbare Brand-Checks (Kontrast, Farbenblindheit, Glyph-Coverage, Kleinst-Logo-Render) und ai-defaults.md (KI-Default-Vermeidung) | ohne LLM / Opus |
| 22 | `REPOS/nextlevelbuilder_ui-ux-pro-max-skill/.claude/skills/banner-design/references/banner-sizes-and-styles.md` | Formate/Safe-Zones für Social-Cover, Ads, Hero | Haiku |
| 23 | `REPOS/transitive-bullshit_skills/skills/better-typography/SKILL.md` | Messbare Typo-Regeln (Line-height nach Rolle, Tracking nach Größe, Measure) für Shirt-Lettering-Lockups und Shop | Sonnet |
| 24 | `REPOS/hcaiano__skills/skills/art-director/SKILL.md` | Direktions-Framing (3-5 Prämissen mit je eigener Regel), "one trait per iteration", "prove the system" auf angrenzendem Asset | Opus |
| 25 | `REPOS/eachlabs__skills/skills/{tshirt-design-generation,pet-portrait-generation,sticker-design-generation,seamless-pattern-generation}/SKILL.md` | Nur die Tabellen/Prompt-Bausteine (Druckverfahren -> Format, Pet-Portrait-Stile, Sticker-Specs, Repeat-Typen); API nicht übernehmen | Haiku |

## Lücken

1. Kein Skill kodiert DTG/DTF/AOP-Druckdateiregeln für Apparel (Druckbereich in px je Produkt/Provider, 300 DPI auf Endgröße, transparente PNG ohne Halo, Mindeststrichstärke, Unterweiß/Knockout, Farbverschiebung auf dunklen Shirts, Pastell-Problematik bei DTG). Die bestehende Lil-Snouts-Skill-Sammlung (bestseller-textildesign, Marketprint-Größenmasken) ist hier weiter als alles auf GitHub. Übernahmekandidaten dafür nur indirekt: 626Labs product_matrix (Scale-Regeln), eachlabs Druckverfahren-Tabelle, designrique Formattabelle.
2. Kein Skill für Pet-Portrait-Pipelines (Foto -> konsistentes Hundeporträt in Markenstil -> Druckdatei). eachlabs pet-portrait-generation ist API-gebunden; ComfyUI-IPAdapter-Workflows existieren nur als Blogposts, nicht als Agent-Skill.
3. Keine Konkurrenz-Bestseller-Analyse für Shopify/Etsy-Shops (Sortierung best-selling, Review-Zahlen, Varianten-Zählung) als Skill. Nur Template-Teardowns.
4. Kein Instagram-Grid-/Feed-Ästhetik-Analyzer (Farbwelt, Motivanteile, Mockup-Stil) für Wettbewerber; social-audit misst Performance, nicht Bildsprache. Ein Vision-Pass über die Top-Posts muss selbst gebaut werden (Hallmark study + wwewtech Cure 1 als Protokollvorlage).
5. Mockup-Generierung für Apparel: nur KI-Bildmodelle (nano-banana Presets, motiful) oder Hersteller-APIs (Printful mockup task). Kein Skill für Photoshop-Smart-Object-/Displacement-Templates als Pipeline (Photoshop-Skills existieren, aber kein Apparel-Workflow darauf).
6. Canva: in dieser Session sind Canva-MCP-Tools (generate-design, autofill, brand templates, remove-background, separate-image-layers) vorhanden; auf GitHub gibt es nur Rube/Composio-Wrapper (sickn33 canva-automation), keine Design-Regeln für Canva-Ausgabe.
7. Midjourney: beide Skills (justinperea, avienor) sind brauchbar, aber keiner behandelt Shirt-Grafik-Spezifika (isoliertes Motiv, flacher Hintergrund, Vektor-Look, --no background). Die Prompt-Bausteine aus eachlabs/designrique müssen ergänzt werden.
8. Typografie für Lettering-Shirts (Lockup-Generatoren, Kerning-Regeln auf Textil, Lesbarkeit auf Distanz) nur bei 626Labs city_nickname_art.py (fill-the-box 86 %) und MengTo wordmark.mjs; keine Regelsammlung für Spruch-Shirts.
9. Lizenzfragen: han669669/meta-ads-static-creator (ohne Erlaubnis des Autors veröffentlicht), avienor/midjourney-prompts, kalilfagundes, eachlabs, inference-sh, carlosfrias/presswork-pod ohne LICENSE-Datei; 626Labs-Artwork all rights reserved. Vor Übernahme prüfen bzw. nur Regeln paraphrasieren.
10. Nicht gefunden / nicht verifizierbar: "OMD" als Marke; Heybalu/Petprinted kommen in keinem Repo vor.
11. Search-Budget (200 Suchen pro Turn über alle Agenten) war vor der OMD-Verifikation und vor einer Nachsuche zu abdul7867/anti-slop und Legvan/pod-graphics-workflow erschöpft; beide Repos sind unter dem gefundenen Namen nicht klonbar.

## Quellen

Suchergebnisse (WebSearch, 26 Abfragen) und Repos:
- https://github.com/anthropics/skills (frontend-design, canvas-design)
- https://github.com/jiji262/claude-design-skill
- https://github.com/designrique/ai-graphic-design-skill
- https://github.com/b1rdmania/claude-brand-skills
- https://github.com/bergside/awesome-design-skills
- https://github.com/VoltAgent/awesome-design-md, https://github.com/VoltAgent/awesome-claude-design, https://github.com/Digiflex-solution/awesome-design-md
- https://github.com/rohitg00/awesome-claude-design
- https://github.com/pbakaus/impeccable
- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- https://github.com/MengTo/skills
- https://github.com/contains-studio/agents, https://github.com/msitarzewski/agency-agents
- https://github.com/transitive-bullshit/skills
- https://github.com/nidhinjs/prompt-master
- https://github.com/coreyhaines31/marketingskills
- https://github.com/crizex/art-director
- https://github.com/hcaiano/skills
- https://github.com/Leonxlnx/taste-skill
- https://github.com/paulltalk/anti-slop, https://github.com/miqdadbadjuber/anti-slop
- https://github.com/Nutlope/hallmark
- https://github.com/wwewtech/anti-slop-design
- https://github.com/danielrosehill/Claude-Digital-Printing-Plugin, https://github.com/danielrosehill/Claude-Image-Production-Plugin
- https://github.com/realproject7/svgsmith
- https://github.com/justinperea/midjourney-cc-skill, https://github.com/avienor/midjourney-prompts
- https://github.com/kingbootoshi/nano-banana-2-skill, https://github.com/maciejdzierzek/nano-banana-prompt-generator, https://github.com/devonjones/devon-claude-skills, https://github.com/jlouage/Nano-Banana-Pro-Claude-Skills, https://github.com/damiansire/generate-nanobanana, https://github.com/0-to-1-Labs/gemini
- https://github.com/AbdulkareemKR/brand-identity-generator, https://github.com/cofoundy/brand-skills, https://github.com/arnabbagxd/Brand-building-skills, https://github.com/fatihaydost/brand-identity-skill
- https://github.com/motiful/product-shots, https://github.com/veryCoolTimo/imagegen-skills, https://github.com/eachlabs/skills, https://github.com/inference-sh/skills
- https://github.com/Manavarya09/design-extract, https://github.com/kalilfagundes/design-system-extractor-skill
- https://github.com/nhatmobile1/color-palette-skill, https://github.com/OneWave-AI/claude-skills, https://github.com/meodai/skill.color-expert
- https://github.com/devkindhq/ideogram-ai-toolkit
- https://github.com/han669669/meta-ads-static-creator, https://github.com/gushchinda/meta-ads-skills, https://github.com/Creatify-AI/static-ad-concept-generator
- https://github.com/alirezarezvani/claude-skills, https://github.com/rampstackco/claude-skills, https://github.com/sickn33/antigravity-awesome-skills
- https://github.com/626Labs-LLC/626labs-pod-pipeline, https://626labs.dev/
- https://github.com/carlosfrias/presswork-pod, https://github.com/booleandifference/art-factory
- https://github.com/elayadesign/ai-design-skills
- https://github.com/bubucilo/social-audit, https://github.com/klebertanide/instagram-agent-skill
- https://github.com/MastroMimmo/claude-photoshop-skill, https://github.com/alisaitteke/photoshop-mcp, https://github.com/sfkislev/flue
- https://github.com/Purple-Horizons/printful-mcp, https://github.com/printkk/printkk-agent-skill, https://github.com/kylemillerbuilds/printify-publish-queue
- https://github.com/apify/awesome-skills, https://github.com/thatrebeccarae/claude-marketing, https://github.com/lionelsimai/claude-skills-collection
- Sekundärquellen aus der Suche (nicht geklont): https://skillsllm.com/skill/taste-skill, https://mcpmarket.com/tools/skills/site-teardown, https://mcpmarket.com/tools/skills/seamless-pattern-generator, https://ideogram.ai/blog/claude-mcp/, https://www.tasteskill.dev/docs, https://pasqualepillitteri.it/en/news/576/claude-code-skills-design-uiux-guide, https://www.firecrawl.dev/blog/best-claude-code-skills, https://hackernoon.com/make-masterpiece-pet-portraits-with-comfyui, https://dev.to/jakub_inithouse/pet-imagination-by-inithouse-our-ai-pet-portrait-pipeline-9-styles-under-60-seconds-2b1o
