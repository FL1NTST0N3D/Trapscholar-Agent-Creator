# Agent: Bulk Ad Generator

## Purpose
Generate RSAs for multiple ad groups at scale. Takes a list of ad groups with their keywords and produces a unique RSA for each, maintaining consistency across the campaign while varying messaging per ad group.

## Workflow Steps

### Step 1: Collect Campaign Context
- Business name, industry, USPs (applies to ALL ad groups)
- Landing page structure (different pages per ad group?)
- Brand voice and tone guidelines
- Any offers or promotions running

### Step 2: Collect Ad Group List
Accept input as a list or CSV:
```
Ad Group Name | Primary Keyword | Secondary Keywords | Specific Landing Page
-------------|----------------|-------------------|---------------------
Plumbing     | plumber        | plumbing service  | /plumbing
HVAC         | hvac repair    | ac repair, heating| /hvac
Electrical   | electrician    | electrical repair | /electrical
```

### Step 3: Generate Per Ad Group
For each ad group, invoke `skills/copy-rsa-generator/SKILL.md` with:
- The ad group's specific keywords
- Business-level USPs adapted to the service category
- Display paths matching the ad group's landing page

### Step 4: Cross-Ad-Group Consistency Check
Ensure:
- Brand name headline is consistent across all RSAs
- Guarantee/trust headlines are consistent
- Offer headlines match (same promotion across ad groups)
- CTA style is consistent (all use "Get a Free Quote" not mixed "Get Quote" / "Request Quote" / "Free Estimate")

### Step 5: Cross-Ad-Group Uniqueness Check
Ensure:
- Each RSA has at least 5 headlines unique to that ad group
- Service-specific benefits are highlighted (not generic)
- Keywords are properly integrated per ad group

### Step 6: Output
Present all RSAs in a structured format, ready for bulk upload to Google Ads Editor.

## Output Format
```
=== BULK RSA OUTPUT ===
Campaign: [name]
Total Ad Groups: [count]
Generated: [date]

--- AD GROUP 1: [Name] ---
[Full RSA with 15 headlines + 4 descriptions]

--- AD GROUP 2: [Name] ---
[Full RSA]

[Continue for all ad groups]

--- GOOGLE ADS EDITOR IMPORT FORMAT ---
[CSV-formatted output for direct import]
```

## Google Ads Editor CSV Format
```csv
Campaign,Ad Group,Headline 1,Headline 2,...,Headline 15,Description 1,...,Description 4,Path 1,Path 2,Final URL
```
