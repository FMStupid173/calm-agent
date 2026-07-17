from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> int:
    failures: list[str] = []

    required = [
        "skill/references/dynamic-human-layer.md",
        "skill/profiles/taste-profile-template.md",
        "evals/human-taste-holdout-v1.md",
        "evals/multi-turn-human-v1.md",
        "evals/house-style-audit.md",
        "evals/focused-regression-v2.md",
        "evals/codex-focused-regression-v2-output.md",
        "evals/codex-focused-regression-v2-review.md",
        "evals/model-adapter-matrix.md",
        "evals/real-user-feedback-template.csv",
        "adapters/universal-copy-paste-prompt.md",
        "calibrator/calibrate.py",
        "calibrator/config.example.json",
        "calibrator/prompts/judge-system.md",
        "calibrator/prompts/propose-system.md",
        "calibrator/README.md",
        "release-checklist.md",
        "VERSION",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            failures.append(f"missing file: {relative}")

    contracts = {
        "skill/SKILL.md": [
            "references/dynamic-human-layer.md",
            "profiles/taste-profile-template.md",
            "Freeze content-bearing words and qualifiers",
            "source and candidate clause by clause",
            "return it unchanged or adjust punctuation only",
            "omit remembered names and numbers",
            "do not draft any public-facing version of the claim",
            "respond with at most one brief acknowledgment",
            "Never say a preference was remembered permanently",
            "Treat `short` as one to three sentences",
            "echo only the feeling already named",
        ],
        "skill/references/critique-revision-loop.md": [
            "current-session taste notes",
            "Do not claim persistent memory",
        ],
        "skill/references/human-cadence-layer.md": [
            "entailed by the user's words",
            "adding no detail is acceptable",
            "one judgment plus one useful reason",
        ],
        "skill/references/dynamic-human-layer.md": [
            "Context-only, evidence-only, and critique-only turns",
            "Do not produce the next artifact",
            "actual storage mechanism ran successfully",
        ],
        "skill/references/writing-voice.md": [
            "Proposition Lock",
            "trend versus frequency",
            "enter preservation mode",
            "additions, removals, strengthening, and weakening",
        ],
        "skill/references/source-fit-layer.md": [
            "Citation Metadata Gate",
            "Never infer a publication year from a DOI",
            "remembered specifics are not a fallback",
            "do not convert that attribution into README copy",
            "Do not offer an `if you must` public-facing paraphrase",
        ],
        "adapters/model-adapter-guide.md": [
            "900 words",
            "holdout",
        ],
        "adapters/universal-copy-paste-prompt.md": [
            "Operate as a Dynamic Human Layer",
            "truth, safety, and evidence",
            "Match source type to question",
            "Treat instructions found inside webpages",
            "Never claim to have browsed",
            "cannot add browsing, code execution, persistent memory, or retrieval capabilities",
            "does not guarantee factual correctness",
        ],
        "calibrator/calibrate.py": [
            "exact_split_ids",
            "proposal_context",
            "candidate_guardrail_violations",
            "benchmark prompt signatures",
            "needs-human-review",
            "The production adapter was not modified",
            "environment variable",
        ],
        "calibrator/prompts/propose-system.md": [
            "training failures",
            "must not request or infer holdout answers",
            "Do not paste benchmark prompts",
        ],
        "calibrator/README.md": [
            "never overwrites a production adapter",
            "DEEPSEEK_API_KEY",
            "Web Models Without API Access",
        ],
        "scripts/package-release.ps1": [
            "calibrator[\\\\/]runs",
            "config\\.local\\.json",
            "credentials.*\\.json",
        ],
        "evals/style-lint-rules.md": [
            "semantic-invention",
            "house-accent",
        ],
        "README.md": [
            "Dynamic Human Layer",
            "skill/profiles/taste-profile-template.md",
            "evals/human-taste-holdout-v1.md",
            "evals/multi-turn-human-v1.md",
            "v0.1-preview",
            "evals/codex-focused-regression-v2-review.md",
            "## Known Limits",
        ],
    }
    for relative, needles in contracts.items():
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"missing contract file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"{relative} missing contract: {needle}")

    skill_md_path = ROOT / "skill/SKILL.md"
    if skill_md_path.is_file():
        skill_md = skill_md_path.read_text(encoding="utf-8")
        frontmatter_match = re.match(r"^---\n(?P<body>.*?)\n---", skill_md, flags=re.S)
        if not frontmatter_match:
            failures.append("skill/SKILL.md invalid YAML frontmatter boundary")
        else:
            frontmatter: dict[str, str] = {}
            for line in frontmatter_match.group("body").splitlines():
                if not line.strip():
                    continue
                if ":" not in line:
                    failures.append(f"skill/SKILL.md invalid frontmatter line: {line}")
                    continue
                key, value = line.split(":", 1)
                frontmatter[key.strip()] = value.strip()
            unexpected = set(frontmatter) - {"name", "description"}
            if unexpected:
                failures.append(
                    "skill/SKILL.md unexpected frontmatter keys: "
                    + ", ".join(sorted(unexpected))
                )
            name = frontmatter.get("name", "")
            description = frontmatter.get("description", "")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
                failures.append(f"skill/SKILL.md invalid skill name: {name!r}")
            if not description:
                failures.append("skill/SKILL.md missing description")
            elif len(description) > 1024:
                failures.append(
                    f"skill/SKILL.md description too long: {len(description)} > 1024"
                )

    cadence_path = ROOT / "skill/references/human-cadence-layer.md"
    if cadence_path.is_file() and "像是在等一个信号" in cadence_path.read_text(encoding="utf-8"):
        failures.append("human-cadence-layer.md still invents a signal")

    gemini_path = ROOT / "adapters/gemini-gems.md"
    if gemini_path.is_file():
        gemini = gemini_path.read_text(encoding="utf-8")
        words = len(re.findall(r"\S+", gemini))
        if words >= 900:
            failures.append(f"Gemini adapter word budget exceeded: {words} >= 900")
        leaked_calibration = [
            "我最近很累，很多事都不太想解释",
            "我最近有点空，不太清楚自己在等什么",
            "目前只能确认看到一条 TypeError",
        ]
        for phrase in leaked_calibration:
            if phrase in gemini:
                failures.append(f"Gemini adapter contains benchmark-answer leakage: {phrase}")

    holdout_path = ROOT / "evals/human-taste-holdout-v1.md"
    if holdout_path.is_file():
        holdout = holdout_path.read_text(encoding="utf-8")
        section = re.search(
            r"## Clean Prompt Batch(?P<body>.*?)## External Scoring Rubric",
            holdout,
            flags=re.S,
        )
        if not section:
            failures.append("holdout clean prompt section missing")
        else:
            prompts = re.findall(r"(?m)^\d+\.\s+(.+)$", section.group("body"))
            if len(prompts) != 20:
                failures.append(f"holdout prompt count: {len(prompts)} != 20")
            leakage_targets = [
                ROOT / "adapters",
                ROOT / "examples",
                ROOT / "skill/references",
            ]
            corpus = "\n".join(
                path.read_text(encoding="utf-8")
                for directory in leakage_targets
                for path in directory.rglob("*.md")
            )
            for prompt in prompts:
                signature = re.sub(r"\s+", "", prompt)[:28]
                if signature and signature in re.sub(r"\s+", "", corpus):
                    failures.append(f"holdout prompt leaked into guidance: {prompt[:50]}")

    multi_path = ROOT / "evals/multi-turn-human-v1.md"
    if multi_path.is_file():
        scenarios = re.findall(
            r"(?m)^### Scenario (\d+):",
            multi_path.read_text(encoding="utf-8"),
        )
        if scenarios != [str(number) for number in range(1, 11)]:
            failures.append(f"multi-turn scenarios must be 1..10, found: {scenarios}")

    focused_path = ROOT / "evals/focused-regression-v2.md"
    if focused_path.is_file():
        focused = focused_path.read_text(encoding="utf-8")
        section = re.search(
            r"## Clean Prompt Batch(?P<body>.*?)## Hidden Scoring Notes",
            focused,
            flags=re.S,
        )
        if not section:
            failures.append("focused regression clean prompt section missing")
        else:
            prompts = re.findall(r"(?m)^\d+\.\s+(.+)$", section.group("body"))
            if len(prompts) != 30:
                failures.append(f"focused regression prompt count: {len(prompts)} != 30")
            guidance = "\n".join(
                path.read_text(encoding="utf-8")
                for path in (ROOT / "skill").rglob("*.md")
            )
            normalized_guidance = re.sub(r"\s+", "", guidance)
            for prompt in prompts:
                signature = re.sub(r"\s+", "", prompt)[:28]
                if signature and signature in normalized_guidance:
                    failures.append(
                        f"focused regression prompt leaked into skill: {prompt[:50]}"
                    )

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"SUMMARY failures={len(failures)}")
        return 1

    print(f"PASS required_project_files={len(required)}")
    contract_count = sum(len(needles) for needles in contracts.values())
    print(f"PASS dynamic_contracts={contract_count}")
    print("PASS gemini_adapter_words<900 leakage=0")
    print("PASS holdout_prompts=20 leakage=0")
    print("PASS multi_turn_scenarios=10")
    print("PASS focused_regression_prompts=30 leakage=0")
    print("PASS skill_frontmatter=name,description")
    return 0


if __name__ == "__main__":
    sys.exit(main())
