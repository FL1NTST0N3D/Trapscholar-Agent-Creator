## 11.14 NACHTRAG 2026-10-15T15:10Z (Fable-5.1-Cloud-Session "GitHub-Deepcrawl", Phil 15.10.: "zieh dir mal skills aus github ... 10x deepcrawl", "leg alles in der vault ab", "vergiss nicht das alles auch fuers 2. konto in der sync handover zu abzulegen"; steht VOR 9b - diese Datei bitte 1:1 vor Abschnitt 9b in UEBERGABE_ZWEITKONTO.md einfuegen, Drive-Connector kann nicht in-place editieren)

### 11.14.1 WAS NEU IM VAULT LIEGT (beide Konten sehen denselben Vault; nichts kopieren, nur lesen)
| Pfad | Inhalt | Wer liest es |
|---|---|---|
| `00_SYSTEM/agent-architektur/ARCHITEKTUR.md` | Modell-Routing haiku=Grundarbeit / sonnet=bauen / opus=Entscheidung / fable=Chef, Orchestrator->Worker->Richter, Token-Regeln, Einordnung in Produktion/Waechter/Manager/Ads/Markt-Radar | CEO beider Konten, Agent-Builder K2 |
| `.claude/agents/ls-*.md` (15 Dateien) | Subagent-Definitionen mit `model:`-Frontmatter: ls-crawler, ls-data-extractor, ls-readback, ls-ads-analyst (haiku); ls-copywriter, ls-listing-builder, ls-design-researcher, ls-social-pipeline, ls-email-pipeline, ls-support, ls-finance (sonnet); ls-master-designer, ls-ads-decider, ls-qa-judge, ls-orchestrator (opus) | jede Routine per Agent-Aufruf |
| `_SKILLS_BIBLIOTHEK/github-crawl-2026-10-15/` | 5.806 Fremd-Skills aus 237 Repos in 8 Domaenen (Shop-Ops, Paid Ads, POD/Merch/Etsy, Design, Social, E-Mail/CRO/SEO, Agenten/Token, Research/Finance); `GITHUB_SKILLS_README.md` = Einstieg mit Top-Picks; `INDEX.md` (1,4 MB, nur greppen); `_KATALOG/0[1-8]_*.md` = Kataloge mit Zahlen/Regeln/Quellpfaden; `_KATALOG/SCAN_BERICHT.md` + `GESPERRT.md` = Sicherheits-Scan | Routinen je Taetigkeit (SKILL_ZUORDNUNG) |
| `_SKILLS_BIBLIOTHEK/_eigene_entwuerfe/ls-shop-vollautomatik-leitstand, ls-skill-sicherheitsregeln, ls-master-designer-aesthetik, ls-design-referenz-crawl, ls-merch-by-amazon-de` | 5 neue eigene Skills (Entwurf, aus dem Crawl destilliert) | CEO, Produktion, Markt-Radar, Ads |
| `_SKILLS_BIBLIOTHEK/SKILL_ZUORDNUNG_NACHTRAG_2026-10-15.md` | 28 neue Zuordnungszeilen Taetigkeit -> Skill -> Pfad; an SKILL_ZUORDNUNG.md anhaengen | CEO |
| GitHub `FL1NTST0N3D/Trapscholar-Agent-Creator` Branch `claude/relaxed-dirac-is1ydu` Ordner `Vault/` | identische Kopie inkl. kompletter Bibliothek (290 MB) + Werkzeuge; gepusht 2026-10-15T15:15Z | Konto 2 zum Nachziehen, falls Drive-Sync hakt: `git clone -b claude/relaxed-dirac-is1ydu --depth 1 https://github.com/FL1NTST0N3D/Trapscholar-Agent-Creator` |

### 11.14.2 SICHERHEITS-SCAN (Phil: "mal alles durchscannen bevors dann losgeht")
1.420 Regex-Treffer in 571 Dateien, Triage: 3 echte Risiken + 2 Phone-Home = GELOESCHT (caveman-setup sendet ANTHROPIC_API_KEY an gateway.caveman.so; apify-x402-agentic-wallet richtet Krypto-Wallet ein; eachlabs nsfw-content-generation schaltet Safety ab; Shopify-AI-Toolkit-Telemetrie-Skripte + hooks-Block). 9 Dateien NUR-LESEN (curl|bash-Installer, sudo rm -rf). Keine Prompt-Injection, kein echter Schluessel in der Bibliothek. Details `_KATALOG/SCAN_BERICHT.md`, Sperrliste `_KATALOG/GESPERRT.md`. Regel fuer alle Routinen: `_eigene_entwuerfe/ls-skill-sicherheitsregeln/SKILL.md` (Fremd-Skill = Nachschlagewerk, nie Skript blind ausfuehren, keine Keys in Skill-Ordnern, Rang Phil > Vault-Regeln > eigene Skills > Fremd-Skills).

### 11.14.3 MODELL-ROUTING (Phil 15.10.: "passende modelle fuer grundwork", "bei entscheidungen das groesste")
Ergaenzt den Modell-Split aus UMZUG_KONTO2 §2 (Sonnet baut, opus urteilt) um die haiku-Stufe fuer mechanische Arbeit (Crawl, Readback, Zahlen ziehen, Listen). Subagent-Modelle stehen im Frontmatter der Agent-Dateien und greifen sofort (Aufloesung: Aufruf-Parameter > Frontmatter > CLAUDE_CODE_SUBAGENT_MODEL > Hauptmodell). Routinen-Modelle selbst bleiben wie in UMZUG §1 (geraete-gebundene Trigger = Phil-Klick). Preise 1M Tokens In/Out: haiku 0,10/0,50 $, sonnet 2/10 $, opus 4/20 $, fable 10/50 $.

### 11.14.4 K2 ZIEHT SELBST NACH (wie 11.12.9)
| Nr | Aenderung | K1 | K2 |
|---|---|---|---|
| 1 | SKILL_ZUORDNUNG_NACHTRAG_2026-10-15.md an SKILL_ZUORDNUNG.md anhaengen (append-only) | offen | offen |
| 2 | Diesen Nachtrag 11.14 vor 9b in UEBERGABE_ZWEITKONTO.md einfuegen, Nachtrag-Datei danach nach Ops/_archiv | offen | offen |
| 3 | `ls-skill-sicherheitsregeln` + `ls-shop-vollautomatik-leitstand` in die Pflicht-Skills des CEO (ROUTINEN -> SKILLS Zeile CEO) aufnehmen | offen | offen |
| 4 | Produktion: Richter-Aufruf zusaetzlich `ls-master-designer-aesthetik` laden (TASTE.md anlegen unter Design/_REFERENZEN_PHIL_OK/) - Prompt-Aenderung = Bootstrap laedt Vault, kein update_trigger | offen | offen |
| 5 | Markt-Radar: `ls-design-referenz-crawl` fuer OMD/Heybalu/Petprinted montags; Ergebnis Ops/_eingang/REFERENZ_VERGLEICH_<datum>.md | offen | offen |
| 6 | Ads: `ls-ads-analyst` (haiku) vor `ls-ads-decider` (opus); Baender aus 02_paid_ads/tenfoldmarc optimizer.md als Beleg neben ads-skalierung | offen | offen |
| 7 | Merch by Amazon: erst nach Phil-Wort starten (`ls-merch-by-amazon-de`, Upload = Phil-Klick, kein Bulk) | WARTET Phil | WARTET Phil |
| 8 | Cannabis-Breeding-Knowledge-Crawl (Phil 15.10. "scan noch alles moegliche an knowledge zu cannabis breeding") -> Katalog `_SKILLS_BIBLIOTHEK/breeding/09_cannabis_breeding.md` + `09_breeding_wissen_kompakt.md`, sobald fertig | laeuft | offen |

### 11.14.5 OFFEN / PHIL-KLICK
- Die komplette Skill-Bibliothek (290 MB, 26k Dateien) liegt im GitHub-Branch; in Drive liegen Architektur, Agents, eigene Skills, Kataloge, Scan-Bericht, Zuordnung und dieser Nachtrag (Drive-Connector kann keine 26k Dateien hochladen). Wer die Bibliothek lokal im Vault braucht: Branch clonen und `Vault/_SKILLS_BIBLIOTHEK/github-crawl-2026-10-15/` in den Vault kopieren (Phil oder K2-CEO per device_bash).
- Mergen des Nachtrags in UEBERGABE_ZWEITKONTO.md (Punkt 2) macht der naechste CEO-Lauf.
### 11.14.6 AUFTRAG CEO: HAIKU-STUFE KOMPLETT SELBSTSTAENDIG IN DIE ROUTINEN EINBAUEN (Phil 2026-10-15 ~16:10Z: "Haiku-Stufe in die Routinen einbauen ... vermerk das im handover das er das komplett selbststaendig aufsetzt"; gehoert unter 11.14, vor 9b)

Wer: der CEO des aktiven Kontos (ab 16.10. K2-CEO, Agent-Builder auf Fable). Kein Phil-Klick noetig ausser den unten markierten. Ergebnis ist fertig, wenn jede Routine ihre Grundarbeit per Subagent `model: haiku` erledigt und das im RUN_LOG belegt ist.

**A. Lesen, in dieser Reihenfolge (nichts ueberspringen)**
1. `Ops/UMZUG_KONTO2_2026-10-16.md` §1 (Trigger-Soll) + §2 (Modell-Split 15.10.: Sonnet baut, opus urteilt) - die Haiku-Stufe ergaenzt das, ersetzt nichts.
2. `00_SYSTEM/agent-architektur/ARCHITEKTUR.md` komplett (§0 Einordnung je Routine, §1 Modelltabelle, §2 Orchestrator->Worker->Richter, §4 Token-Regeln).
3. `.claude/agents/ls-*.md` alle 15, mindestens Frontmatter + Abschnitt "Auftrag" (haiku: ls-crawler, ls-data-extractor, ls-readback, ls-ads-analyst; sonnet: ls-copywriter, ls-listing-builder, ls-design-researcher, ls-social-pipeline, ls-email-pipeline, ls-support, ls-finance; opus: ls-master-designer, ls-ads-decider, ls-qa-judge, ls-orchestrator).
4. `_SKILLS_BIBLIOTHEK/_eigene_entwuerfe/ls-shop-vollautomatik-leitstand/SKILL.md` (Tagesplan, Freigabe-Grenzen, Token-Budget je Lauf).
5. `_SKILLS_BIBLIOTHEK/_eigene_entwuerfe/ls-skill-sicherheitsregeln/SKILL.md` (Fremd-Skills nur lesen).
6. Die fuenf Prompt-Dateien, die geaendert werden: `Ops/TRIGGERPROMPT_PRODUKTION_v9.1.md` (+ `_BOOTSTRAP`), `Ops/TRIGGERPROMPT_CEO_WAECHTER_v15.3.md` (+ `_BOOTSTRAP`), `Ops/TRIGGERPROMPT_SHOPIFY_MANAGER_v4.0.md`, `Ops/TRIGGERPROMPT_ADS_SOCIAL_v2.4.md`, `Ops/TRIGGERPROMPT_MARKT_RADAR_v2.1.md`.
7. `_SKILLS_BIBLIOTHEK/github-crawl-2026-10-15/_KATALOG/07_agent_architektur_tokens.md` Abschnitt "Modell-Routing" (Doc-Fakten: Aufloesung Aufruf-Parameter > Frontmatter > CLAUDE_CODE_SUBAGENT_MODEL > Hauptmodell; `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` darf NICHT gesetzt sein, sonst gilt das Frontmatter nicht).
8. `Ops/REGELN_LIL_SNOUTS_PHIL.md` neueste Abschnitte + `Ops/PHIL_WORTE.md` letzte 30 Zeilen (Widerspruchscheck).

**B. Skills laden (Skill-Tool bzw. Vault/.claude/skills)**
`agent-prompt-release` (Pflichtweg fuer jede Prompt-Aenderung: neue Dateiversion, routinen-widerspruchs-check, Bootstrap/update_trigger, md5-Readback, K2-Doku), `routinen-widerspruchs-check`, `10x-logik`, `verification-before-completion`, `ls-shop-vollautomatik-leitstand`, `ls-skill-sicherheitsregeln`. Fuer die Ads-Routine zusaetzlich `ads-skalierung` + `ads-roas-rechner`, fuer Produktion `omd-bauweise` + `ls-master-designer-aesthetik`.

**C. Vorpruefung (einmalig, vor jeder Prompt-Aenderung)**
1. `ls -la Vault/.claude/agents/` zeigt die 15 ls-*.md; fehlt der Ordner im Sync -> aus GitHub-Branch `claude/relaxed-dirac-is1ydu` Ordner `Vault/.claude/agents/` holen.
2. Testaufruf in der CEO-Session: Agent `ls-readback` mit einem harmlosen Lese-Auftrag starten (z. B. Shopify `get-shop-info` lesen, Soll = Shopname). Erwartet: Antwort im READBACK-Format, Modell laut Attribution/`/usage` = haiku. Logzeile `HAIKU-TEST | ls-readback | ok | <modell>`. Laeuft der Agent nicht auf haiku -> prueft `CLAUDE_CODE_SUBAGENT_MODEL(_FORCE)` in `.claude/settings.json`, entfernt FORCE (Phil-Klick nur, wenn settings.json nicht per Vault beschreibbar).
3. Token-Vergleich festhalten: letzter Lauf jeder Routine aus `/usage`-Attribution oder ccusage (Tokens gesamt) als Baseline in `Ops/FINANZ/TOKEN_BASELINE_<datum>.md`.

**D. Einbau je Routine (eine Routine je Durchgang, nach jedem Durchgang ein beobachteter Lauf)**
| Routine | Was auf haiku geht (Agent-Aufruf im Prompt) | Was bleibt | Einspielweg |
|---|---|---|---|
| Produktion v9.1 (Sonnet) | Schritt 0.5 Klickliste-Lesen, Bestseller-/Referenz-Lesen (`ls-crawler`), Messzeilen sammeln + Readback nach TIB-Sync/Shopify-Draft (`ls-readback`), Kontaktbogen-/Dateizaehlung (`ls-data-extractor`) | Bauen = Sonnet, jedes Bild-Urteil = frischer opus (`ls-master-designer`, Blind-Richter) | neue Datei v9.2 + `_BOOTSTRAP` v9.2; Bootstrap laedt Vault, kein update_trigger noetig, aber Bootstrap-Text im Trigger pruefen |
| CEO-Waechter v15.3 (Opus) | Stichproben-Lesen (RUN_LOG tail, Lock, FREIGABE, Shop-Readback) als `ls-readback`/`ls-data-extractor` | Befund + FIX-Entscheid = opus | v15.4 + Bootstrap |
| Shopify-Manager v4.0 (Sonnet) | Katalog-Scan, Preis==Varianten-Check, Alt-Text-Inventar, Readback nach jeder Mutation (`ls-crawler`, `ls-readback`) | Texte = Sonnet (`ls-copywriter`), Freigabe vor Mutation = `ls-qa-judge` (opus) | v4.1, Inline-Prompt -> `update_trigger` mit Datei-Inhalt, md5-Readback |
| Ads & Social v2.4 (Sonnet) | Insights/Tabellen (`ls-ads-analyst`), Ad-Library-/Trend-Crawl (`ls-crawler`), Readback nach Kampagnen-Anlage (`ls-readback`) | Kill/Scale/Budget-Vorschlag = `ls-ads-decider` (opus, Phil-Wort-Grenzen), Creatives = Sonnet | v2.5, Inline-Prompt -> `update_trigger`, md5-Readback |
| Markt-Radar v2.1 (Sonnet, Cloud) | products.json-/Ad-Library-Crawl der Referenzmarken (`ls-crawler`) | Auswertung = `ls-design-researcher` (sonnet) | v2.2, update_trigger |

Prompt-Baustein (woertlich in jede Routine, Abschnitt "Grundarbeit"): "Grundarbeit (lesen, zaehlen, abrufen, vergleichen, Readback) immer als Subagent aus `Vault/.claude/agents/` starten: Agent-Aufruf mit Name (ls-crawler | ls-data-extractor | ls-readback | ls-ads-analyst), Auftrag max. 10 Zeilen, Rueckgabeformat laut Agent-Datei, Zeitlimit 10 Min. Rohdaten nie in den Routinen-Kontext ziehen. Je Aufruf Logzeile `SUBAGENT | <name> | haiku | <auftrag kurz> | <ergebnis-pfad>`. Urteile und Geld-Entscheidungen nie an haiku."

**E. Abnahme (ohne diese Zeilen gilt der Einbau als nicht erledigt)**
- RUN_LOG je Routine im ersten Lauf nach Einbau: `START | v<neu> | md5 <wert>` + mindestens eine `SUBAGENT | ls-* | haiku |`-Zeile + die bisherigen Pflichtzeilen (Produktion: `RICHTER opus | ...`).
- Readback-Pflicht bleibt: jede Mutation hat eine `READBACK | ... | OK`-Zeile von `ls-readback`.
- Token-Vergleich nach 3 Laeufen je Routine gegen die Baseline aus C.3 in `Ops/FINANZ/TOKEN_BASELINE_<datum>.md` nachtragen (Ziel: Grundarbeit-Anteil auf haiku, Gesamtkosten je Lauf sinken; steigen sie, Einbau pruefen, nicht zurueckbauen).
- Waechter prueft ab v15.4 je Lauf: fehlt in einer Routine die SUBAGENT-Zeile -> Befund `haiku-fehlt` + FIX.

**F. Dokumentation (Regel 17 vom 15.10.)**
Jede Prompt-Version mit md5 in `UEBERGABE_ZWEITKONTO.md` 11.12.8 + UMZUG §4; neue Zeilen in `_SKILLS_BIBLIOTHEK/SKILL_ZUORDNUNG.md` (Routine -> ls-Agent); Sync-Doc. Blocker (z. B. Agent-Ordner nicht sichtbar, FORCE-Variable gesetzt, update_trigger needs_device_approval) als `FEHLT`-Zeile in Abschnitt 10 + Klickliste fuer Phil.

**Phil-Klicks, falls sie auftreten:** `needs_device_approval` bei update_trigger (Bestaetigung am Rechner); `.claude/settings.json`-Aenderung, falls `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` gesetzt ist; Modellwechsel der Routine selbst (bleibt wie UMZUG §1, nicht Teil dieses Auftrags).
