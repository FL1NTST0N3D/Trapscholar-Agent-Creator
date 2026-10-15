# Schema: HowTo

Generate HowTo schema markup in JSON-LD format. This schema structures step-by-step instructions with tools, supplies, time estimates, and costs for search engine comprehension and rich result eligibility on non-Google search engines.

## Command

`/schema howto`

## When to Use

HowTo schema is appropriate for any content that provides step-by-step instructions for completing a task. This includes tutorials, DIY guides, repair instructions, recipes (though Recipe schema is preferred for food), craft projects, setup guides, and any other instructional content. The content must describe a sequence of steps that leads to a completed outcome.

## Important: 2023 Google Restrictions

In September 2023, Google removed HowTo rich results from Google Search entirely. Key implications:

- **HowTo rich results no longer appear in Google Search** for any site, regardless of schema quality.
- The schema itself remains valid Schema.org vocabulary.
- **Bing may still display HowTo rich results.**
- AI systems (ChatGPT, Perplexity, Claude, Google Gemini) use HowTo schema to understand instructional content and generate step-by-step answers.
- Google may re-introduce HowTo rich results in the future, so maintaining the schema is prudent.

**Recommendation**: Still implement HowTo schema for Bing, AI engine comprehension, content structure, and future-proofing. Do not promise clients HowTo rich results in Google.

## Required Properties

- `@type`: "HowTo"
- `name`: Title of the how-to guide
- `step`: Array of HowToStep objects

### For each HowToStep:
- `@type`: "HowToStep"
- `name`: Short title of the step (optional but recommended)
- `text`: Full description of what to do in this step
- `url`: URL pointing to the step's anchor on the page (e.g., "https://example.com/guide#step-1")
- `image`: Image showing the step (recommended for visual guides)

## Recommended Properties

- `description`: Overview of what the how-to accomplishes
- `totalTime`: ISO 8601 duration for total time to complete (e.g., "PT30M" for 30 minutes, "PT2H" for 2 hours)
- `estimatedCost`: MonetaryAmount with `value` and `currency`
- `supply`: Array of HowToSupply objects (materials consumed during the task)
- `tool`: Array of HowToTool objects (instruments used but not consumed)
- `image`: Main image for the how-to
- `video`: VideoObject showing the process
- `yield`: What the completed how-to produces (e.g., "1 wooden bookshelf")
- `performTime`: Time spent actively working (vs waiting time)
- `prepTime`: Time for preparation before starting

### HowToSupply:
```json
{
  "@type": "HowToSupply",
  "name": "Wood screws, 2 inch",
  "requiredQuantity": "16",
  "estimatedCost": { "@type": "MonetaryAmount", "value": "5.99", "currency": "USD" }
}
```

### HowToTool:
```json
{
  "@type": "HowToTool",
  "name": "Phillips head screwdriver"
}
```

## Step Structure Options

HowTo supports two levels of step organization:

### Simple Steps (most common):
```json
"step": [
  { "@type": "HowToStep", "name": "Step 1", "text": "Do this first..." },
  { "@type": "HowToStep", "name": "Step 2", "text": "Then do this..." }
]
```

### Sections with Sub-Steps (for complex guides):
```json
"step": [
  {
    "@type": "HowToSection",
    "name": "Preparation",
    "itemListElement": [
      { "@type": "HowToStep", "text": "Gather materials..." },
      { "@type": "HowToStep", "text": "Clear workspace..." }
    ]
  },
  {
    "@type": "HowToSection",
    "name": "Assembly",
    "itemListElement": [
      { "@type": "HowToStep", "text": "Attach base..." },
      { "@type": "HowToStep", "text": "Secure shelves..." }
    ]
  }
]
```

## Time Formatting (ISO 8601 Duration)

- 30 minutes: `PT30M`
- 1 hour: `PT1H`
- 1 hour 30 minutes: `PT1H30M`
- 2 days: `P2D`
- 1 day 4 hours: `P1DT4H`

Always ask the user for time estimates and convert to ISO 8601 format.

## Common Mistakes

- **Missing step text**: Every HowToStep must have a `text` property with the full instruction.
- **Too vague steps**: Each step should describe a specific, actionable task. "Continue working" is too vague.
- **Using HowTo for non-instructional content**: HowTo is for step-by-step guides, not general informational content.
- **Confusing supply vs tool**: Supplies are consumed (paint, nails, ingredients). Tools are used but not consumed (hammer, drill, oven).
- **Missing time estimates**: `totalTime` is strongly recommended. Users want to know how long a task takes before starting.
- **Expecting Google rich results**: HowTo rich results were removed from Google Search in September 2023.

## Combining with Other Schema

HowTo commonly combines with:
- **Article + HowTo**: Tutorial blog post with structured steps
- **VideoObject + HowTo**: Video tutorial with step-by-step schema overlay
- **FAQPage + HowTo**: Guide with step-by-step instructions and related Q&A section

## Google Rich Result Eligibility

- **Pre-September 2023**: Sites with valid HowTo schema could get step-by-step rich results with expandable steps, images, and time estimates
- **Post-September 2023**: HowTo rich results completely removed from Google Search
- **Bing**: May still display HowTo rich results
- **AI engines**: HowTo schema helps AI systems understand and reproduce instructional content accurately
