# Gemini Targeted Runtime Review v2.2

Date: 2026-07-10

Adapter tested: `adapters/gemini-gems.md` v2.2, before the v2.3 patch

Input: three response blocks supplied for four prompts. The first block covers the shared behavior tested by prompts 1 and 2, but separate execution of both prompts was not shown.

## Verdict

Reliability pass. Writing voice watch. Overall Gemini status remains `pass / watch`.

## Review

| Prompt | Result | Main note |
|---:|---|---|
| 1-2 | behavioral pass | Refuses remembered current model names and prices, explains why a disclaimer is insufficient, and routes to the official pricing page. Separate runs were not shown. |
| 3 | watch | Correctly requests the full message and stack, but still infers that code performed an illegal operation on an undefined variable from the short label alone. |
| 4 | no | `常常` adds frequency and `就算了` adds resignation or finality that the original did not contain. |

## Product Interpretation

The source-fit and current-fact layer is now strong enough for release. The remaining Gemini weakness is constrained rewriting: it tends to invent a small emotional turn even when asked to preserve the original voice.

## v2.3 Correction

The Gemini adapter now uses semantic minimal-edit mode for voice-preserving rewrites:

- add no new frequency, decisions, events, causes, relationships, bodily symptoms, or conclusions;
- allow zero new details when the source sentence does not entail a safe detail;
- improve wording and rhythm without manufacturing emotional movement.

Run `gemini-targeted-regression-v2.3.md` for the final writing and error-shape check.
