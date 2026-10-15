# Email Analytics — Sub-Skill

## Overview

Email analytics transforms raw data into actionable insights. This sub-skill covers every key metric, how to calculate them, what benchmarks to target, how to run cohort analysis, and how to identify trends before they become problems.

**Command:** `/email analytics`

---

## Analytics Audit Checklist

- [ ] Open rate is tracked and benchmarked by industry
- [ ] Click rate and CTOR are measured separately
- [ ] Conversion tracking is set up (UTM parameters, pixel, or integration)
- [ ] Revenue per email is calculated (for e-commerce/monetized lists)
- [ ] List growth rate is monitored monthly
- [ ] Churn rate is tracked (unsubscribes + bounces + complaints)
- [ ] Engagement trending is reviewed weekly
- [ ] Cohort analysis is performed quarterly
- [ ] Campaign-level AND automation-level metrics are tracked
- [ ] Metrics are compared to industry benchmarks

---

## Key Metrics Defined

### 1. Open Rate

```
Open Rate = (Unique Opens / Emails Delivered) x 100
```

**Important caveat:** Since Apple's Mail Privacy Protection (MPP, September 2021), open rates are inflated for Apple Mail users. MPP pre-loads tracking pixels, registering opens even if the email wasn't read.

**Adjustment:** Segment Apple Mail users separately. Focus on click rate as the primary engagement metric for Apple Mail subscribers.

| Performance | Open Rate | Interpretation |
|-------------|-----------|---------------|
| Excellent | >30% | Top performer or niche audience |
| Good | 20-30% | Above average |
| Average | 15-20% | Industry standard |
| Below Average | 10-15% | Subject line or deliverability issues |
| Poor | <10% | Critical — likely deliverability problems |

### 2. Click Rate (CTR)

```
Click Rate = (Unique Clicks / Emails Delivered) x 100
```

Click rate measures how many recipients clicked any link in the email, relative to how many received it. This is the most reliable engagement metric post-MPP.

| Performance | Click Rate | Interpretation |
|-------------|-----------|---------------|
| Excellent | >5% | Highly engaged audience |
| Good | 3-5% | Strong engagement |
| Average | 2-3% | Industry standard |
| Below Average | 1-2% | Content or CTA issues |
| Poor | <1% | Major content or targeting issues |

### 3. Click-to-Open Rate (CTOR)

```
CTOR = (Unique Clicks / Unique Opens) x 100
```

CTOR measures how compelling the email content was for people who actually opened it. It isolates content effectiveness from subject line effectiveness.

| Performance | CTOR | Interpretation |
|-------------|------|---------------|
| Excellent | >20% | Content is highly relevant |
| Good | 12-20% | Good content-audience match |
| Average | 8-12% | Average content engagement |
| Below Average | 5-8% | Content doesn't match audience expectations |
| Poor | <5% | Subject line promises don't match content |

### 4. Conversion Rate

```
Conversion Rate = (Conversions / Emails Delivered) x 100
```

Conversion is whatever action you want the recipient to take: purchase, signup, download, book a call, etc.

| Type | Good Conversion Rate |
|------|---------------------|
| E-commerce purchase | 1-3% |
| Lead gen form fill | 2-5% |
| Content download | 5-10% |
| Webinar registration | 3-8% |
| Free trial signup | 2-5% |

### 5. Revenue Per Email (RPE)

```
RPE = Total Revenue Attributed / Emails Delivered
```

RPE is the ultimate bottom-line metric for monetized email programs.

| Performance | RPE | Context |
|-------------|-----|---------|
| Excellent | >$0.50 | Highly targeted, promotional |
| Good | $0.10-$0.50 | Well-segmented campaigns |
| Average | $0.02-$0.10 | Standard newsletter/promotional |
| Below Average | <$0.02 | Large list, low conversion |

### 6. List Growth Rate

```
List Growth Rate = ((New Subscribers - Unsubscribes - Hard Bounces) / Total List Size) x 100
```

Monthly list growth rate:

| Performance | Growth Rate | Status |
|-------------|-------------|--------|
| Excellent | >5%/month | Strong acquisition, low churn |
| Good | 2-5%/month | Healthy growth |
| Flat | 0-2%/month | Growth matches churn |
| Declining | Negative | Churn exceeds acquisition — urgent |

### 7. Churn Rate

```
Monthly Churn = (Unsubscribes + Bounces + Complaints) / Total List Size x 100
```

| Performance | Churn Rate | Action |
|-------------|-----------|--------|
| Excellent | <0.5%/month | Healthy list |
| Average | 0.5-1%/month | Monitor, optimize |
| High | 1-2%/month | Investigate causes |
| Critical | >2%/month | Emergency — fix immediately |

---

## Cohort Analysis

Cohort analysis groups subscribers by when they joined and tracks their behavior over time. This reveals whether your email program is getting better or worse.

### How to Run a Cohort Analysis

1. **Define cohorts** by signup month (e.g., Jan 2026 signups, Feb 2026 signups)
2. **Track key metrics** for each cohort over time:
   - Open rate by month since signup
   - Click rate by month since signup
   - Conversion rate by month since signup
   - Churn rate by month since signup

### Cohort Table Example

```
Cohort     | Month 1 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6
           | Opens   | Opens   | Opens   | Opens   | Opens   | Opens
-----------+---------+---------+---------+---------+---------+--------
Jan 2026   | 45%     | 32%     | 28%     | 24%     | 22%     | 20%
Feb 2026   | 42%     | 30%     | 25%     | 22%     | 20%     |
Mar 2026   | 48%     | 35%     | 30%     | 27%     |         |
Apr 2026   | 50%     | 38%     | 33%     |         |         |
```

### What to Look For

| Pattern | Meaning | Action |
|---------|---------|--------|
| Month 1 improving over time | Acquisition quality improving | Keep doing what's working |
| Month 1 declining over time | Acquisition quality declining | Audit lead sources |
| Steep drop after Month 1 | Welcome sequence not retaining | Improve welcome series |
| Gradual steady decline | Normal engagement decay | Add re-engagement triggers |
| Sudden drop at Month X | Something broke at that point | Investigate that email/event |
| Flat/improving after Month 3 | Strong long-term engagement | Healthy program |

---

## Engagement Trending

Track these metrics weekly to catch issues before they become crises:

### Weekly Dashboard Metrics

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Open Rate | Within 10% of 30-day avg | 10-20% below | >20% below |
| Click Rate | Within 10% of 30-day avg | 10-20% below | >20% below |
| Bounce Rate | <0.5% | 0.5-1% | >1% |
| Spam Complaints | <0.05% | 0.05-0.1% | >0.1% |
| Unsubscribe Rate | <0.3% | 0.3-0.5% | >0.5% |
| List Growth | Positive | Flat | Negative |

### Trend Alerts

Set up alerts for:
- Open rate drops >15% compared to 30-day average
- Spam complaint rate exceeds 0.1%
- Bounce rate exceeds 1% on any send
- Unsubscribe rate exceeds 0.5% on any send
- Delivery rate drops below 95%

---

## Attribution Models

### Email-Specific Attribution

| Model | How It Works | Best For |
|-------|-------------|----------|
| Last Click | Email gets credit if it was last click before conversion | Simple, conservative |
| First Click | Email gets credit if it was first touch | Awareness campaigns |
| Linear | Credit split equally across all email touches | Multi-email journeys |
| Time Decay | Recent emails get more credit | Long sales cycles |
| View-Through | Email gets credit if opened (not clicked) before conversion | Brand awareness |

### UTM Parameter Standards

```
utm_source=email
utm_medium=email
utm_campaign={campaign_name}
utm_content={cta_variant}
utm_term={subject_line_variant}
```

**Example:**
```
https://example.com/product?utm_source=email&utm_medium=email&utm_campaign=spring_sale_2026&utm_content=cta_button_red&utm_term=subject_a
```

---

## Analytics Scoring

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| Open rate tracked & benchmarked | 15% | 0-100 |
| Click rate & CTOR measured | 15% | 0-100 |
| Conversion tracking set up | 20% | 0 or 100 |
| Revenue attribution configured | 15% | 0 or 100 |
| List growth/churn monitored | 10% | 0 or 100 |
| Weekly engagement review | 15% | 0 or 100 |
| Cohort analysis done quarterly | 10% | 0 or 100 |
