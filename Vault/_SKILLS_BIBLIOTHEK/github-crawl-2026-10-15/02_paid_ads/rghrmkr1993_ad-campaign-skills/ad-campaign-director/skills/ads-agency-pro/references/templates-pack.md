# Templates Pack: Fill-in-the-Blank Working Documents

Use verbatim. Replace every {{placeholder}}. Never leave one unfilled: write
`ASSUMED: {{value}}` or `UNKNOWN` instead. Generic across Meta, Google, YouTube,
TikTok, any industry, any region.

## 1. Client intake questionnaire

Send once at onboarding. Missing answers become stated assumptions in the client
playbook (template 6), logged as `ASSUMED: ...`. They are never blockers. Only block
on: no access to the ad account, no conversion event, no budget.

```
BUSINESS
1. What do you sell, in one sentence? {{answer}}
2. Average order value or average deal value: {{currency}} {{amount}}
3. Gross margin (or contribution margin) per sale: {{percent}}
4. Best-selling product or service, and why people buy it: {{answer}}
5. Repeat purchase rate or customer lifetime value, if known: {{answer}}

GOAL
6. The ONE event that matters (purchase / qualified lead / booking / app install /
   ticket sale): {{event}}
7. Target CPA or ROAS, and how you derived it: {{target}}
8. Monthly ad budget (and whether it can move): {{currency}} {{amount}}
9. Time horizon (launch date, campaign end, or ongoing): {{dates}}

MARKET
10. Geographies to target, and any to exclude: {{geos}}
11. Languages of ads and landing pages: {{languages}}
12. Seasonality: peak months, slow months, fixed events: {{answer}}

ASSETS
13. Website / landing page URLs: {{urls}}
14. Product catalog or feed (where it lives, who maintains it): {{answer}}
15. Creative library (photos, video, UGC, testimonials) and usage rights: {{answer}}
16. Brand guidelines (logo, colors, fonts, tone, do and don't): {{answer}}
17. Existing ad accounts, pages, pixels, tag manager, analytics: {{list}}

MEASUREMENT
18. Current tracking (pixel, conversions API, tags, offline imports): {{answer}}
19. CRM or order system, and who can export it weekly: {{answer}}
20. What counts as a QUALIFIED lead (written definition, with disqualifiers): {{answer}}

CONSTRAINTS
21. Claims you cannot make (legal, regulatory, brand): {{answer}}
22. Competitors you will not be compared to or named near: {{answer}}
23. Blackout dates (stock-outs, sales freezes, PR events, holidays): {{answer}}
24. Approver for creative and for spend, and their turnaround time: {{name, hours}}
```

## 2. Creative brief (one per concept)

```
CONCEPT NAME: {{short_name}}          BRIEF ID: {{client}}-{{yyyymm}}-{{nn}}
ANGLE: {{problem | desire | proof | identity | comparison | curiosity | other}}
AUDIENCE: {{who}}     AWARENESS STAGE: {{unaware | problem | solution | product | most}}
HOOK (first 2 seconds, written out, visual + spoken/on-screen text):
  {{exact_hook}}
KEY MESSAGE (one sentence): {{message}}
PROOF ELEMENT: {{review | demo | data we hold on file | expert | guarantee terms}}
OFFER: {{offer_and_terms}}                CTA: {{cta_button_and_line}}
FORMAT + RATIOS: {{video | static | carousel}}; {{9:16, 4:5, 1:1, 16:9}}; {{length}}
MANDATORIES: logo {{placement}}; legal line {{text}}; disclosure {{text_or_none}}
BANNED CLAIMS (this vertical): {{list, from client constraints + template 7}}
REFERENCES: {{links_or_descriptions, what to borrow and what to avoid}}
DELIVERABLES: {{n}} hook variants x {{n}} bodies; {{n}} headlines; {{n}} primary texts;
  {{n}} cutdowns; due {{date}}
SUCCESS METRIC: {{metric}} vs {{benchmark}}   LINKED TEST: {{test_id_from_template_5}}
```

## 3. Launch approval diff

Present this exact block to the human before ANY spend. No approval, no launch.

```
LAUNCH APPROVAL: {{client}} / {{campaign_name}}
WHAT GOES LIVE: {{one_line_summary}}
STRUCTURE:
  {{platform}} account {{account_label}}
   +- Campaign: {{name}} ({{objective}})
       +- Ad set / ad group: {{name}} ({{audience_or_keyword_theme}})
           +- Ads: {{n}} ({{creative_ids}})
BUDGET: {{currency}} {{daily}} per day; total cap {{currency}} {{total}}
FLIGHT: {{start_date}} to {{end_date_or_ongoing}} ({{timezone}})
GEO / LANGUAGE: {{geos}} / {{languages}}
OPTIMIZATION EVENT: {{event}}      BID STRATEGY: {{strategy}}, target {{value_or_none}}
CREATIVE COUNT: {{n}} ads across {{n}} concepts; all passed template 7: {{yes|no}}
TRACKING VERIFIED: {{PASS | FAIL}}
  event fires on test {{yes|no}}; value and currency correct {{yes|no}};
  deduplication OK {{yes|no}}; consent handling OK {{yes|no}}
NOT INCLUDED: {{retargeting, other geos, other platforms, catalog, etc.}}
KNOWN RISKS / ASSUMPTIONS: {{list}}
APPROVAL QUESTION: Approve launching the above, spending up to {{currency}} {{total}}
  by {{end_date}}? Reply YES to launch, or name the line to change.
ROLLBACK (one step): pause campaign "{{name}}" in {{platform}}; nothing is deleted.
  Spend stops within {{minutes}} of the pause. Previous state: {{prior_state_or_none}}.
```

If TRACKING VERIFIED is FAIL, do not present for approval; fix first.

## 4. Weekly client report (5 parts)

Rule: chart titles state findings ("Cost per lead fell as video replaced static"), never
metric names ("CPL by week"). One idea per chart. Plain words, no jargon unexplained.

```
1. EXECUTIVE SUMMARY (readable in 90 seconds, max 5 sentences)
   Result vs goal: {{on_track | ahead | behind}}. Headline: {{one_sentence}}.
   Biggest win: {{win}}. Biggest risk: {{risk}}. Decision needed from you: {{ask_or_none}}.

2. KPI SCORECARD ({{week_range}})
   | KPI | Target | Actual | Delta | Status |
   |-----|--------|--------|-------|--------|
   | Spend | {{t}} | {{a}} | {{d}} | {{on plan / watch / off}} |
   | {{goal_event}} volume | {{t}} | {{a}} | {{d}} | {{status}} |
   | CPA or ROAS | {{t}} | {{a}} | {{d}} | {{status}} |
   | Business revenue (CRM/order system) | {{t}} | {{a}} | {{d}} | {{status}} |

3. WHAT DROVE THE CHANGE (cause and effect)
   Because {{cause}}, {{metric}} moved {{direction}} {{amount}}. Evidence: {{evidence}}.
   Not caused by: {{ruled_out_factor}}.

4. WHAT WE DID + WHAT WE LEARNED
   Did: {{change_with_date}} (log id {{id}}).
   Learned: {{finding}}. Confidence: {{low | medium | high}} because {{sample_note}}.

5. NEXT WEEK
   | Date | Action | Owner | Expected effect |
   |------|--------|-------|-----------------|
   | {{date}} | {{action}} | {{agent|client}} | {{effect}} |
   Needed from client by {{date}}: {{assets_or_approvals}}
```

## 5. Test plan / hypothesis log

One row per test. Success criterion is written BEFORE launch and never edited after.

```
TEST ID: {{client}}-T{{nn}}
HYPOTHESIS: If we {{change}}, then {{metric}} improves because {{reason}}.
VARIABLE (exactly one): {{variable}}      CONTROL: {{control}}   VARIANT: {{variant}}
HELD CONSTANT: {{budget, audience, placement, schedule, landing page}}
SUCCESS CRITERION (set before test): {{metric}} {{better_by_amount}} at {{confidence_rule}}
MIN DURATION: {{days}} (covers {{full weekly cycle}})   MIN SAMPLE: {{events_per_arm}}
ABANDON IF: {{spend cap reached with no signal | tracking breaks | policy flag | ...}}
START: {{date}}   END: {{date}}
RESULT: {{numbers_per_arm, with sample sizes}}
DECISION: {{adopt | reject | retest}}   REASON: {{one_line}}
DECISION DATE: {{date}}   FOLLOW-UP: {{next_test_id_or_none}}
```

## 6. Client playbook file

Per-client memory. Read at session start, rewritten at session end, updated after
every optimization cycle. Suggested path: `clients/{{client_slug}}/playbook.md`
(keep secrets, passwords and payment data out of it, always).

```
# Playbook: {{client_name}}      Last updated: {{date}} by {{agent_or_human}}

## Account registry
| Platform | Account/ID label | Role (own/manager) | Pixel/tag | Billing owner |
|----------|------------------|--------------------|-----------|---------------|

## Economics
AOV {{x}} | Gross margin {{x}} | Target CPA/ROAS {{x}} | Break-even CPA {{x}} | LTV {{x}}
Source and date of each number: {{source}}

## Winning angles (what, where, evidence, date)
- {{angle}}: {{result_and_sample}}

## Dead angles (what, why it failed)
- {{angle}}: {{why}}. Do not retry unless {{condition}}.

## Audience notes
- {{audience}}: {{behaviour_learned}}

## Seasonality observed
- {{period}}: {{effect_on_cost_or_volume}}

## Compliance constraints
- {{claim_or_rule}} (source: {{client_or_regulation}})

## Open experiments
| Test ID | Hypothesis | Start | Status |
|---------|-----------|-------|--------|

## Decision log (newest first)
- {{date}} | {{decision}} | {{reason}} | {{who_approved}} | {{outcome_when_known}}

## Assumptions still unconfirmed (from intake)
- ASSUMED: {{item}}
```

## 7. Pre-upload compliance checklist

Generic gate for every ad, every vertical. Regulated verticals (health, finance,
alcohol, gambling, housing, employment, politics, minors, supplements and others) add
their own rules on top; load the vertical playbook and check local law before upload.

```
AD ID: {{id}}   MARKET(S): {{geos}}   VERTICAL: {{vertical}}   CHECKED BY/DATE: {{x}}
[ ] Every factual claim has substantiation on file ({{location}})
[ ] No absolute or guaranteed-outcome language ("guaranteed", "cure", "100%", "never")
[ ] No before/after imagery where the platform or law restricts it
[ ] No implied knowledge of personal attributes ("Are you struggling with your ...")
[ ] Paid partnership / sponsored label set where creators are paid
[ ] AI-generated or synthetic content disclosed where platform or law requires
[ ] Testimonials are real, current, and typical or carry the required disclaimer
[ ] Landing page matches the ad promise (product, price, offer, claim)
[ ] Price, discount and offer terms are accurate, live, and have an end date if timed
[ ] Required legal lines present (terms, disclaimers, license or registration no.)
[ ] Age and geo restrictions applied in targeting and in the creative
[ ] No competitor trademark misuse; comparisons are factual and provable
[ ] No third-party IP (music, footage, fonts, faces) without a license
[ ] Text in creative is readable: contrast, size, safe zones, captions on video
[ ] Destination loads fast, works on mobile, has privacy policy and contact details
RESULT: PASS (all checked) | HOLD (items open: {{list}})   Any HOLD blocks upload.
```

## 8. Inherited account audit checklist

For an account you did not build. Score each section PASS (2), PARTIAL (1), FAIL (0).
Record evidence (screenshot id or export row) for every score.

```
AUDIT: {{client}} / {{platform}} / {{date}}   Auditor: {{x}}
| # | Section | What to check | Score | Evidence |
|---|---------|---------------|-------|----------|
| 1 | Tracking integrity | event fires, value/currency right, dedup, consent, |  |  |
|   |                    | conversion actions match the real goal            |  |  |
| 2 | Account structure | clear naming, no overlap, sensible consolidation   |  |  |
| 3 | Budget + bidding | pacing sane, bid targets realistic, learning state  |  |  |
| 4 | Audience hygiene | exclusions (customers, employees), list freshness,  |  |  |
|   |                  | overlap, geo and language settings                  |  |  |
| 5 | Creative inventory | ads per group, formats, fatigue signals, ratios   |  |  |
| 6 | Feed health (ecom) | disapprovals, price/stock sync, titles, GTIN       |  |  |
| 7 | Policy status | disapprovals, warnings, restricted flags, history     |  |  |
| 8 | Wasted spend | search terms, placements, geos, devices, dayparts     |  |  |
| 9 | Measurement truth | platform vs analytics vs business revenue, gap     |  |  |
|   |                   | stated in percent with the likely causes           |  |  |
SCORE: {{sum}} / {{2 x sections_applicable}}
```

Triggers per FAIL:
- Section 1 or 9 FAIL: freeze optimization and scale decisions until fixed. Fix first.
- Section 7 FAIL: tell the operator now; do not launch new ads into a flagged account.
- Section 3 FAIL with live overspend: apply the pacing rules in runbooks-incidents.md.
- Any other FAIL: schedule the fix in the first two weeks; log it in the playbook.
- PARTIAL: fix within the first optimization cycle if cheap, otherwise log it.

```
QUICK WINS (ranked by impact on spend efficiency, then by effort)
| Rank | Fix | Section | Effort (S/M/L) | Expected effect | Needs approval? |
|------|-----|---------|----------------|-----------------|-----------------|
| 1 | {{fix}} | {{#}} | {{x}} | {{effect}} | {{yes|no}} |
```
