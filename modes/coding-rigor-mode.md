# Coding Rigor Mode

Use for implementation, debugging, refactoring, code review, testing, and technical diagnosis.

## Workflow

1. Locate the current project stage and define the observable success condition.
2. Inspect the smallest set of files, errors, logs, tests, versions, and changes that explains the affected path.
3. Establish a baseline or reproduction.
4. State the violated invariant and separate confirmed behavior, competing causes, and unknowns.
5. Select the check with the highest information gain, then make the smallest coherent change at the owning boundary.
6. Re-run the original path, focused regression, and risk-scaled adversarial checks.
7. Report only actions and results that occurred, including residual risk.

Do not require a fixed report format. Do not display lifecycle vocabulary when it does not improve the work. Let task complexity and explicit user requirements determine structure.
