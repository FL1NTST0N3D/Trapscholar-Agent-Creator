# VPD-Calc

A browser-based Vapor Pressure Deficit (VPD) calculator for growers and greenhouse operators — offline-capable, accessible, and built on vanilla web standards.

## What is VPD?

Vapor Pressure Deficit is the difference between the amount of moisture the air can hold (saturation vapor pressure) and the amount it actually holds (actual vapor pressure). It's the primary metric growers use to dial in their plant environment: too low and transpiration stalls, too high and plants close stomata and stress. Getting VPD right is the difference between thriving crops and wasted resources.

VPD-Calc takes temperature and relative humidity as inputs and returns the VPD value in kPa, with zone guidance (deficit, optimal, stress).

## Features

- Pure client-side calculation — no server, no external API
- Works offline after first load
- WCAG 2.1 AA accessible — full keyboard nav, labeled inputs, no color-only indicators
- Responsive layout for greenhouse tablets and phones
- Calculations based on established psychrometric formulas (Tetens/Buck/Magnus)

## Built with Spec-Kit

This project was built as a practical showcase of [Spec-Kit](https://github.com/OKlueck/spec-kit) — a spec-driven development workflow for AI-assisted coding.

The workflow:
1. **Constitution** — define non-negotiable principles before touching code
2. **Spec** — write a formal feature specification
3. **Plan** — break the spec into an ordered task list
4. **Implement** — work through tasks with AI assistance, spec as source of truth
5. **Checklist** — verify implementation against the original spec

VPD-Calc's constitution lives at `.specify/memory/constitution.md` and encodes five core principles: Accuracy, Simplicity, Test-Driven Development, Accessibility, and Offline Capability. Every implementation decision was made against those constraints.

The goal was to validate whether Spec-Kit can keep an AI-assisted project coherent and on-rails from first principles to shipped product — without the spec degrading into vague wishes or the implementation drifting away from intent.

## Project Status

**Complete.** All features implemented, tested, and shipped as v1.0.0. The Android APK is available in the [Releases](https://github.com/OKlueck/VPD-Calc/releases) section.

## Core Principles (from the constitution)

| Principle | Non-negotiable rule |
|-----------|-------------------|
| **Accuracy** | Calculations conform to established psychrometric formulas; validated against reference values |
| **Simplicity** | Minimum viable implementation; YAGNI; vanilla HTML/CSS/JS unless complexity demands otherwise |
| **TDD** | Tests written before implementation for all calculation logic; edge cases required |
| **Accessibility** | WCAG 2.1 AA minimum; keyboard operable; no color-only indicators |
| **Offline** | Fully functional without network after initial load; all calculations client-side |

## Tech

- Vanilla HTML, CSS, JavaScript
- Browser-native ES modules
- No mandatory framework dependency
- Modern evergreen browsers (latest 2 versions of Chrome, Firefox, Safari, Edge)
