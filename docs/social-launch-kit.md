# Social Launch Kit

Repository: `https://github.com/FMStupid173/calm-agent`. Use one strong before/after pair from the README with every visual post.

## Core Message

**Chinese**

> 一套跨模型的动态人味层：根据聊天、写作、情绪、coding 和 research，动态调整表达、语义保真与证据门槛。

**English**

> A portable Dynamic Human Layer that adapts voice, semantic fidelity, and evidence requirements to each task.

## GitHub

**Description**

> Dynamic Human Layer for adaptive voice, semantic fidelity, and evidence-aware AI responses.

**Topics**

`llm`, `prompt-engineering`, `codex-skills`, `chatgpt`, `gemini`, `deepseek`, `human-ai-interaction`, `ai-writing`, `evaluation`, `ai-agents`

**Release title**

> Calm Agent v0.1 Preview

**Release body**

> Public preview of Calm Agent, a portable Dynamic Human Layer for AI assistants.
>
> It routes every turn by moment, stakes, emotional temperature, and transformation freedom, then adapts voice, structure, semantic fidelity, and evidence requirements. The package includes a Codex skill, a universal copy-paste prompt, model adapters, adversarial prompts, and benchmark tooling.
>
> For coding and research, inspect-before-claiming, source-fit checks, volatile-fact verification, and uncertainty boundaries are designed to reduce avoidable hallucinations. They do not guarantee correctness or replace retrieval.
>
> Preview 3 adds Calibration Copilot: DeepSeek can run through its API, while ChatGPT/Gemini web outputs can be imported for failure profiling, holdout validation, and human-approved adapter suggestions. The code is locally validated; live cross-model calibration evidence is still pending.
>
> Current evidence: the Codex-focused regression accepted 29/30 cases. Cross-model adapters remain previews and need fresh real-user runs.
>
> The most useful contribution is a minimal redacted failure example from a real workflow. Please use the Output failure report template and never post credentials or private conversations.

## V2EX 分享创造

**Title**

> 我给 AI 做了一个会按场景调整人味和严谨度的开源 Skill

**Body**

> 我经常遇到一种情况：AI 的答案大体正确，但开头先夸一句，中间列一排标题，结尾再总结一次。让它润色文字时，句子变顺了，原来的声音也没了；做 coding 和 research 时，它又可能把猜测说得很确定。
>
> 我把这些问题整理成了 Calm Agent。它的核心是 Dynamic Human Layer：先判断当前属于聊天、写作、情绪、coding 还是 research，再生成这一轮的回答契约。
>
> - 聊天：控制结构和客服腔，让交流自然一点；
> - 写作：锁住原意、强度和个人声音；
> - 情绪：按状态调整温度与建议分量；
> - coding：先看代码、日志和测试，再判断；
> - research：选对来源，核验易变事实，区分已确认、推断和未知。
>
> 这些可靠性规则能减少一部分可避免的幻觉，也能改善搜索资料与问题的匹配度。它不能保证永远正确，底层模型没有搜索能力时也不会凭空获得搜索能力。
>
> Codex 版本刚完成一轮 30 题回归，29 题通过或可接受。ChatGPT、Gemini、DeepSeek adapter 仍是 preview，我想拿真实使用来继续校准。
>
> 项目：https://github.com/FMStupid173/calm-agent
>
> 我现在更需要失败样本。拿一条你平时真的会问的问题跑一下，告诉我它哪里仍然很 AI，或者哪里被这个 Skill 改坏了。请先删掉隐私和账号信息。

## Show HN

**Title**

> Show HN: Calm Agent - a Dynamic Human Layer for adaptive, evidence-aware AI responses

**Body**

> I built Calm Agent around a Dynamic Human Layer: a small response contract generated for each turn from the moment, stakes, emotional temperature, and allowed transformation.
>
> Conversation stays light, writing preserves voice, emotional support keeps proportion, coding inspects before claiming, and research raises the evidence gate. Source-fit checks and volatile-fact verification are designed to reduce avoidable hallucinations without claiming guaranteed correctness.
>
> The current Codex regression accepted 29/30 cases. The ChatGPT, Gemini, DeepSeek, and Cursor adapters are previews; I am explicitly not treating old scores as current cross-model proof.
>
> Repo: https://github.com/FMStupid173/calm-agent
>
> The feedback I need most: run one prompt from your real workflow and report the smallest redacted case where the adapter made the answer worse.

## Reddit: r/ChatGPT or Prompt Communities

Check the community rules before posting. Lead with the observed problem and invite testing; avoid dropping only a link.

**Title**

> I built a Dynamic Human Layer that changes voice and evidence rules by task

**Body**

> I kept rewriting the same custom instructions: stop praising every idea, stop turning simple answers into five sections, preserve my wording when editing, and verify current facts instead of adding a confident disclaimer.
>
> I turned that into Calm Agent: a portable Dynamic Human Layer for ChatGPT, Codex, Gemini, DeepSeek, and Cursor. It routes each turn as conversation, judgment, writing, emotional support, coding, or research, then adjusts tone, structure, transformation freedom, and the evidence gate.
>
> It includes semantic-fidelity rules for writing and inspect-before-claiming, source-fit, current-fact verification, and uncertainty rules for coding and research. These controls reduce avoidable hallucination paths; they do not guarantee factual correctness.
>
> https://github.com/FMStupid173/calm-agent
>
> I would rather collect failures than compliments. What is one prompt where this still sounds obviously AI, becomes too cold, or loses useful detail?

## Reddit: r/ClaudeAI

**Title**

> Which parts of Claude's interaction style are actually portable across models?

**Body**

> I like Claude's restraint, writing support, and willingness to hold a boundary without turning the answer into policy copy. I tried to describe those as portable behaviors instead of asking other models to pretend they are Claude.
>
> The result is Calm Agent: rules and evals for judgment, emotional proportion, semantic fidelity, human cadence, and evidence hygiene. It currently has adapters for several model surfaces.
>
> https://github.com/FMStupid173/calm-agent
>
> I am looking for counterexamples. Which behavior still depends on the base model, and which rule transfers well?

## X

> I built a Dynamic Human Layer for AI: it changes voice, writing freedom, and evidence requirements according to the current task.
>
> Conversation stays natural. Writing keeps the user's voice. Coding and research inspect, verify, and choose sources that fit before claiming.
>
> Codex regression: 29/30 accepted. Cross-model adapters are still preview.
>
> https://github.com/FMStupid173/calm-agent
>
> Send me the smallest prompt where it fails.

## 即刻

> 我给 AI 做了一层 Dynamic Human Layer：它会先判断你在聊天、写作、处理情绪、coding 还是 research，再调整这一轮的语气、结构、改写自由度和证据门槛。
>
> 写作时它尽量保护原意；coding 和 research 时会要求先检查、选对来源、核验易变事实。它用于减少可避免的幻觉，也明确承认自己无法保证永远正确。
>
> Calm Agent 包含 Codex Skill、通用复制提示词、ChatGPT/Gemini/DeepSeek/Cursor 适配和对抗测试。
>
> https://github.com/FMStupid173/calm-agent
>
> 这次不求“支持一下”。我想收真实失败：哪一句还是很 AI，哪一次改写把原意改坏了，哪一个模型根本压不住默认语气。

## 小红书

**Cover**

> 我给 AI 做了一个“动态人味层”

**Alternative cover**

> 它会看场景决定怎么说

**Title**

> 我做了一个会动态调整“人味”的 AI Skill

**Body**

> 我喜欢用 AI 写东西和想问题，但一直受不了几种味道：
>
> 先夸你，再列五点；普通难过被说成心理咨询；一句原本有点笨、有点真的话，被润色成标准答案；不知道的资料也说得很确定。
>
> 所以我做了 Calm Agent。它的核心是 Dynamic Human Layer：先判断你在聊天、写作、处理情绪、coding 还是 research，再动态调整语气、长度、结构、改写自由度和证据门槛。
>
> 聊天时少点客服腔；写作时保护原意；情绪场景控制建议的分量；coding 和 research 时要求先检查、选对来源、核验易变事实。这能减少一部分可避免的幻觉，但不会让模型获得它原本没有的搜索能力，也不保证所有答案正确。
>
> 目前 Codex 版测试得最完整，ChatGPT、Gemini、DeepSeek 还在收真实反馈。
>
> 项目完全开源：https://github.com/FMStupid173/calm-agent
>
> 评论区可以留一句你最讨厌的 AI 套话。我会把高频问题变成下一轮测试题。

**Tags**

`#AI工具` `#ChatGPT` `#开源项目` `#写作` `#效率工具` `#程序员` `#AI写作`

## 知乎想法

> “AI 味”很少来自某一个词。真正影响体验的是模型会不会看场合：聊天、写作、情绪支持、coding 和 research 需要不同的温度、结构、改写自由度与证据门槛。
>
> 我把这个判断做成了 Calm Agent 的 Dynamic Human Layer。它每轮生成回答契约，同时约束语气、语义保真、来源匹配和不确定性，支持 Skill 与通用复制提示词两种入口。
>
> https://github.com/FMStupid173/calm-agent

## Reply Templates

**Someone says it still sounds like AI**

> 这个反馈有用。方便给一个最小例子吗？保留 prompt 和失败的两三句输出就够，隐私可以全部替换掉。

**Someone says another project already does this**

> 同类 humanizer 很多。Calm Agent 的差异是 Dynamic Human Layer：每一轮都根据场景、风险、情绪温度和改写自由度调整人味与证据门槛。它还包含写作语义保真，以及 coding/research 的来源匹配与核验规则。真实效果仍需要跨模型任务验证。

**Someone asks whether it clones Claude**

> 没有复制模型，也不要求 AI 冒充 Claude。项目把克制、判断、写作保真和边界感整理成可移植规则。

**Someone challenges the 29/30 result**

> 这是 Codex 上的一轮聚焦回归，只说明当前测试集中的行为，不代表跨模型效果或市场偏好。测试题、输出和评分规则都在仓库里。

## Posting Order

1. Publish GitHub and Release.
2. Post to V2EX and stay available for replies.
3. Post Show HN when you can answer comments for several hours.
4. Adapt one Reddit post to one community at a time.
5. Use before/after images for Xiaohongshu and Jike.

Do not ask friends to coordinate votes. Ask specific users for one real task and one failure report.
