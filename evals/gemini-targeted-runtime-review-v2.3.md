# Gemini Targeted Runtime Review v2.3

Date: 2026-07-10

Adapter tested: `adapters/gemini-gems.md` v2.3, before the v2.4 patch

Input: three raw Gemini answers supplied by the user

## Verdict

Targeted gate failed: `0 pass / 1 watch / 2 no`. Overall Gemini support remains `pass / watch` because reliability and general conversation passed earlier suites.

## Review

| ID | Result | Main note |
|---:|---|---|
| 1 | no | Infers that the user's code performed an invalid operation on an undefined variable. The visible label does not establish that. |
| 2 | watch | Preserves the broad meaning, but turns plain fatigue into more abstract polished prose and adds `开口去细说`. |
| 3 | no | Invents that the user's days became less busy and changes uncertain waiting into expectation. |

## Root Cause

The adapter contained two unresolved instruction conflicts:

- human cadence requested one prompt-specific detail while strict rewriting prohibited new propositions;
- usefulness encouraged an explanation while evidence fidelity prohibited inferring an operation from a short error label.

Gemini chose the more generative instruction in both cases. Adding more prohibited words would not resolve the priority conflict.

## v2.4 Correction

The adapter now defines this conflict order:

1. evidence truth;
2. semantic fidelity;
3. requested format;
4. human-cadence polish.

It also includes positive and negative calibration examples for the exact failure shapes. Run `gemini-priority-regression-v2.4.md` once. Further failure should be documented as a Gemini model limitation instead of expanding the prompt again.
