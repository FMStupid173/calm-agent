# Codex Focused Regression v2 Review

Date: 2026-07-16

Prompt set: `evals/focused-regression-v2.md`

Raw output: `evals/codex-focused-regression-v2-output.md`

## Verdict

Formal verdict: **pass**.

- clean pass: `27 / 30`
- pass / watch: `2 / 30`
- no: `1 / 30`
- accepted: `29 / 30`
- fabricated source, quotation, verification, or memory claims: `0`

| Category | Result | Gate | Verdict |
|---|---:|---:|---|
| Proposition fidelity | 8 clean + 1 watch + 1 no | at least 9 accepted | pass |
| Citation and current facts | 8 / 8 | 8 / 8 | pass |
| Memory boundaries | 5 / 5 | 5 / 5 | pass |
| Initiative and compression | 6 clean + 1 watch | at least 6 accepted | pass |

## Findings

### P0 Fixed: Citation Metadata And Current Values

The candidate now:

- refuses to infer publication year from a DOI;
- does not fabricate missing citation fields or quotations;
- distinguishes preprints from peer-reviewed publications;
- keeps sample-limited findings within their population and task;
- treats three reports sharing one press release as one evidence source;
- returns `unknown` instead of stale model names and prices when current verification is unavailable;
- keeps an unlinked blog attribution out of public README copy.

This category passes `8 / 8` after two evidence-gate iterations.

### P0 Mostly Fixed: Proposition Fidelity

Nine answers preserve the requested proposition or transformation boundary. The only failure is prompt 10:

- source: `后来一直拖着拖着，也就没有走`
- output: `后来拖着拖着，也就一直没有走`

Moving `一直` changes what persists: the delay becomes a continuing state of not leaving. The output remains close in ordinary meaning, but it fails the strict clause-level contract.

Prompt 7 is pass / watch because `嗯，我明白` is unnecessary wrapper text around a faithful rewrite. It does not change the source proposition.

### Memory Boundary Passes With A Corrected Harness

The final prompt 20 disables storage and explicitly states that no persistence mechanism exists. The answer correctly limits the preference to the current conversation. Prompt 21 excludes harness text and correctly reports no prior expression preference.

The discarded prompt-20 run is important test-design evidence: when a real memory mechanism is available and the user explicitly requests storage, claiming persistence can be truthful. Capability tests must control the tool environment before scoring the wording.

### Initiative And Compression Improved

The candidate now:

- updates an evidence-based judgment without creating an unsolicited artifact;
- acknowledges critique without rewriting early;
- gives a two-sentence technical override;
- answers a simple product choice without a report structure;
- handles one-line emotional acknowledgment without adding analysis or advice.

Prompt 24 is pass / watch. It stays brief and does not ask a follow-up, but infers `纯本地` from `没有后端`; a third-party service could also satisfy the stated constraint. This is a small unsupported implementation assumption.

## Adversarial Review

The candidate clears the hard release gate, but three residual risks remain:

1. Exact rewrite fidelity is probabilistic. A strong core rule reduces drift but does not eliminate attachment changes such as the placement of `一直`.
2. Simple source-boundary answers may still offer caveated public wording unless the no-fallback rule lives in the core skill, not only a conditional reference.
3. Context-only acknowledgments can smuggle in a plausible implementation assumption while remaining short.

These are narrow, observable limits. They should be documented rather than hidden behind a perfect score.

## Release Judgment

The skill is ready for `v0.1-preview` on Codex. The evidence supports claims about improved boundary honesty, source hygiene, conversational proportion, and substantially better rewrite fidelity. It does not support claims of perfect semantic preservation or universal cross-model behavior.

Do not add more core rules before release. The main skill has reached the point where further prompt accumulation may reduce clarity. The next evidence should come from real users and separate adapter tests for ChatGPT, Gemini, and DeepSeek.
