# Meta Pixel Health Audit

## Command
`/meta pixel`

## Description
Comprehensive audit of Meta Pixel installation, standard event firing, custom event configuration, event deduplication, and data quality scoring. This skill validates that your tracking foundation is solid before analyzing performance.

## Why Pixel Health Matters

Meta Pixel is the foundation of all Meta Ads optimization. A misconfigured Pixel means:
- **Broken optimization**: Meta cannot optimize delivery without accurate conversion data
- **Inflated audiences**: Duplicate events create bloated retargeting pools
- **Wasted spend**: Without proper event tracking, budget flows to non-converting placements
- **Attribution gaps**: Missing events create holes in the conversion funnel

37% of advertisers have at least one broken Pixel event. The average account loses 15-20% of optimization signal due to Pixel misconfiguration.

## Audit Checklist (35 Points)

### 1. Pixel Installation Verification (8 points)

- [ ] **Base Pixel Code Present**: Verify `fbq('init', 'PIXEL_ID')` is on every page
- [ ] **Single Pixel Per Page**: Check for duplicate Pixel installations (common with GTM + hardcoded)
- [ ] **Pixel ID Consistency**: Ensure the same Pixel ID is used across all pages
- [ ] **Pixel Loading Order**: Pixel should fire in `<head>` before page content loads
- [ ] **No JavaScript Errors**: Check browser console for Pixel-related JS errors
- [ ] **Cross-Domain Tracking**: If multi-domain, verify first-party cookie settings
- [ ] **GTM Implementation Check**: If using GTM, verify trigger configuration and firing order
- [ ] **Pixel Helper Status**: Run Meta Pixel Helper extension and capture all warnings/errors

### 2. Standard Events Validation (10 points)

The 9 standard Meta Pixel events must be validated:

| Event | Required Parameters | Where It Should Fire |
|-------|-------------------|---------------------|
| `PageView` | None | Every page load |
| `ViewContent` | `content_ids`, `content_type`, `value`, `currency` | Product/service pages |
| `AddToCart` | `content_ids`, `content_type`, `value`, `currency` | Add to cart action |
| `InitiateCheckout` | `value`, `currency`, `num_items` | Checkout start |
| `AddPaymentInfo` | `value`, `currency` | Payment info entry |
| `Purchase` | `content_ids`, `content_type`, `value`, `currency` | Order confirmation |
| `Lead` | `value`, `currency` | Form submissions |
| `CompleteRegistration` | `value`, `currency`, `status` | Account creation |
| `Search` | `search_string`, `content_category` | Search results page |

**Validation checks per event:**
- [ ] Event fires on the correct page/action
- [ ] All required parameters are populated (not null/undefined)
- [ ] `value` parameter contains numeric data (not string "0" or empty)
- [ ] `currency` uses valid ISO 4217 code (USD, EUR, GBP, etc.)
- [ ] `content_ids` match product catalog IDs (if using catalog)
- [ ] Event fires only once per action (no duplicate triggers)

### 3. Custom Events Audit (5 points)

- [ ] **Custom Event Inventory**: List all custom events and their purpose
- [ ] **Naming Convention**: Check for consistent naming (e.g., `CustomEvent_FormStep2`)
- [ ] **Parameter Completeness**: Custom events should pass relevant parameters
- [ ] **Event Volume**: Flag custom events with < 10 fires/week (too few for optimization)
- [ ] **Redundancy Check**: Identify custom events that duplicate standard events

### 4. Event Deduplication (5 points)

Deduplication prevents double-counting when both Pixel and CAPI send the same event.

- [ ] **Event ID Implementation**: Check that `eventID` parameter is set on browser Pixel events
- [ ] **Event ID Format**: IDs should be unique per event instance (UUID or transaction ID)
- [ ] **Dedup Window**: Meta deduplicates within 48 hours — verify events have timestamps
- [ ] **Dedup Rate Monitoring**: Check Events Manager for deduplication rate (target: < 5%)
- [ ] **Cross-Channel Dedup**: If using both Pixel and CAPI, verify matching `event_id` values

### 5. Data Quality Scoring (7 points)

- [ ] **Event Match Quality (EMQ)**: Pull EMQ score from Events Manager (target: 6.0+/10)
- [ ] **Parameter Fill Rate**: Calculate % of events with all required parameters filled
- [ ] **Value Accuracy**: Spot-check `value` parameters against actual transaction values
- [ ] **Funnel Integrity**: Verify logical event sequence (PageView > ViewContent > AddToCart > Purchase)
- [ ] **Event Volume Trends**: Flag sudden drops (> 30% day-over-day) indicating tracking breaks
- [ ] **Browser vs Server Events**: Compare Pixel event count to CAPI event count (should be within 10%)
- [ ] **Test Event Verification**: Use Meta's Test Events tool to validate real-time event firing

## Scoring Methodology

| Score Range | Grade | Interpretation |
|-------------|-------|---------------|
| 90-100 | A+ | Pixel implementation is robust and complete |
| 80-89 | A | Minor parameter gaps or dedup improvements needed |
| 70-79 | B | Some events missing parameters or dedup issues |
| 60-69 | C | Multiple tracking gaps affecting optimization |
| 40-59 | D | Significant Pixel problems — optimization severely impacted |
| 0-39 | F | Critical — Pixel is broken or missing key events |

### Point Allocation
- Each checked item = full points for that item
- Partial implementation = half points
- Missing or broken = 0 points
- Total raw points converted to 0-100 scale

## Common Issues & Fixes

### Issue: Duplicate PageView Events
**Symptom**: PageView count is 2x actual page loads
**Cause**: Pixel installed both in GTM and hardcoded in page HTML
**Fix**: Remove one installation method. If using GTM, remove hardcoded Pixel.

### Issue: Purchase Event Missing Value
**Symptom**: Purchase events fire but `value` is 0 or undefined
**Cause**: Dynamic value not properly pulled from order confirmation page
**Fix**: Map `value` to order total variable in GTM or update dataLayer push.

### Issue: Event Deduplication Not Working
**Symptom**: Events Manager shows > 10% deduplication rate
**Cause**: `event_id` not matching between Pixel and CAPI events
**Fix**: Ensure identical `event_id` is passed in both browser and server events.

### Issue: ViewContent Not Firing on Product Pages
**Symptom**: ViewContent volume is much lower than product page views
**Cause**: Event trigger only fires on specific product templates, missing others
**Fix**: Update GTM trigger to fire on all product page URL patterns.

### Issue: EMQ Score Below 4.0
**Symptom**: Events Manager shows poor Event Match Quality
**Cause**: Missing customer information parameters (email, phone, external_id)
**Fix**: Pass hashed customer data via `fbq('init')` advanced matching or CAPI.

## Data Requirements

To run this audit, provide one or more of:
1. **Events Manager screenshot/export** — Shows event activity, EMQ, and dedup rates
2. **Meta Pixel Helper output** — Browser extension results showing all events on key pages
3. **GTM container export** — JSON export of Google Tag Manager configuration
4. **Website URL** — For live Pixel detection and validation
5. **Meta Business Manager access** — For API-based validation

## Output Format

```
## Pixel Health Audit Results

**Score: XX/100** (Grade: X)
**Events Tracked: X/9 standard events active**
**EMQ Score: X.X/10**
**Dedup Rate: X.X%**

### Critical Findings (P0)
- [e.g., Purchase event missing value parameter — optimization cannot work]

### High Priority (P1)
- [e.g., No event deduplication configured — inflating conversion counts]

### Medium Priority (P2)
- [e.g., Search event not implemented — missing optimization signal]

### Event Status Table
| Event | Status | Parameters | Dedup | Notes |
|-------|--------|-----------|-------|-------|
| PageView | OK | N/A | N/A | Fires correctly |
| Purchase | WARN | Missing value | No ID | Needs fix |
| ... | ... | ... | ... | ... |

### Recommendations
1. [Action item with priority and expected impact]
```
