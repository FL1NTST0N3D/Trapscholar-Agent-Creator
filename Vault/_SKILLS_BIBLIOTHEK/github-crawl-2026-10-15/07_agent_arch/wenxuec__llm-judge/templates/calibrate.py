"""
Calibration: compare judge scores against human labels.

Usage:
  python calibrate.py --human human_labels.csv --judge results.json

Expected human CSV columns:
  id,criterion,score

Expected judge JSON: output of run_eval.py (a list of records with `verdicts`).

Prints per-criterion agreement:
  - Cohen's kappa for categorical scales (binary, 3-point, 5-point).
  - Spearman for numeric scales.
  - Raw agreement rate for reference.

Targets (from the skill): kappa >= 0.6 for categorical, Spearman >= 0.7 for numeric.
If below target, iterate on the judge prompt or rubric anchors.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path


def cohens_kappa(a: list, b: list) -> float:
    assert len(a) == len(b) and a, "need equal non-empty sequences"
    labels = sorted(set(a) | set(b), key=lambda x: str(x))
    idx = {label: i for i, label in enumerate(labels)}
    n = len(labels)
    mat = [[0] * n for _ in range(n)]
    for x, y in zip(a, b):
        mat[idx[x]][idx[y]] += 1
    total = len(a)
    observed = sum(mat[i][i] for i in range(n)) / total
    row = [sum(mat[i]) / total for i in range(n)]
    col = [sum(mat[i][j] for i in range(n)) / total for j in range(n)]
    expected = sum(row[i] * col[i] for i in range(n))
    if expected == 1.0:
        return 1.0
    return (observed - expected) / (1 - expected)


def spearman(a: list[float], b: list[float]) -> float:
    assert len(a) == len(b) and a

    def ranks(xs: list[float]) -> list[float]:
        order = sorted(range(len(xs)), key=lambda i: xs[i])
        r = [0.0] * len(xs)
        i = 0
        while i < len(xs):
            j = i
            while j + 1 < len(xs) and xs[order[j + 1]] == xs[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r

    ra, rb = ranks(a), ranks(b)
    mean_a = sum(ra) / len(ra)
    mean_b = sum(rb) / len(rb)
    num = sum((x - mean_a) * (y - mean_b) for x, y in zip(ra, rb))
    den_a = math.sqrt(sum((x - mean_a) ** 2 for x in ra))
    den_b = math.sqrt(sum((y - mean_b) ** 2 for y in rb))
    if den_a == 0 or den_b == 0:
        return 0.0
    return num / (den_a * den_b)


def is_numeric(xs: list) -> bool:
    try:
        [float(x) for x in xs]
        return True
    except (TypeError, ValueError):
        return False


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--human", required=True, help="CSV with id,criterion,score")
    p.add_argument("--judge", required=True, help="results.json from run_eval.py")
    args = p.parse_args()

    human: dict[tuple[str, str], str] = {}
    with open(args.human, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            human[(row["id"], row["criterion"])] = row["score"]

    records = json.loads(Path(args.judge).read_text(encoding="utf-8"))
    judge: dict[tuple[str, str], object] = {}
    for rec in records:
        for v in rec["verdicts"]:
            judge[(rec["id"], v["criterion"])] = v["score"]

    by_crit: dict[str, list[tuple[object, object]]] = defaultdict(list)
    for (ex_id, crit), h_score in human.items():
        j_score = judge.get((ex_id, crit))
        if j_score is None:
            continue
        by_crit[crit].append((h_score, j_score))

    if not by_crit:
        print("No overlapping (id, criterion) pairs.")
        return

    print(f"{'criterion':<24} {'n':>4}  {'agreement':>10}  {'metric':<18}")
    print("-" * 62)
    for crit, pairs in by_crit.items():
        h = [p[0] for p in pairs]
        j = [p[1] for p in pairs]
        agree = sum(1 for a, b in zip(h, j) if str(a) == str(b)) / len(pairs)
        if is_numeric(h) and is_numeric(j):
            metric = spearman([float(x) for x in h], [float(x) for x in j])
            label = f"spearman={metric:+.3f}"
        else:
            metric = cohens_kappa(h, j)
            label = f"kappa={metric:+.3f}"
        print(f"{crit:<24} {len(pairs):>4}  {agree:>9.1%}  {label:<18}")


if __name__ == "__main__":
    main()
