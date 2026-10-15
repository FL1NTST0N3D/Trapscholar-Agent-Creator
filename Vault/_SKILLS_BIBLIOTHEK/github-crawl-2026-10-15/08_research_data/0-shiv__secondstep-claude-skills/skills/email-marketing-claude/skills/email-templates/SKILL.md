# Email Templates — Sub-Skill

## Overview

Template design directly impacts engagement, accessibility, and deliverability. This sub-skill audits HTML email templates for responsive design, dark mode compatibility, image-to-text ratio, accessibility, CTA styling, and rendering across clients.

**Command:** `/email templates`

---

## Template Audit Checklist

- [ ] Responsive design (mobile-first)
- [ ] Dark mode compatible
- [ ] Image-to-text ratio is 60:40 or lower (text-heavier)
- [ ] All images have alt text
- [ ] CTA buttons are min 44x44px (touch target)
- [ ] Unsubscribe link is visible and functional
- [ ] Preheader text is set (not showing "View in browser")
- [ ] Physical address is included
- [ ] Fonts are web-safe or have fallbacks
- [ ] Email width is 600px max
- [ ] Email file size is under 102KB (Gmail clipping threshold)
- [ ] Links are working (no broken URLs)
- [ ] Plain text version exists
- [ ] Renders correctly in top 5 email clients

---

## Responsive Design Audit

### Layout Rules

| Rule | Standard | Why |
|------|----------|-----|
| Max width | 600px | Widest that works across all clients |
| Min font size (body) | 14px (mobile: 16px) | Readability on small screens |
| Min font size (headings) | 22px | Scannable hierarchy |
| Line height | 1.5x font size | Readability |
| Padding | 20px sides minimum | Breathing room on mobile |
| Single column on mobile | Required | Multi-column breaks on small screens |

### Responsive Breakpoints

```css
/* Desktop */
@media screen and (min-width: 601px) {
  .email-container { width: 600px; }
}

/* Mobile */
@media screen and (max-width: 600px) {
  .email-container { width: 100% !important; }
  .column { width: 100% !important; display: block !important; }
  .mobile-hide { display: none !important; }
  .mobile-full-width { width: 100% !important; }
  img { max-width: 100% !important; height: auto !important; }
}
```

### Mobile Optimization Checklist
- [ ] Single column layout on mobile
- [ ] Touch targets min 44x44px
- [ ] Font size 16px+ on mobile (prevents iOS zoom)
- [ ] Images scale to container width
- [ ] CTA button is full-width on mobile
- [ ] Adequate spacing between clickable elements (8px+)
- [ ] No horizontal scrolling

---

## Dark Mode Compatibility

Dark mode is used by 30-40% of email recipients. Emails that ignore dark mode look broken for a significant audience.

### Dark Mode Behavior by Client

| Email Client | Dark Mode Type | Behavior |
|-------------|---------------|----------|
| Apple Mail | Full | Inverts light backgrounds, keeps images |
| Gmail (iOS) | Partial | Inverts some colors, keeps images |
| Gmail (Android) | Partial | Light backgrounds become dark |
| Outlook (Desktop) | Full | Aggressively inverts colors |
| Outlook (iOS) | Partial | Selective color changes |
| Yahoo Mail | None | No dark mode changes |

### Dark Mode Best Practices

1. **Use transparent PNGs** for logos — solid white backgrounds look bad on dark
2. **Add white outline/stroke** to dark logos so they're visible on dark backgrounds
3. **Use CSS `color-scheme`** meta tag:
```html
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
```
4. **Use `@media (prefers-color-scheme: dark)`** for targeted dark mode styles:
```css
@media (prefers-color-scheme: dark) {
  .email-body { background-color: #1a1a1a !important; }
  .text-color { color: #ffffff !important; }
  .email-container { background-color: #2d2d2d !important; }
}
```
5. **Avoid pure white (#ffffff)** backgrounds — use #f5f5f5 (inverts better)
6. **Avoid pure black (#000000)** text — use #333333 (more readable in both modes)
7. **Test in dark mode** before every send

---

## Image-to-Text Ratio

Spam filters flag emails that are mostly images. Some subscribers have images disabled by default.

### Target Ratio: 60% Text, 40% Images

| Ratio | Status | Risk |
|-------|--------|------|
| 80%+ text | Excellent | Very low spam risk |
| 60:40 text:image | Good | Standard, safe |
| 50:50 | Acceptable | Monitor deliverability |
| 40:60 image-heavy | Warning | Higher spam risk |
| Image-only email | Critical | Very high spam risk, broken with images off |

### Image Best Practices
- Always include alt text on every image
- Don't use a single image for the entire email
- Keep image file sizes under 200KB each
- Use compressed formats (WebP where supported, otherwise JPEG/PNG)
- Include key information in text, not embedded in images
- Use background colors behind images as fallback

---

## CTA Button Styling

### Minimum Requirements

| Property | Standard | Why |
|----------|----------|-----|
| Size | 44x44px minimum | Apple's Human Interface Guidelines touch target |
| Padding | 12px top/bottom, 24px left/right | Comfortable click/tap area |
| Font size | 16px minimum | Readable on mobile |
| Font weight | Bold (700) | Stands out from body text |
| Border radius | 4-8px | Modern, clickable appearance |
| Color contrast | 4.5:1 minimum | WCAG AA accessibility |

### Bulletproof Button (Works Everywhere)

```html
<!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:w="urn:schemas-microsoft-com:office:word"
  href="https://example.com"
  style="height:44px;v-text-anchor:middle;width:200px;"
  arcsize="10%" strokecolor="#E87811" fillcolor="#E87811">
<w:anchorlock/>
<center style="color:#ffffff;font-family:Arial,sans-serif;font-size:16px;font-weight:bold;">
  Shop Now
</center>
</v:roundrect>
<![endif]-->
<!--[if !mso]><!-->
<a href="https://example.com" style="background-color:#E87811;border-radius:4px;color:#ffffff;display:inline-block;font-family:Arial,sans-serif;font-size:16px;font-weight:bold;line-height:44px;text-align:center;text-decoration:none;width:200px;">
  Shop Now
</a>
<!--<![endif]-->
```

### CTA Text Best Practices

| Instead Of | Use | Why |
|-----------|-----|-----|
| Click Here | Shop Now | Action-oriented |
| Submit | Get My Free Guide | Benefit-oriented |
| Learn More | See How It Works | Specific |
| Buy Now | Add to Cart | Lower commitment |
| Download | Get Your Copy | Ownership language |

---

## Accessibility Standards

### WCAG 2.1 AA for Email

| Requirement | Standard | Check |
|-------------|----------|-------|
| Color contrast (text) | 4.5:1 ratio minimum | Use contrast checker tool |
| Color contrast (large text) | 3:1 ratio minimum | 18px+ or 14px bold |
| Alt text | All images | Describe content, not "image of..." |
| Link text | Descriptive | Not "click here" |
| Reading order | Logical | Makes sense without CSS |
| Language | Set in HTML | `<html lang="en">` |
| Table role | `role="presentation"` | For layout tables |

### Font Stack

```css
/* Primary: System fonts (fast, accessible) */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
  'Helvetica Neue', Arial, sans-serif;

/* Fallback: Web-safe only */
font-family: Arial, Helvetica, sans-serif;

/* Serif alternative */
font-family: Georgia, 'Times New Roman', serif;
```

**Never use:** Custom web fonts without fallbacks. Many email clients strip `@font-face`.

---

## Email Client Rendering

### Top 10 Email Clients (Global Market Share)

| Client | Share | Key Issues |
|--------|-------|-----------|
| Apple Mail | 57% | Most standards-compliant |
| Gmail | 28% | Strips `<style>` in non-app versions |
| Outlook (Desktop) | 7% | Uses Word rendering engine (!), breaks everything |
| Yahoo Mail | 3% | Limited CSS support |
| Outlook (Mobile) | 2% | Better than desktop but still limited |
| Samsung Mail | 1% | Android default, decent support |
| Thunderbird | <1% | Good standards support |

### Gmail-Specific Issues
- File size limit: **102KB** (clips email beyond this)
- Strips `<style>` tags in non-Gmail app
- Requires inline CSS
- No `@media` query support in some versions
- Caches images aggressively

### Outlook-Specific Issues
- Uses Microsoft Word rendering engine
- No `border-radius`, `background-image`, or `CSS3`
- Requires VML for rounded buttons
- `max-width` doesn't work — use `width` attribute on tables
- Conditional comments needed: `<!--[if mso]>...<![endif]-->`

---

## Template Scoring

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| Responsive (mobile-friendly) | 20% | 0-100 |
| Dark mode compatible | 15% | 0-100 |
| Image:text ratio (60:40 or better) | 15% | 0-100 |
| Alt text on all images | 10% | 0 or 100 |
| CTA button meets standards | 15% | 0-100 |
| Under 102KB file size | 10% | 0 or 100 |
| Accessibility (contrast, lang, roles) | 10% | 0-100 |
| Unsubscribe link visible | 5% | 0 or 100 |
