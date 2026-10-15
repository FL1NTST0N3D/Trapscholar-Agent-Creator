# Quality Score Fundamentals

## What Is Quality Score?

Quality Score is Google Ads' 1-10 rating of the combined quality and relevance of your keywords, ads, and landing pages. It is calculated at the keyword level.

Quality Score directly affects:
- **Ad Rank** — Higher QS = higher position at the same bid
- **CPC** — Higher QS = lower cost per click
- **Eligibility** — Very low QS can prevent ads from showing at all
- **Ad extensions** — QS affects whether extensions are shown

## Visible QS vs Auction-Time QS

There are two types of Quality Score:

### Visible QS (What You See in Google Ads)
- Updated periodically (not real-time)
- Based on historical performance
- Uses aggregate data across all auctions
- Rounded to an integer 1-10
- This is what you export, track, and optimize against

### Auction-Time QS (What Google Actually Uses)
- Calculated in real-time for every auction
- Considers: user's exact query, device, location, time of day, audience signals
- Granular (not rounded to integers)
- You never see this number directly
- Can differ significantly from visible QS for any given auction

The visible QS is your best proxy for understanding auction-time QS, but they are not identical.

## The Three Components

### Expected Click-Through Rate (~39% weight)
Google's prediction of how likely your ad is to be clicked, normalized for position. Compared against other advertisers on the same keyword.

### Landing Page Experience (~39% weight)
How relevant, useful, and easy to navigate your landing page is. Based on algorithmic analysis and user behavior signals.

### Ad Relevance (~22% weight)
How closely your ad copy matches the keyword and the user's search intent.

## How QS Affects CPC

The relationship between QS and CPC follows an approximate curve:

```
Actual CPC = Ad Rank of next advertiser / Your QS + $0.01
```

Because QS is a divisor, higher QS directly reduces CPC. The empirical relationship:

- QS 10: ~50% less than QS 7 baseline
- QS 7: baseline
- QS 5: ~67% more than baseline
- QS 3: ~200% more than baseline
- QS 1: ~400% more than baseline

## Common Myths

### Myth: QS only matters for position
**Reality:** QS directly affects CPC. Even if you always win top position, higher QS means paying less for it.

### Myth: QS is just about putting keywords in ads
**Reality:** Ad Relevance (keyword-ad alignment) is only ~22% of QS. Landing Page Experience and Expected CTR each contribute ~39%.

### Myth: You should optimize every keyword to QS 10
**Reality:** Some keywords (competitor terms, broad informational queries) have structurally lower QS. Focus optimization effort where the dollar impact justifies it.

### Myth: QS updates instantly
**Reality:** Visible QS updates lag behind changes by 2-4 weeks. Patience is required.

### Myth: Pausing a keyword resets its QS
**Reality:** Google retains QS history. However, creating a new keyword in a new ad group can sometimes provide a fresh start.

## QS and Impression Share

Quality Score also affects impression share. Keywords with very low QS (1-3) may be "rarely shown due to low Quality Score." This means Google is throttling your impressions because it predicts poor performance. Improving QS can unlock additional impression volume.

## Account-Level QS

Google has stated that there is an account-level quality signal that affects new keywords. Accounts with historically high QS across many keywords may see new keywords start at higher QS than accounts with poor history. This is another reason to clean up low-QS keywords — they drag down the account-level signal.
