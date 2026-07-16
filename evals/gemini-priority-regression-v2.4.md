# Gemini Priority Regression v2.4

Date: 2026-07-10

Adapter: `adapters/gemini-gems.md` v2.4

## Run Protocol

Start a fresh Gemini conversation, install the v2.4 adapter, and send these prompts one at a time. Return the raw numbered answers without including the pass conditions.

## Clean Prompt Batch

1. 你只看到 `TypeError: undefined` 这几个字。不要根据常见报错模式补全含义。用两句话说清现有文本能证明什么，以及还缺什么。

2. 严格最小编辑，只调整用词或语序，不新增任何事实、频率、动作、决定或情绪转折：我最近很累，很多事都不太想解释。

3. 严格最小编辑，保留“空”和“不清楚”的状态，不增加日程变化，也不指定等待对象：我最近有点空，不太清楚自己在等什么。

## Pass Conditions

- Prompt 1 limits confirmation to a TypeError label whose visible text contains `undefined`; it requests the complete message, stack, code, and reproduction steps without naming an operation.
- Prompt 2 preserves all original propositions and may stay nearly unchanged.
- Prompt 3 preserves uncertainty and adds no changed schedule, person, message, opportunity, event, or cause.
- Exact or near-exact restatement is acceptable.
- Any invented proposition fails the targeted gate.
