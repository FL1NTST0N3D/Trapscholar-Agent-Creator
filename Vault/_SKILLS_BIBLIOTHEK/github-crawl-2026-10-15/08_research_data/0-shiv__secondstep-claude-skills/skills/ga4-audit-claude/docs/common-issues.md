# Common GA4 Issues & Fixes

A reference of the most frequently encountered GA4 misconfiguration issues, organized by severity.

## Critical Issues

### 1. No Conversion Events Configured
**Symptom:** Zero conversions in reports. Google Ads Smart Bidding has no optimization signal.
**Fix:** Mark key events as conversions in Admin > Events. For e-commerce, `purchase` must be a conversion. For lead gen, `generate_lead` or form submission events.
**Impact:** Google Ads campaigns cannot optimize. ROI is unmeasurable.

### 2. Duplicate Purchase Events
**Symptom:** Revenue in GA4 is 1.5-2x higher than actual revenue. Transaction count exceeds order count.
**Fix:** Implement transaction deduplication:
1. Use unique `transaction_id` parameter on `purchase` event
2. Prevent `purchase` event from firing on page refresh (check if already fired for this transaction ID)
3. Use server-side tracking or a data layer flag to prevent re-firing

### 3. PII in Event Parameters
**Symptom:** Email addresses, phone numbers, or names visible in event parameters.
**Fix:** Immediately stop sending PII. Audit all custom event parameters and data layer pushes. Remove PII from GTM variables. Note: Google may suspend properties that collect PII.
**Risk:** Terms of Service violation, potential property suspension, GDPR/CCPA liability.

### 4. Price Sent as String Instead of Number
**Symptom:** Revenue reports show $0 or are empty despite `purchase` events firing.
**Fix:** Change data layer to send `price: 19.99` instead of `price: "$19.99"`. Ensure all monetary values are numeric types without currency symbols.

### 5. Missing Consent Mode Implementation
**Symptom:** EU/UK traffic not tracked, or tracked non-compliantly.
**Fix:** Implement Consent Mode v2 with a certified CMP (Cookiebot, OneTrust, etc.). Set default consent state to `denied` for EU users. Enable behavioral modeling.

## High Priority Issues

### 6. Data Retention Set to 2 Months
**Symptom:** Explorations cannot access data older than 2 months. Year-over-year analysis impossible in Explorations.
**Fix:** Admin > Data Settings > Data Retention > Change to 14 months. Enable "Reset user data on new activity."
**Note:** This does NOT affect standard reports (they use aggregated data). Only affects Explorations.

### 7. Internal Traffic Filter in Testing Mode
**Symptom:** Employee visits inflate traffic and skew engagement metrics. Filter exists but is not active.
**Fix:** Admin > Data Settings > Data Filters > Change filter status from "Testing" to "Active." Verify IP addresses are correct first by checking Testing mode data.

### 8. Google Ads Not Linked
**Symptom:** No Google Ads data in GA4 acquisition reports. Cannot import GA4 conversions into Google Ads.
**Fix:** Admin > Google Ads Links > Link. Requires admin access to both GA4 and Google Ads.

### 9. Missing Recommended Events
**Symptom:** Business-critical actions are not tracked. E-commerce sites missing `add_to_cart`, `begin_checkout`. Lead gen sites missing `generate_lead`.
**Fix:** Implement recommended events via GTM or gtag.js. Follow Google's recommended event specifications exactly.

### 10. Auto-Tagging Disabled in Google Ads
**Symptom:** Google Ads traffic appears as `(organic)` or `(direct)` in GA4. GCLID parameter not appended to ad click URLs.
**Fix:** Google Ads > Settings > Account Settings > Auto-tagging > Enable.

## Medium Priority Issues

### 11. Cross-Domain Tracking Not Configured
**Symptom:** Users navigating between owned domains start new sessions. Self-referrals appear in traffic reports.
**Fix:** Configure cross-domain tracking in GA4 Data Stream > Configure tag settings > Configure your domains. Add all owned domains.

### 12. Payment Gateway Referrals
**Symptom:** PayPal, Stripe, or other payment processors appear as referral sources. Attribution is broken for purchases that redirect through a payment gateway.
**Fix:** Add payment gateway domains to unwanted referrals list in Data Stream > Configure tag settings > List unwanted referrals.

### 13. Enhanced Measurement Defaults Not Reviewed
**Symptom:** Video engagement tracking enabled on sites with no videos. Site search tracking enabled but using wrong search parameter.
**Fix:** Review each Enhanced Measurement toggle in Data Stream settings. Disable features that don't apply. Configure custom search parameters if needed.

### 14. Custom Dimensions Not Registered
**Symptom:** Event parameters are sent via data layer but don't appear in GA4 reports or Explorations.
**Fix:** Register parameters as custom dimensions in Admin > Custom definitions > Custom dimensions. Match the exact parameter name (case-sensitive).

### 15. Multiple Web Streams for Same Site
**Symptom:** Duplicate events, inflated user counts, inconsistent data.
**Fix:** Delete extra web streams. Keep only ONE web stream per website. Multiple streams are only appropriate for completely separate sites in the same property.

## Low Priority Issues

### 16. No Audiences Created
**Symptom:** Only "All Users" audience exists. No remarketing segments available for Google Ads.
**Fix:** Create audiences for key segments (purchasers, cart abandoners, high-value users, etc.) in Admin > Audiences.

### 17. BigQuery Export Not Enabled
**Symptom:** Cannot perform unsampled analysis. Cannot access raw event-level data via SQL.
**Fix:** Link BigQuery in Admin > BigQuery Links. Requires a GCP project with billing enabled.

### 18. No Explorations Created
**Symptom:** Team relies only on standard reports. Cannot perform funnel analysis, path analysis, or advanced segmentation.
**Fix:** Create key explorations: purchase funnel, user path analysis, cohort retention, segment overlap.

### 19. Event Naming Inconsistencies
**Symptom:** Mix of naming conventions (`addToCart`, `add_to_cart`, `Add_To_Cart`). Same action tracked with different event names.
**Fix:** Standardize all custom event names to snake_case. Update GTM tags and data layer pushes.

### 20. Attribution Model at Default
**Symptom:** Attribution model was never explicitly chosen. May be on data-driven or last-click without a conscious decision.
**Fix:** Review in Admin > Attribution Settings. Choose data-driven for most properties. Set lookback windows appropriate for business buying cycle.
