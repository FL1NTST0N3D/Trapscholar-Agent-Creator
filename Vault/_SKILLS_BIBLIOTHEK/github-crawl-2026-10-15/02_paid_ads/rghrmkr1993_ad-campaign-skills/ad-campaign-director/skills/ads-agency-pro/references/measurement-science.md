# Measurement Science: Metrics, Attribution, Experiments

If measurement lies, every optimization is noise. This layer defines the metrics, the
attribution lens, and the experiment designs the agent uses to know what's true.

## Metric definitions + health logic

| Metric | Definition | Read it as |
|---|---|---|
| CTR | Clicks/impressions | Creative-audience fit (diagnostic, not a goal) |
| CPM | Cost per 1000 impressions | Auction pressure + audience quality + negative-feedback tax |
| CPC/CPL/CPA | Cost per click/lead/acquisition | Efficiency at each funnel depth |
| CAC | Fully-loaded cost per NEW customer | The real acquisition price (includes fees/creative) |
| ROAS | Platform-attributed revenue ÷ spend | Efficiency CLAIM, verify against blended |
| Blended ROAS / MER | Total revenue ÷ total ad spend | The truth metric; platform ROAS can rise while MER falls |
| AOV | Revenue ÷ orders | Bundle/upsell lever |
| LTV | Margin-adjusted customer lifetime value | Sets the real CAC ceiling: LTV:CAC ≥ 3 healthy |
| Conversion rate | Stage-to-stage % | Locate the funnel leak before buying more traffic |
| Frequency | Impressions ÷ reach | >3-4/week prospecting = fatigue tax rising |
| Quality/relevance scores | Platform ad-quality diagnostics | Below-average = creative or LP problem, fix before scaling |
| Retention / repeat rate | Cohort repurchase % | The compounding engine; report by cohort, not aggregate |

Guardrail: pick ONE north-star efficiency metric per client (usually MER or CAC-payback),
2-3 supporting diagnostics. A dashboard with 20 co-equal metrics decides nothing.

## Attribution models, what each is for

| Model | Logic | Use |
|---|---|---|
| Last click | 100% to final touch | Default lens of most platforms; undervalues upper funnel |
| First click | 100% to first touch | Demand-creation analysis |
| Linear | Equal credit across touches | Simple multi-touch overview |
| Time decay | More credit near conversion | Considered purchases |
| Position-based | 40/20/40 first-mid-last | Balanced default for MTA reporting |
| Data-driven (DDA) | ML-assigned credit (Google default) | Best in-platform option; still walled-garden |
| Markov chains | Removal effect: how much conversion prob. drops if a channel vanishes | Cross-channel modeling with full path data |
| Shapley values | Game-theory fair credit across channels | MMM-adjacent budget arguments |
| **Incrementality / lift** | Holdout experiment: conversions vs no-ads control | **The ground truth, trumps all click models** |

Doctrine:
1. Attribution models are lenses, not truth. Only incrementality experiments measure cause.
2. Never compare numbers across lenses (platform 7-day-click vs GA4 last-click WILL
   disagree, footnote the basis everywhere).
3. Retargeting and brand-search always look heroic on click attribution; test their
   incrementality before crediting them.
4. Watch signal loss (ATT, cookie decay): CAPI + enhanced conversions + first-party data
   are the floor; modeled conversions are estimates, treat small deltas as noise.

## Consent and signal (2026)

- [F] Google Consent Mode now uses `ad_storage` as the single control for Google Ads data use.
- [F] Offline and enhanced-conversions-for-leads uploads moved to the Data Manager API.
- [F] Third-party cookies remain in Chrome by default (deprecation was abandoned), while some
  Privacy Sandbox APIs are being removed. Do not plan around either outcome.
- [F] India DPDP: consent-manager phase begins around November 2026, full enforcement in 2027.
- Verify current state per market before building consent architecture.

## Experiment designs

| Design | Use for | Rules |
|---|---|---|
| A/B test | Creative, LP, offer | One variable; pre-set sample/duration; no peeking-and-stopping |
| Multivariate | Element interactions on LPs | Needs big traffic; otherwise sequential A/Bs |
| Bayesian testing | Ongoing creative rotation | Probability-of-best beats p-values for ad decisions; platforms already run bandits, don't fight them with tiny manual splits |
| Sequential testing | Early stopping with validity | Use platform experiment tools' built-ins |
| Holdout groups | Email/retargeting/CRM incrementality | Suppress a random %, measure the delta |
| **Geo experiments** | Channel/budget incrementality without user tracking | Matched market pairs; the privacy-proof workhorse |
| Conversion lift | Platform-run RCT (Meta lift, Google CLX) | Gold standard for "does this channel work" |
| Budget stair-step | Marginal ROAS discovery | Raise budget 20-30%, hold 7-10 days, watch marginal (not average) ROAS |

Cadence: every client runs ≥1 real experiment per month. Minimum annual set: one channel
lift test, one creative-system test, one landing-page test, one budget-elasticity test.

## Forecasting & modeling (agent-level, honest versions)

- **Response curves:** assume diminishing returns; estimate marginal ROAS from budget
  stair-steps, never extrapolate average ROAS linearly to 2x spend.
- **Cohort LTV:** project from early-cohort repeat curves (D30/D60/D90 repeat rate ×
  margin); update monthly; sets CAC ceiling and payback window.
- **Churn/propensity signals:** recency-frequency-monetary segments are 80% of the value
  of fancy models at SMB scale, build RFM segments before dreaming of neural nets.
- **Media mix modeling (MMM):** for multi-channel clients at scale, regression of sales on
  channel spends with seasonality controls (open-source: Meta Robyn, Google Meridian).
  Directional, needs 2+ years data, position honestly.
- **Seasonality:** always model against the geo festival calendar (geo-playbooks.md), a "performance drop" that is actually a CPM season is a diagnosis failure.
