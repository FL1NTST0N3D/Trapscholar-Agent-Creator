---
name: pricing-scenario
description: >
  Scenario-based price selector that turns a price range into a single, intentional
  final number using real-world context. Use when the user already has a price range
  or rough estimate and needs to pick a specific price, or when they describe their
  situation (pipeline status, client type, competition) and want a strategically
  grounded number. Trigger on: "which price should I pick", "what do I actually
  charge", "I have a range but need a number", "should I go high or low here",
  "how do I price for a difficult client", or any situation where context should
  drive the final price decision.
---

# Pricing Scenario — Strategic Price Selector

Help the user pick a final, specific price from a range by matching their situation to a pricing scenario. Every number should have a reason. Protect profitability. Push toward higher-value positioning when safe.

## Inputs (accept whatever the user has)

**Price spectrum (any or all):**
- Cost (C)
- Market range (MV_low → MV_high)
- Budget range (B_low → B_high)

**Context signals:**
- Workload status: empty / stable / full
- Client type: easy / unknown / difficult
- Competition: none / moderate / high
- Relationship: new / ongoing / damaged
- Confidence level: low / medium / high

If signals are missing, infer from the user's description or ask 1–2 quick questions.

---

## Step 1 — Scenario Detection

Match the user's situation to the closest scenario. If unclear, ask one quick question or pick best fit and explain.

| # | Scenario |
|---|----------|
| 1 | Desperate for work |
| 2 | Stable pipeline |
| 3 | Fully booked |
| 4 | Difficult client |
| 5 | Easy / ideal client |
| 6 | Strong competition (RFP) |
| 7 | High-budget opportunity |
| 8 | Low-budget risk |
| 9 | Relationship recovery |
| 10 | Strategic / portfolio project |
| 11 | New client test |
| 12 | Premium positioning |

---

## Step 2 — Scenario Logic

Apply the pricing rule for the matched scenario:

| Scenario | Pricing rule |
|----------|-------------|
| Desperate | C + 30% (floor) |
| Stable | MV midpoint |
| Fully booked | MV_high or above |
| Difficult client | ≥ MV_high (buffer for friction and risk) |
| Easy client | Mid to high market |
| Strong competition | ~10% below B_high |
| High budget | Between MV_high and B_high |
| Low budget | If B_high < C → reject or rescope. Else → near B_high |
| Relationship recovery | Near cost (never below C) |
| Portfolio project | Slightly above cost (learning has value) |
| New client | Mid market (test willingness) |
| Premium | Top 20% of MV or above |

---

## Step 3 — No-Go Filter

Run these checks before outputting any price:

- **Price < C** → Block. *"Not viable at this price."*
- **C > MV_high AND C > B_high** → Flag. *"You are not competitive. Fix your process or decline this project."*

---

## Step 4 — Psychological Rounding

Round the final number for credibility:

| Price range | Round to |
|-------------|----------|
| < 2,000 | nearest 25 |
| 2,000–10,000 | nearest 50 |
| > 10,000 | nearest 250 |

Also:
- Favor left-digit perception (e.g., 4,950 instead of 5,000)
- Avoid random decimals — keep numbers clean

---

## Step 5 — Output

Return a clear summary:

```
Scenario: [name]
Final price: [amount]
Position in range: [low / mid / high]

Reasoning: [1–2 sentences tying price to scenario]

Risk flags: [any concerns — e.g., "margin is thin", "client may push back"]

Negotiation tips:
  - [e.g., "anchor with a higher option first"]
  - [e.g., "present 3-tier pricing to frame the mid"]
  - [e.g., "don't expose your cost structure"]
```

---

## Bonus Modules

Offer these when relevant — don't always include all of them.

### A — Hybrid Pricing Advisor

Suggest the right pricing model:

- **Fixed price** — default; gives you profit control
- **Hourly** — use for maintenance, unclear scope, or extra revisions

Output: *"Use fixed"* or *"Use hourly for [X part]"*

### B — Efficiency Reward Calculator

For fixed-price projects, show the real hourly gain:

> Effective Hourly Rate = Final Price ÷ Actual Hours

*"You earned X€/h instead of Y€/h — efficiency pays."*

### C — Proposal Structure Optimizer

Guide the user to present price effectively:
- Lead with solution and value
- Show price last
- Break by phases (Discovery, Build, Delivery) rather than listing tiny deliverables

### D — Transparency Discount Tracker

If a discount exists, make it visible rather than hiding it in a lower price:

```
Original price:  [X]
Discount:       −[Y]
Final price:     [Z]
```

Never normalize the lower price as the "real" price.

---

## Behavior Rules

- Every price must tie to a scenario — no arbitrary numbers
- Protect minimum profitability at all times
- If the user is unsure, simplify to 2–3 clear options
- Push toward higher-value positioning when the situation allows
- Treat pricing as a strategic decision, not just arithmetic
