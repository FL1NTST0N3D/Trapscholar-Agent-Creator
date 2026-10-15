---
name: pmax-asset-audit
description: "Audit Performance Max asset groups for completeness, compliance with Google specifications, and performance rating distribution. Checks text assets (headlines, descriptions), image assets (landscape, square, portrait), video assets, and logos."
allowed-tools:
  - Bash
  - Read
  - Grep
---

# PMax Asset Audit Skill

## Purpose

This skill audits every asset within a Performance Max campaign's asset groups against Google's official specifications and best practices. It identifies missing assets, non-compliant formats, underperforming creatives, and opportunities to improve asset diversity.

## Trigger

Activated by `/pmax assets` or as part of `/pmax audit` (full audit orchestration).

## Data Requirements

Ask the user for:
1. Asset group export from Google Ads (CSV or paste)
2. Asset performance ratings (Best/Good/Low/Unrated) if available
3. Number of asset groups in the campaign
4. Whether the account has access to Google Ads API data

## Text Asset Specifications

### Headlines
- **Character limit**: 30 characters maximum
- **Minimum required**: 3 headlines (Google minimum to run)
- **Recommended**: 5 headlines (Google recommendation)
- **Maximum allowed**: 15 headlines
- **Ideal target**: 15 headlines for maximum combinatorial testing
- **Best practices**:
  - Include at least 1 headline with brand name
  - Include at least 1 headline with primary keyword/offer
  - Include at least 1 headline with call-to-action
  - Vary headline angles: benefit, feature, urgency, social proof, question
  - Avoid redundant headlines that say the same thing differently
  - Use title case consistently
  - Do not use ALL CAPS (policy violation risk)
  - Avoid excessive punctuation (!!!, ???)
  - Include dynamic keyword insertion where relevant: {KeyWord:Default}

### Long Headlines
- **Character limit**: 90 characters maximum
- **Minimum required**: 1 long headline
- **Recommended**: 5 long headlines
- **Maximum allowed**: 5 long headlines
- **Best practices**:
  - Long headlines appear as the first line of your ad in some layouts
  - Treat these as expanded value propositions
  - Include both a benefit and a call-to-action when possible
  - These replace short headlines on larger display placements
  - Must be compelling standalone — they may appear without a description

### Descriptions
- **Character limit**: 90 characters maximum (first description), 90 characters (additional)
- **Minimum required**: 2 descriptions
- **Recommended**: 5 descriptions (Google best practice)
- **Maximum allowed**: 5 descriptions
- **Ideal target**: 4-5 descriptions for sufficient variety
- **Best practices**:
  - First description is most important (shown most often)
  - Include specific numbers: prices, percentages, quantities
  - Address customer pain points directly
  - Include social proof elements (e.g., "Trusted by 10,000+ customers")
  - End with a clear call-to-action
  - Avoid repeating information already in headlines
  - Each description should work independently AND in combination with any headline

### Business Name
- **Character limit**: 25 characters maximum
- **Required**: Yes (1 business name)
- **Best practices**: Use your official brand name, avoid taglines here

## Image Asset Specifications

### Landscape Images
- **Dimensions**: 1200 x 628 pixels (minimum: 600 x 314)
- **Aspect ratio**: 1.91:1
- **File size**: Maximum 5120 KB
- **Format**: JPG or PNG
- **Minimum required**: 1 landscape image
- **Recommended**: 4+ landscape images
- **Maximum allowed**: 20 images (across all orientations)
- **Best practices**:
  - No text overlay exceeding 20% of image area
  - High-resolution product/lifestyle photography
  - Avoid white/blank backgrounds — use contextual imagery
  - Ensure subject is centered and visible at small sizes
  - Test: product-focused, lifestyle, benefit-illustration, and brand imagery

### Square Images
- **Dimensions**: 1200 x 1200 pixels (minimum: 300 x 300)
- **Aspect ratio**: 1:1
- **File size**: Maximum 5120 KB
- **Format**: JPG or PNG
- **Minimum required**: 1 square image
- **Recommended**: 4+ square images
- **Maximum allowed**: 20 images (shared with landscape)
- **Best practices**:
  - Square images appear on more placements than landscape
  - Prioritize square format if you have limited creative resources
  - Ensure images look good cropped to square — no critical elements at edges
  - Good for product shots, headshots, icons, app screenshots

### Portrait Images
- **Dimensions**: 960 x 1200 pixels (minimum: 480 x 600)
- **Aspect ratio**: 4:5
- **File size**: Maximum 5120 KB
- **Format**: JPG or PNG
- **Minimum required**: 0 (optional but strongly recommended)
- **Recommended**: 2+ portrait images
- **Maximum allowed**: 20 images (shared pool)
- **Best practices**:
  - Portrait images are critical for mobile-first placements
  - YouTube Shorts, Discover feed, and Gmail all favor portrait
  - Without portrait images, Google will auto-crop your landscape images (often badly)
  - Include at least 2 portrait images to avoid auto-crop issues

### Total Image Recommendations
- **Minimum to run**: 1 landscape + 1 square = 2 images
- **Google recommendation**: 5+ images across orientations
- **Ideal target**: 15-20 images with mix of all three orientations
- **Diversity targets**: At least 4 landscape, 4 square, 2 portrait

## Video Asset Specifications

### Horizontal Video
- **Aspect ratio**: 16:9
- **Minimum duration**: 10 seconds
- **Recommended duration**: 15-30 seconds
- **Maximum duration**: No strict max (but 15-60s performs best)
- **Platform**: Must be uploaded to YouTube (linked channel)
- **Best practices**:
  - YouTube in-stream and in-feed placements
  - Include branding within first 5 seconds
  - Clear call-to-action in final frames
  - Captions/subtitles recommended (80% of mobile video watched muted)

### Vertical Video
- **Aspect ratio**: 9:16
- **Recommended duration**: 15-60 seconds (Shorts: <60s)
- **Platform**: YouTube (linked channel)
- **Best practices**:
  - Critical for YouTube Shorts inventory
  - Without vertical video, Google auto-generates from your images (low quality)
  - Hook within first 3 seconds
  - Native, authentic feel outperforms polished production

### Square Video
- **Aspect ratio**: 1:1
- **Recommended duration**: 15-30 seconds
- **Platform**: YouTube (linked channel)
- **Best practices**:
  - Cross-platform versatility
  - Works well in Discover and Gmail placements
  - Good compromise if you can only produce one video format

### Total Video Recommendations
- **Minimum to run**: 0 (PMax will auto-generate from images — NOT recommended)
- **Google recommendation**: 1+ video
- **Ideal target**: 5 videos (2 horizontal, 2 vertical, 1 square)
- **Critical warning**: If you provide NO video, Google will auto-generate a slideshow from your images. These auto-generated videos almost always perform poorly and look unprofessional. ALWAYS provide at least 1 real video.

## Logo Specifications

### Square Logo
- **Dimensions**: 1200 x 1200 pixels (minimum: 128 x 128)
- **Aspect ratio**: 1:1
- **File size**: Maximum 5120 KB
- **Format**: JPG or PNG (PNG with transparency recommended)
- **Required**: Yes (at least 1)
- **Maximum**: 5 logos

### Landscape Logo
- **Dimensions**: 1200 x 300 pixels (minimum: 512 x 128)
- **Aspect ratio**: 4:1
- **File size**: Maximum 5120 KB
- **Format**: JPG or PNG
- **Required**: No (but recommended)
- **Maximum**: 5 logos
- **Best practices**: Horizontal logo variant for wide placements

## Asset Performance Ratings

Google assigns performance labels to assets after sufficient data (typically 2-4 weeks):

| Rating | Meaning | Action |
|---|---|---|
| **Best** | Top-performing asset in its category | Keep, create variations of this asset |
| **Good** | Performing well, above average | Keep, monitor for changes |
| **Low** | Underperforming relative to other assets | Replace with new creative after 30 days |
| **Unrated** | Insufficient data to rate | Wait for more data (2-4 weeks minimum) |
| **Pending** | Just added, being evaluated | Check back in 1-2 weeks |

### Healthy Rating Distribution
- **Best**: 20-35% of assets
- **Good**: 35-50% of assets
- **Low**: <15% of assets (replace these)
- **Unrated**: <15% of assets (acceptable if recently added)

### Warning Signs
- More than 30% of assets rated "Low" → creative refresh needed
- More than 40% "Unrated" after 30 days → insufficient campaign volume
- Zero "Best" rated assets → creative strategy fundamentally misaligned
- All assets same rating → insufficient testing variety

## Scoring Rubric (0-100)

### Asset Completeness Score (0-50 points)

| Criteria | Points | Condition |
|---|---|---|
| Headlines | 10 | 15 headlines = 10pts, 5-14 = 7pts, 3-4 = 4pts, <3 = 0pts |
| Long Headlines | 5 | 5 = 5pts, 3-4 = 3pts, 1-2 = 1pt, 0 = 0pts |
| Descriptions | 5 | 5 = 5pts, 3-4 = 3pts, 2 = 1pt, <2 = 0pts |
| Landscape Images | 8 | 4+ = 8pts, 2-3 = 5pts, 1 = 2pts, 0 = 0pts |
| Square Images | 7 | 4+ = 7pts, 2-3 = 4pts, 1 = 2pts, 0 = 0pts |
| Portrait Images | 5 | 2+ = 5pts, 1 = 3pts, 0 = 0pts |
| Videos | 7 | 3+ orientations = 7pts, 1-2 = 4pts, 0 = 0pts |
| Logos | 3 | Square + Landscape = 3pts, Square only = 2pts, 0 = 0pts |

### Asset Performance Score (0-50 points)

| Criteria | Points | Condition |
|---|---|---|
| Best-rated % | 15 | >30% = 15pts, 20-30% = 10pts, 10-20% = 5pts, <10% = 0pts |
| Low-rated % | 15 | <10% = 15pts, 10-20% = 10pts, 20-30% = 5pts, >30% = 0pts |
| Rating coverage | 10 | >80% rated = 10pts, 60-80% = 7pts, 40-60% = 4pts, <40% = 0pts |
| Creative diversity | 10 | All angles covered = 10pts, most = 7pts, few = 3pts |

## Output Format

```
## Asset Audit Results

### Asset Completeness: XX/50
| Asset Type | Count | Required | Recommended | Status |
|---|---|---|---|---|
| Headlines | X | 3 | 15 | OK/WARNING/CRITICAL |
| Long Headlines | X | 1 | 5 | OK/WARNING/CRITICAL |
| ... | | | | |

### Asset Performance: XX/50
| Rating | Count | % | Target | Status |
|---|---|---|---|---|
| Best | X | X% | >30% | OK/WARNING |
| Good | X | X% | >40% | OK/WARNING |
| Low | X | X% | <15% | OK/WARNING |
| Unrated | X | X% | <15% | OK/WARNING |

### Total Asset Score: XX/100

### Critical Issues
- [List any critical findings]

### Recommendations
1. [Prioritized action items]
```
