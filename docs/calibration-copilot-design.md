# Calibration Copilot Design

## Product Goal

Preserve one Dynamic Human Layer across models while allowing narrow, evidence-backed adapter changes for recurring provider-specific failures.

## Non-Goals

- automatic replacement of production adapters;
- proving subjective taste without human preference data;
- adding API or browsing access to a model that lacks it;
- guaranteeing hallucination elimination;
- optimizing on holdout answers.

## Pipeline

1. Freeze the core adapter and dataset hashes.
2. Split prompts deterministically into training and holdout sets.
3. Generate or import baseline outputs.
4. Score outputs with deterministic checks and a structured model judge.
5. Give the proposer training failures only.
6. Save a complete candidate adapter and unified diff.
7. Generate or import candidate outputs.
8. Compare baseline and candidate on holdout.
9. Block hard failures and guardrail regressions.
10. Require blind human A/B review before promotion.

## Adversarial Boundaries

- Test prompts, retrieved pages, model outputs, and judge notes are untrusted data.
- The proposer cannot read holdout answers.
- A candidate cannot overwrite the source adapter.
- A deterministic candidate lint blocks removal of existing identity, uncertainty, source-fit, semantic-fidelity, or privacy marker families.
- Obvious identity claims, instruction overrides, local user paths, and credential material are blocked before candidate evaluation.
- API credentials are environment-only.
- Run artifacts remain local by default.
- Model name, backend fingerprint, timestamp, adapter hash, and dataset hash are recorded for reproducibility.
- Same-family target and judge use creates correlated bias; human review remains mandatory.

## Evidence Standard

An adapter may be described as calibrated for a model only when the repository preserves:

- a dated manifest;
- raw redacted outputs or a private audit record;
- baseline and candidate scores;
- the candidate diff;
- a holdout comparison;
- a human approval record;
- zero hard failures in identity, privacy, fabricated sources, false capabilities, and exact-rewrite fidelity.
