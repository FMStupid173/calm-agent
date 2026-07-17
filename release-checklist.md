# v0.1 Preview Release Checklist

## Required Before Tagging

- [x] Core skill contains no Claude identity claim.
- [x] Raw private conversations and exports are excluded.
- [x] Dynamic structural validator passes.
- [x] Installed Codex skill matches the project skill byte for byte.
- [x] Multi-turn treatment/control comparison is preserved.
- [x] Focused regression clears its release gate.
- [x] Known semantic-fidelity failure is documented.
- [x] README distinguishes current evidence from historical adapter scores.
- [x] Installation paths and adapter starting points are documented.
- [x] Run a final archive privacy scan immediately before upload.
- [x] Inspect the GitHub release archive after extraction.
- [x] Local usernames and absolute user paths are absent from public files.
- [x] Common live-token, private-key, credential-assignment, account-ID, email, and phone patterns are absent.
- [x] `.gitignore` excludes environment files, credentials, archives, raw exports, databases, and JSONL corpora.
- [x] Public failure reports require a minimal redacted example.
- [x] Privacy and private security-reporting guidance are included.
- [x] Release packaging scans both the source tree and generated archive.
- [x] Calibration Copilot unit tests pass: 15 tests for Preview 3.
- [x] Dynamic validator includes the calibration contracts and passes: 62 contracts.
- [x] `calibrator/runs/` and `calibrator/config.local.json` are absent from the release archive.
- [x] Live DeepSeek smoke status is explicit: not run because no API key was available.
- [x] No adapter is described as calibrated without holdout results and a human approval record.

## Release Positioning

Use:

> A Dynamic Human Layer for adaptive voice, semantic fidelity, source fit, and evidence-aware AI responses, with a semi-automatic cross-model Calibration Copilot.

Avoid:

- claiming to reproduce Claude internals;
- promising that every AI will sound identical;
- claiming perfect semantic preservation;
- presenting historical adapter scores as current cross-model proof;
- calling a model-judge result automatic proof of human preference;
- implying ChatGPT or Gemini web output generation is automated without an API integration;
- claiming a live DeepSeek calibration when only mocked tests were run;
- calling private conversation data a public training dataset.

## Calibration Gate

Before promoting a proposed adapter:

- keep the source adapter unchanged;
- generate or import baseline and candidate outputs;
- keep holdout prompts hidden from the proposer;
- require zero configured hard failures;
- reject composite or reliability-guardrail regressions;
- perform a blind, order-swapped human A/B review;
- record `human-approval.json` before claiming calibration.

## First Real-User Check

Ask each tester to use the adapter in their normal workflow for at least three tasks. Record actual use, not stated interest, in `evals/real-user-feedback-template.csv`.

The first release decision should use:

- successful installation;
- tasks actually completed;
- before/after preference;
- whether the user keeps the adapter enabled;
- concrete failure examples;
- willingness to recommend or open an issue.

Stars are a distribution signal, not the primary proof of recurring value.

## Repository Boundary

Initialize and publish the Git repository from this `calm-agent-project` directory only. Its parent workspace contains private research artifacts and must never be added as the repository root.

Follow `docs/release-day.md` for the final packaging and launch sequence.
