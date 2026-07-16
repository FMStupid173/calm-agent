# Dynamic Human Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add adaptive human-taste routing, user preference controls, repair memory, unseen evaluation, and maintainable model adapters to Calm Agent.

**Architecture:** Keep the core skill as a progressive-disclosure router. Put dynamic decisions in one shared reference, preferences in a profile template, model-specific drift in compact adapters, and generalization evidence in isolated eval files.

**Tech Stack:** Markdown skill resources, Python 3 standard library structural validation, PowerShell packaging.

## Global Constraints

- Preserve the no-model-identity boundary.
- Publish no raw conversation data.
- Use truth and semantic fidelity ahead of stylistic polish.
- Keep holdout prompts out of adapters, examples, and references.
- Keep the Gemini adapter below 900 words.
- Do not add dependencies.

---

### Task 1: Dynamic-Layer Contract Validator

**Files:**
- Create: `benchmark-agent/validate_dynamic_layer.py`

**Interfaces:**
- Consumes: project root path from the script location.
- Produces: exit code `0` with `PASS` lines, or exit code `1` with explicit contract failures.

- [ ] Write checks for required files, core references, adapter word budget, holdout count, multi-turn count, house-style audit, and forbidden holdout leakage.
- [ ] Run the validator before implementation and confirm it fails because the dynamic artifacts do not exist.

### Task 2: Dynamic Human Policy And Preference Profile

**Files:**
- Create: `skill/references/dynamic-human-layer.md`
- Create: `skill/profiles/taste-profile-template.md`
- Modify: `skill/SKILL.md`
- Modify: `skill/references/critique-revision-loop.md`

**Interfaces:**
- Consumes: request context and optional taste profile.
- Produces: one response contract and at most one domain-layer route.

- [ ] Define conflict priority, four-axis moment routing, six taste controls, no-fake-memory behavior, and session-only repair updates.
- [ ] Route taste-sensitive requests through the dynamic layer in `SKILL.md`.
- [ ] Extend critique repair to update current-session preferences without inventing persistence.

### Task 3: Contradiction And Adapter Cleanup

**Files:**
- Modify: `skill/references/human-cadence-layer.md`
- Modify: `skill/references/human-taste-rubric.md`
- Modify: `skill/references/conversation-taste.md`
- Modify: `skill/references/daily-chat.md`
- Modify: `examples/preference-pairs.md`
- Modify: `adapters/gemini-gems.md`
- Modify: `adapters/model-adapter-guide.md`

**Interfaces:**
- Consumes: dynamic response contract.
- Produces: grounded specificity without invented propositions and compact model-specific corrections.

- [ ] Replace the invented `waiting for a signal` example with entailed specificity.
- [ ] Mark concrete detail as optional and source-bound.
- [ ] Vary repeated house phrases across examples.
- [ ] Rewrite Gemini as a compact v3 adapter below 900 words with no exact benchmark answers.
- [ ] Add adapter size and holdout-isolation rules to the guide.

### Task 4: Generalization And Multi-Turn Evaluation

**Files:**
- Create: `evals/human-taste-holdout-v1.md`
- Create: `evals/multi-turn-human-v1.md`
- Create: `evals/house-style-audit.md`
- Modify: `evals/style-lint-rules.md`

**Interfaces:**
- Consumes: raw model responses that have not seen the rubric.
- Produces: separate single-turn, multi-turn, and phrase-diversity verdicts.

- [ ] Add exactly 20 unseen prompts with no answer keys in model context.
- [ ] Add exactly 10 multi-turn scenarios covering continuity, correction, preference retention, and stance revision.
- [ ] Add repeated-opening and signature-phrase checks.
- [ ] Extend style lint with semantic-invention and house-accent tags.

### Task 5: Documentation, Verification, And Packaging

**Files:**
- Modify: `README.md`
- Regenerate: `../calm-agent-project.zip`

**Interfaces:**
- Consumes: all completed artifacts.
- Produces: a documented preview package and fresh validation output.

- [ ] Document dynamic routing, taste profiles, holdout isolation, multi-turn status, and adapter boundaries.
- [ ] Run `benchmark-agent/validate_dynamic_layer.py` and require zero failures.
- [ ] Run existing benchmark summarizer checks.
- [ ] Verify UTF-8, local references, privacy patterns, and ZIP entries.
- [ ] Sync the installed Codex skill after project verification when permission allows.
