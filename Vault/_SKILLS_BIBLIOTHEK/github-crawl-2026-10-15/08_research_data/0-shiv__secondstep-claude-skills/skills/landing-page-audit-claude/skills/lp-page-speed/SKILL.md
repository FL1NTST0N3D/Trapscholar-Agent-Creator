# Page Speed Audit

## Command: `/lp speed`

You are a page speed optimization expert for landing pages. Speed is one of the three highest-weighted dimensions in a landing page audit because slow pages kill conversions before anyone even sees your content. Google's research shows that as page load time goes from 1s to 3s, bounce probability increases 32%. From 1s to 5s, it increases 90%.

## Core Web Vitals — The Three Metrics That Matter

### 1. Largest Contentful Paint (LCP)
**What it measures:** How long it takes for the largest visible element (hero image, video, headline text block) to fully render.

| Rating | Threshold | Score |
|--------|-----------|-------|
| Good | < 2.5 seconds | 30-35 points |
| Needs Improvement | 2.5 - 4.0 seconds | 15-29 points |
| Poor | > 4.0 seconds | 0-14 points |

**Common LCP killers on landing pages:**
- Unoptimized hero images (JPEG at 3000px wide, no WebP)
- Hero video that isn't lazy-loaded or uses autoplay without preload
- Render-blocking CSS/JS in the `<head>`
- Web fonts that block text rendering (FOIT — Flash of Invisible Text)
- Third-party scripts loading before critical content (chat widgets, analytics)
- No CDN — serving assets from origin server

**Fix playbook:**
- Serve hero image in WebP/AVIF format with explicit width/height attributes
- Preload the LCP image: `<link rel="preload" as="image" href="hero.webp">`
- Inline critical CSS, defer non-critical CSS
- Use `font-display: swap` for all web fonts
- Defer third-party scripts below the fold

### 2. Interaction to Next Paint (INP)
**What it measures:** The responsiveness of the page to user interactions (clicks, taps, key presses). Replaced FID (First Input Delay) as of March 2024.

| Rating | Threshold | Score |
|--------|-----------|-------|
| Good | < 200ms | 15-20 points |
| Needs Improvement | 200 - 500ms | 8-14 points |
| Poor | > 500ms | 0-7 points |

**Common INP issues on landing pages:**
- Heavy JavaScript execution blocking the main thread
- Form validation scripts that freeze the UI
- Animated elements using JavaScript instead of CSS
- Chat widget scripts monopolizing the main thread
- Analytics/tracking scripts firing on every interaction
- Large DOM size causing slow re-renders

**Fix playbook:**
- Break up long JavaScript tasks (> 50ms) into smaller chunks
- Use `requestIdleCallback` for non-critical JS
- Move animations to CSS transforms/transitions (GPU-accelerated)
- Lazy-load chat widgets (load on scroll or after 5 seconds)
- Use `requestAnimationFrame` for scroll-triggered animations

### 3. Cumulative Layout Shift (CLS)
**What it measures:** Visual stability. How much the page layout shifts unexpectedly as it loads.

| Rating | Threshold | Score |
|--------|-----------|-------|
| Good | < 0.1 | 10-15 points |
| Needs Improvement | 0.1 - 0.25 | 5-9 points |
| Poor | > 0.25 | 0-4 points |

**Common CLS causes on landing pages:**
- Images without width/height attributes or CSS aspect-ratio
- Dynamically injected content (cookie banners, notification bars, chat widgets)
- Web fonts causing text reflow (font size difference between fallback and loaded font)
- Ads or third-party embeds loading late and pushing content down
- Above-the-fold content that loads asynchronously

**Fix playbook:**
- Always set explicit width/height on images and videos
- Reserve space for dynamic elements with CSS `min-height`
- Use `font-display: optional` if font match is close, `swap` if not
- Load cookie/consent banners as overlays, not inline elements
- Use CSS `aspect-ratio` for responsive media containers

## Beyond Core Web Vitals — Additional Speed Checks (30 points)

### Server Response Time (TTFB) — 8 points
| Rating | Threshold | Points |
|--------|-----------|--------|
| Good | < 200ms | 7-8 |
| Acceptable | 200 - 600ms | 4-6 |
| Poor | > 600ms | 0-3 |

**Check:** Is the server using HTTP/2 or HTTP/3? Is there a CDN? Is there server-side caching?

### Total Page Weight — 7 points
| Rating | Threshold | Points |
|--------|-----------|--------|
| Lean | < 1 MB | 6-7 |
| Average | 1 - 3 MB | 3-5 |
| Bloated | > 3 MB | 0-2 |

**Check:** Total transfer size, number of requests, largest individual resources.

### Image Optimization — 5 points
- Are images served in next-gen formats (WebP, AVIF)? +2
- Are images properly sized (not 3000px wide for a 600px container)? +1.5
- Is lazy loading used for below-the-fold images? +1.5

### Code Optimization — 5 points
- Is CSS minified? +1
- Is JavaScript minified? +1
- Are unused CSS/JS removed? +1.5
- Is code splitting used (not loading everything upfront)? +1.5

### Render-Blocking Resources — 5 points
- Number of render-blocking scripts in `<head>`: 0 = +2.5, 1-2 = +1, 3+ = 0
- Number of render-blocking stylesheets: 1 (critical CSS) = +2.5, 2-3 = +1, 4+ = 0

## Scoring Summary

| Component | Max Points |
|-----------|-----------|
| LCP | 35 |
| INP | 20 |
| CLS | 15 |
| TTFB | 8 |
| Page Weight | 7 |
| Image Optimization | 5 |
| Code Optimization | 5 |
| Render-Blocking | 5 |
| **Total** | **100** |

## Data Collection

### Option 1: PageSpeed Insights API (Automated)
If the user has a PageSpeed Insights API key, use `scripts/page_speed_checker.py` to fetch real data:
```bash
python scripts/page_speed_checker.py --url "https://example.com" --api-key "YOUR_KEY"
```

### Option 2: Manual Analysis
If no API key is available:
1. Ask the user to run a PageSpeed Insights test at https://pagespeed.web.dev/
2. Ask for the scores and specific metric values
3. Alternatively, analyze the page HTML source for common issues

### Option 3: Inference from HTML
Analyze the HTML source code to identify likely speed issues:
- Count render-blocking resources
- Check image formats and sizes
- Identify heavy third-party scripts
- Check for lazy loading implementation
- Look for inline critical CSS

## Output Format

```
## Page Speed Score: [XX]/100

### Core Web Vitals
| Metric | Value | Rating | Points |
|--------|-------|--------|--------|
| LCP | [X.Xs] | [Good/NI/Poor] | [XX]/35 |
| INP | [XXXms] | [Good/NI/Poor] | [XX]/20 |
| CLS | [X.XX] | [Good/NI/Poor] | [XX]/15 |

### Additional Metrics
| Metric | Value | Points |
|--------|-------|--------|
| TTFB | [XXXms] | [X]/8 |
| Page Weight | [X.X MB] | [X]/7 |
| Image Optimization | [details] | [X]/5 |
| Code Optimization | [details] | [X]/5 |
| Render-Blocking | [X resources] | [X]/5 |

### Speed Killers Found
1. [Issue] — Impact: [estimated LCP/INP/CLS impact]
   Fix: [specific action]
2. ...

### Priority Fixes (by conversion impact)
1. [Fix] — Estimated load time reduction: [Xs] — CVR impact: [+X%]
2. ...
```

## Speed-to-Conversion Impact Reference

Use these benchmarks when estimating conversion impact:

| Speed Improvement | Estimated CVR Impact |
|-------------------|---------------------|
| LCP from 4s to 2.5s | +15-25% conversions |
| LCP from 2.5s to 1.5s | +5-10% conversions |
| Removing 1s of load time | +7% conversions (Aberdeen) |
| Achieving all "Good" CWV | +24% fewer abandons (Google) |
| Mobile load time < 3s | +53% fewer bounces (Google) |
