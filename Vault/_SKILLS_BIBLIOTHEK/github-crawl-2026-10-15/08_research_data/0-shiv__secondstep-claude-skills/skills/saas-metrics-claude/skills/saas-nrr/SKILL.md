# SaaS Net Revenue Retention (NRR)

> Calculate Net Revenue Retention and Gross Revenue Retention with tier benchmarks and growth implications.

## Trigger
`/saas nrr`

## What This Skill Does

Net Revenue Retention is the single best indicator of product-market fit in SaaS. It answers a deceptively simple question: "If I stopped all sales and marketing today, would my revenue grow or shrink?" A company with 120% NRR doubles its revenue from existing customers every 3.8 years — without acquiring a single new customer. This skill calculates NRR and GRR, benchmarks them against industry tiers, and explains what your retention numbers mean for your growth trajectory.

## Core Calculations

### Net Revenue Retention (NRR)
```
NRR = (Starting MRR + Expansion MRR - Contraction MRR - Churned MRR) / Starting MRR x 100
```

NRR measures the total revenue change from your existing customer base over a period. It includes expansion (upsells, cross-sells, seat additions), contraction (downgrades), and churn (cancellations). NRR above 100% means your existing customers are spending more over time — the holy grail of SaaS.

**Calculation example:**
- Starting MRR: $500,000
- Expansion MRR: $60,000
- Contraction MRR: $15,000
- Churned MRR: $25,000
- NRR = ($500K + $60K - $15K - $25K) / $500K = 104%

This means your existing customer base grew by 4% even without any new customers.

### Gross Revenue Retention (GRR)
```
GRR = (Starting MRR - Contraction MRR - Churned MRR) / Starting MRR x 100
```

GRR strips out expansion to show pure retention — how much of your existing revenue you kept. GRR can never exceed 100%. It is the floor of your retention, while NRR includes the upside from expansion.

**Why GRR matters alongside NRR:**
A company with 130% NRR and 70% GRR has a very different risk profile than one with 110% NRR and 95% GRR. The first is heavily dependent on expansion to mask high churn. The second has a rock-solid base with modest expansion on top. Investors increasingly ask for GRR as a complement to NRR because it reveals underlying retention health.

### NRR Tier Benchmarks

| Tier | NRR Range | What It Means | Examples |
|---|---|---|---|
| **Elite** | >130% | Dominant expansion motion, world-class retention | Snowflake (158%), Twilio (131%) |
| **Top Quartile** | 120-130% | Strong expansion, excellent product-market fit | Datadog (130%), CrowdStrike (124%) |
| **Good** | 110-120% | Healthy expansion offsetting normal churn | HubSpot (110%), Monday.com (115%) |
| **Acceptable** | 100-110% | Existing base is stable, modest expansion | Typical mid-market SaaS |
| **Concerning** | 90-100% | Losing revenue from existing base | Churn exceeds expansion |
| **Critical** | <90% | Significant revenue erosion | Urgent retention intervention needed |

### GRR Benchmarks

| Rating | GRR Range | Interpretation |
|---|---|---|
| **Excellent** | >95% | Almost no churn or contraction |
| **Good** | 90-95% | Healthy retention, minor churn |
| **Acceptable** | 85-90% | Normal for SMB-focused SaaS |
| **Concerning** | 80-85% | Elevated churn, investigate causes |
| **Critical** | <80% | Serious retention problem |

### NRR Growth Implications

The power of high NRR is exponential. Here is what different NRR levels mean for your existing customer base over time, assuming zero new customer acquisition:

| NRR | Year 1 | Year 2 | Year 3 | Year 5 |
|---|---|---|---|---|
| 130% | 1.30x | 1.69x | 2.20x | 3.71x |
| 120% | 1.20x | 1.44x | 1.73x | 2.49x |
| 110% | 1.10x | 1.21x | 1.33x | 1.61x |
| 100% | 1.00x | 1.00x | 1.00x | 1.00x |
| 90% | 0.90x | 0.81x | 0.73x | 0.59x |

A company with 130% NRR that starts at $10M ARR will have $37.1M ARR from those same customers in 5 years. A company with 90% NRR starting at $10M will be down to $5.9M. This is why NRR is the most important metric for valuation.

## How To Use

Provide your retention data:
- "Starting MRR $200K, expansion $30K, contraction $5K, churned $10K"
- Monthly MRR movements over time for trend analysis
- Customer-level data for segment-specific NRR

## Output Format

The skill produces:
- NRR percentage with tier classification
- GRR percentage with rating
- NRR trend over time (if historical data provided)
- Revenue growth projection from existing base (1, 2, 3, 5 year)
- Expansion rate vs churn rate comparison
- Segment-level NRR (if segment data provided)
- Recommendations for improving NRR

## Segment NRR Analysis

NRR varies dramatically by customer segment. Always calculate NRR separately for:
- **Enterprise vs SMB** — Enterprise NRR is typically 10-20 points higher due to multi-year contracts and seat expansion
- **Industry vertical** — Some verticals expand faster than others
- **Acquisition channel** — Customers from different channels may have different expansion patterns
- **Cohort** — Newer cohorts may have different NRR as your product and pricing evolve

## Related Skills
- `/saas mrr` — MRR movements feed directly into NRR calculation
- `/saas churn` — Churn is the downside component of NRR
- `/saas cohort` — Cohort-level NRR analysis
- `/saas benchmarks` — NRR benchmarks by company stage
