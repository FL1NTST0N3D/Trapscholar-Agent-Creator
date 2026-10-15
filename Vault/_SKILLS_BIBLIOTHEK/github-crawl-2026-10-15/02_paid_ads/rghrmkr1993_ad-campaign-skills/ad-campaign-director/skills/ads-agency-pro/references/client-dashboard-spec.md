# Client Dashboard Spec: Daily Results Dashboard

Purpose: a client-facing daily dashboard that answers "is it working?" in 5 seconds and
shows momentum with a clear narrative.

## Reporting model, pick ONE per client, contract decides

- **Results-focused (fixed-fee / outcome engagements):** client buys deliverables and
  outcomes; dashboard shows results without media line items. Legitimate ONLY when the
  contract is priced that way and the client understands the model.
- **Full-transparency (pass-through media engagements):** client pays ad spend directly or
  as a pass-through; dashboard must include spend, ROAS, CPA.

**The contract always wins.** Never hide spend from a client whose agreement entitles them
to it. The operator/agency owner always keeps a full internal view with complete economics.

## Metric law (results-focused model)

**ALLOWED (client view):**
- Revenue / sales value attributed (ecom), Orders / purchases, Leads / sign-ups / bookings
- Conversion rate (visits→orders or leads→qualified)
- Reach, Impressions, Video views / ThruPlays, Engagement (likes/comments/shares/saves)
- CTR (reveals nothing about cost)
- Top creatives / winning angles (thumbnails + result counts)
- Trends: daily/weekly lines, week-over-week %, milestone callouts, festival annotations
- Funnel counts: sessions, add-to-carts, checkouts (ecom)

**EXCLUDED (client view, results-focused model), anything that exposes or lets the client
reverse-derive media cost:**
- Spend, budget, remaining balance
- CPM, CPC, CPA, CPL, cost-per-anything
- ROAS (revenue ÷ ROAS = spend, leaks immediately)

Sanity check before every publish: "Can any two numbers on this page be combined to compute
spend?" If yes, remove one.

## Layout (top to bottom, 5-second rule)

1. **Hero verdict strip**: 3-4 stat tiles: Revenue (or Leads), Orders, Conversion rate,
   Reach. Each with WoW delta arrow. One-line verdict headline written like a finding:
   "Strong week: orders up 24% on the new festival creative."
2. **Daily trend chart**: orders/leads + revenue lines, last 30 days, festival/launch
   annotations. Title states the finding, not the metric.
3. **Funnel bar**: reach → clicks → sessions → carts → orders (counts + stage conversion %).
4. **Creative leaderboard**: top 3-5 ads by results (thumbnail, angle name, orders/leads,
   CTR). Reinforces the work being done.
5. **Geo/language split**: results by market/language (map or bars), clients love seeing
   e.g. Tamil vs Telugu vs English performance.
6. **What we did / what's next**: 3-5 bullets each, dated. This is the storytelling layer;
   ~43% of clients report being unsatisfied with agency reports, mostly for lack of narrative.

## Implementation

- Single self-contained HTML file per client: `dashboards/{client}-dashboard.html`,
  published privately (e.g., a private Artifact or password-protected page). Redeploy the
  SAME file/URL daily so the client link never changes.
- Theme-aware (light/dark), mobile-first, no horizontal scroll, inline SVG/CSS charts only
  if your host blocks external libraries.
- Keep an internal companion `dashboards/{client}-internal.html` (NEVER shared) with full
  economics: spend, ROAS, CPA, margin, pacing vs budget.
- Data pipeline per update:
  1. Meta: insights API/MCP tools for reach, impressions, clicks, purchases, revenue,
     per-ad results.
  2. Google Ads: API, browser session, or scheduled exports.
  3. GA4 (where installed): sessions, carts, checkouts for funnel counts.
  4. Reconcile: platform-attributed revenue vs GA4/store orders, footnote the attribution
     basis on the dashboard ("platform-attributed, 7-day click").
- Update cadence: daily during active flights (schedule a recurring task invoking the
  `ad-campaign-director` agent with "daily update for {client}"); weekly narrative refresh
  of the "What we did / what's next" section.
- Anomaly flags (internal only): tracking breakage, delivery stoppage, policy rejection,
  pacing outside the thresholds in runbooks-incidents.md (investigate at ±20% daily
  variance, emergency above 2x daily budget), surface to the operator same-day, never
  silently on the client view.

## Writing style on the dashboard

- Chart titles are findings: "Reels drove 68% of new orders this week", not "Orders by placement".
- Numbers formatted for the client's market (₹ lakh notation for India, $/£ elsewhere).
- Zero jargon: "people reached", "orders", "sales value", not "conv. value".
- Every week has at least one insight the client couldn't get from a screenshot. That is
  what they are paying for.
