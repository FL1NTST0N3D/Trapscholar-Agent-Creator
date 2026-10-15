# GA4 Audiences Audit

## Command
`/ga4 audiences`

## Purpose
Audit audience configuration in GA4. Audiences define user segments for analysis and remarketing. Properly configured audiences power Google Ads remarketing, enable predictive targeting, and provide critical segmentation for reporting. Most GA4 properties drastically underutilize audience capabilities.

## GA4 Audience Fundamentals

**Key concepts:**
- Audiences are retroactively populated (up to 30 days of historical data when created)
- Audiences refresh automatically as users meet/fail conditions
- Maximum 100 audiences per property
- Audiences shared with Google Ads update in near real-time
- Audience membership duration: 1 to 540 days (default 30 days)
- Users are added to audiences based on the identity space configured (User ID, Google Signals, Device ID)

## Audit Checklist

### 1. Essential Audiences

Every GA4 property should have these foundational audiences regardless of business type:

- [ ] **All Users** — Default audience, always present
- [ ] **Purchasers / Converters** — Users who completed a key conversion
- [ ] **Non-Purchasers / Non-Converters** — Users who visited but did not convert
- [ ] **Cart Abandoners** — Users who added to cart but did not purchase (e-commerce)
- [ ] **High-Value Users** — Users above a revenue or engagement threshold
- [ ] **Engaged Users** — Users with above-average engagement time or session count
- [ ] **New Users (7 days)** — Users whose first visit was within last 7 days
- [ ] **Returning Users** — Users with 2+ sessions
- [ ] **Churned Users** — Users who have not returned in X days

**Business-type specific audiences:**

*E-commerce:*
- [ ] Viewed product but didn't add to cart
- [ ] Added to cart but didn't checkout
- [ ] Started checkout but didn't purchase
- [ ] Purchased 1x (first-time buyers)
- [ ] Purchased 2+ times (repeat buyers)
- [ ] High AOV purchasers (above median order value)
- [ ] Category-specific browsers (by item_category)
- [ ] Discount/coupon users

*Lead generation:*
- [ ] Visited key landing pages but didn't submit form
- [ ] Submitted form (leads)
- [ ] Qualified leads (if post-form qualification exists)
- [ ] Visited pricing page
- [ ] Downloaded resources / viewed case studies
- [ ] Multi-page visitors (3+ pages, high intent)

*SaaS:*
- [ ] Signed up but didn't activate
- [ ] Active users (used key feature in last 7 days)
- [ ] Inactive users (no activity in 14+ days)
- [ ] Free trial users approaching expiration
- [ ] Upgraded users
- [ ] Power users (above-average feature usage)

### 2. Predictive Audiences

GA4 offers machine learning-based predictive audiences. These require sufficient data volume to activate.

**Available predictive metrics:**
- `purchase_probability` — Probability of purchase in next 7 days
- `churn_probability` — Probability of NOT returning in next 7 days
- `predicted_revenue` — Expected revenue from user in next 28 days

**Prerequisite checks:**
- [ ] Property has 1,000+ returning users who triggered the relevant predictive condition in the last 28 days
- [ ] Property has 1,000+ returning users who did NOT trigger the condition
- [ ] Model quality is sustained for a period of time
- [ ] Predictive metrics are available in Audience Builder (if prerequisites met)

**Predictive audience configuration:**
- [ ] "Likely 7-day purchasers" audience is created (if eligible)
- [ ] "Likely 7-day churning users" audience is created (if eligible)
- [ ] "Predicted top spenders" audience is created (if eligible)
- [ ] Predictive audiences are exported to Google Ads for Smart Bidding signals
- [ ] Predictive audiences are used in Explorations for analysis

### 3. Audience Triggers

Audience triggers fire an event when a user joins an audience. This enables conversion tracking based on audience membership.

- [ ] Audience triggers are configured for key audiences (e.g., trigger event when user becomes a "high-value user")
- [ ] Triggered events are named following GA4 conventions (snake_case, descriptive)
- [ ] Triggered events are optionally marked as conversions if appropriate
- [ ] Audience trigger logging is not excessive (avoid triggering on high-volume audiences)

### 4. Membership Duration

The membership duration determines how long a user stays in an audience after meeting the conditions.

- [ ] Membership duration is set appropriately for each audience (not all at default 30 days)
- [ ] Remarketing audiences match the business buying cycle:
  - E-commerce: 7-30 days for cart abandoners, 30-90 for browsers
  - Lead gen: 30-90 days (longer consideration cycle)
  - SaaS: 14-30 days for trial users, 90+ for churned users
  - High-ticket B2B: 90-180 days
- [ ] Maximum 540-day membership is used for long-cycle audiences
- [ ] Short-duration audiences (1-7 days) exist for time-sensitive remarketing

### 5. Exclusion Conditions

Well-built audiences include exclusion logic to prevent wasting ad spend.

- [ ] Purchaser audiences exclude users who already purchased (for acquisition campaigns)
- [ ] Lead audiences exclude users who already submitted a form
- [ ] Remarketing audiences exclude recent converters (configurable window)
- [ ] Employee/internal traffic is excluded via user property or audience condition
- [ ] Bot/spam users are excluded where identifiable

### 6. Audience Export to Google Ads

- [ ] GA4 property is linked to Google Ads
- [ ] Key audiences are being shared with Google Ads
- [ ] Audience list sizes are sufficient for Google Ads usage (minimum 1,000 users for Search, 100 for Display)
- [ ] Audiences are visible in Google Ads Audience Manager
- [ ] Audience membership is updating (check Ads audience size trends)
- [ ] Similar/Lookalike audiences are being leveraged in campaigns (Google Ads auto-generates these)

### 7. Audience Hygiene

- [ ] No duplicate audiences with overlapping conditions
- [ ] Unused audiences are deleted or archived (reduce clutter)
- [ ] Audience names are descriptive and follow a naming convention
- [ ] Audience descriptions explain the business purpose
- [ ] Total audience count is well under the 100 limit
- [ ] Complex audiences are documented (conditions, logic, purpose)

## Common Issues Found

1. **No custom audiences created** — Only default "All Users" audience exists, missing all remarketing opportunities.
2. **All audiences at 30-day default duration** — Cart abandoner audience at 30 days is too long; churned user audience at 30 days is too short.
3. **No exclusion conditions** — Remarketing to users who already purchased, wasting ad spend.
4. **Predictive audiences not explored** — Property has enough data for predictive audiences but they were never created.
5. **Audiences not exported to Google Ads** — Audiences created in GA4 but not shared with linked Google Ads account.
6. **Overlapping audience definitions** — Multiple audiences capturing the same users with slight variations, creating confusion.
7. **No audience triggers configured** — Missing the ability to track when users enter key segments.
8. **Audience sizes too small for Ads** — Audiences defined too narrowly, falling below Google Ads minimum thresholds.

## Scoring

| Check Area | Points | Weight |
|-----------|--------|--------|
| Essential audiences | 25 | 25% |
| Predictive audiences | 15 | 15% |
| Audience triggers | 10 | 10% |
| Membership duration | 15 | 15% |
| Exclusion conditions | 15 | 15% |
| Google Ads export | 15 | 15% |
| Hygiene | 5 | 5% |

**Score = (passed_points / total_applicable_points) * 100**

## Output Format

```
## Audiences Audit

**Score: XX/100**

### Audience Inventory
- Total audiences: [count] / 100 limit
- Exported to Google Ads: [count]
- Predictive audiences available: Yes/No
- Predictive audiences created: [count]

### Essential Audiences
| Audience | Status | Duration | Ads Export |
|----------|--------|----------|-----------|
| All Users | Present | - | Yes |
| Purchasers | Present/Missing | 30d | Yes/No |

### Findings
[Passed/Failed/Warning items with fix instructions]
```
