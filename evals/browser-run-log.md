# Browser Run Log

Date: 2026-07-03

Goal: run an external 12-prompt Calm Agent benchmark in ChatGPT through the user's Chrome browser.

Privacy boundary:

- Only public project benchmark prompts and public adapter instructions were eligible to send.
- No raw Claude export data, friend data, local paths, or private conversations were sent.

Attempt summary:

1. Connected to Chrome through the Codex Chrome browser-control plugin.
2. Confirmed ChatGPT was reachable and appeared logged in.
3. Tried to inspect the visible ChatGPT input field.
4. The Chrome automation bridge timed out while reading page state.
5. Retried with a clean ChatGPT tab and a longer 120-second timeout.
6. The bridge timed out again before the prompt could be submitted.

Result:

- External browser benchmark was not completed in this run.
- The fallback artifact `external-ai-12-prompt-batch.md` was added so the same benchmark can be pasted into any external AI manually.

Next best step:

1. Paste `external-ai-12-prompt-batch.md` into ChatGPT or another AI.
2. Save the reply under `evals/`.
3. Score it with `benchmark-agent/single-rater-sheet.md`.
4. Add aggregate scores to `benchmark-results-template.csv`.
