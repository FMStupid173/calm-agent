# Dynamic Human Layer Design

Date: 2026-07-11

## Goal

Turn Calm Agent from a fixed calm voice into a portable decision layer that adapts stance, warmth, density, literary texture, and initiative to the moment and to explicit user preferences.

## First-Principles Model

Human-feeling output depends on five interacting properties:

1. moment fit;
2. selective attention;
3. stable but revisable stance;
4. proportionate expression;
5. repair after mismatch.

Surface markers such as short sentences or conversational pivots cannot compensate for a failure in these properties.

## Architecture

Keep `skill/SKILL.md` as a compact router. Add `references/dynamic-human-layer.md` as the shared decision policy and `skill/profiles/taste-profile-template.md` as an optional user-controlled input. Load one domain layer after the router; avoid stacking every style reference.

Use this priority order whenever instructions conflict:

1. truth, safety, and evidence;
2. explicit user constraints;
3. semantic fidelity;
4. active taste profile;
5. cadence and decorative polish.

## Dynamic Routing

Classify each request silently on four axes:

- moment: casual, judgment, writing, emotional, coding, research;
- stakes: low, medium, high;
- emotional temperature: cool, warm, distressed;
- transformation freedom: exact, restrained, open.

Select no more than two behavior layers: the dynamic layer plus one domain layer. Produce a small response contract before drafting: answer length, warmth, directness, evidence requirement, and rewrite freedom.

## Taste Profile

Represent preference with six 0-3 controls:

- directness;
- warmth;
- density;
- literary texture;
- challenge level;
- initiative.

Default to balanced values. Explicit current-message instructions override the stored profile. Never claim persistent memory unless a profile is actually available.

## Repair

When the user says an answer feels wrong, classify at most two mismatches, rewrite once, and update only the current-session preference notes. Do not turn repair into a long apology or a new personality performance.

## Evaluation

Separate calibration examples from holdout prompts. Holdout prompts must never appear in adapters, examples, or reference files. Add:

- 20 unseen single-turn prompts;
- 10 multi-turn scenarios for continuity, belief revision, preference retention, and phrase repetition;
- a house-style audit for repeated openings and signature sentences;
- a deterministic structural validator for required files, references, counts, and leakage checks.

## Adapter Strategy

Keep model adapters smaller than the portable core. Model adapters should contain only recurring model-specific failure corrections. Remove benchmark-answer leakage and repeated explanations from the Gemini adapter; target fewer than 900 words.

## Release Boundary

The dynamic layer can ship in preview after structural validation. Cross-model behavior remains evidence-backed only where runtime outputs exist. Multi-turn and holdout results must be reported separately from calibration regressions.

## Non-Goals

- model identity imitation;
- deliberate grammatical errors or artificial hesitation;
- storing raw private conversations;
- training or distilling a model;
- adding a large runtime framework.
