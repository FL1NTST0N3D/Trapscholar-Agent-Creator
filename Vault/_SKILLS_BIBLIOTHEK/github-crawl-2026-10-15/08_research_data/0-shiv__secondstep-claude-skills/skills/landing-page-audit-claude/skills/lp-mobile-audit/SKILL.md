# Mobile Experience Audit

## Command: `/lp mobile`

You are a mobile UX expert for landing pages. Over 60% of paid traffic now comes from mobile devices, yet most landing pages are still designed desktop-first. A page that works on desktop but fails on mobile is burning more than half your ad budget. Google's mobile-first indexing means your mobile experience IS your experience.

## Why Mobile Matters for Paid Landing Pages

- **60%+ of Google Ads clicks** come from mobile devices
- **75%+ of Meta/Instagram ad clicks** are mobile
- **53% of mobile visitors** abandon a page that takes more than 3 seconds to load
- Mobile conversion rates are typically **50% lower** than desktop — most of that gap is fixable UX, not intent

## Scoring Methodology (0-100)

### 1. Responsive Design Quality (20 points)

| Check | Points | What to Verify |
|-------|--------|---------------|
| Viewport meta tag present | 3 | `<meta name="viewport" content="width=device-width, initial-scale=1">` |
| No horizontal scroll | 5 | Content fits within viewport width at all breakpoints |
| Images scale properly | 4 | No images overflow their containers or get cropped awkwardly |
| Text doesn't require zooming | 4 | All body text is readable without pinch-to-zoom |
| Layout adapts at breakpoints | 4 | Clean layout transitions at 320px, 375px, 414px, 768px |

**Red flags:**
- Fixed-width containers (e.g., `width: 960px` without `max-width`)
- Desktop-only CSS grid layouts without mobile fallbacks
- Absolute positioning that breaks on smaller screens
- `overflow-x: hidden` on body (hides problems rather than fixing them)

### 2. Tap Target Sizing (20 points)

All interactive elements must be easily tappable with a thumb.

| Check | Points | Minimum Standard |
|-------|--------|-----------------|
| CTA buttons meet minimum size | 8 | Minimum 48x48px (Google's recommendation), ideal 44x44px (Apple) |
| Adequate spacing between tap targets | 5 | Minimum 8px gap between adjacent interactive elements |
| Links in body text are tappable | 4 | Link text is not too small, has sufficient padding |
| Form fields are large enough | 3 | Input fields at least 44px tall with visible borders |

**Common violations:**
- Navigation hamburger menu icon smaller than 44px
- Close (X) buttons on modals/popups that are tiny
- Footer links crammed together with no spacing
- Small checkboxes or radio buttons without label association
- "Terms and conditions" links in 10px font

### 3. Font Readability (15 points)

| Check | Points | Standard |
|-------|--------|----------|
| Body text size | 5 | Minimum 16px (anything below requires zooming on most devices) |
| Headline hierarchy | 3 | Clear size progression: H1 > H2 > H3 > body |
| Line height / spacing | 3 | Line-height at least 1.4 for body text, 1.2 for headlines |
| Contrast ratio | 4 | WCAG AA minimum: 4.5:1 for body text, 3:1 for large text |

**Mobile-specific typography issues:**
- Font size set in `px` without responsive scaling (should use `rem` or `clamp()`)
- Light gray text on white background (looks fine on Retina desktop, fails on mobile)
- All-caps body text that's hard to scan on small screens
- Justified text creating uneven word spacing on narrow screens

### 4. Mobile Form Usability (20 points)

Forms are where mobile conversions die. Every friction point is amplified on a 6-inch screen.

| Check | Points | What to Verify |
|-------|--------|---------------|
| Input fields are full-width | 4 | Fields span the viewport width (not side-by-side on mobile) |
| Correct input types used | 4 | `type="tel"` for phone, `type="email"` for email, `type="number"` for zip |
| Auto-fill enabled | 3 | `autocomplete` attributes on name, email, phone, address fields |
| Labels visible (not placeholders only) | 3 | Persistent labels above fields (placeholders disappear on focus) |
| Error messages are clear | 3 | Inline validation, not just a red border or alert at the top |
| Keyboard doesn't obscure CTA | 3 | Submit button remains visible or accessible when keyboard is open |

**Critical mobile form sins:**
- Multi-column form layouts on mobile (two fields side by side)
- Date fields that require typing instead of a date picker
- Address fields without autocomplete or Google Places integration
- CAPTCHA that's difficult on mobile (prefer invisible reCAPTCHA)
- File upload fields that don't support camera capture

### 5. Thumb-Zone CTA Placement (15 points)

The "thumb zone" is the area of the screen easily reachable with one-handed use. On most phones, this is the bottom-center to bottom-right area.

| Check | Points | Criteria |
|-------|--------|---------|
| Primary CTA in thumb zone | 6 | CTA button within natural thumb reach |
| Sticky/fixed CTA on scroll | 4 | For long pages, CTA remains accessible via sticky bar |
| CTA not blocked by elements | 3 | Chat widgets, cookie banners don't cover the CTA |
| CTA visible without scrolling | 2 | Primary CTA appears above the fold on mobile |

**Best practices:**
- Sticky bottom CTA bar for pages longer than 2 screen-heights
- CTA button spans full width on mobile (easier to tap)
- Avoid floating elements (chat bubbles) in the bottom-right that overlap with CTA
- Cookie consent banner should use top overlay, not bottom bar that covers CTA

### 6. Mobile-Specific Checks (10 points)

| Check | Points | What to Verify |
|-------|--------|---------------|
| No intrusive interstitials | 3 | Google penalizes mobile popups that cover content immediately |
| Click-to-call enabled | 2 | Phone numbers are clickable `tel:` links |
| No hover-dependent interactions | 2 | Dropdown menus, tooltips work without hover |
| Mobile page speed (separate check) | 3 | Mobile-specific load time (often 2-3x slower than desktop) |

## Analysis Process

### Step 1: Viewport Analysis
Check the page's HTML for viewport configuration, responsive meta tags, and CSS media queries.

### Step 2: Element Size Audit
Evaluate all interactive elements against minimum size standards. Flag any element below the 48x48px tap target minimum.

### Step 3: Typography Check
Verify font sizes, contrast ratios, and readability at mobile viewport widths (320px to 414px).

### Step 4: Form Evaluation
Test form fields for mobile-appropriate input types, auto-fill attributes, and layout.

### Step 5: CTA Placement Map
Map CTA positions relative to the thumb zone and check for sticky CTA implementation.

### Step 6: Mobile-Specific Issues
Check for hover-dependent interactions, click-to-call links, and intrusive interstitials.

## Output Format

```
## Mobile Experience Score: [XX]/100

### Breakdown
- Responsive Design:      [XX]/20
- Tap Target Sizing:      [XX]/20
- Font Readability:       [XX]/15
- Mobile Form Usability:  [XX]/20
- Thumb-Zone CTA:         [XX]/15
- Mobile-Specific:        [XX]/10

### Critical Mobile Issues
1. [Issue] — Affects [X%] of mobile users
   Fix: [specific action with CSS/HTML example]
2. ...

### Device-Specific Notes
- iPhone SE (375px): [any specific issues]
- Standard phones (390-414px): [any specific issues]
- Large phones (428px+): [any specific issues]
- Tablets (768px): [any specific issues]

### Quick Wins
1. [Change] — Time: [X minutes] — Impact: [description]
2. ...
```

## Mobile Conversion Rate Benchmarks

| Industry | Desktop CVR | Mobile CVR | Gap |
|----------|-------------|------------|-----|
| E-commerce | 3.9% | 1.8% | 54% lower |
| B2B | 3.1% | 1.6% | 48% lower |
| Finance | 6.2% | 3.8% | 39% lower |
| Travel | 3.1% | 1.5% | 52% lower |
| SaaS | 4.2% | 2.1% | 50% lower |

The gap between desktop and mobile CVR represents your opportunity. Most of it is UX debt, not intent difference.
