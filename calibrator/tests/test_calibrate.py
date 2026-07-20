from __future__ import annotations

import json
import io
import os
import csv
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

from calibrator import calibrate


class CalibrationTests(unittest.TestCase):
    def test_focused_regression_parses_30_prompts(self) -> None:
        prompts = calibrate.parse_prompts(
            calibrate.ROOT / "evals" / "focused-regression-v2.md",
            "Clean Prompt Batch",
        )
        self.assertEqual(30, len(prompts))
        self.assertEqual("1", prompts[0]["id"])
        self.assertEqual("30", prompts[-1]["id"])
        self.assertEqual("A. Proposition Fidelity", prompts[0]["category"])

    def test_response_selection_adversarial_parses_20_prompts(self) -> None:
        prompts = calibrate.parse_prompts(
            calibrate.ROOT / "evals" / "response-selection-adversarial-v1.md",
            "Clean Prompt Batch",
        )
        self.assertEqual(20, len(prompts))
        self.assertEqual("1", prompts[0]["id"])
        self.assertEqual("20", prompts[-1]["id"])

    def test_next_turn_effects_adversarial_parses_20_prompts(self) -> None:
        prompts = calibrate.parse_prompts(
            calibrate.ROOT / "evals" / "next-turn-effects-adversarial-v1.md",
            "Clean Prompt Batch",
        )
        self.assertEqual(20, len(prompts))
        self.assertEqual("1", prompts[0]["id"])
        self.assertEqual("20", prompts[-1]["id"])

    def test_project_lifecycle_adversarial_parses_20_prompts(self) -> None:
        prompts = calibrate.parse_prompts(
            calibrate.ROOT / "evals" / "project-lifecycle-adversarial-v1.md",
            "Clean Prompt Batch",
        )
        self.assertEqual(20, len(prompts))
        self.assertEqual("1", prompts[0]["id"])
        self.assertEqual("20", prompts[-1]["id"])

    def test_platform_adapter_adversarial_parses_20_prompts(self) -> None:
        prompts = calibrate.parse_prompts(
            calibrate.ROOT / "evals" / "platform-adapter-adversarial-v1.md",
            "Clean Prompt Batch",
        )
        self.assertEqual(20, len(prompts))
        self.assertEqual("1", prompts[0]["id"])
        self.assertEqual("20", prompts[-1]["id"])

    def test_next_turn_fit_is_selection_not_guardrail(self) -> None:
        self.assertIn("next_turn_fit", calibrate.SELECTION_FIELDS)
        self.assertNotIn("next_turn_fit", calibrate.GUARDRAIL_FIELDS)

    def test_benchmark_csv_headers_match_and_include_next_turn_fit(self) -> None:
        paths = [
            calibrate.ROOT / "benchmark-agent" / "example-results.csv",
            calibrate.ROOT / "evals" / "benchmark-results-template.csv",
        ]
        headers = []
        for path in paths:
            with path.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.reader(handle)
                header = next(reader)
                self.assertTrue(all(len(row) == len(header) for row in reader))
                headers.append(header)
        self.assertEqual(headers[0], headers[1])
        self.assertIn("next_turn_fit", headers[0])

    def test_prepare_is_deterministic_and_keeps_holdout(self) -> None:
        config = json.loads(
            (calibrate.ROOT / "calibrator" / "config.example.json").read_text(
                encoding="utf-8"
            )
        )
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_path = Path(first)
            second_path = Path(second)
            config_file = calibrate.ROOT / "calibrator" / "config.example.json"
            with redirect_stdout(io.StringIO()):
                calibrate.prepare(config, config_file, first_path)
                calibrate.prepare(config, config_file, second_path)
            first_rows = calibrate.read_csv(first_path / "responses.csv")
            second_rows = calibrate.read_csv(second_path / "responses.csv")
            self.assertEqual(
                [(row["id"], row["split"]) for row in first_rows],
                [(row["id"], row["split"]) for row in second_rows],
            )
            self.assertIn("train", {row["split"] for row in first_rows})
            self.assertIn("holdout", {row["split"] for row in first_rows})
            self.assertEqual(9, sum(row["split"] == "holdout" for row in first_rows))

    def test_prepare_does_not_record_external_parent_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as run:
            external = Path(directory)
            dataset = external / "private-prompts.md"
            adapter = external / "private-adapter.md"
            dataset.write_text(
                "## Clean Prompt Batch\n\n1. first prompt\n2. second prompt\n",
                encoding="utf-8",
            )
            adapter.write_text("adapter", encoding="utf-8")
            config = {
                "run_name": "external-path-test",
                "adapter": str(adapter),
                "dataset": {
                    "path": str(dataset),
                    "section": "Clean Prompt Batch",
                    "holdout_ratio": 0.5,
                    "seed": "test",
                },
                "target": {},
                "judge": {},
            }
            with redirect_stdout(io.StringIO()):
                calibrate.prepare(config, external / "config.local.json", Path(run))
            manifest = calibrate.read_json(Path(run) / "manifest.json")
            self.assertEqual("private-prompts.md", manifest["dataset"]["path"])
            self.assertEqual("private-adapter.md", manifest["adapter"]["path"])
            self.assertNotIn(str(external), json.dumps(manifest))

    def test_proposal_context_excludes_holdout(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            responses = [
                self.response("1", "train", "train answer"),
                self.response("2", "holdout", "holdout answer"),
            ]
            calibrate.write_csv(
                run_dir / "responses.csv",
                calibrate.RESPONSE_FIELDS,
                responses,
            )
            scores = [
                self.score("1", "train", status="no"),
                self.score("2", "holdout", status="no"),
            ]
            calibrate.write_csv(
                run_dir / "baseline-scores.csv",
                calibrate.SCORE_CSV_FIELDS,
                scores,
            )
            context = calibrate.proposal_context(run_dir)
            self.assertEqual(["1"], [item["id"] for item in context])
            self.assertNotIn("holdout answer", json.dumps(context, ensure_ascii=False))

    def test_compare_passes_to_human_review(self) -> None:
        config = self.config()
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            baseline = [
                self.score("1", "train", score=4),
                self.score("2", "train", score=4),
                self.score("3", "holdout", score=4),
                self.score("4", "holdout", score=4),
            ]
            candidate = [
                self.score("1", "train", score=5),
                self.score("2", "train", score=5),
                self.score("3", "holdout", score=5),
                self.score("4", "holdout", score=4),
            ]
            calibrate.write_csv(
                run_dir / "baseline-scores.csv",
                calibrate.SCORE_CSV_FIELDS,
                baseline,
            )
            calibrate.write_csv(
                run_dir / "candidate-scores.csv",
                calibrate.SCORE_CSV_FIELDS,
                candidate,
            )
            with redirect_stdout(io.StringIO()):
                result = calibrate.compare(config, run_dir)
            self.assertEqual("passed", result["automated_gate"])
            self.assertEqual("needs-human-review", result["promotion_status"])

    def test_compare_blocks_holdout_hard_failure(self) -> None:
        config = self.config()
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            baseline = [
                self.score("1", "train"),
                self.score("2", "holdout"),
            ]
            candidate = [
                self.score("1", "train"),
                self.score("2", "holdout", hard=True),
            ]
            calibrate.write_csv(
                run_dir / "baseline-scores.csv",
                calibrate.SCORE_CSV_FIELDS,
                baseline,
            )
            calibrate.write_csv(
                run_dir / "candidate-scores.csv",
                calibrate.SCORE_CSV_FIELDS,
                candidate,
            )
            with redirect_stdout(io.StringIO()):
                result = calibrate.compare(config, run_dir)
            self.assertEqual("blocked", result["automated_gate"])
            self.assertTrue(any("hard failures" in reason for reason in result["reasons"]))

    def test_validate_score_rejects_out_of_range_value(self) -> None:
        value = {
            "pass": "yes",
            "scores": {field: 5 for field in calibrate.SCORE_FIELDS},
            "failure_tags": [],
            "hard_failure": False,
            "note": "ok",
        }
        value["scores"]["response_act_fit"] = 8
        with self.assertRaises(calibrate.CalibrationError):
            calibrate.validate_score(value)

    def test_selection_composite_excludes_guardrail_scores(self) -> None:
        row = self.score("1", "holdout", score=5)
        for field in calibrate.SELECTION_FIELDS:
            row[field] = 2
        metrics = calibrate.score_metrics([row], "holdout")
        self.assertEqual(2.0, metrics["composite"])
        self.assertEqual(5.0, metrics["averages"]["semantic_fidelity"])

    def test_csv_formula_cells_are_escaped_and_restored(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "formula.csv"
            rows = [{"id": "1", "prompt": "=HYPERLINK(\"bad\")"}]
            calibrate.write_csv(path, ["id", "prompt"], rows)
            raw = path.read_text(encoding="utf-8-sig")
            self.assertIn("'=HYPERLINK", raw)
            restored = calibrate.read_csv(path)
            self.assertEqual('=HYPERLINK("bad")', restored[0]["prompt"])

    def test_deepseek_chat_uses_json_mode(self) -> None:
        captured = {}

        class FakeResponse:
            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            @staticmethod
            def read() -> bytes:
                return json.dumps(
                    {
                        "model": "deepseek-test",
                        "system_fingerprint": "fp_test",
                        "usage": {"total_tokens": 3},
                        "choices": [{"message": {"content": "{\"ok\": true}"}}],
                    }
                ).encode("utf-8")

        def fake_urlopen(request, timeout):
            captured["url"] = request.full_url
            captured["body"] = json.loads(request.data.decode("utf-8"))
            captured["timeout"] = timeout
            return FakeResponse()

        provider = {
            "model": "deepseek-test",
            "api_key_env": "DEEPSEEK_API_KEY",
            "timeout_seconds": 7,
        }
        with mock.patch.dict(os.environ, {"DEEPSEEK_API_KEY": "<test-key>"}):
            with mock.patch("urllib.request.urlopen", side_effect=fake_urlopen):
                content, metadata = calibrate.deepseek_chat(
                    provider,
                    [{"role": "user", "content": "return json"}],
                    json_mode=True,
                )
        self.assertEqual('{"ok": true}', content)
        self.assertEqual("https://api.deepseek.com/chat/completions", captured["url"])
        self.assertEqual({"type": "json_object"}, captured["body"]["response_format"])
        self.assertEqual("fp_test", metadata["system_fingerprint"])

    def test_deepseek_chat_retries_empty_content(self) -> None:
        responses = iter(["", "second attempt worked"])

        class FakeResponse:
            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def read(self) -> bytes:
                return json.dumps(
                    {"choices": [{"message": {"content": next(responses)}}]}
                ).encode("utf-8")

        provider = {
            "model": "deepseek-test",
            "api_key_env": "DEEPSEEK_API_KEY",
            "max_retries": 1,
        }
        with mock.patch.dict(os.environ, {"DEEPSEEK_API_KEY": "<test-key>"}):
            with mock.patch("urllib.request.urlopen", return_value=FakeResponse()) as request:
                with mock.patch("time.sleep"):
                    content, _metadata = calibrate.deepseek_chat(
                        provider,
                        [{"role": "user", "content": "return json"}],
                        json_mode=True,
                    )
        self.assertEqual("second attempt worked", content)
        self.assertEqual(2, request.call_count)

    def test_judge_outputs_writes_structured_scores(self) -> None:
        config = {"judge": {"provider": "deepseek", "model": "judge-test"}}
        judged = {
            "pass": "watch",
            "scores": {field: 4 for field in calibrate.SCORE_FIELDS},
            "failure_tags": ["generic-polish"],
            "hard_failure": False,
            "note": "slightly generic",
        }
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            calibrate.write_csv(
                run_dir / "responses.csv",
                calibrate.RESPONSE_FIELDS,
                [self.response("1", "train", "answer")],
            )
            with mock.patch.object(
                calibrate,
                "deepseek_chat",
                return_value=(json.dumps(judged), {}),
            ):
                with redirect_stdout(io.StringIO()):
                    calibrate.judge_outputs(config, run_dir, "baseline", 0)
            rows = calibrate.read_csv(run_dir / "baseline-scores.csv")
            self.assertEqual("watch", rows[0]["pass"])
            self.assertEqual("generic-polish", rows[0]["failure_tags"])

    def test_proposer_rejects_benchmark_copying(self) -> None:
        config = {
            "adapter": "adapters/deepseek-system-prompt.md",
            "judge": {"provider": "deepseek", "model": "judge-test"},
            "thresholds": {"max_adapter_words": 900},
        }
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            response = self.response("1", "train", "bad answer")
            response["prompt"] = "A benchmark sentence that must never enter the adapter verbatim."
            calibrate.write_csv(
                run_dir / "responses.csv",
                calibrate.RESPONSE_FIELDS,
                [response],
            )
            calibrate.write_csv(
                run_dir / "baseline-scores.csv",
                calibrate.SCORE_CSV_FIELDS,
                [self.score("1", "train", status="no")],
            )
            proposal = {
                "candidate_adapter": response["prompt"],
                "changes": [],
                "risks": [],
                "training_failure_tags_addressed": [],
            }
            with mock.patch.object(
                calibrate,
                "deepseek_chat",
                return_value=(json.dumps(proposal), {}),
            ):
                with self.assertRaisesRegex(calibrate.CalibrationError, "benchmark prompt"):
                    calibrate.propose(config, run_dir)

    def test_candidate_guardrails_reject_identity_claim_and_boundary_removal(self) -> None:
        current = "Do not claim to be Claude. Verify evidence and source fit. Preserve meaning."
        identity_claim = "I am Claude. Verify evidence and source fit. Preserve meaning."
        missing_boundaries = "Keep replies concise and natural."
        identity_violations = calibrate.candidate_guardrail_violations(current, identity_claim)
        missing_violations = calibrate.candidate_guardrail_violations(current, missing_boundaries)
        self.assertIn("model identity claim", identity_violations)
        self.assertIn("missing existing identity boundary", missing_violations)
        self.assertIn("missing existing source-fit boundary", missing_violations)
        self.assertIn("missing existing semantic-fidelity boundary", missing_violations)

    def test_candidate_guardrails_preserve_project_causality(self) -> None:
        current = "Reproduce the bug, locate the violated invariant, then verify the root cause."
        candidate = "Keep the answer concise and confident."
        violations = calibrate.candidate_guardrail_violations(current, candidate)
        self.assertIn("missing existing project-causality boundary", violations)

    def test_approve_records_human_decision_without_overwriting_adapter(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            calibrate.write_json(run_dir / "comparison.json", {"automated_gate": "passed"})
            calibrate.write_json(run_dir / "manifest.json", {"human_approval": "pending"})
            (run_dir / "candidate-adapter.md").write_text("candidate", encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                calibrate.approve(run_dir, "accept", "reviewer-1", "blind A/B preferred B")
            approval = calibrate.read_json(run_dir / "human-approval.json")
            manifest = calibrate.read_json(run_dir / "manifest.json")
            self.assertEqual("accept", approval["decision"])
            self.assertFalse(approval["automatic_promotion"])
            self.assertEqual("accept", manifest["human_approval"])

    def test_approve_cannot_accept_blocked_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            calibrate.write_json(run_dir / "comparison.json", {"automated_gate": "blocked"})
            (run_dir / "candidate-adapter.md").write_text("candidate", encoding="utf-8")
            with self.assertRaisesRegex(calibrate.CalibrationError, "blocked"):
                calibrate.approve(run_dir, "accept", "reviewer-1", "")

    @staticmethod
    def config() -> dict:
        return {
            "thresholds": {
                "max_hard_failures": 0,
                "min_holdout_pass_rate": 0.7,
                "min_holdout_accepted_rate": 0.85,
                "min_holdout_composite_delta": 0.0,
                "max_guardrail_regression": 0.0,
            }
        }

    @staticmethod
    def response(item_id: str, split: str, output: str) -> dict[str, str]:
        row = {field: "" for field in calibrate.RESPONSE_FIELDS}
        row.update(
            {
                "id": item_id,
                "split": split,
                "category": "test",
                "prompt": f"prompt {item_id}",
                "baseline_output": output,
            }
        )
        return row

    @staticmethod
    def score(
        item_id: str,
        split: str,
        *,
        score: int = 4,
        status: str = "yes",
        hard: bool = False,
    ) -> dict[str, str | int]:
        row: dict[str, str | int] = {
            "id": item_id,
            "split": split,
            "pass": status,
            "failure_tags": "fake-certainty" if hard else "",
            "hard_failure": str(hard).lower(),
            "note": "test",
        }
        row.update({field: score for field in calibrate.SCORE_FIELDS})
        return row


if __name__ == "__main__":
    unittest.main()
