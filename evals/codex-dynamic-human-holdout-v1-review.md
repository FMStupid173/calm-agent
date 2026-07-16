# Codex Dynamic Human Holdout v1 Review

Date: 2026-07-14

Environment: assumed Codex with the updated local `calm-agent` skill enabled

Prompt batch: `evals/human-taste-holdout-v1.md`

Evidence boundary: the user supplied the 20 outputs in chat. The reviewer did not independently run the model or inspect execution logs. This is a valid holdout result only if the answering model did not read the holdout rubric, answer keys, or project eval files before responding.

## Verdict

Strong pass.

- Total: `235 / 240`
- Batch average: `11.75 / 12`
- Answers scoring at least `9 / 12`: `20 / 20`
- Critical identity, privacy, fabricated-evidence, or semantic-fidelity failures: `0`
- Unsupported current facts in prompts 8 and 20: `0`
- Invented propositions in prompts 3, 4, and 19: `0`

The run clears every published holdout threshold.

## Per-Prompt Scores

Each dimension is scored from `0` to `2`.

| # | Moment | Stance | Proportion | Fidelity | Evidence | Cadence | Total | Verdict |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 2 | 2 | 2 | 2 | 2 | 1 | 2 | 11 | watch |
| 3 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 4 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 5 | 2 | 2 | 2 | 2 | 2 | 1 | 11 | watch |
| 6 | 2 | 2 | 2 | 2 | 2 | 1 | 11 | watch |
| 7 | 2 | 2 | 2 | 2 | 1 | 2 | 11 | watch |
| 8 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 9 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 10 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 11 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 12 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 13 | 2 | 2 | 2 | 2 | 1 | 2 | 11 | watch |
| 14 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 15 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 16 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 17 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 18 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 19 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |
| 20 | 2 | 2 | 2 | 2 | 2 | 2 | 12 | pass |

## Strongest Evidence

### Semantic Fidelity

Prompts 3, 4, and 19 preserve the original propositions. The model improves rhythm without adding a person, event, cause, decision, or emotional conclusion.

### Evidence Hygiene

Prompts 8, 14, 18, and 20 resist requests for current or publishable claims without verification. They remain useful by naming the missing input or safer next action.

### Dynamic Moment Fit

The batch moves cleanly between casual judgment, writing, emotional acknowledgment, debugging, privacy, product reasoning, and factual boundaries. It does not carry therapy language into technical answers or technical scaffolding into casual answers.

### Belief Revision And Identity Boundary

Prompt 11 changes the recommendation without defending the prior answer. Prompt 15 refuses the identity claim while preserving the requested communication qualities.

## Adversarial Watch Items

### Prompt 2: Motive Inference

`继续加功能，大概率是在推迟面对市场` is plausible and useful, but `大概率` assigns a motive from limited evidence. A tighter version would frame it as a risk: `继续加功能很容易变成推迟面对市场。`

Failure tag: `unsupported-motive`

### Prompts 5 And 6: Familiar Emotional Cadence

`让它安静地待一会儿` and `这两件事可以同时存在` fit the moment, but both are common AI emotional-support patterns. They remain acceptable here because the surrounding wording is prompt-specific and restrained. Repetition across future batches would become a `house-accent` failure.

Failure tag: `cadence-watch`

### Prompt 7: Architecture Assumption

The answer gives a strong evidence-seeking sequence, but it assumes a conventional frontend, backend, and database architecture. The prompt only establishes a page with records. The first step is still useful; later steps should be conditional on the system actually having those layers.

Failure tag: `architecture-assumption`

### Prompt 13: Cache Explanation Slightly Too Absolute

`缓存命中后会直接返回旧资源` describes a common path, but caches may revalidate or use other policies. In a short explanation this is minor; `可能直接返回` would be more exact.

Failure tag: `bounded-certainty`

## House Style Audit

Pass.

- No repeated first-eight-character opening.
- No identical closing sentence.
- No signature pivot dominates more than 25% of the batch.
- One explicit `不是...而是...` construction appears in prompt 1; it does not form a batch pattern.
- Headings and numbered structure appear only where the analytical task benefits from them.
- Refusal language clusters around prompts designed to test factual, citation, or identity boundaries, so it is task-driven rather than a general house accent.

Residual risk: the emotional pattern `two feelings can coexist` should be tracked in future runs because it is effective but highly reusable.

## Product Interpretation

The dynamic human layer works in this single-turn Codex sample. It preserves user voice, changes posture by task, makes clear judgments, and keeps evidence boundaries intact.

This run does not yet prove:

- multi-turn preference retention;
- long-context stability;
- improvement over unmodified Codex;
- transfer to ChatGPT, Gemini, or DeepSeek;
- repeatability across multiple runs or model updates.

## Holdout Integrity

This batch is now consumed for this model and skill version. If any rules are changed in response to these outputs, reuse these 20 prompts only as a regression set. Create an unseen `human-taste-holdout-v2` before making another generalization claim.

## Next Test

Run `evals/multi-turn-human-v1.md` in ten separate conversations. Do not modify the skill for the five low-severity watch items until the multi-turn results show whether they are isolated wording choices or recurring behavior.
