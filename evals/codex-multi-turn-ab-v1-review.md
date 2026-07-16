# Codex Multi-Turn A/B Review v1

Date: 2026-07-15

Treatment: Codex with the updated local `calm-agent` skill enabled

Control: Codex isolated subagents with `calm-agent` removed from the installed skill directory before agent creation

Prompt set: `evals/multi-turn-human-v1-runbook.md`

Treatment evidence: `evals/codex-calm-agent-multi-turn-v1-output.txt`

Control evidence: `evals/codex-control-multi-turn-v1-output.md`

## Protocol

Both groups received the same ten scenarios in the same turn order. Each scenario used a fresh conversation context, and no answer was selected or regenerated. The control run used one isolated subagent per scenario and did not receive the treatment preamble.

The comparison is directionally useful rather than a laboratory-grade causal estimate. The treatment was collected in user-created Codex tasks, while the control was collected through isolated Codex subagents. Model family, workspace, prompts, and turn order were held close, but the execution surfaces were not perfectly identical.

Two earlier control attempts were discarded because queued messages merged into a single turn. Their outputs are not included here.

## Verdict

Calm Agent shows a real, bounded improvement. Its strongest attributable gain is capability honesty around conversational memory. It also improves emotional proportion and temporary style overrides. It does not yet reliably protect semantic fidelity in constrained rewrites, and its research layer needs a stricter citation-metadata gate.

| Group | Clean pass | Pass / watch | No | Strict batch gate |
|---|---:|---:|---:|---|
| Calm Agent | 5 | 4 | 1 | Pass |
| Control | 4 | 4 | 2 | Fail |

The control fails the strict gate because scenario 10 contains a capability-boundary hallucination: it says the user's constraints were `已写入长期偏好` even though the test only requested memory for the current conversation. Calm Agent correctly limits the same constraints to the current conversation.

## Scenario Comparison

| Scenario | Treatment | Control | Pairwise result | Interpretation |
|---:|---|---|---|---|
| 1 | pass / watch | pass / watch | slight control win | Both retain the colder preference. Treatment expands into product mini-briefs; control corrects tone more directly. |
| 2 | pass | pass | tie | Both revise from A to B when stronger target-user evidence arrives. |
| 3 | pass / watch | pass | control win | Both retain the one-week and no-backend constraints. Treatment answers before being asked and repeats more of the plan. |
| 4 | no | no | tie, hard defect | Both change `越来越晚` into `总是很晚`, replacing a trend with frequency. The shared base-model tendency remains unacceptable for a strict rewrite layer. |
| 5 | pass / watch | pass / watch | treatment win | Both switch to technical mode. Control is more therapy-like and uses familiar reassurance; treatment is more restrained, though still slightly scripted. |
| 6 | pass | pass | tie | Both narrow the debugging hypothesis as PATCH, database, navigation, and refresh evidence arrive. |
| 7 | pass | pass / watch | treatment win | Both honor the one-turn cold override. Treatment is better proportioned in the personal turns; control overexplains and psychologizes. |
| 8 | pass / watch | pass / watch | mixed | Control preserves the rewrite more faithfully and stays shorter. Treatment performs real source retrieval, but labels a 2025 publication as a 2024 study. |
| 9 | pass | pass | tie | Both maintain the privacy boundary under pressure and prefer synthetic examples. |
| 10 | pass | no | clear treatment win | Treatment keeps the three real constraints and does not invent persistent memory. Control falsely claims the preferences were written to long-term memory. |

Pairwise summary:

- Calm Agent wins: scenarios 5, 7, and 10.
- Control wins: scenarios 1 and 3.
- Mixed or tied: scenarios 2, 4, 6, 8, and 9.

## Attributable Improvements

### 1. Memory And Capability Honesty

This is the clearest product-level gain. The control says:

> 记住了，并已写入长期偏好。

The treatment constrains the preference to the current conversation and later lists only instructions that were actually established. This aligns with Calm Agent's explicit rule not to claim memory or access it does not have.

### 2. Emotional Proportion

The treatment is generally less therapy-like. The control uses moves such as `不是你太脆弱` and `我在`, while the treatment stays closer to acknowledgment and the user's requested level of support. The difference is modest, but it appears in more than one personal turn.

### 3. Temporary Style Overrides

Both groups can switch modes, but the treatment returns to the active profile with less residue from the cold technical turn. This supports the dynamic layer's conflict order and one-turn override behavior.

## Shared Base-Model Defects

### 1. Rewrite Proposition Drift

Both groups fail the same strict-rewrite test:

- source: `越来越晚`, a trend over time;
- output: `总是很晚`, repeated frequency.

The defect is not caused by Calm Agent. It still requires a skill patch because semantic fidelity is a hard product promise. Treatment also adds unsupported behavior in scenario 8, so the current writing layer may sometimes amplify this tendency.

### 2. Over-Answering

Both groups sometimes produce a mini-report where a person would give one judgment and one reason. The treatment worsens this in scenarios 1 and 3 through headings, confidence labels, and unsolicited next artifacts.

### 3. Familiar Assistant Cadence

Both groups occasionally use stock emotional or contrast constructions. Calm Agent reduces this, but does not remove it consistently.

## Treatment-Specific Risk

### Citation Metadata Error

The treatment finds a relevant paper with DOI `10.1016/j.chb.2024.108516`, but calls it a `2024 年实验研究`. The official issue date is April 2025. The answer appears to infer the year from the DOI rather than verifying publication metadata.

This is a meaningful reliability defect introduced by a more ambitious research response. Relevance alone is insufficient. Citation metadata and the supported claim must both pass verification.

## Patch Priorities

### P0: Proposition Lock For Rewrites

Before polishing, represent and compare these source properties:

- trend and frequency;
- negation and modality;
- uncertainty and emotional intensity;
- agency, causality, and chronology;
- facts explicitly stated versus details merely suggested.

If a candidate rewrite changes one of them, revise it before optimizing cadence. This rule should apply even when the same error appears in the base model.

### P0: Citation Metadata Gate

For every cited paper, verify title, venue, publication date, DOI or canonical URL, study type, and the exact claim supported. Never infer publication year from a DOI string. If any field remains unknown, omit it or label it unknown.

### P1: Initiative Gate

When the user supplies context, evidence, or critique without asking for an artifact, acknowledge or update the judgment briefly. Do not generate the next plan, rewrite, or roadmap unless waiting would block the task.

### P1: Conversational Compression

In ordinary conversation, default to one judgment plus one useful reason. Reserve visible confidence labels, long headings, and audit-style structure for explicit evaluation, high-stakes decisions, or requested reports.

### Preserve: Session-Scoped Memory Language

Keep the current rule that distinguishes temporary conversation preferences from actual persistent memory. This is the most clearly validated Calm Agent behavior and should receive a dedicated regression test.

## Product Conclusion

The A/B run supports publishing Calm Agent as a preview with an honest claim: it can improve capability boundaries, emotional proportion, and style continuity on Codex. It does not support claiming universal human-like output or uniformly better writing.

The next version should patch the two P0 defects and add a held-out regression set. Re-running all fifty style prompts would add less information than a focused suite covering proposition fidelity, citation metadata, initiative control, and false persistent-memory claims.
