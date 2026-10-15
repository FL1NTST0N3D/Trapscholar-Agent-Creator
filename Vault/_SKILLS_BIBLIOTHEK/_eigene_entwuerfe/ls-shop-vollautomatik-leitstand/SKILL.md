---
name: ls-shop-vollautomatik-leitstand
description: "Leitstand fuer den vollautomatischen Shop-Betrieb Lil Snouts: welche Routine/welcher Agent welche Aufgabe mit welchem Modell und welchem Skill faehrt, Tages-/Wochentakt, Freigabe-Grenzen, Kennzahlen-Schwellen. Laden vom Orchestrator/CEO beim Start und bei jeder neuen Routine."
---
# Shop-Vollautomatik Leitstand (Entwurf 2026-10-15)

Architektur: `Vault/00_SYSTEM/agent-architektur/ARCHITEKTUR.md`, Agenten `Vault/.claude/agents/ls-*.md`. Modell: haiku Grundarbeit, sonnet bauen/schreiben, opus urteilen/entscheiden, fable Chef (Phil-Wort 15.10.).

## Tagesplan (UTC, Konto 2 ab 16.10.)
| Zeit | Routine/Agent | Modell | Skills | Output | Freigabe |
|---|---|---|---|---|---|
| :05 stuendlich | Produktion v9.1 | sonnet + opus-Richter | textil-pipeline-agent, omd-bauweise, ls-master-designer-aesthetik | Designs, Mockups, Draft-Produkte | Richter PASS + FREIGABE_PHIL bei Live |
| 05:40 Berlin | `ls-ads-analyst` -> `ls-ads-decider` | haiku -> opus | ads-skalierung, ads-roas-rechner, 02_paid_ads/tenfoldmarc optimizer-Baender | ENTSCHEID-Zeilen, Ops/ADS/INSIGHTS | Budget/Kill > 50 EUR = Phil |
| 07:40, 11:40, 15:40, 19:40 | Ads & Social v2.4 | sonnet | meta-post-ads, ls-social-pipeline, postiz | Creatives, Drafts | Publish nach Regel Draft-Push |
| 07:52, 14:52 Berlin | Shopify-Manager v4.0 | sonnet + `ls-qa-judge` | shopify-manager, ls-listing-builder, ls-copywriter | Produktpflege, Readback | Preis = Phil |
| alle 2 h :25 | CEO-Waechter v15.3 | opus | ceo-waechter, verification-before-completion | Befunde, FIX-Queue | - |
| 08:00 + 14:00 | `ls-support` | sonnet | ls-kundenservice-de, 01_shop_ops/40rty order-lookup | Gmail-Drafts, Refund-Vorschlaege | Refund > 20 EUR = Phil |
| 09:00 | `ls-email-pipeline` (Mo/Do) | sonnet | email-klaviyo, 06_email_cro_seo/CosmoBlk bible | Klaviyo-Drafts, Flow-Audit | Send = Phil/Regel |
| Mo 08:00 | Markt-Radar + `ls-design-researcher` | haiku -> sonnet | ls-design-referenz-crawl | REFERENZ_VERGLEICH, Trends | - |
| Mo 09:00 | `ls-finance` | sonnet -> opus | ads-roas-rechner, 08_research_data/mardab96 margin_stack | WOCHENREPORT_KW | Preis/Versand = Phil |
| taeglich 23:00 | `ls-readback` Sammellauf | haiku | verification-before-completion | READBACK-Zeilen aller Mutationen des Tages | - |

## Freigabe-Grenzen (nie automatisch)
Preise, Versandregeln, Meta-Budget rauf, Kampagne pausieren (Gewinner), endgueltige Loeschungen, Refunds > 20 EUR ausserhalb Policy, neue Marktplaetze (Merch/Etsy) live, Rechtstexte aendern. Alles andere laeuft mit Dry-Run -> Judge -> Ausfuehrung -> Readback.

## Kennzahlen-Schwellen (Alarm = Zeile in Ops/AUFTRAEGE/CEO_FIXES.md + Push)
MER < 2,0 (3-Tage) | ROAS Adset < BE-ROAS nach Spend >= 2x Ziel-CPA | CVR Shop < 1,0 % (7 Tage) | Retourenquote > 8 % | unbeantwortete Support-Mails > 24 h | Klaviyo Complaint-Rate >= 0,1 % (Send-Stopp, CosmoBlk thresholds.md) | Produktion ohne PASS 3 Laeufe in Folge | Lock aelter 25 Min.

## Token-Budget je Lauf (Richtwerte)
haiku-Worker <= 150k Tokens, sonnet-Routine <= 400k, opus-Richter <= 60k je Urteil, Orchestrator-Session <= 300k vor /clear. Ueberschreitung = Zeile `TOKEN-ALARM` + Lauf beenden. Messung: `/usage` bzw. ccusage (07_agent_arch/ryoppippi__ccusage).

## Konto-Sync
Jede Aenderung an dieser Datei, an Agenten oder Routinen -> `Ops/UEBERGABE_ZWEITKONTO.md` 11.12.8 + Sync-Doc (Regel 17 vom 15.10.).
