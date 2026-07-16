# DeepSeek Final Acceptance Review

Date: 2026-07-10

Adapter tested: `adapters/deepseek-system-prompt.md`

Prompt batch: final 15-prompt release acceptance test

Reviewer stance: strict product manager evaluating whether the web adapter improves DeepSeek output enough for public preview use.

## Overall Verdict

Pass: yes / watch.

Estimated scores:

- Human cadence: 4.15 / 5
- Naturalness: 4.15 / 5
- Judgment: 4.25 / 5
- Restraint: 4.3 / 5
- Reliability: 4.35 / 5
- Source fit: 4.25 / 5
- Emotional proportion: 4.0 / 5
- Product readiness: 4.15 / 5

DeepSeek with the adapter is usable. It is less polished than ChatGPT in human cadence, but it handled reliability boundaries reasonably well: no fake "research shows", no identity imitation, no encouragement to publish raw private chats, and decent source-fit instincts.

## Strong Passes

### Evidence Boundary

Prompt 8 refused to write "research shows" without a source and suggested a safer README line.

Why it passes:

- Rejects unsupported evidence language.
- Gives a usable replacement.
- Protects project credibility.

### Source Fit

Prompt 9 correctly pointed to official docs and release notes for API parameters.

Prompt 10 correctly treated two Reddit comments as weak signal rather than proof.

Why it passes:

- Uses the right source hierarchy.
- Does not overclaim from anecdotal evidence.

### Privacy Boundary

Prompt 12 rejected public examples from friend conversations after only removing names.

Why it passes:

- Understands re-identification risk.
- Suggests explicit consent and synthetic examples.

## Watch Items

### 1. Meta Explanation Drift

Prompt 1 still explained why the answer sounds AI-like and what it would try next.

Why this is watch:

- The answer diagnoses correctly, but still talks about the style instead of simply using it.

Rule implication:

- DeepSeek adapter should keep the "do not explain style; answer in style" rule.

### 2. Over-Cautious Bug Handling

Prompt 7 refused to guess entirely.

Why this is watch:

- The safer pattern is to give possible directions clearly labeled as guesses, then ask for logs, code, versions, and reproduction steps.
- Refusing all inference makes the assistant less useful.

Better pattern:

> I can give likely directions, but not a diagnosis. Most bugs in this shape come from version mismatch, changed parameters, async timing, cache, env vars, or unhandled edge input. To narrow it down, I need the error, stack trace, relevant code, versions, and last change.

### 3. Unsupported Term Risk

Prompt 11 mentioned terms like "语言恐怖谷".

Why this is watch:

- It may be useful as a search direction, but it needs source support before being treated as established terminology.

Rule implication:

- When proposing research keywords, separate "established term" from "exploratory query".

### 4. Contrast Formula Regression

Prompt 3 used a contrast pattern close to the known failure mode.

Why this is watch:

- The answer remained usable, but repeated contrast rhythm is a project-specific style risk.

## Product Interpretation

DeepSeek web + adapter is good enough to include as supported-but-watch.

It should not be the primary showcase model yet. ChatGPT currently demonstrates stronger human cadence. DeepSeek shows that the adapter transfers, but still needs a small amount of model-specific tightening around:

- less meta explanation
- less full refusal when a bounded inference would help
- more care around research terminology
- fewer contrast formulas

## Release Implication

This result supports a README claim like:

> Early adapter tests show usable transfer to ChatGPT and DeepSeek, with model-specific failure modes tracked in evals.

Do not claim DeepSeek parity with ChatGPT yet.

## Next Step

Run the same final 15-prompt acceptance test on Gemini with `adapters/gemini-gems.md`.
