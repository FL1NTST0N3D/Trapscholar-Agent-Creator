# Workflows and Deliverable Formats

Task procedures and output conventions for the most common deliverables. This file tells you how to structure the output; get the facts from the wiki pages (see the routing table in [SKILL.md](SKILL.md)). This file is always applicable — it is not a network fallback.

---

## Programme Audit Checklist

When asked to audit or review an email/CRM programme, work through these areas in order. For each, state what's in place, what's missing, and a severity (critical / important / nice-to-have). Don't produce a wall of generic recommendations — tie every finding to something observed.

1. **Foundations and deliverability**
   - SPF, DKIM, DMARC all passing? DMARC policy beyond `p=none`? One-click unsubscribe honoured?
   - Spam complaint rate, bounce handling, and suppression hygiene. Any shared vs dedicated IP mismatch for volume?
2. **List and data health**
   - Net list growth vs churn. Where do subscribers come from, and is source tracked?
   - Sunset policy for inactives? A list that only grows is a deliverability problem in waiting.
   - Consent records: could they evidence opt-in per contact if challenged?
3. **Lifecycle coverage**
   - Map what exists against acquisition → onboarding → engagement → retention → winback. Most programmes over-invest in broadcast and under-invest in the welcome window.
   - Is there a welcome sequence at all? It's the highest-leverage automation; flag its absence as critical.
4. **Automations**
   - Which triggered flows exist (welcome, abandoned cart/browse, post-purchase, re-engagement)? Does each have a stated goal and a measured conversion?
   - Any flow built without a goal is theatre — say so.
5. **Campaigns and cadence**
   - Frequency: consistent, and matched to what was promised at sign-up? Any frequency capping across channels?
   - Segmentation: is it earning its complexity, or slicing a small list into unmeasurable cells?
6. **Measurement**
   - What's actually measured: opens (directional only), clicks, conversions, revenue per email?
   - Any holdout or control groups? Any attribution beyond last-click? If the programme's value has never been measured against a control, note that its reported ROI is unverified.
7. **Compliance**
   - Unsubscribe honoured promptly and cross-channel? Physical address present where required? Transactional and marketing streams kept clean of each other?

**Output format:** lead with a 3–5 bullet executive summary of the biggest gaps, then findings by area with severity, then a prioritised action list (max ~8 items, quick wins flagged).

---

## Deliverability Triage Sequence

When someone reports "emails going to spam" or falling engagement, diagnose in this order — cheapest checks first, and don't recommend fixes before locating the problem:

1. **Scope it.** All recipients or one mailbox provider (Gmail vs Outlook vs Yahoo)? Spam folder, Promotions tab, or silently dropped? Marketing stream, transactional, or both? Since when — and what changed around that date (new template, list import, volume spike, new domain/IP, ESP migration)?
2. **Check authentication.** SPF, DKIM, DMARC alignment on the actual sending domain (not just the org domain). One failing DKIM signature after an ESP change is a classic cause.
3. **Check reputation signals.** Google Postmaster Tools (domain and IP reputation, spam rate vs the 0.1%/0.3% thresholds), blocklist checks, bounce codes from recent sends — bounce messages often say exactly what's wrong.
4. **Check list quality.** Recent list imports or purchased data? Complaint rate trend? Share of sends going to 180-day+ inactives? Engagement *is* deliverability: sending to people who never open trains providers to junk you.
5. **Check content and volume last.** Sudden volume spikes, drastic template changes, link shorteners, mismatched from-domains. Content is the most commonly blamed and least commonly guilty factor — do not lead with "avoid spam words".
6. **Prescribe in order of leverage:** fix auth failures → cut sends to inactives and tighten the audience to engaged recipients → fix the complaint source (expectation mismatch, cadence, opt-in quality) → rebuild reputation gradually. Warn that recovery takes weeks of consistent good behaviour, not a single fix.

---

## Campaign / Automation Brief Template

Before building or writing anything, produce (or ask for) a brief in this shape. If the goal can't be filled in, stop — that's the finding.

- **Goal:** the single measurable outcome (e.g. "recover 5% of abandoned carts within 7 days"), not "engagement".
- **Audience:** who exactly receives it, entry criteria, exclusions/suppressions.
- **Trigger or schedule:** event-triggered (what event, what delay) or broadcast (when, why then).
- **Message(s):** count, sequence, and the one job of each message.
- **Offer/incentive:** if any — and what it costs.
- **Success measure:** the metric, the baseline, and how it will be read (holdout? conversion window? attribution basis).
- **Exit conditions:** what removes someone from the flow (conversion, unsubscribe, entering another flow).

---

## Output Conventions

**Sequence specs.** Deliver multi-email sequences as a table — one row per message — with columns: # / timing (relative to trigger) / job of the email / subject line / key content beats / CTA. Follow with full copy per email only if asked or if the task is explicitly copywriting.

**Subject line batches.** When asked for subject lines, give 5–10 options grouped by angle (benefit-led, curiosity, urgency, plain-spoken), each with a one-line rationale. Flag any that risk over-promising — a subject line that wins the open but breaks the promise costs more than it earns. Recommend a favourite; don't leave it as an undifferentiated list.

**Copy deliverables.** Provide subject line, preview text, body, and CTA as distinct labelled parts. Write preview text deliberately — it's the second subject line, not an afterthought.

**Test proposals.** Any proposed A/B test must state: hypothesis, primary metric, minimum detectable effect, required sample size per cell, and expected duration. If the audience can't power the test, say so and propose a bigger lever instead — an underpowered test is worse than no test.

**Metric reporting.** When interpreting performance, always distinguish directional metrics (opens, clicks) from outcome metrics (conversions, revenue), and never present a small difference as a win without noting whether it clears statistical noise.
