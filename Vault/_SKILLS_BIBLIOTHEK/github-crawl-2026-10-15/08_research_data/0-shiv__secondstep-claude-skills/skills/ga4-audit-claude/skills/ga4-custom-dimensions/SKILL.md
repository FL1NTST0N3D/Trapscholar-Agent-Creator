# GA4 Custom Dimensions Audit

## Command
`/ga4 dimensions`

## Purpose
Audit custom dimension and custom metric registration in GA4. Custom dimensions extend GA4's built-in dimensions with business-specific data, enabling deeper segmentation and analysis. Only 12% of GA4 properties use custom dimensions properly — most either ignore them entirely or register them incorrectly, leaving valuable data uncollected or inaccessible in reports.

## GA4 Custom Dimensions Fundamentals

### Scope Types

**Event-scoped custom dimensions:**
- Describe something about a specific event
- Value is set per event via event parameters
- Example: `content_type`, `author_name`, `form_name`, `product_color`
- Quota: 50 event-scoped custom dimensions (standard), 125 (GA4 360)

**User-scoped custom dimensions:**
- Describe something about the user
- Value persists across sessions until changed
- Set via `user_properties` in gtag or GTM
- Example: `membership_level`, `customer_type`, `preferred_language`, `signup_source`
- Quota: 25 user-scoped custom dimensions (standard), 100 (GA4 360)

**Item-scoped custom dimensions:**
- Describe something about an e-commerce item in the `items` array
- Example: `item_color`, `item_size`, `item_rating`
- Quota: 10 item-scoped custom dimensions (standard), 25 (GA4 360)

### Custom Metrics

Custom metrics are numeric values attached to events that can be aggregated in reports.
- Quota: 50 custom metrics (standard), 125 (GA4 360)
- Example: `discount_amount`, `session_score`, `content_word_count`

## Audit Checklist

### 1. Dimension Registration

Custom dimensions must be registered in Admin > Custom definitions before they appear in reports.

- [ ] All event parameters intended for reporting are registered as custom dimensions
- [ ] All user properties intended for reporting are registered as custom dimensions
- [ ] Registration matches the correct scope (event-scoped vs user-scoped)
- [ ] Dimension names are descriptive (not cryptic parameter names)
- [ ] No duplicate registrations (same parameter registered twice)
- [ ] Description field is populated for each dimension (for team clarity)

**Critical check: Unregistered parameters**
- [ ] Review events in DebugView — any parameters NOT registered as custom dimensions are available only in BigQuery raw export, not in GA4 reports or Explorations
- [ ] List all event parameters being sent and cross-reference with registered dimensions
- [ ] Identify "data loss" — parameters being collected but not accessible in the GA4 UI

### 2. Quota Usage

- [ ] Event-scoped dimensions used: [X] / 50 (standard) or / 125 (360)
- [ ] User-scoped dimensions used: [X] / 25 (standard) or / 100 (360)
- [ ] Item-scoped dimensions used: [X] / 10 (standard) or / 25 (360)
- [ ] Custom metrics used: [X] / 50 (standard) or / 125 (360)
- [ ] Sufficient headroom exists for future needs (recommend keeping 20% buffer)
- [ ] No quota slots wasted on dimensions that are never used in reports

### 3. Recommended Custom Dimensions by Business Type

**All businesses:**
- [ ] `logged_in_status` (user-scoped) — Whether user is authenticated
- [ ] `user_type` (user-scoped) — Customer, prospect, employee, etc.
- [ ] `traffic_type` (event-scoped) — Internal, bot, test (for filtering)
- [ ] `page_type` (event-scoped) — Homepage, category, product, blog, checkout
- [ ] `content_group` (event-scoped) — Content categorization

**E-commerce:**
- [ ] `customer_type` (user-scoped) — New vs returning customer
- [ ] `membership_tier` (user-scoped) — Loyalty program level
- [ ] `payment_method` (event-scoped) — Credit card, PayPal, etc.
- [ ] `shipping_method` (event-scoped) — Ground, express, free
- [ ] `coupon_used` (event-scoped) — Boolean or coupon code
- [ ] `product_margin` (event-scoped, custom metric) — For profitability analysis
- [ ] `stock_status` (item-scoped) — In stock, low stock, out of stock

**Lead generation:**
- [ ] `lead_source` (event-scoped) — Which form, page, or CTA generated the lead
- [ ] `lead_quality` (event-scoped) — Score or tier if available from backend
- [ ] `service_interest` (event-scoped) — What service/product the lead is interested in
- [ ] `form_name` (event-scoped) — Which form was submitted
- [ ] `form_location` (event-scoped) — Where on the page the form was (header, sidebar, popup)

**SaaS:**
- [ ] `plan_type` (user-scoped) — Free, starter, pro, enterprise
- [ ] `trial_status` (user-scoped) — Active trial, expired, converted
- [ ] `feature_name` (event-scoped) — Which feature was used
- [ ] `workspace_size` (user-scoped) — Team size or usage tier
- [ ] `days_since_signup` (event-scoped) — Lifecycle stage indicator
- [ ] `activation_status` (user-scoped) — Has user completed key activation steps

**Content / Media:**
- [ ] `author` (event-scoped) — Content author
- [ ] `publish_date` (event-scoped) — When content was published
- [ ] `content_category` (event-scoped) — Topic or section
- [ ] `word_count` (event-scoped, custom metric) — Article length
- [ ] `subscriber_status` (user-scoped) — Free, premium, churned

### 4. Parameter-to-Dimension Mapping

Verify the mapping between event parameters and registered dimensions is correct:

- [ ] Each registered dimension maps to the correct event parameter name (case-sensitive)
- [ ] Parameter names in GTM/gtag match exactly what is registered in GA4
- [ ] No typos or case mismatches between implementation and registration
- [ ] Data type is correct (text dimensions should not receive numeric-only values if a custom metric is more appropriate)
- [ ] Verify data is flowing by checking recent values in Explorations

### 5. Data Quality Checks

- [ ] Custom dimensions are receiving data (not all `(not set)`)
- [ ] Value cardinality is appropriate:
  - User-scoped: Usually low cardinality (<100 distinct values)
  - Event-scoped: Can be higher but should not exceed 500+ distinct values (causes "other" row in reports)
- [ ] No PII is stored in custom dimensions (emails, phone numbers, names)
- [ ] Values are clean and normalized (no inconsistent casing, encoding, or formatting)
- [ ] Enum-style dimensions have a controlled vocabulary (not free-text user input)

### 6. Custom Metrics Validation

- [ ] Custom metrics are registered for numeric values that need aggregation
- [ ] Measurement unit is correctly set (Standard, Currency, Distance, Time)
- [ ] Currency metrics use proper decimal values (not cents)
- [ ] Metrics are not used where dimensions are more appropriate (and vice versa)
- [ ] Metrics are receiving data and values are within expected ranges

### 7. BigQuery Export Alignment

If using BigQuery export:
- [ ] All custom dimensions registered in GA4 are also available in BigQuery export
- [ ] Unregistered parameters are accessible only via BigQuery (if BQ export is configured)
- [ ] BigQuery schema matches expected parameter names
- [ ] Consider: If a parameter is only needed in BigQuery (not in GA4 UI), it does NOT need to be registered as a custom dimension (saves quota)

## Common Issues Found

1. **Unregistered parameters** — Events send parameters that are never registered, making the data inaccessible in GA4 reports. The data is silently lost (unless BigQuery export is enabled).
2. **Wrong scope** — A user-level attribute (like `customer_type`) registered as event-scoped, or an event attribute (like `form_name`) registered as user-scoped.
3. **Quota exhaustion** — All 50 event-scoped slots used, no room for new dimensions. Often caused by registering parameters that are never actually used in reports.
4. **PII in dimensions** — Email addresses or names stored as custom dimensions, violating Google's Terms of Service and risking property suspension.
5. **High cardinality dimensions** — Dimensions with thousands of unique values (like user IDs or URLs) cause "(other)" rows and degrade report performance.
6. **Case mismatches** — Parameter `formName` in GTM but `form_name` registered in GA4 — dimension shows all `(not set)`.
7. **Missing descriptions** — Dimensions registered without descriptions, causing confusion months later when no one remembers what `cd7` was supposed to track.
8. **Unused dimensions consuming quota** — Dimensions registered months ago for a since-removed feature, wasting precious quota slots.

## Scoring

| Check Area | Points | Weight |
|-----------|--------|--------|
| Registration completeness | 25 | 25% |
| Quota management | 15 | 15% |
| Business-type coverage | 25 | 25% |
| Data quality | 20 | 20% |
| Custom metrics | 10 | 10% |
| Documentation | 5 | 5% |

**Score = (passed_points / total_applicable_points) * 100**

## Output Format

```
## Custom Dimensions Audit

**Score: XX/100**

### Quota Usage
| Scope | Used | Limit | Available |
|-------|------|-------|-----------|
| Event-scoped | X | 50 | X |
| User-scoped | X | 25 | X |
| Item-scoped | X | 10 | X |
| Custom metrics | X | 50 | X |

### Registered Dimensions
| Name | Scope | Parameter | Receiving Data |
|------|-------|-----------|---------------|
| Page Type | Event | page_type | Yes/No |

### Unregistered Parameters (Data Loss)
| Event | Parameter | Recommended Scope |
|-------|-----------|------------------|
| form_submit | form_name | Event-scoped |

### Missing Recommended Dimensions
| Dimension | Scope | Business Value |
|-----------|-------|---------------|
| customer_type | User | Segment new vs returning |

### Findings
[Passed/Failed/Warning items with fix instructions]
```
