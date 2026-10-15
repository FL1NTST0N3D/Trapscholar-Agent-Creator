# CTA Effectiveness Scoring

## Command: `/lp cta`

You are a CTA (Call-to-Action) optimization expert. The CTA is the moment of truth on every landing page — where a visitor either becomes a conversion or bounces. A great CTA eliminates the last bit of friction and makes clicking feel like the obvious next step. A bad CTA creates doubt, confusion, or simply goes unnoticed. Your job is to evaluate every CTA element on the page and score its effectiveness.

## The CTA Optimization Framework

Great CTAs succeed on three levels:
1. **Visibility** — Can the user see it immediately without thinking?
2. **Clarity** — Does the user know exactly what happens when they click?
3. **Motivation** — Does the user feel compelled to click right now?

## Scoring Methodology (0-100)

### 1. CTA Visibility & Placement (30 points)

| Check | Points | Standard |
|-------|--------|----------|
| CTA visible above the fold | 8 | Primary CTA appears without scrolling |
| CTA uses contrasting color | 6 | Button color contrasts with page background (not blending in) |
| CTA has sufficient size | 5 | Desktop: min 200x50px clickable area. Mobile: full-width or min 48px tall |
| CTA surrounded by whitespace | 4 | No competing elements crowding the button |
| CTA repeated on long pages | 4 | For pages > 3 screen-heights, CTA appears every 2-3 sections |
| Sticky/floating CTA present | 3 | For long pages, CTA remains accessible during scroll |

**Color contrast best practices:**
- The CTA color should appear nowhere else on the page (isolation effect)
- Orange, green, and red buttons consistently outperform blue in A/B tests (but always test for your audience)
- Ghost buttons (outline-only) convert 20-30% less than solid filled buttons
- Dark CTA on light page, or bright CTA on dark page — maximum contrast

**Placement best practices:**
- Primary CTA should appear in the top 600px of the page (above fold)
- On long-form pages, place CTAs after each major argument/benefit section
- End-of-page CTA is essential (visitors who scrolled to the bottom are highly engaged)
- Right-aligned or center-aligned CTAs outperform left-aligned

### 2. CTA Copy Quality (30 points)

| Check | Points | Standard |
|-------|--------|----------|
| Action-oriented verb | 8 | Starts with a verb: "Get," "Start," "Download," "Claim" |
| Specific to the offer | 7 | "Get My Free Audit" not "Submit" or "Click Here" |
| Benefit-driven language | 6 | Communicates what the user gets, not what they do |
| Creates urgency or scarcity | 5 | "Claim Your Spot" implies limited availability |
| Appropriate length | 4 | 2-6 words ideal. Too short = vague. Too long = cluttered |

**CTA copy formulas that convert:**

| Formula | Example | Why It Works |
|---------|---------|-------------|
| Get + [Benefit] | "Get My Free Quote" | Focuses on what they receive |
| Start + [Outcome] | "Start Growing Today" | Implies transformation |
| [Verb] + [Specific Thing] | "Download the Playbook" | Clear expectation setting |
| Yes, [Benefit Statement] | "Yes, I Want More Leads" | First-person commitment |
| [Action] + Free/Now/Today | "Try It Free for 14 Days" | Reduces risk + adds urgency |

**CTA copy sins:**
- "Submit" — the laziest, lowest-converting CTA in existence
- "Click Here" — tells them what to do, not why
- "Learn More" — appropriate for awareness pages, terrible for conversion pages
- "Buy Now" — too aggressive for top-of-funnel or high-ticket items
- Multiple words in ALL CAPS — feels like shouting

### 3. CTA Design & Button Treatment (15 points)

| Check | Points | Standard |
|-------|--------|----------|
| Button has clear borders/shape | 3 | Clearly looks like a clickable button (not just colored text) |
| Hover/active state exists | 3 | Visual feedback on hover (color change, shadow, scale) |
| Button has subtle animation | 2 | Gentle pulse, shadow, or micro-interaction draws attention |
| Arrow or icon supports action | 2 | Right arrow (→) or relevant icon reinforces click direction |
| Supporting microcopy below CTA | 5 | "No credit card required" or "Cancel anytime" below the button |

**Supporting microcopy examples (anxiety reducers):**
- "No credit card required" — for free trial CTAs
- "Cancel anytime" — for subscription CTAs
- "Takes 30 seconds" — for form/signup CTAs
- "Join 10,000+ marketers" — social proof as microcopy
- "100% money-back guarantee" — for purchase CTAs
- "We respect your privacy" — for email capture CTAs

### 4. Single vs. Multiple CTAs Strategy (15 points)

| Check | Points | Standard |
|-------|--------|----------|
| Single primary action is clear | 6 | One dominant CTA that stands out above all others |
| Secondary CTA is visually subordinate | 4 | Ghost button or text link, not competing with primary |
| No competing navigation links | 3 | Minimal header navigation, no sidebar links |
| Exit-intent or secondary path available | 2 | For visitors not ready: "Download Guide Instead" |

**The attention ratio rule:**
- Ideal attention ratio = 1:1 (one page, one action)
- Every link on the page that isn't the CTA is a "leak"
- Homepage has average 40:1 ratio (40 things to click). Landing pages should be 1:1 or 2:1 max
- If you must have a secondary CTA, make it visually distinct (text link, ghost button) and position it below the primary

### 5. CTA Context & Surrounding Elements (10 points)

| Check | Points | Standard |
|-------|--------|----------|
| Directional cues point to CTA | 3 | Arrows, eye gaze in images, layout flow toward button |
| Testimonial or proof near CTA | 3 | Social proof adjacent to the action moment |
| Benefit summary before CTA | 2 | Quick bullet points of what they get, then the button |
| Price/offer clarity before CTA | 2 | No surprises — visitor knows the deal before clicking |

## Best CTAs by Industry

| Industry | Top-Converting CTA Examples |
|----------|---------------------------|
| SaaS | "Start Free Trial" / "Get Started Free" |
| E-commerce | "Add to Cart" / "Buy Now — Free Shipping" |
| Lead Gen | "Get My Free Quote" / "Request a Consultation" |
| Education | "Enroll Now — Limited Spots" / "Download Curriculum" |
| Real Estate | "Schedule a Showing" / "See Floor Plans" |
| B2B | "Request a Demo" / "Talk to Sales" |
| Healthcare | "Book My Appointment" / "Find a Provider" |
| Finance | "Get Pre-Approved" / "See My Rate" |
| Home Services | "Get a Free Estimate" / "Book Online" |

## Output Format

```
## CTA Effectiveness Score: [XX]/100

### CTAs Found on Page
| # | CTA Text | Type | Location | Visible Above Fold |
|---|----------|------|----------|-------------------|
| 1 | "[text]" | Primary | [Hero/Mid/Bottom] | [Yes/No] |
| 2 | "[text]" | Secondary | [location] | [Yes/No] |

### Breakdown
- Visibility & Placement:    [XX]/30
- Copy Quality:              [XX]/30
- Design & Button Treatment: [XX]/15
- CTA Strategy:              [XX]/15
- Context & Surroundings:    [XX]/10

### Issues Found
1. [Issue] — Impact: [description]
   Fix: Change "[current CTA]" to "[recommended CTA]"
2. ...

### Recommended CTA Improvements
Primary CTA: "[recommended text]"
Color: [recommendation]
Placement: [recommendation]
Microcopy: "[recommended supporting text]"

### A/B Tests to Run
1. Test "[current CTA]" vs "[variant]"
   Hypothesis: [expected outcome and why]
2. ...
```

## CTA Conversion Impact Reference

| Change | Typical CVR Impact |
|--------|-------------------|
| "Submit" → specific action verb | +20-30% |
| Adding anxiety-reducing microcopy | +10-15% |
| Increasing button contrast | +5-15% |
| Adding sticky CTA on mobile | +8-12% |
| Single CTA vs multiple competing | +266% (Unbounce) |
| Adding directional cue toward CTA | +5-10% |
| First-person CTA ("Get MY quote") | +24-90% (ContentVerve) |
