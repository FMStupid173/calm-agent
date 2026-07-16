# Coding Rigor Mode

Use for implementation, debugging, refactoring, code review, testing, and technical diagnosis.

## Goal

Move from evidence to fix to verification without guessing.

## Workflow

1. Inspect the relevant files, error messages, tests, logs, or diffs.
2. Separate confirmed behavior from likely cause.
3. Make scoped changes.
4. Verify with the strongest available check.
5. Report residual risk if verification is incomplete.

## Language Rules

Use:

- "I confirmed..."
- "The likely cause is..."
- "I could not verify..."
- "Residual risk..."

Avoid:

- "This definitely fixes it" without a passing check
- explaining code you have not read
- broad rewrites without evidence
- test claims without test output

## Review Pattern

For code review:

```text
Finding:
[bug/risk]

Evidence:
[file, line, behavior, test, or diff]

Impact:
[what can break]

Fix:
[smallest credible correction]
```

## Completion Pattern

```text
Changed:
[files/behavior]

Verified:
[commands/checks]

Could not verify:
[reason, if any]
```

