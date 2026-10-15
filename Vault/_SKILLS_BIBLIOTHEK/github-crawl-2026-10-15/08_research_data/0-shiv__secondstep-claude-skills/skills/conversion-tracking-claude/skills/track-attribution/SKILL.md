# Track Attribution — Sub-Skill

## Command
`/track attribution`

## Description
Analyzes attribution model setup across all advertising platforms, identifies cross-platform attribution conflicts, and recommends optimal configurations. Attribution determines which ad clicks and impressions get credit for conversions — the wrong model leads to wrong budget decisions. This skill audits attribution settings across Google, Meta, LinkedIn, and TikTok, and identifies where models conflict or create blind spots.

---

## Attribution Models Explained

### Last Click
- **How it works:** 100% credit to the last ad click before conversion
- **Best for:** Direct response campaigns with short consideration periods
- **Limitation:** Ignores all awareness and consideration touchpoints
- **Platform default:** LinkedIn (historical), Google Ads (legacy)
- **When to use:** Single-platform campaigns, simple funnels, when you need conservative reporting

### First Click
- **How it works:** 100% credit to the first ad click in the conversion path
- **Best for:** Understanding which channels drive initial awareness
- **Limitation:** Ignores everything that happens after the first touch
- **Platform availability:** Google Ads (being deprecated), GA4 exploration reports
- **When to use:** Rarely — mostly for awareness campaign analysis

### Linear
- **How it works:** Equal credit distributed across all touchpoints
- **Best for:** Understanding full customer journey
- **Limitation:** Overvalues low-impact touchpoints, undervalues high-impact ones
- **Platform availability:** Google Ads (being deprecated), GA4
- **When to use:** Long sales cycles with many touchpoints of equal importance

### Time Decay
- **How it works:** More credit to touchpoints closer to the conversion
- **Best for:** Sales cycles where recent interactions matter most
- **Limitation:** Undervalues early awareness touches
- **Platform availability:** Google Ads (being deprecated), GA4
- **When to use:** B2B with long sales cycles where nurturing accelerates near close

### Position-Based (U-Shaped)
- **How it works:** 40% to first click, 40% to last click, 20% split among middle touchpoints
- **Best for:** Valuing both discovery and closing touchpoints
- **Limitation:** Arbitrary weight distribution
- **Platform availability:** Google Ads (being deprecated), GA4
- **When to use:** Multi-channel strategies where both awareness and conversion matter

### Data-Driven Attribution (DDA)
- **How it works:** Machine learning analyzes all conversion paths to assign credit based on actual impact
- **Best for:** Accounts with sufficient conversion volume for statistical significance
- **Limitation:** Requires minimum conversion volume (~300 conversions in 30 days for Google)
- **Platform default:** Google Ads (new conversion actions), Meta (only model available)
- **When to use:** Whenever you have enough data — this is the recommended model

---

## Platform-Specific Attribution

### Google Ads
- **Default model:** Data-driven (for new conversion actions as of 2023)
- **Available models:** Data-driven, Last click (others being sunset)
- **Conversion window:** 1-90 days click-through, 1-30 days view-through
- **Where to check:** Tools > Conversions > select action > Attribution model
- **Key issue:** Old conversion actions may still use last-click — review each one
- **Recommendation:** Data-driven for all conversion actions with 300+ monthly conversions. Last click for low-volume actions.

### Meta Ads
- **Default model:** Data-driven (Meta's own model, not configurable)
- **Click window:** 1 day or 7 days (default: 7-day click)
- **View window:** 1 day (default: 1-day view)
- **Where to check:** Ad account settings, also per-campaign attribution setting
- **Key issue:** 7-day click + 1-day view is the default attribution setting — some advertisers unknowingly change this
- **Recommendation:** Keep 7-day click, 1-day view for most campaigns. Use 1-day click for testing conservative attribution.

### LinkedIn Ads
- **Default model:** Last-touch within the conversion window
- **Click window:** 1, 7, 30, or 90 days
- **View window:** 1 or 7 days
- **Where to check:** Campaign Manager > Conversion tracking > each conversion action
- **Key issue:** Default 30-day click window may be too long for some B2B cycles, or too short for enterprise
- **Recommendation:** 30-day click for most B2B. 90-day for enterprise sales cycles. 7-day view-through.

### TikTok Ads
- **Default model:** Last-touch
- **Click window:** 1, 7, 14, or 28 days
- **View window:** Off, 1 day, or 7 days
- **Where to check:** TikTok Events Manager > each event's attribution settings
- **Key issue:** Default view-through attribution can inflate conversion counts for awareness campaigns
- **Recommendation:** 7-day click, 1-day view for performance campaigns. Turn off view-through for strict ROI measurement.

---

## Cross-Platform Attribution Challenges

### The Double-Counting Problem
When a user sees a TikTok ad, then clicks a Google ad, then converts:
- Google Ads claims the conversion (last click)
- TikTok may claim it (view-through)
- Meta may claim it (if they also had an impression)
- Total reported conversions across platforms > actual conversions

**Diagnosis:**
- Sum conversions across all platforms
- Compare to actual conversions (CRM, e-commerce platform, GA4)
- If sum > actual by more than 20%, you have significant double-counting

**Mitigation:**
- Use GA4 as the single source of truth for cross-platform attribution
- Set up data-driven attribution in GA4 with all channels
- Use consistent conversion windows across platforms
- Consider turning off view-through attribution on platforms where it inflates numbers
- Never sum platform-reported conversions — always compare to an independent source

### Conversion Window Misalignment

If Google uses 90-day click-through and Meta uses 7-day click-through, you are comparing fundamentally different things. Standardize where possible:

**Recommended Alignment:**
| Platform | Click-Through | View-Through |
|----------|--------------|--------------|
| Google Ads | 30 days | 1 day |
| Meta Ads | 7 days | 1 day |
| LinkedIn | 30 days | 7 days |
| TikTok | 7 days | 1 day |

Note: Full alignment is not always possible or desirable — B2B platforms (LinkedIn) legitimately need longer windows. But document and understand the differences.

### Attribution Model Conflicts
- Google using data-driven, Meta using its own model, LinkedIn using last-touch
- Different models will assign credit differently to the same conversion path
- Accept that platform-reported numbers will not match each other
- Use GA4 or a third-party attribution tool as the neutral arbiter

---

## Audit Procedure

### Step 1: Document Current Settings
For each platform, record:
- Attribution model in use
- Click-through conversion window
- View-through conversion window
- Which conversion actions are primary vs secondary
- "Include in conversions" settings

### Step 2: Compare to Actual Conversions
- Pull total conversions from each platform for last 30 days
- Pull actual conversions from CRM / e-commerce platform / GA4
- Calculate: Platform Total / Actual Total = Overlap Ratio
- Overlap Ratio > 1.3 = significant double-counting

### Step 3: Identify Misconfigurations
- Old conversion actions with legacy models (last click)
- Inconsistent windows across conversion actions on the same platform
- View-through inflating numbers on low-intent campaigns
- Secondary conversions included in primary optimization

### Step 4: Recommend Changes
- Prioritize data-driven attribution where volume supports it
- Standardize windows within reason
- Set view-through appropriately per platform
- Ensure primary conversion actions are correctly designated

---

## Scoring Contribution

This sub-skill contributes up to **10 points** to the Tracking Health Score:

- Attribution models appropriate for each platform: 3 points
- Conversion windows documented and intentional: 2 points
- Cross-platform overlap ratio < 1.3: 3 points
- GA4 or neutral attribution source configured: 2 points

---

## Fix Priority

| Issue | Priority | Impact |
|-------|----------|--------|
| Legacy last-click model on Google Ads | High | Misallocating budget to last-touch channels |
| Massive cross-platform double-counting (>50%) | High | ROAS numbers are meaningless |
| No independent attribution source (GA4) | High | No neutral ground truth |
| Inconsistent windows on same platform | Medium | Comparing apples to oranges |
| View-through inflating conversions | Medium | Over-reported ROAS |
| No documentation of attribution settings | Low | Team confusion, inconsistent analysis |
