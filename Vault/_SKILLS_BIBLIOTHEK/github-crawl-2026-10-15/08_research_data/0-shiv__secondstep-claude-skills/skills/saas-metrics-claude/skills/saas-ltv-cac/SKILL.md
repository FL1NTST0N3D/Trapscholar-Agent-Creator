# SaaS LTV:CAC Ratio

> Full lifetime value and customer acquisition cost analysis with payback period, fully-loaded CAC, and efficiency benchmarks.

## Trigger
`/saas ltv-cac`

## What This Skill Does

The LTV:CAC ratio is the fundamental equation of SaaS unit economics. It answers the question: "For every dollar I spend acquiring a customer, how many dollars does that customer generate over their lifetime?" A ratio below 1:1 means you are burning money on every customer. A ratio of 3:1 is the widely-accepted target. A ratio above 5:1 might mean you are under-investing in growth. This skill calculates both sides of the equation with precision and gives you the payback period that tells you when you break even on each customer.

## Core Calculations

### Customer Lifetime Value (LTV)

**Basic LTV Formula:**
```
LTV = ARPU x Gross Margin % x (1 / Monthly Churn Rate)
```

Where:
- **ARPU** = Average Revenue Per User (monthly). Total MRR / Total Active Customers.
- **Gross Margin %** = (Revenue - COGS) / Revenue. For SaaS, COGS includes hosting, support staff, onboarding costs, and third-party software costs that scale with customers. Typical SaaS gross margins range from 65-85%.
- **1 / Monthly Churn Rate** = Average customer lifetime in months. If monthly churn is 2%, average lifetime is 50 months. If monthly churn is 5%, average lifetime is 20 months.

**Advanced LTV with Expansion:**
```
LTV = (ARPU x Gross Margin %) / (Monthly Churn Rate - Monthly Expansion Rate)
```

This version accounts for expansion revenue. If customers expand faster than they churn (net negative churn), LTV is theoretically infinite — which is why companies like Snowflake and Datadog command premium valuations. In practice, cap lifetime at 5-7 years for modeling purposes.

**Discounted LTV (DCF-adjusted):**
```
LTV = ARPU x Gross Margin % x (1 / (Monthly Churn Rate + Monthly Discount Rate))
```

For financially rigorous analysis, discount future revenue at your cost of capital. A dollar received 3 years from now is worth less than a dollar today. Use a monthly discount rate of 0.8-1.0% (roughly 10-12% annual) for most SaaS businesses.

### Customer Acquisition Cost (CAC)

**Blended CAC:**
```
CAC = Total Sales & Marketing Spend / New Customers Acquired
```

Total S&M spend includes: salaries, commissions, ad spend, marketing tools, content production, events, and any other cost directly attributable to acquiring customers. Divide by new customers (not total customers, not leads, not trials — customers who started paying).

**Fully-Loaded CAC:**
```
Fully-Loaded CAC = (S&M Spend + Allocated Overhead + Onboarding Costs) / New Customers
```

Fully-loaded CAC includes a proportional share of overhead (office, HR, etc.) and the cost of onboarding each customer. This is the honest number. Many companies present blended CAC to investors while their fully-loaded CAC tells a different story. Always know both numbers.

**CAC by Channel:**
```
Channel CAC = Channel Spend / Customers Acquired via Channel
```

Break CAC down by acquisition channel: paid search, organic, referrals, outbound sales, partnerships. You will often find that your blended CAC obscures massive differences — organic might be $200 CAC while paid search is $2,000. This informs budget allocation.

### LTV:CAC Ratio
```
LTV:CAC = Customer Lifetime Value / Customer Acquisition Cost
```

**Benchmarks:**
- **<1:1** — You lose money on every customer. Stop spending on acquisition until you fix retention or pricing.
- **1:1 to 2:1** — Marginal economics. You are barely breaking even on customer acquisition after accounting for operational costs.
- **3:1** — The gold standard target. For every $1 spent acquiring, you generate $3 in gross profit over the customer lifetime.
- **3:1 to 5:1** — Strong economics. Healthy, fundable business.
- **>5:1** — Possibly under-investing in growth. You could spend more on acquisition and grow faster while maintaining healthy economics.

### CAC Payback Period
```
CAC Payback Period = CAC / (ARPU x Gross Margin %)
```

Payback period tells you how many months it takes to recoup the cost of acquiring a customer. After the payback period, every month of revenue is profit (minus ongoing operational costs).

**Benchmarks:**
- **<6 months** — Excellent. Capital-efficient growth.
- **6-12 months** — Good. Standard for most healthy SaaS.
- **12-18 months** — Acceptable for enterprise SaaS with high contract values.
- **18-24 months** — Concerning. You need a lot of capital to fund growth.
- **>24 months** — Dangerous. Unless you have very high NRR, this is unsustainable.

## How To Use

Provide your data:
- "Our ARPU is $200/month, gross margin 75%, monthly churn 3%, we spent $500K on sales and marketing last quarter and acquired 200 customers"
- Customer-level revenue and cost data
- Channel-by-channel spend and acquisition data

## Output Format

The skill produces:
- LTV calculation (basic, with expansion, and discounted)
- CAC calculation (blended and fully-loaded)
- LTV:CAC ratio with benchmark rating
- CAC Payback Period in months
- Channel-level CAC breakdown (if data provided)
- Sensitivity analysis showing how changes in churn or ARPU affect LTV:CAC
- Recommendations for improving the ratio

## Key Insight

LTV:CAC is a lagging indicator — it uses historical churn and historical costs. Use it for strategic decisions (are we building a viable business?) but not for real-time optimization. For operational decisions, focus on CAC payback period (how fast do we recover our investment?) and channel-level CAC (where should we spend next dollar?).

## Related Skills
- `/saas churn` — Churn rate is the denominator in LTV
- `/saas mrr` — ARPU derived from MRR data
- `/saas unit-economics` — LTV:CAC in broader unit economics context
- `/saas benchmarks` — Stage-specific LTV:CAC benchmarks
