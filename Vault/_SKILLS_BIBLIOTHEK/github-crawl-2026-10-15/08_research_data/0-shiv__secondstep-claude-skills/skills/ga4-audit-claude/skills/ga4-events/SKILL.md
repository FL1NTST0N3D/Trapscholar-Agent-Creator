# GA4 Events Audit

## Command
`/ga4 events`

## Purpose
Audit the event implementation across a GA4 property. Events are the core data unit in GA4 — every interaction, pageview, and conversion is an event. Incorrect event implementation means unreliable reporting, broken audiences, and wasted ad spend.

## GA4 Event Categories

### Automatically Collected Events
These fire without any configuration. Verify they exist in your event list:

| Event | Platform | Description |
|-------|----------|-------------|
| `first_visit` | Web + App | First time a user visits |
| `session_start` | Web + App | New session begins |
| `page_view` | Web | Page is loaded or history state changes |
| `screen_view` | App | Screen transition occurs |
| `user_engagement` | Web + App | App in foreground or web page in focus for 1+ second |
| `first_open` | App | First time app is opened |
| `app_remove` | Android | App package removed |
| `app_update` | App | App is updated to new version |
| `os_update` | App | Device OS is updated |
| `ad_click` | App | User clicks an ad (AdMob) |
| `ad_impression` | App | User sees an ad impression (AdMob) |

### Enhanced Measurement Events
Configured in Data Stream settings (see ga4-data-streams skill):

| Event | Trigger |
|-------|---------|
| `scroll` | User scrolls past 90% of page |
| `click` | User clicks outbound link |
| `view_search_results` | User performs site search |
| `video_start` | YouTube video starts playing |
| `video_progress` | YouTube video reaches 10%, 25%, 50%, 75% |
| `video_complete` | YouTube video ends |
| `file_download` | User clicks file download link |
| `form_start` | User first interacts with a form |
| `form_submit` | User submits a form |

## Audit Checklist

### 1. Event Coverage by Business Type

**E-commerce sites MUST have:**
- [ ] `view_item_list` — Product list/category page views
- [ ] `select_item` — Product click from list
- [ ] `view_item` — Product detail page view
- [ ] `add_to_wishlist` — Wishlist additions
- [ ] `add_to_cart` — Cart additions
- [ ] `remove_from_cart` — Cart removals
- [ ] `view_cart` — Cart page views
- [ ] `begin_checkout` — Checkout initiation
- [ ] `add_shipping_info` — Shipping step completion
- [ ] `add_payment_info` — Payment step completion
- [ ] `purchase` — Completed purchase with revenue
- [ ] `refund` — Refund processing

**Lead generation sites MUST have:**
- [ ] `generate_lead` — Lead form submission (with value parameter)
- [ ] `form_submit` — Any form submission
- [ ] `click` — CTA button clicks (phone, email, directions)
- [ ] `page_view` — Thank you / confirmation page
- [ ] Custom: `phone_call` — Phone number clicks
- [ ] Custom: `email_click` — Email link clicks
- [ ] Custom: `chat_start` — Live chat initiations
- [ ] Custom: `schedule_appointment` — Booking/scheduling actions

**SaaS / App businesses MUST have:**
- [ ] `sign_up` — Account creation
- [ ] `login` — User authentication
- [ ] `tutorial_begin` — Onboarding start
- [ ] `tutorial_complete` — Onboarding completion
- [ ] `purchase` or `subscribe` — Subscription/payment
- [ ] Custom: `feature_use` — Key feature engagement
- [ ] Custom: `upgrade` — Plan upgrades
- [ ] Custom: `invite_sent` — User invitations
- [ ] Custom: `api_key_created` — Developer engagement

**Content / Media sites MUST have:**
- [ ] `page_view` — Article/content views
- [ ] `scroll` — Content consumption depth
- [ ] `video_start` / `video_complete` — Video engagement
- [ ] `file_download` — Resource downloads
- [ ] `share` — Social sharing
- [ ] `search` — Content search
- [ ] Custom: `newsletter_signup` — Email subscription
- [ ] Custom: `article_read` — Read completion (custom threshold)
- [ ] Custom: `paywall_hit` — Paywall encounters (if applicable)

### 2. Event Naming Convention Validation

- [ ] All custom events use `snake_case` (e.g., `add_to_cart`, NOT `AddToCart` or `add-to-cart`)
- [ ] No event names exceed 40 characters
- [ ] All event names start with a letter (not number or special character)
- [ ] No reserved prefixes used (`firebase_`, `ga_`, `google_`, `gtag.`)
- [ ] No reserved event names used (e.g., `app_exception`, `app_store_refund`, etc.)
- [ ] Total distinct event names are under 500 limit
- [ ] Event names are descriptive and follow a consistent taxonomy
- [ ] No duplicate events with different naming (e.g., `formSubmit` AND `form_submit`)
- [ ] Events use Google's recommended names when applicable (not custom alternatives)
- [ ] No PII in event names (email addresses, user IDs in event name itself)

### 3. Event Parameter Validation

**For each event, verify parameters:**
- [ ] Required parameters are present (per Google's recommended event specs)
- [ ] Parameter names use snake_case
- [ ] Parameter names do not exceed 40 characters
- [ ] Parameter values do not exceed 100 characters
- [ ] No more than 25 custom parameters per event
- [ ] Numeric parameters use numbers (not strings of numbers)
- [ ] Currency parameters use ISO 4217 format (e.g., `USD`, `EUR`)
- [ ] No PII in parameter values (no emails, phone numbers, SSNs, etc.)

**Critical parameter checks by event:**

| Event | Required Parameters |
|-------|-------------------|
| `purchase` | `transaction_id`, `value`, `currency`, `items[]` |
| `add_to_cart` | `value`, `currency`, `items[]` |
| `view_item` | `value`, `currency`, `items[]` |
| `generate_lead` | `value`, `currency` |
| `sign_up` | `method` |
| `login` | `method` |
| `share` | `method`, `content_type`, `item_id` |
| `search` | `search_term` |
| `select_content` | `content_type`, `item_id` |

**Items array validation (for e-commerce events):**
- [ ] `item_id` is present and unique per product
- [ ] `item_name` is present
- [ ] `item_category` is populated (supports up to 5 levels: `item_category`, `item_category2`, etc.)
- [ ] `price` is a number (not a formatted string like "$19.99")
- [ ] `quantity` is present and is a positive integer
- [ ] `item_brand` is populated
- [ ] `item_variant` is used for product variations (size, color)
- [ ] `affiliation` is set if using marketplace/multi-seller model
- [ ] `coupon` is set when applicable
- [ ] `discount` is set when applicable

### 4. Event Firing Validation

- [ ] Events fire at the correct trigger point (not too early, not too late)
- [ ] Events fire exactly once per action (no duplicate firing)
- [ ] Events are not firing on page load when they should fire on user action
- [ ] Events fire on all relevant pages/screens (not just some)
- [ ] Events are visible in GA4 Realtime report within 30 seconds of firing
- [ ] Event count in GA4 matches expected count from GTM debug mode
- [ ] No events fire on error pages (404, 500) unless intentionally tracked
- [ ] Events respect consent state (do not fire when analytics consent is denied)

### 5. Debug Mode Validation

- [ ] GA4 DebugView is accessible (Admin > DebugView)
- [ ] Debug mode can be activated via GTM Preview mode
- [ ] Debug mode can be activated via Chrome GA Debugger extension
- [ ] Events appear in DebugView with correct parameters
- [ ] No excessive events flooding DebugView (indicates duplicate firing)
- [ ] User properties appear correctly in DebugView

### 6. Event Modification Rules

- [ ] Event modifications are documented (Admin > Events > Modify event)
- [ ] Created events are documented (Admin > Events > Create event)
- [ ] No conflicting modification rules exist
- [ ] Modification rules are not breaking existing event data
- [ ] Created events have proper conditions and parameters

## Common Issues Found

1. **Missing recommended event parameters** — `purchase` event without `transaction_id` causes duplicate revenue counting.
2. **String values for numeric parameters** — `price: "19.99"` instead of `price: 19.99` breaks revenue calculations.
3. **PII in event parameters** — Email addresses or phone numbers in custom parameters violate Google's TOS and can cause property suspension.
4. **Duplicate event firing** — Same event fires from both GTM and gtag.js hardcoded on the page.
5. **Custom events replacing recommended events** — Using `form_complete` instead of Google's recommended `generate_lead` loses reporting features.
6. **Exceeding 500 event name limit** — Dynamic event names (e.g., `click_button_123`) consuming the 500 distinct event quota.
7. **Missing currency parameter** — Revenue events without `currency` default to the property's currency, causing miscalculation for multi-currency sites.
8. **Events firing before consent** — Analytics events firing before user grants consent, violating GDPR/CCPA.

## Scoring

| Check Area | Points | Weight |
|-----------|--------|--------|
| Event coverage | 30 | 30% |
| Naming conventions | 20 | 20% |
| Parameter validation | 25 | 25% |
| Firing validation | 15 | 15% |
| Debug & modification | 10 | 10% |

**Score = (passed_points / total_applicable_points) * 100**

## Output Format

```
## Events Audit

**Score: XX/100**

### Event Summary
- Total distinct events: [count] / 500 limit
- Automatically collected: [count]
- Enhanced measurement: [count]
- Recommended events: [count]
- Custom events: [count]

### Business Type: [E-commerce / Lead Gen / SaaS / Content]

### Event Coverage
| Recommended Event | Status | Parameters Valid |
|------------------|--------|-----------------|
| event_name | Present/Missing | Yes/No/Partial |

### Naming Issues
| Event | Issue | Fix |
|-------|-------|-----|
| EventName | Not snake_case | Rename to event_name |

### Parameter Issues
| Event | Parameter | Issue | Fix |
|-------|-----------|-------|-----|
| purchase | currency | Missing | Add currency: "USD" |

### Findings
[Passed/Failed/Warning items with fix instructions]
```
