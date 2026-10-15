# Email Marketing Skill for Claude

A skill that gives Claude deep, opinionated expertise in email, lifecycle, and CRM marketing.

This isn't a generic best-practice summary. It reflects the experience and opinions of a practitioner.

## What the skill can do

With this skill loaded, Claude can:

- **Audit an email programme** — work through a structured checklist (deliverability, list health, lifecycle coverage, automations, cadence, measurement, compliance) and deliver prioritised findings with severity ratings, not generic recommendations
- **Diagnose deliverability problems** — triage in the order a practitioner would (scope, then authentication, then reputation, then list quality, then content last) and prescribe fixes in order of leverage
- **Design automations and sequences** — welcome flows, abandoned cart, post-purchase, re-engagement and winback, each specified with trigger, timing, audience, exit conditions, and a measurable goal
- **Write email copy** — subject lines with rationale, preview text, body copy, and CTAs, delivered in labelled parts; multi-email sequences as structured specs
- **Set up authentication** — SPF, DKIM, and DMARC records, alignment, and troubleshooting failures after ESP changes
- **Plan list building and opt-in** — forms, lead magnets, single vs double opt-in, consent records, and source tracking
- **Design segmentation** — segment models (RFM, value tiers, lifecycle stage, propensity) with an honest account of when segmentation isn't worth its cost
- **Plan and analyse tests** — A/B tests with hypothesis, sample size per cell, minimum detectable effect, and duration; flag underpowered tests instead of running them
- **Measure whether the programme works** — holdouts and control groups, attribution methods and their limits, incrementality, retention and LTV, and impact sizing before anything gets built
- **Compare and select ESPs** — a five-factor evaluation framework applied to your actual requirements
- **Advise beyond email** — SMS/RCS, WhatsApp, mobile and browser push, in-app, wallet passes, direct mail, and more: each channel's permission rules, constraints, costs, and measurement
- **Answer compliance questions** — CAN-SPAM, GDPR, UK GDPR/PECR, CASL, CCPA, and consent for tracking pixels as distinct from consent to send

## Powered by the CRM Open Knowledge Wiki

The skill is driven by the **[CRM Open Knowledge Wiki](https://github.com/jacquescorbytuech/crm-open-knowledge-wiki)** — an open-source practitioner knowledge base in the [Open Knowledge Format (OKF)](https://github.com/jacquescorbytuech/crm-open-knowledge-wiki), browsable at [crmknowledgebase.com](https://crmknowledgebase.com). When Claude has network access, it fetches the relevant wiki pages and grounds its answers in them, covering five layers: principles, foundations, channels, measurement, and references.

The topic files bundled in this repo are a condensed offline fallback for environments without network access.

## Bundled fallback topics

- **[Authentication](email-marketing/authentication.md)** — SPF, DKIM, DMARC setup and troubleshooting; transactional vs marketing email
- **[List building](email-marketing/list-building.md)** — Forms, lead magnets, single vs double opt-in, subscriber source tracking
- **[Segmentation and data](email-marketing/segmentation-and-data.md)** — Segmentation types, dynamic vs static segments, data hygiene, privacy compliance, personalisation and merge tags
- **[Copywriting](email-marketing/copywriting.md)** — Subject lines, email anatomy, CTAs, spam trigger avoidance
- **[Automation and sequences](email-marketing/automation-and-sequences.md)** — Automation triggers, welcome sequences, abandoned cart, re-engagement, campaign goal-setting
- **[Deliverability and metrics](email-marketing/deliverability.md)** — How inbox placement works, getting out of spam, IP warming, full metrics reference, Gmail Promotions tab, MIME structure
- **[ESP selection and reference](email-marketing/esp-and-reference.md)** — Five-factor ESP evaluation framework, legislation quick reference (CAN-SPAM, GDPR, CASL, CCPA), common mistakes, glossary
- **[Impact sizing](email-marketing/impact-sizing.md)** — How to size the potential impact of email experiments: model types, formula mechanics, input gathering, sample size planning
- **[Measurement](email-marketing/measurement.md)** — Core metrics, attribution, holdouts and control groups, retention/LTV, sample size and power, testing frameworks, uplift and incrementality
- **[Channels](email-marketing/channels.md)** — SMS/RCS, push, browser push, in-app, wallet passes, conversational messaging, direct mail, and more: permissions, constraints, and measurement per channel

The bundle also includes **[Workflows](email-marketing/workflows.md)** — task procedures and output formats (programme audit checklist, deliverability triage sequence, campaign brief template, deliverable conventions). Unlike the topic files, this applies whether or not the wiki is reachable.

## Usage

### Claude Code

Clone the repo, then add the skill directory path to your project or user settings in `.claude/settings.json`:

```json
{
  "skills": [
    "/path/to/email-marketing-skill/email-marketing"
  ]
}
```

### Claude.ai

Upload the skill directly: zip the `email-marketing/` directory and add it under **Settings → Capabilities → Skills**. This preserves the bundled topic files, so the skill works even when web access is unavailable.

Alternatively, add the contents of [`email-marketing/SKILL.md`](email-marketing/SKILL.md) as custom instructions in a [Claude.ai project](https://claude.ai) — but note this drops the offline fallback files, so it relies on Claude being able to fetch the wiki (web search/fetch must be enabled on your plan or organisation).

### API / other integrations

Include the contents of [`email-marketing/SKILL.md`](email-marketing/SKILL.md) in your system prompt.

## Examples

Once Claude has access to the skill, ask about anything email marketing related:

- "Help me plan a welcome email sequence"
- "What's wrong with my deliverability?"
- "Write subject lines for a product launch campaign"
- "Should I use single or double opt-in?"
- "Compare Mailchimp and Klaviyo for my use case"
- "Set up SPF and DKIM for my domain"

## Contributing

Contributions are welcome. If you have practitioner-level insights to add, open a PR. Keep the tone opinionated and practical — this skill deliberately avoids wishy-washy "it depends" advice where a clear recommendation is warranted.

## License

MIT
