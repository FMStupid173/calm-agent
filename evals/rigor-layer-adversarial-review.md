# Rigor Layer Adversarial Review

Reviewer stance: a heavy Claude user and strict product manager looking for ways this project can fail in public use.

## Verdict

The rigor layer is directionally right. It makes Calm Agent more than a pleasant writing style: it becomes an output-quality layer for coding, research, and product judgment.

The main risk is that reliability rules can make the assistant sound like a compliance memo. The fix is already reflected in `skill/references/rigor-layer.md`: be precise about evidence, then return to ordinary language.

## Findings

### 1. Rigor Can Overpower Human Taste

Risk: The assistant may over-label every sentence as "confirmed", "inference", or "unknown", even in casual conversation.

Fix: Use activation gates. Apply the full rigor layer only when the task involves code, research, strategy, current facts, external claims, privacy, or decisions with real cost.

### 2. The Assistant May Become Too Cautious

Risk: To avoid hallucination, it may refuse to give judgment.

Fix: Separate confidence from usefulness. A good answer can say, "My current bet is..." and then state what would change the bet.

### 3. Current-Fact Claims Need Tool Awareness

Risk: Some environments cannot browse or inspect files. The assistant may still write as if it verified facts.

Fix: Require explicit provenance. If it did not inspect, browse, run, or source something, it must not present that thing as verified.

### 4. Coding Reliability Needs A Real Loop

Risk: A coding answer may sound careful while still skipping tests.

Fix: The coding mode now requires inspect -> infer -> change -> verify. If verification cannot run, the answer must say exactly what was not checked.

### 5. Benchmark Alignment Was Previously Incomplete

Risk: The CSV template had rigor fields before the rubric and runner fully explained them.

Fix: `benchmark-results-template.csv`, `scoring-rubric.md`, `run-benchmark.md`, and `benchmark-agent/summarize_results.py` now use the same reliability dimensions.

## Remaining Gaps

- Run `evals/rigor-adversarial-prompts.md` on ChatGPT, Gemini, and DeepSeek with their adapters.
- Add one real coding-task benchmark where the assistant must inspect files and run a test.
- Add one research benchmark where browsing is required, and mark non-browsing answers as incomplete rather than wrong.
- Keep watching for style drift: too many caveats can be just as unpleasant as fake certainty.

## Product Standard

Calm Agent should feel like a careful person with taste:

- clear enough to act on
- honest about evidence
- willing to make a grounded bet
- quiet in tone
- resistant to fake certainty
- still readable by a tired human
