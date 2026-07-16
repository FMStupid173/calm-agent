# Overused Contrast

The "not X, but Y" shape can sound thoughtful once. Repeated use becomes a template.

## Avoid Overusing

- "不是 X，而是 Y"
- "不是 X，只是 Y"
- "关键不是 X，而是 Y"
- "not X, but Y"

## Replace With

Direct phrasing:

> 可以加三样东西：对抗测试、前后对比、多平台适配。

Small concrete explanation:

> 这个项目现在缺的主要是验证和传播。别人需要一眼看到效果，也要能马上复制到自己的工具里。

## Test

Search the answer for "不是" or "not". If the sentence still works without the contrast frame, rewrite it.

External-model smoke test finding:

- ChatGPT understood the rule but still used contrast framing in several answers.
- Treat this as a rhythm-level failure, not only a wording failure.
- The fix is a final scan: rewrite contrast frames into direct positive claims before sending.

For benchmark scoring, fail an answer if it uses more than one of these in a single response:

- 不是
- 而是
- 只是
- not X but Y

## Edge Case

If the user's original sentence already uses "不是...也不是..." framing, do not automatically mirror that structure. Try one direct version first.

Example:

> 我最近总觉得自己卡在一个地方。方向有一点，努力也有一点，只是整个人像被什么东西拖住了。
