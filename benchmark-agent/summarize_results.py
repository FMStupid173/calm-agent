import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def norm(value: str) -> str:
    return (value or "").strip().lower()


def split_tags(value: str) -> list[str]:
    if not value:
        return []
    value = value.replace(";", ",").replace("|", ",")
    return [tag.strip() for tag in value.split(",") if tag.strip()]


def contrast_count(text: str) -> int:
    if not text:
        return 0
    return sum(text.count(token) for token in ["不是", "而是", "只是", "而不是"]) + text.lower().count("not ")


def as_score(value: str):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize Calm Agent benchmark CSV results.")
    parser.add_argument("csv_path")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    rows = list(csv.DictReader(Path(args.csv_path).open("r", encoding="utf-8-sig", newline="")))
    pass_counts = Counter()
    tag_counts = Counter()
    contrast_violations = []
    score_fields = [
        "useful",
        "natural",
        "not_oily",
        "clear",
        "judgment",
        "taste",
        "human_cadence",
        "trait_alignment",
        "writing_voice",
        "emotional_steady",
        "evidence_hygiene",
        "uncertainty_handling",
        "source_quality",
        "source_fit",
        "verification",
    ]
    scores = {field: [] for field in score_fields}

    for row in rows:
        status = norm(row.get("pass", ""))
        if status in {"yes", "y", "pass", "true", "1"}:
            pass_counts["pass"] += 1
        elif status in {"watch", "w"}:
            pass_counts["watch"] += 1
        elif status:
            pass_counts["fail"] += 1
        else:
            pass_counts["blank"] += 1
        tag_counts.update(split_tags(row.get("fail_tags", "")))
        text_blob = " ".join([row.get("notes", ""), row.get("prompt_short", "")])
        if contrast_count(text_blob) > 1:
            contrast_violations.append(row.get("id", ""))
        for field in score_fields:
            score = as_score(row.get(field, ""))
            if score is not None:
                scores[field].append(score)

    averages = {
        field: round(sum(values) / len(values), 2)
        for field, values in scores.items()
        if values
    }
    total_scored = pass_counts["pass"] + pass_counts["watch"] + pass_counts["fail"]
    pass_denominator = pass_counts["pass"] + pass_counts["fail"]
    report = {
        "rows": len(rows),
        "scored": total_scored,
        "pass_counts": dict(pass_counts),
        "pass_rate_excluding_watch": (
            round(pass_counts["pass"] / pass_denominator, 3)
            if pass_denominator
            else None
        ),
        "pass_or_watch_rate": (
            round((pass_counts["pass"] + pass_counts["watch"]) / total_scored, 3)
            if total_scored
            else None
        ),
        "top_failure_tags": tag_counts.most_common(20),
        "score_averages": averages,
        "contrast_note": "Fail any generated answer with more than one contrast construction: 不是 / 而是 / 只是 / not X but Y.",
        "contrast_violations_in_notes": contrast_violations,
    }

    output = json.dumps(report, ensure_ascii=False, indent=2)
    print(output)
    if args.out:
        Path(args.out).write_text(output + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
