#!/usr/bin/env python3
"""
Ad Strength Scorer

Analyzes an RSA and predicts Ad Strength rating based on Google's known criteria:
uniqueness, keyword relevance, CTA diversity, asset quantity, and popular keyword inclusion.

Usage:
    python ad_strength_scorer.py --headlines "H1|H2|H3|..." --descriptions "D1|D2|..." --keywords "kw1,kw2,kw3"
"""

import argparse
import re
from collections import Counter
from typing import List, Dict


def tokenize(text: str) -> set:
    """Extract meaningful words from text, lowercased."""
    words = re.findall(r"[a-z]+", text.lower())
    stop_words = {"the", "a", "an", "in", "on", "at", "to", "for", "of", "and", "or", "is", "are", "by", "with"}
    return set(words) - stop_words


def semantic_similarity(h1: str, h2: str) -> float:
    """Calculate Jaccard similarity between two headlines."""
    tokens1 = tokenize(h1)
    tokens2 = tokenize(h2)
    if not tokens1 or not tokens2:
        return 0.0
    intersection = tokens1 & tokens2
    union = tokens1 | tokens2
    return len(intersection) / len(union)


def score_uniqueness(headlines: List[str]) -> Dict:
    """Score headline uniqueness. Detects semantic duplicates."""
    duplicates = []
    for i in range(len(headlines)):
        for j in range(i + 1, len(headlines)):
            sim = semantic_similarity(headlines[i], headlines[j])
            if sim > 0.5:
                duplicates.append((i + 1, j + 1, headlines[i], headlines[j], round(sim, 2)))

    if len(duplicates) == 0:
        score = 10
    elif len(duplicates) == 1:
        score = 7
    elif len(duplicates) == 2:
        score = 5
    elif len(duplicates) <= 4:
        score = 3
    else:
        score = 1

    return {
        "score": score,
        "duplicates": duplicates,
        "detail": f"{len(duplicates)} semantic duplicate pairs found",
    }


def score_keyword_relevance(headlines: List[str], descriptions: List[str], keywords: List[str]) -> Dict:
    """Score how well keywords are integrated into ad copy."""
    keyword_hits_headlines = 0
    keyword_hits_descriptions = 0
    keyword_details = []

    for kw in keywords:
        kw_lower = kw.lower().strip()
        h_count = sum(1 for h in headlines if kw_lower in h.lower())
        d_count = sum(1 for d in descriptions if kw_lower in d.lower())
        keyword_hits_headlines += min(h_count, 3)  # Cap at 3 per keyword
        keyword_hits_descriptions += min(d_count, 2)
        keyword_details.append({
            "keyword": kw,
            "in_headlines": h_count,
            "in_descriptions": d_count,
        })

    total_hits = keyword_hits_headlines + keyword_hits_descriptions
    if total_hits >= 6:
        score = 10
    elif total_hits >= 4:
        score = 8
    elif total_hits >= 2:
        score = 6
    elif total_hits >= 1:
        score = 4
    else:
        score = 1

    return {
        "score": score,
        "details": keyword_details,
        "total_hits": total_hits,
    }


def score_cta_diversity(headlines: List[str], descriptions: List[str]) -> Dict:
    """Score CTA variety across ad copy."""
    cta_verbs = [
        "get", "start", "try", "book", "call", "shop", "buy", "order",
        "download", "claim", "request", "schedule", "visit", "see",
        "learn", "discover", "find", "join", "sign up", "subscribe",
        "save", "compare", "browse", "apply", "enroll", "reserve",
    ]

    found_ctas = set()
    all_text = headlines + descriptions

    for text in all_text:
        text_lower = text.lower()
        for verb in cta_verbs:
            if verb in text_lower:
                found_ctas.add(verb)

    unique_count = len(found_ctas)
    if unique_count >= 5:
        score = 10
    elif unique_count >= 4:
        score = 8
    elif unique_count >= 3:
        score = 7
    elif unique_count >= 2:
        score = 5
    elif unique_count >= 1:
        score = 3
    else:
        score = 1

    return {
        "score": score,
        "ctas_found": sorted(found_ctas),
        "unique_count": unique_count,
    }


def score_asset_quantity(headlines: List[str], descriptions: List[str]) -> Dict:
    """Score based on number of assets provided."""
    h_count = len(headlines)
    d_count = len(descriptions)

    h_score = min(10, max(1, h_count - 2))  # 3 headlines = 1, 15 = 10
    d_score = {1: 2, 2: 5, 3: 7, 4: 10}.get(d_count, 1)

    score = round((h_score * 0.6 + d_score * 0.4))

    return {
        "score": score,
        "headlines": h_count,
        "descriptions": d_count,
        "detail": f"{h_count}/15 headlines, {d_count}/4 descriptions",
    }


def score_char_utilization(headlines: List[str], descriptions: List[str]) -> Dict:
    """Score how well character limits are utilized."""
    h_lengths = [len(h) for h in headlines]
    d_lengths = [len(d) for d in descriptions]

    avg_h = sum(h_lengths) / len(h_lengths) if h_lengths else 0
    avg_d = sum(d_lengths) / len(d_lengths) if d_lengths else 0

    # Good headlines average 22-28 chars (using the space without being padded)
    if 22 <= avg_h <= 28:
        h_score = 10
    elif 18 <= avg_h <= 30:
        h_score = 7
    else:
        h_score = 4

    # Good descriptions average 80-90 chars
    if 80 <= avg_d <= 90:
        d_score = 10
    elif 70 <= avg_d <= 90:
        d_score = 7
    else:
        d_score = 4

    score = round((h_score + d_score) / 2)

    return {
        "score": score,
        "avg_headline_length": round(avg_h, 1),
        "avg_description_length": round(avg_d, 1),
        "headline_lengths": h_lengths,
        "description_lengths": d_lengths,
    }


def predict_ad_strength(scores: Dict) -> str:
    """Predict overall Ad Strength rating."""
    total = sum(s["score"] for s in scores.values())
    max_total = len(scores) * 10

    percentage = total / max_total * 100

    if percentage >= 80:
        return "Excellent"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 40:
        return "Average"
    else:
        return "Poor"


def run_analysis(headlines: List[str], descriptions: List[str], keywords: List[str]):
    """Run full Ad Strength analysis."""
    scores = {
        "uniqueness": score_uniqueness(headlines),
        "keyword_relevance": score_keyword_relevance(headlines, descriptions, keywords),
        "cta_diversity": score_cta_diversity(headlines, descriptions),
        "asset_quantity": score_asset_quantity(headlines, descriptions),
        "char_utilization": score_char_utilization(headlines, descriptions),
    }

    prediction = predict_ad_strength(scores)
    total = sum(s["score"] for s in scores.values())

    print("\n" + "=" * 60)
    print("AD STRENGTH ANALYSIS")
    print("=" * 60)

    print(f"\n{'Pillar':<25} {'Score':>6} {'Details'}")
    print("-" * 60)
    for name, data in scores.items():
        label = name.replace("_", " ").title()
        detail = data.get("detail", data.get("unique_count", ""))
        print(f"  {label:<23} {data['score']:>3}/10  {detail}")

    print("-" * 60)
    print(f"  {'TOTAL':<23} {total:>3}/50")
    print(f"\n  PREDICTED AD STRENGTH: {prediction}")

    # Show issues
    if scores["uniqueness"]["duplicates"]:
        print(f"\n  DUPLICATE PAIRS:")
        for d in scores["uniqueness"]["duplicates"]:
            print(f"    H{d[0]} \"{d[2]}\" ~ H{d[1]} \"{d[3]}\" (similarity: {d[4]})")

    if scores["keyword_relevance"]["total_hits"] < 3:
        print(f"\n  KEYWORD ISSUES:")
        for kd in scores["keyword_relevance"]["details"]:
            if kd["in_headlines"] == 0:
                print(f"    Missing from headlines: \"{kd['keyword']}\"")

    if scores["cta_diversity"]["unique_count"] < 3:
        print(f"\n  CTA ISSUES: Only {scores['cta_diversity']['unique_count']} unique CTAs found")
        print(f"    Found: {', '.join(scores['cta_diversity']['ctas_found'])}")

    print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Ad Strength Scorer")
    parser.add_argument("--headlines", type=str, required=True, help="Headlines separated by |")
    parser.add_argument("--descriptions", type=str, required=True, help="Descriptions separated by |")
    parser.add_argument("--keywords", type=str, required=True, help="Keywords separated by ,")

    args = parser.parse_args()

    headlines = [h.strip() for h in args.headlines.split("|") if h.strip()]
    descriptions = [d.strip() for d in args.descriptions.split("|") if d.strip()]
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]

    run_analysis(headlines, descriptions, keywords)


if __name__ == "__main__":
    main()
