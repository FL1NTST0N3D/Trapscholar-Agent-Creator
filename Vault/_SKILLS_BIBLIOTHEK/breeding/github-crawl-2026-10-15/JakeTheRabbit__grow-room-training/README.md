# Grow Room Training

> **This repo is free. My 2am dryback debugging is not.** If it saved you a crop, a weekend, or a nervous breakdown — [buy the rabbit a bag of nutes](https://github.com/sponsors/JakeTheRabbit). If it didn't, keep your money. I respect a tight nutrient budget.

A small collection of self-contained HTML and Markdown reference material for cannabis
cultivation rooms. Distilled from a publicly available systems framework on grow-room
levers, restructured around four balances, eleven levers, six failure modes, and a
diagnostic chain from light to disease.

Each file is single-file and works by double-clicking — no build step, no bundler, no
external JS dependencies, no browser storage. Refresh wipes any on-screen state.

## Files

| Path | What it is |
|---|---|
| [`docs/training/grow-room-systems-manual.html`](docs/training/grow-room-systems-manual.html) | **Start here.** Mobile-first visual manual. Landing page = 6 navigation cards; floating menu button bottom-right for jumping anywhere. Modern UI, big titles, diagrams everywhere. |
| [`docs/training/grow-room-systems-training.html`](docs/training/grow-room-systems-training.html) | The deep textbook. 15 chapters, end-of-chapter exercises, full glossary, 4 printable field cards, a competency assessment with auto-scored MCQ + scenarios, and a printable certificate. |
| [`docs/training/grow-room-systems-app.html`](docs/training/grow-room-systems-app.html) | An earlier interactive learning app. Superseded by the manual above. Kept for reference. |
| [`docs/training/grow-room-agent-playbook.md`](docs/training/grow-room-agent-playbook.md) | LLM-agent playbook for autonomous Home Assistant control. Dense, machine-oriented — capability map (entity\_ids), stage envelopes as JSON, 11 levers with magnitude limits and cool-downs, 6 failure-mode detection rules, decision algorithm, hard safety rails, response-protocol JSON schema. |

## Content

- **The four balances** — energy, moisture, CO₂, salt
- **The eleven levers** — six environmental (light, temp, RH, airflow, exhaust, CO₂), three root-zone (irrigation, feed chemistry, root-zone temp & O₂), two crop (canopy architecture, sensing & biosecurity)
- **The chain** — eleven nodes from PPFD at canopy through transpiration, dryback, pore EC, photosynthesis, HVAC load, to disease pressure
- **The six failure modes** (F-01 to F-06) with mechanism, signals, and fix
- **Twelve symptoms** with probable causes and first-action lookup
- **Athena-style stage targets** from tissue culture through dry & cure
- **Glossary** — 34 terms

## Scientific anchors

The content is opinionated about seven points commonly mis-stated in operator-level
material:

1. Healthy leaf temperature is **1–3 °C BELOW** air, not at or above. A leaf at air temp has stalled transpiration.
2. Pore EC drifts from feed EC via **two simultaneous mechanisms** — selective ion uptake AND evaporative concentration. Lowering feed EC alone addresses neither.
3. Light saturation is **conditional on CO₂** — ~1500 μmol/m²/s at ambient, ~1800–2000 at 1200–1500 ppm enrichment. Not a fixed number.
4. Cannabis stomata begin **anticipatory closure around leaf-VPD 1.5–1.6 kPa**, well before tissue water deficit. Past that the lever inverts.
5. Botrytis requires **sustained RH >93–95% OR free water on tissue**. Brief humidity excursions are forgiven.
6. F-02 (boundary-layer suffocation) is the mechanism by which a "perfect" room sensor can coexist with a sick canopy.
7. A refrigerant dehumidifier is a **net heater** of the room — AC and dehum capacities are coupled.

## License & attribution

Personal/private project content adapted from a publicly available cannabis-cultivation
systems framework. Use at your own risk; this is reference material, not professional or
medical advice.