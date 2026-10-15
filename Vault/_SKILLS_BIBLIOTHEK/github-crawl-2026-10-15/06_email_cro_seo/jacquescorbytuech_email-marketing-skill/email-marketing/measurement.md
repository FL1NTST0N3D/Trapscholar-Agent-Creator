---
name: email-marketing/measurement
description: >
  Condensed measurement reference covering core metrics, holdouts and control
  groups, attribution, retention and LTV, sample size and power, volume
  thresholds, frequentist vs Bayesian testing, variance reduction, uplift and
  incrementality, and measuring platform intermediation. Reference this when
  evaluating whether a lifecycle programme worked or planning how to test it.
---

# Measurement

> Condensed offline fallback. The canonical, more complete versions live in the [CRM Open Knowledge Wiki measurement section](https://github.com/jacquescorbytuech/crm-open-knowledge-wiki/tree/main/measurement).

The discipline running through everything here: every method hands you a distribution, not a verdict, and a number without a control group is usually just the customers who were going to act anyway.

## Core Metrics

**The metric tree.** A lifecycle programme is measured in layers, each closer to money than the last. A win at one level only counts if it survives to the next:

1. **Engagement** — opens, clicks, click-to-open, replies. Earliest, noisiest, most corrupted by intermediation. Useful for diagnosis, dangerous as goals.
2. **Conversion** — the action the message existed to drive. The first level that means something on its own.
3. **Retention** — whether the customer stays, repeats, and remains reachable. Where the economics are actually decided.
4. **Revenue and value** — incremental revenue, margin, LTV. What the business cares about; everything else should ladder up to it.

**Decision metrics vs vanity metrics.** A decision metric changes what you do when it moves; a vanity metric only changes how you feel. The test: if this number moved 10%, would it change what you do next week? Name the concrete action a swing would trigger. If there is none, move the metric off the scorecard and into diagnostics. Open rate post-Mail Privacy Protection is a clear example: MPP inflated opens and severed the link to attention, so an open-rate rise while conversion stays flat is a vanity result — often not even real. Most dashboards show more vanity than decision metrics — the work is demoting decoration, not adding more.

**Choosing a North Star.** Pick one metric that best proxies the value the programme creates — often incremental revenue per recipient or a retention measure. A candidate must pass all three tests:

| Test | Meaning |
|---|---|
| In the causal path to value | Moving it moves the business, not just a dashboard |
| Movable by the programme | Shiftable via content, targeting, timing, frequency — not swamped by pricing/product/acquisition |
| Not a vanity proxy | Cannot be inflated without creating value |

Incremental revenue per recipient and repeat purchase rate pass. Open rate fails (vanity post-MPP). Total company revenue fails (programme cannot move it). Emails sent fails (activity count). Prefer the incrementally-measured version, against a holdout, over a gross last-touch total.

**Guardrails.** Any single optimised number can be hit by gaming what it ignores. Ask how a lazy optimiser would cheat the North Star, then cap each cheat: unsubscribe rate (caps mailing harder), spam complaint rate (caps annoyance that never shows as an unsubscribe), deliverability/inbox placement (protects the channel itself), and frequency per recipient (caps list-burning). A North Star move only counts if every guardrail stayed inside its cap. Set cap levels from your own baseline, not invented benchmarks.

**Tie metrics to lifecycle stages.** A single blended dashboard averages a working stage and a failing stage into a flat number. Give each stage one decision metric: onboarding → activation rate; mid-lifecycle → active rate; retention → cohort retention (read as a cohort, never a snapshot, so new users cannot mask churn in old ones); winback → reactivation rate.

**Leading and lagging indicators.** A North Star like cohort retention is lagging — true, but late. Watch leading indicators (week-one activation leads month-three retention; click-to-conversion leads incremental revenue) to act fast, and lagging ones to confirm. Never trust a leading move until the lagging number follows; a leading indicator that stops predicting its lagging partner has decayed into a vanity metric.

## Holdouts and Control Groups

Attribution tells you which messages preceded a conversion; it cannot tell you which conversions would have happened anyway. Only withholding the message from a randomly chosen, otherwise identical group isolates the lift the programme caused. This is the only number that proves the programme created value rather than taking credit for it.

**The always-on global holdout.** Hold back a small, randomly selected share of the addressable audience from *all* lifecycle messaging, continuously. The gap versus the messaged population — on conversion, retention, revenue — is the incremental contribution of the whole programme. It is the single most valuable measurement a CRM team can run, because it answers what would happen to revenue if we sent nothing. Keep it small, random, and permanent.

**Per-campaign controls** read the incremental effect of a specific send, sequence, or automation — how a new idea proves itself before rollout. Same discipline direct mail has always used.

**Sizing the holdout.** No universal percentage. Bigger tightens the read; bigger withholds more revenue. Pick the smallest holdout that can still detect the effect size that would change a decision, over the period you are willing to wait. Work the n from baseline rate, minimum effect worth detecting, and available volume (see sample size below).

**Randomise correctly, or the gap is selection bias:**

1. Assign at the person level, not the send level — a user stays out of *every* message.
2. Use a stable random key: hash a durable user id, bucket on the hash, so membership is fixed without a flag you might forget to honour.
3. Assign before eligibility, not after. Split the whole addressable audience first, then let targeting run inside both arms. Picking treated = qualified and control = the rest makes the arms differ on exactly the thing that drives conversion.

Pitfalls: re-rolling assignment each run; excluding the holdout from journey entry criteria; another channel or team messaging the holdout; splitting on anything correlated with behaviour (sign-up date, region, list source).

**Maintaining the global holdout.** Fix membership for the whole measurement window. Read the gap over a quarter, not a week — the point is the slow signal in retention and revenue. New users flow into both arms automatically via the hash. Re-randomise only at a clean period boundary, rarely, never mid-read, and document the date.

**Reading results.** Compute the outcome rate per arm on the same definition and window; take treatment minus control as the absolute incremental rate; attach an interval; judge significance with the two-proportion test — never by eye.

**Geo experiments** when individuals cannot be split (brand, offline): randomise comparable geographies, establish a pre-period baseline relationship, treat some regions, and read lift as divergence from a synthetic control — a weighted combination of untreated regions modelling what the treated region would have done. Standard tooling: Meta GeoLift, Google Meridian.

Incrementality is the higher bar, so incremental return reads *lower* than last-touch return. Adjusting expectations to that is part of the method, not a failure of it.

## Attribution

Attribution is not one question with competing answers — it is three questions, and each method answers one well and the others badly. Before any of them: a tracked click proves nothing about causation. It proves a send was opened and acted on, not that it changed what the user would have done. Only a controlled holdout establishes that.

- **Last-click** gives all credit to the final touch. Simple, available, and systematically wrong in one direction: it over-credits whatever sat closest to a conversion that was often already going to happen, and credits nothing to demand built earlier.
- **Multi-touch (MTA)** spreads credit across the observed journey. Sharper for near-real-time within-channel optimisation, but it only sees the trackable slice — eroded by cookie deprecation, ATT, and the walled gardens. Both are bottom-up and correlational; neither establishes cause.
- **Marketing mix modelling (MMM)** works top-down, regressing outcomes on aggregate spend and external factors. Values offline and brand, survives privacy decay (no user-level tracking needed). A credible model captures adstock (carryover decay over weeks) and saturation (diminishing returns as spend rises). Costs: data-hungry, needs real expertise, vulnerable to multicollinearity when channel budgets move together. It answers portfolio budget allocation, not which message to send next.
- **Incrementality is the referee.** Only a controlled experiment measures causation directly. It does not replace attribution or MMM; it calibrates them. When last-touch says one number and MMM another, a clean lift test is the tiebreaker.

For a lifecycle programme: build the read on the authenticated cohort, where identity is deterministic, and anchor on a holdout rather than the click. The destination-conversion frame is also the one that survives platform intermediation.

## Retention and LTV

Engagement and conversion metrics measure the message; retention and LTV measure the business. These are the numbers a lifecycle programme should be judged on.

**Build a cohort retention curve.** Group by acquisition month; define "active in period" (purchase, login, paid renewal, in a fixed window); denominator is cohort size fixed at acquisition; retention(N) = active in month N / cohort size. Plot months since acquisition against percent retained.

**Read the shape.** Decline then flatten: casual sign-ups fall away, settling onto the floor that is your stable core. The height of that floor is the number that matters. A curve that never flattens has no core — a product or fit problem no messaging will fix. Segment by acquisition channel; customers acquired cheaply through one route often retain quite differently from another.

**Contractual vs non-contractual.** In contractual businesses churn is observed (a renewal happens or it does not); project with a shifted-beta-geometric model, workable from a handful of periods in a spreadsheet (Fader & Hardie 2007). In non-contractual businesses nobody announces departure; use buy-till-you-die models — Pareto/NBD or the lighter BG/NBD — which infer dropout from purchase frequency and recency. Reach for the wrong family and the projection misleads.

**Why the curve rises, and why one churn rate misleads.** Period-on-period retention climbs as a cohort ages — not because customers grow loyal, but because high-churn customers leave first and what remains is enriched in the loyal. It is a sorting effect in a mixed population. Applying one blended early-period churn rate flat into the future understates LTV, often badly. Never extrapolate by eye either (that overstates); fit a model, cap the horizon, and re-fit per cohort.

**LTV.** Sum contribution margin per period, weighted by retention, discounted:

```
LTV = Σ over t: M × retention(t) / (1 + d)^t
```

Use contribution margin, not revenue. Discount future value. Prefer cohort LTV to a blended figure.

**LTV:CAC and payback.** LTV:CAC around 3:1 is the common health marker. Payback period = periods until cumulative margin clears CAC — how long acquisition spend is underwater. Compute both segmented by acquisition source (a cheap channel can be the worst once retention is weighed), by cohort (earliest read on whether changes are working), and by tier. LTV is an input to a decision, and the decision lives at the segment level, not the average.

**Retention sensitivity.** Nudge each input by the same proportion and compare LTV impact. Retention wins: it compounds through every later period, while a margin change scales a fixed set of flows. One widely cited estimate (Gupta, Lehmann & Stuart 2004) puts firm-value impact of a 1% retention gain at ~5%, versus ~1% for an equivalent margin gain. That is the quantified case for spending on the retention stage, and it usually beats cutting price.

**Prove retention gains against a holdout.** Retention responds to onboarding that drives early activation, relevant well-paced messaging, and timely pre-lapse intervention (targeted by a churn propensity model) — not heavier discounting. A retention gain claimed without a control group is usually just the customers who were going to stay anyway.

## Sample Size and Power

A sizing model without a sample size estimate tells you what you could achieve, not whether you can detect it. The required sample grows explosively as the effect shrinks, so the real use of the formula is deciding *in advance* which tests are not worth running. Treat it as a filter, not a recipe.

The standard planning form is a two-proportion z-test, two-sided, 80% power, 95% confidence:

```
Users per variant = (Z_a + Z_b)² × (p1(1−p1) + p2(1−p2)) / (p2 − p1)²
```

with Z_a = 1.96 and Z_b = 0.8416, giving (Z_a + Z_b)² ≈ 7.85. Two-sided is the right default — you do not know which variant wins in advance. Then:

```
Test duration = (Users per variant × 2) / Users entering per week
```

Evan Miller's sample size calculator handles the proportion case interactively. Fix the sample in advance; stopping when the result looks good is what breaks the false-positive rate.

**Reading the result.** For observed proportions p1, p2 over n1, n2:

```
SE = sqrt( p1(1−p1)/n1 + p2(1−p2)/n2 )
```

The 95% CI on the difference is (p2 − p1) ± 1.96 × SE; significant when the interval excludes zero. Report the interval, not just the point. Below the volume floor the interval is a wide band around zero whatever the point estimate looks like.

Note the wiki standard here is the two-sided test; the [impact sizing](impact-sizing.md) fallback uses a one-sided variant for planning. Sub-percent effects (platform intermediation territory) sit where required n is infeasible for most teams, and difference-in-differences designs need more than this optimistic floor.

## Volume Thresholds

Anchored on a 2% campaign click rate (defensible round number for typical B2C, per 2026 Klaviyo/Mailchimp benchmarks), at 95% confidence and 80% power, sends per cell needed to detect a relative shift:

| Relative shift | Absolute change | Sends per cell | What it usually represents |
|---|---|---|---|
| 20% | +0.40pp | ~21,000 | Major creative pivot, exceptional |
| 10% | +0.20pp | ~80,000 | Strong A/B win, well-run programme |
| 5% | +0.10pp | ~315,000 | Typical mature programme win |
| 3% | +0.06pp | ~870,000 | Clean intermediation effect |
| 2% | +0.04pp | ~1,940,000 | Low-end intermediation effect |
| 1% | +0.02pp | ~7,720,000 | Platform internal A/B territory |
| 0.5% | +0.01pp | ~30,800,000 | Meta-scale notification optimisation |

These are floors for the easiest design; complex designs raise them, and every cohort/segment/channel split multiplies the cells. For another channel, substitute your own measured baseline rate into the formula — higher base rates need proportionally fewer observations, lower need more.

**How to use the table** — read it before designing a test, not after it fails:

- Size to a realistic win. Genuine A/B wins are mostly 5–10% relative, needing ~80,000–315,000 sends per cell. If a cell cannot reach that, do not run the test — ship the better-reasoned option and move on.
- Do not over-segment. Every split shrinks cells toward the noise floor; segmentation buys relevance with statistical power.
- Pool comparable campaigns and lengthen windows to accumulate volume a single send cannot.
- Chase bigger swings. A small list can only detect large effects — spend test budget on creative pivots and new offers, not subject-line micro-tweaks it can never read.
- Lean on holdouts for the big questions. Programme-level incrementality is a large effect, readable at far lower volume than a per-campaign click delta.

## Frequentist vs Bayesian Testing

Two schools, answering subtly different questions. In a low-volume programme the choice is a rounding error against the real question — whether you have the volume for either to say anything.

**Frequentist:** if there were truly no difference, how surprising is this data? The p-value is that surprise; significance is conventionally below 5%. Demands you fix the sample in advance and read once. The default for good reason: well understood, no priors, simple planning maths. But a p-value of 0.03 does *not* mean a 97% chance the variant wins — it means data this extreme would occur 3% of the time if the variants were identical. That misreading is the most common error in marketing analytics.

**Bayesian:** start from a prior, update with data, get a posterior distribution. Yields the statements stakeholders actually want — "92% probability B beats A", "expected loss from shipping B is 0.1%". Costs: the prior (a strong one smuggles in a guess), and heavier machinery fewer practitioners can defend.

**The peeking trap catches both.** Stopping a running test the moment it crosses significance inflates the false-positive rate far above the nominal 5% — noise gets many chances to cross the line. Naive Bayesian dashboards are not immune; stopping at "95% probability to be best" has the same problem. Fixes: fix the sample in advance, or use a method built for repeated looks (sequential testing, always-valid p-values, a proper Bayesian loss-threshold rule).

**Which to reach for in CRM:** default to frequentist with a fixed sample — it forces the volume discipline a small list needs. Reach for Bayesian when communicating to non-statisticians, or use its expected-loss rule to ship a marginal winner rather than declaring no result. Bayesian hierarchical shrinkage genuinely helps when running many small tests: it pools across campaigns and damps the false dramatic wins a low-volume programme throws off. Either way, never peek without a method that allows it.

## Variance Reduction and Sequential Testing

The two standard ways to get more from the volume you have. Neither manufactures signal or repeals the volume floor; they lower it, sometimes enough to make a test that was theatre into one worth running.

**CUPED.** Use a pre-experiment metric correlated with the outcome (each user's prior spend or activity) to subtract the part of the result the pre-period already explains. Variance reduction is roughly the square of the correlation: a covariate correlated at 0.6 removes about a third of the variance — equivalent to a third more users for free. A particularly good fit for CRM, which already holds rich per-customer history on an identified base. Requirements: covariate measured on the same users before treatment, and not itself affected by the test.

**Sequential testing.** Always-valid p-values, group-sequential designs, and mSPRT methods hold the error rate no matter how often you look, so you can monitor continuously and stop as soon as the evidence is in. The trade: slightly more conservative than a fixed test at any given n. Worth it when stopping early has real value (cutting a holdout's withheld revenue, killing a losing variant); if you would run to a fixed sample anyway, the plain fixed test is more powerful.

**What they cannot do:** a list that cannot detect a 1% effect with the plain test will detect a 1.4% effect instead of a 2% one — not the 1%. Use these to make a borderline test viable, not to pretend a list has volume it does not.

## Uplift and Incrementality

The real question is not "did the user open it" but "did sending it change what they did, versus an identical user left alone". That separates three groups: **persuadables** (a message wins them over), **sure things** (convert anyway — a wasted send), and **do-not-disturbers** (would have converted if you had stayed quiet — messaging actively loses them).

**Two different jobs share the word "uplift":**

1. **Measuring incrementality** — how much did this send/sequence/programme change behaviour in aggregate. A single number with a confidence interval, read from a randomised holdout. Most teams need only this.
2. **Modelling uplift** — which individual users are persuadable, so you can target them and suppress the rest. Needs a model trained on experimental data; worth it only at high volume.

Do the first before attempting the second. A team that cannot measure programme incrementality has no clean signal to train an uplift model on.

**The incrementality arithmetic:**

```
Incremental rate (absolute) = conversion_treatment − conversion_control
Relative uplift             = incremental rate / conversion_control
Incremental conversions     = incremental rate × audience size
```

Worked read: winback flow to 100,000 eligible, 5,000 held back. Treated convert at 4.0%, control at 3.4%. Absolute lift 0.6pp, relative 17.6%, ~570 incremental conversions — not the ~3,800 a last-touch report would claim. But with 5,000 in control the SE on that 0.6pp is ~0.26pp, so the 95% interval runs ~0.08pp to 1.1pp (roughly 80 to 1,060 conversions). Significant, but only just. The gap between 570 and 3,800 is the point; the width of the interval is the second point.

**Why prediction is not decisioning.** A propensity model targets people most likely to act — which keeps messaging the sure things and annoying the do-not-disturbers. An uplift model must be willing to send nothing; the skill is knowing whom *not* to message. Cumulative incremental effect peaks well before the whole list; past the peak, more targeting reduces it, and sending to everyone lands in zero or negative territory.

**Modelling approaches** (all need randomised training data, never observational history): T-learner (two models, treated and control — simple but small effects drown in the errors of two large models); S-learner (treatment as a feature — stable but underplays weak treatment effects); class transformation (clean with a 50/50 split, a good first real attempt); direct uplift trees/forests and meta-learners like the X-learner (best when arm sizes differ). Use libraries — scikit-uplift, CausalML, EconML — not scratch implementations.

**Evaluation:** no per-user ground truth exists, so classifier metrics do not apply. Use a held-back randomised set: the Qini/uplift curve (a useful model bends above the diagonal and peaks before the full audience — the peak is your optimal targeting depth), the Qini coefficient (area over the diagonal, the uplift AUC), and uplift by decile (measured incremental rate must fall monotonically; a model whose top decile does not show the highest real lift is not ready).

**Why most brands cannot do it.** A platform can read a 0.42% lift across tens of millions per arm. A list in the tens of thousands cannot detect sub-percent moves in anything, which is the real reason the long tail clings to cheap surface metrics. For most senders the honest stopping point is a programme-level holdout plus a handful of per-flow controls.

## Measuring Intermediation

When a platform changes how it filters, ranks, or summarises your sends (a spam policy, a summarisation feature, a tab re-sort), it does not report what it did. These methods estimate the effect from your own data — but first, the blunt gate: **most senders should not attempt this at all.** The methods need hundreds of thousands of sends per cell, often millions. Below that floor they return wide intervals around zero whatever the platform did. The useful output below the floor is the diagnostic — intermediation is bending your numbers and you cannot cleanly say by how much — so treat corrupted metrics with suspicion instead of spending effort quantifying the distortion.

**The probe kit, for those with the volume:**

- **Difference-in-differences around platform release dates.** Affected cohort vs unaffected cohort, change across the known release date, difference the two. Caveats: parallel trends is an assumption; your own copy shifted around the same date; and eligibility is not treatment, so you read a diluted intent-to-treat effect.
- **Sender-side ablation.** Hold the audience constant, vary what you control (subject structure, preheader, HTML weight, image-to-text ratio). The delta should be larger on the eligible cohort if the suspected layer is doing the work. The cleanest internal experiment.
- **Cohort comparison by platform eligibility.** The weakest probe — cohorts are not random samples of each other and selection bias swamps the signal. Sanity check only.
- **Transactional sends as a within-user control.** Never compare promotional-to-transactional ratios directly. Use transactional engagement only inside a diff-in-diff, to confirm general willingness to engage did not crater for an unrelated reason. A tiebreaker, not a method.

For email specifically: Postmaster Tools and SNDS monitoring, Mozilla/5.0 user-agent segmentation for MPP, inbox-provider cohort comparison, seed-list tab placement (directional only), one-click unsubscribe timing, DMARC aggregate reports, reply rate.

**What survives:** shift measurement weight off channel-surface click-through and onto channel-to-destination and destination-to-outcome conversion. The first is mediated by the platform; the second is not. Build on the authenticated cohort, where attribution is deterministic — the frame that holds up as more of the inbox is summarised or acted on by assistants.

## Sizing and Prioritising Experiments

For estimating how many incremental actions an experiment will drive — model types, the core formula, input hygiene, and prioritisation — see [impact sizing](impact-sizing.md). Pair its output with the sample size formula and volume threshold table above: a compelling opportunity that needs sixteen weeks of test time to confirm may be a worse use of resources than a faster test on a smaller prize.
