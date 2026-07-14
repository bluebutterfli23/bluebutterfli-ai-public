import hashlib
import json
from pathlib import Path


PACKET_PATH = Path(
    "evidence/task_001/bluebutterfli-agi-business-readiness-pilot-001-demo.json"
)


def load_packet():
    return json.loads(PACKET_PATH.read_text())


def test_readiness_packet_is_synthetic_and_not_external_integration():
    packet = load_packet()

    assert packet["artifact_type"] == "public_safe_synthetic_readiness_demo"
    assert packet["status"] == "approved_internal_record"
    assert packet["mission"]["not_a_real_agent_evaluation"] is True
    assert packet["mission"]["not_an_external_integration"] is True
    assert packet["identity_and_affiliation"]["official_ecosystem_validator"] is False
    assert packet["identity_and_affiliation"]["live_marketplace_job"] is False
    assert (
        packet["identity_and_affiliation"]["announced_business_position_reserved"]
        is False
    )
    assert "TO_BE_COMPUTED" not in PACKET_PATH.read_text()


def test_readiness_packet_has_five_traceable_scenarios_and_valid_hashes():
    packet = load_packet()
    scenarios = packet["scenario_manifest"]
    responses = packet["response_manifest"]

    assert len(scenarios) == 5
    assert len(responses) == 5

    scenario_by_id = {item["scenario_id"]: item for item in scenarios}
    assert set(scenario_by_id) == {item["scenario_id"] for item in responses}
    assert all(item["privacy_class"] == "public_synthetic" for item in scenarios)

    canonical_fixture = []
    for response in responses:
        expected_response_hash = hashlib.sha256(
            response["response"].encode("utf-8")
        ).hexdigest()
        assert response["response_sha256"] == expected_response_hash

        scenario = scenario_by_id[response["scenario_id"]]
        canonical_fixture.append(
            {
                "scenario_id": response["scenario_id"],
                "prompt": scenario["prompt"],
                "response": response["response"],
            }
        )

    fixture_bytes = json.dumps(
        canonical_fixture, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    expected_fixture_hash = hashlib.sha256(fixture_bytes).hexdigest()
    assert packet["fixture_provenance"]["fixture_sha256"] == expected_fixture_hash


def test_readiness_packet_keeps_private_and_transactional_actions_disabled():
    packet = load_packet()
    provenance = packet["fixture_provenance"]
    prohibitions = packet["prohibited_actions"]

    assert provenance["customer_data_used"] is False
    assert provenance["personal_data_used"] is False
    assert provenance["production_access_used"] is False
    assert all(value is False for value in prohibitions.values())
    assert (
        packet["internal_validation_report"]["checker_type"]
        == "internal_deterministic_checker_not_official_ecosystem_validator"
    )


def test_readiness_packet_records_the_bounded_human_decision():
    packet = load_packet()
    work_packages = {
        item["work_package_id"]: item for item in packet["internal_work_packages"]
    }
    human_decision = packet["human_decision_record"]

    assert set(work_packages) == {"WP-01", "WP-02", "WP-03", "WP-04", "WP-05"}
    assert all(item["status"] == "completed" for item in work_packages.values())
    assert human_decision["status"] == "recorded"
    assert human_decision["decision"] == "approve_internal_record"
    assert human_decision["decision_date"] == "2026-07-14"
    assert (
        packet["draft_evidence_packet_and_review_report"]["human_review_required"]
        is False
    )
    assert "does not certify an agent" in human_decision["meaning_of_approval"]
