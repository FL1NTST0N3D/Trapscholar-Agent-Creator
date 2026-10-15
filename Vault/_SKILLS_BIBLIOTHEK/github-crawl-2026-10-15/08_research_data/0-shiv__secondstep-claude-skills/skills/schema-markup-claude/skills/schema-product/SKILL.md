# Schema: Product

Generate complete Product + Offer schema markup in JSON-LD format. This schema powers product rich results in Google Search, Google Shopping, and Google Merchant Center, displaying prices, availability, ratings, and reviews directly in search results.

## Command

`/schema product`

## When to Use

Product schema belongs on every product detail page (PDP) in an e-commerce store. It is also appropriate for product review pages, comparison pages, and affiliate content that references specific products. This is one of the highest-impact schema types for e-commerce -- product rich results with price and availability can increase CTR by 30% or more.

## Required Properties (Google)

- `@type`: "Product"
- `name`: Full product name
- `image`: At least one product image URL (array recommended; Google prefers multiple angles)
- `offers` or `review` or `aggregateRating`: At least ONE of these must be present for rich result eligibility

### For Offers (required within Offer object)
- `@type`: "Offer"
- `price`: Numeric price value (no currency symbols)
- `priceCurrency`: ISO 4217 currency code (USD, EUR, GBP, INR, etc.)
- `availability`: ItemAvailability enum (InStock, OutOfStock, PreOrder, BackOrder, Discontinued, SoldOut)

## Recommended Properties

- `description`: Product description (plain text, no HTML)
- `brand`: Brand object with `name`
- `sku`: Stock keeping unit (unique product identifier)
- `gtin` / `gtin8` / `gtin12` / `gtin13` / `gtin14`: Global Trade Item Number (UPC, EAN, ISBN)
- `mpn`: Manufacturer Part Number
- `color`: Product color
- `material`: Product material
- `size`: Product size
- `weight`: QuantitativeValue for product weight
- `aggregateRating`: AggregateRating with `ratingValue`, `reviewCount`, `bestRating`
- `review`: Array of Review objects with `author`, `reviewRating`, `reviewBody`, `datePublished`
- `offers.url`: Direct URL to purchase
- `offers.priceValidUntil`: Date when the price expires (ISO 8601)
- `offers.seller`: Organization or Person selling the product
- `offers.shippingDetails`: OfferShippingDetails for shipping cost and delivery time
- `offers.hasMerchantReturnPolicy`: MerchantReturnPolicy for return information
- `offers.itemCondition`: OfferItemCondition (NewCondition, UsedCondition, RefurbishedCondition, DamagedCondition)

## Product Variants

For products with variants (size, color, material), use `AggregateOffer` or multiple `Offer` objects:

```json
"offers": {
  "@type": "AggregateOffer",
  "lowPrice": "29.99",
  "highPrice": "49.99",
  "priceCurrency": "USD",
  "offerCount": "4",
  "availability": "https://schema.org/InStock"
}
```

Or list individual offers for each variant with distinguishing properties like `sku`, `name`, or `description`.

## Google Merchant Center Integration

Product schema feeds into Google Merchant Center and Google Shopping. For maximum compatibility:

1. Include `gtin` or `mpn` + `brand` -- Google Merchant Center requires product identifiers
2. Use `availability` URLs from schema.org namespace (e.g., "https://schema.org/InStock")
3. Keep `price` consistent with the visible price on the page (Google verifies this)
4. Include `shippingDetails` and `hasMerchantReturnPolicy` for enhanced Shopping listings

## Shipping and Returns (2024+)

Google increasingly values shipping and return information in Product schema:

```json
"shippingDetails": {
  "@type": "OfferShippingDetails",
  "shippingRate": {
    "@type": "MonetaryAmount",
    "value": "0",
    "currency": "USD"
  },
  "deliveryTime": {
    "@type": "ShippingDeliveryTime",
    "handlingTime": { "@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY" },
    "transitTime": { "@type": "QuantitativeValue", "minValue": 3, "maxValue": 7, "unitCode": "DAY" }
  },
  "shippingDestination": {
    "@type": "DefinedRegion",
    "addressCountry": "US"
  }
}
```

## Common Mistakes

- **Price with currency symbol**: `price` must be numeric only. Use `priceCurrency` for the currency.
- **Missing availability**: Without availability, Google will not show the price in rich results.
- **Outdated prices**: Google cross-checks schema prices against page content. Mismatches result in rich result removal.
- **Self-authored reviews**: Reviews in schema must be genuine customer reviews, not written by the seller.
- **Missing product identifiers**: Without `gtin` or (`mpn` + `brand`), Google Merchant Center will flag the product.
- **No image**: Product schema without at least one image is ineligible for rich results.
- **Wrong availability URL**: Use full Schema.org URLs like "https://schema.org/InStock", not short strings like "in stock".

## Google Rich Result Eligibility

Product schema enables:
- **Product snippets**: Price, availability, rating stars in organic results
- **Google Shopping**: Free product listings in the Shopping tab
- **Merchant listings**: Enhanced product cards with shipping and return info
- **Product Knowledge Panels**: For well-known products
- **Price drop annotations**: Google can show price drop badges when prices decrease

## Testing

1. Google Rich Results Test: https://search.google.com/test/rich-results
2. Google Merchant Center: Upload and validate product feeds
3. Schema.org Validator: https://validator.schema.org/
