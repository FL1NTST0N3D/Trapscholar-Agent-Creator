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
