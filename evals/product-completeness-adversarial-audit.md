# Product Completeness Adversarial Audit

Date: 2026-07-10

Reviewer stance: strict product manager and adversarial evaluator. The question is not "does the skill have many files?" The question is whether the project can survive public use, third-party testing, and skeptical readers.

## Checks Run

- Python compile check for `benchmark-agent/summarize_results.py`
- Empty benchmark summary on `evals/benchmark-results-template.csv`
- Example benchmark summary on `benchmark-agent/example-results.csv`
- CSV header consistency check
- Markdown reference existence check
- Privacy/path scan for local paths and raw export indicators
- Negative phrase scan for identity and raw-data risks
- Manual review of `benchmark-agent/benchmark-agent-prompt.md`
- Manual review of `benchmark-agent/single-rater-sheet.md`
- Manual review of README benchmark claims

## Results

### Passed

- No missing Markdown/file references were found.
- `summarize_results.py` compiles.
- Empty benchmark template returns `null` pass rates instead of misleading zero scores.
- Privacy scan found no local export paths or friend-data artifacts.
- Source-fit, trait, cadence, and rigor metrics are now represented in the CSV and summarizer.

### Fixed During Audit

1. `benchmark-agent/example-results.csv` was still using the old column set.
   - Fixed by updating it to match the 21-column benchmark template.

2. `benchmark-agent/benchmark-agent-prompt.md` was still judging only old style metrics.
   - Fixed by adding human cadence, trait alignment, evidence hygiene, source fit, and verification.

3. `benchmark-agent/single-rater-sheet.md` still used "Like Claude" as a score.
   - Fixed by replacing it with human cadence, taste, judgment, and reliability.

4. README benchmark claims did not mention that newer source-fit and trait modules still need fresh cross-model runs.
   - Fixed by adding a validation snapshot and remaining benchmark gaps.

## Remaining Product Gaps

### 1. Evidence Ledger

Problem: The current benchmark records scores and notes, but not enough structured evidence.

Why it matters: A skeptical user will ask, "What answer got this score?" The repo has some review files, but the scoring CSV does not consistently preserve raw answer, reviewer rationale, and exact failure span.

Recommended addition:

- `evals/evidence-ledger-template.csv`
- columns: `run_id`, `model`, `adapter`, `prompt_id`, `answer_excerpt`, `scores`, `failure_tags`, `rationale`, `revision_rule`

### 2. Model Adapter Matrix

Problem: The project supports ChatGPT, Gemini, DeepSeek, Cursor, and generic prompts, but it does not yet show which modules are strong or weak per model.

Why it matters: Different models fail differently. ChatGPT may be polished and generic; Gemini may over-structure; DeepSeek may infer too much without sources.

Recommended addition:

- `evals/model-adapter-matrix.md`
- rows: model / adapter / known strengths / common failures / required tests / latest result

### 3. Install And Usage Path

Problem: The project is rich, but a first-time user may not know whether to copy an adapter, install a skill, or run a benchmark.

Why it matters: GitHub stars often come from instant comprehension.

Recommended addition:

- README first-screen quickstart:
  - "For ChatGPT: copy this"
  - "For Claude/Codex-style skills: use this folder"
  - "To test: run this 12-prompt batch"

### 4. Before / After Gallery

Problem: The README has examples, but the project needs a stronger, dedicated gallery across the new modules.

Why it matters: Users believe examples faster than theory.

Recommended addition:

- `examples/before-after-gallery.md`
- categories: oily opening, writing taste, emotional proportion, product judgment, source fit, coding rigor

### 5. Release Checklist

Problem: There is no final gate for publishing.

Why it matters: The project touches brand boundaries, private data, benchmark claims, and source claims.

Recommended addition:

- `release-checklist.md`
- gates: privacy scan, brand wording, benchmark freshness, source claims, adapter smoke test, zip update

## First-Principles Product View

A complete product needs five surfaces:

1. Promise: what it improves.
2. Mechanism: how it improves it.
3. Proof: tests, examples, and evidence.
4. Usage: how a user applies it in under one minute.
5. Safety: privacy, identity, and reliability boundaries.

Calm Agent is strong on mechanism. It is now fairly strong on safety. It is improving on proof.

The next biggest product lift is usage and proof packaging: make the value obvious before asking anyone to read the theory.

## Priority Recommendation

Add these next, in order:

1. `examples/before-after-gallery.md`
2. `evals/model-adapter-matrix.md`
3. `evals/evidence-ledger-template.csv`
4. README quickstart rewrite
5. `release-checklist.md`

Do not add more abstract style rules until these are done. The core behavior system is already deep enough.
