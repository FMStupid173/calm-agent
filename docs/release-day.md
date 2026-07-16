# Release Day

## Before Posting

1. Run `powershell -ExecutionPolicy Bypass -File scripts/prepublish-audit.ps1`.
2. Build the archive with `powershell -ExecutionPolicy Bypass -File scripts/package-release.ps1`.
3. Extract the archive into a temporary directory and inspect the top-level file list.
4. Enable GitHub private vulnerability reporting.
5. Open the README in GitHub and test every Quick Start path.
6. Check screenshots for profile names, avatars, browser tabs, local paths, and notifications.

Upload only the versioned archive produced by the packaging script and its `.sha256` file.

## V2EX Draft

**Title**

我把“AI 说话太油、太满、太像客服”整理成了一个可测试的开源 Skill

**Body**

Calm Agent 是一套可移植的 AI 输出约束，主要处理套话、过度解释、客服腔、写作过度润色和缺少证据边界的问题。

目前 Codex 版本完成了一轮新的回归测试；ChatGPT、Gemini 和 DeepSeek adapter 仍需要更多真实使用验证。项目不要求模型假装成 Claude，也不包含原始聊天记录。

我现在最需要失败样本：请拿一条你平时真的会问的问题跑一次，告诉我回答哪里仍然有 AI 味、哪里变差了。提交前请删掉隐私和账号信息。

## Show HN Draft

**Title**

Show HN: Calm Agent - portable rules for less templated AI responses

**Body**

Calm Agent is an open-source output-quality layer for AI assistants. It focuses on plain judgment, lower-hype writing, semantic fidelity, emotional proportion, and evidence boundaries.

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
