# GA4 Event Reference

Complete reference of all Google Analytics 4 event types, their parameters, and implementation requirements.

## Automatically Collected Events

These events are collected automatically by GA4 without any additional configuration.

### Web Events

| Event | Description | Key Parameters |
|-------|-------------|---------------|
| `first_visit` | First time user visits the site | — |
| `session_start` | New session begins | `session_id` |
| `page_view` | Page loads or history state changes | `page_location`, `page_referrer`, `page_title` |
| `user_engagement` | Page was in focus for 1+ second | `engagement_time_msec` |
| `click` | Outbound link click (Enhanced Measurement) | `link_domain`, `link_url`, `outbound` |
| `scroll` | 90% page scroll (Enhanced Measurement) | — |
| `view_search_results` | Site search performed (Enhanced Measurement) | `search_term` |
| `file_download` | File link click (Enhanced Measurement) | `file_name`, `file_extension`, `link_url` |
| `video_start` | YouTube video starts (Enhanced Measurement) | `video_title`, `video_url`, `video_provider` |
| `video_progress` | YouTube video 10/25/50/75% (Enhanced Measurement) | `video_percent`, `video_title` |
| `video_complete` | YouTube video ends (Enhanced Measurement) | `video_title`, `video_url` |
| `form_start` | First form interaction (Enhanced Measurement) | `form_id`, `form_name` |
| `form_submit` | Form submission (Enhanced Measurement) | `form_id`, `form_name`, `form_submit_text` |

### App Events

| Event | Description |
|-------|-------------|
| `first_open` | First time app is opened after install |
| `screen_view` | Screen transition occurs |
| `app_update` | App is updated to a new version |
| `app_remove` | App package is removed (Android only) |
| `os_update` | Device OS is updated |

## Recommended Events

### E-commerce Events

| Event | Required Parameters | Recommended Parameters |
|-------|-------------------|----------------------|
| `view_item_list` | — | `item_list_id`, `item_list_name`, `items[]` |
| `select_item` | — | `item_list_id`, `item_list_name`, `items[]` |
| `view_item` | — | `currency`, `value`, `items[]` |
| `add_to_wishlist` | — | `currency`, `value`, `items[]` |
| `add_to_cart` | — | `currency`, `value`, `items[]` |
| `remove_from_cart` | — | `currency`, `value`, `items[]` |
| `view_cart` | — | `currency`, `value`, `items[]` |
| `begin_checkout` | — | `currency`, `value`, `coupon`, `items[]` |
| `add_shipping_info` | — | `currency`, `value`, `coupon`, `shipping_tier`, `items[]` |
| `add_payment_info` | — | `currency`, `value`, `coupon`, `payment_type`, `items[]` |
| `purchase` | `currency`, `transaction_id`, `value` | `affiliation`, `coupon`, `shipping`, `tax`, `items[]` |
| `refund` | `currency`, `transaction_id`, `value` | `affiliation`, `coupon`, `shipping`, `tax`, `items[]` |
| `view_promotion` | — | `creative_name`, `creative_slot`, `promotion_id`, `promotion_name`, `items[]` |
| `select_promotion` | — | `creative_name`, `creative_slot`, `promotion_id`, `promotion_name`, `items[]` |

### General Events

| Event | Recommended Parameters |
|-------|----------------------|
| `login` | `method` |
| `sign_up` | `method` |
| `search` | `search_term` |
| `select_content` | `content_type`, `item_id` |
| `share` | `method`, `content_type`, `item_id` |
| `generate_lead` | `currency`, `value` |

### Gaming / App Events

| Event | Recommended Parameters |
|-------|----------------------|
| `tutorial_begin` | — |
| `tutorial_complete` | — |
| `level_start` | `level_name` |
| `level_end` | `level_name`, `success` |
| `level_up` | `level`, `character` |
| `unlock_achievement` | `achievement_id` |
| `post_score` | `score`, `level`, `character` |
| `earn_virtual_currency` | `virtual_currency_name`, `value` |
| `spend_virtual_currency` | `item_name`, `virtual_currency_name`, `value` |

## Items Array Schema

The `items` array is used across all e-commerce events.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `item_id` | string | Yes* | Product SKU or ID |
| `item_name` | string | Yes* | Product name |
| `affiliation` | string | No | Store or seller name |
| `coupon` | string | No | Product-level coupon |
| `discount` | number | No | Discount amount |
| `index` | number | No | Position in list |
| `item_brand` | string | No | Brand name |
| `item_category` | string | No | Primary category |
| `item_category2` | string | No | Sub-category 2 |
| `item_category3` | string | No | Sub-category 3 |
| `item_category4` | string | No | Sub-category 4 |
| `item_category5` | string | No | Sub-category 5 |
| `item_list_id` | string | No | List ID |
| `item_list_name` | string | No | List name |
| `item_variant` | string | No | Variant (size, color) |
| `location_id` | string | No | Physical location |
| `price` | number | No | Unit price |
| `quantity` | number | No | Quantity |

*At least one of `item_id` or `item_name` is required.

## Event Naming Rules

1. **Format**: snake_case only
2. **Length**: Maximum 40 characters
3. **Start**: Must begin with a letter
4. **Characters**: Letters, numbers, underscores only
5. **Prefixes**: Cannot use `firebase_`, `ga_`, `google_`, `gtag.`
6. **Limit**: Maximum 500 distinct event names per property
7. **Parameters**: Maximum 25 custom parameters per event
8. **Parameter names**: Maximum 40 characters
9. **Parameter values**: Maximum 100 characters (strings)

## Event Limits

| Limit | Standard | GA4 360 |
|-------|----------|---------|
| Distinct event names | 500 | 500 |
| Event parameters per event | 25 | 25 |
| Event parameter name length | 40 chars | 40 chars |
| Event parameter value length | 100 chars | 100 chars |
| User properties | 25 | 25 |
| Custom dimensions (event) | 50 | 125 |
| Custom dimensions (user) | 25 | 100 |
| Custom metrics | 50 | 125 |
| Conversions | 30 | 50 |
| Audiences | 100 | 400 |
