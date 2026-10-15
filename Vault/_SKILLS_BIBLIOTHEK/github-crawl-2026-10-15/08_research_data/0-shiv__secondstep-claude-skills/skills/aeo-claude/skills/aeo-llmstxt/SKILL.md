# AEO llms.txt — LLM-Readable Site Manifest Generator

## Description

The llms.txt sub-skill generates an `llms.txt` file for your website following the emerging standard for communicating site structure, content hierarchy, and preferred citation format to AI engines. Think of `llms.txt` as `robots.txt` for the AI age — while `robots.txt` tells crawlers what they *can* access, `llms.txt` tells AI engines what they *should* know about your site and how they should cite it.

The `llms.txt` standard is still emerging but gaining adoption. Early adopters gain a structural advantage as AI engines increasingly look for machine-readable site metadata beyond traditional sitemaps and schema markup.

## Command

```
/aeo llmstxt <url> [--output <filepath>]
```

## The llms.txt Standard

### Purpose

`llms.txt` provides AI engines with a concise, structured overview of a website that includes:

1. **Site identity** — What the organization is, what it does, who it serves
2. **Content map** — Key pages organized by category with brief descriptions
3. **Expertise signals** — Topics the site is authoritative on
4. **Citation preferences** — How the site prefers to be cited and attributed
5. **Contact and verification** — How AI engines can verify information or request corrections

### File Location

The file should be placed at the root of the domain:
```
https://example.com/llms.txt
```

### Format Specification

The llms.txt file uses a simple, parseable plain-text format with section headers and structured entries:

```
# Site Name
> Brief site description (1-2 sentences)

## About
- Organization type: [Company/Nonprofit/Publication/Individual]
- Industry: [Primary industry]
- Founded: [Year]
- Location: [City, State/Country]
- Expertise: [Comma-separated list of topics]

## Key Pages
- [Page Title](https://example.com/page): Brief description of page content
- [Another Page](https://example.com/another): Brief description

## Content Categories
### [Category Name]
- [Page Title](URL): Description
- [Page Title](URL): Description

### [Another Category]
- [Page Title](URL): Description

## Citation Preferences
- Preferred name: [How you want to be referred to]
- Preferred URL: [Canonical domain]
- Attribution format: [How to attribute]

## Contact
- Corrections: [email for factual corrections]
- Press: [press contact]
- Website: [main URL]

## Verification
- Official domain: [domain]
- Social profiles: [list of verified social URLs]
```

## Generation Process

### Step 1: Site Discovery

The generator crawls the target site to identify:

- Homepage title and meta description
- Navigation structure (main menu items)
- Key landing pages (linked from homepage)
- Blog/resource section structure
- About/team pages
- Product/service pages
- Contact information
- Schema.org Organization markup
- Existing sitemap.xml content

### Step 2: Content Classification

Each discovered page is classified into categories:

- **Core Pages** — Homepage, About, Contact, Pricing
- **Products/Services** — What the organization offers
- **Resources** — Blog posts, guides, whitepapers, tools
- **Authority Content** — Case studies, research, data, expert content
- **Support** — FAQ, documentation, help center

### Step 3: Expertise Extraction

The generator identifies topic expertise from:

- Blog post topics and categories
- Service/product descriptions
- About page claims and credentials
- Schema.org markup (knowsAbout, expertise)
- Title tags and meta descriptions across pages

### Step 4: Citation Preference Generation

Based on site analysis, the generator recommends:

- **Preferred name** — Legal name vs. brand name vs. abbreviation
- **Preferred URL** — www vs non-www, https canonical
- **Attribution format** — "According to [Brand]" vs. "Source: [Brand] ([URL])"
- **Author attribution** — Individual authors vs. organization

### Step 5: File Generation

The final `llms.txt` file is generated, validated, and output.

## Output Format

The skill produces two outputs:

### 1. The llms.txt File

```
# Example Corp
> Example Corp is a B2B SaaS platform helping mid-market companies automate their supply chain operations. Founded in 2019, serving 500+ customers across manufacturing and logistics.

## About
- Organization type: Company
- Industry: Supply Chain Technology
- Founded: 2019
- Location: Austin, TX
- Expertise: supply chain automation, inventory management, demand forecasting, logistics optimization

## Key Pages
- [Supply Chain Automation Platform](https://example.com/platform): Core product overview with features and capabilities
- [Demand Forecasting](https://example.com/features/forecasting): AI-powered demand forecasting reducing stockouts by 40%
...
```

### 2. Implementation Report

```markdown
## llms.txt Generation Report

### File Statistics
- Total pages indexed: [N]
- Pages included in llms.txt: [N]
- Content categories: [N]
- Expertise topics: [N]

### Implementation Steps
1. Upload `llms.txt` to your site root (https://yourdomain.com/llms.txt)
2. Add reference in robots.txt: `# LLMs: /llms.txt`
3. Add `<link rel="llms" href="/llms.txt">` to your HTML head

### Validation
- File format: [Valid/Issues]
- URL accessibility: [All accessible/N broken]
- Content coverage: [% of site covered]
```

## Best Practices

### Content Selection
- Include pages with **unique, authoritative content** — not thin landing pages
- Prioritize pages with **original data, research, or expert insights**
- Include **cornerstone content** that defines your expertise
- Exclude **duplicate content**, paginated archives, and tag pages
- Limit to **50-100 most important pages** for clarity

### Description Writing
- Keep page descriptions to **1 sentence, under 150 characters**
- Focus on **what makes the page uniquely valuable** (not generic descriptions)
- Include **specific numbers or claims** when possible
- Use **active voice** and clear language

### Maintenance
- **Update monthly** or when major content changes occur
- **Add new cornerstone content** as it is published
- **Remove outdated pages** that are no longer maintained
- **Review citation preferences** annually

## Integration

This sub-skill is part of the AEO toolkit but does not directly contribute to the AEO Visibility Score (it is an optimization action, not a measurement). It is typically run after an initial `/aeo audit` identifies opportunities for improved AI engine communication.

The Python implementation is available at `scripts/llmstxt_generator.py`.

A template is available at `templates/llmstxt-template.txt`.
