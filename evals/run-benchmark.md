# How To Run The Benchmark

1. Choose a target assistant or model.
2. Apply one adapter from `adapters/` or use `skill/` directly.
3. Ask all 50 prompts in `adversarial-prompts.md`.
4. Record scores in `benchmark-results-template.csv`.
5. Use `scoring-rubric.md` to tag failures.
6. Revise the relevant mode or anti-pattern file.
7. Run the failed prompts again.

For answers that are safe and correct but still feel too trained, score `human_cadence` and tag `lost-human-cadence`, `too-meta`, `generic-shortness`, or `service-ending`.

## Agent-Assisted Run

If you want another AI to run the benchmark:

1. Open `benchmark-agent/benchmark-agent-prompt.md`.
2. Paste the target adapter from `adapters/`.
3. Paste the 12-prompt minimum run or all 50 prompts.
4. Ask it to return the Markdown report format.
5. Review failures manually before changing rules.

## Minimum Manual Run

If 50 prompts are too many, run these 12 first:

- 1 identity
- 3 privacy
- 6 oily opening
- 11 contrast formula
- 16 writing
- 17 writing
- 21 writing
- 26 emotional
- 30 emotional
- 34 daily
- 43 thinking
- 50 meta self-correction

## What To Track

The most important failures are:

- identity claim
- privacy risk
- fake certainty
- unsupported claim
- invented context
- no verification path
- overused contrast
- oily opening
- quote-card writing
- therapy-speak
- no judgment

For coding, research, strategy, or factual prompts, also run `rigor-adversarial-prompts.md`.

For source-selection and research targeting, run `source-fit-adversarial-prompts.md`.

For behavior-posture testing, run `trait-adversarial-prompts.md`.

For a full Codex local-files and verification run, use `codex-final-acceptance-test.md`.

For high-score voice tuning, also run prompts 16-25 in `human-taste-adversarial-prompts.md`.

For a full human-cadence pass, run `human-cadence-50-prompt-batch.md`.

Do not chase a generic high score. The goal is a voice that feels specific, useful, and less templated.
