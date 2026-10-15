# Incident Runbooks: When Things Go Wrong

Each runbook: DETECT (signal), TRIAGE (first 3 checks, in order), ACT (agent does),
ESCALATE (needs the human operator), PREVENT (stops recurrence). Generic across
Meta, Google, YouTube, TikTok, any industry, any region.

**Global rules (apply to every runbook)**
- Stabilise, then diagnose, then change. One change at a time, logged with a timestamp.
- Never optimize on data you have not validated. Broken data is worse than no data.
- Never enter, store or request payment details, passwords or 2FA codes. Ever.
- Never delete campaigns, ads, audiences or pixels during an incident. Pause, do not purge.
- Client-facing wording: state what happened, what is paused, what it costs, next step.

## Severity scale

| Sev | Meaning | Response clock | Examples |
|-----|---------|----------------|----------|
| S1 | Spend at risk or account down | Act in minutes, tell operator now | disabled account, >2x daily spend, billing block, tracking dead on live spend, compromised access |
| S2 | Performance degraded, spend still safe | Same day | CPA +30% for 3 days, fatigue, pacing off by >20%, partial rejections |
| S3 | Cosmetic or low impact | Next review | one ad rejected with spare ads live, label or naming errors, dashboard lag |

## Canonical pacing thresholds (this file is the SOURCE OF TRUTH)

| Level | Trigger | Action |
|-------|---------|--------|
| Normal | Daily spend within ±20% of plan | none |
| Investigate | Daily spend off plan by more than ±20% (either way) | runbook 5, same day |
| Emergency (S1) | Spend above 2x the daily budget in a single day | pause, tell operator now |

Other files quoting ±30% or other pacing numbers are superseded by this table.
Platform context [E], verify in current platform docs before quoting to a client: Meta may
spend over a daily budget on a given day and balances across the week; Google may spend up
to ~2x daily budget on a day and caps the month at roughly 30.4x the daily figure. Over 2x
in a day is still treated as broken here, not as "normal delivery variance".

## 1. Ad account disabled / Business Manager restricted (Meta, Google)

- **DETECT:** account status banner, delivery stops, email from platform, API errors
  on every call, "account restricted" in Business Manager or Ads Manager.
- **TRIAGE:** (1) Read the exact reason and the reference ID shown, not the email
  summary. (2) Check billing status and any recent failed charge. (3) Check change
  history and security centre for unknown logins, new admins, new payment methods.
  Then check linked assets: a banned page, pixel, domain or sibling account can drag
  others down.
- **ACT:**
  - File ONE appeal, with evidence matched to the stated reason (business registration,
    domain ownership, invoices, ID verification, landing-page compliance screenshots).
    Never spam appeals or open duplicates: repeat submissions reset or lower priority.
  - Wait the stated review window before any follow-up. Use the escalation channel
    the platform gives (support chat, account rep) once, with the case ID.
  - Live campaigns on OTHER accounts: do not move budget into them in a panic, and do
    not copy the offending ads or landing page into them (contamination risk). Check
    those accounts share no payment method, admin or page with the restricted one,
    then run them at current budget and watch policy status daily.
  - Do not create replacement accounts to evade a ban. That is a policy violation.
- **ESCALATE:** operator for identity verification, business documents, any payment
  method change, and the decision to inform the client.
- **PREVENT:** verified business, 2+ admins, 2FA on all, separate asset hygiene per
  client, documented billing owner, policy review before launch, no restricted-claim
  creative.

## 2. Ad / creative policy rejection

- **DETECT:** "Not approved", "Limited", "Disapproved" status; policy email; spend
  drops on a subset of ads.
- **TRIAGE:** (1) Open the exact policy name cited and read the full text and examples.
  (2) Look at what actually tripped it: image, copy, landing page, destination mismatch,
  targeting. (3) Check account history: strikes, prior rejections of the same pattern.
- **ACT (fix vs appeal rule):**

| Situation | Decision |
|-----------|----------|
| Violation is real or plausible (claim, before/after, personal attributes) | FIX, resubmit as new version |
| Policy clearly misapplied and you can quote the clause | ONE appeal with evidence |
| Ambiguous, fix is cheap | FIX, do not argue |
| Same pattern rejected twice | Stop, rewrite the whole angle, ask operator |

  - Regulated verticals (health, skincare claims, finance, gambling, alcohol, medical
    devices, jobs, housing): the claim is usually the cause. Remove outcome promises,
    "cure", "guaranteed", body-condition callouts, implied before/after, unsupported
    superlatives. Check local ad rules (e.g. ASCI and cosmetic claim rules in India,
    ASA/CAP in the UK, FTC in the US) and special-category requirements per platform.
  - Landing page must match the ad claim. Fix the page, then resubmit the ad.
  - Repeat offences accumulate at account level and can lead to disablement
    (runbook 1). Never resubmit the identical rejected asset in a new ad.
- **ESCALATE:** operator if the claim is the client's core selling point and the fix
  changes the offer; client sign-off for claim changes.
- **PREVENT:** pre-flight policy checklist per vertical, claim substantiation file,
  always keep 2+ approved ads per ad set so one rejection never stops delivery.

## 3. Tracking break mid-flight

- **DETECT:** clicks/impressions steady, conversions flatline or drop >50% day over day
  with no matching traffic or site change; platform vs backend conversion gap widens
  past your normal band; event diagnostics warnings.
- **TRIAGE (in this order):**
  1. Does the tag fire? Tag assistant / pixel helper / network tab on the thank-you or
     purchase step. Recent site, theme, checkout or CMP deploy is the usual culprit.
  2. Consent: did the consent banner, CMP update or consent mode change block events?
  3. Dedup and event IDs: browser and server events double counting or cancelling.
  4. Server endpoint: server-side container, conversions API, token expiry, endpoint
     status codes, queue backlog.
  5. Attribution or conversion-action change: window changed, primary action edited,
     account-level setting altered (check change history).
- **ACT:** compare to backend orders/leads to confirm real sales are still happening.
  **Do NOT optimize on broken data.** No bid changes, no kills, no scaling, no creative
  verdicts while the signal is wrong; automated bidding will chase the false drop.
  - Freeze vs pause: backend shows demand healthy and spend is modest, FREEZE (no edits,
    keep running, cap budget at current level, bidding on manual or cost cap if the
    platform allows without resetting learning). Spend is large or backend shows no
    sales either, PAUSE until verified.
  - After the fix, mark the gap in the log and annotate dashboards; exclude those days
    from trend decisions. Learning may need a few days to recover.
- **ESCALATE:** operator if the fix needs site, GTM, server or CMP changes, or the
  client's developer.
- **PREVENT:** daily platform-vs-backend reconciliation, alerts on zero-conversion
  days, test purchase after every deploy, documented tracking spec.

## 4. Sudden CPA spike / performance collapse

- **DETECT:** CPA or CAC +30% or more vs 7-day baseline for 2+ days, or ROAS drop of
  the same size, with spend steady.
- **TRIAGE (strict order, do not skip ahead):**
  1. Tracking (runbook 3). If conversions are mis-reported, stop here.
  2. Landing page and offer availability: site up, checkout works, page speed, price
     or stock-out, expired promo, payment gateway errors, wrong link in the ad.
  3. Auction and seasonality: CPM, CPC, CTR movement; holidays, sale events, competitor
     surges. CPM up but CVR flat means the market moved, not you.
  4. Audience saturation and frequency (runbook 6 thresholds).
  5. Creative fatigue (runbook 6).
  6. Competitor offer, policy limitation, learning reset from a recent edit, and
     bid/budget changes made in the last 7 days.
- **ACT:** match the fix to the layer found. Rule: **never blame creative before
  tracking and landing-page availability are cleared.** Never make more than one
  change at a time per ad set. Seasonal CPM lifts are absorbed, not "fixed".
- **ESCALATE:** operator for stock-outs, site faults, offer or price changes, and any
  client-facing explanation. Collapse >50% for 3 days is S1.
- **PREVENT:** change log, weekly baseline per metric, stock and promo calendar from
  the client, uptime monitor on the landing page.

## 5. Pacing anomaly

- **DETECT:** daily spend vs plan beyond ±20% (investigate) or above 2x daily budget
  in a day (S1 emergency). See the canonical table above.
- **TRIAGE:** (1) Plan correct? Budget, dates, schedule and time zone as intended.
  (2) Any edit in the last 48h (budget, bid, audience, new ads, resumed campaigns)?
  (3) Delivery status: learning, limited by budget, limited by bid, rejections,
  billing, reporting lag (runbook 8).

| Cause | Under-pacing fix | Over-pacing fix |
|-------|------------------|-----------------|
| Bid/cost cap too tight | Raise cap 10-15% | Lower cap or switch to cost control |
| Audience too narrow | Widen, add placements | n/a |
| Ads rejected / few ads | Add approved variants | n/a |
| Learning limited / low volume | Consolidate ad sets | n/a |
| Billing / limit hit | Runbook 7 | n/a |
| Schedule or time-zone error | Correct dates and hours | Correct dates and hours |
| Scaling edits too large | n/a | Cut edit steps to 20-30% |
| Resumed or duplicated campaigns | n/a | Pause duplicates |
| Auto-applied recommendations | Review and revert | Review and revert |

- **ACT:** Over-pacing with CPA/ROAS at target and under 2x: let it run, note it. Above
  2x: pause the offender immediately, check for duplicated campaigns, edited budgets,
  uncapped portfolio strategies, then resume at corrected budget. Under-pacing: fix
  the cause, do not just raise budget.
- **ESCALATE:** every 2x event goes to the operator now. Possible platform credit:
  operator files a billing dispute with evidence.
- **PREVENT:** daily spend alerts at ±20% and 2x, account-level spend cap where
  available, no budget edits above 30% in one step.

## 6. Creative fatigue emergency

- **DETECT:** frequency rising, CTR decaying, CPA rising together over 5-7 days. One
  signal alone is not fatigue. Reference zones: prospecting frequency above ~3 in 7
  days; retargeting above ~8; CTR down 25%+ from the ad's own first-week level.
- **TRIAGE:** (1) Tracking and landing page clear (runbook 4). (2) Audience size vs
  budget: saturation looks like fatigue. (3) Which ads carry the spend: one ad hogging
  80% of budget is the usual case.
- **ACT:** launch the pre-built replacement batch (new hooks and formats, not recolours),
  keep the fatigued ad live at a reduced share until the new ones have data, widen or
  rotate audiences, exclude recent converters and high-frequency users. Do not kill all
  incumbents at once.
- **ESCALATE:** operator if no fresh creative exists; the client for new assets or
  shoot approval.
- **PREVENT:** creative pipeline of 3-5 new concepts per cycle, fatigue dashboard, ads
  refreshed before frequency crosses the zone.

## 7. Billing / payment failure

- **DETECT:** payment declined notice, "billing issue" status, delivery stopped,
  prepaid balance at zero, tax-information or threshold block, spend limit reached.
- **TRIAGE:** (1) Exact billing message and which account/payment profile. (2) Prepaid
  balance or credit line vs current daily spend. (3) Pending verification (tax ID,
  business address, 3-D Secure, bank block).
- **ACT:** **The agent never enters or handles payment details.** Escalate immediately
  with the exact error text and the remaining runway. Meanwhile: leave campaigns
  as they are if delivery is merely at risk; do not duplicate to other accounts or
  switch billing; do not raise budgets. Failed-billing pauses are automatic, so note
  exact pause time for the log. After the fix, re-check that campaigns resumed and
  were not left paused, and that learning was not reset.
- **ESCALATE:** operator and client billing owner now (S1), with a top-up amount
  and date needed; tax-info forms need the account owner.
- **PREVENT:** balance alert at 5 days of runway, backup payment method owned by the
  client, calendar of card expiry, monthly invoicing where eligible.

## 8. Platform outage or reporting delay

- **DETECT:** spend or conversions look low or zero across ALL campaigns, UI errors,
  API timeouts, dashboards stale, other advertisers report the same.
- **TRIAGE:** (1) Platform status pages (Meta Business status, Google Ads status
  dashboard, TikTok and YouTube status channels) and official support accounts.
  (2) Same symptom across every campaign and every account? Platform side. One
  campaign only? Your side. (3) Compare against backend orders and platform spend in
  billing, which updates independently of reports.
- **ACT:** **Do not react to delayed data.** Conversion lag of 24-72h is normal, more
  for longer attribution windows and offline conversions. No pauses, no bid or budget
  edits on a same-day dip. Wait for the platform to confirm recovery, then re-read the
  affected window after 48h before judging.
- **ESCALATE:** only if the outage lasts beyond 24h, or billing and delivery are both
  affected.
- **PREVENT:** judge on 3-7 day windows, backend reconciliation, annotate outage dates.

## 9. Client asks to cut or pause budget mid-flight

- **DETECT:** client message requesting a pause, a cut, or "stop until next month".
- **TRIAGE:** (1) Reason: cash flow, stock, poor results, internal doubt. (2) Where
  campaigns sit: in learning, recently scaled, or stable. (3) Contract and committed
  spend (flights, reservations, prepaid).
- **ACT (the honest conversation):** stop-start has a cost. Pausing for more than a
  few days usually sends ad sets back into learning, with higher CPAs for roughly a
  week after restart. Offer options in order of least damage: (a) reduce, not stop:
  cut 20-30% per step so delivery stays stable; (b) concentrate: keep the top 1-2 ad
  sets and pause the rest; (c) pause only specific campaigns such as prospecting and
  keep retargeting; (d) full pause with a defined restart date. Quote the expected
  cost of each option in plain numbers.
  - To pause without destroying learning: do not edit audiences, creatives or
    optimisation settings during the pause; do not delete; keep conversion tracking
    live; on restart return at 50-70% of prior budget and step up 20-30% every 2-3 days.
  - If the reason is poor results, do the diagnosis first (runbook 4) and report it.
- **ESCALATE:** operator for any contract, refund or commitment question.
- **PREVENT:** agree a pause policy and notice period in the scope, show learning-cost
  note in onboarding, monthly forecast sent before the client has to ask.

## 10. Compromised access / unexpected changes in the account

- **DETECT:** edits nobody on the team made, new admin or user, new payment method,
  changed pixel or conversion action, budget raised, unknown campaigns, login alerts.
- **TRIAGE:** (1) Open change history and activity log first; list who, what, when,
  from where. (2) Check users and roles, partner access, connected apps, API tokens.
  (3) Check spend since the change versus plan (runbook 5).
- **ACT:** screenshot and export the change history before touching anything. Pause
  affected campaigns if spend or content is not the team's. Do not remove users or
  rotate tokens yourself: report exactly which ones look wrong. Revert bad edits only
  after the operator confirms who is legitimate (a client, agency partner or rep
  often made the edit).
- **ESCALATE:** operator at once (S1). The operator handles credentials, 2FA reset,
  removing users, platform security report, and informing the client.
- **PREVENT:** least-privilege roles, 2FA on every user, quarterly access review,
  alerts on user or payment changes, client edits routed through a change request.

## Incident log format

Keep one entry per incident in the client's log. Append only; never rewrite history.

| Field | Content |
|-------|---------|
| Date/time | When detected (with time zone), when resolved |
| Severity | S1 / S2 / S3 |
| Detection | Signal and who or what noticed it |
| Root cause | Confirmed cause, or "unconfirmed" plus the leading hypothesis |
| Action | What was done, in order, with timestamps; what was paused or frozen |
| Impact | Spend wasted or lost, conversions lost, days affected (real numbers only) |
| Prevention | The control added, owner, due date |
