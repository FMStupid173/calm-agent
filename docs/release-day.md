# Release Day

## Before Posting

1. Run `powershell -ExecutionPolicy Bypass -File scripts/prepublish-audit.ps1`.
2. Build the archive with `powershell -ExecutionPolicy Bypass -File scripts/package-release.ps1`.
3. Extract the archive into a temporary directory and inspect the top-level file list.
4. Enable GitHub private vulnerability reporting.
5. Open the README in GitHub and test every Quick Start path.
6. Check screenshots for profile names, avatars, browser tabs, local paths, and notifications.

Upload only the versioned archive produced by the packaging script and its `.sha256` file.

For Preview 3, run the Calibration Copilot unit suite and a three-item API smoke test before claiming live DeepSeek support. Without an API key, describe it as code-validated and awaiting a live provider run.

## V2EX Draft

**Title**

我给 AI 做了一个会按场景调整人味和严谨度的开源 Skill

**Body**

Calm Agent 的核心是 Dynamic Human Layer。它会判断当前属于聊天、写作、情绪、coding 还是 research，再动态调整语气、结构、改写自由度和证据门槛。

聊天时它减少客服腔；写作时保护原意；情绪场景控制建议的分量；coding 和 research 场景要求先检查、选对来源、核验易变事实，并区分已确认、推断和未知。这些规则用于减少可避免的幻觉，不能保证模型永远正确。

目前 Codex 版本完成了一轮新的回归测试；ChatGPT、Gemini 和 DeepSeek adapter 仍需要更多真实使用验证。项目不要求模型假装成 Claude，也不包含原始聊天记录。

我现在最需要失败样本：请拿一条你平时真的会问的问题跑一次，告诉我回答哪里仍然有 AI 味、哪里变差了。提交前请删掉隐私和账号信息。

## Show HN Draft

**Title**

Show HN: Calm Agent - a Dynamic Human Layer for adaptive, evidence-aware AI responses

**Body**

Calm Agent is an open-source Dynamic Human Layer for AI assistants. It routes each turn by moment, stakes, emotional temperature, and transformation freedom, then adapts voice, structure, semantic fidelity, and the evidence gate.

For coding and research, it is designed to reduce avoidable hallucinations through inspect-before-claiming, source-fit checks, volatile-fact verification, and explicit separation of confirmed facts, inference, and unknowns. It does not guarantee correctness or replace retrieval.

The Codex skill has a fresh regression pass. The ChatGPT, Gemini, DeepSeek, and Cursor adapters are available as previews and still need current cross-model validation.

I would value one kind of feedback most: run a prompt from your real workflow, then report the smallest redacted example where the adapter made the answer worse.

## Reddit Framing

Lead with the language problem and one before/after pair. Explain the method before linking the repository. Check each community's self-promotion rules and ask moderators when unclear. Do not paste the same promotional text across multiple communities.

## Seven-Day Signal

- 5 successful installs or copies;
- 3 people using it on real tasks;
- 2 concrete failure examples;
- 1 person keeping it enabled after three days.

Stars measure distribution. Repeated use and specific failures are stronger early product evidence.
