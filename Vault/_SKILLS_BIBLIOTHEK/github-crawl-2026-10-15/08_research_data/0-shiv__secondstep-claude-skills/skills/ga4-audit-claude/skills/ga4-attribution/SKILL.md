# GA4 Attribution Audit

## Command
`/ga4 attribution`

## Purpose
Audit attribution model settings and conversion path analysis in GA4. Attribution determines how credit for conversions is assigned to marketing touchpoints. Incorrect attribution settings lead to misallocated budgets — channels that actually drive conversions get underfunded while underperformers get overfunded. This is often the most expensive misconfiguration in a GA4 property.

## GA4 Attribution Models

GA4 offers the following attribution models (note: Google has been sunsetting models, leaving primarily two):

### Currently Available Models

**Data-Driven Attribution (DDA) — Default and Recommended:**
- Uses machine learning to distribute credit based on actual conversion path data
- Analyzes all touchpoints and assigns fractional credit
- Requires sufficient conversion volume to build a reliable model
- Falls back to a rules-based model when data is insufficient
- Best for: Most properties with reasonable conversion volume (50+ conversions/month)

**Last Click (Paid and Organic):**
- 100% credit to the last touchpoint before conversion
- Ignores all earlier touchpoints in the customer journey
- Best for: Properties with very low conversion volume, simple buying cycles, or when comparing to historical UA data
- Caution: Heavily favors brand search and direct traffic, undervalues awareness/prospecting channels

### Deprecated Models (No Longer Available for New Configuration)
Google removed these models in late 2023:
- First click
- Linear
- Time decay
- Position-based

**Audit note:** If a property was set to one of these deprecated models before the cutoff, it was automatically migrated to data-driven or last click. Verify the current setting.

## Audit Checklist

### 1. Attribution Model Settings

Located in Admin > Attribution Settings:

- [ ] Attribution model is explicitly chosen (not left at whatever default was set during property creation)
- [ ] Data-driven attribution is selected (recommended for most properties)
- [ ] If last click is selected, there is a documented business reason
- [ ] Team/stakeholders understand which model is in use and why
- [ ] Model selection is consistent between GA4 and Google Ads (if linked)

**When to use DDA vs Last Click:**
| Factor | Use DDA | Use Last Click |
|--------|---------|---------------|
| Monthly conversions | 50+ | <50 |
| Marketing channels | Multiple (3+) | 1-2 |
| Buying cycle | Multi-touchpoint | Single session |
| Budget allocation | Need accurate channel credit | Simple reporting |
| Google Ads | Smart Bidding campaigns | Manual bidding only |

### 2. Lookback Windows

Lookback windows determine how far back GA4 looks when assigning attribution credit.

**Acquisition conversion events** (first_visit, first_open):
- [ ] Lookback window is set (options: 30, 60, or 90 days)
- [ ] 30 days is appropriate for most businesses
- [ ] Longer windows (60-90 days) for long-consideration products (B2B, real estate, luxury)

**All other conversion events:**
- [ ] Lookback window is set (options: 30, 60, or 90 days)
- [ ] Window matches the typical customer buying cycle
- [ ] E-commerce: 30 days is usually sufficient
- [ ] B2B / High-ticket: 60-90 days recommended
- [ ] Impulse purchases: 30 days or less

**Engaged-view conversions:**
- [ ] Engaged-view lookback is configured (if running YouTube/Video campaigns)
- [ ] Options: Turn off, or set to match other lookback windows
- [ ] Understand: Engaged-view tracks users who watched 10+ seconds of a skippable YouTube ad (or 30 seconds / entire ad if shorter) and later converted

### 3. Conversion Paths Report

The Conversion Paths report (Advertising > Attribution > Conversion paths) shows the touchpoint sequences leading to conversions.

- [ ] Conversion Paths report is being reviewed regularly
- [ ] Multi-touch paths are present (not all single-touch, which suggests tracking issues)
- [ ] Path lengths align with business expectations:
  - E-commerce: Average 2-4 touchpoints
  - B2B: Average 4-8 touchpoints
  - SaaS: Average 3-6 touchpoints
- [ ] Channel groupings in paths are correctly classified (no excessive "Unassigned" or "Direct")
- [ ] "(not set)" values are minimal in path data
- [ ] Paths include paid channels when Google Ads is active

### 4. Model Comparison

Use the Model Comparison report to validate attribution settings.

- [ ] Compare DDA vs Last Click to identify channels that benefit from multi-touch credit
- [ ] Channels with significantly higher DDA credit than last click are awareness/prospecting channels — verify they are funded appropriately
- [ ] Channels with higher last click credit are closing/conversion channels
- [ ] No channel has 0 conversions under DDA that has conversions under last click (or vice versa) — this could indicate a data issue

### 5. Channel Groupings

Attribution accuracy depends on correct channel classification.

- [ ] Default channel grouping correctly classifies all traffic sources
- [ ] Paid search is correctly attributed (GCLID auto-tagging enabled)
- [ ] Organic search is correctly attributed (Search Console linked)
- [ ] Social traffic is correctly classified (organic vs paid)
- [ ] Email traffic has proper UTM parameters
- [ ] Referral traffic is correctly classified (no self-referrals)
- [ ] Direct traffic percentage is reasonable (<30% is good, >50% suggests tracking issues)
- [ ] "Unassigned" channel is minimal (<5% of traffic)
- [ ] Custom channel groupings are created if default groupings don't match business needs

### 6. Google Ads Attribution Alignment

If GA4 is linked to Google Ads, attribution settings should be aligned.

- [ ] GA4 attribution model and Google Ads attribution model are consistent
- [ ] Imported GA4 conversions use the GA4 attribution model in Ads
- [ ] Google Ads conversion action attribution is set to Data-Driven (if using Smart Bidding)
- [ ] Conversion lag is understood and accounted for in reporting
- [ ] Attribution differences between GA4 and Google Ads are documented and understood

### 7. Attribution Data Quality

- [ ] UTM parameters are consistently applied to all marketing campaigns
- [ ] UTM naming convention is documented and enforced (lowercase, consistent source/medium)
- [ ] No UTM parameters on internal links (causes session restarts, breaks attribution)
- [ ] GCLID is not being stripped by redirects or URL shorteners
- [ ] Cross-domain tracking preserves attribution data
- [ ] Attribution data is not being affected by adblockers at a rate >20%

## Common Issues Found

1. **Attribution model never configured** — Still on whatever default was set, often not appropriate for the business.
2. **Lookback window too short for business cycle** — 30-day lookback for a B2B SaaS with 90-day sales cycle means losing credit for early touchpoints.
3. **High "Direct" traffic percentage** — Usually indicates broken UTM tracking, not actual direct visits. Real direct traffic is typically 20-30%, not 50%+.
4. **"Unassigned" channel in paths** — Traffic sources not matching any channel grouping rules, meaning attribution is incomplete.
5. **GA4 and Google Ads attribution mismatch** — Different models in each platform causing conflicting conversion counts.
6. **UTM on internal links** — Internal links with UTM parameters reset the session source, breaking the original attribution.
7. **Missing GCLID** — Auto-tagging disabled or GCLID stripped by redirects, breaking Google Ads attribution.
8. **Deprecated model auto-migration** — Property was on position-based attribution, got migrated to DDA without verification.

## Scoring

| Check Area | Points | Weight |
|-----------|--------|--------|
| Model selection | 25 | 25% |
| Lookback windows | 20 | 20% |
| Conversion paths | 15 | 15% |
| Channel groupings | 20 | 20% |
| Ads alignment | 15 | 15% |
| Data quality | 5 | 5% |

**Score = (passed_points / total_applicable_points) * 100**

## Output Format

```
## Attribution Audit

**Score: XX/100**

### Attribution Settings
- Model: [Data-Driven / Last Click]
- Acquisition lookback: [30/60/90] days
- Other conversion lookback: [30/60/90] days
- Engaged-view: [On/Off]

### Channel Distribution
| Channel | Sessions | Conversions (DDA) | Conversions (Last Click) | Delta |
|---------|----------|-------------------|--------------------------|-------|
| Organic Search | X | X | X | +/-X% |
| Paid Search | X | X | X | +/-X% |

### Path Analysis
- Average path length: [X] touchpoints
- Most common path: [Channel > Channel > Channel]
- Direct traffic %: [X]%
- Unassigned %: [X]%

### Findings
[Passed/Failed/Warning items with fix instructions]
```
