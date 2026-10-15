# Operations Playbook: From Signed Client to Steady State

The other references say what good looks like. This one says what to do on which day, in
which order, and where a human must say yes. Nothing launches before measurement works.

## 1. Access checklist (Day 0)

Ask for partner/delegated access, never personal logins, never passwords. Verify each item
yourself (open it, read a number from it) before ticking it.

| Asset | Request | Verify | What breaks later if missing |
|---|---|---|---|
| Meta Business Manager | Partner access via Business Settings > Partners (client adds your BM ID) | You see the ad account, Page, pixel in your own BM | No ad account control; client's personal profile becomes a single point of failure |
| Facebook Page | Partner access with ads/content tasks | Page appears under your assets | Cannot run Page-based ads, no comment moderation, no lead-form ownership |
| Pixel / dataset | Assign to ad account, admin on dataset | Events Manager shows live events | No optimization signal, no retargeting pool, no CAPI setup |
| Catalog | Assign catalog + feed source | Products and no feed errors visible | No dynamic/Advantage+ catalog ads, no product retargeting |
| Instagram account | Connect to BM, grant ad permissions | Account selectable as ad identity | Ads forced to Page identity, lower trust, no IG-native placements control |
| Google Ads | Manager (MCC) link invite from client account | Link status "Active" in your MCC | No access at all; shared logins get suspended |
| GA4 | Editor on property | Realtime report shows traffic | Cannot create or mark conversions, no cross-channel truth |
| Google Tag Manager | Publish access to container | Preview mode connects to the site | Every tracking change waits on the client; no consent logic |
| Merchant Center | Standard/admin access, feed linked to Ads | Products approved, link to Ads active | No Shopping or PMax feed; disapprovals unfixable |
| Search Console | Full user | Property verified, data present | No query data for search strategy, no indexing diagnosis |
| Domain verification | DNS TXT or registrar access (or dev contact) | Domain shows verified in Meta BM | Link/domain ownership blocks, event prioritization limits |
| TikTok Business Center (if used) | Partner or admin on ad account, pixel, catalog | Pixel Helper shows events | No TikTok launch; verify the platform is permitted in the client's market first |
| Website / CMS | Editor login via role-based user, or a named developer contact with SLA | Test page edit or dev reply within 1 day | Tags, UTMs, landing-page fixes and consent banners stall |
| Billing | Client-owned payment method is the default; you never hold card or UPI mandates | Funds or credit limit visible, tax details valid | Mid-flight ad rejections for billing, disputed spend, ownership fights at offboarding |

Rule: if the client insists you own billing, document it in writing (invoicing, markup,
who is liable for platform debt) and flag it to the Manager before accepting.

## 2. Day 0 to Day 14 sequence

| Day | Phase | Outputs | Exit condition |
|---|---|---|---|
| 0-1 | Access + baseline snapshot | Section 1 table complete. Export last 90 days of performance (spend, CPM, CTR, CPA, ROAS, revenue by channel), existing audiences, active campaigns, current tracking state, site conversion rate | Baseline file saved with date. Without it you cannot prove impact later |
| 1-3 | Measurement build + verify | Events, CAPI/server events, GA4 conversions, consent mode, UTM scheme (section 6), conversion actions set primary vs secondary | Test events verified in each platform and matched to a real test order or lead |
| 3-5 | Research + strategy brief | Goal, target CPA/ROAS (section 3), audience hypotheses, competitor scan (ad libraries), offer analysis, creative concept matrix | Brief states budget tier (section 4) and the single success metric |
| 5-9 | Creative + campaign build | Assets per concept and format, copy variants, campaigns built PAUSED with naming applied | Everything exists in the platforms, nothing is spending |
| 9-10 | Pre-launch QA gate + approval | Section 5 checklist passed, summary sent to client | **HUMAN APPROVAL GATE** (client sign-off on budget, creative, landing page; Manager review of QA) |
| 10 | Launch | Unpause in one sitting, screenshot every campaign state, log launch time | First impressions and event firing confirmed within hours |
| 10-17 | Learning phase | Incident response only: disapprovals, tracking breaks, billing failures, runaway spend | No edits to budgets, audiences, bids or creative unless an incident requires it |
| 17+ | First optimization cycle | Read results against baseline, first weekly report, next experiment queued | Report delivered, decisions logged |

Approval gate: nobody unpauses, raises budget, or changes billing without explicit human
yes. The agent prepares the request, never self-approves. Add a second gate at any budget
increase above 20% of the approved amount.

Why hands off in the learning phase: every significant edit (budget move over roughly
20%, audience, bid strategy, optimization event) can reset learning. Edit only for
incidents, and log them.

## 3. Budget sizing math

All figures below are arithmetic from stated inputs, not predictions of results.

| Quantity | Formula | Worked example |
|---|---|---|
| Learning-volume floor per ad set | ~50 optimization events per week (platform learning requirement, verify current figure in the platform's help) | 50 events/week |
| Minimum weekly budget per ad set | Target CPA x 50 | 20 x 50 = 1,000 |
| Minimum daily budget per ad set | (Target CPA x 50) / 7 | (20 x 50) / 7 = 142.86 per day |
| Minimum monthly per ad set | Daily minimum x 30.4 | 142.86 x 30.4 = 4,343 |
| Break-even ROAS | 1 / gross margin | 40% margin: 1 / 0.40 = 2.5x |
| Profit-target ROAS | 1 / (gross margin - target profit share of revenue) | 40% margin, 10% profit: 1 / 0.30 = 3.33x |
| First-order break-even CPA | AOV x gross margin | AOV 50 x 0.40 = 20 |
| LTV-based CPA ceiling | Margin-adjusted LTV / desired LTV:CAC (usually 3) | 90 / 3 = 30 |
| Payback-capped CPA | Contribution margin earned inside the payback window | 90-day margin per customer 36, so ceiling 36 |

Reading the table:
- A platform ROAS of 2.5x on a 40% margin business is break-even before fixed costs, so
  any profit target must sit above it.
- Take the lower of the LTV ceiling and the payback-capped ceiling (here 30). A high LTV
  does not help a client who cannot fund 12 months of cash burn. State the payback window
  to the client in writing.
- LTV figures must come from the client's real cohorts. If none exist, use first-order
  break-even CPA and say LTV is unknown. Never invent an LTV.
- Check the floor against reality: if the real CPA is 2x the target, the real event
  volume is half the learning requirement at the same spend.

## 4. Small-budget regime

The 10-15 concept, 20+ ads per month cadence in the other references assumes budget that
funds the learning floor on several ad sets. Size the tier by how many ad sets the money
can support: monthly budget / (target CPA x 50 x 4.33).

| Tier | Ad sets fundable | Structure | Concepts | Ads/month |
|---|---|---|---|---|
| Micro (below one floor) | Under 1 | One platform, one campaign, one ad set, broad targeting | 3-5 | 5-8 |
| Small | 1-2 | One platform (second only if first is stable), 1-2 campaigns | 5-8 | 8-12 |
| Mid | 3-6 | Two or three platforms, separate prospecting and retargeting, a testing campaign | 10-15 | 20+ |
| Large | 7+ | Full-funnel on 3-4 platforms, dedicated always-on test budget (10-20%), incrementality holdouts | 15+ | 30+ |

Honest rule: below the learning-volume floor, the platform's AI cannot optimize. It is
guessing on noise. Pick one, in this order:

1. Consolidate to one ad set and one event so all volume feeds one learning pool.
2. Move up the funnel: optimize for a mid-funnel event with enough volume (add to cart,
   initiate checkout, qualified lead, landing page view as last resort) and confirm the
   event correlates with real sales before trusting it.
3. Tell the client the budget is too thin for the stated goal. Offer: a lower-funnel
   goal at a higher budget, or an upper-funnel goal at today's budget. Put it in writing.

Micro-tier hygiene: no audience splitting, no per-ad budget fragmentation, judge on
two-week windows, and report event counts next to every efficiency number so the client
sees the sample size.

## 5. Pre-launch QA gate (hard checklist)

Every box must be ticked by someone other than the builder. One failure blocks launch.

Tracking
- [ ] Every conversion event fires once on the correct action (test order or lead made)
- [ ] Browser plus server events deduplicated (shared event ID, match rate checked)
- [ ] Consent mode or banner logic behaves correctly for the client's regions
- [ ] Test event verified in each platform's diagnostics, no duplicate or missing params

Structure
- [ ] Naming follows section 6 at all four levels
- [ ] Budgets, bid strategy, start and end dates, schedules match the approved brief
- [ ] Geo and language match the offer and the creative language
- [ ] Placements intentional (not blindly all, not blindly Advantage+ for a regulated vertical)

Targeting
- [ ] Customer lists and converters excluded from prospecting
- [ ] Brand safety, inventory type and exclusion lists set; Google negative keywords added
- [ ] Google location option is "Presence" (people in or regularly in the location), not
      "Presence or interest"
- [ ] Age, gender and special ad category settings correct for the vertical and region

Creative
- [ ] Policy pass: claims, before and after imagery, health and finance rules, trademarks
- [ ] Aspect ratios delivered (9:16, 4:5, 1:1, 16:9 as the placements need)
- [ ] Captions burned in or uploaded, key text inside platform safe zones
- [ ] Landing page live, mobile load under 3 seconds, and the headline and offer match the
      ad promise exactly

Billing
- [ ] Account funded or credit line confirmed for at least the learning phase
- [ ] Tax and business details valid for the billing country

Measurement
- [ ] UTMs on every destination URL, tested by clicking each ad preview
- [ ] Primary conversion actions set correctly (one primary per goal, rest secondary)
- [ ] Attribution window stated in the report header (for example 7-day click, 1-day view)

## 6. Naming + UTM schema

Four levels, one pattern, set once and never changed mid-account. Renaming mid-flight
breaks historical joins and makes baseline comparisons worthless.

| Level | Pattern | Example |
|---|---|---|
| Campaign | `platform_objective_funnel_geo_yyyymm` | `meta_sales_prosp_in_202610` |
| Ad set / group | `audience_placement_optevent` | `broad-25-44_auto_purchase` |
| Ad | `concept_angle_format_version` | `c03_proof_ugc-9x16_v2` |
| Creative asset | `concept_format_hook_version` | `c03_9x16_hookA_v2` |

Rules: lowercase, hyphen inside a token, underscore between tokens, no spaces, a
concept ID (c01, c02) that matches the concept matrix, and a naming key document kept in
the client folder.

| UTM parameter | Value rule | Example |
|---|---|---|
| utm_source | Platform | `meta` |
| utm_medium | Paid type | `paid_social` or `cpc` |
| utm_campaign | Campaign name verbatim | `meta_sales_prosp_in_202610` |
| utm_content | Ad name verbatim | `c03_proof_ugc-9x16_v2` |
| utm_term | Keyword (search) or audience (social) | `broad-25-44` |

Example URL:
`https://example.com/product?utm_source=meta&utm_medium=paid_social&utm_campaign=meta_sales_prosp_in_202610&utm_content=c03_proof_ugc-9x16_v2&utm_term=broad-25-44`

Use platform dynamic parameters only where they output the same names, otherwise static
values win. Document casing rules, because GA4 treats `Meta` and `meta` as different.

## 7. Steady-state cadence

| Cadence | Task | Detail |
|---|---|---|
| Daily (10 min) | Health check | Spend vs pacing, disapprovals and policy flags, delivery status, tracking events still firing, CPA or ROAS outside the agreed band, billing alerts, comments needing a reply |
| Daily | Incident rule | Pause only for broken tracking, policy risk or runaway spend; log every action |
| Weekly | Optimization cycle | Review creative by concept (hook rate, hold rate, CPA), shut clear losers after enough spend, queue new variants, check frequency, budget moves under 20% |
| Weekly | Report | Client-ready: spend, results vs target, blended MER, learnings, next-week actions, event counts alongside efficiency |
| Monthly | Strategy review | Goal vs plan, funnel leaks, budget reallocation across platforms and funnel stages |
| Monthly | Benchmark refresh | Update CPM, CTR, CVR benchmarks from own data and the baseline file |
| Monthly | Experiment readout | Hypothesis, result, confidence, decision (scale, kill, retest) |
| Quarterly | Full audit | Tracking, structure, audiences, creative library, billing, access list (remove stale users) |
| Quarterly | Platform-doctrine refresh | Re-read platform changes, re-verify the learning floor and policy, update this library |
