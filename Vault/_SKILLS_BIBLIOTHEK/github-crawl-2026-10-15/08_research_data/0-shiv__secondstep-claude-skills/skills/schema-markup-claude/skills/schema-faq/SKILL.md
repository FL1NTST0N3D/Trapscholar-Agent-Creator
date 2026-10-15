# Schema: FAQ Page

Generate FAQPage schema markup in JSON-LD format. This schema structures Question/Answer pairs for search engine consumption and, on eligible sites, enables FAQ rich results with expandable dropdowns directly in Google Search.

## Command

`/schema faq`

## When to Use

FAQPage schema is appropriate for any page that contains a list of frequently asked questions with their answers. This includes dedicated FAQ pages, product pages with FAQ sections, service pages with common questions, and landing pages with Q&A content. The schema should only be used when the questions and answers are visible on the page -- hidden or dynamically loaded FAQ content that is not in the initial HTML may be flagged by Google.

## Important: 2023 Google Restrictions

In August 2023, Google significantly restricted FAQ rich results. The key changes:

- **FAQ rich results now only appear for well-known, authoritative government and health websites.** Regular business websites, blogs, and e-commerce sites will NOT get FAQ rich results even with perfect schema markup.
- The schema itself remains valid Schema.org vocabulary and is still recognized by Google -- it just will not generate visible rich results for most sites.
- **Bing still shows FAQ rich results** for all sites with valid FAQPage schema.
- Other search engines and AI systems (ChatGPT, Perplexity, Claude) may use FAQ schema to understand page content and generate answers.

**Recommendation**: Still implement FAQPage schema for Bing visibility, AI engine comprehension, and future-proofing. But do not promise clients FAQ rich results in Google.

## Required Properties (Google)

- `@type`: "FAQPage"
- `mainEntity`: Array of Question objects

### For each Question:
- `@type`: "Question"
- `name`: The full question text
- `acceptedAnswer`: Answer object

### For each Answer:
- `@type`: "Answer"
- `text`: The full answer text (HTML is allowed: `<a>`, `<br>`, `<b>`, `<i>`, `<ul>`, `<ol>`, `<li>`, `<p>`, `<h2>`-`<h6>`)

## Content Guidelines

- **One FAQPage per page**: Do not use multiple FAQPage schemas on a single URL.
- **Visible content only**: Every Q&A pair in the schema must be visible on the page. Do not include hidden content.
- **No advertising**: Answer text must not be used for advertising purposes.
- **Author-written**: FAQ content must be written by the site owner. Do not use FAQPage for user-generated Q&A (use QAPage for that).
- **Unique answers**: Each answer should provide unique, helpful information. Do not use FAQ schema for trivially short answers.

## FAQPage vs QAPage

These are different schema types for different use cases:

- **FAQPage**: The site author writes both questions and answers. Used for FAQ sections, help pages, product Q&A written by the brand.
- **QAPage**: Users submit questions and other users provide answers. Used for forums, community Q&A sites, Stack Overflow-style pages.

Do not use FAQPage for user-generated content. Google will ignore or penalize misuse.

## HTML in Answers

Google supports limited HTML in the `text` property of Answer objects. This is useful for including links, lists, and formatting:

```json
"text": "<p>Our return policy allows returns within 30 days of purchase.</p><ul><li>Items must be in original packaging</li><li>Include the receipt or order confirmation</li><li><a href='https://example.com/returns'>Start a return here</a></li></ul>"
```

Supported HTML tags: `<h2>` through `<h6>`, `<br>`, `<ol>`, `<ul>`, `<li>`, `<a>`, `<p>`, `<div>`, `<b>`, `<strong>`, `<i>`, `<em>`.

## Combining with Other Schema

FAQPage schema is commonly combined with:

- **Article + FAQPage**: Blog post with an FAQ section at the bottom
- **Product + FAQPage**: Product page with product-specific questions
- **LocalBusiness + FAQPage**: Location page with common customer questions
- **Service + FAQPage**: Service page with service-related questions

When combining, use `@graph` notation to place multiple schema types on one page.

## Common Mistakes

- **Using FAQPage for forum content**: Use QAPage instead for user-generated Q&A.
- **Hidden FAQ content**: Accordion/expandable FAQ sections are fine, but the content must be in the initial HTML (not loaded via AJAX after user interaction).
- **Too many questions**: While there is no hard limit, Google typically shows 2-4 FAQ results. Keep the schema focused on the most important questions.
- **Duplicate questions across pages**: The same Q&A should not appear in FAQPage schema on multiple pages of the same site.
- **Expecting Google rich results**: After the 2023 changes, most sites will not get FAQ rich results in Google. Set appropriate expectations.

## Google Rich Result Eligibility

- **Pre-August 2023**: All sites with valid FAQPage schema could get FAQ rich results
- **Post-August 2023**: Only well-known government and health authority sites get FAQ rich results in Google
- **Bing**: Still shows FAQ rich results for all qualifying sites
- **AI engines**: FAQ schema helps AI systems understand and cite your Q&A content
