# SaaS Unit Economics

> ARPU, ARPPU, gross margin, contribution margin, customer acquisition efficiency, and the Rule of 40.

## Trigger
`/saas unit-economics`

## What This Skill Does

Unit economics answer the most fundamental question in any business: "Do we make money on each unit we sell?" In SaaS, the "unit" is a customer. If the math does not work at the individual customer level, scaling just means losing money faster. This skill calculates every dimension of SaaS unit economics, from ARPU to contribution margin to the Rule of 40, giving you a complete picture of whether your business model actually works.

## Core Calculations

### ARPU (Average Revenue Per User)
```
ARPU = Total MRR / Total Active Customers
```

ARPU is your average monthly revenue per customer. It is simple but powerful — tracking ARPU over time tells you whether your pricing power is increasing or eroding. Rising ARPU typically means successful upselling, plan upgrades, or pricing increases. Falling ARPU means you are acquiring smaller customers, discounting more, or losing enterprise accounts.

**ARPU segmentation matters.** A $500 blended ARPU might mask a bimodal distribution: $100 SMB customers and $5,000 enterprise customers. Always look at the distribution, not just the average. Median ARPU is often more informative than mean ARPU.

### ARPPU (Average Revenue Per Paying User)
```
ARPPU = Total MRR / Total Paying Customers (excluding free tier)
```

If you have a freemium model, ARPPU excludes free users. This tells you what paying customers actually pay, which is the relevant number for unit economics. The gap between ARPU (including free users) and ARPPU (excluding them) shows the dilution effect of your freemium base.

### Gross Margin
```
Gross Margin = (Revenue - COGS) / Revenue x 100
```

SaaS COGS (Cost of Goods Sold) includes everything required to deliver the service:
- **Infrastructure**: Cloud hosting (AWS, GCP, Azure), CDN, monitoring
- **Support**: Customer support team salaries, helpdesk tools
- **Onboarding**: Implementation and onboarding team costs
- **Third-party costs**: APIs, data providers, payment processing fees
- **DevOps**: Operations team that keeps the product running (not building)

SaaS COGS does NOT include: R&D (product development), sales, marketing, or G&A.

**Benchmarks:**
- **>80%** — Excellent. Software-like margins with minimal per-customer costs.
- **70-80%** — Good. Typical for SaaS with moderate support and infrastructure costs.
- **60-70%** — Acceptable. Common for SaaS with heavy onboarding or managed services.
- **<60%** — Concerning. You may be more of a services business than a software business. Investors price these very differently.

### Contribution Margin
```
Contribution Margin = (Revenue - COGS - Variable Sales & Marketing Costs) / Revenue x 100
```

Contribution margin goes one step further than gross margin by subtracting the variable cost of acquiring and serving each customer. It tells you the true profit contribution of each revenue dollar after all variable costs. Fixed costs (office, R&D, G&A) are excluded because they do not scale linearly with customers.

### Customer Acquisition Efficiency (CAE)
```
CAE = Net New ARR / Sales & Marketing Spend
```

Also known as the **Magic Number** when measured over a specific period. CAE tells you how efficiently you convert sales and marketing dollars into recurring revenue. It is a more operationally useful metric than LTV:CAC because it measures current efficiency, not lifetime projections.

### The Magic Number
```
Magic Number = (Current Quarter ARR - Previous Quarter ARR) / Previous Quarter S&M Spend
```

The Magic Number specifically uses a one-quarter lag between spend and revenue, recognizing that marketing spend takes time to convert to revenue.

**Benchmarks:**
- **>1.0** — Excellent efficiency. Invest more aggressively in S&M.
- **0.75-1.0** — Good. Sustainable growth economics.
- **0.5-0.75** — Acceptable but watch closely. May need to optimize funnel.
- **<0.5** — Inefficient. Fix your funnel or GTM motion before scaling spend.

### Rule of 40
```
Rule of 40 = Revenue Growth Rate (%) + Profit Margin (%)
```

The Rule of 40 balances growth and profitability. A company growing 60% with -20% margins scores 40. A company growing 20% with 20% margins also scores 40. Both are considered healthy. The Rule of 40 says that the sum of growth rate and profit margin should exceed 40% for a healthy SaaS business.

**Benchmarks:**
- **>60** — Elite. Top decile. Premium valuation multiple.
- **40-60** — Strong. Meeting the bar.
- **20-40** — Acceptable for early-stage companies investing in growth.
- **<20** — Concerning. Neither growing fast nor making money.

**Which profit margin to use?**
- **EBITDA margin** — Most common. Used by public company analysts.
- **Free cash flow margin** — More conservative, accounts for capex. Preferred by some investors.
- **Operating margin** — Includes stock-based compensation. Most conservative.

### Burn Multiple
```
Burn Multiple = Net Burn / Net New ARR
```

How much cash do you burn to generate each dollar of new ARR? This is the capital efficiency metric VCs increasingly focus on.

**Benchmarks:**
- **<1.0** — Outstanding. You generate more ARR than you burn.
- **1.0-1.5** — Great. Very capital-efficient growth.
- **1.5-2.0** — Good. Typical for well-run SaaS.
- **2.0-3.0** — Mediocre. Room for improvement.
- **>3.0** — Inefficient. Burning too much cash per unit of growth.

## How To Use

Provide your financial data:
- Revenue, COGS breakdown, S&M spend, customer counts
- "MRR $200K, 500 customers, COGS $40K, S&M spend $80K last month, grew from $180K MRR last month"
- Quarterly or annual financials for Rule of 40 and Magic Number

## Output Format

The skill produces:
- ARPU and ARPPU calculations
- Gross margin with COGS breakdown
- Contribution margin
- Magic Number and CAE
- Rule of 40 score
- Burn Multiple (if burn data provided)
- Benchmark comparisons for each metric
- Recommendations for improving unit economics

## Related Skills
- `/saas ltv-cac` — LTV:CAC is the lifetime view of unit economics
- `/saas mrr` — Revenue data feeds unit economics calculations
- `/saas benchmarks` — Stage-specific benchmarks for all metrics
- `/saas report` — Unit economics section in the full dashboard
