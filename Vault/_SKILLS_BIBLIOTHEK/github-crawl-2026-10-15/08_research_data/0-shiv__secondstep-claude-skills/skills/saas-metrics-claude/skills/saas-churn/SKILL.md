# SaaS Churn Analysis

> Comprehensive churn metrics: customer churn, revenue churn, gross vs net, cohort-based analysis, and reason categorization.

## Trigger
`/saas churn`

## What This Skill Does

Churn is the silent killer of SaaS businesses. A company growing 10% month-over-month with 5% monthly churn is in a fundamentally different position than one growing 10% with 2% churn — the first hits a ceiling, the second compounds into a massive business. This skill calculates every dimension of churn, benchmarks it against industry standards, and helps you categorize churn reasons so you can actually fix the problem.

## Core Calculations

### Customer Churn Rate (Logo Churn)
```
Customer Churn Rate = (Customers Lost in Period / Customers at Start of Period) x 100
```

Logo churn counts the number of customers who leave, regardless of how much they were paying. This metric matters because every customer lost represents a failure of your product, service, or targeting. Even if revenue churn is low because you are only losing small customers, high logo churn signals a product problem.

**Benchmarks:**
- **<2% monthly** (acceptable for SMB-focused SaaS)
- **<1% monthly** (good for mid-market)
- **<0.5% monthly** (expected for enterprise)
- **<5% annual** (excellent across all segments)
- **5-7% annual** (median B2B SaaS — this is where most companies land)
- **>10% annual** (concerning — investigate immediately)

### Revenue Churn Rate (MRR Churn)
```
Gross Revenue Churn = (Churned MRR + Contraction MRR) / Starting MRR x 100
Net Revenue Churn = (Churned MRR + Contraction MRR - Expansion MRR) / Starting MRR x 100
```

Revenue churn tells a different story than logo churn. If you lose ten $50/month customers but upsell two enterprise customers by $500 each, your logo churn is terrible but your net revenue churn is negative (which is good). Both metrics matter — they just answer different questions.

**Gross vs Net Churn:**
- **Gross churn** ignores expansion revenue. It tells you how much revenue you are losing from your existing base, period. You cannot "make up" for churn with expansion in this calculation — it is a pure measure of leakage.
- **Net churn** includes expansion. It tells you whether your existing customer base is growing or shrinking in total. Negative net churn means your existing customers are generating more revenue over time — this is the holy grail.

### Churn by Cohort
```
Cohort Churn Rate = Customers Lost from Cohort / Original Cohort Size x 100
```

Aggregate churn rates are misleading because they blend old cohorts (which have already lost their weakest customers) with new cohorts (which are still in the danger zone). Cohort-based churn shows you the true retention curve and whether your product is getting better or worse at retaining customers over time.

Key patterns to look for:
- **Flattening curves**: Retention stabilizes after month 3-6. This is healthy — early churn from bad-fit customers, then a loyal core remains.
- **Accelerating curves**: Churn rate increases over time. This signals a product that loses value as customers mature — a serious problem.
- **Improving cohorts**: Newer cohorts retain better than older ones. This means your product, onboarding, or targeting is improving.

### Churn Reason Categorization

Not all churn is equal. Categorize every churned customer into one of these buckets:

1. **Product Gap** — Missing features the customer needed. Actionable: feed into product roadmap.
2. **Bad Fit** — Customer should never have been sold. Actionable: tighten ICP definition and qualification.
3. **Price Sensitivity** — Customer could not justify the cost. Actionable: revisit pricing tiers or add a lower tier.
4. **Competitive Loss** — Customer left for a competitor. Actionable: competitive analysis and positioning.
5. **Business Closure** — Customer went out of business or was acquired. Not actionable — natural attrition.
6. **Champion Left** — Internal champion who bought your product left the company. Actionable: multi-thread relationships.
7. **Poor Onboarding** — Customer never reached value realization. Actionable: improve time-to-value.
8. **Support Failure** — Customer had a bad support experience. Actionable: CS process improvement.

Track the distribution of these reasons monthly. If >30% of churn is "Bad Fit," your sales team has a targeting problem. If >30% is "Product Gap," your product team needs to prioritize retention features over acquisition features.

## How To Use

Provide your churn data in any format:
- "We lost 15 out of 300 customers last month, $12K MRR churned, $3K contraction, $7K expansion"
- Customer-level data with cancellation dates and optionally cancellation reasons
- Monthly churn figures over time for trend analysis

## Output Format

The skill produces:
- Customer churn rate (monthly and annualized)
- Gross revenue churn rate
- Net revenue churn rate
- Benchmark comparison with rating
- Churn reason breakdown (if reasons provided)
- Cohort churn analysis (if cohort data provided)
- Recommendations based on the churn profile

## Annualized Churn Conversion
```
Annual Churn = 1 - (1 - Monthly Churn Rate)^12
```

Do NOT simply multiply monthly churn by 12. A 3% monthly churn rate is not 36% annual — it is 30.6% annual due to compounding. This distinction matters for financial modeling and investor conversations.

## Related Skills
- `/saas mrr` — MRR waterfall shows churn in revenue context
- `/saas nrr` — Net Revenue Retention is the inverse view of net churn
- `/saas cohort` — Deep cohort retention analysis
- `/saas ltv-cac` — Churn is a direct input to LTV calculation
