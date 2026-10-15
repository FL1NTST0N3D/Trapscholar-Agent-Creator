# YouTube Targeting Strategy Skill

**Command:** `/yt targeting`

## Purpose

Analyzes and optimizes YouTube ad targeting strategy across all available audience types. YouTube's targeting capabilities are uniquely powerful because they combine Google Search intent data with video viewing behavior — something no other platform can replicate. This skill evaluates audience selection, layering strategy, and exclusion hygiene.

## YouTube Audience Types — Deep Reference

### 1. Custom Intent Audiences (Highest Priority)

Custom Intent is the single most powerful YouTube targeting option. It lets you target users based on what they recently searched on Google — bringing search intent to video advertising.

**How It Works:**
- You provide Google Search keywords (e.g., "best CRM software," "CRM comparison 2026")
- Google identifies users who searched those terms in the last 7-14 days
- Those users see your YouTube ads while watching videos

**Best Practices:**
- Use 10-15 keywords per Custom Intent audience (Google's sweet spot)
- Include branded competitor keywords (e.g., "Salesforce alternatives")
- Mix high-intent commercial keywords with informational keywords
- Create separate Custom Intent audiences for different intent levels:
  - Research intent: "what is [product category]"
  - Comparison intent: "[product A] vs [product B]"
  - Purchase intent: "[product] pricing," "[product] free trial"
- Refresh keywords quarterly — search trends shift

**Scoring (0-20 points):**
- Custom Intent audiences active with 10-15 relevant keywords: 20 points
- Custom Intent active but keywords are too broad or too few: 12 points
- No Custom Intent audiences: 0 points (major gap)

### 2. Affinity Segments

Broad interest-based audiences built from long-term browsing and viewing behavior. Best for top-of-funnel awareness campaigns.

**When to Use:**
- Brand awareness campaigns with broad reach goals
- Layered with demographic targeting for refined reach
- When Custom Intent is too narrow for the desired volume

**When NOT to Use:**
- Performance/conversion campaigns (too broad)
- Small budgets under $2K/month (wastes spend on unqualified viewers)

**Custom Affinity Audiences:**
Instead of using Google's pre-built Affinity segments, create Custom Affinity audiences using:
- URLs of websites your target audience visits
- Apps your target audience uses
- Specific interests and topics

**Scoring (0-10 points):**
- Affinity used appropriately for awareness, not for conversion campaigns: 10 points
- Affinity used as sole targeting for conversion campaigns: 3 points (misuse)

### 3. In-Market Segments

Users actively researching or comparing products in a specific category. Google identifies these users based on recent search activity, website visits, and content consumption patterns.

**Best Practices:**
- In-Market segments are Google's second-most-powerful YouTube audience (after Custom Intent)
- Layer In-Market with demographic filters for precision
- Use In-Market for consideration and conversion campaigns
- Monitor which In-Market segments drive actual conversions, not just views
- Some In-Market segments are very broad (e.g., "Travel") — prefer specific sub-segments

**Scoring (0-15 points):**
- Relevant In-Market segments active with performance data reviewed: 15 points
- In-Market active but no performance analysis done: 8 points
- No In-Market targeting: 3 points

### 4. Life Events

Target users going through major life transitions that trigger purchase behavior. Available Life Events include:

- About to graduate / Recently graduated
- About to move / Recently moved
- About to get married / Recently married
- About to retire / Recently retired
- Starting a new business
- Purchasing a home
- Having a baby

**Best For:** Real estate, insurance, financial services, home furnishing, wedding services, baby products, career services.

**Scoring (0-5 points):**
- Life Events used where relevant to the product: 5 points
- Life Events available but not utilized: 2 points

### 5. Remarketing Lists

Re-engage users who have already interacted with your brand. YouTube remarketing lists include:

- **Video viewers:** Users who watched any video, specific videos, or watched as an ad
- **Channel subscribers:** Current subscribers to your YouTube channel
- **Channel visitors:** Users who visited your channel page
- **Video likers/commenters:** Users who engaged with your content
- **Website visitors:** Users who visited your site (from Google Ads remarketing tag)
- **Customer lists:** Email lists uploaded to Google Ads (Customer Match)
- **App users:** Users of your mobile app

**Best Practices:**
- Create tiered remarketing lists by engagement depth:
  - Tier 1: Watched 75%+ of a video (highest intent)
  - Tier 2: Watched 25-75% of a video
  - Tier 3: Saw a video impression but did not watch
- Exclude converters from prospecting campaigns
- Set appropriate membership duration (30-90 days for most businesses)

**Scoring (0-20 points):**
- 3+ remarketing lists active with tiered strategy: 20 points
- Basic remarketing (all visitors, one list): 10 points
- No remarketing: 0 points

### 6. Placement Targeting

Target specific YouTube channels, videos, websites, or apps where your ads appear:

- **Channel targeting:** Choose specific YouTube channels relevant to your audience
- **Video targeting:** Target individual high-performing videos
- **Topic targeting:** Target videos about specific topics (broader than channel targeting)
- **Keyword targeting:** Target videos with specific keywords in title/description (contextual)

**Scoring (0-10 points):**
- Placement targeting used with exclusions and performance monitoring: 10 points
- Broad placement with no exclusions: 4 points

### 7. Demographic Layering

Always layer demographics on top of audience targeting:
- Age ranges (remove irrelevant age brackets)
- Gender (if product is gender-specific)
- Household income (for premium products, target top 30%)
- Parental status (for family-relevant products)

**Scoring (0-10 points):**
- Demographics refined and irrelevant segments excluded: 10 points
- Default demographics (all ages, all genders): 3 points

## Targeting Strategy Evaluation

### Audience Layering Assessment

The best YouTube campaigns use layered targeting — combining multiple audience signals:

**Example of Strong Layering:**
Campaign: B2B SaaS product
- Custom Intent: "CRM software," "Salesforce alternative," "best CRM 2026"
- In-Market: "Business Software > CRM"
- Demographics: Age 25-54, Household Income Top 30%
- Placement Exclusion: Kids content, gaming channels, music videos

**Example of Weak Targeting:**
Campaign: Same B2B SaaS product
- Audience: Affinity "Technology" (too broad)
- No demographic filters
- No placement exclusions

### Exclusion Hygiene

Exclusions are as important as inclusions. Check for:

- **Content exclusions:** Are sensitive content categories excluded?
- **Placement exclusions:** Are irrelevant channels/topics blocked?
- **Audience exclusions:** Are existing customers excluded from acquisition campaigns?
- **Age exclusions:** Are minors excluded for adult products?

## Composite Targeting Score

```
Targeting Score = Custom Intent + In-Market + Affinity Usage + Life Events +
                  Remarketing + Placements + Demographics + Exclusions
Maximum: 100 points (normalized from components above)
```

## Output Format

```
## Targeting Analysis: [Score]/100

### Audience Strategy Summary
| Audience Type | Status | Quality | Recommendation |
|---------------|--------|---------|----------------|
| Custom Intent | Active/Missing | /20 | |
| In-Market | Active/Missing | /15 | |
| Affinity | Active/Missing | /10 | |
| Life Events | Active/N/A | /5 | |
| Remarketing | Active/Missing | /20 | |
| Placements | Active/Missing | /10 | |
| Demographics | Refined/Default | /10 | |

### Critical Gaps
1. ...

### Recommended Audience Additions
1. Custom Intent audience: [suggested keywords]
2. In-Market segment: [suggested segment]
3. Remarketing list: [suggested configuration]

### Exclusion Recommendations
1. ...
```
