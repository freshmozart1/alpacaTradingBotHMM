"""Exercise the real Bash workflow helper with offline gh/git/sleep stubs."""

import json
import os
from pathlib import Path
import subprocess
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
SHA = "a" * 40
NEW_SHA = "b" * 40
BRANCH = "claude/test-routine"
OUTDATED = "GraphQL: Head branch is out of date. (mergePullRequest)"

STUB = """#!/usr/bin/env python3
import json
import os
from pathlib import Path
import sys

state_path = Path(os.environ["STUB_STATE"])
state = json.loads(state_path.read_text())
tool = Path(sys.argv[0]).name
args = sys.argv[1:]
with open(os.environ["STUB_CALLS"], "a") as log:
    log.write(json.dumps([tool, *args]) + "\\n")

if tool == "gh" and args[:2] == ["pr", "view"]:
    kind = "confirm" if args[args.index("--json") + 1] == "state" else "view"
elif tool == "gh" and args[:2] in (["pr", "merge"], ["pr", "list"], ["pr", "create"]):
    kind = args[1]
elif tool == "git" and args[0] in ("push", "ls-remote"):
    kind = args[0]
elif tool == "sleep":
    sys.exit(0)
else:
    sys.exit("Unexpected stub command: " + repr([tool, *args]))

responses = state.get(kind, [])
if not responses:
    sys.exit("Unexpected stub call: " + kind)
response = responses.pop(0)
state_path.write_text(json.dumps(state))
sys.stdout.write(response.get("stdout", ""))
sys.stderr.write(response.get("stderr", ""))
sys.exit(response.get("code", 0))
"""


def response(stdout="", stderr="", code=0):
    return {"stdout": stdout, "stderr": stderr, "code": code}


def pr(state="OPEN", sha=SHA, mergeable="MERGEABLE", status="CLEAN"):
    return response("\t".join([state, sha, BRANCH, mergeable, status]) + "\n")


class MergeClaudeRoutineTest(unittest.TestCase):
    def run_shell(self, scenario, *, preflight=False):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)
            state_path = path / "state.json"
            calls_path = path / "calls.jsonl"
            state_path.write_text(json.dumps(scenario))
            for name in ("gh", "git", "sleep"):
                stub = path / name
                stub.write_text(STUB)
                stub.chmod(0o755)
            env = {
                **os.environ,
                "PATH": str(path) + os.pathsep + os.environ["PATH"],
                "STUB_STATE": str(state_path),
                "STUB_CALLS": str(calls_path),
                "BRANCH": BRANCH,
                "EXPECTED_SHA": SHA,
                "GITHUB_OUTPUT": str(path / "output"),
            }
            if preflight:
                # Execute the actual workflow step, including its PR creation gate.
                workflow = (ROOT / ".github/workflows/merge-claude-routine.yml").read_text()
                script = workflow.split("        run: |\n", 1)[1]
                script = textwrap.dedent(script.split("      - name:", 1)[0])
                cmd = ["bash", "-c", script]
            else:
                cmd = ["bash", str(ROOT / "scripts/merge-claude-routine.sh"), "217", SHA, BRANCH]
            result = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=10)
            calls = [json.loads(line) for line in calls_path.read_text().splitlines()]
            return result, calls

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def assert_failure(self, result):
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)

    def ready_scenario(self, **overrides):
        return {
            "view": [pr()],
            "merge": [response()],
            "confirm": [response("MERGED\n")],
            "push": [response()],
            **overrides,
        }

    def test_unknown_then_ready_pins_head_and_leases_delete(self):
        result, calls = self.run_shell(self.ready_scenario(view=[pr(mergeable="UNKNOWN", status="UNKNOWN"), pr()]))
        self.assert_success(result)
        self.assertIn(["sleep", "5"], calls)
        self.assertIn(["gh", "pr", "merge", "217", "--squash", "--match-head-commit", SHA], calls)
        self.assertIn(["git", "push", f"--force-with-lease=refs/heads/{BRANCH}:{SHA}", "origin", f":refs/heads/{BRANCH}"], calls)
        self.assertFalse(any("--delete-branch" in call for call in calls))

    def test_observed_out_of_date_error_retries_same_head(self):
        result, calls = self.run_shell(self.ready_scenario(view=[pr(), pr(), pr()], merge=[response(stderr=OUTDATED, code=1), response()]))
        self.assert_success(result)
        self.assertEqual(sum(call[:3] == ["gh", "pr", "merge"] for call in calls), 2)

    def test_superseded_head_before_merge_is_noop(self):
        result, calls = self.run_shell({"view": [pr(sha=NEW_SHA)], "ls-remote": [response(f"{NEW_SHA}\trefs/heads/{BRANCH}\n")]})
        self.assert_success(result)
        self.assertIn("superseded", result.stdout)
        self.assertEqual(len(calls), 2)

    def test_head_changed_during_merge_is_not_merged_or_deleted(self):
        result, calls = self.run_shell({"view": [pr(), pr(sha=NEW_SHA)], "merge": [response(stderr=OUTDATED, code=1)], "ls-remote": [response(f"{NEW_SHA}\trefs/heads/{BRANCH}\n")]})
        self.assert_success(result)
        self.assertIn("superseded", result.stdout)
        self.assertEqual(sum(call[:3] == ["gh", "pr", "merge"] for call in calls), 1)
        self.assertFalse(any(call[:2] == ["git", "push"] for call in calls))

    def test_lease_mismatch_during_merge_is_superseded_noop(self):
        result, calls = self.run_shell({"view": [pr(), pr(sha=NEW_SHA)], "merge": [response(stderr="GraphQL: Head commit changed", code=1)], "ls-remote": [response(f"{NEW_SHA}\trefs/heads/{BRANCH}\n")]})
        self.assert_success(result)
        self.assertIn("superseded", result.stdout)
        self.assertFalse(any(call[:2] == ["git", "push"] or call[0] == "sleep" for call in calls))

    def test_lagging_pr_head_waits_for_current_event(self):
        result, calls = self.run_shell(self.ready_scenario(view=[pr(sha=NEW_SHA), pr()], **{"ls-remote": [response(f"{SHA}\trefs/heads/{BRANCH}\n")]}))
        self.assert_success(result)
        self.assertIn("Waiting for PR", result.stdout)
        self.assertIn(["sleep", "5"], calls)

    def test_lagging_pr_head_after_outdated_error_waits_for_current_event(self):
        result, calls = self.run_shell(self.ready_scenario(view=[pr(), pr(sha=NEW_SHA), pr()], merge=[response(stderr=OUTDATED, code=1), response()], **{"ls-remote": [response(f"{SHA}\trefs/heads/{BRANCH}\n")]}))
        self.assert_success(result)
        self.assertEqual(sum(call[:3] == ["gh", "pr", "merge"] for call in calls), 2)

    def test_lagging_metadata_does_not_retry_unrelated_error(self):
        result, calls = self.run_shell({"view": [pr(), pr(sha=NEW_SHA)], "merge": [response(stderr="HTTP 403: permission denied", code=1)], "ls-remote": [response(f"{SHA}\trefs/heads/{BRANCH}\n")]})
        self.assert_failure(result)
        self.assertIn("permission denied", result.stderr)
        self.assertFalse(any(call[0] == "sleep" for call in calls))

    def test_mismatched_head_ref_failure_is_not_hidden(self):
        result, calls = self.run_shell({"view": [pr(sha=NEW_SHA)], "ls-remote": [response(stderr="fatal: authentication failed", code=128)]})
        self.assert_failure(result)
        self.assertIn("authentication failed", result.stderr)
        self.assertEqual(len(calls), 2)

    def test_old_merged_pr_does_not_claim_latest_live_head_merged(self):
        result, calls = self.run_shell({"view": [pr(state="MERGED", sha=NEW_SHA) for _ in range(12)], "ls-remote": [response(f"{SHA}\trefs/heads/{BRANCH}\n") for _ in range(12)]})
        self.assert_failure(result)
        self.assertIn("after 12 attempts", result.stderr)
        self.assertFalse(any(call[:2] == ["git", "push"] for call in calls))

    def test_already_merged_is_noop(self):
        result, calls = self.run_shell({"view": [pr(state="MERGED")]})
        self.assert_success(result)
        self.assertEqual(len(calls), 1)

    def test_merged_by_another_attempt_is_noop(self):
        result, calls = self.run_shell({"view": [pr(), pr(state="MERGED")], "merge": [response(stderr=OUTDATED, code=1)]})
        self.assert_success(result)
        self.assertFalse(any(call[0] == "git" for call in calls))

    def test_closed_pull_request_fails(self):
        result, calls = self.run_shell({"view": [pr(state="CLOSED")]})
        self.assert_failure(result)
        self.assertIn("state=CLOSED", result.stderr)
        self.assertEqual(len(calls), 1)

    def test_real_conflicts_fail_without_retry(self):
        result, calls = self.run_shell({"view": [pr(mergeable="CONFLICTING", status="DIRTY")]})
        self.assert_failure(result)
        self.assertIn("merge conflicts", result.stderr)
        self.assertEqual(len(calls), 1)

    def test_policy_states_fail_without_retry(self):
        for status in ("BLOCKED", "BEHIND", "DRAFT"):
            with self.subTest(status=status):
                result, calls = self.run_shell({"view": [pr(mergeable="UNKNOWN", status=status)]})
                self.assert_failure(result)
                self.assertIn(status, result.stderr)
                self.assertEqual(len(calls), 1)

    def test_policy_and_unrelated_merge_errors_fail_without_retry(self):
        for error in ("GraphQL: Protected branch rules not satisfied", "HTTP 403: Resource not accessible by integration", "GraphQL: Something else failed"):
            with self.subTest(error=error):
                result, calls = self.run_shell({"view": [pr(), pr()], "merge": [response(stderr=error, code=1)]})
                self.assert_failure(result)
                self.assertIn(error, result.stderr)
                self.assertFalse(any(call[0] in ("git", "sleep") for call in calls))

    def test_unknown_mergeability_exhaustion_is_bounded(self):
        result, calls = self.run_shell({"view": [pr(mergeable="UNKNOWN", status="UNKNOWN") for _ in range(12)]})
        self.assert_failure(result)
        self.assertIn("after 12 attempts", result.stderr)
        self.assertEqual(sum(call[0] == "sleep" for call in calls), 11)
        self.assertEqual(sum(call[:3] == ["gh", "pr", "view"] for call in calls), 12)

    def test_out_of_date_exhaustion_is_bounded(self):
        result, calls = self.run_shell({"view": [pr() for _ in range(24)], "merge": [response(stderr=OUTDATED, code=1) for _ in range(12)]})
        self.assert_failure(result)
        self.assertEqual(sum(call[:3] == ["gh", "pr", "merge"] for call in calls), 12)
        self.assertEqual(sum(call[0] == "sleep" for call in calls), 11)

    def test_status_api_failure_is_not_treated_as_superseded(self):
        result, calls = self.run_shell({"view": [response(stderr="HTTP 401: Bad credentials", code=1)]})
        self.assert_failure(result)
        self.assertIn("Bad credentials", result.stderr)
        self.assertEqual(len(calls), 1)

    def test_malformed_status_is_not_treated_as_superseded(self):
        result, calls = self.run_shell({"view": [response("OPEN\n")]})
        self.assert_failure(result)
        self.assertIn("Invalid", result.stderr)
        self.assertEqual(len(calls), 1)

    def test_status_failure_after_merge_error_is_not_hidden(self):
        result, calls = self.run_shell({"view": [pr(), response(stderr="HTTP 502", code=1)], "merge": [response(stderr=OUTDATED, code=1)]})
        self.assert_failure(result)
        self.assertIn("HTTP 502", result.stderr)
        self.assertFalse(any(call[0] in ("git", "sleep") for call in calls))

    def test_success_without_confirmed_merge_preserves_branch(self):
        result, calls = self.run_shell(self.ready_scenario(confirm=[response("OPEN\n")]))
        self.assert_failure(result)
        self.assertIn("merge was not confirmed", result.stderr)
        self.assertFalse(any(call[0] == "git" for call in calls))

    def test_confirmation_api_failure_preserves_branch(self):
        result, calls = self.run_shell(self.ready_scenario(confirm=[response(stderr="HTTP 502", code=1)]))
        self.assert_failure(result)
        self.assertFalse(any(call[0] == "git" for call in calls))

    def test_newer_push_after_merge_is_preserved_by_delete_lease(self):
        result, calls = self.run_shell(self.ready_scenario(push=[response(stderr="rejected (stale info)", code=1)], **{"ls-remote": [response(f"{NEW_SHA}\trefs/heads/{BRANCH}\n")]}))
        self.assert_success(result)
        self.assertIn("Keeping", result.stdout)
        self.assertEqual(sum(call[:2] == ["git", "push"] for call in calls), 1)

    def test_already_deleted_branch_is_success(self):
        result, _ = self.run_shell(self.ready_scenario(push=[response(stderr="remote ref does not exist", code=1)], **{"ls-remote": [response(code=2)]}))
        self.assert_success(result)
        self.assertIn("already deleted", result.stdout)

    def test_real_delete_failure_is_not_hidden(self):
        result, _ = self.run_shell(self.ready_scenario(push=[response(stderr="remote: permission denied", code=1)], **{"ls-remote": [response(f"{SHA}\trefs/heads/{BRANCH}\n")]}))
        self.assert_failure(result)
        self.assertIn("could not delete", result.stderr)

    def test_cleanup_ref_api_failure_is_not_hidden(self):
        result, _ = self.run_shell(self.ready_scenario(push=[response(stderr="rejected", code=1)], **{"ls-remote": [response(stderr="fatal: authentication failed", code=128)]}))
        self.assert_failure(result)
        self.assertIn("authentication failed", result.stderr)

    def test_stale_event_does_not_create_pr(self):
        result, calls = self.run_shell({"ls-remote": [response(f"{NEW_SHA}\trefs/heads/{BRANCH}\n")]}, preflight=True)
        self.assert_success(result)
        self.assertEqual(len(calls), 1)

    def test_deleted_event_branch_does_not_create_pr(self):
        result, calls = self.run_shell({"ls-remote": [response(code=2)]}, preflight=True)
        self.assert_success(result)
        self.assertEqual(len(calls), 1)

    def test_precreation_ref_failure_is_not_hidden(self):
        result, calls = self.run_shell({"ls-remote": [response(stderr="fatal: authentication failed", code=128)]}, preflight=True)
        self.assert_failure(result)
        self.assertIn("authentication failed", result.stderr)
        self.assertEqual(len(calls), 1)

    def test_current_event_creates_pr(self):
        result, calls = self.run_shell({"ls-remote": [response(f"{SHA}\trefs/heads/{BRANCH}\n")], "list": [response()], "create": [response("https://github.com/owner/repo/pull/217\n")]}, preflight=True)
        self.assert_success(result)
        self.assertTrue(any(call[:3] == ["gh", "pr", "create"] for call in calls))


if __name__ == "__main__":
    unittest.main()
