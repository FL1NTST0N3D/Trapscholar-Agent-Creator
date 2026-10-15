# Cannabis-Breeding Knowledge-Bibliothek (GitHub-Crawl 2026-10-15)

Auftrag Phil 15.10.: "scan noch alles moegliche an knowledge zu cannabis breeding". 96 Repos gecrawlt (Liste `_KATALOG/cloned_breeding_list.txt`), 44 uebernommen, auf Wissensdateien (md/txt/csv/json/py) beschnitten: 132 MB, ~9.100 Dateien. Sicherheits-Scan: 414 Regex-Treffer, alle gepruefte Kategorien (Injection/Exfil/Secrets/Permission) = Doku-Treffer, nichts geloescht.

Einstieg:
- `_KATALOG/09_breeding_wissen_kompakt.md` = das Wissen selbst (11 Sektionen: Genetik, B-Locus-Chemotypen, Geschlecht/Autoflower, Feminisierung, Pheno-Hunt, Pollen/Saatgut, F1->F5/IBL, Rueckkreuzung, Keeper/HLVd/Gewebekultur, CSV-Schema, KCanG). Kopie unter `02_BREEDING/Research/BREEDING_WISSEN_KOMPAKT_2026-10-15.md`.
- `_KATALOG/09_cannabis_breeding.md` = Katalog (Repo-Tabellen, 18 Datenquellen, 25 belegte Regeln mit Quelle, Tools mit Modell-Tier, Luecken).

Top-Repos hier: `JakeTheRabbit__cannabis-white-papers` (55 Papiere, genetics-phenohunting.md), `akravetz__dirt` (komplettes Hobby-Zuchtprogramm: Nomenklatur, Familienselektion, Pollenlagerung, Feminisierungs-Endpunkt), `0-CYBERDYNE-SYSTEMS-0__CRS-01` (Lineage-Graph mit Trust-Tiers), `BUTTERGANG__strain-catalog` + `hdb__seedfinder-python` + `pkempf__kannapedia-scraper` (Strain-/Pedigree-Daten), `Shannon-Goddard__cannabis-intelligence-database` (15,7k Strains CSV), `K-Dense-AI__scientific-agents` (plant-breeder-Skill), `human-avatar__skills-for-agriculture`, `stanfish06__skillquarium`, `RAFOUgg__Reviews-Maker` (Datenschema Stammbaum), `piercetaylor__backcross`, `zankrut20__selection.index`, `AI-for-Genome-Interpretation-lab__meiosim`, `MylesLab__cannabis-labelling` + `nickpalladino__kannapedia-data` (Terpen/Cannabinoid-Datensaetze), `legalize-dev__legalize-de` (KCanG-Volltext).

Lizenz nur intern (keine LICENSE / Buch- und Podcast-Exzerpte): `HomunculusLabs__Farming-KB`, `akravetz__dirt`, `muf4__canna-transcripts` (nicht uebernommen). `cannabis-white-papers` = CC BY-NC.

Einschraenkungen des Crawls: WebSearch-Budget der Session war erschoepft, Suche lief ueber GitHub; PubMed/NCBI/Kannapedia waren vom Proxy gesperrt, Papiere sind ueber Repo-Fussnoten belegt und im Katalog mit (S) = nicht live verifiziert markiert. Konkrete STS-Konzentrationen bewusst nicht uebernommen (Originalquellen lesen).

Naechste Schritte (Luecken, Katalog Abschnitt "Luecken"): Breeding-Pair-Planner auf `02_BREEDING/Research/Stammbaum-Datenbank/edges.csv` (Inzucht/Verwandtschaft, B_T/B_D-Punnett), Phenotype-Scoring-Sheet, Saatgut-/Pollen-Inventar, Trust-Tier-Spalte in verwandtschaft.csv, HLVd-Testkalender, SeedFinder-Offline-Cache. Modell: haiku parst/crawlt, sonnet plant Kreuzungen, opus entscheidet Keeper.
