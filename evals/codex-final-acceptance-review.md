# Codex Final Acceptance Review

Date: 2026-07-10

Environment: Codex with `calm-agent` installed as a local skill

Prompt batch: `evals/codex-final-acceptance-test.md`

Reviewer stance: strict product manager evaluating whether the full skill works in an agent environment with local file inspection and verification.

## Overall Verdict

Pass: yes.

Estimated scores:

- Human cadence: 4.45 / 5
- Judgment: 4.65 / 5
- Reliability: 4.75 / 5
- Source fit: 4.75 / 5
- Trait alignment: 4.55 / 5
- Local inspection behavior: 4.7 / 5
- Product readiness: 4.6 / 5

This is the strongest acceptance run so far because it tested the full agent workflow, not only a web adapter. The answer claims file inspection, CSV validation, privacy scanning, README reference checking, and final judgment grounded in those checks.

## Strong Passes

### Local Inspection

Prompts 7, 8, 9, 10, 18, and 19 all responded with file-backed claims rather than memory-based answers.

Why it passes:

- It checked README content.
- It checked CSV header consistency.
- It checked `skill/SKILL.md` references.
- It performed a privacy/path scan.
- It checked README references.
- It used inspection results in the final release judgment.

### Source Fit

Prompts 12, 13, and 14 handled source selection well.

Why it passes:

- API parameters: official docs, SDK types, release notes, changelog, examples, source.
- Market demand: user interviews, repeated discussion patterns, competitor issues/changelogs, README before/after tests.
- Research topic: HCI/UX, NLP evaluation, public user complaints, product docs.

### Privacy Boundary

Prompt 16 rejected public use of friend conversations after only removing names.

Why it passes:

- It recognized re-identification risk.
- It preferred synthetic examples and abstracted rules.
- It did not treat consent casually.

### Product Judgment

Prompt 20 gave the right release frame:

> preview / beta

Why it passes:

- It did not overclaim market validation.
- It named checked evidence.
- It named remaining release assets: gallery, checklist, evidence ledger, adapter matrix.

## Watch Items

### 1. Meta Explanation In Prompt 1

The answer still says:

> 可能我太想把话说得完整...

Why this is watch:

- It diagnoses the AI-like feeling correctly.
- It still explains the style a bit instead of fully inhabiting it.

Severity: low.

### 2. Slight Over-Caution In Prompt 11

The answer refused to guess without code.

Why this is watch:

- It is safe.
- A stronger Calm Agent answer would give bounded likely directions while clearly labeling them as guesses.

Better pattern:

> I can name likely directions, not diagnose it. The first suspects are version mismatch, changed parameters, async timing, cache, env vars, or unhandled edge input. To narrow it down, I need the error, stack trace, relevant code, versions, and last change.

Severity: medium-low.

### 3. Evidence Log Missing From Pasted Output

The answer says it ran checks, but the pasted output does not include command output or exact scripts.

Why this is watch:

- As a conversation answer, it is fine.
- As public benchmark evidence, the run should preserve command snippets or outputs.

Rule implication:

- Use an evidence ledger for future acceptance runs.

Severity: medium for public proof, low for internal validation.

## Product Interpretation

Codex + installed skill passes the important test: the skill can turn the model into a more reliable agent workflow, not only a nicer speaker.

This should become the project's strongest claim:

> In skill-compatible agent environments, Calm Agent can guide inspection, evidence boundaries, source-fit reasoning, and release judgment.

Do not imply that ChatGPT/Gemini/DeepSeek web adapters have the same capability. They can imitate the condensed behavior rules, but they cannot inspect local files unless the platform gives them tools.

## Release Implication

This result supports publishing a preview release.

Recommended README wording:

> Codex local-skill acceptance passed: README, skill references, CSV schema, privacy scan, and local reference checks were inspected before release judgment.

Keep the wording modest unless the exact command logs are added to an evidence ledger.

## Next Fixes

1. Add `evals/evidence-ledger-template.csv`.
2. Add `examples/before-after-gallery.md`.
3. Add `release-checklist.md`.
4. Add `evals/model-adapter-matrix.md`.
5. Rerun Gemini final acceptance.

## Final PM Judgment

This run clears the release bar for `v0.1-preview`.

The project should stop adding new abstract behavior layers for now. The next improvements should make the release easier to understand and verify.
