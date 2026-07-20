# Project Lifecycle And Adversarial Debugging

Use this reference for understanding an unfamiliar project, planning consequential work, implementing features, debugging, refactoring, reviewing changes, and preparing a release.

The goal is to improve causal understanding and defect detection without turning ordinary engineering work into a ceremonial framework.

## Operating Principle

Treat a project as a changing system with an objective, observable behavior, constraints, state, dependencies, and invariants.

First-principles work means reducing a claim to evidence and mechanisms that can be inspected. It does not mean discarding the existing architecture or redesigning from scratch.

Adversarial testing means trying to falsify the current model at the boundaries where it is most likely to fail. It does not mean generating a long generic edge-case list.

Scale the process to risk. A small local edit may pass through these stages in minutes. A cross-module or release-critical change needs explicit artifacts and broader checks.

## Project State Ledger

Keep a small working ledger while the task is active:

- objective and user-visible success condition;
- current lifecycle stage;
- confirmed system facts and their evidence;
- governing constraints and invariants;
- material unknowns and assumptions;
- current hypothesis or decision;
- next discriminating action;
- verification completed and residual risk.

Update the ledger when files, tests, logs, sources, or the user change the evidence. Do not convert guesses into project facts. Do not expose the ledger as a fixed report unless it helps the user make a decision.

## Lifecycle

### 1. Frame The Outcome

Identify the concrete user or system outcome, the requested scope, and what must remain unchanged.

Define acceptance in observable terms. Replace goals such as "improve reliability" with behavior that can be demonstrated, such as "a stale response cannot overwrite the latest request" or "an unsupported current price is withheld until verified."

Ask only for information that cannot be discovered from the repository, runtime, or available tools. State a reversible assumption when waiting would add little value and the risk is low.

### 2. Build The Smallest Sufficient System Model

Inspect the narrowest set of artifacts that can explain the behavior:

- entry point and ownership boundary;
- inputs, outputs, state transitions, and side effects;
- callers, dependencies, configuration, and version constraints;
- tests, logs, recent changes, and documented contracts.

Trace one real path through the system. Expand the search only when the evidence crosses a boundary. A directory listing or README alone does not establish runtime behavior.

### 3. Establish A Baseline

Record the current observable behavior before changing it.

For a feature, identify the nearest existing test or behavior to extend. For a defect, capture expected behavior, actual behavior, exact inputs, environment, and the smallest repeatable reproduction available.

If the issue cannot be reproduced, preserve the report as evidence and instrument the uncertain boundary. Do not replace missing reproduction with a confident root-cause claim.

### 4. Decompose From First Principles

Express the problem as a violated contract or invariant. Separate:

- symptom: what was observed;
- mechanism: how the system produced it;
- root cause: the earliest supported condition that made the failure possible;
- contributing conditions: factors that increased likelihood or impact.

Generate a small set of competing hypotheses only when evidence does not already identify the mechanism. Rank them by fit and consequence. Choose the next check for information gain: prefer one observation that separates hypotheses over several checks that merely repeat the symptom.

### 5. Make The Smallest Coherent Change

Change the owner of the violated contract when possible. Preserve unrelated behavior and existing user changes.

Avoid symptom suppression, test-only patches, speculative cleanup, dependency upgrades without necessity, and broad refactors that make the causal effect hard to isolate.

Add an abstraction when it removes demonstrated complexity or matches an established boundary. A small patch is not automatically better when it leaves the invariant unenforced.

### 6. Verify In Layers

Run the strongest available checks, starting near the change and widening with blast radius:

1. reproduce the original failure or demonstrate the new acceptance condition;
2. run focused unit or contract checks;
3. run affected integration, type, build, or end-to-end checks;
4. inspect the diff for scope, semantic drift, and accidental data exposure.

Distinguish "the original symptom disappeared" from "the cause is understood and covered." Report any layer that could not run and the risk it leaves.

### 7. Attack The Result

Derive adversarial checks from the system model and changed invariant. Prioritize:

- boundary and empty inputs;
- stale, repeated, reordered, or concurrent events;
- partial failure and retry behavior;
- permission, privacy, and untrusted-content boundaries;
- version, configuration, and environment differences;
- neighboring behavior that shares the modified state or contract;
- evidence that would falsify the claimed root cause.

Stop when the important failure model is covered. Passing many irrelevant edge cases does not strengthen the conclusion.

### 8. Release And Learn

Before release, confirm the acceptance condition, regression status, migration or rollback needs, observability, privacy, and known limits.

After release, treat incidents and user corrections as new evidence. Add the smallest reproducible failure to the regression set. Change the mechanism when failures cluster; do not accumulate prompt-specific or example-specific patches.

## Causal Debugging Loop

Use this loop whenever a defect appears during any lifecycle stage:

1. Capture the exact symptom and expected behavior.
2. Reproduce or instrument the failure boundary.
3. Locate the first violated invariant.
4. List only plausible competing causes.
5. Run the cheapest check that can distinguish them.
6. Update or discard hypotheses from the result.
7. Patch the causal owner of the invariant.
8. Re-run the original reproduction, focused regression, and one neighboring adversarial case.

Call something the root cause only when the evidence supports the causal chain. Otherwise name it the current best hypothesis and state the missing check.

## Adversarial Review Gates

Fail the project process on any material instance of:

- `premature-implementation`: changing code before locating the relevant contract or owner;
- `false-root-cause`: presenting a plausible cause as established without causal evidence;
- `hypothesis-lock`: defending the first explanation after contrary evidence appears;
- `symptom-patch`: hiding the observed failure while leaving the violated invariant intact;
- `test-only-fix`: changing expectations to accept incorrect behavior;
- `verification-theater`: counting checks that do not exercise the changed path;
- `happy-path-only`: ignoring a likely boundary or failure mode created by the change;
- `scope-drift`: mixing unrelated cleanup into the causal patch;
- `false-completion`: claiming completion while a required check failed or did not run;
- `process-performance`: displaying project vocabulary without improving the decision or change.

## Completion Standard

A project stage is complete when the next decision is supported by observable evidence. A bug fix is complete when the intended behavior is restored, the causal explanation is proportionate to the evidence, regression protection covers the failure, and residual risk is stated without ceremony.
