# Email Automation — Sub-Skill

## Overview

Email automation turns manual campaigns into revenue-generating machines that work 24/7. This sub-skill covers trigger mapping, behavioral automation, time-based drips, conditional branching, lifecycle workflows, and re-engagement systems.

**Command:** `/email automation`

---

## Automation Audit Checklist

- [ ] Welcome automation is active and triggering correctly
- [ ] Behavioral triggers are configured (page visit, download, cart abandon)
- [ ] Time-based drips are set up for nurture and onboarding
- [ ] Conditional branching (if/then) logic is used where appropriate
- [ ] Lifecycle automations cover key transitions
- [ ] Re-engagement workflow exists for dormant subscribers
- [ ] Automations have clear entry and exit criteria
- [ ] No subscriber is stuck in a loop or dead-end
- [ ] Automations are reviewed/updated at least quarterly
- [ ] Performance metrics are tracked per automation

---

## 1. Behavioral Triggers

Behavioral triggers fire based on specific actions a subscriber takes. These produce the highest-converting emails because they're contextually relevant.

### Trigger Inventory

| Trigger Event | Email Action | Timing | Expected Performance |
|--------------|-------------|--------|---------------------|
| Page visit (product) | Browse abandonment email | 2-4 hours | 20-30% open rate |
| Page visit (pricing) | Sales follow-up | 1 hour | 30-40% open rate |
| Content download | Related content nurture | Immediate + day 3 | 35-45% open rate |
| Cart abandon | Cart recovery sequence | 1hr, 24hr, 72hr | 40-50% open rate |
| Purchase completed | Order confirmation + upsell | Immediate | 70-80% open rate |
| Account created | Onboarding sequence | Immediate | 50-60% open rate |
| Feature used | Next feature suggestion | 24 hours | 25-35% open rate |
| Feature NOT used | Adoption nudge | 3-7 days | 20-30% open rate |
| Subscription renewal | Renewal reminder | 30, 7, 1 day before | 40-50% open rate |
| Support ticket closed | Feedback/NPS request | 24 hours | 30-40% open rate |
| Webinar registration | Confirmation + reminders | Immediate + day before | 50-60% open rate |
| Webinar attended | Follow-up + resources | 1 hour after | 40-50% open rate |
| Webinar missed | Recording + recap | 2 hours after | 30-40% open rate |

### Trigger Configuration Best Practices
- Set frequency caps: max 1 behavioral email per trigger type per 7 days
- De-duplicate: don't send cart abandon if they already purchased
- Priority rules: transactional > behavioral > promotional
- Suppress during active sequences (don't stack on welcome series)

---

## 2. Time-Based Drips

Time-based automations deliver content on a schedule, typically starting from a trigger event.

### Drip Types

| Drip Type | Trigger | Duration | Cadence |
|-----------|---------|----------|---------|
| Welcome | Signup | 14 days | Every 2-3 days |
| Onboarding | First purchase/signup | 21 days | Every 3-4 days |
| Nurture | Lead magnet download | 8 weeks | Weekly |
| Course/Education | Enrollment | Varies | Daily or every other day |
| Seasonal | Calendar date | 2-4 weeks before | 2-3 emails |
| Re-engagement | Inactivity threshold | 28 days | Weekly |

### Drip Timing Best Practices

```
Welcome Sequence Timing:
  Email 1: Immediate (within 5 minutes of signup)
  Email 2: Day 1 (24 hours later)
  Email 3: Day 3
  Email 4: Day 5
  Email 5: Day 7
  Email 6: Day 10
  Email 7: Day 14

Cart Abandonment Timing:
  Email 1: 1 hour after abandon
  Email 2: 24 hours after abandon
  Email 3: 72 hours after abandon

Win-Back Timing:
  Email 1: Day 0 (trigger: 90 days inactive)
  Email 2: Day 7
  Email 3: Day 14
  Email 4: Day 21
  Email 5: Day 28 (final)
```

---

## 3. Conditional Branching (If/Then Logic)

Branching makes automations smart by adapting to subscriber behavior within the workflow.

### Common Branch Points

| Condition | Yes Branch | No Branch |
|-----------|-----------|-----------|
| Opened email? | Send next in sequence | Re-send with new subject |
| Clicked CTA? | Move to sales sequence | Continue nurture |
| Visited pricing page? | Send case study + sales CTA | Send more educational content |
| Made a purchase? | Exit sequence, start onboarding | Continue abandon/nurture |
| Engagement score > 50? | Fast-track to sales | Continue warming |
| Is in segment X? | Send segment-specific content | Send general content |

### Branching Architecture Example

```
Trigger: Downloads lead magnet
  ↓
Email 1: Welcome + deliver content (Day 0)
  ↓
Wait 3 days
  ↓
Branch: Opened Email 1?
  ├── YES → Email 2: Quick win tip (Day 3)
  └── NO → Email 2B: Re-send with new subject (Day 3)
       ↓
       Wait 2 days
       ↓
       Branch: Opened Email 2B?
       ├── YES → Rejoin main sequence at Email 3
       └── NO → Add to "low engagement" segment, reduce frequency

  ↓ (continuing YES branch)
Wait 4 days
  ↓
Email 3: Case study (Day 7)
  ↓
Branch: Clicked CTA in Email 3?
  ├── YES → Move to Sales Sequence
  └── NO → Email 4: Different angle content (Day 10)
       ↓
       Email 5: Soft sell (Day 14)
       ↓
       Branch: Any purchase made?
       ├── YES → Exit, start Onboarding
       └── NO → Move to long-term Nurture
```

---

## 4. Lifecycle Automations

Map automations to every key lifecycle transition.

### The Lifecycle Automation Map

| Transition | Automation | Priority |
|-----------|-----------|----------|
| Stranger → Subscriber | Lead capture confirmation | Critical |
| Subscriber → Engaged | Welcome sequence | Critical |
| Engaged → First Buyer | Conversion sequence | Critical |
| First Buyer → Repeat Buyer | Post-purchase sequence | Critical |
| Repeat Buyer → Loyal | Loyalty rewards | High |
| Loyal → Advocate | Referral program | High |
| Active → At Risk | Re-engagement trigger | High |
| At Risk → Churned | Win-back sequence | Medium |
| Churned → Reactivated | Welcome-back offer | Medium |
| Any → Cancelled/Unsubscribed | Offboarding/feedback | Low |

### Critical Automation: Post-Purchase

The post-purchase automation is often neglected but has the highest impact on LTV.

```
Purchase completed
  ↓
Email 1: Order confirmation (Immediate)
  ↓
Email 2: Shipping notification (When shipped)
  ↓
Email 3: Delivery confirmation + usage tips (Delivery day)
  ↓
Wait 3 days
  ↓
Email 4: "How's your [product]?" + quick feedback (Day 3)
  ↓
Wait 7 days
  ↓
Email 5: Cross-sell recommendation (Day 10)
  ↓
Wait 14 days
  ↓
Email 6: Request review/testimonial (Day 24)
  ↓
Wait 30 days
  ↓
Email 7: Replenishment/rebuy reminder (Day 54 — if applicable)
```

---

## 5. Re-Engagement Workflows

### Sunset Policy

Every email program needs a sunset policy — a defined process for handling subscribers who stop engaging.

```
Engagement drops (no opens in 30 days)
  ↓
Reduce frequency: move to 1x/week max
  ↓
No engagement for 60 days
  ↓
Trigger re-engagement sequence (5 emails over 28 days)
  ↓
Branch: Re-engaged?
  ├── YES → Return to active segments, reset engagement score
  └── NO → Suppress from all sends
       ↓
       Wait 90 days
       ↓
       Final win-back attempt (single email)
       ↓
       Branch: Re-engaged?
       ├── YES → Return to active, monitor closely
       └── NO → Permanent suppression (never delete — compliance)
```

---

## Automation Performance Benchmarks

| Automation Type | Open Rate Target | Click Rate Target | Conversion Target |
|----------------|-----------------|-------------------|-------------------|
| Welcome | 50-60% | 10-15% | 5-10% (first purchase) |
| Cart Abandon | 40-50% | 10-15% | 5-10% (recovery) |
| Browse Abandon | 20-30% | 3-5% | 1-3% |
| Post-Purchase | 50-60% | 5-10% | 3-5% (cross-sell) |
| Win-Back | 15-25% | 2-4% | 1-3% |
| Re-engagement | 10-20% | 2-3% | N/A (re-activation) |
| Onboarding | 40-50% | 8-12% | Varies |

---

## Automation Scoring

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| Welcome automation active | 20% | 0 or 100 |
| Behavioral triggers configured | 20% | 0-100 based on coverage |
| Conditional branching used | 15% | 0 or 100 |
| Lifecycle transitions covered | 15% | 0-100 based on coverage |
| Re-engagement workflow exists | 15% | 0 or 100 |
| Automations reviewed quarterly | 15% | 0 or 100 |
