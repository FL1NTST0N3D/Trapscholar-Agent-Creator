# pricing-skills

**Stop quoting gut feelings. Start pricing like a strategist.**

![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-blueviolet)
![License](https://img.shields.io/badge/license-MIT-blue)
![Stars](https://img.shields.io/github/stars/alexsmedile/pricing-skills?style=flat)

---

Most freelancers price by instinct — or worse, by fear. They undercharge to win the job, over-deliver to compensate, and walk away wondering why the numbers never add up.

This is a skill library for Claude Code that turns a pricing conversation into a structured strategy session. Three modular skills. One orchestrator. Twelve scenarios. Every price tied to a reason.

---

## What You Get

| Skill | What it does | Use when |
|-------|-------------|----------|
| `at-what-price` | Builds cost / market / budget spectrum → 3 price options | You need a number from scratch |
| `pricing-scenario` | Matches your situation to 1 of 12 scenarios → single final price | You have a range, need a decision |
| `price-intelligence` | Lead notes → signals → scenario → price → proposal strategy | You just had a client call |

**Orchestrator:** `pricing-expert` runs all three as internal advisors — Analyst, Strategist, Interpreter — has them critique each other, then synthesizes a final `PRICE.md`.

---

## Quick Start

Requires [Claude Code](https://claude.ai/code).

```bash
git clone https://github.com/alexsmedile/pricing-skills
```

Add the skills to your Claude Code project, then invoke:

```
/price-intelligence
```

Paste your lead notes or project description. Claude extracts signals, matches a scenario, builds the price spectrum, and outputs a full strategy with anchor price, target price, and negotiation tactics.

---

## The Three Skills

### `at-what-price` — Price Spectrum Builder

Start here when you have a project description but no number.

Inputs: project description, rough hours, income goal, any known costs — or nothing at all. Missing data gets estimated with smart defaults.

Outputs:
- Cost range (low → high)
- Profitability floor ("don't go below X")
- Market value range
- Three options: Low / Mid / High

### `pricing-scenario` — Strategic Price Selector

Use when you have a range and need one specific number to put on a proposal.

Matches your situation to one of 12 scenarios:

| Scenario | Pricing rule |
|----------|-------------|
| Desperate for work | Cost + 30% (survival floor) |
| Stable pipeline | Market value midpoint |
| Fully booked | MV high or above |
| Difficult client | ≥ MV high (friction buffer) |
| Strong competition / RFP | ~10% below budget cap |
| High-budget opportunity | Between MV high and budget high |
| Low-budget risk | Near budget high — or decline |
| Relationship recovery | Near cost, never below |
| Portfolio / strategic | Slightly above cost |
| New client test | Mid market |
| Easy / ideal client | Mid to high market |
| Premium positioning | Top 20% of MV or above |

Applies psychological rounding before output (e.g., 4,950 not 5,000).

### `price-intelligence` — Full End-to-End Advisor

The superset. Covers everything the other two do, plus:

- Lead signal extraction (budget signals, behavior, urgency, competition, pipeline)
- Client profile (startup / SME / corporate)
- Opportunity and risk scan (scope creep, upsell potential, thin margin flags)
- Proposal structure guidance (lead with solution, price comes last)
- Negotiation tactics (anchor high, 3-tier framing, scope trade not price cut)

---

## Pricing Logic

All three skills share the same core math:

**Profitability floor**
```
Min price = Cost ÷ (1 − target margin)
Default margin: 30–50%
Hard rule: never output a price below cost
```

**Market multipliers**
```
Basic:    0.8× cost-based price
Standard: 1.2× cost-based price
Premium:  1.5–3× cost-based price
```

**Psychological rounding**
```
< 2,000     → nearest 25
2,000–10,000 → nearest 50
> 10,000    → nearest 250
```

---

## Orchestrator: `pricing-expert`

For a full pricing session, use the orchestrator agent instead of calling skills individually.

It runs an internal debate:

```
Analyst (at-what-price)     → "Is this profitable? Are assumptions realistic?"
Strategist (pricing-scenario) → "Are we leaving money on the table?"
Interpreter (price-intelligence) → "Did we read the client correctly?"
```

Conflicts surface as options for the user to decide. Final output: `output/PRICE.md` — a complete pricing strategy document with scenario, price decision, negotiation plan, and proposal structure.

---

## Who This Is For

- Freelancers and consultants who want a number they can defend
- Business owners pricing services or custom projects
- Developers building AI agents that need embedded pricing intelligence

## Who It's Not For

- Anyone looking for a static rate card or price list template
- Businesses with fixed, catalog-style pricing

---

## Structure

```
skills/
  at-what-price/SKILL.md       — price spectrum builder
  price-intelligence/SKILL.md  — full lead-to-price pipeline
  pricing-scenario/SKILL.md    — scenario matcher + final price selector
agents/
  pricing-expert.md            — orchestrator agent
```

---

Built for [Claude Code](https://claude.ai/code).
