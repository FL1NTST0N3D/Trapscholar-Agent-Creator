---
name: etsy-browser
description: >
  Etsy shop management via internal API and Playwright browser automation.
  CRUD listings, upload images, manage orders across 4 shops.
  Triggers: "etsy listing", "etsy shop", "upload to etsy", "etsy order",
  "create listing", "update listing", "etsy images", "example-shop",
  "etsy sales", "publish to etsy", "etsy dashboard".
  DO NOT trigger on: generic e-commerce questions, Amazon/eBay, Shopify,
  "how does Etsy work" (general knowledge, not shop management).
---

# Etsy Browser Automation

Manage Etsy shops via direct internal API (httpx + cookies) with Playwright fallback. No Make.com, no official API keys needed.

## When to Use Which API

| Method | Use When | Speed |
|--------|----------|-------|
| **Browser automation** (this skill) | Cookie-based CRUD, image uploads, internal API | ~0.5-1s per call |
| **Official OAuth API** (`etsy-agent`) | SEO content generation, bulk queries, 103 endpoints | ~0.3s per call |

For most listing management, use this browser automation. For SEO-optimized titles/descriptions/tags, use the `etsy-agent`.

## Quick Reference

**Module**: `~/tools/etsy_browser.py`
**Cookie refresh**: `~/tools/etsy_cookie_refresh.py` (systemd timer, every 4h)
**Agent**: `etsy-agent` (SEO content generation via Official OAuth API)

### Shops

| Alias | Shop Name | Shop ID | Cookies |
|-------|-----------|---------|---------|
| shop1 | ExampleShop1 | SHOP_ID_1 | `~/.cookies/etsy-shop1.json` |
| shop2 | ExampleShop2 | SHOP_ID_2 | `~/.cookies/etsy-shop2.json` |
| shop3 | ExampleShop3 | SHOP_ID_3 | `~/.cookies/etsy-shop3.json` |
| shop4 | ExampleShop4 | SHOP_ID_4 | `~/.cookies/etsy-shop4.json` |

Default shop: **shop1**

## API Operations (Fast Path - httpx)

All API functions are synchronous (they wrap async internally).

### Check Sessions
```python
from commander.tools.etsy_browser import etsy_list_shops
result = etsy_list_shops()  # checks all shops with cookies, ~0.5s each
```

### Get Listings
```python
from commander.tools.etsy_browser import etsy_api_get_listings
# All active listings (paginated, may take 60s+ for large shops)
result = etsy_api_get_listings("shop1", state="active")
# Filter by section
result = etsy_api_get_listings("shop1", section_id="52287660")
```

### Get Single Listing
```python
from commander.tools.etsy_browser import etsy_api_get_listing
result = etsy_api_get_listing("shop1", "1889058316")  # ~0.6s, 127 fields
```

### Create Listing (Draft)
```python
from commander.tools.etsy_browser import etsy_api_create_listing
result = etsy_api_create_listing(
    shop="shop1",
    title="Mountain Coffee Mug Gift For Him",
    description="Beautiful mountain scene...",
    price="14.99",
    tags=["coffee mug", "gift for him", "mountain mug"],
    taxonomy_id=6048,       # Mugs category
    state="draft",          # "draft" or "active"
    quantity=99,
)
```

### Update Listing
```python
from commander.tools.etsy_browser import etsy_api_update_listing
result = etsy_api_update_listing(
    shop="shop1",
    listing_id="1889058316",
    title="New Title Here",
    price="16.99",
    quantity=50,
)
```

### Upload Image
```python
from commander.tools.etsy_browser import etsy_api_upload_image
result = etsy_api_upload_image(
    shop="shop1",
    listing_id="1889058316",
    image_path="/path/to/image.jpg",
    rank=1,  # 1 = primary image
)
```

### Delete / Deactivate Listing
```python
from commander.tools.etsy_browser import etsy_api_delete_listing, etsy_api_deactivate_listing
# Permanent delete (returns 204)
etsy_api_delete_listing("shop1", "1889058316")
# Deactivate (set inactive, reversible)
etsy_api_deactivate_listing("shop1", "1889058316")
```

### Batch Update
```python
from commander.tools.etsy_browser import etsy_batch_update
result = etsy_batch_update(
    shop="shop1",
    listing_ids=["1889058316", "1889058317"],
    quantity=99,
)
```

### Get Sections
```python
from commander.tools.etsy_browser import etsy_api_get_sections
result = etsy_api_get_sections("shop1")
# Returns: [{"section_id": "52287660", "title": "Mugs", ...}, ...]
```

## Hybrid Functions (API first, Playwright fallback)

These try the fast API path, fall back to browser automation if API fails:

```python
from commander.tools.etsy_browser import (
    etsy_create_listing,    # create via API, fallback browser
    etsy_update_listing,    # update via API, fallback browser
    etsy_get_listing,       # get via API, fallback browser
    etsy_get_listings,      # get all via API, fallback browser
    etsy_upload_images,     # upload via API, fallback browser
    etsy_delete_listing,    # delete via API, fallback browser
)
```

All return dicts with `_via: "api"` or `_via: "browser"` to indicate which path was used.

## CLI Commands

```bash
# Check all shop sessions
python -m commander.tools.etsy_browser check-sessions

# Check sessions via API only (faster)
python -m commander.tools.etsy_browser check-sessions --api

# Import cookies for a shop (paste from clipboard)
python -m commander.tools.etsy_browser import-cookies shop1

# Test API operations
python -m commander.tools.etsy_browser api-test shop1 [listing_id]
```

## Cookie Management

### Export from Chrome
1. Log into Etsy shop in Chrome
2. DevTools (F12) > Application > Cookies > `https://www.etsy.com`
3. Right-click > "Copy all as JSON" (or use Cookie-Editor extension)
4. Save to `~/.cookies/etsy-{alias}.json`

### Auto-refresh (systemd timer)
Runs every 4 hours automatically:
```bash
systemctl --user status etsy-cookie-refresh.timer   # check timer
journalctl --user -u etsy-cookie-refresh --since today  # view logs
cat ~/logs/etsy-cookie-refresh.log                   # log file
python3 ~/commander/tools/etsy_cookie_refresh.py     # manual run
```

Sends Telegram alert via Joe bot if any session expires. If alert fires, re-export cookies from Chrome.

## Gotchas

- **Price**: Always send as string (`"14.99"`) in create/update, never int
- **Tags**: Max 13 tags, max 20 chars each
- **Title**: Max 140 characters
- **Taxonomy ID**: 6048 for Mugs. Find other IDs from the listing editor network tab in Chrome DevTools.
- **CSRF nonce expires**: Re-fetched automatically every 10 min
- **Cookies expire**: ~30 days if unused. Timer refreshes every 4h.
- **Rate limits**: Max 1 listing create per 60s, 10 per hour (self-imposed, not enforced in code)

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Empty API response | Cookie expired. Re-export from Chrome. |
| 403 Forbidden | CSRF nonce stale. Will auto-refresh, retry in 30s. |
| Playwright timeout | Shop page changed layout. Check selectors in etsy_browser.py. |
| `shop alias not found` | Use one of: shop1, shop2, shop3, shop4 |
