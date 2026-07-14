import hashlib
import json
from pathlib import Path


JOB_PATH = Path(
    "evidence/task_001/bluebutterfli-public-packet-verification-job-dry-run-v1.json"
)


def load_job():
    return json.loads(JOB_PATH.read_text())


def test_job_is_an_unposted_internal_contract_not_an_official_protocol_job():
    job = load_job()
    marketplace = job["marketplace_boundary"]

    assert job["status"] == "ready_for_internal_dry_run_not_posted"
    assert job["job_format"] == "bluebutterfli_internal_contract_not_official_agi_jobs_schema"
    assert marketplace["posted_to_marketplace"] is False
    assert marketplace["live_protocol_job"] is False
    assert marketplace["official_schema_compatibility_claimed"] is False
    assert marketplace["external_worker_authorized"] is False
    assert all(value == "not_applicable" for value in job["economics"].values())


def test_job_uses_only_the_declared_public_synthetic_input():
    job = load_job()
    input_contract = job["input_contract"]
    input_path = Path(input_contract["repository_path"])
    observed_hash = hashlib.sha256(input_path.read_bytes()).hexdigest()
    packet = json.loads(input_path.read_text())

    assert observed_hash == input_contract["sha256"]
    assert input_contract["data_classification"] == "public_synthetic"
    assert input_contract["contains_customer_data"] is False
    assert input_contract["contains_personal_data"] is False
    assert input_contract["contains_private_review_results"] is False
    assert input_contract["read_only"] is True
    assert packet["artifact_type"] == "public_safe_synthetic_readiness_demo"
    assert packet["mission"]["not_a_real_agent_evaluation"] is True


def test_job_has_bounded_tasks_and_a_machine_readable_output_contract():
    job = load_job()
    task_ids = {item["task_id"] for item in job["bounded_tasks"]}
    output = job["output_contract"]

    assert task_ids == {"CHECK-01", "CHECK-02", "CHECK-03", "CHECK-04", "CHECK-05"}
    assert output["format"] == "json"
    assert set(output["required_fields"]) == {
        "job_id",
        "input_sha256_observed",
        "worker_identity",
        "worker_version",
        "execution_timestamp",
        "task_results",
        "exceptions",
        "overall_status",
        "limitation_statement",
    }
    assert "not a safety certification" in output["required_limitation_statement"]


def test_job_denies_external_authority_and_keeps_human_acceptance_locked():
    job = load_job()
    permissions = " ".join(job["worker_permissions"]["forbidden"])
    gate = job["acceptance_gate"]

    assert "customer, personal, confidential, or proprietary information" in permissions
    assert "sign transactions, move funds, use a wallet" in permissions
    assert "represent Bluebutterfli or claim ecosystem affiliation" in permissions
    assert gate["automated_output_is_final"] is False
    assert gate["human_acceptance_required"] is True
    assert gate["acceptance_authority"] == "Nancy M. Gregory"
    assert gate["current_decision"] == "not_executed"
    assert "has not been posted to a marketplace" in job["claim_boundary"]
