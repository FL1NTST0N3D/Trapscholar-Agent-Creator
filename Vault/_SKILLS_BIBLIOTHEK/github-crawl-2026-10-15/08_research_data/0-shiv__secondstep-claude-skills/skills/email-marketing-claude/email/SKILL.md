# Email Marketing Audit & Optimization — Main Skill

## Command Routing

When the user invokes an `/email` command, route to the appropriate sub-skill:

| Command | Route To | Description |
|---------|----------|-------------|
| `/email audit` | Run ALL sub-skills sequentially | Full email marketing audit |
| `/email deliverability` | `skills/email-deliverability/SKILL.md` | SPF, DKIM, DMARC, reputation |
| `/email subjects` | `skills/email-subject-lines/SKILL.md` | Subject line optimization |
| `/email sequences` | `skills/email-sequences/SKILL.md` | Email sequence audit |
| `/email segments` | `skills/email-segmentation/SKILL.md` | Segmentation analysis |
| `/email test` | `skills/email-ab-testing/SKILL.md` | A/B testing framework |
| `/email templates` | `skills/email-templates/SKILL.md` | HTML email template audit |
| `/email automation` | `skills/email-automation/SKILL.md` | Workflow & trigger audit |
| `/email analytics` | `skills/email-analytics/SKILL.md` | Metrics deep dive |
| `/email compliance` | `skills/email-compliance/SKILL.md` | Legal compliance check |
| `/email report` | `skills/email-report/SKILL.md` | Generate audit report |

---

## Email Marketing Fundamentals

### The Email Marketing Stack

Every effective email program has 5 layers:

1. **Infrastructure** — Deliverability, authentication (SPF/DKIM/DMARC), sender reputation
2. **List** — Segmentation, hygiene, growth, consent management
3. **Content** — Subject lines, copy, design, personalization
4. **Automation** — Sequences, triggers, workflows, branching logic
5. **Measurement** — Analytics, attribution, testing, optimization

### Key Principle: The Deliverability-First Approach

Nothing else matters if your emails don't reach the inbox. Always audit deliverability FIRST, then work up the stack.

### Email Types

| Type | Purpose | Frequency | Expected Open Rate |
|------|---------|-----------|-------------------|
| Transactional | Order confirmations, receipts, password resets | Event-driven | 80-90% |
| Triggered/Behavioral | Abandoned cart, browse abandonment, re-engagement | Event-driven | 30-50% |
| Lifecycle | Welcome, onboarding, renewal, win-back | Milestone-based | 25-40% |
| Newsletter | Content, updates, education | Weekly/Bi-weekly | 15-25% |
| Promotional | Sales, offers, product launches | Campaign-based | 10-20% |

---

## Industry Benchmarks

Use these benchmarks to score the client's email performance. Compare their metrics to industry averages.

| Industry | Open Rate | Click Rate | Bounce Rate | Unsub Rate | CTOR |
|----------|-----------|------------|-------------|------------|------|
| E-commerce | 15.68% | 2.01% | 0.19% | 0.27% | 12.82% |
| SaaS | 21.29% | 2.45% | 0.40% | 0.35% | 11.51% |
| Healthcare | 21.48% | 2.69% | 0.51% | 0.28% | 12.52% |
| Finance | 21.56% | 2.72% | 0.28% | 0.25% | 12.62% |
| Real Estate | 19.17% | 1.77% | 0.38% | 0.27% | 9.23% |
| Education | 23.42% | 2.90% | 0.31% | 0.21% | 12.38% |
| Agency | 18.56% | 1.89% | 0.45% | 0.35% | 10.18% |
| Nonprofit | 25.17% | 2.79% | 0.33% | 0.20% | 11.09% |
| Media/Publishing | 22.15% | 4.62% | 0.14% | 0.12% | 20.86% |
| Travel/Hospitality | 20.44% | 2.25% | 0.31% | 0.24% | 11.01% |

**CTOR** = Click-to-Open Rate = (Clicks / Opens) x 100. This is a better engagement metric than raw click rate because it measures how compelling the email content was for people who actually opened it.

### Performance Tiers

| Tier | vs Benchmark | Interpretation |
|------|-------------|----------------|
| Elite | >150% of benchmark | Top performer, optimize for diminishing returns |
| Strong | 100-150% of benchmark | Above average, keep optimizing |
| Average | 75-100% of benchmark | Room for improvement |
| Below Average | 50-75% of benchmark | Significant issues to address |
| Critical | <50% of benchmark | Major problems, likely deliverability issues |

---

## Email Health Score Calculation

The Email Health Score (0-100) is calculated across 10 weighted dimensions:

```
Email Health Score = Sum of (Dimension Score x Weight)

Dimensions:
  Deliverability:  20% weight
  Subject Lines:   10% weight
  Sequences:       15% weight
  Segmentation:    10% weight
  A/B Testing:      5% weight
  Templates:       10% weight
  Automation:      10% weight
  Analytics:        5% weight
  Compliance:      10% weight
  List Health:      5% weight
```

Each dimension is scored 0-100 based on the criteria defined in its sub-skill file.

### Score Interpretation

| Score | Grade | Meaning |
|-------|-------|---------|
| 90-100 | A+ | Elite. Top 5% of email programs. |
| 80-89 | A | Excellent. Minor optimizations only. |
| 70-79 | B | Strong. A few areas need attention. |
| 60-69 | C | Average. Significant revenue left on the table. |
| 50-59 | D | Below average. Multiple areas need work. |
| 40-49 | F | Poor. Major overhaul required. |
| 0-39 | Critical | Emails are likely hurting your brand. |

---

## Audit Workflow

When running `/email audit` (full audit), follow this sequence:

1. **Gather Information**
   - Ask for: ESP/platform (Mailchimp, Klaviyo, HubSpot, etc.)
   - Ask for: Industry vertical
   - Ask for: List size and monthly send volume
   - Ask for: Current metrics (open rate, click rate, bounce rate, unsub rate)
   - Ask for: Domain used for sending
   - Ask for: Key email sequences in place

2. **Run Deliverability Check** (skills/email-deliverability/)
3. **Audit Subject Lines** (skills/email-subject-lines/)
4. **Review Sequences** (skills/email-sequences/)
5. **Analyze Segmentation** (skills/email-segmentation/)
6. **Check A/B Testing** (skills/email-ab-testing/)
7. **Audit Templates** (skills/email-templates/)
8. **Review Automation** (skills/email-automation/)
9. **Analyze Metrics** (skills/email-analytics/)
10. **Check Compliance** (skills/email-compliance/)
11. **Generate Report** (skills/email-report/)

---

## Quick Wins Checklist

These are the highest-impact, lowest-effort fixes. Always surface these first:

- [ ] Authenticate domain (SPF + DKIM + DMARC)
- [ ] Remove hard bounces from list immediately
- [ ] Add double opt-in for new subscribers
- [ ] Set up sunset policy for unengaged subscribers (90+ days no open)
- [ ] Add preheader text to all emails
- [ ] Ensure unsubscribe link is visible (not hidden in tiny text)
- [ ] Test emails in dark mode
- [ ] Add alt text to all images
- [ ] Set up abandoned cart sequence (if e-commerce)
- [ ] Set up welcome sequence for new subscribers
