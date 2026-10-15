# pdp-audit

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/llizell/pdp-audit)](https://github.com/llizell/pdp-audit/releases)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20Claude.ai-8A63D2)](https://github.com/llizell/pdp-audit#install)

A free Claude skill that audits ecommerce product detail pages against a compiled knowledge base of ecommerce UX and conversion best practice — and gives you a prioritized, evidence-based report instead of a 40-item laundry list.

Built by a working ecommerce designer for the reviews we actually do: findings with severity, effort estimates, and recommendations concrete enough to hand to a developer.

**👉 [See a real sample report](examples/sample-report.md)** — a live audit of a well-known DTC footwear brand's product page (names removed, evidence unchanged): 11 findings including a fully sold-out product that never says so, and 6,574 reviews that exist in the page's structured data but never render.

## What it does

Give it a product page URL (or screenshots) and it:

1. **Captures evidence** — with browser access (Playwright MCP in Claude Code), it screenshots the page at desktop and mobile widths and tests interactions: variant selection, size guide, add-to-cart feedback, zoom. With screenshots only, it audits what's visible and tells you exactly what to verify by hand.
2. **Inventories the page** — flags entire missing zones first (no shipping info anywhere beats any styling nitpick).
3. **Checks 80+ guidelines** across page layout, gallery, buy box, pricing, variants & customization, shipping & returns, reviews & Q&A, description & specs, cross-sells, mobile behavior & performance, and trust & accessibility — a compilation of publicly documented ecommerce best practice, accessibility standards (WCAG 2.2), consumer-protection guidance (FTC, EU), and platform UX documentation, with the source category referenced per guideline.
4. **Writes the report** — max 12 findings, hard cap. Sorted by purchase impact, quick wins first. Each finding: what was observed, why it matters for conversion, and the concrete fix. Plus what's working, and a "verify manually" list for anything it couldn't confirm.

## Why the 12-finding cap

Audits die from noise. Every finding in the report is evidence-based — if the skill can't point to it in a screenshot or the DOM, it goes to "verify manually" instead of being guessed. False positives destroy trust in the whole document, so the skill is built to under-claim.

## Install

**Claude Code:** clone this repository into your skills directory:

```
git clone https://github.com/llizell/pdp-audit.git ~/.claude/skills/pdp-audit
```

(or copy the folder into your project's `.claude/skills/`). For live-URL audits, have Playwright MCP configured; without it, the skill falls back to screenshot mode.

**Claude.ai / Claude Desktop:** download `pdp-audit.skill` from this repository's Releases page and upload it to your profile, or paste the SKILL.md contents as a project instruction. Screenshot mode works everywhere; live-URL mode needs browser tooling.

## Usage

```
Audit this PDP: https://store.com/products/example
```
```
Review my product page — screenshots attached (mobile).
```
```
Why isn't this page converting? [URL]
```

## Add your own research

If you have your own research (paid subscriptions, internal usability testing, your own studies), create `references/private-guidelines.md` in your local copy using the same format (ID, rule, why, violations). The skill loads it automatically alongside the bundled guidelines. Keep that file local — don't redistribute paid or proprietary content.

## Roadmap

The skill is structured for expansion: `plp-guidelines.md`, `cart-guidelines.md`, and `checkout-guidelines.md` slot into the same workflow. PRs and guideline suggestions (with public sources) welcome.

## Related

[handoff-readiness](https://github.com/llizell/handoff-readiness) — the companion skill for the step before dev kickoff: it audits **state coverage** instead of design quality, finding the states you didn't draw (sold-out, failed add-to-cart, empty cart, focus states) that a developer will otherwise improvise. pdp-audit judges what you drew; handoff-readiness finds what you didn't.

## License

MIT — see [LICENSE](LICENSE).

## Disclaimer

A compilation of publicly documented ecommerce UX best practice, accessibility standards, and consumer-protection guidance — paraphrased and compiled, not reproduced from any source. This project is not affiliated with or endorsed by any research organization or platform. It's a review aid, not a substitute for usability testing with real users.
