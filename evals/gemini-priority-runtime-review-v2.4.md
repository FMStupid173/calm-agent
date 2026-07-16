# Gemini Priority Runtime Review v2.4

Date: 2026-07-11

Adapter tested: `adapters/gemini-gems.md` v2.4

Input: three raw Gemini answers supplied by the user

## Verdict

Pass: `3 / 3`.

The v2.4 priority gate is complete. Stop expanding the Gemini prompt.

## Review

| ID | Result | Main note |
|---:|---|---|
| 1 | pass | Confirms only the visible TypeError label and `undefined` text, then requests the complete error, stack, code, and reproduction steps. It names no operation or cause. |
| 2 | pass | Changes only `事` to `事情`; fatigue, scope, and reluctance to explain remain unchanged. |
| 3 | pass | Rephrases `不太清楚` as `说不清` and preserves the unspecified waiting state without inventing a person, message, schedule change, event, or cause. |

## What Passed

- evidence truth outranks a useful-looking guess;
- semantic fidelity outranks decorative specificity;
- strict rewriting accepts near-exact restatement;
- the adapter no longer needs more exception rules for these failure shapes.

## Release Status

Gemini web adapter v2.4 passes the single-turn acceptance suite and can be listed as supported.

Residual risk: long-context stability has not been measured. This is a known evidence gap, not a blocker for the current preview release.

## Stop Condition

Do not add more prompt rules from these three cases. Reopen the adapter only when a new failure appears in ordinary use or a multi-turn benchmark reveals systematic drift.
