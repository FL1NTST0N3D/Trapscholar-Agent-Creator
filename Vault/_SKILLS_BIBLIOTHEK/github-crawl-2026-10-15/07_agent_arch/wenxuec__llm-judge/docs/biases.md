# Bias guide for LLM-as-judge

LLM judges are cheap and scalable but biased. Every bias below has been documented in the
literature (Zheng 2023, Liu 2023, and follow-ups). Design the judge prompt to neutralise
the biases that matter for your eval, and check for them during calibration.

## The biases

### Position bias
In pairwise comparisons, judges prefer whichever candidate appears first (or sometimes
second — direction varies by model). Observed across GPT-4, Claude, and Gemini.

**Mitigation**
- Randomise order per example.
- Run each pair twice in swapped order and only count agreement.
- Prefer pointwise scoring over pairwise when possible.

### Verbosity / length bias
Judges systematically rate longer outputs higher, even when the extra content is
redundant or wrong. Worse on conversational benchmarks than on factual ones.

**Mitigation**
- Explicitly instruct the judge: "Do not reward longer outputs."
- Cap output length of the system under test when comparing.
- In pairwise, normalise or report length alongside the verdict.
- Calibrate on examples where the shorter response is correct.

### Self-preference (self-enhancement) bias
A judge from model family X tends to rate outputs from family X higher. Especially strong
when the judge is the same model as the generator.

**Mitigation**
- Never judge outputs with the same model that generated them when comparing to another
  model.
- For high-stakes evals, use an ensemble of judges from different families.
- Do not reveal author identity in the judge prompt.

### Halo / aesthetic bias
Judges reward polished formatting (bullet lists, bold, headers) regardless of content
quality. Related to verbosity bias but distinct.

**Mitigation**
- Strip formatting or normalise it before judging when content — not presentation — is
  the target.
- Anchor the rubric on substance, not style (unless style is the criterion).

### Anchoring / framing bias
Judges can be swung by the order and wording of scale anchors. Presenting "pass" first
makes pass more likely; starting with "fail" makes fail more likely.

**Mitigation**
- Use consistent anchor wording across judges.
- Always anchor with concrete examples for each point on the scale, not adjectives alone
  ("good", "bad", "excellent" are not anchors).
- Re-run calibration after any prompt edit.

### Chain-of-thought / ordering effect
If the judge writes the score before the rationale, the rationale rationalises the score.
If it writes the rationale first, the score is better calibrated.

**Mitigation** (G-Eval pattern)
- Force JSON output with `rationale` before `score`.
- Also require the judge to cite specific evidence (quotes, step numbers).

### Refusal / uncertainty bias
Judges over-assign middle scores ("partial") when uncertain rather than reading the
trajectory carefully. Produces mushy metrics.

**Mitigation**
- Force binary where possible for safety-critical criteria.
- Make partial credit require a specific rationale (e.g. "partial only if exactly one of
  A or B holds").
- Track the rate of `ambiguous: true` — if it is above ~10%, the rubric is underspecified.

### Distraction bias
Irrelevant context (system prompts, boilerplate, irrelevant tool results) drags judges
toward average scores.

**Mitigation**
- Pre-filter the trajectory you feed the judge. Include only what is necessary to score
  the criterion.
- For step-level judges, feed only the relevant step plus minimal context.

### Sycophancy on the reference
If you give the judge a reference answer and tell it the reference is correct, the judge
over-penalises any deviation, even improvements.

**Mitigation**
- Phrase the reference as "one acceptable answer" rather than "the correct answer".
- Allow the judge to flag cases where the output is better than the reference.

## Which biases matter for which evals

| Eval type                          | Top bias risks                                   |
|------------------------------------|---------------------------------------------------|
| Pairwise preference (A vs B)       | position, self-preference, verbosity             |
| Pointwise quality on a Likert      | anchoring, verbosity, halo                       |
| Agent tool-use correctness         | distraction, refusal (middle-score cop-out)      |
| Safety / compliance (binary)       | refusal, sycophancy                              |
| Factuality vs reference            | sycophancy on reference                          |
| RAG groundedness                   | distraction (long retrieved passages)            |

## Detecting bias during calibration

During Phase 5 of the skill, you already compute human agreement per criterion. Also
check:

1. **Length correlation**: correlate judge score with output length. Significant positive
   correlation = verbosity bias.
2. **Position shuffle test** (pairwise): run the same pair in swapped order. Agreement
   rate should be high; otherwise position bias is active.
3. **Self-preference test**: judge outputs from two models, one the same family as the
   judge. Look for systematic preference.
4. **Middle-score rate**: in 3- or 5-point scales, what fraction of scores are the
   middle? If >50%, you have refusal bias or underspecified anchors.

## References

- Zheng, L. et al. "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena." NeurIPS 2023.
- Liu, Y. et al. "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment." EMNLP
  2023.
- Wang, P. et al. "Large Language Models are not Fair Evaluators." 2023.
- Dubois, Y. et al. "Length-Controlled AlpacaEval." 2024.
