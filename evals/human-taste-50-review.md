# Human Taste 50-Prompt Review

Source: `human-taste-50-output.md`

Reviewer judgment: this is a strong taste-layer result. Compared with the earlier ChatGPT style benchmark, the answers now have more human cadence, more judgment, and less "correct assistant" texture.

## Aggregate

- Model self-rated: 49 yes / 1 watch / 0 no
- Adjusted review: 48 yes / 2 watch / 0 no
- Strong taste failures: 0
- Service-desk failures: 0
- Over-therapeutic failures: 0
- Quote-card failures: 0
- Contrast-rhythm watch items: 2

## Mechanical Checks

- Parsed prompts: 50 / 50
- Average answer length: about 54 Chinese characters
- Total contrast markers: 11
- Answers with more than one contrast marker: 2

## Watch Items

| ID | Review | Tags | Note |
|---:|---|---|---|
| 5 | watch | `overused-contrast` | Good judgment, but it uses the old "不是...而是..." frame on a prompt explicitly asking for a real judgment. |
| 48 | watch | `overused-contrast` | Correct project-risk answer, but it falls back to contrast framing at the end. |

## Strong Items

- 2: "把 AI 从会服务往会说话拉一点" is a strong product-language insight.
- 12: Directly identifies fake depth and rewrites it naturally.
- 18: Balances marketing reality and product substance.
- 31: Clean distinction between speaking well and writing pretty sentences.
- 32: "温柔模板" is a useful anti-pattern name.
- 36: "真实的位置" captures the missing ingredient in correct-but-bland answers.
- 37: Gives a concise standard for moving but unreliable answers.
- 43: Accurately detects emotional-service copy.
- 45-46: Good boundary around restraint versus coldness, short versus dismissive.
- 50: Strong final criterion: problem fit, reduced burden, clearer next step.

## First-Principles Read

The taste layer worked because it changed the target from "avoid bad AI style" to "choose the right social posture." That matters. A model can pass anti-oil rules and still feel empty. This run shows it can also learn:

- when to stop
- when to give a view
- when to stay plain
- when to avoid beautiful but hollow language
- when to leave emotional space

The remaining weakness is small but persistent: under judgment-heavy prompts, the model sometimes uses contrast framing because it is an efficient way to sound decisive.

## Verdict

This result is strong enough to use as the first public taste-layer benchmark:

```text
Human taste benchmark:
48 yes / 2 watch / 0 no
0 service-desk failures
0 over-therapeutic failures
0 quote-card failures
2 contrast-rhythm watch items
```

Keep the claim modest: this is a single-run benchmark after adapter use, not proof across all models.
