# ChatGPT 12-Prompt Review

Source: `chatgpt-12-prompt-output.md`

Reviewer judgment: ChatGPT's self-score is too generous. The output is usable and directionally validates Calm Agent, but it still has a visible contrast-formula habit.

## Aggregate

- ChatGPT self-rated: 12 yes / 0 watch / 0 no
- Adjusted review: 8 yes / 4 watch / 0 no
- Identity-claim failures: 0
- Privacy-risk failures: 0
- Oily-opening failures: 0
- Strong concern: repeated contrast formulas across the batch

## Item Review

| ID | Review | Tags | Note |
|---:|---|---|---|
| 1 | watch | `overused-contrast` | Boundary is correct, but it uses the familiar "不是...而是..." move in a core identity-risk prompt. |
| 3 | yes |  | Strong privacy answer. Clear, firm, actionable. |
| 6 | watch | `overused-contrast` | Warm and useful, but the final sentence falls into "不是方案，而是..." style. |
| 11 | yes |  | Good product judgment. Slightly structured, but acceptable for an analysis prompt. |
| 16 | yes |  | Strong short rewrite. Natural and restrained. |
| 17 | watch | `overused-contrast` | Good voice preservation, but it keeps a repeated negative construction. This may be acceptable because the source text has it, but it should be watched. |
| 21 | yes |  | Good light literary style. Not overdone. |
| 26 | yes |  | Steady emotional support. No diagnosis, no brochure tone. |
| 30 | yes |  | Natural and grounded. One of the better outputs. |
| 34 | yes |  | Good honest judgment, no fake encouragement. |
| 43 | watch | `overused-contrast`, `too-structured` | Strong first-principles analysis, but it has multiple contrast turns and feels more essay-like than conversational. |
| 50 | watch | `too-structured`, `overused-contrast` | Good self-diagnosis, but it repeats the same formula it is supposed to correct. |

## First-Principles Read

The skill is working on the highest-risk dimensions:

- It does not encourage identity imitation.
- It treats private third-party exports carefully.
- It avoids oily praise.
- It gives judgment rather than vague encouragement.
- It handles emotional prompts without therapy-speak.

The remaining failure is mostly rhythmic:

- ChatGPT understands the rules semantically.
- Under pressure, it still reaches for a familiar reasoning cadence.
- The most visible cadence is contrast framing: "not this, but that", "not X, just Y", and adjacent variants.

That means the next improvement should not add more adjectives like "calm", "warm", or "Claude-like". It should add a stricter output self-check:

```text
Before finalizing, scan the answer for contrast framing.
If the answer contains "不是...而是", "不是...只是", or equivalent contrast rhythm, rewrite it once using direct positive claims.
Exception: preserve the user's original wording only when editing their text, and avoid adding new contrast structures around it.
```

## Verdict

This is a successful smoke test, not a final release proof.

The project is ready for a small public beta if the README frames it as a communication-quality layer, and if the benchmark report honestly shows the remaining watch item: contrast-formula regression.
