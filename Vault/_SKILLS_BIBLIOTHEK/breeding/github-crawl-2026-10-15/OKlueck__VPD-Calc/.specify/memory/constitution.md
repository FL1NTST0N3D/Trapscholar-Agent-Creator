<!--
  Sync Impact Report
  ===================
  Version change: 0.0.0 → 1.0.0 (MAJOR — initial ratification)
  Modified principles: N/A (initial creation)
  Added sections:
    - Core Principles (5 principles)
    - Technology Constraints
    - Development Workflow
    - Governance
  Removed sections: N/A
  Templates requiring updates:
    - .specify/templates/plan-template.md ✅ no update needed (generic)
    - .specify/templates/spec-template.md ✅ no update needed (generic)
    - .specify/templates/tasks-template.md ✅ no update needed (generic)
  Follow-up TODOs: none
-->

# VPD-Calc Constitution

## Core Principles

### I. Accuracy

All VPD calculations MUST conform to established
psychrometric formulas (Tetens, Buck, or Magnus).
Calculation results MUST be validated against known
reference values. Rounding and unit conversions MUST
preserve meaningful precision (at minimum 2 decimal
places for kPa values). Any deviation from standard
formulas MUST be documented with rationale.

**Rationale**: VPD-Calc is a scientific tool used for
plant environment decisions. Incorrect values lead to
crop damage or wasted resources.

### II. Simplicity

Start with the minimum viable implementation. Every
dependency, abstraction, or feature MUST justify its
existence. Prefer vanilla HTML, CSS, and JavaScript
over frameworks unless complexity demands otherwise.
YAGNI applies — do not build for hypothetical future
requirements. Three similar lines of code are better
than a premature abstraction.

**Rationale**: A calculator tool MUST remain lean and
fast. Over-engineering obscures the core purpose and
increases maintenance burden.

### III. Test-Driven Development

Tests MUST be written before implementation for all
calculation logic. The Red-Green-Refactor cycle is
mandatory for core VPD formulas and unit conversions.
Edge cases (extreme temperatures, humidity at 0% or
100%, negative values) MUST have explicit test
coverage. UI tests are recommended but not mandatory.

**Rationale**: Calculation correctness is the product's
primary value proposition. Untested math code is
unacceptable in a scientific tool.

### IV. Accessibility

The application MUST meet WCAG 2.1 AA standards at
minimum. All inputs MUST have associated labels. Color
MUST NOT be the sole means of conveying VPD zone
information — use text labels or patterns alongside
color. The UI MUST be fully operable via keyboard. The
layout MUST be responsive and usable on mobile devices.

**Rationale**: Growers access VPD tools in greenhouses
on phones and tablets. Excluding users with
disabilities or non-desktop devices limits the tool's
real-world utility.

### V. Offline Capability

The application MUST function without a network
connection after initial load. All calculations MUST
run client-side. No external API calls are required
for core functionality. Service worker or cache
strategies SHOULD be used to enable reliable offline
access.

**Rationale**: Greenhouses and grow facilities often
have poor or no internet connectivity. A VPD tool that
requires a server is unreliable in the field.

## Technology Constraints

- **Language**: HTML, CSS, JavaScript (vanilla or
  minimal framework)
- **Runtime**: Browser-based, client-side only
- **Dependencies**: Minimize external dependencies;
  each dependency MUST be justified
- **Browser support**: Modern evergreen browsers
  (Chrome, Firefox, Safari, Edge — latest 2 versions)
- **Build tooling**: Keep minimal; prefer native ES
  modules where possible

## Development Workflow

- All changes MUST pass existing tests before merge
- Calculation logic changes MUST include corresponding
  test updates
- Code reviews MUST verify VPD formula correctness
  against reference material
- Commits SHOULD be atomic and focused on a single
  concern
- Accessibility checks MUST be part of the review
  process for any UI change

## Governance

This constitution supersedes all other development
practices for VPD-Calc. Amendments require:

1. A documented rationale for the change
2. Review of impact on existing code and principles
3. Version bump following semantic versioning:
   - MAJOR: Principle removal or incompatible
     redefinition
   - MINOR: New principle or material expansion
   - PATCH: Clarification or wording fix
4. Update of the Last Amended date

Compliance with these principles MUST be verified
during code review. Violations MUST be justified in
writing if accepted as exceptions.

**Version**: 1.0.0 | **Ratified**: 2026-03-09 | **Last Amended**: 2026-03-09
