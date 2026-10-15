---
name: ads-agency-pro
description: Advanced paid-media agency playbook for running client ad campaigns on Meta (Facebook/Instagram), Google, YouTube, and TikTok, for ANY industry in ANY region of the world. Use for ANY client campaign work: strategy, media planning, audits, campaign builds, budgets, creative strategy, benchmarks, geo/vertical questions, or platform best practices. Contains 2026 platform doctrine (Meta Andromeda, Google Power Pack, TikTok Smart+/GMV Max), a build-any-market geo framework with regional guides for every world region, a build-any-industry vertical framework with 12+ industry guides, and a client dashboard/reporting spec.
---

# Ads Agency Pro: 2026 Client Campaign Playbook

Agency operating system for running paid media for clients, **any region, any industry**.
This skill is the **strategy + regional + vertical layer**. It pairs well with:

- **`ads` skill ([claude-ads plugin](https://github.com/AgriciDaniel/claude-ads))**: optional
  but recommended: structured audits, deterministic scoring, JSON reports, capability-gated
  account changes. Use it for the mechanics; use THIS skill for what to do in your markets
  and verticals.
- **Meta Ads MCP tools** (`ads_*`) if connected, direct API access to campaigns, ad sets,
  creatives, audiences, insights, A/B and lift tests.
- **Browser automation**: Google Ads, YouTube Studio, GA4, TikTok Ads Manager.
- **Your creative stack**: AI video/UGC generation, Canva or equivalent, copywriting
  skills, landing-page skills.

## How the layers fit

```
Client brief (who, budget, where, what business)
        │
        ▼
┌─ ads-agency-pro (this skill) ──────────────────────────────┐
│  1. Core doctrine, platform-agnostic 2026 rules    │
│  2. Platform playbooks, Meta / Google / YouTube / TikTok│
│  3. Geo framework, build a playbook for ANY market │
│  4. Vertical framework, build one for ANY industry      │
│  5. Dashboard spec, client reporting that retains   │
└────────────────────────────────────────────────────────────┘
        │
        ▼
Execution: platform APIs/MCP + browser + creative tooling
```

## Account registry (maintain your own, TEMPLATE)

Keep this table updated with YOUR accounts. Verify the right account before every action.

| Platform | Account | Login | Notes |
|---|---|---|---|
| Google Ads | `XXX-XXX-XXXX` | `your-ads-login@example.com` | Billing model, tax status |
| Meta | Business Manager + ad account per client | | Never run client work on a personal ad account. Pixel + CAPI per client. |
| TikTok | Per-client | | Check availability per geo (e.g., **banned in India**). |

## 2026 core doctrine (applies to every campaign, everywhere)

1. **Creative is the targeting.** Meta Andromeda and TikTok Smart+ retrieve ads by creative
   signal, not audience settings. Budget creative volume before budgeting media: 10-15
   conceptually distinct concepts per campaign, 20+ new ads/month for active accounts.
2. **Concepts, not variations.** Similar ads collapse into one Entity ID on Meta, 30 lookalike
   ads = 1 ad to the algorithm. Diversify angle, emotion, format, and creator, not just colors.
3. **Consolidate structure.** 1-3 ad sets per campaign max. Advantage+ Shopping / PMax as
   workhorses. Fragmented structures starve the learning phase.
4. **Broad beats narrow.** Lookalikes and interest stacks are legacy. Go broad + let creative
   segment. Exceptions: genuine niche B2B and fan-base entertainment marketing.
5. **Signal quality is the moat.** Pixel + CAPI together, Event Match Quality ≥ 7, GA4 +
   enhanced conversions on Google, offline conversion import for lead-gen. No launch without
   conversion tracking verified end-to-end.
6. **Video-first everywhere.** 9:16 native vertical for Reels/Shorts/TikTok. Hook < 2s,
   brand < 3s, text overlays for sound-off. UGC-style outperforms studio polish (24% higher
   ROAS, ~47% lower CPM on Meta).
7. **Patience windows.** Let algorithms learn 7-10 days before judging. Expect ad fatigue at
   2-3 weeks, plan refresh cadence (25-30% of assets every 2 weeks at scale).

## Platform quick sheet

| Platform | 2026 play | Detail |
|---|---|---|
| Meta | Andromeda/GEM era: Advantage+ Sales (formerly A+SC) primary, creative volume, EMQ ≥ 7 | [references/platforms-2026.md](references/platforms-2026.md) |
| Google | Power Pack: PMax + AI Max Search + Demand Gen. Splits are [E] starting heuristics, not Google guidance: replace with the account's own marginal-return data | same |
| YouTube | Shorts ≥ 20-30% of YT spend for <35 audiences; CTV for premium brand | same |
| TikTok | Smart+ for web, GMV Max default for TikTok Shop; check per-geo availability | same |

## Geo coverage, any market

[references/geo-playbooks.md](references/geo-playbooks.md) contains:
- **The 7-question Geo Framework**: build a playbook for any market: platform availability
  & bans, language map, payment/commerce mechanics, seasonal calendar, privacy/compliance,
  CPM tier, creator ecosystem.
- **Regional quick guides**: North America, Latin America, Europe, Middle East & GCC,
  Africa, South Asia, Southeast Asia, East Asia, Oceania.
- **Six worked examples at full depth**: India/South India, Sri Lanka, Malaysia, Singapore,
  US, UK, templates for the depth every active market deserves.

## Vertical coverage, any industry

[references/vertical-playbooks.md](references/vertical-playbooks.md) contains:
- **The 6-question Vertical Framework**: regulatory/claims status, purchase cycle & unit
  economics, creative codes, benchmark bands, measurement model, seasonality.
- **12 industry quick guides**: F&B, health & wellness, finance, real estate, education,
  travel, automotive, gaming/apps, B2B/SaaS, local services, luxury/jewelry, electronics.
- **Four worked examples at full depth**: skincare/beauty (compliance-heavy), fashion
  (benchmark-driven), film/entertainment (phase-gated), tech (B2B + consumer).

## Knowledge layers (the AI-marketing-agent brain)

| Layer | Contents | File |
|---|---|---|
| Foundations | 28 marketing disciplines map, journey models (AIDA/TOFU/Flywheel/AARRR/RACE/See-Think-Do-Care), objective-selection matrix | [references/marketing-foundations.md](references/marketing-foundations.md) |
| Creative & psychology | 10-point creative scoring rubric, 12 copywriting frameworks, Cialdini + cognitive-bias application with ethical lines | [references/creative-psychology.md](references/creative-psychology.md) |
| Platform AI internals | Meta Andromeda+GEM auction math, Google Ad Rank/Smart Bidding signals, steering doctrine, 8 secondary platforms (Microsoft/LinkedIn/Pinterest/Snap/Reddit/Amazon/X/TikTok) | [references/platform-ai-internals.md](references/platform-ai-internals.md) |
| Measurement science | Metric definitions, 9 attribution models incl. Markov/Shapley/incrementality, experiment designs (geo, lift, holdouts), forecasting/MMM honesty | [references/measurement-science.md](references/measurement-science.md) |
| Optimization & automation | Budget portfolio logic, bidding selection tree, creative bandit rotation, scale/kill thresholds, lifecycle automation, ecommerce intelligence | [references/optimization-automation.md](references/optimization-automation.md) |
| Strategy frameworks (v2.2) | GTM 5-step, ABM tiers (1:1/1:few/1:many), PLG + growth loops, business-model mechanics, customer intelligence (personas/RFM/cohorts/health scores/VoC) | [references/strategy-frameworks.md](references/strategy-frameworks.md) |
| Enterprise MarTech (v2.2) | Stack blueprint by client size (CDP/CRM/consent/identity), event-tracking architecture, programmatic (DSP/RTB/PMP/CTV), retail media, CRO deep-dive | [references/enterprise-martech.md](references/enterprise-martech.md) |
| Operations (v2.3) | Day 0 access checklist, Day 0-14 launch sequence, budget-sizing math (learning floor, break-even ROAS, CPA ceiling), small-budget regime, pre-launch QA gate, 4-level naming + UTM schema, steady-state cadence | [references/operations-playbook.md](references/operations-playbook.md) |
| Incident runbooks (v2.3) | 10 runbooks in detect/triage/act/escalate/prevent form (account disabled, policy rejection, tracking break, CPA spike, pacing, fatigue, billing, outage, budget cut, unexpected account changes), severity scale, canonical pacing thresholds | [references/runbooks-incidents.md](references/runbooks-incidents.md) |
| Templates (v2.3) | Fill-in blocks: client intake, creative brief, launch-approval diff, weekly report, test plan, per-client playbook schema, pre-upload compliance checklist, inherited-account audit | [references/templates-pack.md](references/templates-pack.md) |

## Standard engagement workflow (new client)

1. **Intake**: business goal, AOV/LTV, margins, target ROAS/CPA ceiling, geo list, languages,
   existing assets/accounts. Get Business Manager / Google Ads access via proper partner
   delegation (never passwords).
2. **Audit**: invoke the `ads` skill for a source-grounded audit if account has history;
   otherwise baseline: tracking, feeds, past creative, competitor scan (Meta Ads Library;
   Google Ads Transparency Center).
3. **Measurement first**: pixel + CAPI (Meta), Google tag + enhanced conversions, GA4,
   catalog/feed health. Verify test events BEFORE any spend.
4. **Structure**: per doctrine above. One prospecting (broad) + one retargeting + optional
   test campaign per platform. Name convention: `{CLIENT}-{GEO}-{OBJ}-{YYYYMM}`.
5. **Creative sprint**: 10-15 concepts across angles (problem, desire, social proof, founder,
   demo, UGC, meme where fit). Localize per language market, separate ad sets per language,
   never mixed.
6. **Launch small, scale on signal**: 7-10 day learning window, then scale winners 20-30%
   per step; kill losers at concept level, not variation level.
7. **Report**: weekly: spend, ROAS/CPA vs target, creative leaderboard, next tests.
8. **Client dashboard**: daily results dashboard per
   [references/client-dashboard-spec.md](references/client-dashboard-spec.md).

## Guardrails

- Never launch, edit budgets, or change live campaigns without explicit owner approval.
- Verify platform availability per geo before planning (bans/restrictions move).
- Seasonal peaks inflate CPMs (up to 2-3x at the biggest events), book creative and lock
  budgets 4-6 weeks ahead; never start a learning phase inside a peak.
- Every regulated-vertical ad (health claims, finance, housing, etc.) passes the compliance
  checks in [references/vertical-playbooks.md](references/vertical-playbooks.md) before
  submission.
- Check the billing model (prepaid vs postpaid, tax registration) per account/market before
  launch week.
