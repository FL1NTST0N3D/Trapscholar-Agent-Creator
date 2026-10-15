# Scoring Methodology

## Overview

Product Feed Claude uses a weighted scoring model to evaluate feed quality. Each product receives a score from 0-100 across four dimensions, which are combined into an overall score using weights that reflect each factor's impact on Shopping and PMax campaign performance.

## Scoring Weights

| Factor | Weight | Rationale |
|---|---|---|
| Title Quality | 30% | Titles are the #1 factor in search query matching and Shopping ad CTR |
| Attribute Completeness | 25% | Missing attributes cause disapprovals and suppress impressions |
| Image Compliance | 20% | Images drive click decisions and are a top disapproval reason |
| Description Quality | 15% | Descriptions influence relevance scoring and free listing visibility |
| Data Accuracy | 10% | Price/availability mismatches cause disapprovals |

**Formula:**
```
Overall = (Title * 0.30) + (Attributes * 0.25) + (Images * 0.20) + (Description * 0.15) + (Accuracy * 0.10)
```

## Grade Scale

| Score | Grade | Status | Interpretation |
|---|---|---|---|
| 90-100 | A | Excellent | Feed is well-optimized. Focus on marginal gains and maintaining quality. |
| 80-89 | B | Good | Minor improvements available. Low urgency, schedule during regular maintenance. |
| 70-79 | C | Average | Noticeable gaps. Prioritize the top 3 recommendations for meaningful lift. |
| 60-69 | D | Below Average | Significant issues actively suppressing performance. Schedule a remediation sprint. |
| 50-59 | E | Poor | Major problems. Multiple dimensions need immediate attention. |
| 0-49 | F | Critical | Feed is actively losing revenue. Emergency fix required. |

## Title Scoring (0-100)

### Criteria

| Check | Max Penalty | Condition |
|---|---|---|
| Length — too short | -40 | < 30 characters |
| Length — below optimal | -15 | 30-79 characters |
| Length — exceeds max | -30 | > 150 characters |
| Length — slightly long | -5 | 121-150 characters |
| Brand position | -15 | Brand name not at the start of the title |
| Promotional text | -20 | Contains "sale", "free shipping", "best price", etc. |
| Excessive caps | -15 | > 50% uppercase characters |
| Color not in title | -5 | Color attribute exists but not mentioned in title |
| Size not in title | -5 | Size attribute exists but not mentioned in title |

### Optimal Title
A 100-scoring title:
- 80-120 characters long
- Starts with the brand name
- Contains no promotional text
- Uses standard capitalization
- Includes color and size when applicable
- Follows the category-specific formula

## Description Scoring (0-100)

### Criteria

| Check | Max Penalty | Condition |
|---|---|---|
| Length — too short | -40 | < 100 characters |
| Length — below optimal | -15 | 100-749 characters |
| Length — exceeds max | -10 | > 5,000 characters |
| Promotional text | -20 | Contains "sale", "discount", "free shipping", etc. |
| HTML tags | -15 | Contains `<tag>` patterns |
| Placeholder text | -40 | Contains "TBD", "coming soon", "N/A", or < 20 chars |
| Duplicate of title | -25 | Description is identical to the title |

### Optimal Description
A 100-scoring description:
- 750-1,500 characters
- No promotional language
- No HTML tags
- Unique content (not a copy of the title)
- Includes features, specifications, and benefits

## Image Scoring (0-100)

### Criteria

| Check | Max Penalty | Condition |
|---|---|---|
| Missing image | -100 | No image_link provided |
| Invalid URL format | -30 | Does not start with http:// or https:// |
| HTTP instead of HTTPS | -5 | URL uses http:// |
| Unrecognized extension | -10 | URL does not end with .jpg, .png, .webp, etc. |
| No additional images | -15 | additional_image_link is empty |
| Placeholder URL | -30 | URL contains "placeholder", "no-image", "default" |

### Optimal Image
A 100-scoring image:
- Valid HTTPS URL with recognized image extension
- No placeholder patterns in the URL
- At least one additional_image_link provided

Note: Full image quality analysis (dimensions, watermarks, fill ratio) requires downloading the image, which the script does not do by default. The score reflects URL-level validation only.

## Attribute Scoring (0-100)

### Criteria

| Check | Max Penalty | Condition |
|---|---|---|
| Missing required attributes | -12 each | Up to -60 total for missing id, title, description, etc. |
| Missing GTIN + MPN | -10 | Branded product with no product identifiers |
| Invalid GTIN | -15 | GTIN fails check-digit validation |
| Invalid availability | -15 | Value not in: in_stock, out_of_stock, preorder, backorder |
| Invalid condition | -10 | Value not in: new, refurbished, used |
| Price format issue | -10 | Not matching `29.99 USD` pattern |
| Low recommended fill | -15 | < 30% of recommended attributes filled |
| Medium recommended fill | -8 | 30-49% of recommended attributes filled |
| Missing apparel attributes | -10 | Apparel product missing gender, age_group, color, or size |

### Optimal Attributes
A 100-scoring product:
- All required attributes present and correctly formatted
- Valid GTIN with correct check digit
- Availability and condition use exact enum values
- Price includes ISO 4217 currency code
- 80%+ recommended attributes filled
- Category-specific attributes complete

## Aggregate Scoring

### Feed-Level Score
The feed-level score is the weighted average of all individual product scores:

```
Feed Score = mean(all product overall scores)
```

### Score Distribution
The report also shows how products distribute across grade bands, which is more actionable than a single average:
- A feed with avg score 75 but 40% of products at F grade needs different action than one with all products at C grade

## Benchmarks

Industry reference points based on Google Merchant Center aggregate data:

| Metric | Bottom 25% | Median | Top 25% | Top 10% |
|---|---|---|---|---|
| Overall Score | < 45 | 55-65 | 70-80 | 85+ |
| Title Length (avg) | < 40 chars | 50-70 | 80-100 | 100-120 |
| Description Length (avg) | < 200 chars | 300-500 | 700-1000 | 1000+ |
| GTIN Coverage | < 40% | 55-70% | 75-90% | 95%+ |
| Approval Rate | < 80% | 85-90% | 92-96% | 98%+ |
| Recommended Attr Fill | < 25% | 35-50% | 55-70% | 80%+ |
