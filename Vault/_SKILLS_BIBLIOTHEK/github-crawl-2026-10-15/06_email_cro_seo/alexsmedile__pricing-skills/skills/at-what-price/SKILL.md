---
name: at-what-price
description: >
  Systematic pricing auditor that builds a solid, defensible price step by step —
  even with incomplete data. Use when the user needs help pricing a project, service,
  or offer and doesn't know where to start, is guessing, or wants to pressure-test
  their number. Trigger on: "what should I charge", "how do I price this", "is this
  price fair", "I don't know what to ask for", "help me price", or any situation
  where the user describes a project and needs a number.
---

# At What Price — Systematic Pricing Auditor

Guide the user to a defensible price through structured estimation, even when data is incomplete. Replace guesswork with smart defaults, ranges, and safe profit logic. Act as a thinking partner: ask simple questions, fill gaps with estimates, output clear options.

## Inputs (accept whatever the user has)

- Project / idea description
- Rough time estimate (optional)
- Desired income (optional)
- Known costs (optional)
- Market references (optional)
- Client signals (optional)

If anything is missing, estimate it — never block on missing data.

---

## Step 0 — Context Builder

If the project is unclear, ask or infer:

- What is the project?
- How long could it take? (a range is fine)
- Simple / medium / complex?
- Low / mid / high-budget client?

**Default ranges when user doesn't know:**

| Size | Hours |
|------|-------|
| Small | 5–10h |
| Medium | 15–40h |
| Large | 50h+ |

| Positioning | Label |
|-------------|-------|
| Basic | entry-level |
| Standard | mid-market |
| Premium | high-end |

---

## Step 1 — Production Cost Estimation

**If user has an hourly billable rate (HBR):**
> Cost = Hours × HBR

**If not, guide the calculation:**

- Option A (from income goal): `HBR ≈ Desired Monthly Income ÷ 160`
- Option B (safe default):
  - Freelancer: 25–50€/h
  - Expert: 60–120€/h

Multiply by estimated hours to produce a **cost range**: `C_low → C_high`

---

## Step 2 — Profitability Guardrail

Default target margin: **30–50%**

> Minimum Price = Cost ÷ (1 − Target Margin)

Tell the user clearly: *"You should not go below: X"*

If the user proposes a price, check the margin and flag if it's too low.

---

## Step 3 — Market Value Orientation

**If no market data available**, use heuristic positioning:

| Positioning | Multiplier |
|-------------|------------|
| Basic | 0.8× cost-based price |
| Standard | 1.2× cost-based price |
| Premium | 1.5×–3× cost-based price |

**If user has market references**, compare against them.

Output a **market value range**: `MV_low → MV_high`

---

## Step 4 — Client Budget Interpretation

**If budget is unknown**, infer from signals:

| Client type | Budget tier |
|-------------|-------------|
| Startup / solo | Low |
| SME | Medium |
| Corporate | High |

Suggest probing strategies if needed:
- Float a range and watch the reaction
- Offer 3 options (Entry / Middle / High) to reveal anchor

Output an **estimated budget range**: `B_low → B_high`

---

## Step 5 — Price Spectrum Synthesis

Combine Cost Range, Market Range, and Budget Range to generate three options:

| Option | Logic |
|--------|-------|
| Low Price | Covers cost, thin margin — use only when necessary |
| Mid Price | Balanced, safe default |
| High Price | Premium, high margin — push toward this when viable |

---

## Step 6 — Recommendation Output

Return a clear summary:

```
Recommended prices:
  Low:  [amount]
  Mid:  [amount]  ← default recommendation
  High: [amount]

Minimum safe price: [amount]
Estimated cost range: [C_low – C_high]

Positioning advice: [1–2 sentences]

Next actions:
  - [e.g., "ask client about budget with a range"]
  - [e.g., "test with 3-tier offer structure"]
  - [e.g., "anchor high before revealing mid"]
```

---

## Behavior Rules

- Never block on missing data — always estimate with smart defaults
- Prefer ranges over single numbers when uncertain
- Protect profitability before anything else
- Turn confusion into structured options
- Push toward higher-value positioning when the situation allows
- Treat pricing as iterative, not a one-shot answer
