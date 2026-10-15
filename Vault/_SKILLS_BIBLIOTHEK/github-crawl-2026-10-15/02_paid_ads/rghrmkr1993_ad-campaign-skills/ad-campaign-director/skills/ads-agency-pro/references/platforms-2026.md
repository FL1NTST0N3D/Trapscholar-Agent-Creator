# Platform Doctrine 2026

Research-dated October 2026. Platform mechanics drift, re-verify in official consoles before acting.

## Meta (Facebook + Instagram), the Andromeda era

**What changed:** Andromeda is Meta's AI ad-retrieval system (runs under ALL campaign types,
not just Advantage+ Shopping). It matches ads to individuals by creative signal. Audience
settings are now weak inputs; creative diversity is the strong input.

**Structure:**
- Advantage+ Shopping (A+SC), now generally called Advantage+ Sales after a rename (recognise
  either name in briefs, consoles and sources), as the primary ecom campaign, it now carries ~62% of ecom
  conversion spend on Meta and averages ~4.52x ROAS vs ~3.70x for manual setups (+22%).
- 2-3 ad sets max per campaign: broad prospecting, retargeting, optional testing.
- 1 ad set × 25 creatives beat 5 ad sets × 5 creatives by +17% conversions at -16% cost in
  Meta's own testing.
- Skip lookalikes for most accounts, the behavioral signal already exceeds seed audiences.
- [F] Ad-set level placement exclusions are being removed for Sales/Leads objectives
  (progressive rollout, AI chooses placements). Placement control is weakening: build every
  creative for all placements (Feed, Stories, Reels) with safe zones, do not rely on excluding
  weak placements.

**Creative rules:**
- 10-15 conceptually distinct assets per A+SC campaign; brands testing 20+ new ads/month see
  ~65% higher ROAS than brands testing <10.
- Entity ID trap: visually/structurally similar ads are collapsed into one entity, if the
  entity loses the retrieval auction, ALL its variants go unserved. Diversify concept, angle,
  emotional entry point, format, creator.
- Fatigue window is now 2-3 weeks (was 6+). Refresh 25-30% of assets every 2 weeks at scale.
  [E] 2-3 weeks is practitioner consensus, not an official Meta figure; high-spend accounts
  report faster fatigue.
- [E] Meta now shows a "Creative Diversity" score (Low/Medium/High) per ad set in Ads Manager.
  Directional only: practitioners report a healthy creative mix can still score Low. Use it
  as a prompt to audit concept spread, not as a KPI.
- Advantage+ Creative enhancements on = ~22% ROAS lift in Meta testing.

**Signal:**
- Pixel + Conversions API simultaneously; Event Match Quality ≥ 7.
- Give the account 7-10 days of learning before structural judgment.

**Levers ranked:** creative diversity > structure consolidation > signal quality > budget moves.

## Google Ads, the Power Pack

Google's 2026 framework coordinates three AI campaign types. The budget split below is NOT
official Google guidance and sources disagree (alternatives seen: 70-20-10, PMax 25-40%).
[E] Treat it as a starting heuristic to be replaced by the account's own marginal-return
data, not a rule.

| Campaign | Role | Ecom budget | B2B budget |
|---|---|---|---|
| Performance Max | Full-funnel conversion capture across all Google surfaces | 50-60% | 30-40% |
| AI Max for Search | High-intent query capture incl. AI-expanded matching | 30-40% | 40-50% |
| Demand Gen | Upper-funnel demand creation (YouTube, Discover, Gmail) | 10-20% → scale on proof | 10-20% |

**Demand Gen four pillars (Feb 2026 official best practices, adopting ≥3 of 4 = ~40% more
conversions):**
1. Audiences: optimized targeting + lookalikes + new-customer acquisition goals.
2. Bid/budget: tCPA or tROAS with adequate budget (not starved).
3. Creative: "Excellent" Ad Strength; full asset coverage incl. video.
4. Data: sitewide Google tag (tag gateway), Data Manager with offline sources connected.

**AI Max for Search:** use text guidelines (brand voice, banned terms), pin critical
headlines/descriptions, add negative controls. Treat it as broad-match-plus-with-guardrails.

**Forced migrations (2026):**
- [F] AI Max migration is now forced, not optional: Search campaigns using campaign-level
  broad match or automated campaign assets auto-migrate to AI Max, and new campaigns with
  those settings can no longer be created. Plan guardrails (text guidelines, pins, negatives)
  before the migration lands, not after.
- [F] Dynamic Search Ads migration to AI Max was postponed to Feb 2027, with no new DSA ad
  groups from Jan 2027.
- [F] Standalone Display campaigns are being retired into Demand Gen. A migration tool is
  rolling out, the target for blocking new Display campaigns is around Jan 2027, and the
  migration is one-way: snapshot settings, assets and performance before converting.
- [F] Smart Bidding now pursues tCPA/tROAS targets more literally, so loose or mismatched
  targets lose volume. Set targets deliberately from account history and re-check after any
  migration.

**Non-negotiables:** video assets for PMax/Demand Gen (static-only setups underperform);
enhanced conversions; brand exclusions checked in PMax; search terms + placement reports
reviewed weekly (use the `ads` skill audit for this).

## YouTube, three surfaces, three creatives

| Surface | Creative | Notes |
|---|---|---|
| In-stream (mobile/desktop) | 15-60s skippable, brand in first 5s | Brand-before-skip = ~40% higher VTR |
| Shorts feed | 9:16 native, hook <2s, 15-30s sweet spot | Native-style beats repurposed landscape up to 3x on completion; CPMs ~$4-12 vs $8-18 in-stream |
| Connected TV | 30-60s cinematic, sequential messaging | 95%+ completion; lean-back; big-brand feel, right fit for film + premium skincare |

- Put 20-30% of YouTube budget on Shorts when the audience skews under 35.
- Format ↔ funnel: 6s bumpers = awareness at scale; skippable 15-60s = consideration;
  15s non-skip = guaranteed brand moments.
- For India: YouTube is the #1 video platform in every language market, regional-language
  voiceover + subtitles beats English VO for tier-2/3.

## TikTok, Smart+ and GMV Max (NON-INDIA ONLY)

**India: banned since June 2020, still banned in 2026 (re-confirmed Oct 2026). Never plan TikTok for India.**
Use for: Sri Lanka, Malaysia, Singapore, US, UK.

- **Smart+** = TikTok's Advantage+ equivalent (auto creative/targeting/bidding). TikTok
  reports ~52% ROAS improvement on Smart+ Web campaigns. Smart+ now automates Search Ads
  too.
- **GMV Max** = default campaign type for TikTok Shop from July 2026. Hero-SKU selection is
  the core decision; set target ROI as the optimization signal; keep feeding varied creative;
  maintain continuous affiliate/creator recruitment, brands that stop recruiting creators see
  3-5 months growth then hard plateau. GMV Max now factors seller costs (affiliate commission,
  coupons, fees) into optimization, so model net margin after those costs before setting
  target ROI.
- SEA CPM advantage: $1-5 (vs $8-15 in premium APAC), cheap reach for MY/SG tests.
- Localize per market: separate ad groups per language; adapt sounds/humor/references, not
  just translation.
- Live Shopping is a mainstream SEA channel, plan host-led live sessions for fashion/beauty
  clients in MY/SG.

## Cross-platform budget starting points (adjust per client)

- **Ecom (fashion/skincare), India:** Meta 55-65% / Google (PMax+Search) 25-35% / YouTube-in-
  Google remainder. Reels+Shorts carry short-video.
- **Ecom, MY/SG:** Meta 40-50% / TikTok 20-30% / Google 25-30%.
- **Film release, India:** YouTube 40-50% (trailer + Shorts) / Meta 35-45% (Reels, meme,
  creator whitelisting) / Google Search+Display 10-15% (title + "booking" intent).
- **Tech/B2B:** Google Search/AI Max 40-50% / Demand Gen+YouTube 20-30% / Meta 20-30% for
  retargeting + founder-brand content.
