# Feed Description Skill

## Command
`/feed descriptions`

## Overview

Product descriptions in Google Merchant Center serve two critical purposes: they help Google understand your product for query matching, and they appear in free listings and some Shopping ad formats. While descriptions carry less weight than titles for ad rendering, they significantly influence product relevance scoring and can be the difference between matching a long-tail query or being filtered out.

The maximum length is 5,000 characters, but the first 150-200 characters matter most. Google truncates descriptions in most placements, so front-load key information just like titles. The description should complement the title — not repeat it — by adding features, specifications, use cases, and benefits that help both Google and shoppers understand what the product is.

## Description Rules

### Character Limits
- **Maximum:** 5,000 characters
- **Recommended minimum:** 500 characters (short descriptions = low relevance)
- **Optimal range:** 750-1,500 characters
- **First 150 chars:** Treated as a "meta description" — make them count

### Content Requirements
1. **Key features** — 3-5 bullet-style features (material, dimensions, weight, compatibility)
2. **Specifications** — technical details that differentiate (processor speed, resolution, capacity)
3. **Benefits** — what the product does for the buyer (comfort, durability, performance)
4. **Use cases** — when and where the product is used (everyday wear, outdoor activities, professional use)
5. **Included items** — what comes in the box (charger, case, accessories)

### Policy Compliance — What NOT to Include
Google will disapprove products with descriptions containing:
- **Promotional text:** "Sale," "50% off," "free shipping," "best price," "limited time"
- **Excessive capitalization:** "AMAZING QUALITY" — use normal sentence case
- **Competitor comparisons:** "Better than [competitor brand]"
- **External links:** URLs or references to other websites
- **Irrelevant keywords:** Terms unrelated to the product
- **Placeholder text:** "Description coming soon," "TBD," "N/A"
- **HTML tags:** Raw HTML is not rendered and may cause parsing errors
- **Excessive whitespace:** Multiple blank lines or excessive spacing

### Keyword Integration Strategy
Write descriptions that naturally include relevant search terms without stuffing:

**Bad (keyword stuffing):**
"Running shoes for men, men's running shoes, best running shoes, athletic shoes for running, running sneakers men, men running footwear."

**Good (natural integration):**
"Designed for daily training and long-distance runs, these men's running shoes feature a responsive foam midsole that returns energy with every stride. The breathable mesh upper keeps feet cool during warm-weather workouts, while the rubber outsole provides reliable grip on both road and trail surfaces."

## Description Templates

### Apparel
```
The [Brand] [Product Name] is designed for [use case]. Made from [material/fabric]
with [key feature], this [product type] offers [benefit]. Features include
[feature 1], [feature 2], and [feature 3]. Available in [color options] and
sizes [size range]. [Care instructions]. Perfect for [occasion/activity].
```

### Electronics
```
The [Brand] [Model] delivers [primary benefit] with its [key spec]. Powered by
[processor/chipset], it features [storage/RAM], a [screen size/resolution] display,
and [battery life]. [Connectivity options]. Includes [in-box accessories].
Compatible with [ecosystem/OS]. Ideal for [use case].
```

### Home & Kitchen
```
The [Brand] [Product Name] brings [benefit] to your [room/space]. Constructed from
[material] with a [finish/color] finish, it measures [dimensions] and supports up
to [weight capacity]. Features include [feature 1], [feature 2], and [feature 3].
Assembly [required/not required]. [Warranty information].
```

### Beauty & Personal Care
```
[Brand] [Product Name] is formulated with [key ingredients] to [primary benefit].
This [product type] is [skin type/hair type] friendly and [cruelty-free/vegan/organic
as applicable]. Apply [usage instructions] for best results. [Volume/weight].
[Fragrance: scented/unscented]. Dermatologist [tested/recommended].
```

## Optimization Process

### Step 1: Audit Current Descriptions
Evaluate each description against these criteria:
- **Length:** Is it at least 500 characters?
- **Keyword presence:** Does it include the primary product category keyword?
- **Policy compliance:** Any promotional text or prohibited content?
- **Completeness:** Does it cover features, specs, and benefits?
- **Uniqueness:** Is it distinct from the title and other product descriptions?

### Step 2: Score and Prioritize
Score descriptions 0-100:
- 90-100: Well-written, keyword-rich, compliant, 750+ chars
- 70-89: Adequate but could include more detail
- 50-69: Too short, missing key information, or partially non-compliant
- Below 50: Missing, placeholder text, or policy-violating

### Step 3: Rewrite Low-Scoring Descriptions
For each product scoring below 70:
1. Pull product data from other feed attributes (title, brand, color, size, material)
2. Research the product category for relevant keywords
3. Write using the category template
4. Verify policy compliance
5. Check character count (target 750-1,500)

### Step 4: Bulk Description Generation
For feeds with 100+ products needing rewrites:
1. Group products by category
2. Create category-specific templates with variable placeholders
3. Merge product data into templates
4. Manual review of a 10% sample
5. Upload via supplemental feed for testing

## Common Mistakes

| Mistake | Impact | Fix |
|---|---|---|
| Copy-pasted from website | Duplicate content penalty | Write unique feed-specific descriptions |
| Too short (< 100 chars) | Low relevance score | Expand to 750+ characters |
| Promotional language | Product disapproval | Remove all sales/pricing language |
| Same description for variants | Duplicate content | Differentiate by color, size, material |
| Missing specs | Poor query matching | Add technical specifications |
| Keyword stuffing | Manual review flag | Write naturally, vary keyword usage |

## Impact
- **Relevance improvement:** 10-20% more query matches
- **Free listing visibility:** Descriptions appear in full on free listings
- **Disapproval prevention:** Policy-compliant descriptions avoid account flags
- **Long-tail matching:** Detailed descriptions capture specific search queries

## Author
Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | Second Step
