# YouTube Placements Skill

**Command:** `/yt placements`

## Purpose

Audits YouTube ad placement strategy including channel exclusions, content exclusions, placement performance, brand safety settings, and inventory type selection. Placement hygiene is one of the most neglected areas in YouTube advertising — most advertisers never review where their ads actually appear, resulting in wasted spend on irrelevant or brand-unsafe placements. This skill provides a systematic framework for placement optimization.

## Placement Hygiene Framework

### Inventory Type Selection

Google Ads offers three inventory types that control the breadth of content where your ads can appear. This is the first and most important placement decision:

| Inventory Type | Description | Best For | Risk Level |
|---------------|-------------|----------|------------|
| **Expanded Inventory** | Ads can appear on all YouTube content that meets minimum monetization standards. Includes edgy, controversial, and mature content. | Maximum reach at lowest CPM. Only for brands with high risk tolerance. | High |
| **Standard Inventory** | Ads appear on content suitable for most brands. Excludes extremely sensitive content but allows some mature themes. | Default for most advertisers. Balanced reach and safety. | Medium |
| **Limited Inventory** | Ads only appear on content verified as brand-safe. Excludes any content with profanity, sexual themes, violence, or controversial topics. | Brand-sensitive advertisers (luxury, children, healthcare, financial). | Low |

**Scoring (0-15 points):**
- Inventory type consciously selected and appropriate for brand: 15 points
- Using default Standard without conscious choice: 8 points
- Using Expanded for a brand-sensitive advertiser: 0 points

### Content Exclusion Settings

Beyond inventory type, Google Ads offers granular content exclusions. Review each:

**Content Suitability Exclusions:**
| Category | Default | Recommendation |
|----------|---------|----------------|
| Embedded YouTube videos | Included | Exclude (low visibility, poor placements) |
| Live streaming videos | Included | Keep for events, exclude for always-on |
| Tragedy and conflict | Excluded in Limited | Always exclude for brand safety |
| Sensitive social issues | Excluded in Limited | Exclude unless advocacy brand |
| Profanity and rough language | Varies by inventory | Exclude for family/professional brands |
| Sexually suggestive content | Excluded in Limited | Always exclude unless adult industry |
| Sensational and shocking | Excluded in Limited | Always exclude |

**Digital Content Labels:**
- DL-G (General audiences): Always include
- DL-PG (Most audiences): Include for most brands
- DL-T (Teen and older): Include selectively
- DL-MA (Mature audiences): Exclude for most brands

**Scoring (0-15 points):**
- Content exclusions reviewed and configured: 15 points
- Partial exclusions, some gaps: 8 points
- Default settings, never reviewed: 3 points

### Channel Exclusion Strategy

Channel exclusions prevent your ads from appearing on specific YouTube channels. This is critical for both brand safety and performance optimization.

**Channels to Exclude (Universal):**
1. **Kids' content channels** (unless targeting parents with children's products)
2. **Music video channels** — high impressions but extremely low engagement (viewers are there for music, not ads). Average view rate on music channels is 50% lower than non-music.
3. **Gaming compilation channels** — young demographic, low purchase intent for most B2B/professional products
4. **ASMR and ambient channels** — viewers in passive/sleep mode, near-zero ad engagement
5. **Foreign language channels** (if targeting English-speaking audiences)
6. **Competitor channels** — debatable. Some brands exclude competitors to avoid appearing as subordinate. Others target competitor channels intentionally.

**Building a Channel Exclusion List:**
1. Export the Placement Report from Google Ads (Where Ads Showed > YouTube channels)
2. Sort by cost (highest first)
3. Review top 50 channels by spend
4. Exclude any channel that has high cost but zero conversions and low view rate
5. Repeat monthly — new channels constantly enter the rotation

**Scoring (0-20 points):**
- Active channel exclusion list with 50+ channels, reviewed monthly: 20 points
- Some exclusions but not regularly reviewed: 10 points
- No channel exclusions: 0 points (critical gap)

### Placement Performance Analysis

For accounts with placement targeting (not just exclusions), evaluate:

**Managed Placements:**
Managed placements are specific YouTube channels or videos that you choose to target. This is a precision tactic:

- Review CTR and view rate per managed placement
- Compare performance to automatic placements
- Remove placements with CTR below 0.3% and view rate below 15%
- Identify top 10 placements by conversion rate and increase bids on them
- Test adding new placements quarterly based on audience research

**Automatic vs. Managed Placement Split:**
- 100% automatic: Account is relying entirely on Google's algorithm for placement decisions. Works for broad awareness but wastes spend for performance campaigns.
- 70% automatic + 30% managed: Healthy split. Managed placements for high-intent targeting, automatic for discovery.
- 100% managed: Very restrictive. Limited scale but maximum control. Best for small budgets or brand-safety-critical advertisers.

**Scoring (0-20 points):**
- Regular placement review, managed placement strategy, exclusions active: 20 points
- Automatic placements only with some exclusions: 10 points
- No placement strategy at all: 0 points

### Topic & Keyword Targeting

Topic and keyword targeting control the type of content (not specific channels) where ads appear:

**Topic Targeting:**
- Select broad topic categories (Technology, Business, Health, etc.)
- Useful for aligning ad context with product category
- Do not stack too many topics — each additional topic narrows reach significantly

**Keyword Targeting (Contextual):**
- Target videos with specific keywords in title, description, or tags
- More precise than topic targeting but lower volume
- Use 5-15 keywords per ad group
- Include competitor brand names as keywords (your ad appears on videos about competitors)

**Scoring (0-15 points):**
- Topic or keyword targeting used strategically: 15 points
- Overly broad or no contextual targeting: 5 points

### Brand Safety Configuration

Beyond content and channel exclusions, verify these brand safety settings:

1. **Third-party verification:** Is a brand safety vendor active? (IAS, DoubleVerify, MOAT)
2. **Google Ads brand safety center:** Are suitability settings configured?
3. **Negative keyword lists:** Are there content-level negative keywords? (e.g., exclude content mentioning "scandal," "controversy," "crime")
4. **Advertiser verification:** Is the account verified for expanded placement controls?
5. **Incident response plan:** Does the team have a process for pausing ads if they appear on inappropriate content?

**Scoring (0-15 points):**
- Third-party verification active, comprehensive settings: 15 points
- Google settings configured, no third-party: 8 points
- Default settings: 3 points

## Composite Placement Score

```
Placement Score = Inventory Type (15) + Content Exclusions (15) +
                  Channel Exclusions (20) + Placement Performance (20) +
                  Topic/Keyword Targeting (15) + Brand Safety (15)
Maximum: 100 points
```

## Output Format

```
## Placement Audit: [Score]/100

### Inventory & Safety
| Setting | Current | Recommended | Impact |
|---------|---------|-------------|--------|
| Inventory Type | | | |
| Content Exclusions | | | |
| Brand Safety Vendor | | | |

### Channel Exclusion Analysis
- Current exclusion list size: [X channels]
- Top 5 wasteful placements (high cost, low performance):
  1. ...

### Placement Performance
| Metric | Managed | Automatic |
|--------|---------|-----------|
| View Rate | | |
| CTR | | |
| Conv Rate | | |
| CPV/CPM | | |

### Recommended Actions
1. [Immediate exclusion actions]
2. [Placement targeting additions]
3. [Brand safety improvements]
```
