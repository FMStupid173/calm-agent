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

## Release Positioning

Use:

> A portable output-quality layer for calmer, clearer, less templated AI responses, with explicit rules for human cadence, semantic fidelity, and evidence boundaries.

Avoid:

- claiming to reproduce Claude internals;
- promising that every AI will sound identical;
- claiming perfect semantic preservation;
- presenting historical adapter scores as current cross-model proof;
- calling private conversation data a public training dataset.

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
