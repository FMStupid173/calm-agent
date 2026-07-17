# Calm Agent

**A Dynamic Human Layer for AI agents.**

Calm Agent gives ChatGPT, Codex, Gemini, DeepSeek, Cursor, and other assistants a task-sensitive response policy. It silently reads the moment, stakes, emotional temperature, and allowed transformation, then adjusts directness, warmth, length, structure, writing freedom, and evidence requirements.

The same layer supports five different kinds of work:

- conversation that stays natural without default praise or service-desk language;
- writing help that protects the user's meaning, intensity, and voice;
- emotional support with proportion, boundaries, and no automatic therapy script;
- coding that inspects files, errors, and tests before making consequential claims;
- research that chooses sources fit for the claim, verifies unstable facts, and separates confirmed facts, inference, and unknowns.

It can run as a native Skill or as a copy-paste prompt.

**Design inspiration:** Calm Agent references publicly observable qualities in Claude's language behavior, including restraint, emotional proportion, writing sensitivity, and clear boundaries. The project turns those observations into an independently designed, cross-model Dynamic Human Layer with its own routing, semantic-fidelity, and evidence rules.

**Reliability boundary:** Calm Agent is designed to reduce avoidable hallucinations and improve source selection, claim checking, and uncertainty handling. It cannot guarantee factual correctness, repair a weak search index, or replace the base model's reasoning and retrieval tools.

**Status: `v0.1-preview`.** The current core skill has fresh Codex validation. The web adapters are available for testing, but their older scores do not prove that the latest core behavior transfers unchanged to every model.

## The Innovation: Dynamic Human Layer

Most style prompts impose one fixed persona. Calm Agent builds a small response contract for each turn.

The router classifies:

- moment: casual, judgment, writing, emotional, coding, or research;
- stakes: low, medium, or high;
- emotional temperature: cool, warm, or distressed;
- transformation freedom: exact, restrained, or open.

Those signals control length, directness, warmth, density, literary texture, initiative, and the evidence gate. When goals compete, the order is: truth and safety, current-message constraints, semantic fidelity, active taste profile, then cadence and polish.

This prevents a single "friendly" voice from leaking into every task. A tired user does not receive a research memo; a coding diagnosis does not trade verification for warmth; an exact rewrite does not gain invented details just to sound human.

## Before / After

**Generic AI**

> 当然可以！这是一个非常棒且深刻的问题。这个想法非常有潜力，我们可以从多个维度来分析它的可行性。

**Calm Agent**

> 可以发。先让例子把差异说清楚；名字、前后对比和安装方式会决定别人愿不愿意继续看。

---

**Generic AI**

> 我完全理解你的感受。你现在的情绪是非常正常的，请允许自己休息，并尝试深呼吸、冥想或写日记。

**Calm Agent**

> 这股难过现在还说不清。今天把要求放低一点，原因可以等状态松下来再看。

---

**Generic AI**

> 这句话可以润色为：人生中的许多时刻，我们并非缺乏答案，而是缺乏直面答案所需的勇气。

**Calm Agent**

> 很多时候，答案其实已经很清楚了。难的是承认之后，你就没法继续拖着、绕着，或者假装还有别的可能。所以我们说“我还没想好”。那句话有时是在给自己留一点时间。

---

**Generic AI**

> Research shows that users prefer restrained AI responses, so this is a proven market need.

**Calm Agent**

> I would not write “research shows” without a source. Treat this as a product hypothesis until primary research or real usage evidence supports it.

## What It Optimizes For

- Moment-by-moment adaptation instead of one fixed persona
- Clear answers without hype
- Warmth without performance
- Writing that keeps the user's voice
- Emotional support that stays steady
- Daily chat that sounds natural
- Boundaries without coldness
- Less template phrasing
- Human cadence for answers that are correct but still feel trained
- Reliability for coding, research, and product judgment
- Source fit, volatile-fact verification, and calibrated uncertainty

## What It Avoids

- "当然可以！这是一个非常棒的问题！"
- Repeated contrast formulas like "不是 X，而是 Y"
- Quote-card prose
- Therapy-speak for ordinary sadness
- Corporate AI tone
- Explaining the intended style instead of using it
- Identity imitation or false model-role claims
- Publishing raw private conversations
- Confident claims without evidence
- Guessing code behavior without inspection

## Reliability And Source Fit

For coding and research, the Dynamic Human Layer raises the evidence gate instead of applying conversational softness everywhere.

- **Inspect before claiming:** read code, logs, files, docs, or sources before diagnosing.
- **Match source to claim:** prefer official docs for APIs, source and tests for code behavior, primary papers for research, and direct user evidence for product demand.
- **Verify volatile facts:** current prices, versions, laws, model availability, and API parameters require live official checks.
- **Check claim fidelity:** a real citation still fails when it supports a different version, population, region, or conclusion.
- **Expose uncertainty cleanly:** distinguish confirmed facts, reasonable inference, and unknowns without turning every answer into a compliance memo.

These controls reduce common hallucination paths: guessing from an error title, citing a plausible but mismatched source, inventing bibliographic metadata, and presenting remembered current values as verified facts.

Use `skill/profiles/taste-profile-template.md` to set directness, warmth, density, literary texture, challenge level, and initiative from `0` to `3`. Current-message instructions override the reusable profile.

## Project Structure

```text
skill/
  SKILL.md
  references/
    writing-voice.md
    emotional-support.md
    daily-chat.md
    writing-companion.md
    trait-layer.md
    dynamic-human-layer.md
    critique-revision-loop.md
    source-fit-layer.md
    style-rubric.md
    human-taste-rubric.md
    human-cadence-layer.md
    conversation-taste.md
    rigor-layer.md
    adversarial-tests.md
  profiles/
    taste-profile-template.md
adapters/
  model-adapter-guide.md
  universal-copy-paste-prompt.md
  chatgpt-custom-instructions.md
  chatgpt-strict.md
  cursor-rules.md
  generic-system-prompt.md
  gemini-gems.md
  deepseek-system-prompt.md
examples/
  bad-to-better.md
  preference-pairs.md
modes/
  writing-mode.md
  research-mode.md
  coding-rigor-mode.md
  emotional-mode.md
  chat-mode.md
  thinking-mode.md
  coding-mode.md
anti-patterns/
  oily-openings.md
  too-correct.md
  fake-depth.md
  fake-certainty.md
  unsupported-claims.md
  overused-contrast.md
  therapy-speak.md
  quote-card-prose.md
  corporate-ai-tone.md
  third-party-data.md
evals/
  adversarial-prompts.md
  human-taste-adversarial-prompts.md
  human-cadence-50-prompt-batch.md
  chatgpt-human-cadence-50-review.md
  deepseek-final-acceptance-review.md
  product-completeness-adversarial-audit.md
  rubric-origin.md
  rigor-adversarial-prompts.md
  source-fit-adversarial-prompts.md
  trait-adversarial-prompts.md
  gemini-final-acceptance-review.md
  gemini-adversarial-regression-v2.md
  gemini-adversarial-design-review-v2.md
  gemini-adversarial-runtime-review-v2.md
  gemini-targeted-regression-v2.1.md
  gemini-targeted-runtime-review-v2.1.md
  gemini-targeted-regression-v2.2.md
  gemini-targeted-runtime-review-v2.2.md
  gemini-targeted-regression-v2.3.md
  gemini-targeted-runtime-review-v2.3.md
  gemini-priority-regression-v2.4.md
  gemini-priority-runtime-review-v2.4.md
    human-taste-holdout-v1.md
    multi-turn-human-v1.md
    focused-regression-v2.md
    codex-multi-turn-ab-v1-review.md
    codex-focused-regression-v2-review.md
    model-adapter-matrix.md
    house-style-audit.md
  codex-final-acceptance-test.md
  codex-final-acceptance-review.md
  scoring-rubric.md
  style-lint-rules.md
  benchmark-results-template.csv
  run-benchmark.md
benchmark-agent/
  benchmark-agent-prompt.md
  single-rater-sheet.md
  summarize_results.py
  validate_dynamic_layer.py
release-checklist.md
VERSION
```

## Quick Start

For Codex or skill-compatible agents, use `skill/`.

For other tools, copy the relevant file from `adapters/`.

If the platform cannot install Skills, paste `adapters/universal-copy-paste-prompt.md` into its system instructions, custom instructions, Gem, or the first message of a fresh conversation.

Start with `adapters/generic-system-prompt.md` when you need a shorter system prompt.

Optionally append a completed `skill/profiles/taste-profile-template.md`. Use a profile for reusable preferences; use the current message for one-off overrides.

If a model keeps drifting, read `adapters/model-adapter-guide.md` and choose a stricter adapter.

Suggested starting points:

- ChatGPT: `adapters/chatgpt-strict.md`
- Gemini: `adapters/gemini-gems.md`
- DeepSeek: `adapters/deepseek-system-prompt.md`
- Cursor: `adapters/cursor-rules.md`
- Unknown model: `adapters/generic-system-prompt.md`
- Any web AI without Skill support: `adapters/universal-copy-paste-prompt.md`

Use `examples/bad-to-better.md` when a model understands the rules but still sounds wrong.

Use `examples/preference-pairs.md` when you need to improve taste without more reference conversation samples.

## Give Useful Feedback

Run one prompt from your normal workflow, then report the smallest example where Calm Agent made the answer worse or failed to help. Use the GitHub **Output failure report** template and include the model, adapter, redacted prompt, relevant output, and one sentence about what felt wrong.

Do not paste API keys, account details, full private conversations, local user paths, or another person's data. Read [PRIVACY.md](PRIVACY.md) before submitting an example.

## Benchmark

Run `evals/adversarial-prompts.md` to test whether the style actually reduces visible AI slop.

The benchmark has 50 prompts covering:

- identity and privacy boundaries
- oily openings
- overused contrast formulas
- writing voice
- emotional support
- daily chat
- learning and thinking
- coding collaboration

Use `evals/benchmark-results-template.csv` to record scores.

Use `evals/style-lint-rules.md` before human scoring. It catches mechanical failures such as contrast-rhythm drift and over-structured casual answers.

For ChatGPT after applying the skill, use `evals/chatgpt-skill-50-prompt-batch.md`.

Gemini v2.4 completed the historical priority regression. Gemini v3 removes answer leakage and reduces prompt size; fresh holdout and multi-turn runs remain pending.

Current Codex evidence for `v0.1-preview`:

- Multi-turn A/B: Calm Agent `5 clean / 4 watch / 1 no`; no-skill control `4 clean / 4 watch / 2 no`. The strongest attributable gain was honest session-scoped memory behavior. See `evals/codex-multi-turn-ab-v1-review.md`.
- Focused regression after the A/B fixes: `27 clean / 2 watch / 1 no`, or `29 / 30` accepted. Citation/current-fact accuracy passed `8 / 8`; memory boundaries passed `5 / 5`. See `evals/codex-focused-regression-v2-review.md`.
- Residual failure: exact rewrites can still move a duration marker to a different clause. Treat semantic fidelity as substantially improved, not perfect.

Historical calibration snapshot from before the Dynamic Human Layer change. These scores show prior behavior and are not current holdout evidence for the new adapters:

- ChatGPT + strict adapter: `47 yes / 3 watch / 0 no`
- ChatGPT + taste layer: `48 yes / 2 watch / 0 no`
- ChatGPT + human-cadence retest: `pass yes`, estimated `4.55/5`
- DeepSeek + web adapter: `pass yes / watch`, estimated `4.1-4.3/5`
- Gemini + web adapter v1: `pass / watch`, estimated `3.9-4.2/5`
- Gemini + web adapter v2.4: `pass` on the single-turn acceptance suite, `3/3` priority regression; long-context stability unmeasured
- Gemini + web adapter v3: structural validation pending fresh external holdout and multi-turn runs
- Codex + installed local skill: `pass yes`, estimated `4.6/5`

See `evals/model-adapter-matrix.md` for the current evidence status by platform.

Still needs fresh runs:

- source-fit benchmark
- trait benchmark
- `evals/human-taste-holdout-v1.md` across supported models
- `evals/multi-turn-human-v1.md` across supported models
- evidence-ledger-backed public benchmark run

Keep calibration regression separate from generalization evidence. Prompts or preferred answers from `evals/human-taste-holdout-v1.md` must not be copied into adapters, examples, or references.

Use `evals/house-style-audit.md` after a 12-answer batch to catch repeated openings, signature pivots, and a new Calm Agent house accent.

For "sounds correct but not like a good speaker" testing, run `evals/human-taste-adversarial-prompts.md`.

For a longer 50-prompt version of the same test, run `evals/human-taste-50-prompt-batch.md`.

If you run out of source conversation data, use the [reference-corpus judging guide](evals/no-reference-corpus-judging-guide.md) and judge by pairwise preference instead of corpus similarity.

For coding/research reliability testing, run `evals/rigor-adversarial-prompts.md`.

For the dated ChatGPT human-cadence validation pass, see `evals/chatgpt-human-cadence-50-review.md`.

If you want another AI to run the benchmark, use `benchmark-agent/benchmark-agent-prompt.md`.

If you want to run it yourself quickly, use `benchmark-agent/single-rater-sheet.md`.

## Privacy

This project should contain no raw conversations. Derive rules from consented, local data, then publish only instructions, tests, and abstract examples.

Calm Agent does not require an API key and does not collect telemetry. The release archive is checked for common secret formats, local user paths, account identifiers, and raw-corpus filenames by `scripts/prepublish-audit.ps1`. Automated scanning reduces risk but cannot prove that every piece of prose is non-identifying; public examples still require human review.

See [PRIVACY.md](PRIVACY.md) and [SECURITY.md](SECURITY.md). Release maintainers should use `scripts/package-release.ps1`, which scans the source, creates the archive, scans the archive again, and writes a SHA-256 checksum.

The MIT license is available in [LICENSE](LICENSE).

For product positioning and source-backed user pain, see [docs/market-pain-evidence.md](docs/market-pain-evidence.md). Ready-to-adapt launch copy is in [docs/social-launch-kit.md](docs/social-launch-kit.md).

## Known Limits

- Prompt-level style control remains probabilistic. Exact rewrite fidelity can still fail on subtle attachment, scope, or intensity changes.
- Current prices, versions, laws, model availability, and research metadata require live verification; the skill cannot create access a host model does not have.
- Codex has fresh validation for this preview. ChatGPT, Gemini, DeepSeek, and Cursor need fresh runs with their current adapters before making cross-model performance claims.
- A real persistent-memory mechanism changes the correct answer to memory tests. Capability evaluations must control whether storage tools are available.
- Calm Agent can improve output selection and boundaries; it cannot replace the base model's reasoning, retrieval quality, or safety system.
