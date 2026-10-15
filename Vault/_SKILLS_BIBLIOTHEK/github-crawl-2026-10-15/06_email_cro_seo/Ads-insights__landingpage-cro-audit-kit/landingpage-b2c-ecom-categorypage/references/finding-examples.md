# Worked finding examples — category page quality calibration

These examples show what a high-quality category page finding looks like across different categories, brand snapshots, and ICE scores. Use them as a reference standard. Findings should match this depth and specificity — not be vaguer, not be more generic.

---

## Example 1: 🔴 Critical — Filtering UX (mid-market apparel, 500+ SKUs)

### 🔴 Filtering UX — Filters hidden behind a single "Filter" button on desktop with 540-product category

**Diagnosis**
The category page shows 540 products but exposes no visible filter facets on desktop — all filters live behind a single "Filter" button at the top-right that opens a drawer. Per Baymard's filter & faceted search research, sites with large assortments and hidden filters see 25-40% higher PLP bounce rates than sites with always-visible facets. The hidden-drawer pattern is acceptable on mobile where space is constrained, but on desktop it actively suppresses filter usage — visitors don't realise filtering options exist, browse a few rows, and bounce. Iyengar's choice overload research applies directly: 540 unsorted products without visible narrowing tools creates paralysis. The Hick's Law calculation is unfavourable here — every decision is unstructured.

**Recommendation**
Expose the filter sidebar on desktop as a persistent left column (220-280px wide). Surface the top 5 facets always-open: Price, Brand, Size, Color, Category. Other facets in collapsible accordion sections. Display applied filters as removable chips at the top of the grid. Add a visible "Clear all" link. On mobile keep the current drawer pattern with a sticky "Filter" button at the top-right of the screen — that part works.

**Test specification**
- **Hypothesis:** If we expose filter facets in a persistent left sidebar on desktop, then click-to-PDP rate and filter-interaction rate will increase because visitors immediately see narrowing tools and self-select a manageable subset (Baymard filter research; Iyengar choice overload).
- **Variant A:** filters behind "Filter" button drawer on desktop
- **Variant B:** persistent left sidebar with top 5 facets always visible + applied-filter chips
- **Primary metric:** click-to-PDP rate
- **Secondary metrics:** filter interaction rate, bounce rate on category page, session-level add-to-cart rate
- **Expected impact:** +8% to +18% on click-to-PDP rate
- **ICE:** I=9, C=9, E=7 → 8.3
- **Source:** Baymard Institute filter & faceted search research; Iyengar choice overload (Columbia Business School)

---

## Example 2: 🔴 Critical — Default sort (mid-market home goods, 240 products)

### 🔴 Sorting — Default sort "Newest" suppresses bestseller social proof on a category dominated by repeat-purchase products

**Diagnosis**
The category page defaults to "Sort by: Newest". The visible first row contains items launched in the past 30 days, none of which have review counts above 12. Per Kahneman/Tversky's default-effect research, the default choice silently shapes ~70% of session behavior — most visitors never change the sort. For this category (kitchen essentials with strong repeat-purchase patterns and 4.5+ star bestsellers in the 300+ review range), defaulting to "Newest" buries the strongest social proof signal. Visitors compare unverified new items instead of seeing what the category's loyal buyers already endorsed. Baymard's research consistently shows that sort defaults matching customer intent (browse-and-discover → bestsellers; specific search → relevance) outperform recency-driven defaults for replenishment categories.

**Recommendation**
Change default sort to "Popularity" (algorithm-driven by 30-day add-to-cart count) or "Bestseller" (cumulative sales). Keep "Newest" as a sort option for visitors who specifically want new arrivals. Make the sort label visible in the top-right of the grid: "Sort: Popular" instead of an icon-only dropdown. For visitors arriving from a "New arrivals" campaign URL, you can override the default to "Newest" via URL parameter — this preserves campaign intent without affecting the rest.

**Test specification**
- **Hypothesis:** If we change the default sort from "Newest" to "Popularity", then click-to-PDP rate and session-level add-to-cart rate will increase because the strongest social-proof products appear first instead of unverified new arrivals (Kahneman/Tversky default effect; Cialdini social proof).
- **Variant A:** default sort "Newest"
- **Variant B:** default sort "Popularity"
- **Primary metric:** session-level add-to-cart rate (sessions starting on this category page)
- **Secondary metrics:** click-to-PDP rate on top 5 product cards, time on category page, sort-interaction rate
- **Expected impact:** +5% to +12% on session-level add-to-cart rate
- **ICE:** I=8, C=8, E=10 → 8.7
- **Source:** Kahneman & Tversky (default effect); Cialdini's social proof principle; Baymard sort research

---

## Example 3: 🔴 Critical — Product card content (premium multi-brand retailer)

### 🔴 Product card content — Cards show only image and price, missing brand name and rating

**Diagnosis**
Each product card on this premium multi-brand category page shows only product image, product name, and price. Brand name is absent (despite the retailer carrying 80+ designers), and no rating or review count is shown. For a multi-brand premium retailer where brand is often the primary purchase driver, this is a major information gap. Per Nielsen Norman's card scanability research, visitors examine 6-12 cards before clicking — each card has 2-3 seconds to communicate value. Without brand, visitors must hover or click into each PDP to verify the brand, multiplying the friction across the browse session. Cialdini's social proof is also unused: review aggregates exist in the product database but are not surfaced on cards.

**Recommendation**
Add two information layers to each card: (1) brand name in small-caps above the product name (typographic restraint matching premium aesthetic — no logos, just text), and (2) rating + review count below the price when reviews exist (★★★★☆ 4.6 · 24 reviews). For cards without reviews, leave the rating section empty rather than showing "No reviews yet" (which is a negative signal). Maintain card whitespace and editorial typography. Test layout with brand placement above name vs. below name.

**Test specification**
- **Hypothesis:** If we add brand name and rating + review count to product cards, then click-to-PDP rate will increase because visitors can confirm brand fit and trust signal at scan-time instead of clicking through to verify (Nielsen Norman card scanability; Cialdini social proof).
- **Variant A:** cards with image + name + price only
- **Variant B:** cards with brand + name + price + rating + review count
- **Primary metric:** click-to-PDP rate
- **Secondary metrics:** cards-clicked per session, return-to-category rate (lower = better card-level decision quality), time on category page
- **Expected impact:** +6% to +14% on click-to-PDP rate
- **ICE:** I=8, C=9, E=8 → 8.3
- **Source:** Nielsen Norman Group card scanability research; Cialdini's social proof principle; Baymard PLP card research

---

## Example 4: 🟠 Important — Pagination (mid-market specialty retailer)

### 🟠 Pagination — Infinite scroll without back-to-top or scroll-position memory loses user context

**Diagnosis**
The category page uses infinite scroll: as the visitor scrolls, new products load automatically with no visible page count or sticky position indicator. After scrolling past 50+ products and clicking into a PDP, returning to the category resets the scroll position to the top — the visitor must scroll back through 50 products to resume. Per Baymard's pagination research, this is a common infinite-scroll failure pattern that reduces session conversion in two ways: visitors give up on deep browsing, and back-navigation feels punitive. The footer is also effectively unreachable on the category page (more products load when scrolling approaches it). For SEO this is also a loss — search engines see only the initial product load.

**Recommendation**
Two changes. First, replace pure infinite scroll with a hybrid pattern: auto-load the first 2-3 batches, then show a "Load more (X of Y products)" button. This preserves the smooth experience for low-effort browsing while making the footer reachable and providing clear progress. Second, implement scroll-position restoration: when a visitor clicks into a PDP and returns via browser back-button, restore the previous scroll position and the products already loaded. Most modern frameworks (React, Next, Shopify Hydrogen) support this via session storage.

**Test specification**
- **Hypothesis:** If we replace pure infinite scroll with a hybrid "load first 2-3 batches then button", then deep-scroll engagement will increase and pogo-sticking back-to-top behavior will decrease because the visitor regains control and orientation (Baymard pagination research).
- **Variant A:** pure infinite scroll
- **Variant B:** auto-load 2-3 batches + "Load more" button + scroll-position restoration on back-nav
- **Primary metric:** session-level add-to-cart rate on sessions that scroll past the first batch
- **Secondary metrics:** scroll depth, return-to-category rate (lower is better — fewer pogo-stick sessions), pages-per-session
- **Expected impact:** +3% to +8% on session-level add-to-cart rate for deep-scroll sessions
- **ICE:** I=6, C=7, E=6 → 6.3
- **Source:** Baymard Institute pagination research; Nielsen Norman scroll-vs-pagination research

---

## Example 5: 🟠 Important — Mobile experience (value brand, 800+ SKUs)

### 🟠 Mobile experience — Filter and sort buttons non-sticky, invisible after first scroll

**Diagnosis**
On mobile, the "Filter" and "Sort" buttons appear at the top of the category page, immediately above the first row of products. After scrolling past the first 4-6 products they disappear from view, with no sticky variant returning them to the screen. Per Baymard's mobile commerce research, mobile visitors use filter and sort 2-3x more frequently than desktop visitors (smaller screens require more aggressive narrowing). Making these tools invisible after one scroll forces visitors to scroll all the way back up to access them — a friction pattern that suppresses filter usage and reduces click-to-PDP rate. The desktop experience does not have this problem (sidebar persistent), but mobile is likely 60-70% of traffic for this value-brand audience.

**Recommendation**
Implement a sticky bar at the top of the mobile category-page viewport (after the visitor scrolls past the initial filter+sort buttons) containing two buttons: "Filter (3)" — showing the count of applied filters — and "Sort: [current option]". The bar should be 44-48px tall, semi-transparent dark background, and dismissable by scroll-up gesture. Maintain the original filter+sort placement at page top for the first-paint experience. Both buttons should open their respective drawers as the existing mobile pattern does.

**Test specification**
- **Hypothesis:** If we add a sticky filter+sort bar that appears on mobile after the initial buttons scroll off-screen, then mobile filter usage and click-to-PDP rate will increase because the narrowing tools remain accessible regardless of scroll position (Baymard mobile commerce; Fitts's Law).
- **Variant A:** filter and sort visible only at top of page on mobile
- **Variant B:** sticky filter+sort bar appears after initial scroll
- **Primary metric:** mobile click-to-PDP rate
- **Secondary metrics:** mobile filter-interaction rate, mobile scroll depth, mobile bounce rate
- **Expected impact:** +5% to +12% on mobile click-to-PDP rate
- **ICE:** I=7, C=8, E=7 → 7.3
- **Source:** Baymard Institute mobile commerce research; Fitts's Law applied to mobile UX

---

## Example 6: 🟢 Nice-to-have — Out-of-stock handling (Dutch specialty retailer)

### 🟢 Out-of-stock handling — OOS products hidden entirely instead of greyed out with notify-me

**Diagnosis**
Products that are out of stock are removed entirely from the category page. Returning visitors looking for a specific remembered item see no trace of it and assume it's been discontinued. Per Baymard's out-of-stock research and Kahneman/Tversky's loss-aversion principle, showing out-of-stock products with a clear "Out of stock — Notify me" CTA captures email signups, preserves visitor mental model of the assortment, and triggers mild loss aversion that encourages wishlist or notify-me action. Hiding OOS entirely loses all three opportunities. Note: I cannot fully verify from screenshots how many products are currently OOS; the recommendation assumes a non-trivial portion. If <5% of catalog is ever OOS this finding has lower priority.

**Recommendation**
Show out-of-stock products in the grid with these treatments: (1) image at 70% opacity, (2) "Out of stock" badge in the top-right of the card, (3) "Notify me when back in stock" CTA on hover/tap that captures email, (4) "Out of stock" filter facet available — but default = all (visitor opts in). Optionally: a "Wishlist" toggle on each OOS card for returning customer convenience.

**Test specification**
- **Hypothesis:** If we surface out-of-stock products with notify-me capture, then email signups and wishlist activity will increase with no negative impact on click-to-PDP rate (Baymard OOS research; Kahneman/Tversky loss aversion).
- **Variant A:** OOS products hidden from category page
- **Variant B:** OOS products visible with greyed treatment + notify-me CTA + wishlist toggle
- **Primary metric:** notify-me email captures per category page visit
- **Secondary metrics:** click-to-PDP rate on in-stock products (must not decrease), wishlist additions, eventual purchase from notify-me cohort
- **Expected impact:** moderate impact on email captures (new metric); minimal effect on direct conversion
- **ICE:** I=4, C=7, E=7 → 6.0 (nice-to-have because direct revenue impact is delayed)
- **Source:** Baymard Institute out-of-stock research; Kahneman & Tversky loss aversion

---

## What makes these examples high-quality

- **Specific:** every observation names an exact element with position and behavior
- **Sourced:** every claim references a specific principle, study, or institution
- **Brand-aware:** recommendations consider whether they fit the brand snapshot (premium vs mid-market vs value) and assortment density
- **Honest about uncertainty:** when data is missing (e.g. example 6's OOS percentage), the finding says so and recommends research, not action
- **Test-ready:** hypothesis follows "If X, then Y, because Z"; primary metric is named (category page metrics: click-to-PDP rate, filter interaction, scroll depth, session-level add-to-cart); ICE is justified by the breakdown
- **Concrete copy and behavior:** not "improve the filters" — actual filter facet names, position, drawer pattern
- **Dutch translations natural:** when output is Dutch, JTBD framing avoids "huren"; terms like "categoriepagina" or untranslated "filter" used appropriately

Always match this standard. If a finding can't reach this standard, either dig deeper or remove it from the audit.
