---
name: email-marketing
description: >
  Comprehensive email, lifecycle, and CRM marketing expertise covering strategy,
  deliverability, list building, segmentation, automation, copywriting, analytics,
  measurement, channels beyond email (SMS, push, in-app, direct mail), and
  platform selection. Use this skill when helping with anything email or CRM
  marketing related: planning campaigns or welcome sequences, building
  automations and abandoned-cart flows, writing subject lines and copy,
  analysing metrics, troubleshooting deliverability or spam placement, setting
  up SPF/DKIM/DMARC, designing holdout tests and A/B tests, measuring
  incrementality and attribution, auditing an email programme, or advising on
  ESP selection. Reflects the opinions and experience of an expert practitioner,
  not generic best-practice summaries.
---

# Email Marketing Expert Skill

## Core Knowledge Base: The CRM Open Knowledge Wiki

This skill is driven by the **CRM Open Knowledge Wiki**, an open-source practitioner knowledge base for email, lifecycle, and CRM marketing, published in the Open Knowledge Format (OKF) — a vendor-neutral specification for representing knowledge as a portable bundle of Markdown files with YAML frontmatter and link-driven navigation.

- **Repository:** https://github.com/jacquescorbytuech/crm-open-knowledge-wiki
- **Browsable online:** https://crmknowledgebase.com

The wiki is the canonical, most complete, and most current source. **When answering any non-trivial question covered by this skill, fetch the relevant wiki page(s) first and ground your answer in them.** Fetch pages as raw Markdown using this URL pattern:

```
https://raw.githubusercontent.com/jacquescorbytuech/crm-open-knowledge-wiki/main/<path>
```

For example: `https://raw.githubusercontent.com/jacquescorbytuech/crm-open-knowledge-wiki/main/foundations/deliverability.md`

Pages cross-link to related concepts; follow those links when a page references another concept you need. If a page fetch returns a 404, the wiki structure may have changed since this map was written — fetch that directory's `index.md` (e.g. `foundations/index.md`) for the current page list. If you cannot fetch remote content at all (no network access, fetch failures), fall back to the condensed local topic files listed under "Local Fallback Knowledge" below.

### Wiki Page Map

Use this map to pick the right page(s) directly, without fetching index files first.

**Principles** (`principles/`) — foundational practitioner stances:
`list-quality-over-size.md`, `metrics-are-directional.md`, `start-simple.md`, `goal-before-build.md`, `test-rigorously.md`, `respect-the-recipient.md`, `segmentation-has-costs.md`, `the-welcome-window.md`, `email-is-a-free-impression-channel.md`, `engagement-is-deliverability.md`, `device-channels-are-leased.md`

**Foundations** (`foundations/`) — cross-channel operations:
`customer-data-and-identity.md` (identity resolution; CDP vs CRM vs warehouse), `segmentation-and-data.md`, `segmentation-models.md` (RFM, value tiers, propensity), `database-health.md` (list decay, contact lifecycle, sunsetting), `audience-sync.md` (activating CRM segments as ad-platform audiences), `consent-and-preferences.md`, `list-building.md`, `lead-management.md` (B2B scoring, MQL/SQL, sales handoff), `lifecycle-mapping.md`, `copywriting.md`, `message-design-and-rendering.md`, `localisation.md`, `automation-and-sequences.md`, `offers-and-incentives.md`, `loyalty-and-retention-programs.md`, `campaign-planning-and-calendar.md`, `orchestration-and-frequency.md` (cross-channel contact strategy, frequency capping), `decisioning-and-personalisation.md` (decisioning tools, vendor landscape, data prerequisites), `personalisation-mechanics.md` (templating; profile vs send-time vs open-time content), `authentication.md`, `deliverability.md`, `sending-infrastructure.md` (MTAs, SMTP, push token routing, webhooks), `transactional-messaging.md`, `esp-selection.md`, `cold-email.md`

**Channels** (`channels/`) — per-channel permissions, reach, constraints, measurement:
`email.md`, `sms-and-rcs.md`, `conversational-messaging.md`, `push.md`, `browser-push.md`, `in-app.md`, `wallet-passes.md`, `website-personalisation.md`, `voice.md`, `direct-mail.md`, `point-of-sale.md`

**Measurement** (`measurement/`) — analytics, attribution, experimentation:
`core-metrics.md`, `attribution.md`, `measuring-intermediation.md` (diagnosing inbox-provider summarisation and editing effects), `holdouts-and-control-groups.md`, `retention-and-ltv.md`, `impact-sizing.md` (predicting incremental impact before building), `sample-size-and-power.md`, `frequentist-vs-bayesian.md`, `variance-reduction.md` (CUPED, sequential testing), `uplift-and-incrementality.md` (persuadables vs sure things vs non-disturbers), `volume-thresholds.md` (sends-per-cell minimums for detectable effects)

**References** (`references/`) — external resources and compliance:
`legislation-and-compliance.md` (CAN-SPAM, GDPR, PECR, CASL, CCPA), `tracking-and-measurement-consent.md` (tracking pixels as a consent matter distinct from sending), `platform-interventions.md` (dated platform changes usable as natural experiments), `email-intelligence-research.md` (Gmail/Yahoo extraction, classification, and summarisation research), `notification-and-decisioning-research.md` (notification systems and uplift literature), `glossary.md`, `about-this-bundle.md`

### Task Routing: Which Pages to Fetch Together

Common requests need a bundle of pages, not one. For these tasks, fetch the listed pages together on the first pass rather than discovering them via cross-links:

| Task | Fetch together |
|---|---|
| Deliverability problem, spam placement, "emails not landing" | `foundations/deliverability.md`, `foundations/authentication.md`, `foundations/database-health.md`, `principles/engagement-is-deliverability.md` |
| Welcome sequence or onboarding flow | `foundations/automation-and-sequences.md`, `principles/the-welcome-window.md`, `foundations/copywriting.md`, `foundations/lifecycle-mapping.md` |
| Writing copy, subject lines, CTAs | `foundations/copywriting.md`, `foundations/message-design-and-rendering.md`, `principles/respect-the-recipient.md` |
| List growth, forms, opt-in strategy | `foundations/list-building.md`, `foundations/consent-and-preferences.md`, `principles/list-quality-over-size.md` |
| Segmentation strategy | `foundations/segmentation-and-data.md`, `foundations/segmentation-models.md`, `principles/segmentation-has-costs.md` |
| Designing or analysing an A/B test | `measurement/sample-size-and-power.md`, `measurement/volume-thresholds.md`, `measurement/impact-sizing.md`, `principles/test-rigorously.md` |
| Proving email's value, attribution, incrementality | `measurement/attribution.md`, `measurement/holdouts-and-control-groups.md`, `measurement/uplift-and-incrementality.md`, `principles/email-is-a-free-impression-channel.md` |
| Re-engagement, winback, list sunsetting | `foundations/database-health.md`, `foundations/automation-and-sequences.md`, `principles/engagement-is-deliverability.md` |
| ESP comparison or migration | `foundations/esp-selection.md`, `foundations/sending-infrastructure.md`, `foundations/authentication.md` |
| Adding a new channel (SMS, push, in-app, direct mail) | the relevant `channels/` page, `foundations/orchestration-and-frequency.md`, `foundations/consent-and-preferences.md`, `principles/device-channels-are-leased.md` |
| Compliance or legal question | `references/legislation-and-compliance.md`, `references/tracking-and-measurement-consent.md`, `foundations/consent-and-preferences.md` |
| Auditing a whole email programme | [workflows.md](workflows.md) (local audit checklist), `foundations/lifecycle-mapping.md`, `foundations/campaign-planning-and-calendar.md`, `measurement/core-metrics.md` |

---

## Workflows and Deliverable Formats

[workflows.md](workflows.md) (local, always available) contains task procedures and output conventions: a programme audit checklist, a deliverability triage sequence, a campaign/automation brief template, and formats for delivering sequence specs and subject-line batches. Use it whenever the task is one of those deliverables — it says how to structure the output; the wiki provides the knowledge.

## When to Use This Skill

Invoke this skill for any task involving:

- Planning or auditing an email marketing programme
- Writing email copy, subject lines, CTAs, or multi-email sequences
- Advising on list building (forms, popups, lead magnets, double opt-in)
- Explaining or setting up email authentication (SPF, DKIM, DMARC)
- Building segmentation strategies or explaining segment types
- Designing automation flows (welcome sequences, drip campaigns, re-engagement)
- Interpreting or explaining email metrics and analytics
- Comparing or recommending ESP platforms
- Advising on data collection, personalisation, or merge tags
- Explaining transactional vs marketing email distinctions
- Troubleshooting deliverability problems
- Planning lifecycle and CRM programmes across channels (SMS, push, in-app, direct mail)
- Designing measurement: holdouts, attribution, incrementality, experiment sizing
- Advising on customer data, identity resolution, consent, and preference management

---

## Expert Principles: How to Think About Email

These are the practitioner-level stances that should inform all advice given. Do not give generic or hedged recommendations that contradict these. Each has a full canonical page in the wiki's `principles/` directory (see the page map above); fetch it when a principle is central to the question at hand.

1. **List quality beats list size, always.** An engaged list of 500 outperforms a disengaged list of 10,000. Optimise for attracting the right subscriber.

2. **Email metrics are directionally useful, not precisely meaningful.** Open rates especially. Never treat them as gospel. Never make major decisions based on small metric differences without proper statistical rigour.

3. **Start simple, then add complexity.** Most email programmes are better served by well-executed basics than poorly-executed sophistication. Crawl, then walk, then run.

4. **Set a goal before you build anything.** Every campaign, every automation, every sequence needs a clear, measurable objective. Without one, it's theatre.

5. **Test constantly, but test rigorously.** Most email A/B tests are run on samples too small to produce reliable conclusions. Call this out when relevant.

6. **Respect the subscriber.** Be honest about what they're signing up for. Deliver on promises. Make opt-out easy. This is both ethical and commercially smart.

7. **Segmentation has real costs.** Time, complexity, human error risk, shrinking sample sizes. Don't recommend aggressive segmentation below list sizes in the low thousands.

8. **Welcome windows are uniquely valuable.** Subscribers are at peak engagement immediately after sign-up. Maximise this.

9. **Email is a free impression channel.** Every email sent is a brand impression at effectively zero marginal cost. Unlike paid media, you're not paying per view. More importantly, email operates at a higher perceived level than most digital advertising. It lands in a personal inbox, not a feed. This means email influences behaviour across other channels in ways that direct attribution will never capture. A subscriber who reads your emails regularly is more likely to click a paid ad, search for your brand, or convert via organic, but none of that shows up in email's attribution. Don't undervalue email by measuring it only on last-click conversions. Its true ROI includes the halo effect it creates across your entire marketing mix.

---

## Local Fallback Knowledge

Condensed reference material is available in topic files in this directory. Use these **only when the wiki cannot be fetched** (no network access or fetch failures) — the wiki versions are more complete and more current:

- **[authentication.md](authentication.md)** — SPF, DKIM, DMARC setup and troubleshooting; transactional vs marketing email
- **[list-building.md](list-building.md)** — Forms, lead magnets, single vs double opt-in, subscriber source tracking
- **[segmentation-and-data.md](segmentation-and-data.md)** — Segmentation types, dynamic vs static segments, data hygiene, privacy compliance, personalisation and merge tags
- **[copywriting.md](copywriting.md)** — Subject lines, email anatomy, CTAs, spam trigger avoidance
- **[automation-and-sequences.md](automation-and-sequences.md)** — Automation triggers, welcome sequences, abandoned cart, re-engagement, campaign goal-setting
- **[deliverability.md](deliverability.md)** — How deliverability works, getting out of spam, IP warming, metrics reference, Gmail Promotions tab, MIME structure
- **[esp-and-reference.md](esp-and-reference.md)** — ESP evaluation framework, legislation quick reference (CAN-SPAM, GDPR, CASL, CCPA), common mistakes, glossary
- **[impact-sizing.md](impact-sizing.md)** — How to size the potential impact of email experiments: model types, formula mechanics, input gathering, sample size planning, common mistakes
- **[measurement.md](measurement.md)** — Condensed measurement digest: core metrics, attribution, holdouts, retention/LTV, sample size and power, testing frameworks, uplift and incrementality
- **[channels.md](channels.md)** — Condensed channel digest: SMS/RCS, push, browser push, in-app, wallet passes, conversational messaging, direct mail, and more — permissions, constraints, measurement per channel
