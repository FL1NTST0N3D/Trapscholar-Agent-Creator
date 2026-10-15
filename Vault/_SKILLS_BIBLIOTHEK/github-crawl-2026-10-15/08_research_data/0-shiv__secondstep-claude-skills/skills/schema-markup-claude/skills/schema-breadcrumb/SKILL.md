# Schema: Breadcrumb

Generate BreadcrumbList schema markup in JSON-LD format. This schema defines the navigation hierarchy of a page within a website, enabling breadcrumb rich results that replace the URL slug in Google Search results with a clean, clickable path.

## Command

`/schema breadcrumb`

## When to Use

BreadcrumbList schema should be on every page of a website that has hierarchical navigation. This includes virtually all e-commerce sites, content sites, documentation sites, and any site with more than a flat structure. Breadcrumb rich results are one of the most reliable and consistently displayed rich result types -- Google shows them for most sites that implement the schema correctly. They improve both CTR (users see context about the page's location) and crawlability (search engines understand site structure).

## Required Properties (Google)

- `@type`: "BreadcrumbList"
- `itemListElement`: Array of ListItem objects in order from root to current page

### For each ListItem:
- `@type`: "ListItem"
- `position`: Integer indicating the position in the breadcrumb trail (1 = root/home)
- `name`: Display name for this breadcrumb level
- `item`: URL of this breadcrumb level (omit for the last/current item)

## Template Structure

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Category",
      "item": "https://example.com/category/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Current Page"
    }
  ]
}
```

Note: The last item in the breadcrumb trail (the current page) should have `name` but NO `item` URL. This tells Google it is the current page.

## E-Commerce Breadcrumbs

E-commerce sites often have multiple valid breadcrumb paths to the same product. Google recommends choosing one canonical path:

```
Home > Electronics > Smartphones > iPhone 15 Pro
```

If a product belongs to multiple categories, pick the primary category for the breadcrumb schema. Do not include multiple BreadcrumbList schemas with different paths for the same page.

## Multi-Level Hierarchies

For deep hierarchies, include all levels:

```
Home > Documentation > API Reference > Authentication > OAuth 2.0
```

There is no hard limit on breadcrumb depth, but keep it practical. More than 5-6 levels may indicate the site structure is too deep.

## Common Patterns

### Blog Post
```
Home > Blog > Category > Post Title
```

### E-Commerce Product
```
Home > Department > Category > Subcategory > Product Name
```

### Documentation
```
Home > Docs > Section > Subsection > Page Title
```

### Location Page
```
Home > Locations > State > City > Branch Name
```

## Combining with Other Schema

BreadcrumbList is almost always used alongside other schema types on the same page. It is one of the most commonly combined schema types:

- **Article + BreadcrumbList**: Blog post with navigation context
- **Product + BreadcrumbList**: Product page with category hierarchy
- **LocalBusiness + BreadcrumbList**: Location page within site structure
- **Event + BreadcrumbList**: Event page within events section

When combining, use `@graph` notation:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "BreadcrumbList", "itemListElement": [...] },
    { "@type": "Product", "name": "...", ... }
  ]
}
```

## Common Mistakes

- **Including item URL on the last breadcrumb**: The current page (last item) should NOT have an `item` property. Including it is not an error but is unnecessary.
- **Wrong position numbering**: Positions must start at 1 and increment by 1. Do not start at 0 or skip numbers.
- **Mismatched URLs**: Breadcrumb `item` URLs must match the actual URLs of those pages. Do not use redirect URLs or URL variants.
- **Missing intermediate levels**: Do not skip hierarchy levels. If the URL structure is `/shoes/running/trail-runner`, include all three levels.
- **Using breadcrumb schema on the homepage**: The homepage does not need breadcrumb schema since it IS the root.
- **Dynamic breadcrumbs from search/filter**: If breadcrumbs change based on how a user navigated to the page, use the canonical category path in schema, not the dynamic path.

## Google Rich Result Eligibility

BreadcrumbList schema enables:
- **Breadcrumb rich results**: The URL path in search results is replaced with a formatted breadcrumb trail (e.g., "example.com > Category > Subcategory" instead of "example.com/category/subcategory/page-slug")
- **Sitelinks enhancement**: Breadcrumb data helps Google generate more accurate sitelinks
- **Search result navigation**: Users can click individual breadcrumb levels directly from search results

This is one of the most reliably displayed rich results -- Google shows breadcrumbs for the vast majority of sites that implement the schema correctly. There are no restrictions similar to the FAQ/HowTo changes.

## Implementation Priority

BreadcrumbList should be one of the first schema types implemented on any site because:
1. It is universally applicable (every non-homepage page benefits)
2. It has near-universal rich result display (Google shows it consistently)
3. It improves Google's understanding of site structure
4. It is simple to implement with low risk of errors
5. It can be templated and auto-generated from URL structure or CMS categories
