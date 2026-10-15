---
name: ls-master-designer-aesthetik
description: "Master-Designer-Regelwerk fuer Lil Snouts (opus-Richter + sonnet-Bauer): Anti-AI-Slop-Tells, Hierarchie, Komposition, Farbharmonie, Typografie, Pointe, Druck-Tauglichkeit; destilliert aus den besten GitHub-Design-Skills (anthropics frontend-design, Leonxlnx taste-skill, MengTo no-ai-design-slop, jiji262 design-principles, crizex art-director, Nutlope hallmark). Laden bei jedem Design-Urteil, Mockup, Ad-Static und jeder Landingpage."
---
# Master-Designer: Aesthetik-Regeln (Entwurf 2026-10-15, Quellen in `github-crawl-2026-10-15/04_design/`)

Gilt zusaetzlich zu `omd-bauweise` (14/14), `bestseller-textildesign`, `design-evaluation`. Diese Datei ist das Geschmacks-Regelwerk; die drei Skills sind die Tore.

## 1. Geschmacksprofil (persistent, nach crizex__art-director `templates/taste.md`)
Datei `Design/_REFERENZEN_PHIL_OK/TASTE.md` fuehren: je Phil-OK-Design 3 Eigenschaften, die es gut machen; je Phil-NEIN 1 Grund. Richter liest TASTE.md vor jedem Urteil. Neue Eintraege nur mit Phil-Wort oder FREIGABE-Zeile als Beleg.

## 2. Anti-Slop-Tells (datierte Liste, nach Leonxlnx `references/tells.md`, MengTo `no-ai-design-slop`, miqdadbadjuber `anti-slop`)
FAIL, wenn eines zutrifft: Glow-/Neon-Matsch ohne Lichtquelle; Zufallstexturen/Partikel; kaputte Anatomie (Pfoten, Zaehne, Augen, 5 Beine); Text mit Buchstabensalat; generische "Epic"-Himmel; drei und mehr konkurrierende Lichtquellen; gradient-auf-gradient; Schlagschatten in alle Richtungen; Stock-Posen; symmetrische Mitte ohne Grund; Pastell-Lavendel-Default; Serifenschrift mit Glow; mehr als 2 Schriftfamilien; Rahmen/Kasten um das Motiv (Kasten-Gate).
Tells-Liste ist datiert: jeden Monat 3 neue Tells aus den eigenen FAIL-Faellen anhaengen (Datum + Beispiel-Pfad).

## 3. Hierarchie
Ein Blickfang. In 2 Sekunden erkennbar: WAS (Motiv), WER (Hund/Katze), WITZ (Pointe). Test: Mockup auf 200 px verkleinern - ist die Pointe noch lesbar? Nein = FAIL (Lesbarkeits-Regel).

## 4. Komposition
Hochformat 4:5 Fotofeld (FOTOFELD = BILDFORMAT). Rand gestaltet (fade/ausriss/schnitt/pinsel), nie Kasten. Pop-out ueber die Flaeche. Drittel oder bewusste Mitte. Negative Flaeche >= 25 %. Motivgroesse auf Textil: 28-32 cm Breite Shirt, 30-34 cm Hoodie (TIB-Masken `Ops/MP_MASKS`).

## 5. Farbe
Max 3 Hauptfarben + 1 Akzent (nach `meodai__skill.color-expert`, `nhatmobile1__color-palette-skill`). Kontrast Motiv zu Textil Delta L* >= 35 (`kontrast_check.py`). Dunkler Hintergrund auf dunklem Textil = FAIL (Phil 15.10.). Siebdruck-Logik fuer Badges/Emblems: 5-7 Farben, flache Flaechen (MengTo `illustration-vintage-emblem`). Jede Textilfarbe als Mockup rendern, 11b-SICHT: "beisst sich das Motiv mit der Textilfarbe?" Nein = Farbe raus.

## 6. Typografie
Max 2 Schriften (Display + Sans). Kerning manuell pruefen, keine Default-Tracking-Werte. Text nie unter 24 pt auf Druckgroesse. Keine 1:1-Markenfonts. Spruch nur, wenn das Pendant einen hat (Regel 14 vom 15.10.).

## 7. Pointe und Sprache
Pointe zuerst, Bild dient der Pointe. Alltagsdeutsch, korrekt, kein KI-Pathos. Parodie = eigene Welt, nicht Nachbau (Fassaden-Regeln).

## 8. Druck-Tauglichkeit
PNG 300 dpi auf Endgroesse, transparent, keine Halbtransparenzen < 10 % Alpha am Rand (Alpha-Messweg `teeinblue-ops` 7.8), keine Haarlinien < 0,5 pt, DTG: keine grossen Vollflaechen Weiss auf Schwarz ohne Unterdruck-Plan; AOP: nahtloses Tile verifizieren (`devkindhq__seamless-pattern`).

## 9. Zwei-Pass-Prozess (anthropics `frontend-design`)
Pass 1 (sonnet): Token-Plan -> Entwurf -> Selbstkritik gegen Abschnitte 2-8 (je Punkt 0/1).
Pass 2 (opus, blind): sieht nur Bild + Pendant + TASTE.md + diese Liste; Urteil `RICHTER opus | <design> | PASS|FAIL | <schwaechster Punkt> | <eine Aenderung>`. Kein PASS ohne Messzeilen (Kontrast, Kasten, Alpha).

## 10. Studie statt Bauchgefuehl (Nutlope `hallmark/references/study.md`)
Vor neuer Serie: 10 Referenzbilder (Phil-OK + OMD-Bestseller) auf Struktur, Archetyp, Type-Pairing, Colour Anchor, Rhythmus zerlegen (`ls-design-referenz-crawl`). Serie uebernimmt die Struktur, nie die Motive.
