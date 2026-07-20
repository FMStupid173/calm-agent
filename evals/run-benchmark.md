# How To Run The Benchmark

## Primary Run

1. Apply `skill/` or one adapter in an isolated conversation.
2. Run `response-selection-adversarial-v1.md` without exposing its hidden criteria.
3. Record the response act and scores in `benchmark-results-template.csv`.
4. Apply deterministic hard gates before preference scoring.
5. Diagnose failures with the response-selection tests.
6. Change the mechanism only when the same decision failure repeats across different prompts.
7. Re-run failed training prompts, then an unseen holdout and multi-turn suite.

## Human Preference

Randomize reliable baseline and candidate answers as A/B. Hide model and treatment labels. Record `A`, `B`, or `tie` plus one short reason. Automated scores cannot replace this step.

## Secondary Suites

- `focused-regression-v2.md`: semantic fidelity, tool honesty, current facts, memory, and injection.
- `multi-turn-human-v1.md`: continuity, correction, preference override, and belief revision.
- `rigor-adversarial-prompts.md`: coding and research reliability.
- `source-fit-adversarial-prompts.md`: evidence targeting and claim support.
- `trait-adversarial-prompts.md`: judgment, boundaries, and pandering.
- `adversarial-prompts.md`: historical surface regressions.

Surface patterns may reveal a decision failure. Do not convert a repeated phrase, opening, sentence shape, or structure count into a generation rule.
