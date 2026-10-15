# Lil Snouts Agenten-Architektur (Vollautomatik-Shop)

Stand: 2026-10-15. Quelle der Modellregeln: code.claude.com/docs/en/sub-agents + /costs (gelesen 15.10.2026), Preise aus der Anthropic-Preistabelle (Stand 06.10.2026).

## 0. Einordnung in die laufenden Routinen (Stand UMZUG_KONTO2_2026-10-16.md §1-2)

| Routine (Konto 2 ab 16.10.) | Modell heute | Was die neue Architektur ergaenzt |
|---|---|---|
| Produktion v9.1 | Sonnet baut, jedes Bild-Urteil frischer opus-Subagent (Modell-Split 15.10.) | Crawl/Readback/Messung an haiku-Subagents (`ls-crawler`, `ls-readback`, `ls-data-extractor`); Richter = `ls-master-designer` (opus, Blind-Richter, gleiche Tore) |
| CEO-Waechter v15.3 | Opus (Sicherheitsnetz) | bleibt Opus; Stichproben-Lesen an haiku delegieren, Befund bleibt opus |
| Shopify-Manager v4.0 | Sonnet | `ls-listing-builder`, `ls-copywriter` (sonnet) + `ls-readback` (haiku) + `ls-qa-judge` (opus) vor jeder Mutation |
| Ads & Social v2.4 | Sonnet (Empfehlung), Budget nur mit Phils Wort | `ls-ads-analyst` (haiku) zieht Zahlen, `ls-ads-decider` (opus) entscheidet Kill/Scale mit Zahl, `ls-social-pipeline` (sonnet) baut Drafts |
| Markt-Radar | Sonnet | `ls-crawler` (haiku) fuer products.json/Ad Library, `ls-design-researcher` (sonnet) wertet aus |

Phil-Wort 15.10. (UMZUG §2): "so das opus nur judget und sonnet die gruntwork macht". Phil-Wort 15.10. (Chat): "das die jeweiligen agents immer passende modelle haben fuer grundwork" + "bei entscheidungen das groesste genommen wird". Daraus die Dreiteilung: haiku = mechanische Grundarbeit (lesen, zaehlen, abrufen, vergleichen), sonnet = bauen/schreiben, opus = urteilen/entscheiden. Fable nur fuer den Chat-CEO/Agent-Builder.

Modellwechsel an geraete-gebundenen Triggern geht nicht per update_trigger (UMZUG §1 Hinweis) -> Phil-Klick in der App. Subagent-Modelle dagegen stehen im Frontmatter der Agent-Datei (`model: haiku|sonnet|opus`) und greifen sofort, sobald die Dateien unter `Vault/.claude/agents/` liegen (Claude Code liest `.claude/agents/` des Projekts; Aufloesung: Aufruf-Parameter > Frontmatter > CLAUDE_CODE_SUBAGENT_MODEL > Hauptmodell, Docs sub-agents 15.10.2026).

## 1. Grundprinzip: Modell nach Aufgabe, nicht nach Gewohnheit

| Stufe | Modell | Alias im Frontmatter | Preis In/Out je 1M Tokens | Wofür |
|---|---|---|---|---|
| Grundarbeit | Claude Haiku 5.5 | `model: haiku` | 0,10 $ / 0,50 $ | Crawlen, Scrapen, Parsen, Klassifizieren, Listen bauen, Lookups, Log-Lesen, Formatieren, Readback-Checks, Datenextraktion, Bulk-Captions-Rohfassung |
| Standard | Claude Sonnet 5.5 | `model: sonnet` | 2 $ / 10 $ | Texte schreiben (Produkt, E-Mail, Captions final), Listings, Prompt-Bau, Code, Reports, Routine-Entscheidungen innerhalb fester Regeln |
| Entscheidung | Claude Opus 5.5 | `model: opus` | 4 $ / 20 $ | Alles mit Geld oder Marke: Budget rauf/runter, Kill/Scale, Preis, Design-Urteil (Gate), Strategie, Konfliktauflösung, finale Freigabe vor Live-Schaltung |
| Chef | Claude Fable 5.1 | `model: fable` | 10 $ / 50 $ | Nur Orchestrator-Hauptsession und Quartals-/Strategie-Reviews. Nie als Worker. |

Faustregel (Phil-Wort 15.10.): **Grundarbeit immer auf das kleinste Modell, Entscheidungen immer auf das grösste verfügbare.** Haiku ist 40x billiger als Opus im Input, 40x im Output. Ein Crawl mit 8 Haiku-Workern kostet weniger als ein einziger Opus-Worker.

Effort je Stufe: Haiku `effort: low`, Sonnet `effort: medium`, Opus `effort: high`, Fable `effort: xhigh` nur bei Strategie.

## 2. Muster: Orchestrator -> Worker -> Richter

```
Orchestrator (fable/opus, 1 Session, hält nur Zusammenfassungen)
   │
   ├─ fan-out: N Worker (haiku) ──> Rohdaten, je Worker eigener Kontext
   │       Worker geben NUR Zusammenfassung + Dateipfad zurück, nie Rohdaten
   ├─ Verarbeitung: Sonnet-Worker schreiben/bauen aus den Worker-Dateien
   └─ Richter (opus): bewertet, entscheidet, gibt frei oder schickt zurück
```

Regeln:
1. Rohdaten (HTML, CSV, Logs, Screenshots-Beschreibungen) bleiben im Worker-Kontext. Rückgabe an den Orchestrator: max. 300 Wörter + Pfade.
2. Jeder Worker hat `maxTurns` und ein Zeitlimit; Blocker-Meldepflicht statt Endlosschleife.
3. Richter sieht nie den ganzen Crawl, nur die Kandidatenliste mit Zahlen.
4. Schreibende Aktionen (Shopify-Mutation, Ad-Budget, Klaviyo-Send, Post veröffentlichen) laufen immer: Dry-Run (haiku/sonnet) -> Diff -> Opus-Freigabe -> Ausführung -> Readback (haiku).
5. Geld-Aktionen über Schwellen (Budget > 50 €/Tag Änderung, Preisänderung, Kampagne pausieren) bleiben Phils Wort, Opus liefert die Entscheidung mit Zahl.

## 3. Agenten-Rollen (Dateien in `agents/`)

| Agent | Modell | Aufgabe | Schreibrecht |
|---|---|---|---|
| `ls-orchestrator` | fable/opus | Tagesplan, verteilt Aufträge, liest nur Zusammenfassungen | nein |
| `ls-crawler` | haiku | Web-/Shop-/Ad-Library-/IG-Crawl, Rohdaten in Dateien | nur Dateien |
| `ls-data-extractor` | haiku | CSV/JSON/Shopify-Export parsen, KPIs berechnen | nur Dateien |
| `ls-readback` | haiku | Nach jeder Mutation: Ist-Zustand lesen, mit Soll vergleichen | nein |
| `ls-copywriter` | sonnet | Produkttexte, Captions, E-Mails, Ad-Copy DE/EN im Brand-Voice | nur Dateien |
| `ls-listing-builder` | sonnet | Shopify/TeeInBlue/Etsy/Merch-Listings aus Design + Briefing | Dry-Run |
| `ls-design-researcher` | haiku+sonnet | Referenz-Crawl (OMD, Heybalu, Petprinted), Designsprache extrahieren | nur Dateien |
| `ls-master-designer` | opus | Design-Urteil, Ueberbieten-Plan, Gate (5 Kriterien), Print-Freigabe | nein |
| `ls-ads-analyst` | haiku | Meta/TikTok Insights ziehen, Tabellen bauen | nein |
| `ls-ads-decider` | opus | Kill/Scale/Budget-Entscheidung mit Zahl nach ads-skalierung | Vorschlag, Phil-Wort |
| `ls-social-pipeline` | haiku->sonnet | Idee -> Caption -> Scheduler (Postiz) | Post nach Freigabe |
| `ls-email-pipeline` | sonnet | Klaviyo Flows/Campaigns als Draft, nie Send ohne Freigabe | Draft |
| `ls-support` | sonnet | Kundenanfragen (Gmail/Shopify) beantworten nach Policy, Refund-Vorschlag | Draft/Refund-Vorschlag |
| `ls-finance` | sonnet->opus | Unit Economics, Deckungsbeitrag je SKU, MER, Wochenreport | nein |
| `ls-qa-judge` | opus | Prüft Output aller Sonnet-Worker vor Live | nein |

## 4. Token-Sparregeln (verbindlich, Quelle: Claude-Code-Docs /costs + Crawl 07)

1. CLAUDE.md unter 200 Zeilen; alles Spezifische in Skills (laden nur bei Bedarf, ~100 Tokens Frontmatter je Skill im Leerlauf).
2. Subagents mit `model: haiku` für alles Laute (Tests, Logs, Crawls); nur Zusammenfassung kommt zurück.
3. Hooks filtern Tool-Output vor dem Kontext (grep ERROR statt 10.000 Zeilen Log).
4. `/clear` zwischen unabhängigen Aufgaben; Routinen starten frisch, nicht in alten Sessions.
5. MCP-Server, die nicht gebraucht werden, aus (`/mcp`); CLI (`gh`, `shopify`) statt MCP, wo möglich.
6. Prompt-Cache warm halten: stabile System-Prompts zuerst, variable Daten zuletzt; keine Timestamps im System-Prompt.
7. Effort runter für Routine (`low` bei Haiku-Workern); Thinking nur bei Entscheidern.
8. Scheduled Tasks: jede Zündung sendet den vollen Kontext -> Routinen kurz halten, Lock+Doppelzündungsschutz (siehe textil-pipeline-agent 0.2).
9. Keine Rohdaten in Chat/Log: Pfad + 3 Zeilen Zusammenfassung.
10. Caveman-Stil für Worker-Antworten (keine Füllwörter, keine Wiederholung des Auftrags).

## 5. Pfade im Vault

- `00_SYSTEM/agent-architektur/agents/*.md` -> Agenten-Definitionen (nach `Vault/.claude/agents/` kopieren, damit Claude Code sie lädt).
- `00_SYSTEM/skills/github-skills/<domain>/` -> gecrawlte Skill-Sammlungen (Offline-Kopie, Stand im README).
- `_SKILLS_BIBLIOTHEK/SKILL_ZUORDNUNG_GITHUB.md` -> Tätigkeit -> Skill -> Modell.
- `01_LIL_SNOUTS/Ops/UEBERGABE_ZWEITKONTO_SKILLS.md` -> Sync-Handover für Konto 2.
