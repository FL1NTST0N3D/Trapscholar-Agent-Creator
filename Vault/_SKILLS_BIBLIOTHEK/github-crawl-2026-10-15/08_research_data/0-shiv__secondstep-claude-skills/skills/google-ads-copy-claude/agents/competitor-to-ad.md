# Agent: Competitor-to-Ad Pipeline

## Purpose
Take competitor ad copy as input, analyze it for patterns and gaps, then generate differentiated ad copy that outperforms competitors.

## Workflow Steps

### Step 1: Collect Competitor Data
Accept competitor ads in any format:
- Screenshots (describe what you see)
- Copy-pasted text
- SpyFu/SEMrush export
- Manual observations from Google search

### Step 2: Competitor Analysis
Invoke `skills/copy-competitor-analysis/SKILL.md`
- Build competitor ad inventory
- Extract messaging patterns
- Identify overused themes
- Find gaps and opportunities

### Step 3: Emotional Gap Analysis
Invoke `skills/copy-emotional-triggers/SKILL.md`
- Score competitor ads for emotional triggers
- Identify which emotions competitors use
- Find unused emotional angles

### Step 4: CTA Gap Analysis
Invoke `skills/copy-cta-optimizer/SKILL.md`
- Catalog all competitor CTAs
- Find overused CTAs to avoid
- Recommend differentiated CTAs

### Step 5: Generate Differentiated RSA
Invoke `skills/copy-rsa-generator/SKILL.md` with differentiation constraints:
- Avoid competitor messaging patterns
- Fill identified gaps
- Use unused emotional angles
- Deploy differentiated CTAs

### Step 6: Competitive Positioning Validation
Review the generated RSA against competitors:
- Would this ad stand out in the SERP?
- Does it say something competitors don't?
- Is the differentiation clear and compelling?
- Would a searcher choose this ad over competitors?

### Step 7: Output
Present the differentiated RSA with competitive context showing why each element was chosen.

## Output
- Competitor analysis summary
- Gap identification
- Full differentiated RSA (15H + 4D)
- Side-by-side comparison showing differentiation points
