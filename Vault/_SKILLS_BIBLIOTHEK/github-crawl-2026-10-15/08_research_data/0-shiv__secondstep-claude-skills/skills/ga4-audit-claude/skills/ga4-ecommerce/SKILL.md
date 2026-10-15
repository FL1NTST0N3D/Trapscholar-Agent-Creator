# GA4 E-commerce Audit

## Command
`/ga4 ecommerce`

## Purpose
Audit the e-commerce event implementation in GA4. E-commerce tracking is the most complex and highest-value tracking implementation — it directly measures revenue, product performance, and purchase funnel efficiency. When e-commerce tracking is broken, you cannot trust revenue data, product reports are useless, and Google Ads Smart Bidding receives garbage signals. An estimated 67% of GA4 e-commerce implementations have at least one critical flaw.

## E-commerce Event Funnel

GA4 e-commerce follows a defined funnel of events, each building on the previous step. All events use the `items` array parameter to pass product data.

### Complete E-commerce Event Flow

```
view_item_list → select_item → view_item → add_to_wishlist
                                          → add_to_cart → remove_from_cart
                                                        → view_cart → begin_checkout
                                                                    → add_shipping_info
                                                                    → add_payment_info
                                                                    → purchase → refund
```

**Promotion events (parallel flow):**
```
view_promotion → select_promotion
```

## Audit Checklist

### 1. Event Implementation — Required Events

Each event below has required and recommended parameters. The audit checks both presence and correctness.

**`view_item_list` — Product listing / category page:**
- [ ] Event fires on all product listing pages (category, search results, collections)
- [ ] Parameters: `item_list_id`, `item_list_name`, `items[]`
- [ ] Items array contains all visible products (or at least the first viewport)
- [ ] Fires once per page load (not per product)
- [ ] Does NOT fire on non-product list pages

**`select_item` — Product click from list:**
- [ ] Event fires when user clicks a product from a list
- [ ] Parameters: `item_list_id`, `item_list_name`, `items[]` (single item)
- [ ] Carries the list context (which list the product was clicked from)
- [ ] Fires before navigation to product page

**`view_item` — Product detail page:**
- [ ] Event fires on every product detail page view
- [ ] Parameters: `currency`, `value`, `items[]` (single item)
- [ ] `value` matches the product price
- [ ] `currency` is set (ISO 4217: USD, EUR, GBP, etc.)
- [ ] Fires once per page load
- [ ] All item parameters are populated (id, name, category, price, brand)

**`add_to_wishlist` — Wishlist addition:**
- [ ] Event fires when user adds product to wishlist (if feature exists)
- [ ] Parameters: `currency`, `value`, `items[]`
- [ ] Skip this check if site has no wishlist functionality

**`add_to_cart` — Cart addition:**
- [ ] Event fires on every add-to-cart action
- [ ] Parameters: `currency`, `value`, `items[]`
- [ ] `value` = price * quantity for the added item(s)
- [ ] `quantity` is correct in items array
- [ ] Fires on quick-add, modal-add, and PDP add (all add-to-cart methods)
- [ ] Does NOT fire on page load of cart page

**`remove_from_cart` — Cart removal:**
- [ ] Event fires when item is removed from cart
- [ ] Parameters: `currency`, `value`, `items[]`
- [ ] Value reflects the removed item(s)

**`view_cart` — Cart page view:**
- [ ] Event fires when cart page is viewed
- [ ] Parameters: `currency`, `value`, `items[]`
- [ ] `value` = total cart value
- [ ] `items[]` contains ALL items in cart
- [ ] Fires once per cart page load

**`begin_checkout` — Checkout initiation:**
- [ ] Event fires when checkout process starts
- [ ] Parameters: `currency`, `value`, `coupon`, `items[]`
- [ ] `value` = total checkout value (may include shipping/tax or not — be consistent)
- [ ] `coupon` is populated if a coupon code is applied
- [ ] Fires exactly once per checkout initiation (not on every checkout step)

**`add_shipping_info` — Shipping step:**
- [ ] Event fires when user completes shipping information
- [ ] Parameters: `currency`, `value`, `coupon`, `shipping_tier`, `items[]`
- [ ] `shipping_tier` indicates the shipping method chosen (e.g., "Ground", "Express", "Free")
- [ ] Fires after shipping form submission, not on page load

**`add_payment_info` — Payment step:**
- [ ] Event fires when user enters payment information
- [ ] Parameters: `currency`, `value`, `coupon`, `payment_type`, `items[]`
- [ ] `payment_type` indicates payment method (e.g., "Credit Card", "PayPal", "Apple Pay")
- [ ] Fires after payment info entry, not on page load
- [ ] Does NOT fire if payment is declined (only on successful submission)

**`purchase` — Completed purchase:**
- [ ] Event fires on order confirmation / thank-you page
- [ ] Parameters: `transaction_id`, `value`, `currency`, `tax`, `shipping`, `coupon`, `items[]`
- [ ] `transaction_id` is UNIQUE per order (critical for deduplication)
- [ ] `value` = order total (typically including tax and shipping)
- [ ] `currency` is set correctly
- [ ] `tax` and `shipping` are numeric values
- [ ] Items array contains all purchased items with correct quantities
- [ ] Event fires ONCE per purchase (not on page refresh)
- [ ] Event does NOT fire on failed/pending payments
- [ ] `transaction_id` is consistent with backend order system

**`refund` — Order refund:**
- [ ] Event fires when refund is processed (may be server-side)
- [ ] Parameters: `transaction_id`, `value`, `currency`, `items[]`
- [ ] `transaction_id` matches the original purchase transaction_id
- [ ] For full refunds: all items included, value matches original
- [ ] For partial refunds: only refunded items included, value matches refund amount

### 2. Items Array Validation

The `items` array is the backbone of e-commerce tracking. Validate for EVERY e-commerce event:

| Parameter | Required | Format | Notes |
|-----------|----------|--------|-------|
| `item_id` | Yes | String | Unique product SKU/ID, consistent across events |
| `item_name` | Yes | String | Product name, consistent across events |
| `affiliation` | No | String | Store or channel name |
| `coupon` | No | String | Product-level coupon code |
| `discount` | No | Number | Discount amount |
| `index` | No | Number | Position in list (for list events) |
| `item_brand` | Recommended | String | Brand name |
| `item_category` | Recommended | String | Primary category |
| `item_category2` | No | String | Sub-category level 2 |
| `item_category3` | No | String | Sub-category level 3 |
| `item_category4` | No | String | Sub-category level 4 |
| `item_category5` | No | String | Sub-category level 5 |
| `item_list_id` | No | String | List identifier |
| `item_list_name` | No | String | List name |
| `item_variant` | No | String | Size, color, variant |
| `location_id` | No | String | Physical location |
| `price` | Yes | Number | Unit price (number, NOT string) |
| `quantity` | Yes | Number | Quantity (positive integer) |

**Critical item checks:**
- [ ] `item_id` is consistent across all events for the same product
- [ ] `item_name` is consistent across all events for the same product
- [ ] `price` is a number, not a formatted string (19.99, NOT "$19.99")
- [ ] `price` does not include tax or shipping
- [ ] `quantity` is always a positive integer
- [ ] At least `item_id` OR `item_name` is present (one is required)
- [ ] Items array is not empty on any e-commerce event
- [ ] Items array does not exceed 200 items per event (GA4 limit)

### 3. Revenue Validation

- [ ] Total `purchase` event revenue in GA4 approximately matches backend revenue (within 5-10%)
- [ ] No $0 purchases recorded (unless legitimate free orders)
- [ ] No abnormally high purchase values (test transactions in production)
- [ ] Revenue currency is consistent across all events
- [ ] Refund events correctly reduce total revenue
- [ ] Tax and shipping values are reasonable and consistent

### 4. Funnel Completeness

Check the funnel for data leaks:
- [ ] `view_item` count >= `add_to_cart` count (logical flow)
- [ ] `add_to_cart` count >= `begin_checkout` count
- [ ] `begin_checkout` count >= `purchase` count
- [ ] No step has 0 events while adjacent steps have data
- [ ] Funnel conversion rates are within expected ranges:
  - view_item to add_to_cart: 5-15% typical
  - add_to_cart to begin_checkout: 30-60% typical
  - begin_checkout to purchase: 40-70% typical

### 5. Promotion Tracking

- [ ] `view_promotion` fires when promotions are displayed (banners, hero images, sale sections)
- [ ] `select_promotion` fires when user clicks a promotion
- [ ] Parameters: `creative_name`, `creative_slot`, `promotion_id`, `promotion_name`
- [ ] Promotion events link to correct landing pages

## Common Issues Found

1. **Missing `transaction_id`** — Without it, page refreshes on confirmation page create duplicate purchases. Revenue is inflated.
2. **Price as string** — `"$19.99"` instead of `19.99` breaks revenue calculations. GA4 silently drops non-numeric values.
3. **Inconsistent `item_id`** — Same product has different IDs in `view_item` vs `purchase`, breaking product reports.
4. **Purchase fires on page load** — Confirmation page reloads or back-button navigation triggers duplicate purchase events.
5. **Missing currency** — Events default to property currency, causing errors for multi-currency sites.
6. **Empty items array** — E-commerce events fire but with empty `items[]`, making product reports useless.
7. **Cart value mismatch** — `begin_checkout` value does not equal sum of item prices * quantities.
8. **Checkout funnel gaps** — `begin_checkout` fires but `add_shipping_info` and `add_payment_info` are missing entirely.

## Scoring

| Check Area | Points | Weight |
|-----------|--------|--------|
| Event implementation | 35 | 35% |
| Items array | 25 | 25% |
| Revenue validation | 20 | 20% |
| Funnel completeness | 15 | 15% |
| Promotion tracking | 5 | 5% |

**Score = (passed_points / total_applicable_points) * 100**

## Output Format

```
## E-commerce Audit

**Score: XX/100**

### E-commerce Funnel
| Event | Status | Event Count (28d) | Parameters Valid |
|-------|--------|-------------------|-----------------|
| view_item_list | Present | X | Yes/Partial/No |
| select_item | Present/Missing | X | - |
| view_item | Present | X | Yes/Partial/No |
| add_to_cart | Present | X | Yes/Partial/No |
| begin_checkout | Present | X | Yes/Partial/No |
| purchase | Present | X | Yes/Partial/No |

### Revenue Summary
- GA4 Revenue (28d): $X
- Backend Revenue (28d): $X (if provided)
- Discrepancy: X%

### Items Array Issues
| Event | Parameter | Issue |
|-------|-----------|-------|
| purchase | price | String instead of number |

### Findings
[Passed/Failed/Warning items with fix instructions]
```
