# DKI Helper — Dynamic Keyword Insertion, IF Functions & Ad Customizers

## Command: `/copy dki`

Set up Dynamic Keyword Insertion (DKI), IF functions, countdown timers, and location insertion with correct syntax, formatting rules, and best-practice guidelines.

## What Is Dynamic Keyword Insertion (DKI)?

DKI automatically replaces a placeholder in your ad with the keyword that triggered the ad. This makes ads hyper-relevant to the search query, increasing CTR and Quality Score.

### Basic Syntax

```
{KeyWord:Default Text}
```

- `KeyWord` — The capitalization format (see table below)
- `Default Text` — What shows if the keyword is too long or can't be inserted
- The DEFAULT TEXT counts toward the character limit, not the DKI syntax

### Capitalization Options

| Syntax | What It Does | Input: "chocolate truffles" |
|--------|-------------|------------------------|
| `{keyword:default}` | all lowercase | chocolate truffles |
| `{Keyword:default}` | First word capitalized | Chocolate truffles |
| `{KeyWord:default}` | Every Word Capitalized | Chocolate Truffles |
| `{KEYWord:default}` | FIRST WORD CAPS Rest Title | CHOCOLATE Truffles |
| `{KeyWORD:default}` | First Title REMAINING CAPS | Chocolate TRUFFLES |
| `{KEYWORD:default}` | ALL CAPS | CHOCOLATE TRUFFLES |

**Recommendation:** Use `{KeyWord:Default}` (Title Case) for headlines 95% of the time. It looks professional and matches how most headlines are formatted.

### DKI in Headlines

```
Headline: Buy {KeyWord:Premium Widgets}
```
If keyword = "blue widgets" → "Buy Blue Widgets" (18 chars)
If keyword = "extra large premium blue widgets" (too long) → "Buy Premium Widgets" (19 chars)

**Character counting rule:** Count the DEFAULT text, not the DKI syntax. If the default text version exceeds 30 characters, the headline will be disapproved.

### DKI in Descriptions

```
Description: Shop our selection of {KeyWord:premium products}. Free shipping on orders over $50.
```

Same character rule applies — count the version with default text against the 90-character limit.

### DKI in Display Paths

```
Path 1: {KeyWord:Widgets}
Path 2: Sale
```
15-character limit per path applies to the default text.

## When to Use DKI

**Use DKI when:**
- Ad group has 5-20 tightly themed keywords
- Keywords are clean, professional terms (brand names, product categories)
- You want to boost CTR by matching the search query in the headline
- You have single-keyword-theme ad groups (SKAGs) or tight theme ad groups

**Do NOT use DKI when:**
- Keywords include competitor brand names (legal/policy risk)
- Keywords are long-tail phrases that won't fit in 30 characters
- Keywords contain misspellings (Google may insert the misspelled version)
- Keywords are generic or awkward when placed in a sentence
- Ad group has broad match keywords with unpredictable queries
- Keywords include sensitive terms (medical conditions, legal issues)

### DKI Quality Checklist

Before using DKI, check every keyword in the ad group:
- [ ] Does every keyword make grammatical sense in the headline/description?
- [ ] Is every keyword short enough to fit within character limits?
- [ ] Are there any misspelled keywords that would look unprofessional?
- [ ] Are there any competitor names that could cause trademark issues?
- [ ] Does the default text work as a strong standalone headline?

## IF Functions

IF functions show different text based on the device or audience.

### Syntax

```
{IF(device=mobile,Text for mobile):Default text}
{IF(audience IN(remarketing_list),Returning visitor text):Default text}
```

### Device-Based IF Functions

```
Headline: {IF(device=mobile,Call Now — Free Quote):Get Your Free Quote}
```
- Mobile users see: "Call Now — Free Quote"
- Desktop users see: "Get Your Free Quote"

### Audience-Based IF Functions

```
Description: {IF(audience IN(past_purchasers),Welcome back! Enjoy 20% off your next order.):New here? Get 15% off your first order today.}
```
- Past purchasers see the loyalty offer
- New visitors see the acquisition offer

### IF Function Rules
- Character limit applies to BOTH the IF text AND the default text separately
- You can nest DKI inside IF functions but it gets complex — test carefully
- Only `device=mobile` is available for device targeting (not tablet/desktop separately)
- Audience lists must be set up in the Google Ads audience manager first

## Countdown Customizers

Show a live countdown to a deadline in your ad copy.

### Syntax

```
{COUNTDOWN(yyyy-MM-dd HH:mm:ss,language)}
```

### Examples

```
Headline: Sale Ends in {COUNTDOWN(2026-04-15 23:59:59,en)}
```
Shows: "Sale Ends in 5 days" → "Sale Ends in 2 hours" → etc.

### Countdown Parameters
- **End date format**: yyyy-MM-dd HH:mm:ss
- **Language**: "en" for English (matches ad language)
- **Days before**: Ads start showing the countdown 5 days before the deadline by default
- **Character counting**: Google counts the longest possible output (e.g., "10 days" = 7 chars)

### Countdown Best Practices
- Set the countdown at least 5-7 days out to get enough impression volume
- Pair with urgency descriptions: "Don't miss our biggest sale of the year."
- Use for seasonal promotions, enrollment deadlines, event registrations
- The ad automatically stops showing after the deadline passes

## Location Insertion

Dynamically insert the user's city, state, or country into ad copy.

### Syntax

```
{LOCATION(City):Default City}
{LOCATION(State):Default State}
{LOCATION(Country):Default Country}
```

### Examples

```
Headline: Best Plumber in {LOCATION(City):Your Area}
Description: Serving {LOCATION(City):your city} for 15 years. Licensed, bonded & insured. Call now.
```

### Location Insertion Rules
- Default text is shown when location can't be determined
- Character limit applies to the default text
- Works best with location-targeted campaigns
- Test that the ad makes sense for ALL locations in your targeting
- Some cities have long names — "San Francisco" = 13 chars, which may cause issues

## Combining DKI Elements

You can use multiple customizers in one ad, but keep it readable:

```
Headline 1: {KeyWord:Best Widgets}
Headline 2: {LOCATION(City):Local} Deals
Headline 3: {COUNTDOWN(2026-04-15 23:59:59)} Left

Description 1: {IF(device=mobile,Call for a free {KeyWord:widget} quote today!):Get a free {KeyWord:widget} quote online. Fast, easy & no obligation.}
```

**Warning:** The more customizers you stack, the harder it is to predict what the ad will look like. Always preview every combination before launching.

## Output Format

When the user asks for DKI setup, provide:

```
=== DKI SETUP ===
Ad Group: [name]
Keywords in group: [list]

HEADLINES WITH DKI:
H1: {KeyWord:Default Text} (default = XX chars)
H2: [Static headline] (XX chars)
H3: {IF(device=mobile,Mobile Text):Desktop Text}

DESCRIPTIONS WITH DKI:
D1: [with DKI syntax and char counts for both versions]
D2: [static description for safety]

KEYWORD COMPATIBILITY CHECK:
  "keyword 1" → fits, grammatically correct
  "keyword 2" → fits, grammatically correct
  "keyword 3" → TOO LONG (32 chars) — will show default
  "keyword 4" → awkward phrasing — recommend static headline instead

PREVIEW (top 3 keyword combinations):
  Query: "keyword 1" → [full ad preview]
  Query: "keyword 2" → [full ad preview]
  Query: "keyword 3" → [full ad preview with default]
```
