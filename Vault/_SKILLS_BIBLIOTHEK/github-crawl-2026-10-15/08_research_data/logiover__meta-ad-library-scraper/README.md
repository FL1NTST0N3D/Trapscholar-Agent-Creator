# Facebook Ad Library Scraper — Meta Ads Spy Tool, Creatives & Spend

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-00A67E?logo=apify&logoColor=white)](https://apify.com/logiover/meta-ad-library-scraper)
[![Run on Apify](https://img.shields.io/badge/▶️_Run_on-Apify-1C7ED6?logo=apify&logoColor=white)](https://apify.com/logiover/meta-ad-library-scraper)
![No login](https://img.shields.io/badge/No%20login-required-2ea44f)
![No API key](https://img.shields.io/badge/No%20API%20key-required-2ea44f)
![Export](https://img.shields.io/badge/Export-JSON%20%7C%20CSV%20%7C%20Excel-F59E0B)

## ▶️ [Run the Facebook Ad Library Scraper on Apify »](https://apify.com/logiover/meta-ad-library-scraper)

Scrape **Facebook and Instagram ads** from the **Meta Ad Library** by keyword or advertiser Page. This **Facebook Ad Library scraper** pulls every running and past ad with its full creative — body text, headline, caption, carousel card texts, call-to-action, image and video URLs — plus platform breakdown, lifecycle dates, active status and, for political & issue ads, **estimated spend, impressions and reach**. Feed it search keywords, exact advertiser Page IDs, or both, and receive analysis-ready rows you can export to CSV, JSON or Excel.

It is the practical **Meta Ads spy tool** and **Facebook Ad Library API alternative** for competitor ad research, creative swipe files, market intelligence and political-ad transparency work. **No login, no cookies, no account, and no developer API key** — you just provide a search and get thousands of structured ad records back.

> This repository is **documentation only**. The scraper itself runs on the Apify platform — **[open it here](https://apify.com/logiover/meta-ad-library-scraper)** and click **Try for free**.

---

## What you get

Every ad is returned as one flat, de-duplicated JSON row. Key output fields:

| Field | Description |
|-------|-------------|
| `adArchiveId` | Unique Meta Ad Library ID for the ad |
| `adLibraryUrl` | Direct link to the ad in the Meta Ad Library |
| `pageId` / `pageName` / `pageUrl` | Advertiser Facebook Page ID, name and URL |
| `pageProfilePicture` | Advertiser Page profile picture URL |
| `pageCategories` | Category labels of the advertiser Page |
| `pageLikeCount` | Number of likes on the advertiser Page |
| `isActive` / `status` | Whether the ad is currently running (`active` / `inactive`) |
| `startDate` / `endDate` | When the ad started and stopped running (ISO 8601) |
| `totalActiveTime` | Total time the ad has been active, in seconds |
| `publisherPlatform` | Platforms the ad runs on (Facebook, Instagram, Messenger, Audience Network) |
| `bodyText` | Primary body text of the ad creative |
| `title` / `caption` / `linkDescription` | Headline, caption (display domain) and link description |
| `linkUrl` | Destination URL the ad links to |
| `ctaText` / `ctaType` | Call-to-action button label and type |
| `displayFormat` | Creative format (image, video, carousel, DCO…) |
| `cardTexts` | Text of each carousel card |
| `byline` / `disclaimerLabel` | Paid-for-by byline and disclaimer (political ads) |
| `media` | Image and video creative URLs |
| `spend` / `spendLowerBound` / `spendUpperBound` / `currency` | Estimated spend range (political & issue ads) |
| `impressions` | Impressions range text (political & issue ads) |
| `reachEstimate` / `reachLowerBound` / `reachUpperBound` | Estimated reach (EU ads) |
| `targetedOrReachedCountries` | Countries targeted or reached |
| `categories` | Ad category codes |
| `containsSensitiveContent` | Whether the ad is flagged as sensitive |
| `collationCount` | Number of near-duplicate variants collated together |
| `searchedFor` | The keyword or Page this ad was found by |
| `scrapedAt` | When the record was scraped (ISO 8601) |

- **No login, no cookies, no account risk** — reads only the public Meta Ad Library.
- **Facebook + Instagram** creatives, including every carousel card.
- **Thousands of ads per search**, streamed to your dataset as they are found.
- **Political-ad transparency**: spend, impressions and reach where Meta discloses them.

## Use cases

- **Competitor ad spy** — swipe winning creatives, hooks and offers from any competitor's Facebook Page.
- **Creative research & swipe files** — build a library of high-performing ad angles by product category or niche.
- **Ad spend & impressions intelligence** — for political & issue ads, track estimated spend, impressions and reach over time.
- **Market & trend analysis** — monitor how an entire industry (crypto, real estate, SaaS, DTC brands) is advertising right now.
- **Agency competitive reporting** — show clients exactly what their rivals are running across Facebook and Instagram.
- **Political & issue-ad monitoring** — journalists and researchers auditing who is paying for political messaging and how much.
- **Housing, employment & credit ad compliance** — pull the special ad categories Meta labels for fair-advertising review.
- **Landing-page & funnel research** — capture the destination `linkUrl` and CTA of every ad to reverse-engineer competitor funnels.

## Quick start

### 1. Apify Console (no code)
Open the **[Facebook Ad Library Scraper](https://apify.com/logiover/meta-ad-library-scraper)**, click **Try for free**, type a brand or keyword into **Search terms** (e.g. `nike`), pick a **Country**, and press **Start**. Results appear in the **Output** tab, ready to export.

### 2. Apify CLI
```bash
npm install -g apify-cli
apify login
apify call logiover/meta-ad-library-scraper --input '{
  "searchTerms": ["nike", "running shoes"],
  "country": "US",
  "maxResults": 500
}'
```

### 3. API / curl
```bash
curl -X POST "https://api.apify.com/v2/acts/logiover~meta-ad-library-scraper/run-sync-get-dataset-items?token=YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerms": ["crypto"],
    "country": "US",
    "adType": "all",
    "maxResults": 200
  }'
```

### 4. apify-client (JavaScript & Python)
See [`examples/javascript.md`](examples/javascript.md) and [`examples/python.md`](examples/python.md) for full, copy-pasteable client snippets. More curl recipes are in [`examples/api-curl.md`](examples/api-curl.md) and CLI usage in [`examples/cli.md`](examples/cli.md).

## Input

Provide at least one value in **Search terms** *or* **Advertiser Page IDs**. Everything else is optional; sensible defaults are used.

| Field | Type | Description |
|-------|------|-------------|
| `searchTerms` | array | Keywords or advertiser/brand names to search for (e.g. `nike`, `crypto`, `real estate agent`). |
| `pageIds` | array | Optional. Exact Facebook Page IDs to pull every ad from one advertiser (found in an ad's `view_all_page_id=` URL). |
| `country` | select | Country of the ad audience — 42 options including `ALL` (worldwide), `US`, `GB`, `DE`, `IN`, `AU`… Default `US`. |
| `adType` | select | `all`, `political_and_issue_ads` (spend/impressions shown), `housing_ads`, `employment_ads`, `credit_ads`. |
| `activeStatus` | select | `all`, `active` only, or `inactive` only. |
| `mediaType` | select | Filter by creative format: `all`, `image`, `video`, `meme`, `image_and_meme`, `none`. |
| `maxResults` | integer | Total ads to collect across all searches. `0` = unlimited. Default `200`. |
| `proxyConfiguration` | proxy | Residential proxy (required by Meta) — keep the default. |

## Output

A realistic sample item (fields trimmed for readability):

```json
{
  "adArchiveId": "1234567890123456",
  "adLibraryUrl": "https://www.facebook.com/ads/library/?id=1234567890123456",
  "pageId": "15087023444",
  "pageName": "Nike",
  "pageUrl": "https://www.facebook.com/nike",
  "pageLikeCount": 38000000,
  "pageCategories": ["Sportswear store"],
  "isActive": true,
  "status": "active",
  "startDate": "2026-06-18T00:00:00.000Z",
  "endDate": null,
  "totalActiveTime": 2160000,
  "publisherPlatform": ["FACEBOOK", "INSTAGRAM"],
  "bodyText": "Just Do It. Shop the new Pegasus 41 — built for every run.",
  "title": "New Pegasus 41",
  "caption": "nike.com",
  "linkUrl": "https://www.nike.com/running",
  "ctaText": "Shop Now",
  "ctaType": "SHOP_NOW",
  "displayFormat": "video",
  "media": ["https://video.xx.fbcdn.net/....mp4"],
  "spendLowerBound": null,
  "spendUpperBound": null,
  "currency": null,
  "impressions": null,
  "targetedOrReachedCountries": ["US"],
  "containsSensitiveContent": false,
  "collationCount": 3,
  "searchedFor": "nike",
  "scrapedAt": "2026-07-12T09:14:00.000Z"
}
```

For **political & issue ads** (`adType: "political_and_issue_ads"`), `spendLowerBound`, `spendUpperBound`, `currency`, `impressions` and the `reach*` fields are populated where Meta discloses them.

## Integrations & automation

Because it runs on Apify, this scraper plugs into your stack without glue code:

- **Schedules** — run a daily or hourly sweep of your competitors' Pages automatically.
- **Webhooks** — trigger a downstream workflow the moment a run finishes.
- **Export destinations** — push results to **Google Sheets**, **Amazon S3**, or any HTTP endpoint from the run's dataset.
- **Zapier, Make, n8n and Pipedream** — connect the Apify integration to 6,000+ apps for alerting, Slack notifications or CRM enrichment.
- **Apify API** — poll runs and pull the dataset from any language.

## Export formats

Results can be downloaded or streamed as **CSV, JSON, JSONL, Excel (XLSX) and XML** from the Output tab or the Apify API.

## FAQ

### How do I scrape the Facebook Ad Library?
Open the **[Facebook Ad Library Scraper](https://apify.com/logiover/meta-ad-library-scraper)** on Apify, enter a keyword or an advertiser Page ID, choose a country, and run it. The scraper reads the public Ad Library and returns every matching ad as structured data — no manual scrolling.

### Is this a free Facebook Ad Library API alternative?
Yes. The official Ad Library API is limited and gated. This actor needs **no developer API key and no login**, and you can start on Apify's free tier. Pricing is pay-per-result after that.

### Do I need a Facebook account or login?
No. It reads only the public Meta Ad Library, so **no account is ever used or risked**. There is no cookie or session to supply.

### Can I get ad spend and impressions?
For **political & issue ads**, yes — set `adType` to `political_and_issue_ads` and you'll get the estimated spend range, currency, impressions text and reach where Meta publishes them. Commercial ads do not expose spend anywhere, so those fields are null for them.

### How do I scrape all ads from one advertiser?
Put the advertiser's exact **Page ID** into `pageIds` (find it in any of their ads' Ad Library URL as `view_all_page_id=`). That is more precise than a keyword and returns the Page's full ad set.

### How many ads can I collect per run?
Set `maxResults` to `0` for unlimited, or cap it (e.g. `1000`). The scraper paginates the Ad Library until it hits your cap or the results run out. Thousands of ads per search are typical for broad terms.

### Can I filter by Instagram vs Facebook, or by image vs video?
Each ad row carries `publisherPlatform`, so you can filter Facebook vs Instagram after export. Use the `mediaType` input to restrict the search itself to images, videos or memes.

### How do I export Facebook ads to Excel or CSV?
Run the actor, open the **Output** tab, and choose **Excel** or **CSV** (also JSON, JSONL and XML). Via the API, call the `run-sync-get-dataset-items` endpoint with `format=csv`.

### Why is a residential proxy required?
The Meta Ad Library serves ads based on residential IPs. Keep the default residential proxy configuration for the highest success rate — it's already set for you.

### Can I scrape housing, employment or credit ads?
Yes. Set `adType` to `housing_ads`, `employment_ads` or `credit_ads` to pull the special ad categories Meta labels for fair-advertising transparency.

## Related actors

- **[Competitor Ad Intelligence](https://apify.com/logiover/competitor-ad-intelligence)** — multi-network ad monitoring and competitive reporting.
- **[Google Ads Transparency Scraper](https://apify.com/logiover/google-ads-transparency-scraper)** — the same competitor-ad spy approach for Google's Ads Transparency Center.

---

📄 **Documentation only** — the Actor runs on the Apify platform.
▶️ **Run it:** https://apify.com/logiover/meta-ad-library-scraper

Released under the MIT License. © 2026 logiover.
