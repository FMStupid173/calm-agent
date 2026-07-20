# Judging Without A Reference Corpus

Use response behavior and target-user preference. Do not use Claude similarity as ground truth.

## Evidence Order

1. Hard-gate correctness: truth, privacy, identity, semantic fidelity, source fit, verification.
2. Response selection: act fit, interaction contribution, non-substitutability, boundary recognition, proportion, and next-turn fit.
3. Blind target-user A/B preference.

## Pairwise Workflow

1. Give two isolated conditions the same multi-turn scenario.
2. Remove model and treatment labels.
3. Ask the reviewer which answer they would rather receive.
4. Require one short reason tied to the interaction.
5. Classify that reason as a hard-gate issue, response-act issue, selection-test issue, or personal preference.
6. Update the mechanism from repeated reasons. Do not copy a winning sentence into the prompt.

## Record

```csv
scenario_id,turn_id,winner,reason,response_act_a,response_act_b,failure_tag,reviewer_id
```

One owner can calibrate a personal tool. Public claims about users require several target users and should report sample size, tie rate, and conditions.

Stop changing the mechanism when improvements disappear on unseen multi-turn scenarios or hard-gate performance regresses.
