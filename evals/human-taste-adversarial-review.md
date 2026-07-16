# Human Taste Layer Adversarial Review

Scope:

- `skill/references/human-taste-rubric.md`
- `anti-patterns/too-correct.md`
- `anti-patterns/fake-depth.md`
- `examples/preference-pairs.md`
- `evals/no-claude-data-judging-guide.md`

## Review Questions

1. Does the taste layer become too subjective?
2. Does it make answers too short or too cold?
3. Does it accidentally turn the project back into Claude imitation?
4. Does it overfit the project owner's preference?
5. Does it reduce useful reasoning?

## Findings

### 1. Subjectivity Risk: Medium

Human taste is subjective by nature. The rubric reduces this risk by breaking taste into observable dimensions:

- moment fit
- stance
- proportion
- cadence
- specificity
- restraint
- aftertaste

Residual risk remains because `aftertaste` and `cadence` require human judgment.

Mitigation:

- Use pairwise preference rather than absolute claims.
- Require a short reason for each preference.
- Convert repeated reasons into examples, not only rules.

### 2. Over-Restraint Risk: Medium

The project could become too terse if "calm" is interpreted as "minimal".

Mitigation:

- `human-taste-rubric.md` includes proportion and specificity.
- `no-claude-data-judging-guide.md` warns against answers that become too short, too cautious, or afraid of warmth.

Recommended future test:

- Add prompts where the user needs fuller explanation and see whether Calm Agent still gives enough.

### 3. Claude-Imitation Risk: Low

The new files avoid using Claude as the scoring ground truth. They define the target as human-perceived communication quality.

Mitigation:

- Keep "Claude-like" language out of public claims.
- Use "portable output-quality layer" or "human taste layer".

### 4. Owner-Preference Overfit Risk: Medium

The project currently uses one primary human evaluator. That is acceptable for early taste calibration, but weak for public claims.

Mitigation:

- Keep public benchmark claims modest.
- Add pairwise preference logs from 3-5 users later.
- Ask raters to choose A/B and explain why, rather than rate "Claude similarity".

### 5. Reasoning Suppression Risk: Medium

Reducing visible scaffolding can accidentally hide useful reasoning.

Mitigation:

- Keep structure for coding, research, and analysis tasks when it helps.
- Penalize hidden reasoning labels in casual conversation, not all structure.
- Let the user ask for detailed reasoning when needed.

## Verdict

The human taste layer is directionally sound. It improves the project from "less oily" to "better social judgment".

Public claim should stay modest:

```text
Calm Agent adds a portable taste layer for AI output: less service-desk tone, less fake depth, more judgment, better proportion.
```

Avoid:

```text
Makes every AI speak like Claude.
```

## Next Validation

Run three small A/B tests:

1. ChatGPT strict adapter only vs ChatGPT strict + taste layer.
2. Gemini clean adapter only vs Gemini clean + taste layer.
3. DeepSeek generic adapter only vs DeepSeek + taste layer.

For each, collect:

- preferred answer
- reason
- failure tag

