# Worked finding examples — quality calibration

These examples show what a high-quality finding looks like across different categories, brand snapshots, and ICE scores. Use them as a reference standard. Findings should match this depth and specificity — not be vaguer, not be more generic.

---

## Example 1: 🔴 Critical — Add-to-cart CTA (mid-market apparel brand)

### 🔴 Add-to-cart CTA — Insufficient visual hierarchy above the fold

**Diagnosis**
The add-to-cart button on the desktop PDP uses the same medium-grey color as the "Add to wishlist" and "Share" buttons (#7A7A7A). Per Cialdini and basic visual hierarchy principles, the primary action must dominate visually. When the primary CTA shares styling with secondary actions, users hesitate or click the wrong button. Baymard's PDP benchmark identifies this as one of the top 5 conversion blockers on consumer PDPs, with documented impact on add-to-cart rate.

**Recommendation**
Change the add-to-cart button to the brand's accent color (#E84A2C, which is already used in the homepage hero) with white text. Secondary buttons (wishlist, share) should be outline-only or light grey. Maintain minimum 4.5:1 contrast ratio for readability. Button copy stays "Add to cart" — clearest term, no need for clever variants.

**Test specification**
- **Hypothesis:** If we change the add-to-cart button to brand accent color (#E84A2C) and demote secondary buttons to outline style, then add-to-cart rate will increase because users perceive the primary action more quickly (visual hierarchy).
- **Variant A:** current grey treatment
- **Variant B:** add-to-cart in #E84A2C accent, secondary buttons outline-only
- **Primary metric:** add-to-cart rate (PDP visits → cart add)
- **Secondary metrics:** time-to-first-click on PDP, bounce rate from PDP
- **Expected impact:** +4% to +12% on add-to-cart rate
- **ICE:** I=8, C=9, E=10 → 9.0
- **Source:** Baymard Institute PDP Usability research (2024-2025 benchmark); Cialdini's principles applied via visual prominence

---

## Example 2: 🔴 Critical — Reviews (mid-market home goods brand)

### 🔴 Reviews — No social proof above the fold

**Diagnosis**
The product has 142 reviews averaging 4.4 stars, but no rating summary appears above the fold. Users must scroll past two full screens to find any review information. Per Spiegel Research Center data, products with visible review summaries convert ~270% better than products without. The reviews already exist — they're just hidden from the moment of decision. This is leaving demonstrated trust on the table.

**Recommendation**
Add a compact review summary immediately below the product title, before the price: star rating visualization (★★★★☆) + numeric average (4.4) + clickable review count ("142 reviews") that scrolls to the reviews section. Place above the fold on both desktop and mobile.

**Test specification**
- **Hypothesis:** If we surface the existing review summary above the fold, then add-to-cart rate will increase because social proof is visible at the moment of purchase decision (Cialdini).
- **Variant A:** reviews only visible after scroll
- **Variant B:** review summary (stars + count) above the fold, clickable to scroll to reviews section
- **Primary metric:** add-to-cart rate
- **Secondary metrics:** scroll-to-reviews rate, click-through to review section
- **Expected impact:** +5% to +15% on add-to-cart rate (more conservative than Spiegel's headline figure since this is incremental, not adding reviews from zero)
- **ICE:** I=8, C=9, E=10 → 9.0
- **Source:** Spiegel Research Center (Northwestern); Cialdini's social proof principle; Baymard Institute review display research

---

## Example 3: 🟠 Important — Hero imagery (premium brand)

### 🟠 Hero & imagery — Missing lifestyle context shots

**Diagnosis**
The product page shows 4 product images, all studio-shot on white background. Per Baymard's PDP image research, considered consumer purchases benefit from in-context lifestyle shots that help users visualize the product in their own life. For a €240 premium ceramic vase, users need to assess scale, styling fit, and aesthetic context — none of which is possible with studio-only photography. The brand snapshot (premium, editorial, lifestyle-oriented) makes this gap even more visible: the homepage uses editorial lifestyle imagery extensively, but the PDP does not match this style.

**Recommendation**
Add 2-3 lifestyle shots: vase in a styled interior, vase on a dining table with flowers, vase in scale next to a reference object. Maintain the brand's editorial photography style (natural light, neutral tones, minimal styling) — do not switch to commercial product photography. Place lifestyle shots as image 2 and 3 in the gallery so they appear in the first swipe on mobile.

**Test specification**
- **Hypothesis:** If we add 2-3 editorial lifestyle shots to the image gallery, then add-to-cart rate will increase because users can better evaluate fit and aesthetics, reducing purchase anxiety (MECLABS conversion sequence, "a" factor).
- **Variant A:** current 4 studio shots
- **Variant B:** 4 studio + 3 lifestyle shots, with lifestyle as images 2-4 in gallery order
- **Primary metric:** add-to-cart rate
- **Secondary metrics:** image gallery interactions per session, returns rate (4-week lag)
- **Expected impact:** +3% to +8% on add-to-cart rate
- **ICE:** I=7, C=7, E=5 → 6.3
- **Source:** Baymard Institute PDP imagery research; MECLABS Conversion Sequence Heuristic (anxiety reduction)

---

## Example 4: 🟠 Important — Mobile sticky CTA (value brand)

### 🟠 Mobile experience — Missing sticky add-to-cart

**Diagnosis**
The mobile PDP is long-form: hero, variants, description, specs, reviews, related products — approximately 8 screens of scroll. The add-to-cart button appears only once, above the fold near the hero. Once the user scrolls past it to read reviews or specs, they must scroll all the way back up to act on intent. Per Baymard's mobile checkout research and Fitts's Law (action proximity), high-performing mobile PDPs use a sticky bottom-fixed add-to-cart that follows the user.

**Recommendation**
Implement a sticky bottom-fixed CTA on mobile only, appearing after the user scrolls past the original CTA. The sticky bar should contain: product thumbnail + price + "Add to cart" button. Use the same accent color as the primary CTA. Hide on the cart and checkout pages. Ensure tap target is minimum 44×44px (Apple HIG / Fitts's Law).

**Test specification**
- **Hypothesis:** If we add a sticky bottom-fixed add-to-cart bar on mobile PDP, then mobile add-to-cart rate will increase because the action remains available at the moment of intent regardless of scroll position.
- **Variant A:** mobile PDP without sticky CTA
- **Variant B:** sticky CTA bar appearing after scroll past original CTA
- **Primary metric:** mobile add-to-cart rate
- **Secondary metrics:** mobile PDP scroll depth, time-to-cart on mobile
- **Expected impact:** +4% to +10% on mobile add-to-cart rate
- **ICE:** I=7, C=8, E=7 → 7.3
- **Source:** Baymard Institute mobile commerce research; Fitts's Law applied to mobile UX

---

## Example 5: 🟢 Nice-to-have — Variant selector (mid-market)

### 🟢 Variant selectors — Out-of-stock sizes hidden instead of disabled

**Diagnosis**
When a size is out of stock, the size button disappears entirely from the selector. Per Baymard's PDP variant research, out-of-stock options should remain visible but disabled (greyed out, struck-through, or marked "out of stock"). Hiding them causes two issues: users can't tell whether their size simply doesn't exist or is temporarily unavailable, and the page silently fails users who would otherwise opt into stock notifications.

**Recommendation**
Show all sizes always. Out-of-stock sizes should appear greyed out with a strike-through or "out of stock" label. Add a "Notify me when back in stock" option that appears when an OOS variant is selected. Capture email for replenishment marketing.

**Test specification**
- **Hypothesis:** If we show out-of-stock variants as visible-but-disabled with notify-me capture, then notify-me signups will increase and abandoned-due-to-OOS will decrease.
- **Variant A:** OOS variants hidden
- **Variant B:** OOS variants visible-disabled + notify-me CTA
- **Primary metric:** notify-me email captures per PDP visit
- **Secondary metrics:** PDP exit rate when a popular size is OOS, eventual purchase rate from notify-me cohort
- **Expected impact:** moderate impact on notify-me captures (new metric), small impact on direct conversion
- **ICE:** I=4, C=8, E=6 → 6.0 (still nice-to-have because direct revenue impact is modest)
- **Source:** Baymard Institute PDP variant research; loss aversion (Kahneman/Tversky)

---

## Example 6: Test-not-recommended-yet finding

### 🟠 Detailed description — Possible scannability issue

**Diagnosis**
The detailed product description is approximately 600 words in 4 long paragraphs with no headers, bullets, or visual structure. Visually, this looks like a scanability problem per Nielsen Norman's F-pattern research. However, without scroll-depth data or session recordings, I cannot confirm whether users actually read this section or skip it entirely. The description might be a low-priority issue if users add to cart based on hero + reviews and never scroll here.

**Recommendation**
Restructure the description with: a 1-sentence opening benefit, 3-5 bullet points covering key benefits-over-features, a "More details" expandable section for the longer narrative. Use subheaders if narrative is preserved.

**Test specification**
Test not recommended yet — research first:
- Session recordings of 30-50 PDP sessions to confirm whether users scroll past description or read it
- Scroll-depth analytics on PDP to see the percentage of users reaching this section
- 5-second test on restructured description draft to validate clarity improvement
- If research confirms users read or attempt to read this section: proceed to A/B test with restructured version. Expected impact in that case: +2% to +6% on add-to-cart rate.

**ICE if research confirms relevance:** I=5, C=7, E=7 → 6.3

**Source:** Nielsen Norman Group F-pattern reading research; Baymard PDP description guidelines

---

## What makes these examples high-quality

- **Specific:** every observation names an exact element with attributes (color codes, pixel sizes, position)
- **Sourced:** every claim references a specific principle, study, or institution
- **Brand-aware:** recommendations consider whether they fit the brand snapshot
- **Honest about uncertainty:** when data is missing, the finding says so and recommends research, not action
- **Test-ready:** hypothesis follows "If X, then Y, because Z"; primary metric is named; ICE is justified by the breakdown
- **Concrete copy and behavior:** not "improve the CTA" — actual color hex, position, button text

Always match this standard. If a finding can't reach this standard, either dig deeper or remove it from the audit.
