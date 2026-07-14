import hashlib
import json
from pathlib import Path


JOB_PATH = Path(
    "evidence/task_001/bluebutterfli-public-packet-verification-job-dry-run-v1.json"
)
RESULT_PATH = Path(
    "evidence/task_001/bluebutterfli-public-packet-verification-dry-run-result-v1.json"
)


def load_records():
    return json.loads(JOB_PATH.read_text()), json.loads(RESULT_PATH.read_text())


def test_dry_run_result_matches_the_job_and_current_input():
    job, result = load_records()
    input_path = Path(job["input_contract"]["repository_path"])
    observed_hash = hashlib.sha256(input_path.read_bytes()).hexdigest()

    assert result["job_id"] == job["job_id"]
    assert result["input_sha256_observed"] == observed_hash
    assert result["input_sha256_observed"] == job["input_contract"]["sha256"]
    assert job["internal_dry_run"]["result_path"] == str(RESULT_PATH)


def test_dry_run_result_records_all_five_checks_as_passed():
    job, result = load_records()
    expected_task_ids = {item["task_id"] for item in job["bounded_tasks"]}
    result_by_id = {item["task_id"]: item for item in result["task_results"]}

    assert set(result_by_id) == expected_task_ids
    assert all(item["status"] == "passed" for item in result_by_id.values())
    assert result["exceptions"] == []
    assert result["overall_status"] == "pass_candidate_for_human_acceptance"
    assert (
        result["limitation_statement"]
        == job["output_contract"]["required_limitation_statement"]
    )


def test_dry_run_result_used_no_external_agent_or_network_and_records_acceptance():
    _, result = load_records()
    acceptance = result["human_acceptance"]

    assert result["execution_mode"] == "local_internal_deterministic_check"
    assert result["network_used"] is False
    assert result["external_agent_used"] is False
    assert result["worker_type"] == "local_checker_not_an_external_or_registered_agent"
    assert acceptance["status"] == "accepted"
    assert acceptance["acceptance_authority"] == "Nancy M. Gregory"
    assert acceptance["decision"] == "accept_dry_run_record"
    assert acceptance["decision_date"] == "2026-07-14"
