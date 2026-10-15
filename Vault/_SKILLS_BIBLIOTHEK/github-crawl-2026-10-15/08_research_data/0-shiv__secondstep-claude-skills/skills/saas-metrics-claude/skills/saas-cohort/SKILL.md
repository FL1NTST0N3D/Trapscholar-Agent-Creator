# SaaS Cohort Analysis

> Monthly cohort retention curves, revenue retention by cohort, activation rates, expansion patterns, and cohort heatmap visualization.

## Trigger
`/saas cohort`

## What This Skill Does

Aggregate metrics lie. A company reporting "5% monthly churn" might have 15% churn in month 1 and 1% churn from month 6 onward — those are two completely different stories with completely different solutions. Cohort analysis breaks down your metrics by the month (or quarter) customers joined, revealing the true shape of retention, the impact of product changes, and whether your business is fundamentally improving over time. This skill builds cohort retention tables, revenue retention curves, and activation analysis that tell you what your aggregate numbers cannot.

## Core Calculations

### Customer Retention by Cohort
```
Cohort Retention Rate (Month N) = Active Customers in Month N / Original Cohort Size x 100
```

Group customers by their signup or first-payment month. Then for each cohort, track what percentage of the original customers remain active in each subsequent month. This produces the retention curve — the most revealing chart in SaaS analytics.

**Reading Retention Curves:**
- **Steep early drop, then flat**: Normal. You lose bad-fit customers in months 1-3, then retain a loyal core. The key metric is where the curve flattens and at what level.
- **Gradual continuous decline**: Concerning. Customers are leaving at a steady rate, suggesting the product loses value over time or competitors are consistently winning.
- **Curve never flattens**: Dangerous. Every customer eventually leaves. You do not have product-market fit for long-term retention.
- **Smile curve (dips then rises)**: Rare but possible with reactivation campaigns. Track carefully — reactivated customers often churn again.

### Revenue Retention by Cohort
```
Cohort Revenue Retention (Month N) = MRR from Cohort in Month N / MRR from Cohort in Month 0 x 100
```

Revenue retention can exceed 100% if expansion revenue from surviving customers exceeds lost revenue from churned customers. This is the cohort-level view of NRR. A cohort that shows revenue retention above 100% after 12 months has excellent expansion economics.

### Activation Rate by Cohort
```
Activation Rate = Customers Who Hit Activation Milestone / Total Customers in Cohort x 100
```

Define your activation milestone — the specific action that correlates with long-term retention. For Slack, it was 2,000 messages sent. For Dropbox, it was placing a file in a shared folder. For your product, it might be completing onboarding, importing data, inviting a team member, or reaching a usage threshold.

Track activation rate by cohort to see if your onboarding is improving. If January's cohort had 40% activation and March's cohort had 55%, something you changed is working.

### Expansion Patterns by Cohort
```
Cohort Expansion Rate (Month N) = (Cohort MRR in Month N - Cohort MRR in Month N-1 + Churned MRR in Month N) / Cohort MRR in Month N-1 x 100
```

When do customers expand? Is there a pattern? Many SaaS companies see expansion cluster around contract renewal dates, fiscal year-end, or after specific usage thresholds. Understanding expansion timing helps you build proactive expansion playbooks.

## Cohort Heatmap Format

The standard cohort heatmap displays cohorts as rows and months as columns, with color intensity representing retention percentage:

```
Cohort Retention Heatmap
========================
         M0    M1    M2    M3    M4    M5    M6
Jan-26  100%   85%   78%   72%   70%   68%   67%
Feb-26  100%   87%   80%   75%   73%   71%    —
Mar-26  100%   88%   82%   77%   74%    —     —
Apr-26  100%   90%   84%   78%    —     —     —
May-26  100%   91%   85%    —     —     —     —

Color scale: 90%+ = green, 70-90% = yellow, <70% = red
```

In this example, newer cohorts (Apr, May) retain better in early months than older cohorts (Jan, Feb), suggesting product or onboarding improvements are working.

## How To Use

Provide customer-level data:
- CSV or JSON with `customer_id`, `signup_date` (or `first_payment_date`), `current_status`, and optionally `mrr` and `activation_date`
- Or monthly aggregated cohort data: "January cohort: 100 customers, Month 1: 85, Month 2: 78..."
- Specify your activation milestone if you want activation analysis

## Output Format

The skill produces:
- Customer retention cohort table (heatmap format)
- Revenue retention cohort table (if MRR data provided)
- Retention curves by cohort (text-based visualization)
- Activation rates by cohort (if activation data provided)
- Cohort-over-cohort improvement analysis
- Identification of the "flattening point" where retention stabilizes
- Expansion timing analysis (if expansion data provided)
- Recommendations for improving weak cohorts

## Advanced Analysis

### Cohort Comparison
Compare cohorts before and after a specific change (pricing change, onboarding redesign, new feature launch) to measure the impact on retention. This is the most reliable way to measure the retention impact of product changes.

### Segment x Cohort
Cross-reference cohorts with customer segments (plan tier, acquisition channel, company size) to find which segments retain best. This informs both product and go-to-market strategy.

## Related Skills
- `/saas churn` — Cohort churn is more accurate than aggregate churn
- `/saas nrr` — Cohort-level NRR analysis
- `/saas mrr` — MRR by cohort shows revenue quality
- `/saas unit-economics` — Cohort economics reveal true unit profitability
