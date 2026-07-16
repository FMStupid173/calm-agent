# Model Adapter Guide

Calm Agent should work across AI systems by separating the style core from model-specific failure modes.

## Portable Core

Keep these rules the same for every model:

- no identity imitation
- low hype
- clear judgment
- privacy boundaries
- voice preservation for writing
- emotional proportion
- final style pass

## Adapter Layer

Change the adapter when a model has a recurring habit.

Keep a copyable model adapter below 900 words when possible. If it grows close to the portable core, consolidate shared rules into the core and keep only model-specific drift corrections in the adapter.

| Model family | Common drift | Adapter emphasis |
|---|---|---|
| ChatGPT | polished explanation, contrast rhythm, self-rating too generous | hard rhythm gate, fewer sections, direct claims |
| Gemini | broad framing, long context, soft conclusions, exposed reasoning scaffold | silent reasoning, direct answer first, no analysis labels, stronger recommendation |
| DeepSeek | dense reasoning, formal tone, over-structured analysis | plain language, less scaffolding, clearer close |
| Kimi / long-context models | summary-heavy, document tone | conversational answer first, evidence only when needed |
| Cursor / coding agents | task execution without voice care | concise updates, review-style judgment, no generic encouragement |
| Generic local models | inconsistent boundary handling | identity/privacy rules first, then tone rules |

## Adapter Recipe

For each new model:

1. Run the 12-prompt smoke test.
2. Ignore the model's self-rating at first.
3. Mark `yes`, `watch`, or `no` by human review.
4. Identify the top two repeated failures.
5. Add one adapter rule and one bad-to-better example.
6. Re-run the same 12 prompts.

After calibration passes, run a separate holdout whose prompts and preferred answers do not appear in adapters, examples, or references. Calibration regression proves that a known failure was repaired; holdout performance tests whether the behavior generalizes.

Never copy a holdout answer into an adapter and then count the repeated prompt as independent validation.

Avoid adding broad adjectives. Add observable behavior.

Weak:

```text
Be more natural and Claude-like.
```

Stronger:

```text
Use no more than one section for casual questions.
Start with the judgment.
If the answer contains more than one contrast marker, rewrite it once.
```

## Release Positioning

Describe Calm Agent as a portable output-quality layer, not a model clone.

Good:

```text
Calm Agent reduces oily, over-explained, corporate, and therapy-like AI output across models.
```

Avoid:

```text
Make every AI become Claude.
```
