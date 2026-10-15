# Feed Images Skill

## Command
`/feed images`

## Overview

Product images are the first thing shoppers see in Shopping ads and free listings. They are also one of the top reasons for product disapprovals — Google enforces strict image requirements and will reject products with non-compliant images instantly. Unlike titles and descriptions which can be fixed in the feed file, image issues often require going back to the product photography pipeline, making them more expensive to fix after the fact.

Getting images right from the start prevents disapprovals, improves CTR, and ensures your products compete visually with every other listing in the Shopping carousel. This skill audits your image_link and additional_image_link attributes against Google's requirements and flags violations before Google does.

## Image Requirements

### Minimum Size
| Product Category | Minimum Size | Recommended Size |
|---|---|---|
| Non-apparel products | 100 x 100 px | 800 x 800 px |
| Apparel products | 250 x 250 px | 1200 x 1200 px |
| Maximum file size | 16 MB | Under 5 MB for fast loading |

### Supported Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif) — non-animated only
- BMP (.bmp)
- TIFF (.tif, .tiff)
- WebP (.webp)

### Image Content Rules

**Required:**
- Product must be clearly visible and identifiable
- Image must accurately represent the product being sold
- Product should fill 75-90% of the image frame
- Main image must show the actual product (not a lifestyle/context shot)

**Prohibited:**
- Watermarks of any kind (logo, copyright, store name)
- Promotional text overlays ("Sale," "Free Shipping," price badges)
- Borders or frames around the image
- Placeholder images or generic stock photos
- Multiple products in the main image (unless a bundle/multipack)
- Blurry, pixelated, or distorted images
- Logos or icons instead of actual product photos

### Background Requirements
- **Preferred:** Pure white or light solid-color background
- **Acceptable:** Clean, non-distracting backgrounds
- **Not recommended:** Busy lifestyle backgrounds for main image (save for additional images)
- **Apparel exception:** Apparel on a model is acceptable for main image

### Additional Images (additional_image_link)
You can submit up to 10 additional images per product. Use them for:
- Different angles (side, back, top, bottom)
- Close-up details (texture, stitching, ports)
- Product in context (lifestyle/usage shots)
- Color variants
- Scale reference (product next to common object)
- Package contents (what's in the box)

## Audit Process

### Step 1: URL Validation
Check every image_link and additional_image_link:
- URL is accessible (returns HTTP 200)
- No redirect chains (direct URL to image)
- HTTPS preferred (HTTP still works but HTTPS is better)
- URL returns an actual image file (correct MIME type)

### Step 2: Size Compliance
Download and check dimensions:
- Width >= minimum for category
- Height >= minimum for category
- File size < 16 MB
- Aspect ratio is reasonable (not extremely stretched)

### Step 3: Content Analysis
Flag images that likely violate policies:
- Text detection — flag images containing overlaid text
- Border detection — flag images with uniform border pixels
- Fill ratio — calculate what percentage of frame the product occupies
- Background analysis — detect busy or non-white backgrounds
- Duplicate detection — find products sharing the same image URL

### Step 4: Quality Scoring
Score each image 0-100:
- **Size (25 pts):** Meets recommended size (800x800+ or 1200x1200+ for apparel)
- **Background (25 pts):** Clean white or solid background
- **Fill ratio (25 pts):** Product fills 75-90% of frame
- **Compliance (25 pts):** No watermarks, text, borders, or violations

## Common Disapproval Reasons

| Issue | Detection Method | Fix |
|---|---|---|
| Image too small | Check pixel dimensions | Re-shoot or upscale with AI tools |
| Promotional overlay | Text detection on image | Remove text in image editor |
| Watermark present | Logo/pattern detection | Use clean originals without watermark |
| Generic placeholder | Hash comparison to known placeholders | Replace with actual product photo |
| Broken image URL | HTTP HEAD request returns non-200 | Fix URL or re-upload image |
| Wrong product shown | Manual review required | Match image to correct product ID |
| Excessive white space | Fill ratio < 50% | Crop image to show product larger |
| Blurry/low quality | Resolution and sharpness analysis | Re-shoot or use higher quality source |

## Image Optimization Best Practices

### For Higher CTR
1. **Use white backgrounds** for main image — they perform best in Shopping carousels
2. **Show the product at an angle** — slight 3/4 angle is more engaging than flat front
3. **Consistent style** across your catalog — builds brand recognition
4. **High contrast** — product should pop against the background
5. **Show scale** — include a subtle size reference when product size matters

### For Apparel Specifically
1. **On-model shots** outperform flat-lay for main image
2. **Show the full garment** — no cropping at awkward points
3. **Consistent model poses** across the catalog
4. **Ghost mannequin** is an excellent alternative to live models
5. **Include detail shots** as additional images (fabric texture, buttons, labels)

### Technical Optimization
1. **Compress images** — use TinyPNG or similar to reduce file size without quality loss
2. **Use CDN-hosted URLs** — faster loading improves crawl efficiency
3. **Consistent naming convention** — helps with debugging (sku-color-angle.jpg)
4. **Keep originals** — always save uncompressed originals for future re-processing

## Impact
- **Disapproval reduction:** 30-50% of image-related disapprovals can be fixed
- **CTR improvement:** Professional, compliant images improve CTR by 20-35%
- **Impression eligibility:** Compliant images are required for Shopping ad eligibility
- **Free listing performance:** Better images drive more clicks in organic Shopping

## Author
Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | Second Step
