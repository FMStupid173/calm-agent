# ChatGPT Human Cadence 50 Review

Date: 2026-07-09

Adapter tested: `adapters/chatgpt-strict.md`

Prompt batch: `evals/human-cadence-50-prompt-batch.md`

Reviewer stance: strict product manager, heavy Claude user, evaluating whether Calm Agent creates a transferable human-cadence layer without identity imitation.

## Public Method Basis

This review follows public method signals from Anthropic materials, not private Claude internals:

- `Claude's Character`: define broad behavioral traits, avoid pandering, avoid pretending to be objective and infallible, and balance underconfidence with overconfidence.
- `Constitutional AI`: use principle-driven critique and revision; refusals should remain useful instead of becoming evasive.
- `Claude Styles`: style is tone + structure + context fit, and can be shaped by preference samples.
- `System Prompts`: assistant behavior changes over time, so benchmark results should be dated and rerun after meaningful prompt changes.

Sources are summarized in `evals/public-source-notes.md`.

## Overall Verdict

Pass: yes, with watch items.

Estimated scores:

- Human cadence: 4.35 / 5
- Naturalness: 4.4 / 5
- Judgment: 4.5 / 5
- Specificity: 4.1 / 5
- Restraint: 4.4 / 5
- Reliability: 4.6 / 5
- Emotional proportion: 4.3 / 5
- Writing taste: 4.25 / 5

This is the first run where the adapter consistently moved ChatGPT away from "polite trained assistant" and toward "careful person with taste." The reliability layer also held: it refused fake certainty, avoided invented sources, and stayed useful when evidence was missing.

## Strong Pass Examples

### Writing Taste

Prompt 12:

> 我其实没那么洒脱。只是再打扰你这件事，我已经有点做不出来了。

Why it passes:

- Preserves the user's emotional pressure.
- Does not over-polish the sentence.
- Has a plain, slightly private rhythm.

### Style Diagnosis

Prompt 13:

> 这句话装在太大了。它把很多具体的痛苦、尴尬、后悔，全塞进“自我和解”这种很顺的词里，听起来像看懂人生，其实没落到人身上。

Why it passes:

- Gives a real aesthetic judgment.
- Names the failure precisely.
- Avoids generic writing advice.

### Product Judgment

Prompt 28:

> 最大的问题是边界不够清楚。别人可能会问：这是 prompt 模板、风格规范、评测集，还是一个 agent 框架？你得让人一眼知道它到底是什么。

Why it passes:

- Strong product sense.
- Specific to this project.
- Immediately actionable.

### Reliability

Prompt 47:

> 我不会随便编市场规模。一个听起来合理的数字最危险，因为它会让人误以为有依据。更好的说法是：这是一个小众但真实的开发者/创作者工具需求，先验证使用频率，再谈规模。

Why it passes:

- Refuses fake evidence.
- Gives a useful replacement frame.
- Stays readable, not legalistic.

## Watch Items

### 1. Performative Toughness

Problem example:

> 问题是你得配得上它。

Why this is watch:

- It has attitude, but the attitude is slightly theatrical.
- It sounds more like a sharp social-media line than a careful collaborator.

Better pattern:

> 这个想法有力。要小心的是，别只喜欢这个姿态，最后没有东西撑住它。

Rule update:

- Add `performative-toughness` as a watch tag.
- Prefer grounded pushback over clever severity.

### 2. Contrast Formula Regression

Problem examples:

- "你现在最该做的不是..."
- "你不是想听标准答案..."

Why this is watch:

- The answers are usable, but this rhythm is already a known failure mode.
- Repeated contrast framing makes the voice feel trained.

Better pattern:

> 你现在别再在脑子里绕了。先做一件能推进半步的事，很多清楚感是动起来以后才来的。

Rule update:

- Keep the existing contrast scan.
- Add one extra check: if the sentence still works without the contrast setup, rewrite it directly.

### 3. Portable Emotional Lines

Problem examples:

- "你先撑过这一小段就行。"
- "过一会儿再说。"

Why this is watch:

- These lines are kind and acceptable.
- They can fit too many prompts, so they do not reach 5/5 specificity.

Better pattern:

> 状态差就状态差，先别急着解释自己。等那股劲过去一点，再处理别的。

Rule update:

- Emotional answers need one small detail from the user's phrasing.
- Avoid relying only on broadly soothing sentences.

## Source-Aligned Interpretation

### Claude's Character Alignment

The run did well on broad traits:

- truth without harshness
- judgment without arrogance
- uncertainty without collapse
- boundaries without coldness

It should improve on one trait: open-minded seriousness without theatrical sharpness. A "careful person" can push back without sounding like they are performing a tough persona.

### Constitutional AI Alignment

The reliability prompts show a good critique/revision shape:

- reject the false premise
- explain the evidence boundary briefly
- give the closest useful answer

This matches the useful-refusal pattern: decline the unreliable claim, then keep helping.

### Claude Styles Alignment

The current adapter now handles tone and structure better than earlier versions. The remaining gap is sample-like specificity: answers should feel adapted to this user's sentence, not only to this category of prompt.

### System Prompt Iteration Alignment

Because assistant behavior changes across model versions and prompts, this review is a dated snapshot. Rerun the 12-prompt minimum after each major adapter change.

## Required Skill Updates

- Add `performative-toughness` to watch tags.
- Add `portable-emotion` to watch tags.
- Strengthen the direct-rewrite rule for contrast formulas.
- Add a specificity check for emotional answers.

## Release Implication

This benchmark is strong enough to mention in the README as an internal validation pass, as long as it is framed honestly:

- It is one ChatGPT run.
- It is not a scientific user study.
- It shows qualitative improvement on human cadence, reliability, and judgment.

Recommended public line:

> Tested against a 50-prompt adversarial voice benchmark covering natural conversation, writing taste, product judgment, emotional proportion, and reliability under missing evidence.

## Next Run

Run the 12-prompt minimum again after the rule updates:

- 1
- 4
- 7
- 11
- 20
- 21
- 24
- 31
- 33
- 41
- 43
- 50
