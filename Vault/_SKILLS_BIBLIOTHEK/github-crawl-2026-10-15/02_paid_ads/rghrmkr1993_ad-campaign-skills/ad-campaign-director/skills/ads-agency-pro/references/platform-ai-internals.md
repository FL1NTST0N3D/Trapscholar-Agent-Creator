# Platform AI Internals: How the Machines Decide (and how to feed them)

Understanding WHY the platforms behave as they do turns knob-twiddling into engineering.
Formulas below are conceptual/approximate (platforms don't publish exact math). Research-
dated July 2026 (Meta/Google items revised October 2026).

## Meta, the 2026 AI stack

**Architecture:** Advertiser goal → campaign objective → Advantage+ AI → audience expansion
→ real-time auction → prediction models → ad ranking → delivery optimization → continuous
learning.

**Two brains:**
- **Andromeda**: the retrieval engine: picks which ads even enter ranking, keyed on
  creative signal (Entity IDs). Why concept diversity matters.
- **GEM (Generative Ads Recommendation Model)**: the LLM-scale ranking brain (announced and
  rolled out through 2025; sources vary between March, Q2 and a November paper, so no single
  date is reliable): trained across thousands of GPUs, transformer-based user modeling. Meta
  reported ~+5% Instagram / +3% FB Feed conversions from GEM alone. Andromeda completed
  rollout around October 2025.
- **Generative Recommender**: [F] Meta disclosed (earnings call, 2026) a further LLM-based
  ranking/matching layer alongside GEM and Andromeda. Practical implication is unchanged:
  creative supply and signal quality are the levers, not bid micro-management.
- [E] Ad-fatigue window of 2-3 weeks (see platforms-2026.md) is practitioner consensus, not
  an official Meta figure; high-spend accounts report faster fatigue.
- Supporting models: DNNs, multi-task learning, CTR/CVR/value prediction, large embeddings,
  graph neural networks (social graph), reinforcement learning, AutoML.

**Auction (every impression):**
```
Total Value ≈ (Advertiser Bid × Estimated Action Rate) + User Value − Negative Feedback
```
- Estimated Action Rate = predicted probability of YOUR optimization event (click,
  purchase, lead…) for THIS user.
- User Value / quality = predicted positive experience; Negative Feedback (hide/report
  rates) directly taxes delivery.
- Highest Total Value wins, a better-predicted ad beats a higher bid.

**Practical levers this implies:**
1. Raise Estimated Action Rate → better creative-audience fit, stronger hooks, cleaner
   conversion signal (Pixel+CAPI, EMQ ≥ 7). This beats raising bids.
2. Avoid negative-feedback taxes → no clickbait, no comment-bait, watch hide rates in
   account quality.
3. Feed the learning loop → consolidated structure, stable optimization events, exit
   learning phase (~50 events/week per ad set) before judging.
4. Advantage+ suite (Shopping, Audience, Placements, Creative, Catalog) = giving the two
   brains maximum freedom; constrain only with reason (brand safety, compliance).
5. DCO/Advantage+ Creative reassembles your assets, supply modular assets that survive
   recombination.

## Google, the 2026 AI stack

**Architecture:** Business goal → campaign → PMax/AI Max → auction-time AI → intent
prediction → real-time bid → Ad Rank → serving → learning loop. Gemini-powered LLMs for
creative generation + AI Brief brand guidance; TPU-scale training; transformer intent
models.

**Ad Rank (conceptual):**
```
Ad Rank ≈ Bid × Quality (Expected CTR × Ad Relevance × Landing Page Experience) + asset/context factors
```
Quality multiplies bid, a 2x-better ad can beat a 2x-higher bidder. Landing page
experience is IN the formula: LP work is ad work.

**Smart Bidding** (tCPA, tROAS, Max Conversions, Max Conversion Value) bids per-auction
using signals you can't segment manually: query intent, device, location, time, OS,
language, prior searches/purchases, audience membership, site interactions, Merchant
Center feed, conversion history, Customer Match lists.

**Practical levers:**
1. Smart Bidding is only as good as the conversion data → enhanced conversions, offline
   import (lead-gen), value rules for margin-weighted bidding. Garbage events in = garbage
   bidding out.
2. Feed quality IS targeting for Shopping/PMax → titles, attributes, price sync,
   availability (see ecommerce section in optimization-automation.md).
3. tROAS/tCPA targets are throttles: set from account history (start ~10-15% looser than
   goal, tighten in steps), not from wishes. Too-aggressive targets strangle volume.
4. Give PMax full asset coverage (text+image+video) or it under-serves surfaces; use AI
   Max with text guidelines + pinned headlines + negatives as guardrails.
5. Audience signals in PMax are hints, not limits, seed with buyers, not broad interests.

## Steering doctrine (both platforms)

The platforms run the microseconds (auction, bid, per-user prediction). You run the
macro-inputs: objective/event choice, signal quality, creative supply, budget structure,
guardrails, measurement truth. Never fight the machine at its own layer (manual bid
micro-management, hyper-segmentation), improve its inputs instead.

## Secondary platforms, quick objective map

| Platform | Formats | Wins for | Notes |
|---|---|---|---|
| Microsoft/Bing | Search, Audience Network | B2B, older/desktop demos, cheap search intent | Import Google campaigns, then prune |
| LinkedIn | Sponsored Content, Lead Gen Forms, Conversation, Dynamic | B2B ABM, high-ACV pipeline | Expensive CPCs; offline-conversion feedback essential |
| TikTok | In-feed, Spark Ads, Shop | Gen-Z/millennial commerce (geo-check: banned in India) | Spark = whitelisted organic; Smart+/GMV Max per platforms-2026.md |
| Pinterest | Shopping, Idea ads | Home, fashion, wedding, food planning intent | Long content half-life; early-funnel + catalog |
| Snapchat | Story, Collection, AR | Under-25 reach, KSA/GCC strength | AR try-on for beauty/fashion |
| Reddit | Promoted posts | Tech, gaming, finance, niche communities | Community-native copy or death by downvote |
| Amazon | Sponsored Products/Brands, DSP | Marketplace-heavy retail | Bottom-funnel harvest; defend brand terms |
| X | Promoted posts, video | News-adjacent, tech, live moments | Brand-safety controls first |

Budget rule: master Meta+Google first (80%+ of most SMB/mid-market results), add
secondaries only with a specific job (LinkedIn for B2B ABM, Amazon for marketplace share,
Snapchat for GCC youth), never for coverage vanity.
