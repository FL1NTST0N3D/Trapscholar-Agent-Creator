# Frameworks for B2C Ecommerce Category Page Audits

This reference file contains the CRO frameworks, principles, and applied research used in the category page audit. Each section maps to a finding category from the main skill.

---

## CRITICAL — Visual verification before every finding

Many of the categories below involve checking whether an element is **present, absent, or insufficient** on the page. Examples:
- Filter drawers and faceted-search panels (often JavaScript-rendered, may only appear after interaction)
- Quick-view modals (triggered by hover or click, invisible in static HTML)
- Infinite-scroll triggers (load more on scroll, may not have visible button)
- Product card hover states (extra image, quick-add button)
- Lazy-loaded product cards below the fold
- Sticky filter buttons that appear only after scroll
- Out-of-stock badges that render conditionally

**For every finding in these categories, verify the claim against screenshots before delivering.** The most common failure mode is claiming an element is missing when it is visually present but invisible in fetched HTML. A finding that says "no filter system visible" while the page has a JavaScript-rendered filter drawer is worse than no finding at all — it destroys credibility.

If a finding cannot be visually verified, either:
1. Remove it from the audit, or
2. Convert it to a "research first" finding asking the user to confirm before testing

This rule overrides every other instruction in this file.

---

## CRITICAL — Conditional HTML strings on category pages

Most ecom platforms ship status strings into the DOM as **conditional placeholders** that JavaScript decides whether to render. The string is always in HTML; the visitor only sees it under specific conditions.

Category-page-specific examples:
- Shopify: `"Sale"`, `"New"`, `"Bestseller"`, `"Out of stock"` badges — all hardcoded in Liquid templates, conditionally displayed
- WooCommerce: `"On sale"`, `"Featured"`, variant labels on product cards
- Magento: `compare_at_price` strings on every card (only renders on sale items)
- Faceted search platforms (Algolia, Searchspring, Klevu): filter facet labels may appear in HTML before any product loads

**Implication for the audit:** finding a "low stock" badge string in HTML does NOT mean any visible card actually shows it. Filter facets in HTML do NOT mean all facets are surfaced on every category.

**The hard rule:** badge state, stock state, filter availability per facet, and dynamic card content rely on screenshots only. Never on HTML strings.

A finding may legitimately say: *"product cards show no rating-star signal — consider adding ratings to cards to support social proof at scan-time (Cialdini)"*.

A finding may NOT say: *"the HTML contains 'low stock' badges but no card shows them — likely a configuration bug"*. That finding is almost always wrong; it is template-default behavior.

---

## Core frameworks (apply across the entire audit)

### Baymard Institute PLP research
Baymard's research consistently identifies category page issues as among the highest-impact ecom conversion problems:
- 49% of all category pages have filter usability issues that materially hurt conversion
- Sites with poor PLP filtering see 25-40% higher PLP bounce rates than sites with strong filtering
- Average user examines 6-12 product cards before deciding to click into a PDP — card scanability is critical
- Mobile category-page UX gaps account for the largest single conversion loss across funnels

### Iyengar choice overload research
Sheena Iyengar's classic "jam study" showed that choice paralysis reduces decision-making:
- 24 jams displayed: 60% stopped, 3% bought
- 6 jams displayed: 40% stopped, 30% bought

Implication for category pages: showing 100+ products without filtering / sorting / curation tools creates choice paralysis. Strong filtering is the antidote — it lets users self-select a manageable subset.

### Hick's Law
The time to make a decision increases logarithmically with the number of choices. On category pages this applies to:
- Filter facets (too many = paralysis; too few = no narrowing)
- Sort options (5-7 is the sweet spot)
- Product card actions (one primary action, not five competing icons)

### Nielsen Norman F-pattern eye-tracking
On category pages, eyes scan in an F-pattern:
- Top horizontal sweep (title, filter bar, first row of products)
- Second horizontal sweep, shorter (filter sidebar, top of grid)
- Vertical scan down the left edge (filter sidebar, first product column)

Implication: the highest-impact placements are top-left and the first product column. Most-valuable filters and most-important products belong there.

### Cialdini's principles on PLP
- **Social proof on cards** — rating stars, review counts, "X+ sold this month", "Bestseller" badges
- **Scarcity on cards** — "Only X left", "Almost gone" — use carefully, never fake
- **Authority** — editorial picks, "Editor's choice", brand-curator quotes

### Kahneman/Tversky — default effect
Whatever is the default sort, filter, or display preference shapes ~70% of decisions. Default-sort choice is among the most impactful invisible decisions on a category page.

### Jobs-to-be-Done on category pages
Visitors on category pages are usually doing one of:
1. **Browse / discover** — no specific need yet, exploring
2. **Filter to specific** — has criteria in mind (size, color, price range)
3. **Compare** — narrowed to 3-5 options, comparing details
4. **Quick reorder** — returning customer wanting fast access

Different jobs need different routes. A category page optimized only for "browse" loses filter-driven and quick-reorder users.

**Important Dutch translation:** never use "huren" for JTBD framing. Instead: "kiezen voor", "zoeken om X te vinden", "bezoekers die X willen".

---

## Category 1: Above-the-fold clarity & category framing

### Information scent (Nielsen Norman)
The visitor arrives with an expectation — "this should be the page for X". The above-the-fold area must confirm the scent within 5 seconds:
- Clear category title (matching what the visitor searched or clicked)
- Visible product count ("254 items") — calibrates expectations
- Optional intro-copy for SEO/editorial framing (but not blocking the grid)

### WiderFunnel LIFT relevance factor
Mismatched scent → bounce. A visitor searching "Pokémon booster boxes" who lands on a page titled "Trading Card Games" with mixed content doubts they're in the right place.

### Best practices
- Title in customer language matching the navigation path
- Product count visible
- Filter breadcrumb showing applied filters
- Optional intro paragraph that doesn't dominate above-the-fold real estate
- Lifestyle banner image acceptable for premium brands; problematic for utility shoppers

### Common failures
- Category title hidden below a hero banner that occupies 80% of above-the-fold
- No product count
- Intro-copy walls of SEO-text pushing products below the fold
- Title in internal taxonomy ("S/S 2025") instead of customer language

### Brand calibration
- Premium brands: editorial banner + concise title acceptable, generous whitespace
- Mid-market: title + count + filters above the fold; banner optional
- Value brands: title + count + filters + sort + first row of products all above the fold

---

## Category 2: Filtering UX

### Baymard filter research
This is the single biggest conversion lever on category pages. Key findings:
- **Visible facets outperform "all filters" dropdowns** — visitors miss filtering options entirely when hidden
- **Top facets at top of sidebar** — price, size, color, brand are typically high-priority; specs lower
- **Multi-select per facet** — users want to see "Red OR Blue", not "Red XOR Blue"
- **Applied filters visible as removable chips** at top of grid — critical for filter exploration
- **"Clear all" button** prominent — visitors recover from over-filtering
- **Filter counts per option** ("Red (24)") — sets expectations before clicking

### Filter sidebar vs. top-bar
- **Sidebar (left or right):** works best on desktop for sites with 5+ facets, allows always-visible filtering
- **Top horizontal bar:** works for sites with 3-4 high-priority filters; mobile-friendly extension
- **Drawer (slide-in):** standard for mobile; weak on desktop unless space is constrained

### Common failures
- All filters hidden behind a "Filter" button on desktop with significant SKU counts
- No applied-filter chips — visitor doesn't know what's narrowing the result
- Single-select filters where multi-select would be intuitive (size, color, brand)
- No filter counts — visitor doesn't know if a facet returns 0 or 240 results
- Filters that close after applying one — friction for multi-filter exploration

### Brand calibration
- Premium small-assortment brands: minimal filters, often just category + price + size
- Mid-market: full faceted sidebar with 6-10 facets
- Value brands: aggressive faceted search with deal/discount filters prominent

---

## Category 3: Sorting

### Baymard sort research
- **5-7 sort options is the sweet spot** — more creates choice paralysis (Hick's Law)
- **"Relevance" as default** outperforms "Newest" or "Price low" for most categories — algorithm-driven relevance leverages buyer signals
- **"Bestseller" as default sort** appropriate for value/discovery-focused categories; less appropriate for premium
- Default-sort choice silently shapes ~70% of session behavior

### Standard sort options
- Relevance / Featured / Popular
- Price: Low to High
- Price: High to Low
- Newest / Recently Added
- Bestseller / Most Sold
- Customer Rating
- Discount % (when sale is active)

### Best practices
- Sort dropdown in top-right of grid, always visible
- Sort label visible ("Sort: Featured" vs. an icon-only dropdown)
- Mobile: keep sort prominent, not buried in a filter drawer

### Common failures
- Default sort is "Newest" on a category where bestsellers convert better
- Sort dropdown buried in mobile filter drawer (mobile users use sort 2-3x more than desktop)
- Too many sort options (10+ creates paralysis)
- Sort label hidden behind an icon, fragmented from the active selection

---

## Category 4: Product card content

### Nielsen Norman card scanability
Visitors examine 6-12 cards before clicking. Each card has 2-3 seconds to communicate its value. Effective cards contain:
- Primary image (consistent crop and style across cards)
- Brand name (when relevant — for multi-brand retailers)
- Product name (truncated cleanly if long)
- Price (current + crossed-out original if on sale)
- Rating + review count (when available)
- Color/variant indicators (small swatches or "+ 4 colors")

### Baymard PLP card research
- **Lifestyle vs. clinical product photography**: lifestyle drives engagement on apparel/home; clinical drives clarity on electronics/tools
- **Consistent crop/orientation**: cards with inconsistent product framing reduce scan efficiency
- **Hover state**: showing alternative image or quick-add reduces clicks to PDP for low-intent browsers
- **Save / wishlist icon**: visible on hover, low priority but adds returning-visitor value

### Common failures
- Cards too dense (8+ text elements compete for attention)
- Cards too sparse (no rating, no review count, no variant indicators)
- Inconsistent product crops (some full-body, some close-up)
- Price hidden until hover
- Brand name missing on multi-brand retailers

### Brand calibration
- Premium brands: clean cards, generous whitespace, minimal text, no badges
- Mid-market: full information cards with rating + reviews + variants
- Value brands: prominent prices, deal/discount badges, multiple visual cues

---

## Category 5: Product card interaction

### Hover states (desktop)
Effective hover states include:
- Alternative product image (back view, in-context shot)
- Quick-view button (modal with key info without leaving category)
- Wishlist / save icon

Hover should not require precise mouse positioning — entire card should be hoverable.

### Quick-view modals
- Useful for visitors comparing 5+ products
- Should include: large image, full description, variant selection, add-to-cart
- Should NOT require dismissing and re-clicking to compare
- Mobile equivalent: full-screen overlay with swipe-to-next

### Tap targets (mobile)
Per Fitts's Law and Apple HIG: minimum 44×44px for any tappable card area. Common failure: tiny wishlist icons in card corners that mis-tap to the product link.

### Common failures
- Hover-only quick-add (mobile users excluded)
- Quick-view that just navigates to PDP (defeats purpose)
- Tap targets too small on mobile
- Multiple competing card actions (wishlist + quick-view + compare + add-to-cart = paralysis)

---

## Category 6: Visual hierarchy & grid density

### Iyengar choice overload applied
Showing 60+ products without curation overwhelms. Above-the-fold sweet spot:
- 4-row × 4-column desktop grid (16 cards) is the upper bound
- 2-row × 3-column above-the-fold mobile (6 cards)
- More than this: enable pagination or load-more to manage cognitive load

### Gestalt principles
- **Proximity**: cards grouped close (small gutters) read as a unit; large gutters break flow
- **Similarity**: consistent card design (same size, same fields, same image crop) supports scanning
- **Continuity**: aligned grid (consistent row heights) reduces visual noise

### Grid density patterns
- **Tight (3-4 columns desktop, 2 mobile):** more cards visible, faster scanning
- **Spacious (2-3 columns desktop, 1-2 mobile):** more detail per card, slower deliberate browsing
- **Mixed:** featured product cards (2× size) interspersed with regular — works for editorial brands

### Common failures
- Single-column desktop layout (massively wastes horizontal space)
- Inconsistent card heights (creates jagged grid, breaks Gestalt continuity)
- Too-small cards making images unreadable
- Massive gutters that fit only 2 cards across when 4 would work

---

## Category 7: Pagination, infinite scroll, or load more

### Baymard pagination research
Three main patterns, each with trade-offs:

**Pagination ("Page 1, 2, 3")**:
- Pro: predictable navigation, supports bookmarking, good for SEO
- Con: friction (click to load next page), risk of bouncing on first page
- Best for: large catalogs (500+ products) where users self-select via filters

**Infinite scroll**:
- Pro: smooth browsing experience, mobile-friendly
- Con: weak for SEO, footer becomes unreachable, position lost on back-navigation, drains performance
- Best for: discovery-driven categories with strong visual scanning (fashion, photography)

**Load more button**:
- Pro: balances discovery and control, footer remains reachable
- Con: still requires explicit interaction
- Best for: most categories with moderate SKU counts (50-500)

### Best practices
- Default to "Load more" for most B2C ecom categorypages
- If using infinite scroll: include sticky pagination indicator + "back to top"
- If using pagination: show clear "Page X of Y" + jump-to-page
- Mobile: never use desktop pagination patterns on mobile

### Common failures
- Infinite scroll without back-to-top → user lost after scrolling 200+ products
- Pagination with no page count → user doesn't know how many results
- Load-more that loses scroll position on click
- Pagination buttons too small on mobile

---

## Category 8: Breadcrumbs & navigation context

### Nielsen Norman breadcrumb research
Breadcrumbs serve two functions:
1. **Show position in site hierarchy** — "Home > Men > Shoes > Sneakers"
2. **Allow up-level navigation** — clicking "Men" returns to parent category

### Best practices
- Above the fold, below header
- Customer language ("Sneakers") not internal codes ("FW25-SN")
- Last item (current page) styled differently (heavier or non-clickable)
- Mobile: keep visible (compressed if needed) — visitors arrive on mobile from search and need orientation

### Common failures
- No breadcrumbs at all on deep category levels
- Breadcrumbs that hide on mobile (visitors lose context after one tap)
- Breadcrumbs in internal taxonomy
- Last item clickable when it shouldn't be (causes page reload)

### Cross-category navigation
Strong category pages offer secondary navigation:
- "Related categories" links ("Customers viewing Sneakers also browse Sports shoes")
- Sibling categories ("Back to: All Men's footwear")
- Filter-driven sub-categories ("Filter by brand → see brand-specific pages")

---

## Category 9: Trust signals & social proof on PLP

### Cialdini social proof at scan-time
The category page is where visitors decide which product is worth a PDP click. Social proof at this level accelerates the choice:
- **Rating stars on cards** (4.6★) — fast scan signal
- **Review count on cards** (124 reviews) — credibility signal
- **"Bestseller" / "Popular" badges** — implicit social proof
- **"X% bought this in the last 30 days"** — temporal social proof (advanced)

### Trust strip on category pages
Some retailers display the site-wide USP/trust strip on category pages (free returns, customer rating). This is acceptable but lower-priority than on homepage — visitors already crossed the trust threshold.

### Spiegel Research Center finding
Products with reviews convert ~270% better than products without. Category pages with visible rating signals see meaningfully higher click-to-PDP rates.

### Best practices
- Rating + review count visible on every card where reviews exist
- "Bestseller" badge for top 5-10% of items (not 50% — dilutes signal)
- Authority badges sparingly: certified, award-winning, editor's pick

### Common failures
- Reviews exist in the product database but not surfaced on cards
- "Bestseller" applied to every other product (signal dilution)
- Average rating displayed without review count (4.5★ from 2 reviews ≠ from 240)

---

## Category 10: Out-of-stock handling

### Baymard out-of-stock research
- Hiding out-of-stock products entirely confuses returning visitors looking for a remembered item
- Showing them with prominent "Out of stock" label allows visitors to filter, wishlist, or expect-restock
- Filter option "Show only in-stock" should be available, but not the default for most categories

### Best practices
- Out-of-stock cards: greyed out, "Out of stock" badge, "Notify me" CTA
- Filter facet: "Availability → In stock" with default = all (visitor opts in)
- Wishlist / notify-me capture for OOS items as email-list growth

### Loss aversion (Kahneman/Tversky)
Showing OOS items triggers mild loss aversion — visitor sees what they almost had, considers wishlisting, returns when restocked. Hiding entirely loses this opportunity.

### Common failures
- OOS items removed from category, breaking returning-visitor expectations
- OOS shown but no notify-me capture
- "In stock" as default filter (cuts visible assortment without user awareness)
- Inconsistent OOS treatment (some greyed out, some hidden, some showing normally)

---

## Category 11: Mobile experience

### Mobile-specific best practices
- **Sticky filter button** at top or bottom — accessible regardless of scroll
- **Sticky sort button** alongside filter
- **Filter drawer**: full-screen overlay with grouped facets, "Apply" button to close
- **2-column grid** as default (single column wastes width; 3-column too dense)
- **Tap targets minimum 44×44px** (Fitts's Law)
- **Lazy-loaded images** to keep mobile load fast
- **No hover states** — replace with always-visible card content
- **Pagination/Load-more friction-free** on mobile

### Baymard mobile commerce research
- Mobile category-page bounce rates are 1.8-2.2x desktop on average
- Filter usage is 2-3x more frequent on mobile (smaller screens → more need for narrowing)
- Sort is used 1.5x more on mobile
- Sticky CTAs measurably increase mobile click-to-PDP rate

### Common failures
- Single-column mobile grid (wastes width on modern phones)
- Filter button non-sticky → invisible after scrolling
- Tap targets too small (especially wishlist icons in card corners)
- Desktop-style hover states ported to mobile (touch never triggers them, features die)
- Mobile sort buried in filter drawer (separates two tools that work together)

---

## Notes on brand calibration

Always reread the brand snapshot before finalizing recommendations. The same finding category leads to different recommendations depending on brand and assortment size:

**Example: Filter density**
- Premium curated brand (30 SKUs): 3-4 high-level filters, generous whitespace, often only price + category sub-type
- Mid-market multi-brand (500 SKUs): full sidebar with 8-12 facets, multi-select, applied chips
- Value bulk retailer (5000+ SKUs): aggressive faceted search with discount filters, brand filter prominent

**Example: Product card design**
- Premium: editorial photography, minimal text, no badges, generous whitespace
- Mid-market: full information cards with rating + reviews + variant swatches + occasional badges
- Value: prominent prices, deal badges (-30%, -50%), urgency cues (Stock low)

**Example: Sort default**
- Premium brand with editorial assortment: "Curated" or "Featured" default — algorithm-driven by editor signals
- Mid-market: "Popularity" or "Relevance" default — algorithm-driven by purchase signals
- Value brand: "Discount %" or "Price low" default — leans into deal-hunter intent

Recommendations that don't match the brand snapshot are wrong, even if they would work for a different brand.

---

## Test-readiness check

Before finalizing each finding, verify:
- [ ] Diagnosis cites a specific principle or source
- [ ] Recommendation is concrete (specific copy / position / behavior)
- [ ] Hypothesis follows "If X, then Y, because Z" structure
- [ ] Primary metric is named (category page metrics: click-to-PDP rate, filter interaction rate, scroll depth, session-level add-to-cart rate, time on category page)
- [ ] ICE score is justified by the I/C/E breakdown
- [ ] Recommendation matches the brand snapshot and assortment density
- [ ] Dutch output: no literal jargon translation ("huren" check)

If any box is unchecked, rework the finding before delivering.
