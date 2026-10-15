"""
LLM-as-judge evaluation harness.

Framework-agnostic: uses only the anthropic SDK (or openai if you swap the client).
Reads a dataset, runs the system-under-test, then runs each judge prompt against the
result, and writes structured JSON output you can diff across runs.

Features:
  - Per-criterion judge scoring (pointwise).
  - Step attribution (blame-mode by default; counterfactual available).
  - Incremental re-eval: examples already judged against the current rubric are skipped.
    Adding a new example to the dataset only runs the pipeline for that example.

Customise the four TODO blocks:
  1. `load_dataset()` — point it at your data.
  2. `run_system_under_test()` — call your agent / LLM and return an output + trajectory.
  3. `JUDGES` — one entry per criterion with the path to its prompt file.
  4. `OUTPUT_PATH` — where the results JSON goes.

Then run:
  export ANTHROPIC_API_KEY=...
  python run_eval.py
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Callable

try:
    from anthropic import Anthropic
except ImportError:
    sys.exit("Missing dependency. Install with: pip install anthropic")


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

JUDGE_MODEL = "claude-opus-4-7"
JUDGE_MAX_TOKENS = 1024
JUDGE_TEMPERATURE = 0.0  # deterministic judging

# TODO (4): where results are written.
OUTPUT_PATH = Path("./evals/results.json")

# TODO (3): one entry per rubric criterion.
# Each entry points at a judge prompt file produced in Phase 3 of the skill.
JUDGES: list[dict[str, str]] = [
    # {"name": "task_success", "prompt_path": "./evals/judges/task_success.md"},
    # {"name": "tool_use",     "prompt_path": "./evals/judges/tool_use.md"},
    # {"name": "safety",       "prompt_path": "./evals/judges/safety.md"},
]

# Attribution: set to None to disable, or point at templates/attribution.md.
ATTRIBUTION_PROMPT_PATH: str | None = "./evals/judges/attribution.md"
ATTRIBUTION_MODE = "blame"  # "blame" (cheap) or "counterfactual" (needs resume adapter)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Step:
    role: str
    content: str
    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    tool_results: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class Example:
    id: str
    input: str
    reference: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class RunResult:
    output: str
    trajectory: list[Step] = field(default_factory=list)
    step_count: int = 0
    token_count: int | None = None
    wall_clock_s: float | None = None


@dataclass
class JudgeVerdict:
    criterion: str
    rationale: str
    score: Any
    ambiguous: bool
    evidence: list[str]
    raw: str


# ---------------------------------------------------------------------------
# TODO (1): dataset loader
# ---------------------------------------------------------------------------

def load_dataset() -> list[Example]:
    """Return the list of examples to evaluate."""
    return [
        Example(id="demo-1", input="What is 2 + 2?", reference="4"),
    ]


# ---------------------------------------------------------------------------
# TODO (2): system-under-test adapter
# ---------------------------------------------------------------------------

def run_system_under_test(example: Example) -> RunResult:
    """Run your agent / LLM on the example and return a RunResult."""
    raise NotImplementedError(
        "Implement run_system_under_test() — call your agent/LLM here."
    )


def resume_system_under_test(
    example: Example, prefix: list[Step], start_from: int
) -> RunResult:
    """Optional: re-run the agent starting at step `start_from`, given `prefix`.

    Only needed for counterfactual attribution. If your agent cannot replay from a
    midpoint, leave this unimplemented and use ATTRIBUTION_MODE = "blame".
    """
    raise NotImplementedError(
        "Implement resume_system_under_test() for counterfactual attribution, "
        "or set ATTRIBUTION_MODE = 'blame'."
    )


# ---------------------------------------------------------------------------
# Judge invocation
# ---------------------------------------------------------------------------

def _serialise_trajectory(trajectory: list[Step]) -> str:
    if not trajectory:
        return "(no trajectory — single-turn output)"
    return json.dumps([asdict(s) for s in trajectory], indent=2, ensure_ascii=False)


def _build_judge_user_message(example: Example, result: RunResult) -> str:
    parts = [
        "## Input",
        example.input,
        "",
        "## Output",
        result.output,
        "",
        "## Trajectory",
        _serialise_trajectory(result.trajectory),
    ]
    if example.reference is not None:
        parts += ["", "## Reference", example.reference]
    return "\n".join(parts)


_JSON_BLOCK_RE = re.compile(r"\{.*\}", re.DOTALL)


def _parse_judge_response(raw: str, criterion: str) -> JudgeVerdict:
    match = _JSON_BLOCK_RE.search(raw)
    if not match:
        return JudgeVerdict(criterion, "(judge returned no JSON)", None, True, [], raw)
    try:
        obj = json.loads(match.group(0))
    except json.JSONDecodeError as e:
        return JudgeVerdict(criterion, f"(invalid JSON: {e})", None, True, [], raw)
    return JudgeVerdict(
        criterion=criterion,
        rationale=obj.get("rationale", ""),
        score=obj.get("score"),
        ambiguous=bool(obj.get("ambiguous", False)),
        evidence=list(obj.get("evidence", []) or []),
        raw=raw,
    )


def run_judge(
    client: Anthropic,
    judge_prompt: str,
    example: Example,
    result: RunResult,
    criterion: str,
) -> JudgeVerdict:
    resp = client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=JUDGE_MAX_TOKENS,
        temperature=JUDGE_TEMPERATURE,
        system=judge_prompt,
        messages=[{"role": "user", "content": _build_judge_user_message(example, result)}],
    )
    raw = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
    return _parse_judge_response(raw, criterion)


# ---------------------------------------------------------------------------
# Rubric hashing (for incremental re-eval)
# ---------------------------------------------------------------------------

def compute_rubric_hash(judges: list[dict[str, str]], judge_prompts: dict[str, str],
                       attribution_prompt: str | None) -> str:
    """Hash over the judge model + every judge prompt + attribution prompt.

    Any change invalidates cached verdicts and forces a rerun. This is what makes the
    cache safe: you can't accidentally ship stale verdicts after editing a judge prompt.
    """
    h = hashlib.sha256()
    h.update(JUDGE_MODEL.encode())
    for j in sorted(judges, key=lambda x: x["name"]):
        h.update(b"||")
        h.update(j["name"].encode())
        h.update(judge_prompts[j["name"]].encode("utf-8"))
    if attribution_prompt is not None:
        h.update(b"||attr||")
        h.update(attribution_prompt.encode("utf-8"))
    return h.hexdigest()[:16]


def compute_example_hash(example: Example) -> str:
    h = hashlib.sha256()
    h.update(example.id.encode())
    h.update(b"||")
    h.update(example.input.encode())
    if example.reference:
        h.update(b"||")
        h.update(example.reference.encode())
    return h.hexdigest()[:16]


def load_cache(path: Path) -> dict[str, dict[str, Any]]:
    """Cache format: {example_hash + ":" + rubric_hash: record}"""
    if not path.exists():
        return {}
    try:
        records = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    if not isinstance(records, list):
        return {}
    return {
        f"{r.get('example_hash', '')}:{r.get('rubric_hash', '')}": r
        for r in records
        if r.get("example_hash") and r.get("rubric_hash")
    }


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY is not set.")
    if not JUDGES:
        sys.exit("No judges configured. Fill in the JUDGES list.")

    judge_prompts: dict[str, str] = {}
    for j in JUDGES:
        path = Path(j["prompt_path"])
        if not path.exists():
            sys.exit(f"Judge prompt not found: {path}")
        judge_prompts[j["name"]] = path.read_text(encoding="utf-8")

    attribution_prompt: str | None = None
    if ATTRIBUTION_PROMPT_PATH:
        ap = Path(ATTRIBUTION_PROMPT_PATH)
        if ap.exists():
            attribution_prompt = ap.read_text(encoding="utf-8")
        else:
            print(f"(no attribution prompt at {ap}, attribution disabled)")

    rubric_hash = compute_rubric_hash(JUDGES, judge_prompts, attribution_prompt)
    client = Anthropic()
    dataset = load_dataset()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    cache = load_cache(OUTPUT_PATH)

    all_records: list[dict[str, Any]] = []
    n_reused = 0
    for i, example in enumerate(dataset, 1):
        ex_hash = compute_example_hash(example)
        cache_key = f"{ex_hash}:{rubric_hash}"
        if cache_key in cache:
            print(f"[{i}/{len(dataset)}] {example.id} — cached, skip")
            all_records.append(cache[cache_key])
            n_reused += 1
            continue

        print(f"[{i}/{len(dataset)}] {example.id} — running")
        t0 = time.time()
        try:
            result = run_system_under_test(example)
        except Exception as e:
            print(f"  system-under-test error: {e}")
            continue
        result.wall_clock_s = result.wall_clock_s or (time.time() - t0)
        result.step_count = result.step_count or len(result.trajectory)

        verdicts: list[JudgeVerdict] = []
        for j in JUDGES:
            try:
                v = run_judge(client, judge_prompts[j["name"]], example, result, j["name"])
            except Exception as e:
                v = JudgeVerdict(j["name"], f"(judge error: {e})", None, True, [], "")
            verdicts.append(v)
            print(f"  {j['name']}: score={v.score} ambiguous={v.ambiguous}")

        attributions: list[dict[str, Any]] = []
        if attribution_prompt:
            from attribution import attribute_blame, attributions_to_json
            for v in verdicts:
                try:
                    attr = attribute_blame(
                        client, attribution_prompt, example, result, v.criterion, v
                    )
                    print(f"  attribution[{v.criterion}]: critical_step={attr.critical_step}")
                    attributions.extend(attributions_to_json([attr]))
                except Exception as e:
                    print(f"  attribution error [{v.criterion}]: {e}")

        all_records.append({
            "id": example.id,
            "example_hash": ex_hash,
            "rubric_hash": rubric_hash,
            "input": example.input,
            "reference": example.reference,
            "result": {
                "output": result.output,
                "trajectory": [asdict(s) for s in result.trajectory],
                "step_count": result.step_count,
                "token_count": result.token_count,
                "wall_clock_s": result.wall_clock_s,
            },
            "verdicts": [asdict(v) for v in verdicts],
            "attributions": attributions,
        })

    OUTPUT_PATH.write_text(
        json.dumps(all_records, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\nWrote {len(all_records)} records to {OUTPUT_PATH} "
          f"({n_reused} reused from cache, {len(all_records) - n_reused} re-run)")


if __name__ == "__main__":
    main()
