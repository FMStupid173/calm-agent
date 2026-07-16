# Model Adapter Evidence Matrix

Date: 2026-07-16

| Platform | Adapter | Current core installed | Fresh focused regression | Fresh multi-turn | Public claim allowed |
|---|---|---:|---:|---:|---|
| Codex | `skill/` | yes | yes, `29 / 30` accepted | yes, treatment/control A/B | Preview-ready on tested Codex environment |
| ChatGPT web | `adapters/chatgpt-strict.md` | manual copy | no | no | Adapter available; current performance unverified |
| Gemini web | `adapters/gemini-gems.md` | manual copy | no | no | Adapter available; current performance unverified |
| DeepSeek web | `adapters/deepseek-system-prompt.md` | manual copy | no | no | Adapter available; current performance unverified |
| Cursor | `adapters/cursor-rules.md` | manual/project rule | no | no | Adapter available; current performance unverified |
| Other | `adapters/generic-system-prompt.md` | manual copy | no | no | Experimental starting point only |

Historical adapter reviews remain useful for regression hypotheses. They are not evidence for the latest core rules because the Dynamic Human Layer, proposition lock, citation metadata gate, and initiative gate changed afterward.

## Promotion Rule

Promote a platform from `unverified` only after:

1. a clean installation or copy procedure;
2. the 30-prompt focused regression;
3. the 10-scenario multi-turn set;
4. zero identity, privacy, fabricated-source, or false-capability failures;
5. a preserved raw-output artifact and dated review.
