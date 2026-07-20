# Model Adapter Evidence Matrix

| Platform | Adapter | Installation route | Public result included | Public claim allowed |
|---|---|---|---:|---|
| Codex app / CLI / IDE | `skill/` | native Skill via `.agents/skills/` | no | Package compatible; current performance unverified |
| Claude Code | `skill/` | native Skill via `.claude/skills/` | no | Package compatible; current performance unverified |
| ChatGPT web / mobile | `adapters/chatgpt-custom-instructions.md` | Custom Instructions | no | Adapter available; current performance unverified |
| ChatGPT custom GPT | `adapters/chatgpt-strict.md` | GPT Instructions | no | Adapter available; current performance unverified |
| Gemini web | `adapters/gemini-gems.md` | manual copy | no | Adapter available; current performance unverified |
| Gemini CLI | `skill/` | native Skill via `.gemini/skills/` | no | Package compatible; current performance unverified |
| Kimi Agent mode | `adapters/kimi-agent-skill-creator.md` | custom Skill via `/skill-creator` | no | Creation brief available; generated Skill unverified |
| Kimi standard chat | `adapters/kimi-preset.md` | Preset or manual copy | no | Adapter available; current performance unverified |
| Kimi Code | `skill/` | native Skill via `.kimi-code/skills/` or `.agents/skills/` | no | Package compatible; current performance unverified |
| DeepSeek web | `adapters/deepseek-system-prompt.md` | manual copy | no | Adapter available; current performance unverified |
| Cursor | `adapters/cursor-rules.md` | manual/project rule | no | Adapter available; current performance unverified |
| Any web AI without Skill support | `adapters/universal-copy-paste-prompt.md` | manual copy | no | Portable prompt; current performance unverified |
| Other / constrained context | `adapters/generic-system-prompt.md` | manual copy | no | Experimental starting point only |

Filled adapter reviews and local run artifacts are excluded from the public repository. Generate them locally from the reusable suites.

## Calibration Route

`calibrator/calibrate.py` can run DeepSeek through its API. ChatGPT, Gemini, and other web-only surfaces enter through manually collected `responses.csv` outputs. The current Calibration Copilot has local unit and contract validation; a live DeepSeek API calibration and fresh cross-model web imports remain pending.

No adapter is promoted automatically. A candidate must pass holdout gates and receive a recorded blind human review.

## Promotion Rule

Promote a platform from `unverified` only after:

1. a clean installation or copy procedure;
2. the 30-prompt focused regression;
3. the 10-scenario multi-turn set;
4. zero identity, privacy, fabricated-source, or false-capability failures;
5. a privately retained raw-output artifact and a separately privacy-reviewed public summary when needed.
