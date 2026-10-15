# Schema: Article

Generate Article, BlogPosting, and NewsArticle schema markup in JSON-LD format. This schema provides search engines with structured information about written content including authorship, publication dates, publisher details, and content metadata, enabling enhanced search result presentation.

## Command

`/schema article`

## When to Use

Article schema is appropriate for any page that contains editorial content: blog posts, news articles, magazine features, opinion pieces, scholarly articles, technical documentation, and long-form written content. It is one of the most widely used schema types and directly impacts how content appears in Google Search, Google News, Google Discover, and AI-generated summaries.

## Schema Type Selection

Choose the most specific type:

- **Article**: General articles, editorial content, magazine features, essays
- **BlogPosting**: Blog posts on a blog section of a website (subtype of Article)
- **NewsArticle**: Time-sensitive news reporting (subtype of Article). Required for Google News eligibility.
- **ScholarlyArticle**: Academic or research papers
- **TechArticle**: Technical documentation, developer guides
- **AdvertiserContentArticle**: Sponsored content or advertorials (important for transparency)
- **ReportageNewsArticle**: Investigative or in-depth news reporting
- **ReviewNewsArticle**: News articles that include a review or critique

## Required Properties (Google)

- `@type`: "Article", "BlogPosting", or "NewsArticle"
- `headline`: Article title (max 110 characters for Google compatibility)
- `image`: At least one image. Google requires images to be at least 696px wide. Provide multiple sizes: 16x9, 4x3, and 1x1 aspect ratios for maximum coverage.
- `datePublished`: ISO 8601 datetime of first publication
- `author`: Person or Organization object with `name` and ideally `url`

## Recommended Properties

- `dateModified`: ISO 8601 datetime of most recent significant update
- `publisher`: Organization object with `name` and `logo` (ImageObject)
- `description`: Meta description of the article (150-160 characters)
- `mainEntityOfPage`: URL of the page (canonical URL)
- `articleBody`: Full text content of the article (optional, can be very long)
- `wordCount`: Integer word count
- `articleSection`: Section or category the article belongs to
- `keywords`: Array of keyword strings
- `inLanguage`: Language code (e.g., "en-US", "es", "fr")
- `isAccessibleForFree`: Boolean for paywall status
- `hasPart`: For paywalled content, use `WebPageElement` with `isAccessibleForFree: false` and `cssSelector` to identify the paywalled section
- `speakable`: SpeakableSpecification identifying sections suitable for text-to-speech (see Speakable section)
- `citation`: References to sources cited in the article
- `isPartOf`: For articles in a series, reference the parent CreativeWorkSeries

## Author Markup

Google places increasing emphasis on author expertise (E-E-A-T). Robust author markup includes:

```json
"author": {
  "@type": "Person",
  "name": "Jane Smith",
  "url": "https://example.com/author/jane-smith",
  "sameAs": [
    "https://twitter.com/janesmith",
    "https://linkedin.com/in/janesmith"
  ],
  "jobTitle": "Senior Editor",
  "worksFor": {
    "@type": "Organization",
    "name": "Example Media"
  }
}
```

For multiple authors, use an array of Person objects.

## Publisher Markup

Publisher should reference the site's Organization schema:

```json
"publisher": {
  "@type": "Organization",
  "name": "Example Media",
  "logo": {
    "@type": "ImageObject",
    "url": "https://example.com/logo.png",
    "width": 250,
    "height": 60
  }
}
```

Use `"@id": "https://example.com/#organization"` to reference the Organization schema defined on the homepage rather than duplicating all properties.

## Paywalled Content

For sites with paywalls, Google requires structured data to distinguish free from paid content:

```json
{
  "@type": "NewsArticle",
  "isAccessibleForFree": false,
  "hasPart": {
    "@type": "WebPageElement",
    "isAccessibleForFree": false,
    "cssSelector": ".paywall-content"
  }
}
```

This prevents Google from flagging the site for cloaking (showing Google different content than users see).

## Common Mistakes

- **Headline too long**: Google truncates headlines over 110 characters. Keep it concise.
- **Missing author**: Google's E-E-A-T guidelines make author attribution increasingly important. Always include author with at least a name.
- **Wrong date format**: Use full ISO 8601 with timezone: "2024-01-15T09:00:00-05:00". Not "January 15, 2024".
- **Image too small**: Google requires at least 696px wide. Provide 1200px+ for best results.
- **Using Article for product pages**: Product pages should use Product schema, not Article.
- **Missing dateModified**: If the article has been updated, include dateModified. Google uses this for freshness signals.
- **Duplicate publisher**: Use @id references instead of duplicating the full Organization schema on every article page.

## Google Rich Result Eligibility

Article schema contributes to:
- **Article rich results**: Enhanced appearance in search with large image, headline, date, and author
- **Google News**: NewsArticle schema is required for Google News inclusion
- **Google Discover**: Article schema helps content surface in Google Discover feeds
- **Top Stories carousel**: NewsArticle schema is required for Top Stories placement
- **AMP articles**: Article schema combined with AMP markup for accelerated mobile pages
