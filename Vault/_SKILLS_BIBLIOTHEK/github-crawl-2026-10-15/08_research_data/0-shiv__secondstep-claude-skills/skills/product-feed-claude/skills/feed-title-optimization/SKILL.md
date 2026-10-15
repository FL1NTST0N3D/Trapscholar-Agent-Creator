# Feed Title Optimization Skill

## Command
`/feed titles`

## Overview

Product titles are the single most important attribute in your Google Merchant Center feed. They determine which search queries your products match, how your Shopping ads render, and ultimately whether a shopper clicks. Google's algorithm weighs the first 75 characters most heavily — what you front-load matters more than what comes after.

The proven title formula is: **Brand + Product Type + Key Attributes** (color, size, material, model). This structure aligns with how Google parses titles for relevance matching and how shoppers scan Shopping results.

## Title Rules

### Character Limits
- **Maximum length:** 150 characters
- **Visible in Shopping ads:** ~75 characters (varies by device)
- **Recommended sweet spot:** 80-120 characters
- **Never go below:** 30 characters (too short = low relevance)

### Front-Loading Strategy
Place the most important keywords in the first 75 characters. Google gives disproportionate weight to the beginning of the title. A title that starts with "Blue Nike Air Max 90 Running Shoes Men's Size 11" will outperform "Men's Athletic Footwear — Nike Brand Air Max 90 in Blue, Size 11."

### What to Include
1. **Brand name** — always first (unless brand is unknown/generic)
2. **Product type** — the core category noun (shoes, laptop, dress)
3. **Key differentiators** — color, size, material, model number
4. **Gender / age group** — for apparel and accessories
5. **Distinguishing specs** — for electronics (storage, processor, screen size)

### What to Avoid
- ALL CAPS (except brand acronyms like HP, LG)
- Promotional text ("Best Price," "Free Shipping," "Sale")
- Excessive punctuation (!!!, ---, ...)
- Keyword stuffing (repeating the same word)
- Foreign characters (unless targeting that language)
- Store name in the title (unless it IS the brand)

## Category-Specific Templates

### Apparel
**Formula:** Brand + Gender + Product Type + Color + Size + Material
```
Nike Women's Running Shorts Black Size M Dri-FIT
Levi's Men's 501 Original Jeans Dark Wash 32x30
Adidas Kids' Ultraboost 22 Running Shoes White Size 5
```

### Electronics
**Formula:** Brand + Model + Key Specs (processor, RAM, storage, screen)
```
Apple MacBook Air M2 13.6" 8GB RAM 256GB SSD Space Gray
Samsung Galaxy S24 Ultra 256GB Titanium Black Unlocked
Sony WH-1000XM5 Wireless Noise-Canceling Headphones Black
```

### Home & Garden
**Formula:** Brand + Product Type + Material + Dimensions + Color/Finish
```
KitchenAid Stand Mixer 5-Quart Stainless Steel Empire Red
Dyson V15 Detect Cordless Vacuum Cleaner Gold
IKEA KALLAX Shelf Unit 4x4 White 147x147cm
```

### Beauty & Personal Care
**Formula:** Brand + Product Line + Product Type + Size/Volume + Variant
```
CeraVe Moisturizing Cream 16oz Fragrance-Free
Maybelline Lash Sensational Mascara Blackest Black Washable
The Ordinary Niacinamide 10% + Zinc 1% Serum 30ml
```

### Food & Grocery
**Formula:** Brand + Product Name + Flavor/Variant + Size + Pack Count
```
KIND Bars Dark Chocolate Nuts & Sea Salt 12-Pack 1.4oz
Nespresso Vertuo Pods Stormio Dark Roast 40 Count
Blue Diamond Almonds Smokehouse 6oz Resealable Bag
```

## Optimization Process

### Step 1: Audit Current Titles
Run the title analyzer to score existing titles:
- Length check (is it 80-120 chars?)
- Brand presence (is brand name first?)
- Keyword density (are key attributes present?)
- Category template match (does it follow the formula?)

### Step 2: Identify Low-Scoring Titles
Flag titles scoring below 70/100:
- Too short (< 50 chars) — missing key attributes
- Too long (> 140 chars) — likely keyword-stuffed
- Missing brand — brand not in first position
- Generic — no differentiating attributes

### Step 3: Generate Optimized Titles
Use category templates to rebuild titles:
1. Extract brand, product type, and attributes from existing data
2. Apply the category-specific formula
3. Front-load the highest-value keywords
4. Verify character count is 80-120

### Step 4: A/B Testing via Supplemental Feed
Use a supplemental feed to test optimized titles:
- Run original vs optimized for 2-4 weeks
- Compare CTR, impression share, and conversion rate
- Roll out winners to the primary feed

## Common Mistakes

| Mistake | Example | Fix |
|---|---|---|
| Brand buried | "Comfortable Running Shoes by Nike" | "Nike Running Shoes Comfort Fit" |
| Too vague | "Nice Blue Shirt" | "Ralph Lauren Men's Oxford Shirt Blue Slim Fit L" |
| Keyword stuffed | "Shoes Running Shoes Athletic Shoes Men" | "Nike Men's Air Max 90 Running Shoes Black Size 10" |
| Promotional | "BEST DEAL Laptop 50% OFF" | "Dell Inspiron 15 Laptop i5 8GB 256GB SSD" |
| Missing specs | "Samsung Phone" | "Samsung Galaxy S24 128GB Phantom Black Unlocked" |

## Impact

- **CTR increase:** 20-40% with optimized titles
- **Impression increase:** 15-25% from better query matching
- **CPC decrease:** 5-15% from improved Quality Score
- **Revenue increase:** 10-30% compounded from all factors

## Files
- `title_templates.json` — Category-specific title templates
- `title_rules.yaml` — Validation rules and scoring criteria

## Author
Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | Second Step
