# Agent: Full RSA Workflow

## Purpose
End-to-end RSA creation workflow that chains multiple skills together for a complete, optimized ad.

## Workflow Steps

### Step 1: Gather Requirements
Collect all inputs from the user:
- Business name, product/service
- Primary and secondary keywords
- USPs (at least 3)
- Current offer or promotion
- Target audience
- Location (if local)
- Campaign goal (leads, sales, calls)
- Landing page URL (if available)

### Step 2: Generate Base RSA
Invoke `skills/copy-rsa-generator/SKILL.md`
- Generate 15 headlines + 4 descriptions
- Tag each with framework and character count
- Include pin recommendations

### Step 3: Headline Enhancement
Invoke `skills/copy-headline-formulas/SKILL.md`
- Generate 10 additional headline alternatives using formulas not yet used
- Replace any weak headlines from Step 2
- Ensure all 6 headline categories are covered

### Step 4: Emotional Scoring
Invoke `skills/copy-emotional-triggers/SKILL.md`
- Score every headline and description for emotional impact
- Identify headlines below 4/10 emotional score
- Replace flat headlines with emotionally charged alternatives
- Ensure emotion mix matches industry best practices

### Step 5: CTA Optimization
Invoke `skills/copy-cta-optimizer/SKILL.md`
- Audit all CTAs across headlines and descriptions
- Ensure CTA diversity (minimum 3 different CTAs)
- Replace generic CTAs with industry-specific high-performers
- Align CTAs with funnel stage and device mix

### Step 6: Ad Strength Audit
Invoke `skills/copy-ad-strength/SKILL.md`
- Score across all 5 pillars
- Fix any issues preventing "Excellent" rating
- Verify keyword inclusion, uniqueness, and variety

### Step 7: Final Output
Invoke `skills/copy-report/SKILL.md` (abbreviated version)
- Present scorecard
- Present final RSA in copy-paste-ready format
- Include display paths
- Recommend A/B test variant for future testing

## Expected Duration
Full workflow: 3-5 minutes with user input time.

## Output
A complete, "Excellent" Ad Strength RSA with:
- 15 unique headlines (30 chars each)
- 4 optimized descriptions (90 chars each)
- Display paths
- Pin recommendations
- Emotional score per headline
- Framework tags
- Predicted Ad Strength: Excellent
