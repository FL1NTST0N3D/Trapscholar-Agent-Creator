# Cannabis Breeding – Knowledge-Crawl (Stand 2026-10-15)

Ziel: alles auf GitHub/Open-Science, was ein ernsthaftes Hobby-/Profi-Zuchtprogramm (KCanG, Erwachsene, Pflanzengenetik/Gartenbau) braucht – Skills, Tools, Datensaetze, Papers, Rechner. Bezug: Vault `02_BREEDING/Research/Stammbaum-Datenbank` (edges.csv/verwandtschaft.csv) + Skill `stammbaum-crawler`.

**Methodik / Einschraenkungen dieses Laufs**
- Das WebSearch-Budget der Session war zu Beginn dieses Agentenlaufs bereits aufgebraucht (200 Calls, geteilt mit anderen Agenten). Ersatz: 42 GitHub-Repo-Suchen + 14 GitHub-Code-Suchen ueber das GitHub-MCP (`search_repositories`/`search_code`), plus GitHub-Topic-Seiten (`topics/cannabis`, `plant-breeding`, `hemp`, `grow`) per WebFetch. Suchbegriffe EN+DE (u. a. "cannabis breeding", "cannabis genome", "seedfinder", "kannapedia", "cannabis lineage", "cannabis terpene", "cannabis COA", "grow journal", "VPD calculator", "seed inventory", "plant breeding pedigree", "AlphaSimR", "punnett square", "cannabis mcp", "hemp genetics", "cannabis pangenome", "tissue culture", "KCanG", "Konsumcannabisgesetz", "Cannabis Anbau", "Hanf Zuechtung", Code-Suchen nach `SKILL.md` mit cannabis/plant breeding/horticulture, "silver thiosulfate", "de Meijer chemotype", "hop latent viroid", "Autoflower1", "seedfinder.eu lineage python").
- Der Proxy laesst nur github.com / raw.githubusercontent.com durch. PubMed, NCBI, Frontiers, MDPI, Kannapedia, Wikipedia waren nicht erreichbar (DNS). Papers sind daher ueber ihre in den Repos zitierten DOIs/URLs belegt (v. a. `JakeTheRabbit/cannabis-white-papers`, das jede Aussage mit Peer-Review-Referenz fusst) – als **Sekundaerbeleg** markiert, nicht live verifiziert.
- 97 Repos geklont nach `scratchpad/crawl/repos_breeding/<owner>__<repo>` (Liste: `scratchpad/crawl/cloned_breeding_list.txt`). Ueber-150-MB-Klone wurden auf Wissensinhalt beschnitten (Sequenzdaten, JSON-Pipelines, Bilder, node_modules, .git entfernt): ci-strains-pro (5,8 GB -> 18 MB), 2024_Hemp_Genomes (1,3 GB -> README+PAR_boundaries), canna-transcripts (970 MB -> 297 MB reine Transkripte), skill-library-mcp (1 GB -> nur Pflanzen-/Garten-Skills), legalize-de (nur KCanG/MedCanG/BtM-Texte), gesetze-corpus-data (nur BJNR06D0B0024 = KCanG), MySeedBook, cannabis-data-science, ViningLab (Dateien > 3 MB entfernt). Gesamt 2,3 GB. Kein Code aus Klonen ausgefuehrt.

## Gecrawlte Repos

Relevanz 1–5 = Nutzen fuer Phils Breeding-Programm (5 = sofort einbauen). Typ: Skill / Tool / Daten / Paper / Wissen / Recht. Offline = laeuft/lesbar ohne Netz.

### A. Zucht-Wissen (Text, agentenfaehig)

| Repo | URL | Lizenz | Inhalt kurz | Typ | Rel. | Offline |
|---|---|---|---|---|---|---|
| JakeTheRabbit/cannabis-white-papers | https://github.com/JakeTheRabbit/cannabis-white-papers | CC BY-NC 4.0 | 55 Fachpapiere (MD+HTML) mit Peer-Review-Fussnoten: `papers/genetics-phenohunting.md` (Genotyp/Phaenotyp/Chemotyp, Saatguttypen, Pheno-Hunt-Protokoll, Stichprobengroesse, Keeper-Redundanz, Gentests), `cannabinoids-terpenes.md` (B-Locus, 5 Chemotypen), `mother-plants.md` (HLVd-Zahlen), `tissue-culture*.md`, `seeds-germination.md`, `cloning.md`; `llms-full.txt` = ganzes Korpus fuer RAG | Wissen/Paper | 5 | ja |
| akravetz/dirt | https://github.com/akravetz/dirt | keine Lizenzdatei | Obsidian-Wiki eines laufenden Hobby-Zuchtprogramms: `wiki/breeding/` – nomenclature (P/F1/F2/BX/S1/IBL), stabilization-strategy, family-selection (2x2-Familienmodell, 16 Plaetze), pheno-hunt-protocol, male-evaluation, pollen-handling (Lagertabelle), cross-procedure (Bestaeubung Tag 14–18), feminized-production (>90 %-Regel), isolation, timeline, BOM | Wissen | 5 | ja |
| HomunculusLabs/Farming-KB | https://github.com/HomunculusLabs/Farming-KB | keine Lizenzdatei (Quellen = Buecher, Clarke/Cervantes/Small – nur intern nutzen) | 10k-Seiten-Wiki; `concepts/cannabis-*` ~25 Seiten: chemotype-classification, backcrossing, pollen-collection-storage-clarke, breeding-selection-principles-clarke, autoflowering-breeding, feminized-seeds, landrace-conservation; teils Template-Fuellsaetze am Ende | Wissen | 4 | ja |
| Jack-MillionMedia/Medcan-Agent | https://github.com/Jack-MillionMedia/Medcan-Agent | keine | `botanical_knowledge_base/.../genetics/advanced_breeding.md` (Pheno-Hunt 100+ Samen, Polyploidie, MAS Bt:Bd), `genetic_stability.md` (Klon-Drift = Epigenetik/Viren, TC-Bank, Cryo), Chemotyp-Taxonomie | Wissen | 4 | ja |
| johnhouston707/cannabis-cultivation-resources | https://github.com/johnhouston707/cannabis-cultivation-resources | README: frei nutzbar (Prime Cuts Nursery) | `phenotype-selection-guide.md` (Scoring-Matrix mit Gewichten Commercial/Personal, 4 Phasen), `hlvd-prevention-protocol.md` (Werkzeug-Desinfektion, Testintervalle), clone-rooting-checklist, terpene-selection-guide; Gists: Genetics-Network JSON, Terpene JSON | Wissen/Daten | 4 | ja |
| RAFOUgg/Reviews-Maker | https://github.com/RAFOUgg/Reviews-Maker | keine | FR; `DOCUMENTATION/DATA_REFERENCE/05_GENETIQUE_GENEALOGIE.md` = wissenschaftlich auditierte Datenschema-Felder fuer Stammbaum-App (generation, seedType, pollinationMethod 9 Werte, chemotype I–V, thcSource breeder_claim/lab_tested, THC-total = THC + 0,877*THCA) mit T1-Zitaten (Sawler 2015, McPartland 2018); `13_REGISTRE_SOURCES.md` | Wissen/Schema | 4 | ja |
| muf4/canna-transcripts | https://github.com/muf4/canna-transcripts | keine (Transkripte fremder Podcasts – nur intern) | 279 Transkripte "The Breeders Syndicate 3.0" + Future Cannabis Project, Medicinal Genomics, Cornell SIPS, DeBacco University, Real Seed Co (Landrassen) u. a.; Oral History der Zuchtlinien (Skunk #1, Haze, Chemdog…) – Quelle fuer Stammbaum-Verifikation | Wissen | 4 | ja |
| JakeTheRabbit/grow-room-training | https://github.com/JakeTheRabbit/grow-room-training | README: Attribution | Textbuch + `grow-room-agent-playbook.md` (LLM-Playbook fuer HA-Steuerung: 4 Balancen, 11 Hebel, 6 Failure Modes, JSON-Schemata) | Wissen/Skill | 3 | ja |
| New-Orbit-Digital/stemma | https://github.com/New-Orbit-Digital/stemma | MIT | Kuratierter Lineage-Katalog (JSON-Karten je Strain mit Quellen + Widerspruchsvermerk), `docs/research/haze.md`, `docs/schema.md`, validate/build (stdlib Python) – Vorbild fuer belegte Stammbaum-Karten | Daten/Wissen | 4 | ja |
| BrooklynCannabisCompany/cannabis-landrace-atlas | https://github.com/BrooklynCannabisCompany/cannabis-landrace-atlas | MIT | Statische Weltkarte der Landrassen, `data/landraces.json` + 455 Write-ups, `docs/taxonomy-guide.md` | Daten/Wissen | 4 | ja |
| Bartlett-Will/garden-wiki | https://github.com/Bartlett-Will/garden-wiki | MIT | 198 MD-Seiten aus "Cannabis Cultivation and Science Podcast" (Science/Practice) | Wissen | 3 | ja |
| JamesTheGiblet/canna-know | https://github.com/JamesTheGiblet/canna-know | MIT | "evidence-base/horticulture.md" u. a.; eher Framework-Prosa, wenig Zucht | Wissen | 2 | ja |
| qnbs/CannaGuide-2025 | https://github.com/qnbs/CannaGuide-2025 | MIT | PWA Grow-Guide/Simulator (DE/EN), Strain-DB, Breeding-Modul im Spiel | Tool/Wissen | 2 | ja |
| J-Stoned/BroBro | https://github.com/J-Stoned/BroBro | README | `kb/cannabis-tissue-culture/` + `tissue-culture-papers/` (Volltexte Medienrezepturen), MCP-Server | Wissen | 3 | ja |
| Verdant-OS/verdant-grow-diary | https://github.com/Verdant-OS/verdant-grow-diary | keine | Grow-Diary-App, `docs/pheno-hunt-lab-territory*.md` (Pheno-Hunt-Datenmodell) | Tool | 2 | ja |

### B. Stammbaum-, Strain- und Genetik-Daten

| Repo | URL | Lizenz | Inhalt kurz | Typ | Rel. | Offline |
|---|---|---|---|---|---|---|
| BUTTERGANG/strain-catalog | https://github.com/BUTTERGANG/strain-catalog | keine | FastAPI-Katalog, `scripts/scrape_seedfinder.py` (41.737 Strains), `seedfinder_enrich.py`, Leafly/Wikileaf-Backfill-JSON; README-Claim 48k Strains / 59k genetische Relationen | Daten/Tool | 5 | ja |
| 0-CYBERDYNE-SYSTEMS-0/CRS-01 | https://github.com/0-CYBERDYNE-SYSTEMS-0/CRS-01 | MIT | "Cannabis Research Sentinel": Evidenz-Graph fuer Lineage mit Trust-Tiers (VERIFIED / COMMUNITY_CONSENSUS 2+ Domains / ANECDOTAL / CONTRADICTED), SQLite-KB, Claim-je-Quelle-Modell, FastAPI+Next.js | Tool/Schema | 5 | ja (ohne Suche) |
| Shannon-Goddard/ci-strains-pro | https://github.com/Shannon-Goddard/ci-strains-pro | MIT | 21k Strains, 50+ Spalten, HTML-verifiziert; `raw-data.csv` (14 MB) + `DATA_DICTIONARY.md`, `BOTANICAL_PATTERNS.md` (Regex fuer Lineage-Extraktion) | Daten | 4 | ja |
| Shannon-Goddard/cannabis-intelligence-database | https://github.com/Shannon-Goddard/cannabis-intelligence-database | MIT, DOI 10.5281/zenodo.17645958 | 15.740 Strains, 8.792 KI-extrahierte Werte (THC/CBD/Sativa-Anteil), REST-API api.loyal9.app | Daten | 4 | ja (CSV) |
| lilbongsai-code/mmj-breeders-catalog | https://github.com/lilbongsai-code/mmj-breeders-catalog | keine | 10.551 Strains / 689 Breeder, community-gepflegt | Daten | 3 | ja |
| zer0pixels0px-dev/cannabis-data-fusion | https://github.com/zer0pixels0px-dev/cannabis-data-fusion | keine | FR "Bloomberg du cannabis": 8-Tabellen-Schema (breeders→cultivars→pedigree mother/father, lab_results, terpenes, cultivation_data, hash_data, market_data), `docs/sources.md` Quellenbewertung (SeedFinder ~20k, Leafly 8.762, GrowDiaries 8.111, Kannapedia 2.411 Genome; Phylos tot) | Schema/Daten | 4 | ja |
| kushyapp/cannabis-dataset | https://github.com/kushyapp/cannabis-dataset | MIT | Tabellen Strains/Products/Brands/Shops (CSV+SQL), 2017 | Daten | 2 | ja |
| MaxValue/Terpene-Profile-Parser-for-Cannabis-Strains | https://github.com/MaxValue/Terpene-Profile-Parser-for-Cannabis-Strains | keine | Scrapy-Parser + CSV-Terpenprofile aus Labor-Webseiten (`labs/`), 137 Sterne | Daten/Tool | 3 | ja |
| MylesLab/cannabis-labelling | https://github.com/MylesLab/cannabis-labelling | keine | Paper-Repo "Cannabis labelling is associated with genetic variation in terpene synthase genes": `data/170428 Bedrocan_chem_sample mg per g.xlsx` (297 Proben Terpene+Cannabinoide), Gen-Annotationen Mono-TPS Chr5 / Sesqui-TPS Chr6, GWAS-R-Code; SNP-Daten auf DRYAD | Paper/Daten | 4 | ja |
| nickpalladino/kannapedia-data | https://github.com/nickpalladino/kannapedia-data | GPL | Kannapedia-Export (712 Genotypen StrainSEEK v1/v2) als `kannapedia.Rda` + VCF, GEBV-Accuracy-Skripte (Genomische Selektion) | Daten/Tool | 4 | ja |
| pkempf/kannapedia-scraper | https://github.com/pkempf/kannapedia-scraper | keine | Python-Scraper Kannapedia (Strain-Seiten) | Tool | 3 | nein |
| Southern-Cross-Plant-Science/HASCH_ILP | https://github.com/Southern-Cross-Plant-Science/HASCH_ILP | MIT, DOI 10.5281/zenodo.11149359 | SNP-Panel-Design (ILP/Gurobi) fuer HASCH Cannabis/Hanf-Genotyping-Plattform | Tool/Paper | 2 | ja |
| terryrabinowitz/Genome-To-Phenome-Prediction | https://github.com/terryrabinowitz/Genome-To-Phenome-Prediction | keine | DL-Modell Terpen/Cannabinoid-Phaenotyp aus Ziel-SNPs (Henry et al. 2018) | Tool/Paper | 2 | ja |
| padgittl/CannabisPangenomeAnalyses (+TerpeneSynthases, ViningLab/CannabisPangenome) | https://github.com/padgittl/CannabisPangenomeAnalyses | keine / GPL-3 | Code+Figuren Cannabis-Pangenom (PAG2024), TPS-Genfamilien | Paper | 2 | ja |
| GMStack/2024_Hemp_Genomes | https://github.com/GMStack/2024_Hemp_Genomes | keine | Stack et al. 2024: 7 de-novo-Assemblies, Rekombinationsraten, `PAR_boundaries` (pseudoautosomale Region X/Y) – Sequenzen entfernt | Paper | 2 | teilw. |
| ahmccormick/Cannabis_Genetics | https://github.com/ahmccormick/Cannabis_Genetics | keine | "Population structure across multiple collections of Cannabis": gefilterte VCFs, PCA/HCPC-CSV, Baeume | Paper/Daten | 2 | ja |
| slavailn/terpene_synthase_project, laullamas/tps-cannabis-phylogeny | github.com/slavailn/terpene_synthase_project | keine | TPS-Gendetektion / Phylogenie (MAFFT+PhyML) | Paper | 2 | ja |
| openthc/vdb | https://github.com/openthc/vdb | GPL-3 | Variety-DB mit stabilen UUIDs je Sorte (Industrie-Datenmodell) | Daten | 2 | ja |
| the1truedan/cmip-terpene-db | https://github.com/the1truedan/cmip-terpene-db | MIT | Schema-Ideen Terpen/Cultivar-DB (keine Daten) | Schema | 2 | ja |
| Banjerr/OpenTerps, Piyush-Bhor/The_Cannabis_API, Loyal9-Elements/grow_search | – | MIT u. a. | Terpen-API (Go), Strain-REST-API (Node/Mongo), Strain-Suche 1.000+ | Daten | 2 | teilw. |
| ATreesThrowaway/leafly_strain_vis, imperfiktillusion/weedtree, alexthegoodman/nugtree, Skewtoob/cannabis-lineage | – | keine | Lineage-Visualisierer (D3/HTML), Skewtoob = "Lineage-Visualizer + Breeding-Project-Planner" (Claude-generiert, WIP) | Tool | 2–3 | ja |
| tytydraco/leafly-strain-scraper, EthanHolleman/leafly_scraper | – | BSD / keine | Leafly-Scraper (Python) | Tool | 2 | nein |
| hdb/seedfinder-python, fiorellis/seedfinder-genotyper | – | MIT / keine | Nutzen die **abgeschaltete** SeedFinder-API (Genotyper: Anteilsberechnung aus Stammbaum – Algorithmus-Idee uebernehmbar) | Tool | 2 | nein |
| Venosta-web/growspace_manager | https://github.com/Venosta-web/growspace_manager | MIT | HA-Integration (HACS): Pflanzen-Lifecycle, Crop-Steering, **`services/seedfinder_scraper.py`** (HTML-Scraper seedfinder.eu inkl. Cloudflare-403-Handling), `websocket/strain.py`, Tests `test_strain_ancestry.py` | Tool | 4 | ja |
| Tegridy539/MyGrowBuddy | https://github.com/Tegridy539/MyGrowBuddy | keine | `backend/app/importers/seedfinder.py`: stdlib-HTML-Parser fuer seedfinder.eu/strain-info (JSON-LD-Auswertung, URL-Normalisierung) | Tool | 3 | ja |
| jluna0413/CultivAREmergent | https://github.com/jluna0413/CultivAREmergent | README | `app/services/agents/seedfinder_scraper.py` + `genetics_data_agent.py` (Agent-Pattern) | Tool | 2 | ja |
| cannlytics/cannabis-data-science, cannlytics/cannabis_results | https://github.com/cannlytics | MIT / CC | Notebooks + "995K+ COAs aus 14 Staaten" (Datenlinks im Repo), Laborergebnis-Statistik | Daten | 3 | teilw. |

### C. Zucht-Tools, Simulation, Genetik-Rechner

| Repo | URL | Lizenz | Inhalt kurz | Typ | Rel. | Offline |
|---|---|---|---|---|---|---|
| HighlanderLab/jbancic_alphasimr_plants | https://github.com/HighlanderLab/jbancic_alphasimr_plants | MIT | R-Skripte Bancic et al. 2024 (Crop Science): Simulation Linien-/Hybrid-/Klonzucht, Rueckkreuzung, genomische Selektion mit AlphaSimR | Tool | 3 | ja (R) |
| piercetaylor/backcross | https://github.com/piercetaylor/backcross | MIT | Browser-App: Recurrent-Parent-Genome-Recovery aus SNP-Genotypen (VCF/HapMap/CSV), Donor-Segmente, BrAPI-Loader | Tool | 3 | ja |
| zankrut20/selection.index | https://github.com/zankrut20/selection.index | GPL-3 | CRAN-Paket Selektionsindex (Smith-Hazel) fuer Mehrmerkmalsselektion | Tool | 3 | ja (R) |
| AI-for-Genome-Interpretation-lab/meiosim | https://github.com/AI-for-Genome-Interpretation-lab/meiosim | GPL-3 | Python: Meiose/Kreuzungen simulieren, Genotyp+Karte-Datenstruktur | Tool | 3 | ja |
| mtwatso2-eng/pedigree-toolbox | https://github.com/mtwatso2-eng/pedigree-toolbox | keine | R-Shiny Pedigree-Visualisierung/Analyse (BreedBase) | Tool | 2 | ja (R) |
| anealchandra/kdlogue | https://github.com/anealchandra/kdlogue | GPL-3 | C++-Builder Saatgut-Inventar fuer Pflanzenzuechter (Barcode, Waage; braucht KDDart) | Tool | 1 | nein |
| Tea4Q/MySeedBook | https://github.com/Tea4Q/MySeedBook | keine | Expo/RN Saatgut-Inventar (Provenienz, Barcode) | Tool | 2 | ja |
| jkh2/pheno-hunter-game | https://github.com/jkh2/pheno-hunter-game | README | Single-HTML Zucht-Simulator: Allelmodell `makeAlleles` (Dominanz-Parameter je Trait), Stabilitaetswert, LLM-"Lab-Partner" | Tool | 2 | ja |
| EddiePiazza/schedule-4-real | https://github.com/EddiePiazza/schedule-4-real | source-available | Grow-Control + "Breeding Planner" + Phenotype Tracking, HA-Integration, Spider Farmer | Tool | 3 | ja |
| MalloyTheDev/growforge | https://github.com/MalloyTheDev/growforge | MIT | Offline C++/Qt Grow-Tracker: Cloning, Breeding, Pheno-Hunt, Rechner, SQLite | Tool | 3 | ja |
| AFICIONADOSEEDS/GENETRAKR | https://github.com/AFICIONADOSEEDS/GENETRAKR | AGPL-3 | Breeding-Management + Raum-Spatialplanung (JS) | Tool | 2 | ja |
| balugabrell-sys/Cultivar-Breeding-Tracker-3.0, lilfirecracker2281/strain-lab, joeydouglas/mule-fuel-x-nana-glue | – | keine | Kleine Breeding-Tracker (JS/Python-Dashboard) – Feldideen | Tool | 1 | ja |
| LJrobinson/CannabisCOA.Parser | https://github.com/LJrobinson/CannabisCOA.Parser | keine | C# COA-PDF/Text-Parser -> JSON/CSV | Tool | 3 | ja |
| CannabisData/cannapy | https://github.com/CannabisData/cannapy | MIT | Python-Modul fuer Cannabis-Daten | Tool | 1 | ja |

### D. Grow-Ops / Automation / Rechner

| Repo | URL | Lizenz | Inhalt kurz | Typ | Rel. | Offline |
|---|---|---|---|---|---|---|
| JakeTheRabbit/HAGR | https://github.com/JakeTheRabbit/HAGR | MIT | Home-Assistant-Growroom: VPD-Klima, 4-Phasen Crop-Steering, Dosierung, ESPHome; `growingSOPs/Indoor Pathogens.md` | Tool/Wissen | 3 | ja |
| Intergalactic-XYZ/awesome-cropsteering | https://github.com/Intergalactic-XYZ/awesome-cropsteering | MIT | Awesome-Liste Grow-Automation (HA, Node-RED, ESPHome, Rechner, MQTT) | Liste | 3 | ja |
| JakeTheRabbit/awesome-grow-room-parts | https://github.com/JakeTheRabbit/awesome-grow-room-parts | CC | Teilekatalog + I2C-Map + ESPHome-Beispiele | Liste | 2 | ja |
| dwot/isley | https://github.com/dwot/isley | MIT | Self-hosted Grow-Journal (Go), AC-Infinity/Ecowitt-Sensoren, Seeds+Harvest-Tabellen | Tool | 3 | ja |
| ober37/ac-infinity-mcp | https://github.com/ober37/ac-infinity-mcp | MIT | MCP-Server AC-Infinity (VPD-Trends, Port-Steuerung, Dry-Run) | MCP | 3 | nein (Cloud-API) |
| OKlueck/VPD-Calc, dlazarogi/VPD-calculator | – | ? / CC | VPD-Rechner (offline-HTML; Python Leaf/Air/Hybrid) | Tool | 2 | ja |
| CannabisAnbau/Cannabis-Anbau | https://github.com/CannabisAnbau/Cannabis-Anbau | GPL-3 | DE: Stromkosten-, Cal/Mag-, Naehrstoffrechner (HTML) | Tool | 2 | ja |
| DeltaLima/CanGrow | https://github.com/DeltaLima/CanGrow | README | ESP8266/ESP32 Growbox-Firmware mit Web-UI | Tool | 2 | ja |
| Franzferdinan51/CannaAI | https://github.com/Franzferdinan51/CannaAI | MIT | CV-Diagnose, Journal, Tent-Monitoring, "Breeding Tools" (TS) | Tool | 2 | teilw. |

### E. Agent-Skills / MCP

| Repo | URL | Lizenz | Inhalt kurz | Typ | Rel. | Offline |
|---|---|---|---|---|---|---|
| K-Dense-AI/scientific-agents | https://github.com/K-Dense-AI/scientific-agents | MIT | `scientific-agents/plant-breeder/skills/plant-breeder/SKILL.md` (R = h²S, BLUP/GBLUP, Selektionsindex, Linkage Drag, G×E, Seed-Purity), `horticulturist/SKILL.md` | Skill | 5 | ja |
| stanfish06/skillquarium | https://github.com/stanfish06/skillquarium | keine | Skill-Sammlung (beschnitten auf 31 Pflanzen-/Genetik-Skills: plant-breeder, geneticist, population-geneticist, cytogeneticist, horticulturist, plant-pathologist, gwas-*) | Skill | 3 | ja |
| human-avatar/skills-for-agriculture | https://github.com/human-avatar/skills-for-agriculture | MIT | 48 Claude-Skills `s4ag-*`: seeds (Isolationsabstaende, Mindestpopulation, Lagerung – Deppe/Ashworth), propagation, controlled-environment, pests, mycology | Skill | 3 | ja |
| Ryukijano/agent-skills | https://github.com/Ryukijano/agent-skills | README | `ai-for-plant-breeding/SKILL.md` (genomische Vorhersage rrBLUP/GBLUP, G×E, Verifikation) | Skill | 3 | ja |
| modbender/skill-library-mcp (beschnitten) | https://github.com/modbender/skill-library-mcp | MIT | `data/cannabis-cultivator/SKILL.md` (EU-Seedbank-Metasuche, Filterlogik), `gardening`, `plant-tracker`, `seasonal-planting-guide` | Skill | 2 | ja |
| avlihachev/claude-skill-garden | https://github.com/avlihachev/claude-skill-garden | README | Garten-Skill mit Pflanzen-Tracker/Journal-Schema (JSON) – Vorlage fuer Grow-Journal-Skill | Skill | 2 | ja |
| cyanheads/brapi-mcp-server | https://github.com/cyanheads/brapi-mcp-server | Apache-2 | BrAPI v2.1 MCP (Germplasm, Pedigree, Genotypen) – Standard-Datenmodell fuer Zuchtdaten | MCP | 3 | nein |
| AgentDank/dank-mcp | https://github.com/AgentDank/dank-mcp | MIT | MCP ueber DuckDB-Cannabis-Datensaetze (CT) | MCP | 2 | ja |
| Weedcommerce/smoke-ai-mcp | https://github.com/Weedcommerce/smoke-ai-mcp | MIT | Remote-MCP 17 Tools, 9.500 Strains (US-Markt) | MCP | 2 | nein |
| rootsbymenda/cannabis-mcp-server | https://github.com/rootsbymenda/cannabis-mcp-server | MIT | Regulatorik-MCP (US/Intl) | MCP | 1 | nein |
| _ref_skills/ (Rohdateien) | Klotzkette/claude-fuer-deutsches-recht | – | `strafrecht-spezial-kcang-cannabisgesetz-konsum-besitz/SKILL.md`, `…-anbauvereinigung-cannabis-club/SKILL.md` (nur Referenz, Phil hat recht/-Skills) | Skill/Recht | 2 | ja |

### F. Recht DE (nur Referenz)

| Repo | URL | Lizenz | Inhalt kurz | Typ | Rel. | Offline |
|---|---|---|---|---|---|---|
| legalize-dev/legalize-de | https://github.com/legalize-dev/legalize-de | MIT | `de/KCANG.md` Volltext (§ 9: max. 3 Pflanzen gleichzeitig am Wohnsitz; § 9 Abs. 2 Weitergabeverbot; § 10 Schutz von Cannabis **und Vermehrungsmaterial**; § 4 Abs. 2 Samenimport nur aus EU-Staaten), `MEDCANG.md`, BtMG-Texte | Recht | 3 | ja |
| eriklueth/gesetze-corpus-data | https://github.com/eriklueth/gesetze-corpus-data | CC | KCanG paragraphenweise (`laws/BJNR06D0B0024/paragraphs/0009.md`) | Recht | 2 | ja |
| konradvoelkel/bubatzblick | https://github.com/konradvoelkel/bubatzblick | AGPL-3 | § 5 KCanG Verbotszonen (100 m Sichtweite) aus OSM, Rust | Recht/Tool | 1 | ja |
| saschadaemgen/cannaUNITY | https://github.com/saschadaemgen/cannaUNITY | MIT (archiviert) | Anbauvereinigungs-Framework (Mitglieder, Track&Trace, UniFi) | Tool | 1 | ja |

Nicht geklont, aber gesichtet (0–1 Sterne, Spiele/Spam/Shops): weed-breed-js, cannabisbreedingsimulator, straingame, greed-and-gross, Ganja-TUI, CANNA-CULTIVATOR, CannabisCoin, diverse Seedshop-Landingpages.

## Datenquellen & Datensaetze

| Quelle | URL | Inhalt | Zugang | Format |
|---|---|---|---|---|
| SeedFinder | https://seedfinder.eu | ~20.000–41.000 Sorten, Eltern/Stammbaum, Bluetezeit, Breeder | API abgeschaltet (seedfinder-genotyper-README); HTML hinter Cloudflare, Scraper in growspace_manager/MyGrowBuddy/strain-catalog | HTML/JSON-LD |
| Kannapedia (Medicinal Genomics) | https://www.kannapedia.net | 712 (2020) bis 2.411 Genome (2026, cannabis-data-fusion), StrainSEEK v2: 3,5 Mb Zielsequenz, 29 Cannabinoid/Terpen-Synthase-Gene, ~30k SNPs, genetische Distanz, Chemotyp | Webseite, VCF je Probe; Export in nickpalladino/kannapedia-data (`kannapedia.Rda`, `vcf/`) | VCF/Rda |
| cs10 / CBDRx Referenzgenom | https://www.ncbi.nlm.nih.gov/assembly/GCF_900626175.2 | Referenz (Grassa et al. 2021), neue Chromosomennummerierung ab 2020 (MylesLab-README) | NCBI Assembly (hier nicht erreichbar) | FASTA/GFF |
| Cannabis-Pangenom | github.com/ViningLab/CannabisPangenome, padgittl/* | 7+ Assemblies, TPS-Genfamilien, TE-Analysen (PAG2024-Material) | GitHub | Code/HTML |
| Stack et al. 2024 Hemp Genomes | github.com/GMStack/2024_Hemp_Genomes | 7 de-novo-Genome, Rekombinationsraten, PAR-Grenzen | GitHub (Annotation/Fasta ~1,3 GB, nicht behalten) | GFF3/FASTA |
| MylesLab Bedrocan-Chemiedaten | github.com/MylesLab/cannabis-labelling | 297 Proben Terpene+Cannabinoide (mg/g), TPS-Gen-Positionen Chr5/Chr6; SNP-Daten auf DRYAD | GitHub / DRYAD | XLSX/TXT/PLINK |
| ci-strains-pro / cannabis-intelligence-database | github.com/Shannon-Goddard/* | 21k bzw. 15,7k Strains mit THC/CBD/Lineage-Feldern; DOI zenodo.17645958 | GitHub CSV / REST api.loyal9.app | CSV/JSON |
| strain-catalog Backfills | github.com/BUTTERGANG/strain-catalog/data | `sf_backfill_v2.json`, `leafly_backfill.json`, `wikileaf_strains.csv`, Lineage-Checkpoints | GitHub | JSON/CSV |
| Stemma Lineage-Karten | github.com/New-Orbit-Digital/stemma/catalog/strains | belegte Eltern/Landrassen-Karten mit Quellen | GitHub | JSON |
| Landrace Atlas | github.com/BrooklynCannabisCompany/cannabis-landrace-atlas/data | `landraces.json` + Write-ups | GitHub | JSON/MD |
| Prime Cuts Gists | README johnhouston707/cannabis-cultivation-resources | Genetics-Network JSON, Terpene JSON | gist.github.com | JSON |
| Cannlytics Lab-Results | github.com/cannlytics/cannabis_results | "995K+ COAs aus 14 US-Staaten" (Links/Loader) | GitHub + extern (HF/Zenodo lt. Repo) | CSV/Parquet |
| Kushy Dataset | github.com/kushyapp/cannabis-dataset | Strains/Products/Shops 2017 | GitHub | CSV/SQL |
| Terpene-Profile-Parser | github.com/MaxValue/… `labs/*/`.csv | Laborterpenprofile je Sorte | GitHub | CSV |
| Open Cannabis Project / Phylos Galaxy | – | laut cannabis-data-fusion/docs/sources.md: Phylos "tot" (Archiv: EBI-EVA, BigQuery); OCP nicht mehr aktiv – keine aktiven GitHub-Repos gefunden | Archiv | – |
| NCBI SRA Cannabis | https://www.ncbi.nlm.nih.gov/sra (Suche "Cannabis sativa") | Rohsequenzen (Jamaican Lion, CBDRx, Purple Kush…) | NCBI (nicht erreichbar in dieser Session) | FASTQ |
| BrAPI-Server (T3, Breedbase) | via cyanheads/brapi-mcp-server | Germplasm/Pedigree-Standardmodell (kein Cannabis-Inhalt, aber Schema) | MCP | JSON |
| canna-transcripts | github.com/muf4/canna-transcripts/transcriptions | 279 Breeders-Syndicate-Folgen u. a. (Oral History der Sorten) | GitHub | TXT |
| KCanG Volltext | github.com/legalize-dev/legalize-de/de/KCANG.md | Gesetzestext | GitHub | MD |

## Wissen in Regeln: die 25 wichtigsten belegten Breeding-Fakten/Regeln

Belegform: `Repo-Pfad` (Primaerzitat im Repo). Nicht live gegengeprueft = (S).

1. **Chemotyp = ein Locus (B) mit kodominanten Allelen B_T/B_D.** F2 aus Typ I × Typ III spaltet 1 : 2 : 1 (THC-dominant : gemischt : CBD-dominant). de Meijer et al. 2003, Genetics 163:335 – `JakeTheRabbit__cannabis-white-papers/papers/cannabinoids-terpenes.md` Z. 159/382 (S).
2. **Der Locus steuert das Verhaeltnis, nicht die Menge.** Gesamt-Cannabinoidgehalt ist polygen + Umwelt (Licht, Reife, Kronendach). Ebd. Z. 163; Small 1979 via `HomunculusLabs__Farming-KB/concepts/cannabis-chemotype-classification-cannabinoid-breeding.md`.
3. **Fuenf Chemotypen:** I THC-dominant, II gemischt, III CBD-dominant, IV CBG-dominant (nachgeschaltete Synthasen defekt), V cannabinoidfrei (rezessives Allel o/o, wieder 1 : 2 : 1). de Meijer 2009 Euphytica 168:95; McPartland 2018 – `cannabinoids-terpenes.md` Z. 159–161; `RAFOUgg__Reviews-Maker/.../05_GENETIQUE_GENEALOGIE.md` §3 (S).
4. **Chemotyp ist vor der Bluete testbar** (Blattprobe/Marker THCAS/CBDAS). Toth et al. 2020 GCB Bioenergy 12:213 – `genetics-phenohunting.md` Tabelle "Uses and limits of genetic tests" (S).
5. **Cannabis: 2n = 20, 9 Autosomenpaare + XY; dioezisch, windbestaeubt; Bluete durch Nachtlaenge.** Divashuk 2014 – `cannabis-white-papers/papers/plant-biology.md` Z. 40–47 (S).
6. **Geschlecht per PCR-Marker im Keimlingsstadium bestimmbar**, Wochen vor Vorblueten (Toth 2020). Ohne Test: Vorblueten Woche 4–6 Veg; Maennchen zeigen ~3–4 Wochen nach Keimung, 1–2 Wochen vor Weibchen; nach Bestaetigung 7–10 Tage bis Pollenflug. `genetics-phenohunting.md` Schritt 3; `akravetz__dirt/wiki/breeding/male-evaluation.md`.
7. **Feminisierung = STS blockiert Ethylen-Rezeptoren** (Ag+), kein Eingriff in die DNA; wenige Spruehungen um den 12/12-Flip, Pollen Wochen spaeter; korrekt gemachtes Saatgut ≈ 100 % weiblich. Ram & Sett 1982 TAG 62:369; Lubell & Brand 2018 HortTechnology 28:743; Flajsman 2021 Front Plant Sci 12:718092; "Optimized guidelines for feminized seed production" 2024 Front Plant Sci 15:1384286 – `genetics-phenohunting.md` Abschnitt Seed types (S).
8. **Hermie-Risiko kommt aus der Elternwahl (Rodelization/Stress-Selbstung), nicht aus STS.** Punja & Holmes 2020 Front Plant Sci 11:718 – ebd. (S). Regel: jedes Maennchen oder reversierte Weibchen mit Pistillen/Spontan-Bananen = Cull (`male-evaluation.md` Krit. 7).
9. **S1 ist nicht der Klon:** jeder heterozygote Locus spaltet weiter; S1 = verwandte Population. `genetics-phenohunting.md` "S1 seed".
10. **Autoflower1 ist rezessiv**: Auto × Photoperiod → F1 alle photoperiodisch (Traeger); Auto-Trait erst in F2 (¼) oder per Rueckkreuzung. Toth et al. 2022 Front Plant Sci 13:991680 – ebd. (S); Introgression als Backcross-Problem: `Farming-KB/concepts/autoflowering-breeding.md`.
11. **Pheno-Hunt-Grundregel: Stecklinge von JEDER Pflanze vor dem 12/12-Flip** (2–3 je Pflanze), sonst ist der Keeper bei der Ernte verloren. `genetics-phenohunting.md` Schritt 5; `dirt/pheno-hunt-protocol.md`.
12. **Stichprobengroesse:** Keeper-Frequenz ~1/20 bei guter Kreuzung → 10 Samen ≈ 40 % Chance, 50 Samen > 90 %; bei regulaerem Saatgut N halbieren (Maennchen). "10 Samen gekeimt" heisst meist "beste von ~4 Weibchen". `genetics-phenohunting.md` "Limits of the sample size". Prime Cuts: min. 10, besser 20–50 Samen je Kreuzung (`phenotype-selection-guide.md`); Medcan: 100+ (`advanced_breeding.md`).
13. **Scoring-Tabelle VOR der Keimung schreiben** (Kriterien, Gewichte, Cull-Schwellen) – Halo-Effekt vermeiden; Kriterien: Chemotyp/Potenz, Terpene (W6 + nach Cure), Trockenertrag, Struktur, Bluetezeit (Tage ab Flip bis Trichomreife), Schimmel/Pest, Hash-Waschtest, Bewurzelungsrate, Stretch (Hoehe Peak/Flip, Tag 21). Gewichte Beispiel Commercial/Personal: Ertrag 25/10, Bag Appeal 20/15, Terpene 15/30, Potenz 10/25, Schwierigkeit 15/5, Finish 15/15. `genetics-phenohunting.md` Tabelle; `cannabis-cultivation-resources/phenotype-selection-guide.md`.
14. **Positionen woechentlich rotieren**, gleiche Toepfe/Medium/Feed; nie in Woche 3 selektieren; **Keeper erst nach Runde 2 aus Backup-Stecklingen** ("one crop is a test, two crops make a cultivar"). `genetics-phenohunting.md` Schritte 6–9.
15. **Keeper-Redundanz:** ≥ 2 Mutterpflanzen (getrennte Raeume), bewurzelte Backup-Stecklinge, HpLVd-Test vor Mutterstatus, Gewebekultur-Archiv frueh (Mutationslast ∝ Zahl der Subkulturen, r > 0,92, Adamek 2024). `genetics-phenohunting.md` "Maintenance of a keeper clone"; `mother-plants.md` Ref. 8 (S).
16. **HpLVd-Zahlen:** ~90 % der CA-Betriebe positiv, ~30 % der Pflanzen; THC −50…70 %; mechanische Uebertragung (Klinge), Saft ~7 Tage, Trockenmaterial ~4 Wochen infektioes; Wurzel-zu-Wurzel in Rezirkulation ≤ 2 Wochen; nach Stichinfektion Wurzeln 2–3 Wo, Blatt erst 4–6 Wo positiv → **Wurzelprobe, Test alle 4–6 Wochen, vor jeder grossen Steckling-Ernte**; 10 % Bleiche oder neue Klinge je Pflanze, Isopropanol unwirksam; Meristemkultur-Bereinigung ⌀ ~41 % (0–100 % je Genotyp); Samenuebertragung lt. 2025-Studie bis 100 % je Los → jedes Los testen. Punja 2025 Plants 14:830; Adkar-Purushothama 2023 Viruses 15:681 – `mother-plants.md` Z. 69–222, `tissue-culture.md` Z. 112 (S).
17. **Pollenlagerung:** offen 1–2 Wochen; dicht RT 2–4 Wochen; Kuehlschrank 4 °C + Trockenmittel 3–6 Monate; **Gefrierer −18 °C, 24–48 h getrocknet, mit Mehl 4:1 gestreckt, vakuumiert, Einmal-Aliquots: 18–24 Monate**; LN2 8+ Jahre. Nie auftauen und wieder einfrieren. `dirt/wiki/breeding/pollen-handling.md` (Praxiswerte, nicht peer-reviewed); Clarke: trocken, Trockenmittel, frueh morgens sammeln (`Farming-KB/concepts/cannabis-pollen-collection-storage-clarke.md`).
18. **Pollenernte:** wenn ~33 % der Saecke aufplatzen, 3 Sessions im Abstand 2–3 Tage, mittags bei RH < 50 %, Ventilator aus; 0,5–2 g je Maennchen, 0,1–0,2 g reichen fuer eine Kreuzung; je Maennchen eigenes Papier/Gefaess, Lots nie mischen. `pollen-handling.md`.
19. **Bestaeubungsfenster:** Stigmen frisch, weiss, klebrig = Woche 2–3 (Tag 14–18 nach Flip); ab Woche 4 faellt die Rezeptivitaet, nach Woche 5 gering. Nur 1–2 untere Aeste bestaeuben (100–500 Samen/Ast), Ast sofort etikettieren (Eltern × Datum × Position), optional 24 h Beutel; Rest der Pflanze mit Wasser nebeln (denaturiert Streupollen); Handschuhe/Maske, danach duschen. `dirt/wiki/breeding/cross-procedure.md`.
20. **Maennchen bewerten statt "Pollenfabrik":** Stamm/Petiolenfarbe (Anthocyan-Proxy), Vigor (Tage bis Vorbluete, Nodien/Woche), Struktur, Blattform, **Stem-Rub-Aroma**, Sackdichte, Hermie = K.o. `male-evaluation.md`. Clarke: Maennchen zeigen dieselben Cannabinoid-Verhaeltnisse wie Weibchen, nur geringer – Chemotyp-Marker am Maennchen nutzen (`cannabis-chemotype-classification-cannabinoid-breeding.md`).
21. **Familienselektion:** "Individuen nach Phaenotyp selektieren, Familien nach Nachkommenleistung weiterfuehren." Standard 2×2 (4 F3-Familien), Screening 4–8 Samen/Familie, Sieger 8–16; Gewinnerfamilie + max. 1 Backup; keine volle 4×4-Matrix bei 16 Plaetzen. `dirt/wiki/breeding/family-selection.md`.
22. **Stabilitaetsschwellen:** < 70 % on-target = nicht stabil (zurueck zu Familienselektion/BX); 70–90 % = Selektionsmaterial; **> 90 % on-target Weibchen, einmal wiederholt = Produktionslos**; Nenner protokollieren (gekeimt, gecullt + Grund, geblueht, on-target, Hermies). `dirt/wiki/breeding/feminized-production.md`.
23. **Rueckkreuzung:** nur fuer einfach vererbte, leicht bonitierbare Merkmale (Schimmelresistenz, Bluetezeit, Auto); rekurrenter Elter = fast ideale Sorte. Erwartete Genomanteile des rekurrenten Elters BC1 75 %, BC2 87,5 %, BC3 93,75 % (Standardgenetik; `piercetaylor/backcross` misst das real per SNP); Szene: "BX3 = auf den Elter stabilisiert". `Farming-KB/concepts/cannabis-backcrossing-breeding.md` (Cervantes); `dirt/nomenclature.md`.
24. **IBL/Fixierung:** F1 = uniform + Heterosis, F2 = maximale Aufspaltung (hier wird gejagt), ab F3 Varianz pro Generation enger bei konsequenter Selektion; **nach 5–6 Generationen sind die meisten Merkmale fixiert** (Clarke). Inzuchtdepression beobachten (Fertilitaet/Vigor), Populationsgroesse halten. `dirt/nomenclature.md`; `Farming-KB/concepts/cannabis-breeding-techniques-acclimatization-trait-fixing-clarke.md`; `K-Dense plant-breeder/SKILL.md` (R = h²·S; Gewinn = Intensitaet × Genauigkeit × σA / Generationszeit).
25. **Sortennamen sind keine Genotypen:** > 35 % der als "Sativa" verkauften Sorten genetisch von Indica-Linien ununterscheidbar (Sawler 2015, PLoS ONE 10:e0133292); gleiche Namen ≠ gleiche Genetik (Schwabe & McGlaughlin 2019). → Stammbaum-DB immer mit Quelle + Trust-Tier fuehren (CRS-01-Modell), Chemotyp/Genotyp ueber Name. `Reviews-Maker/05_GENETIQUE_GENEALOGIE.md` §3; `genetics-phenohunting.md` Ref. 4–5 (S).
26. (Bonus) **Saatgutlagerung:** kuehl, dunkel, trocken, dicht im Kuehlschrank; jahrelang keimfaehig, Keimrate sinkt mit Alter/Lipidoxidation (Cockson 2025); reife Samen hart, dunkelbraun, "Tigerstreifen"; frisches fem. Saatgut > 90 % Keimrate. `cannabis-white-papers/papers/seeds-germination.md` Z. 80–207 (S).
27. (Bonus) **Mutterpflanzen bleiben bei 18 h vegetativ; Bluete wurde bei allen getesteten Sorten schon bei 14 h Licht ausgeloest** (Ahrens 2023, Plants 12:2605) → Langtag fuer Muetter nicht unter 16 h. `mother-plants.md` Ref. 1 (S).
28. (Bonus, Recht) **KCanG § 9: max. 3 Pflanzen gleichzeitig am Wohnsitz, keine Weitergabe; § 10: Vermehrungsmaterial (Samen, Stecklinge) vor Dritten/Kindern sichern; § 4 Abs. 2: Samenimport nur aus EU-Mitgliedstaaten.** → Zuchtprogramm zu Hause = 3-Pflanzen-Budget (z. B. 1 Mutter + 1 bestaeubtes Weibchen + 1 reversiertes/maennliches Elter); groessere Pheno-Hunts nur ueber Anbauvereinigung (§§ 11 ff.). `legalize-dev__legalize-de/de/KCANG.md` Z. 183, 255–263.

## Tools zum Uebernehmen

| Pfad (unter repos_breeding/) | Was es tut | Model-Tier Agent |
|---|---|---|
| `JakeTheRabbit__cannabis-white-papers/llms-full.txt` + `papers/*.md` | RAG-Korpus (CC BY-NC) fuer alle Grow-/Zucht-Fragen mit Zitaten | haiku (Retrieval) / sonnet (Antwort) |
| `akravetz__dirt/wiki/breeding/*.md` | Protokoll-Vorlagen: Pheno-Hunt, Pollen, Kreuzung, Familienselektion, Feminisierung, Nomenklatur → direkt als Vault-Templates uebernehmen | sonnet |
| `0-CYBERDYNE-SYSTEMS-0__CRS-01/backend/src/graph/kb.py`, `SPEC.md` | Claim-/Trust-Tier-Datenmodell (VERIFIED/CONSENSUS/ANECDOTAL/CONTRADICTED) fuer die Stammbaum-DB; SQLite | sonnet (Portierung), haiku (Betrieb) |
| `BUTTERGANG__strain-catalog/scripts/scrape_seedfinder.py`, `seedfinder_enrich.py`; `Venosta-web__growspace_manager/custom_components/growspace_manager/services/seedfinder_scraper.py`; `Tegridy539__MyGrowBuddy/backend/app/importers/seedfinder.py` | Drei aktuelle SeedFinder-HTML-Parser (JSON-LD, Cloudflare-Handling) – Abgleich mit `stammbaum-crawler` | haiku |
| `Shannon-Goddard__ci-strains-pro/raw-data.csv` + `pipeline/12_botanical_extraction/docs/BOTANICAL_PATTERNS.md` | 21k-Strain-CSV + Regex-Muster fuer Lineage/Chemie-Extraktion aus Freitext | haiku |
| `New-Orbit-Digital__stemma/docs/schema.md`, `tools/validate.py` | Karten-Schema mit Quellen/Widerspruch je Strain; stdlib-Validator | haiku |
| `RAFOUgg__Reviews-Maker/DOCUMENTATION/DATA_REFERENCE/05_GENETIQUE_GENEALOGIE.md` | Feldkatalog GenNode/GenEdge (generation, seedType, pollinationMethod, chemotype I–V, thcSource) – Grundlage fuer Kreuzungs-Schema | sonnet |
| `fiorellis__seedfinder-genotyper/index.html` | Algorithmus "genetische Zusammensetzung aus Stammbaum" (Anteile je Vorfahr) – auf edges.csv portieren | haiku |
| `piercetaylor__backcross/` | Browser-App Recurrent-Parent-Recovery aus SNP (falls StrainSEEK/HASCH-Daten vorliegen) | sonnet |
| `zankrut20__selection.index/` (R, CRAN) | Smith-Hazel-Selektionsindex fuer Mehrmerkmals-Scores | sonnet |
| `HighlanderLab__jbancic_alphasimr_plants/` | Simulationen fuer "wie viele Generationen/Samen bis Zielfrequenz" (AlphaSimR) | opus (Modellierung) |
| `AI-for-Genome-Interpretation-lab__meiosim/` | Python-Kreuzungssimulator (Punnett fuer n Loci, Mendel-Ratios) | haiku |
| `K-Dense-AI__scientific-agents/scientific-agents/plant-breeder/skills/plant-breeder/SKILL.md` | Denkrahmen Pflanzenzuechter (h², R = h²S, G×E, Index) → als Sub-Skill fuer Breeding-Agent | sonnet |
| `human-avatar__skills-for-agriculture/skills/s4ag-seeds/SKILL.md` | Saatgut-Lagerung/Isolation/Mindestpopulation (allgemein) | haiku |
| `johnhouston707__cannabis-cultivation-resources/phenotype-selection-guide.md`, `hlvd-prevention-protocol.md` | Scoring-Matrix + HLVd-SOP (Testintervalle, Desinfektion) | haiku |
| `JakeTheRabbit__grow-room-training/docs/training/grow-room-agent-playbook.md` | Agenten-Playbook Klima/Hebel/Failure-Modes (HA) | sonnet |
| `JakeTheRabbit__HAGR/`, `Intergalactic-XYZ__awesome-cropsteering/README.md` | HA/ESPHome-Konfigurationen, Rechner-Links | haiku |
| `dwot__isley/` | Self-hosted Grow-Journal mit Seeds/Harvest-Tabellen (Go, Docker) | – (Betrieb) |
| `MalloyTheDev__growforge/` | Offline Qt-Tracker mit Breeding/Pheno-Hunt-Modul – Feld-/Tabellenmodell als Referenz | haiku |
| `LJrobinson__CannabisCOA.Parser/` | COA-PDF → JSON/CSV (C#); fuer Laborwerte je Phaeno | haiku |
| `MylesLab__cannabis-labelling/data/*.xlsx` | 297-Proben-Chemiedatensatz fuer Terpen-Cluster/Referenzwerte | haiku |
| `nickpalladino__kannapedia-data/*.R` | GEBV/genomische Selektion mit Kannapedia-SNPs (Vorlage) | opus |
| `OKlueck__VPD-Calc/`, `dlazarogi__VPD-calculator/`, `CannabisAnbau__Cannabis-Anbau/` | VPD (Blatt/Luft), Stromkosten, Cal/Mag, Naehrstoff – DE-Rechner | haiku |
| `legalize-dev__legalize-de/de/KCANG.md` | Gesetzestext fuer Zitate (§ 4, 9, 10) | haiku |
| `muf4__canna-transcripts/transcriptions/The Breeders Syndicate 3.0/` | Volltextsuche nach Sortengeschichte zur Verifikation von edges.csv | haiku |

## Luecken (muss gebaut werden)

1. **Breeding-Pair-Planner auf der Stammbaum-Datenbank**: aus `edges.csv/verwandtschaft.csv` Inzuchtkoeffizient/Verwandtschaft (Wright-Pfadmethode) je Kandidatenpaar, Chemotyp-Erwartung (B_T/B_D-Punnett), Auto-Traegerstatus, Hermie-Flags; Ausgabe: Ranking + erwartete F1/F2-Aufspaltung. Kein Repo liefert das (CRS-01 nur Graph, seedfinder-genotyper nur Anteile).
2. **Phenotype-Scoring-Sheet (Vault-Template + CSV-Schema)**: Pflanzen-ID = Packungscode+Samen-Nr., Wochen-Scores, Gewichte vorab, Cull-Schwellen, Runde-2-Vergleich; Vorlagen: white-papers-Tabelle, Prime-Cuts-Matrix, dirt/pheno-hunt-protocol.
3. **Saatgut-/Pollen-Inventar**: Lot-ID, Eltern (Mutter × Vater/Donor), Methode (regular/STS-fem/S1/BX), Datum, Anzahl, Lagerort/Temperatur, Keimtest-Ergebnisse, Aliquot-Verbrauch; kein brauchbares offline-Tool gefunden (MySeedBook = Gemuese, kdlogue = KDDart).
4. **Kreuzungs-Register (GenEdge)**: `pollinationMethod`, Astposition, Bestaeubungstag ab Flip, Samenertrag, Progeny-Test-Nenner (gekeimt/gecullt/on-target/Hermies) – Schema aus Reviews-Maker + dirt uebernehmen.
5. **Trust-Tier-Spalte in verwandtschaft.csv** (SeedFinder = ANECDOTAL, 2+ unabhaengige Quellen = CONSENSUS, Breeder-Originalangabe = VERIFIED) + Widerspruchsliste.
6. **Chemotyp-/Marker-Datenfeld** je Linie (Typ I–V, Bt/Bd-Genotyp wenn getestet, Auto1-Status) und Laboranbindung (COA-Parser → Phaeno-ID).
7. **KCanG-Compliance-Check im Planner**: 3-Pflanzen-Budget simultan, Reversions-/Bestaeubungsplan zeitlich staffeln (Mutter, Donor, Samentraegerin), Samenbezug nur EU; Anbauvereinigung als Option fuer groessere Populationen.
8. **Simulations-Notebook** (meiosim/AlphaSimR): "Wie viele Samen pro Generation fuer p(Keeper) ≥ 90 % bei Keeper-Frequenz 2–5 %", Erwartung F2-Aufspaltung bei 2–3 Zielloci.
9. **HLVd-SOP + Testkalender** im Vault (Wurzelprobe alle 4–6 Wochen, Quarantaene 14 Tage + 2 Tests, Klingenwechsel je Pflanze).
10. **Offline-Zugang zu SeedFinder**: API tot, Cloudflare; eigener Cache + Rate-Limit, HTML-Parser aus growspace_manager/MyGrowBuddy als Fallback fuer `stammbaum-crawler`.

## Quellen

Repos: siehe Tabellen oben (alle github.com). Lokale Klone: `/tmp/claude-0/-home-user-Trapscholar-Agent-Creator/565203ac-a19a-5fc6-82c5-f701b96a51c7/scratchpad/crawl/repos_breeding/`.

Peer-Review-Literatur (ueber Repo-Fussnoten, nicht live verifiziert):
- de Meijer et al. 2003, Genetics 163(1):335–346 – Chemotyp-Vererbung B-Locus. https://academic.oup.com/genetics/article/163/1/335/6052757
- de Meijer, Hammond, Sutton 2009, Euphytica 168:95–112 – cannabinoidfreie Pflanzen (Typ V). https://link.springer.com/article/10.1007/s10681-009-9894-7
- Laverty et al. 2019, Genome Research 29:146 – THCAS/CBDAS-Loci, genetische Karte. https://genome.cshlp.org/content/29/1/146
- Grassa et al. 2021 (cs10/CBDRx), NCBI GCF_900626175.2.
- Toth et al. 2020, GCB Bioenergy 12:213 – Marker fuer Geschlecht und Chemotyp. https://onlinelibrary.wiley.com/doi/10.1111/gcbb.12667
- Toth et al. 2022, Front Plant Sci 13:991680 – Autoflower1/Early1. https://doi.org/10.3389/fpls.2022.991680
- Mohan Ram & Sett 1982, TAG 62:369 – STS/AgNO3-Maskulinisierung. https://link.springer.com/article/10.1007/BF00275107
- Lubell & Brand 2018, HortTechnology 28(6):743 – STS-Blattspray Hanf. https://doi.org/10.21273/HORTTECH04188-18
- Flajsman, Slapnik, Murovec 2021, Front Plant Sci 12:718092 – feminisiertes Saatgut CBD-Hanf. https://doi.org/10.3389/fpls.2021.718092
- Optimized guidelines for feminized seed production in high-THC cultivars 2024, Front Plant Sci 15:1384286. https://doi.org/10.3389/fpls.2024.1384286
- Punja & Holmes 2020, Front Plant Sci 11:718 – Hermaphroditismus. https://doi.org/10.3389/fpls.2020.00718
- Punja et al. 2025, Plants 14(5):830 – HpLVd Uebertragung/Management. https://pmc.ncbi.nlm.nih.gov/articles/PMC11902214/
- Adkar-Purushothama, Sano, Perreault 2023, Viruses 15:681 – HpLVd "hidden threat". https://pmc.ncbi.nlm.nih.gov/articles/PMC10053334/
- Adamek, Jones, Torkamaneh 2024, Plants 13:1910 – Mutationen ∝ Subkulturen. https://pmc.ncbi.nlm.nih.gov/articles/PMC11279941/
- Sawler et al. 2015, PLoS ONE 10:e0133292 – genetische Struktur Marijuana/Hanf. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0133292
- Schwabe & McGlaughlin 2019, J Cannabis Res 1:3 – Sortennamen unzuverlaessig. https://doi.org/10.1186/s42238-019-0001-1
- Ren et al. 2021, Science Advances 7:eabg2286 – Domestikationsgeschichte. https://www.science.org/doi/10.1126/sciadv.abg2286
- McPartland 2018, Cannabis Cannabinoid Res 3:203 – Systematik/5 Chemotypen.
- Divashuk et al. 2014 – XY-Geschlechtschromosomen (zit. in plant-biology.md).
- Ahrens/Moher et al. 2023, Plants 12:2605 – Photoperiode 12–14 h. https://pmc.ncbi.nlm.nih.gov/articles/PMC10386198/
- Cockson et al. 2025, Agrosyst Geosci Environ 8:e70129 – Saatgutfeuchte/Temperatur. https://doi.org/10.1002/agg2.70129
- Caplan et al. 2018, Can J Plant Sci 98:1126 – Stecklingsbewurzelung. https://doi.org/10.1139/cjps-2018-0038
- Monthony et al. 2021, Plants 10:185 – Gewebekultur-Review. https://pmc.ncbi.nlm.nih.gov/articles/PMC7835777/
- Bancic et al. 2024, Crop Science – Plant breeding simulations with AlphaSimR. https://doi.org/10.1002/csc2.21312
- Gaynor et al. 2021, G3 – AlphaSimR. https://doi.org/10.1093/g3journal/jkaa017
- Stack et al. 2024 – 7 Hanfgenome (GMStack/2024_Hemp_Genomes).
- Henry et al. 2018 – Chemovar-Vorhersage aus Ziel-SNPs (Genome-To-Phenome-Prediction).
- Buecher (via Farming-KB): Clarke "Marijuana Botany"; Cervantes "Marijuana Horticulture"; Small 1975/1979/2017.
- Gesetz: KCanG (BGBl. 2024 I Nr. 109), Volltext in legalize-dev/legalize-de.
