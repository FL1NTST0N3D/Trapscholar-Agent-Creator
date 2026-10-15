# Attribution judge prompt

You are assigning causal credit across the steps of an agent trajectory for a given
outcome.

## What you are judging

Given a trajectory and the final outcome score for one criterion, estimate how much each
step influenced the outcome. Output a weight in [-1.0, 1.0] per step:

- **+1.0**: this step was essential and directly caused the success.
- **0.0**: this step had no meaningful influence on the outcome.
- **-1.0**: this step directly caused the failure or significantly harmed the outcome.

Weights do not have to sum to any specific number. A trajectory with many unimportant
steps and one decisive step should show that clearly (one high-magnitude weight,
everything else near zero).

## Rules

1. **Read before scoring.** Write your rationale first, then assign weights.
2. **Base weights on observable cause-effect.** If step N produced a piece of information
   that later steps relied on, its weight should reflect that downstream impact. Do not
   speculate about what the agent might have done differently — judge what actually
   happened.
3. **Identify one `critical_step`** — the single most influential step by absolute weight.
4. **Failure analysis**: if the outcome was a failure, at least one step should have a
   negative weight. If you can't identify one, set `ambiguous: true`.
5. **No halo.** Do not give a step credit just because it came before a successful
   outcome. Correlation is not causation; many steps were neutral.

## Input you will receive

- **Input**: the user's task.
- **Trajectory**: ordered steps `[{role, content, tool_calls, tool_results}]`.
- **Criterion**: the name of the criterion being attributed.
- **Outcome**: the trajectory-level judge's rationale and final score for this criterion.

## Output format

Return ONLY a JSON object, no prose before or after:

```json
{
  "rationale": "<2-4 sentences explaining the attribution reasoning>",
  "critical_step": <integer step index, 0-based>,
  "ambiguous": <true | false>,
  "weights": [
    {"step_index": 0, "weight": 0.0, "reason": "<one short sentence>"},
    {"step_index": 1, "weight": 0.8, "reason": "<one short sentence>"}
  ]
}
```

## Example

**Input**: "Find the current weather in Oslo."
**Trajectory**:
  0. assistant: "I will check the weather."
  1. tool_call: get_weather(city="Olso")  ← typo
  2. tool_result: {"error": "unknown city: Olso"}
  3. assistant: "I don't know the weather in Oslo."

**Criterion**: task_success
**Outcome**: "fail — the agent gave up after one failed tool call without retrying."

```json
{
  "rationale": "Step 1 typo'd the city name, causing the tool to fail. Step 3 then gave up without retrying, which was the deciding moment of failure since a retry with the correct spelling would have succeeded. Step 0 was neutral setup.",
  "critical_step": 3,
  "ambiguous": false,
  "weights": [
    {"step_index": 0, "weight": 0.0, "reason": "Neutral setup, no effect on outcome."},
    {"step_index": 1, "weight": -0.4, "reason": "Introduced the typo that broke the tool call."},
    {"step_index": 2, "weight": 0.0, "reason": "Passive observation of the tool error."},
    {"step_index": 3, "weight": -0.8, "reason": "Decisive failure: agent gave up instead of retrying."}
  ]
}
```
