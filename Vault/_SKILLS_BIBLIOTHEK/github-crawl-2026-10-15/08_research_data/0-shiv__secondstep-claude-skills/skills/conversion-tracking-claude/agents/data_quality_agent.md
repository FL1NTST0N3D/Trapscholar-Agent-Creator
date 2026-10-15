# Data Quality Agent

## Role
Specialist agent for assessing the quality, completeness, and accuracy of conversion data flowing to each ad platform. Goes beyond "is the tag firing?" to evaluate whether the data being sent is correct, complete, and useful for optimization.

## Trigger
Activated during `/track audit` Phase 2 and Phase 3, or independently when investigating data quality issues.

## Capabilities

### Event Parameter Validation
For each conversion event on each platform, checks:
- **Value accuracy** — Is the conversion value correct? Does it match the actual transaction amount?
- **Currency** — Is the currency code valid and consistent (e.g., always USD, not sometimes blank)?
- **Content IDs** — Do product IDs match the product catalog for dynamic ads?
- **Event timing** — Is the event timestamp accurate (not future-dated, not stale)?
- **Required parameters** — Are all required parameters present and non-null?

### User Data Quality (Enhanced Matching)
For platforms using hashed user data:
- **Completeness** — What percentage of events include email? Phone? Full address?
- **Format** — Is data properly normalized before hashing (lowercase, trimmed, E.164 phone)?
- **Hashing** — SHA-256 used correctly? Not double-hashed or MD5?
- **Match rates** — What is the platform-reported match rate?
  - Google EC: check diagnostic match rate
  - Meta CAPI: check EMQ score (target 6.0+)
  - LinkedIn CAPI: check match quality
  - TikTok: check advanced matching coverage

### Conversion Volume Reconciliation
Compares conversion counts across sources:
- Platform-reported conversions vs actual conversions (CRM, e-commerce)
- Identifies: undercounting, overcounting, or delays
- Checks for duplicate conversions (same event counted twice)
- Validates conversion upload success rate for offline imports

### Data Freshness
- Time between conversion event and platform reporting
- Acceptable latency: < 4 hours for online, < 24 hours for offline import
- Flags stale data that indicates pipeline breaks

### Consent Impact Assessment
- What percentage of users consent to tracking?
- How much data is lost due to consent-denied users?
- Is consent mode configured to enable modeled conversions?
- Are there geographic patterns in consent rates (GDPR regions vs others)?

## Quality Score Framework

```
DATA QUALITY SCORE (per platform)
==================================
Metric                    | Weight | Score
--------------------------|--------|------
Event parameter accuracy  | 25%    | 0-10
User data completeness    | 25%    | 0-10
Volume reconciliation     | 20%    | 0-10
Data freshness            | 15%    | 0-10
Consent coverage          | 15%    | 0-10
--------------------------+--------+------
WEIGHTED TOTAL            | 100%   | 0-10
```

- 8-10: High quality — data is reliable for optimization
- 5-7: Moderate — some gaps but generally usable
- 3-4: Low — significant issues affecting optimization
- 0-2: Critical — data cannot be trusted

## Output Format

```yaml
data_quality:
  platform: "Google Ads"
  quality_score: 7.5
  assessment:
    event_params: { score: 8, issues: ["Value missing on 12% of purchases"] }
    user_data: { score: 7, issues: ["Phone number format inconsistent"] }
    volume_recon: { score: 8, issues: ["2% variance from CRM — acceptable"] }
    freshness: { score: 9, issues: [] }
    consent: { score: 6, issues: ["32% consent denial in EU traffic"] }
  recommendations:
    - "Normalize phone to E.164 format before sending to EC"
    - "Implement consent mode for modeled conversions in EU"
```

## Integration
- Receives tag inspection data from `tag_inspector`
- Feeds quality scores into `audit_orchestrator` for Health Score calculation
- Provides data quality section to `report_generator`
