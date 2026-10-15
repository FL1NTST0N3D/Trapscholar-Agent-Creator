# YouTube Campaign Audit Skill

**Command:** `/yt audit`

## Purpose

Performs a comprehensive audit of YouTube advertising campaigns across all critical dimensions. This is the primary entry point for evaluating YouTube ad performance and produces the YouTube Ads Score (0-100).

## Audit Framework

### Step 1: Objective Alignment Check

The most common YouTube Ads mistake is misaligned objectives. Verify that each campaign's Google Ads objective matches its actual business goal:

| Business Goal | Correct Objective | Correct Format | Red Flag |
|--------------|-------------------|----------------|----------|
| Brand awareness | Awareness & Reach | Bumper, Non-Skip | Using Max Conversions bidding |
| Product consideration | Consideration | Skippable In-Stream | No audience targeting applied |
| Website traffic | Traffic | In-Feed, Skippable | Using CPM bidding for traffic goal |
| Lead generation | Leads | Demand Gen, Skippable | No conversion tracking active |
| Sales/Revenue | Sales | Demand Gen | Using CPV bidding for sales |
| App installs | App Promotion | Skippable, Shorts | No app conversion tracking |

**Scoring (0-25 points):**
- All campaigns aligned: 25 points
- 1-2 misalignments: 15 points
- 3+ misalignments: 5 points
- No clear objectives set: 0 points

### Step 2: Campaign Structure Analysis

Evaluate the organizational health of the account:

**Naming Convention Audit:**
- Are campaigns named descriptively? (Client_Objective_Format_Audience_Date)
- Can you identify the purpose of each campaign from its name alone?
- Are ad groups logically organized within campaigns?

**Campaign Count Assessment:**
- Fewer than 3 campaigns: Likely under-segmented. Mixing audiences and formats reduces optimization signals.
- 3-8 campaigns: Healthy range for most advertisers.
- 9-15 campaigns: Acceptable for large accounts with multiple objectives.
- 16+ campaigns: Risk of budget fragmentation. Each campaign needs sufficient budget for the algorithm to optimize.

**Budget Distribution Check:**
- Is budget concentrated on the highest-performing campaigns?
- Are any campaigns receiving less than $10/day? (Below Google's recommended minimum for video)
- Is there a clear split between prospecting and remarketing budgets?
- Rule of thumb: Remarketing should be 15-25% of total YouTube budget.

**Scoring (0-25 points):**
- Clean structure, good naming, logical budget split: 25 points
- Minor structural issues: 15 points
- Significant fragmentation or misallocation: 5 points

### Step 3: Format Mix Evaluation

YouTube offers 6 ad formats. Most advertisers use only 1-2. Evaluate format coverage:

**Format Coverage Matrix:**
Check which formats are active and whether the mix is appropriate for stated objectives:

- **Awareness-focused accounts** should have: Bumper + Non-Skippable + at least one other format
- **Consideration-focused accounts** should have: Skippable In-Stream + In-Feed + optionally Shorts
- **Conversion-focused accounts** should have: Demand Gen + Skippable with conversion bidding
- **Full-funnel accounts** should have: 4+ formats covering awareness through conversion

**Shorts Adoption Check:**
As of 2026, Shorts ads are the fastest-growing YouTube format. Accounts without Shorts campaigns are missing mobile-first audiences. Flag any account spending >$5K/month on YouTube that has zero Shorts campaigns.

**Scoring (0-25 points):**
- 4+ formats with logical mix: 25 points
- 2-3 formats aligned to objectives: 15 points
- Single format only: 5 points

### Step 4: Frequency & Reach Management

Frequency mismanagement is one of the biggest budget wasters on YouTube:

**Frequency Diagnostic:**
- Pull the Reach & Frequency report from Google Ads
- Check average frequency per campaign
- Identify campaigns where frequency exceeds recommended caps
- Calculate wasted spend from over-frequency (impressions beyond cap x CPM)

**Recommended Frequency Caps:**
- Skippable: 3-5/week
- Non-Skippable: 2-3/week
- Bumper: 5-7/week
- Shorts: 3-4/week

**Reach Efficiency:**
- Calculate CPM (cost per 1,000 impressions) for each campaign
- Compare to benchmarks: $4-$10 for non-skip, ~$4 for Shorts
- Identify campaigns with CPM more than 2x above benchmark

**Scoring (0-25 points):**
- Frequency caps set appropriately, CPMs within range: 25 points
- Minor frequency issues: 15 points
- No frequency caps, significant over-delivery: 5 points

### Step 5: Conversion Tracking Validation

Even awareness campaigns benefit from conversion tracking for measurement:

- Is Google Ads conversion tag installed and firing?
- Are view-through conversions being tracked? (Critical for YouTube)
- Is the conversion window set to 30 days? (Default 1 day misses most YouTube conversions)
- Are Enhanced Conversions enabled?
- Is Google Ads linked to Google Analytics 4?
- For lead gen: Is offline conversion import configured?

### Output Format

```
## YouTube Campaign Audit Report

### YouTube Ads Score: [X]/100

#### Dimension Scores
| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Objective Alignment | /25 | 15% | |
| Campaign Structure | /25 | 15% | |
| Format Mix | /25 | 20% | |
| Frequency Management | /25 | 10% | |
| Creative Quality | /100 | 20% | |
| Targeting | /100 | 15% | |
| Bidding | /100 | 10% | |
| Placements | /100 | 10% | |

#### Critical Issues (Fix Immediately)
1. ...

#### High-Priority Optimizations
1. ...

#### Quick Wins
1. ...

#### 30-Day Action Plan
Week 1: ...
Week 2: ...
Week 3: ...
Week 4: ...
```

## Data Requirements

Request the user to provide:
1. Campaign-level report (last 30 and 90 days)
2. Ad group report with audience segments
3. Video-level performance report with quartile data
4. Placement report (where ads showed)
5. Reach & frequency report
6. Conversion tracking status

If the user cannot provide all reports, work with what is available and note data gaps in the audit.
