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
