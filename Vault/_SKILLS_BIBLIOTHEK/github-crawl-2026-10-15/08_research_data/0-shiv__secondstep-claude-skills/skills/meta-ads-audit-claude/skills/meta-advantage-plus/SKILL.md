# Meta Advantage+ Audit

## Command
`/meta advantage`

## Description
Evaluates the configuration and performance of Meta's Advantage+ suite — including Advantage+ Shopping Campaigns (ASC), Advantage+ App Campaigns, Advantage+ Audience, Advantage+ Creative, Advantage+ Placements, and dynamic creative optimization. Advantage+ represents Meta's shift toward AI-driven campaign management, and proper setup is critical to unlocking its potential.

## Why Advantage+ Configuration Matters

Meta's Advantage+ products use machine learning to automate targeting, creative optimization, and placement decisions. When configured correctly, they can:

- **Reduce CPA by 12-20%** compared to manual campaigns (Meta's internal data)
- **Expand reach**: Find high-intent users outside your manually defined audiences
- **Automate creative testing**: Dynamic creative tests combinations algorithmically
- **Simplify account structure**: Fewer campaigns with broader automation

However, misconfigured Advantage+ can also waste budget on low-quality audiences, deliver to poor placements, or over-expand beyond your target market.

## Audit Checklist (25 Points)

### 1. Advantage+ Shopping Campaigns (ASC) (7 points)

ASC is Meta's fully automated shopping campaign type designed for e-commerce advertisers. It combines prospecting and retargeting in a single campaign with minimal manual controls.

- [ ] **ASC Active**: Is the account running Advantage+ Shopping Campaigns?
- [ ] **Existing Customer Budget Cap**: Is the existing customer budget cap set? (Critical — without it, ASC will over-index on retargeting)
  - Recommended: Set cap at 20-30% of budget for existing customers
  - Default (no cap): Meta may spend 50-80% on existing customers
- [ ] **Customer Definition**: Has the advertiser defined "existing customers" via:
  - Customer list upload
  - Pixel-based purchase audience
  - App activity audience
- [ ] **Product Catalog Connected**: Full product catalog linked and up to date
- [ ] **Catalog Quality**: Check for disapproved products, missing images, stale inventory
- [ ] **Geographic Targeting**: Appropriate country/region targeting (ASC defaults to broad)
- [ ] **Performance vs Manual**: Is ASC outperforming manual campaigns? (Run for 2+ weeks before judging)

### 2. Advantage+ App Campaigns (3 points)

For app install and app event advertisers.

- [ ] **App Campaign Setup**: If running app campaigns, is Advantage+ App being used?
- [ ] **Deep Link Configuration**: App deep links properly configured for post-install events
- [ ] **App Event Optimization**: Optimizing for valuable in-app events (not just installs)

### 3. Advantage+ Audience (Audience Expansion) (5 points)

Advantage+ Audience allows Meta to expand beyond your defined targeting when it predicts better results.

- [ ] **Audience Expansion Enabled**: Check which ad sets have Advantage+ Audience active
- [ ] **Audience Suggestions vs Targeting**: Understand the difference:
  - **Audience Suggestions** (new default): Your targeting is a "suggestion" — Meta can go beyond it
  - **Original Audiences**: Traditional targeting with optional expansion toggle
- [ ] **Expansion Impact**: Compare performance metrics inside vs outside defined audience
- [ ] **Geographic Guardrails**: Verify location targeting is not being expanded to unwanted regions
- [ ] **Age/Gender Guardrails**: If product is age/gender specific, verify these restrictions hold

**When to Enable Advantage+ Audience:**
| Scenario | Recommendation |
|----------|---------------|
| Broad e-commerce (wide demo) | Enable — let Meta find buyers |
| Local business (geo-specific) | Caution — verify geo restrictions hold |
| Regulated industry (age/compliance) | Disable — manual targeting for compliance |
| B2B with narrow ICP | Disable — expansion dilutes targeting |
| Retargeting campaigns | Disable — audience already defined |

### 4. Advantage+ Creative (5 points)

Advantage+ Creative applies automatic enhancements to your ads.

| Enhancement | What It Does | Risk Level |
|------------|-------------|-----------|
| Text optimization | Rearranges primary text, headline, description | Low |
| Media enhancement | Adjusts brightness, contrast, cropping | Medium |
| Music | Adds background music to video ads | Medium |
| 3D motion | Adds subtle motion to static images | Low |
| Relevant comments | Shows highly-engaged comments first | Low |
| Label additions | Adds dynamic labels (free shipping, sale) | Low |
| Template variations | Creates new layout variations | Medium |

- [ ] **Enhancement Settings Review**: Which Advantage+ Creative features are enabled?
- [ ] **Brand Safety Check**: Are media enhancements altering brand-critical visuals?
- [ ] **Text Optimization Results**: Is text rearrangement maintaining intended messaging?
- [ ] **Music Appropriateness**: If music is auto-added, does it match brand tone?
- [ ] **Performance Comparison**: Are enhanced versions outperforming originals?

### 5. Dynamic Creative Optimization (DCO) (5 points)

DCO automatically tests combinations of creative elements (images, videos, text, CTAs) and optimizes delivery to the best-performing combinations.

- [ ] **DCO Active**: Are any ad sets using dynamic creative?
- [ ] **Asset Count**: Minimum 3 variations per element for meaningful testing
  - Images/Videos: 3-10 variations
  - Primary text: 3-5 variations
  - Headlines: 3-5 variations
  - Descriptions: 2-3 variations
  - CTAs: 2-3 options
- [ ] **Asset Quality**: All variations are genuinely different (not minor color tweaks)
- [ ] **Combination Coverage**: Total possible combinations sufficient for learning
- [ ] **Performance Breakdown**: Review which combinations are winning — are results expected?

## Advantage+ Readiness Assessment

Before enabling Advantage+, verify:

| Prerequisite | Required For | Status |
|-------------|-------------|--------|
| Product catalog (complete, approved) | ASC | Required |
| Existing customer list (1,000+) | ASC budget cap | Required |
| Pixel with Purchase events | ASC optimization | Required |
| CAPI configured | ASC data quality | Recommended |
| 3+ creative formats | Advantage+ Creative | Recommended |
| $100+/day budget | ASC minimum viable | Required |
| 30+ conversions/week | ASC learning phase | Required |

## Common Issues & Fixes

### Issue: ASC Over-Spending on Existing Customers
**Symptom**: ROAS looks great but most conversions are from existing customers who would have bought anyway
**Root Cause**: No existing customer budget cap set, or cap set too high
**Fix**: Set existing customer budget cap to 20-30%. Upload customer list to define "existing."

### Issue: Advantage+ Audience Expanding to Wrong Regions
**Symptom**: Getting clicks/conversions from countries outside target market
**Root Cause**: Advantage+ Audience overriding location targeting
**Fix**: Location targeting should be set as a hard restriction. Check campaign settings — some objectives allow location expansion.

### Issue: Dynamic Creative Shows Poor Combinations
**Symptom**: Ugly combinations being served (wrong image + wrong headline)
**Root Cause**: Too many unrelated assets mixed together
**Fix**: Ensure all assets work well in any combination. If some assets are product-specific, create separate dynamic creative ad sets per product line.

### Issue: Advantage+ Creative Distorting Brand Imagery
**Symptom**: Ads show with altered colors, cropping, or unwanted filters
**Root Cause**: Media enhancement is auto-adjusting creative
**Fix**: Disable media enhancement at the ad level for brand-critical creative. Keep text optimization enabled (lower risk).

## Output Format

```
## Advantage+ Audit Results

**Score: XX/100** (Grade: X)
**ASC Status: [Active/Not Active/Not Applicable]**
**Advantage+ Audience: [Enabled on X/Y ad sets]**
**Dynamic Creative: [Active on X ad sets]**

### Advantage+ Feature Status
| Feature | Status | Config Quality | Notes |
|---------|--------|---------------|-------|
| ASC | Active | Good | Customer cap at 25% |
| Advantage+ Audience | Enabled | Warning | Expanding beyond geo |
| Advantage+ Creative | Partial | Good | Text only, no media |
| Dynamic Creative | Active | Poor | Only 2 variations |

### Critical Findings (P0)
- [e.g., ASC has no existing customer budget cap — 65% of spend going to existing customers]

### Recommendations
1. [Action item — e.g., Set ASC existing customer cap to 25%]
```
