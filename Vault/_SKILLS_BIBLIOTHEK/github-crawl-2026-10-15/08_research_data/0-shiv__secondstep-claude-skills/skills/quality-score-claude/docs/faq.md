# Frequently Asked Questions

## General

### How accurate are the CPC savings estimates?
The estimates are directionally accurate based on industry-standard QS-to-CPC multipliers. Actual savings vary by auction dynamics, competition, and keyword. We recommend using the "realistic" estimate (not theoretical maximum) for planning purposes. See [CPC Impact Methodology](./cpc-impact-methodology.md) for details.

### How long does it take for QS changes to appear?
Visible Quality Score typically updates 2-4 weeks after changes are made. CPC impact may lag further behind. Plan for 4-8 weeks to see measurable CPC reductions after implementing fixes.

### Should I optimize every keyword to QS 10?
No. Focus on keywords where the dollar impact justifies the effort. A QS 6 keyword spending $50/month is not worth the same optimization effort as a QS 4 keyword spending $5,000/month. Some keyword categories (competitor terms, broad informational queries) have structurally lower QS that may not be worth fighting.

### Does QS matter for Performance Max campaigns?
Performance Max does not surface keyword-level QS data. However, the underlying quality signals (ad relevance, landing page experience, CTR) still affect auction outcomes. The QS analysis in this tool applies to Search campaigns with keyword-level data.

### What about Display and Video campaigns?
Quality Score in Google Ads is primarily a Search concept. Display and Video campaigns have their own quality signals, but they are not surfaced as the same 1-10 QS metric.

## Data

### What columns do I need in my CSV export?
At minimum: Keyword, Quality Score, Cost (or Clicks + Avg CPC). For full analysis, include all QS component columns (Expected CTR, Ad Relevance, Landing Page Experience), plus Impressions, CTR, Conversions, Final URL, Campaign, and Ad Group.

### How do I export QS component data from Google Ads?
In Google Ads, go to Keywords > Search keywords > Columns > Modify columns > Quality Score section. Add: Quality Score, Exp. CTR, Ad relevance, Landing page exp. Then download as CSV.

### What if some keywords show "--" for Quality Score?
This means the keyword does not have enough impression data for Google to calculate QS (typically needs 1,000+ impressions). These keywords are excluded from the analysis. They will receive QS once they accumulate sufficient data.

### Can I use Google Ads API data instead of CSV?
Yes. The Python scripts accept CSV format, but the data can come from any source. If using the API, format the output as CSV with the expected column headers.

## Optimization

### Which QS component should I fix first?
Generally: Landing Page Experience first (fixes affect multiple keywords), then Ad Group Restructuring (improves Ad Relevance), then Ad Copy (improves Expected CTR). But prioritize by dollar impact, not component type.

### Should I use Single Keyword Ad Groups (SKAGs)?
SKAGs maximize Ad Relevance but create management overhead and split data. We recommend Single Theme Ad Groups (STAGs) with 3-8 tightly related keywords as the best balance of relevance and manageability.

### Will pausing low-QS keywords help my account?
Pausing keywords does not directly improve other keywords' QS. However, there is evidence that account-level quality signals exist, so removing consistently poor performers may have a modest positive effect on new keywords.

### How do I fix "Below Average" Landing Page Experience?
Check: page speed (LCP < 2.5s), mobile responsiveness, content relevance to the keyword, easy navigation, trust signals (contact info, reviews, privacy policy), and original content. Page speed is often the biggest quick win.

### How do I fix "Below Average" Expected CTR?
Check: ad copy quality (compelling headlines), ad extensions (sitelinks, callouts), match type bleed (broad match triggering irrelevant queries), and ad fatigue (same ads running too long). Adding negative keywords to eliminate low-CTR impressions is often the fastest fix.

## Scripts

### How do I run the Python scripts?
```bash
python scripts/qs_analyzer.py your_data.csv
python scripts/cpc_impact_calculator.py your_data.csv
python scripts/qs_distribution.py your_data.csv
python scripts/generate_qs_report.py your_data.csv --account-name "Client Name"
```

### Do the scripts require any Python packages?
No. All scripts use Python standard library only (csv, json, argparse, pathlib, collections, dataclasses). No pip install needed.

### Can I automate QS tracking?
Yes. Set up a weekly cron job or Google Ads Script to export keyword QS data. Then use `qs_analyzer.py --compare previous.csv` to track changes over time.
