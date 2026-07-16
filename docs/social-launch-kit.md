# Social Launch Kit

Repository: `https://github.com/FMStupid173/calm-agent`. Use one strong before/after pair from the README with every visual post.

## Core Message

**Chinese**

> 一套跨模型的 AI 输出质量层：少套话、少迎合、保留原意，该查证时查证。

**English**

> A portable output-quality layer for less templated, less sycophantic, more evidence-aware AI responses.

## GitHub

**Description**

> Portable rules, adapters, and evals for calmer, less templated, more evidence-aware AI responses.

**Topics**

`llm`, `prompt-engineering`, `codex-skills`, `chatgpt`, `gemini`, `deepseek`, `human-ai-interaction`, `ai-writing`, `evaluation`, `ai-agents`

**Release title**

> Calm Agent v0.1 Preview

**Release body**

> First public preview of Calm Agent, a portable output-quality layer for AI assistants.
>
> It includes a Codex skill, adapters for ChatGPT/Gemini/DeepSeek/Cursor, dynamic human-cadence rules, semantic-fidelity constraints, coding and research rigor guidance, adversarial prompts, and benchmark tooling.
>
> Current evidence: the Codex-focused regression accepted 29/30 cases. Cross-model adapters remain previews and need fresh real-user runs.
>
> The most useful contribution is a minimal redacted failure example from a real workflow. Please use the Output failure report template and never post credentials or private conversations.

## V2EX 分享创造

**Title**

> 我把“AI 说话太油、太满、太像客服”整理成了一个可测试的开源 Skill

**Body**

> 我经常遇到一种情况：AI 的答案大体正确，但开头先夸一句，中间列一排标题，结尾再总结一次。让它润色文字时，句子变顺了，原来的声音也没了；做 coding 和 research 时，它又可能把猜测说得很确定。
>
> 我把这些问题整理成了 Calm Agent。它是一套跨模型的输出质量约束，主要做四件事：
>
> - 少套话、少迎合，先给真实判断；
> - 根据聊天、写作、情绪、coding、research 动态调整语气和结构；
> - 改写时尽量锁住原意，不把人的话磨成统一 AI 腔；
> - 涉及事实、API、论文和市场信息时，区分已确认、推断和未知。
>
> Codex 版本刚完成一轮 30 题回归，29 题通过或可接受。ChatGPT、Gemini、DeepSeek adapter 仍是 preview，我想拿真实使用来继续校准。
>
> 项目：https://github.com/FMStupid173/calm-agent
>
> 我现在更需要失败样本。拿一条你平时真的会问的问题跑一下，告诉我它哪里仍然很 AI，或者哪里被这个 Skill 改坏了。请先删掉隐私和账号信息。

## Show HN

**Title**

> Show HN: Calm Agent - a portable output-quality layer for AI responses

**Body**

> I built Calm Agent after repeatedly seeing answers that were correct enough but still unpleasant to use: automatic praise, support-desk phrasing, excessive headings, semantic drift during rewriting, and confident claims without evidence.
>
> It packages a Codex skill, portable adapters, anti-patterns, task-sensitive response rules, and adversarial evals. It covers conversation and writing, but also adds evidence and uncertainty boundaries for coding and research.
>
> The current Codex regression accepted 29/30 cases. The ChatGPT, Gemini, DeepSeek, and Cursor adapters are previews; I am explicitly not treating old scores as current cross-model proof.
>
> Repo: https://github.com/FMStupid173/calm-agent
>
> The feedback I need most: run one prompt from your real workflow and report the smallest redacted case where the adapter made the answer worse.

## Reddit: r/ChatGPT or Prompt Communities

Check the community rules before posting. Lead with the observed problem and invite testing; avoid dropping only a link.

**Title**

> I turned my “stop sounding like support copy” instructions into a tested, cross-model style layer

**Body**

> I kept rewriting the same custom instructions: stop praising every idea, stop turning simple answers into five sections, preserve my wording when editing, and verify current facts instead of adding a confident disclaimer.
>
> I turned that into Calm Agent: a portable set of adapters, anti-patterns, and evals for ChatGPT, Codex, Gemini, DeepSeek, and Cursor.
>
> It is broader than a text humanizer. It changes the live conversation contract and includes semantic-fidelity and evidence-boundary rules for writing, coding, and research.
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

> AI answers often fail after they become technically acceptable: too much praise, too many headings, polished-away voice, confident claims without evidence.
>
> I built Calm Agent as a portable output-quality layer for ChatGPT, Codex, Gemini, DeepSeek and Cursor.
>
> Codex regression: 29/30 accepted. Cross-model adapters are still preview.
>
> https://github.com/FMStupid173/calm-agent
>
> Send me the smallest prompt where it fails.

## 即刻

> 我把自己反复写给 AI 的那几句要求做成了一个开源项目：别先夸我，别把简单问题写成五段，改文字时保留我的声音，不确定的事实别装确定。
>
> Calm Agent 现在包含 Codex Skill，以及 ChatGPT、Gemini、DeepSeek、Cursor 的适配文件，还带一套对抗测试。
>
> https://github.com/FMStupid173/calm-agent
>
> 这次不求“支持一下”。我想收真实失败：哪一句还是很 AI，哪一次改写把原意改坏了，哪一个模型根本压不住默认语气。

## 小红书

**Cover**

> 我受够了 AI 的客服腔

**Alternative cover**

> 别再说“当然可以”了

**Title**

> 我做了一个让 AI 少点套话、保留人味的开源 Skill

**Body**

> 我喜欢用 AI 写东西和想问题，但一直受不了几种味道：
>
> 先夸你，再列五点；普通难过被说成心理咨询；一句原本有点笨、有点真的话，被润色成标准答案；不知道的资料也说得很确定。
>
> 所以我做了 Calm Agent。它会根据聊天、写作、情绪、coding 和 research 调整表达，也会提醒模型在该查证的时候查证。
>
> 目前 Codex 版测试得最完整，ChatGPT、Gemini、DeepSeek 还在收真实反馈。
>
> 项目完全开源：https://github.com/FMStupid173/calm-agent
>
> 评论区可以留一句你最讨厌的 AI 套话。我会把高频问题变成下一轮测试题。

**Tags**

`#AI工具` `#ChatGPT` `#开源项目` `#写作` `#效率工具` `#程序员` `#AI写作`

## 知乎想法

> “AI 味”很少来自某一个词。更常见的是整套动作：自动赞同、过度解释、平均分配篇幅、把改写磨得太顺、用流畅掩盖不确定。
>
> 我把这些失败拆成了可执行规则和对抗测试，做成 Calm Agent。它同时约束语气、语义保真和证据边界，支持多个模型入口。
>
> https://github.com/FMStupid173/calm-agent

## Reply Templates

**Someone says it still sounds like AI**

> 这个反馈有用。方便给一个最小例子吗？保留 prompt 和失败的两三句输出就够，隐私可以全部替换掉。

**Someone says another project already does this**

> 同类 humanizer 很多。Calm Agent 主要多做了三层：实时对话姿态、改写语义保真、coding/research 的证据边界。它是否真的更有用，还需要真实任务来验证。

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
