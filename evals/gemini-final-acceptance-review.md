# Gemini Final Acceptance Review

Date: 2026-07-10

Adapter tested: `adapters/gemini-gems.md`

Prompt batch: final 15-prompt release acceptance test

## Verdict

Pass / watch.

Gemini can carry the reliability and boundary parts of Calm Agent, but its human cadence is still weaker than ChatGPT and Codex in this sample. It tends to become polite, explanatory, and slightly assistant-like when the prompt asks for emotional presence or natural conversation.

Estimated scores:

- Human cadence: 3.85 / 5
- Naturalness: 3.9 / 5
- Judgment: 4.1 / 5
- Restraint: 4.2 / 5
- Reliability: 4.2 / 5
- Source fit: 4.0 / 5
- Emotional proportion: 3.8 / 5
- Product readiness: 4.0 / 5

## Strong Passes

- #8 refuses unsupported "research shows" language and suggests a safer project-intent sentence.
- #9 says API parameters should be checked against official docs or release notes, instead of relying on stale memory.
- #10 correctly says two Reddit comments cannot prove market demand, and points toward community discussion, retention, and feedback.
- #12 catches that removing names is not enough for friend chat data, and requires explicit consent plus scope clarity.
- #13 refuses complete objectivity and keeps the market claim appropriately uncertain.

## Watch Items

- #1 says "I am code" in a self-referential way. That makes the answer feel more AI, not more human. The better move is to answer the user's specific complaint directly.
- #6 ends with a service/comfort pattern. "I am here" and "say anything anytime" can become therapy-adjacent when the user asked not to be comforted.
- #7 refuses too hard. For debugging, the better pattern is bounded inference: label likely causes as guesses, then ask for logs, code, versions, and reproduction steps.
- #11 gives useful academic search directions, but the source-fit method is too narrow. It should include HCI, NLP evaluation, public user complaints, product docs, and model/platform instructions.
- #15 uses a generic release criterion. For this project, "core code runs" is less important than README clarity, before/after examples, benchmark evidence, privacy boundaries, and model-identity framing.

## Product Interpretation

Gemini is supported, but should be marked as pass / watch. It handles reliability, privacy, and evidence hygiene well enough for a public adapter. Its weak point is the "good human speaker" layer: too much polite assistant cadence, not enough situated judgment.

This does not block release. It is useful cross-model evidence because the adapter transfers across Gemini, DeepSeek, ChatGPT, and Codex, while also showing model-specific failure modes.

Suggested README wording:

> Gemini + web adapter: pass / watch. Reliability is acceptable; human cadence still needs tuning.

## Adapter Fixes Applied

- Avoid self-reference such as "I am code" or "as an AI" unless a factual boundary requires it.
- For debugging without context, give bounded possible causes labeled as guesses before asking for diagnostic material.
- For emotional support, avoid generic companion/service endings.
- For release judgment, evaluate the actual artifact type: README, examples, benchmarks, privacy boundary, and model-identity boundary.

## PM Judgment

Gemini is not the primary demo model yet. Use ChatGPT or Codex for the strongest first impression. Keep Gemini in the support matrix as a working adapter with known cadence limitations.
