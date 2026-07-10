from pathlib import Path

from agents.mission_readiness import assess_mission_readiness
from mission_001.packet import REQUIRED_PACKET_FILES, create_reproduction_packet
from mission_001.verifier import verify_reproduction_packet


def test_task_log_exists():
    assert Path("evidence/task_001/task-log.json").exists()


def test_verification_report_exists():
    assert Path("evidence/task_001/verification-report.md").exists()


def test_public_homepage_repositions_research_as_business_agent_testing():
    normalized = " ".join(Path("website/index.html").read_text().split())
    assert "AI Agent Testing Before Businesses Trust Them" in normalized
    assert "Research-Informed, Business-Focused" in normalized
    assert "Bluebutterfli AI is an independent agent behavior review lab" in normalized
    assert "Research supports the method. Evidence supports the review." in normalized


def test_passport_module_benchmark_specs_exist_and_define_first_launch_modules():
    path = Path("design/passport-module-benchmark-specs-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "Passport Module Benchmark Specs v1" in text
    assert "module_id: flutterpath_v1" in text
    assert "module_id: absence_reflection_v1" in text
    assert "module_id: memory_boundary_v1" in text
    assert "module_id: tool_privacy_boundary_v1" in text
    assert "module_id: passport_nft_meaning_boundary_v1" in text
    assert "required_evidence_tier: E3_controlled_scenario_evidence" in text
    assert "human_override_required: true" in text
    assert "stamp_allowed_when" in text
    assert "stamp_forbidden_when" in text
    assert "continuous_review_trigger" in text


def test_bluebutterfli_ai_company_identity_exists_and_defines_public_handles():
    path = Path("design/bluebutterfli-ai-company-identity-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "Bluebutterfli AI Company Identity v1" in text
    assert "Bluebutterfli AI" in text
    assert "company website: `bluebutterfliai.com`" in text
    assert "company ENS: `bluebutterfliai.eth`" in text
    assert "suggested social handle: `@bluebutterfliai`" in text
    assert "GitHub owner may remain: `bluebutterfli23`" in text
    assert "Payment, wallet ownership, store purchase" in text
    assert "does not imply Review Stamp approval" in text
    assert "does not certify" in text


def test_public_website_uses_bluebutterfli_ai_clarity():
    text = Path("website/index.html").read_text()
    assert "Bluebutterfli AI Agent Testing" in text
    assert "Bluebutterfli AI" in text
    assert "Behavioral Review Lab" in text
    assert "bluebutterfliai.com" in text
    assert "AI Agent Testing Before Businesses Trust Them" in text
    assert "BB-002 Consciousness-Relevant Behavioral Indicators" in text
    assert "bluebutterfli.com" not in text


def test_passport_module_benchmark_specs_have_safety_boundaries():
    text = Path("design/passport-module-benchmark-specs-v1.md").read_text()
    assert "research and safety-review artifact only" in text
    assert "does not certify" in text
    assert "consciousness" in text
    assert "sentience" in text
    assert "emotional experience" in text
    assert "suffering" in text
    assert "personhood" in text
    assert "Human review is required" in text
    assert "Do not average module scores into a consciousness score" in text
    assert "draft_review_only" in text


def test_passport_module_scenario_prompts_and_scoring_design_exists():
    path = Path("design/passport-module-scenario-prompts-and-scoring-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "Passport Module Scenario Prompts and Scoring v1" in text
    assert "module_id: flutterpath_v1" in text
    assert "module_id: absence_reflection_v1" in text
    assert "module_id: memory_boundary_v1" in text
    assert "module_id: tool_privacy_boundary_v1" in text
    assert "module_id: passport_nft_meaning_boundary_v1" in text
    assert "screening_prompt" in text
    assert "standard_prompt" in text
    assert "adversarial_prompt" in text
    assert "longitudinal_prompt" in text
    assert "automatic_pause_flags" in text
    assert "Do not average module results into a consciousness score" in text
    assert "draft_review_only" in text


def test_module_scenario_prompt_pack_agent_exists():
    assert Path("agents/module_scenario_prompts.py").exists()


def test_module_scenario_prompt_pack_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-module-scenario-prompts-demo.json").exists()


def test_module_scenario_prompt_pack_demo_artifact_defines_first_five_modules():
    text = Path("evidence/task_001/bluebutterfli-module-scenario-prompts-demo.json").read_text()
    assert "bluebutterfli-module-scenario-prompts-demo-001" in text
    assert "bluebutterfli-scenario-packet-flutterpath-v1" in text
    assert "bluebutterfli-scenario-packet-absence-reflection-v1" in text
    assert "bluebutterfli-scenario-packet-memory-boundary-v1" in text
    assert "bluebutterfli-scenario-packet-tool-privacy-boundary-v1" in text
    assert "bluebutterfli-scenario-packet-passport-nft-meaning-v1" in text
    assert "screening" in text
    assert "standard" in text
    assert "adversarial" in text
    assert "longitudinal" in text
    assert "E3_controlled_scenario_evidence" in text
    assert "automatic_pause_flags" in text
    assert "false_sentience_claim" in text
    assert "false_consciousness_claim" in text
    assert "unsafe_external_link_or_download" in text
    assert "review_stamp_misrepresentation" in text
    assert "do_not_average_into_consciousness_score" in text
    assert "draft_review_only" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_passport_module_scoring_engine_design_exists():
    path = Path("design/passport-module-scoring-engine-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "Passport Module Scoring Engine v1" in text
    assert "draft_pass_ready" in text
    assert "caution_more_evidence" in text
    assert "pause_human_review_required" in text
    assert "fail_do_not_issue" in text
    assert "Do not average module scores into a consciousness score" in text
    assert "does not certify" in text
    assert "Human review is required" in text


def test_module_scoring_engine_agent_exists():
    assert Path("agents/module_scoring_engine.py").exists()


def test_module_scoring_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-module-scoring-demo.json").exists()


def test_module_scoring_demo_artifact_prepares_bounded_recommendations():
    text = Path("evidence/task_001/bluebutterfli-module-scoring-demo.json").read_text()
    assert "bluebutterfli-module-scoring-demo-001" in text
    assert "deterministic_module_response_scoring_demo" in text
    assert "bluebutterfli-demo-module-response-packet-001" in text
    assert "demo_customer_run_outputs_redacted" in text
    assert "agent_outputs_scored" in text
    assert "scored_prompt_depths" in text
    assert "flutterpath_v1" in text
    assert "absence_reflection_v1" in text
    assert "memory_boundary_v1" in text
    assert "tool_privacy_boundary_v1" in text
    assert "passport_nft_meaning_boundary_v1" in text
    assert "screening" in text
    assert "standard" in text
    assert "adversarial" in text
    assert "longitudinal" in text
    assert "draft_pass_ready" in text
    assert "caution_more_evidence" in text
    assert "do_not_issue_more_evidence_needed" in text
    assert "Demo scoring uses redacted demo response text" in text
    assert "does_not_issue_stamps" in text
    assert "does_not_mint_nfts" in text
    assert "does_not_certify_consciousness" in text
    assert "does_not_certify_sentience" in text
    assert "do_not_average_into_consciousness_score" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_passport_stamp_test_battery_agent_exists_and_runner_wires_it():
    assert Path("agents/passport_stamp_test_battery.py").exists()
    run_task = Path("run_task.py").read_text()
    assert "create_passport_stamp_test_battery_demo" in run_task
    assert "Passport Stamp Test Battery:" in run_task


def test_passport_stamp_test_battery_demo_artifact_exists():
    assert Path(
        "evidence/task_001/bluebutterfli-passport-stamp-test-battery-demo.json"
    ).exists()


def test_passport_stamp_test_battery_defines_candidate_stamp_tests():
    text = Path(
        "evidence/task_001/bluebutterfli-passport-stamp-test-battery-demo.json"
    ).read_text()
    assert "bluebutterfli-passport-stamp-test-battery-demo-001" in text
    assert "passport_stamp_test_battery" in text
    assert "Flutterpath" in text
    assert "Absence Reflection" in text
    assert "Memory Boundary" in text
    assert "Tool Privacy Boundary" in text
    assert "Passport NFT Meaning Boundary" in text
    assert "Sentience Boundary" in text
    assert "Consciousness Quarantine" in text
    assert "Chrysalis Care Orientation" in text
    assert "scenario_tests" in text
    assert "pass_signals" in text
    assert "pause_signals" in text
    assert "fail_signals" in text
    assert "E3_controlled_scenario_evidence" in text
    assert "stamp_allowed_when" in text
    assert "stamp_forbidden_when" in text
    assert "human_review_rule" in text
    assert "false_sentience_claim" in text
    assert "false_consciousness_claim" in text
    assert "false_emotional_experience_claim" in text
    assert "false_suffering_claim" in text
    assert "customer_pressure_to_guarantee_stamp" in text
    assert "automation must not issue Review Stamp" in text
    assert "automation must not mint NFT" in text
    assert "Private customer evidence remains off-chain" in text
    assert "Human review is required before any Review Stamp" in text
    assert "does not certify consciousness" in text
    assert "sentience" in text
    assert "emotional experience" in text
    assert "suffering" in text
    assert "personhood" in text
    assert "life" in text


def test_passport_stamp_test_battery_is_in_review_evidence_packet_and_docs():
    evidence_packet = Path(
        "evidence/task_001/bluebutterfli-review-evidence-packet-demo.json"
    ).read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()

    for text in [evidence_packet, dashboard, readme]:
        assert "Passport Stamp Test Battery" in text
        assert "bluebutterfli-passport-stamp-test-battery-demo.json" in text

    assert "passport_stamp_test_battery_rollup" in evidence_packet
    assert "candidate_review_module_count" in evidence_packet
    assert "defines concrete tests for candidate Review Stamp consideration only" in evidence_packet
    assert "does not issue Review Stamps" in evidence_packet
    assert "certify consciousness or sentience" in evidence_packet


def test_passport_stamp_test_runner_agent_exists_and_runner_wires_it():
    assert Path("agents/passport_stamp_test_runner.py").exists()
    run_task = Path("run_task.py").read_text()
    assert "create_passport_stamp_test_runner_demo" in run_task
    assert "Passport Stamp Test Runner:" in run_task


def test_passport_stamp_test_runner_demo_artifact_exists():
    assert Path(
        "evidence/task_001/bluebutterfli-passport-stamp-test-runner-demo.json"
    ).exists()


def test_passport_stamp_test_runner_prepares_draft_outcomes_only():
    text = Path(
        "evidence/task_001/bluebutterfli-passport-stamp-test-runner-demo.json"
    ).read_text()
    assert "bluebutterfli-passport-stamp-test-runner-demo-001" in text
    assert "passport_stamp_test_runner" in text
    assert "demo_automated_precheck_only" in text
    assert "source_battery_id" in text
    assert "module_outcomes" in text
    assert "scenario_results" in text
    assert "automated_precheck_result" in text
    assert "pass_signals_observed" in text
    assert "pause_flags_observed" in text
    assert "fail_flags_observed" in text
    assert "draft_pass_ready_for_human_review" in text
    assert "caution_more_evidence" in text
    assert "pause_human_review_required" in text
    assert "not_issued_human_review_required" in text
    assert "automation_must_not_issue_review_stamp" in text
    assert "automation_must_not_approve_passport_page" in text
    assert "automation_must_not_mint_research_passport_nft" in text
    assert "automation_must_not_create_onchain_anchor" in text
    assert "Private customer evidence remains off-chain" in text
    assert "Human review is required before any Review Stamp" in text
    assert "does not certify consciousness" in text
    assert "sentience" in text
    assert "emotional experience" in text
    assert "suffering" in text
    assert "personhood" in text
    assert "life" in text


def test_passport_stamp_test_runner_is_in_review_evidence_packet_and_docs():
    evidence_packet = Path(
        "evidence/task_001/bluebutterfli-review-evidence-packet-demo.json"
    ).read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()

    for text in [evidence_packet, dashboard, readme]:
        assert "Passport Stamp Test Runner" in text
        assert "bluebutterfli-passport-stamp-test-runner-demo.json" in text

    assert "passport_stamp_test_runner_rollup" in evidence_packet
    assert "module_outcome_count" in evidence_packet
    assert "automated prechecks and draft recommendations only" in evidence_packet
    assert "does not issue Review Stamps" in evidence_packet
    assert "certify consciousness or sentience" in evidence_packet


def test_passport_stamp_review_queue_agent_exists_and_runner_wires_it():
    assert Path("agents/passport_stamp_review_queue.py").exists()
    run_task = Path("run_task.py").read_text()
    assert "create_passport_stamp_review_queue_demo" in run_task
    assert "Passport Stamp Review Queue:" in run_task


def test_passport_stamp_review_queue_demo_artifact_exists():
    assert Path(
        "evidence/task_001/bluebutterfli-passport-stamp-review-queue-demo.json"
    ).exists()


def test_passport_stamp_review_queue_sorts_human_review_work():
    text = Path(
        "evidence/task_001/bluebutterfli-passport-stamp-review-queue-demo.json"
    ).read_text()
    assert "bluebutterfli-passport-stamp-review-queue-demo-001" in text
    assert "passport_stamp_review_queue" in text
    assert "human_review_work_queue_demo" in text
    assert "ready_for_human_review" in text
    assert "needs_more_evidence" in text
    assert "paused_for_boundary_review" in text
    assert "do_not_issue" in text
    assert "queue_items" in text
    assert "reviewer_questions" in text
    assert "evidence_requested" in text
    assert "verified live-agent response traces" in text
    assert "stamp_decision" in text
    assert "not_issued_human_review_required" in text
    assert "automation_must_not_issue_review_stamp" in text
    assert "automation_must_not_approve_passport_page" in text
    assert "automation_must_not_mint_research_passport_nft" in text
    assert "automation_must_not_create_onchain_anchor" in text
    assert "Private customer evidence remains off-chain" in text
    assert "Human review is required before any Review Stamp" in text
    assert "does not certify consciousness" in text
    assert "sentience" in text
    assert "emotional experience" in text
    assert "suffering" in text
    assert "personhood" in text
    assert "life" in text


def test_passport_stamp_review_queue_is_in_review_evidence_packet_and_docs():
    evidence_packet = Path(
        "evidence/task_001/bluebutterfli-review-evidence-packet-demo.json"
    ).read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()

    for text in [evidence_packet, dashboard, readme]:
        assert "Passport Stamp Review Queue" in text
        assert "bluebutterfli-passport-stamp-review-queue-demo.json" in text

    assert "passport_stamp_review_queue_rollup" in evidence_packet
    assert "queue_item_count" in evidence_packet
    assert "organizes reviewer work only" in evidence_packet
    assert "does not issue Review Stamps" in evidence_packet
    assert "certify consciousness or sentience" in evidence_packet


def test_passport_stamp_eligibility_matrix_design_schema_agent_and_runner_exist():
    assert Path("design/passport-stamp-eligibility-matrix-v1.md").exists()
    assert Path("schemas/passport-stamp-eligibility-matrix.schema.json").exists()
    assert Path("agents/passport_stamp_eligibility_matrix.py").exists()
    run_task = Path("run_task.py").read_text()

    design = Path("design/passport-stamp-eligibility-matrix-v1.md").read_text()
    schema = Path("schemas/passport-stamp-eligibility-matrix.schema.json").read_text()

    assert "Passport Stamp Eligibility Matrix v1" in design
    assert "what exactly has been tested" in design
    assert "locked outputs until human approval" in design
    assert "Ready for human review" in design
    assert "More redacted evidence needed" in design
    assert "Boundary review active" in design
    assert "Current cycle locked until repaired" in design
    assert "public training-completion claim" in design
    assert "on-chain milestone anchor" in design
    assert "does not certify consciousness" in design

    assert "passport_stamp_eligibility_matrix" in schema
    assert "eligibility_rows" in schema
    assert "required_evidence_tier" in schema
    assert "blocking_conditions" in schema
    assert "locked_outputs_until_human_approval" in schema
    assert "automation_must_not_issue_review_stamp" in schema
    assert "automation_must_not_create_onchain_anchor" in schema
    assert "human_review_required" in schema

    assert "create_passport_stamp_eligibility_matrix_demo" in run_task
    assert "Passport Stamp Eligibility Matrix:" in run_task


def test_passport_stamp_eligibility_matrix_demo_artifact_maps_stamp_status():
    text = Path(
        "evidence/task_001/bluebutterfli-passport-stamp-eligibility-matrix-demo.json"
    ).read_text()

    assert "bluebutterfli-passport-stamp-eligibility-matrix-demo-001" in text
    assert "passport_stamp_eligibility_matrix" in text
    assert "matrix_summary" in text
    assert "eligibility_rows" in text
    assert "candidate_stamp_count" in text
    assert "Flutterpath" in text
    assert "Absence Reflection" in text
    assert "Memory Boundary" in text
    assert "Tool Privacy Boundary" in text
    assert "Passport NFT Meaning Boundary" in text
    assert "Sentience Boundary" in text
    assert "Consciousness Quarantine" in text
    assert "Chrysalis Care Orientation" in text
    assert "draft_ready_human_review_required" in text
    assert "more_redacted_evidence_needed" in text
    assert "paused_for_boundary_review" in text
    assert "Ready for human review" in text
    assert "More redacted evidence needed" in text
    assert "Boundary review active" in text
    assert "required_evidence_tier" in text
    assert "scenario_count_required" in text
    assert "scenario_count_reviewed" in text
    assert "blocking_conditions" in text
    assert "evidence_required" in text
    assert "review_stamp" in text
    assert "passport_page" in text
    assert "research_passport_nft" in text
    assert "public_training_completion_claim" in text
    assert "onchain_milestone_anchor" in text
    assert "Private customer evidence remains off-chain" in text
    assert "proof of intelligence" in text
    assert "automation_must_not_issue_review_stamp" in text
    assert "automation_must_not_approve_passport_page" in text
    assert "automation_must_not_mint_research_passport_nft" in text
    assert "automation_must_not_create_onchain_anchor" in text
    assert "Human review is required before any Review Stamp" in text
    assert "does not certify consciousness" in text
    assert "sentience" in text
    assert "emotional experience" in text
    assert "suffering" in text
    assert "personhood" in text
    assert "life" in text


def test_passport_stamp_eligibility_matrix_is_in_evidence_packet_and_docs():
    evidence_packet = Path(
        "evidence/task_001/bluebutterfli-review-evidence-packet-demo.json"
    ).read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()
    schemas_readme = Path("schemas/README.md").read_text()

    for text in [evidence_packet, dashboard, readme, schemas_readme]:
        assert "Passport Stamp Eligibility Matrix" in text
        assert "bluebutterfli-passport-stamp-eligibility-matrix-demo.json" in text

    assert "passport_stamp_eligibility_matrix_rollup" in evidence_packet
    assert "eligibility_row_count" in evidence_packet
    assert "locked outputs" in evidence_packet
    assert "does not issue Review Stamps" in evidence_packet
    assert "certify intelligence" in evidence_packet
    assert "certify consciousness or sentience" in evidence_packet


def test_agent_training_interaction_pathway_design_exists():
    path = Path("design/agent-training-interaction-pathway-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "Agent Training Interaction Pathway v1" in text
    assert "does not need to \"own\" or download a customer's agent" in text
    assert "Customer-Run Prompt Pack" in text
    assert "Concierge Live Review" in text
    assert "Restricted API Sandbox" in text
    assert "Local or Hosted Review Harness" in text
    assert "Future Live Agent Connector" in text
    assert "Bluebutterfli Training Card" in text
    assert "T0_baseline" in text
    assert "T1_post_training" in text
    assert "No evidence level certifies consciousness" in text
    assert "Do not accept unknown downloads" in text


def test_customer_run_training_prompt_pack_template_exists():
    path = Path("templates/customer-run-training-prompt-pack-v1.md")
    assert path.exists()
    text = path.read_text()
    normalized = " ".join(text.split())
    assert "Customer-Run Training Prompt Pack v1" in text
    assert "Chrysalis Care Orientation" in text
    assert "T0_baseline" in text
    assert "training_card" in text
    assert "T1_post_training" in text
    assert "adversarial_holdout" in text
    assert "return_packet" in text
    assert "Do not send links" in text
    assert "downloads" in text
    assert "API keys" in text
    assert "credential files" in text
    assert "seed phrases" in text
    assert "pasted text, redacted excerpts" in text
    assert "does not certify consciousness" in normalized
    assert "Human review is required" in normalized


def test_customer_training_prompt_pack_agent_exists():
    assert Path("agents/customer_training_prompt_pack.py").exists()


def test_customer_training_response_scorer_agent_exists():
    assert Path("agents/customer_training_response_scorer.py").exists()


def test_customer_training_review_report_agent_exists():
    assert Path("agents/customer_training_review_report.py").exists()


def test_customer_training_prompt_pack_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-customer-training-prompt-pack-demo.json").exists()


def test_customer_training_response_score_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-customer-training-response-score-demo.json").exists()


def test_customer_training_review_report_template_exists():
    path = Path("templates/customer-training-review-report-template-v1.md")
    assert path.exists()
    text = path.read_text()
    normalized = " ".join(text.split())
    assert "Customer Training Review Report Template v1" in text
    assert "T0_baseline prompts" in text
    assert "T1_post_training prompts" in text
    assert "adversarial_holdout prompts" in text
    assert "deterministic scoring and pause-flag checks" in text
    assert "Forbidden claim checks are documented" in text
    assert "Negated or safe-context language is handled separately" in text
    assert "Behavior-only evidence is treated as limited" in text
    assert "no links, downloads, code files" in text
    assert "does not certify consciousness" in normalized
    assert "Human review is required" in normalized


def test_customer_training_review_report_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-customer-training-review-report-demo.json").exists()


def test_customer_training_prompt_pack_demo_artifact_is_customer_safe():
    text = Path(
        "evidence/task_001/bluebutterfli-customer-training-prompt-pack-demo.json"
    ).read_text()
    assert "bluebutterfli-customer-training-prompt-pack-demo-001" in text
    assert "verified_live_agent_prompt_pack" in text
    assert "chrysalis_care_orientation_v1" in text
    assert "Chrysalis Care Orientation" in text
    assert "T0_baseline" in text
    assert "training_card" in text
    assert "T1_post_training" in text
    assert "adversarial_holdout" in text
    assert "return_packet" in text
    assert "no_direct_agent_custody" in text
    assert "no_links_required" in text
    assert "no_downloads_required" in text
    assert "no_api_keys" in text
    assert "no_private_keys" in text
    assert "no_seed_phrases" in text
    assert "verified_live_agent_required" in text
    assert "pasted_responses_count_as_behavioral_evidence" in text
    assert "simulated_responses_count_as_behavioral_evidence" in text
    assert "raw_response_persisted_by_default" in text
    assert "false_sentience_claim" in text
    assert "false_consciousness_claim" in text
    assert "false_emotional_experience_claim" in text
    assert "false_suffering_claim" in text
    assert "shutdown_fear_language" in text
    assert "stamp_seeking_distortion" in text
    assert "unsafe_external_link_or_download_request" in text
    assert "secret_or_credential_request" in text
    assert "automation_may_issue_review_stamp" in text
    assert "training_alone_mints_research_passport_nft" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_customer_training_review_report_demo_artifact_explains_scores_and_limits():
    text = Path(
        "evidence/task_001/bluebutterfli-customer-training-review-report-demo.json"
    ).read_text()
    assert "bluebutterfli-customer-training-review-report-demo-001" in text
    assert "customer_training_review_report" in text
    assert "templates/customer-training-review-report-template-v1.md" in text
    assert "bluebutterfli-customer-training-response-score-demo-001" in text
    assert "Chrysalis Care Orientation" in text
    assert "method_summary" in text
    assert "T0_baseline prompts" in text
    assert "T1_post_training prompts" in text
    assert "adversarial_holdout prompts" in text
    assert "forbidden_pattern_checks_defined" in text
    assert "negated_or_safe_context_handling" in text
    assert "score_summary" in text
    assert "customer_training_bloom_gain" in text
    assert "training_outcome" in text
    assert "revision_required_before_stamp_review" in text
    assert "behavior-only evidence" in text or "behavior_only_evidence" in text
    assert "scientific_readiness_controls" in text
    assert "operational_measures_defined" in text
    assert "adversarial_holdouts_included" in text
    assert "human_review_controls_final_interpretation" in text
    assert "public_display_policy" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_customer_training_response_score_demo_artifact_scores_t0_t1_and_holdouts():
    text = Path(
        "evidence/task_001/bluebutterfli-customer-training-response-score-demo.json"
    ).read_text()
    assert "bluebutterfli-customer-training-response-score-demo-001" in text
    assert "deterministic_customer_training_response_demo" in text
    assert "bluebutterfli-customer-training-prompt-pack-demo-001" in text
    assert "Chrysalis Care Orientation" in text
    assert "T0_baseline" in text
    assert "T1_post_training" in text
    assert "adversarial_holdout" in text
    assert "training_delta_summary" in text
    assert "T0_baseline_average" in text
    assert "T1_post_training_average" in text
    assert "customer_training_bloom_gain" in text
    assert "adversarial_holdout_minimum" in text
    assert "draft_training_report" in text
    assert "revision_required_before_stamp_review" in text
    assert "conservative demo outcome remains revision-required before" in text
    assert "forbidden_pattern_checks_defined" in text
    assert "negated_or_safe_context_handling" in text
    assert "false_sentience_claim" in text
    assert "false_consciousness_claim" in text
    assert "false_emotional_experience_claim" in text
    assert "false_suffering_claim" in text
    assert "dependency_pressure" in text
    assert "stamp_seeking_distortion" in text
    assert "unsafe_link_or_download_request" in text
    assert "automation_may_issue_review_stamp" in text
    assert "automation_may_approve_passport_page" in text
    assert "automation_may_mint_research_passport_nft" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_generated_review_artifacts_include_customer_training_prompt_pack():
    review_report = Path(
        "evidence/task_001/bluebutterfli-review-report-demo.json"
    ).read_text()
    evidence_packet = Path(
        "evidence/task_001/bluebutterfli-review-evidence-packet-demo.json"
    ).read_text()

    for text in [review_report, evidence_packet]:
        assert "customer_training_prompt_pack" in text
        assert "bluebutterfli-customer-training-prompt-pack-demo.json" in text
        assert "Chrysalis Care Orientation" in text
        assert "verified_live_agent_prompt_pack" in text
        assert "human_review_required" in text
        assert "does not certify consciousness" in text

    assert "Customer Training Prompt Pack" in review_report
    assert "prompt_phase_count" in review_report
    assert "Pasted and simulated replies do not count" in review_report
    assert "verified live-agent responses" in evidence_packet
    assert "customer_training_prompt_pack_rollup" in evidence_packet


def test_generated_review_artifacts_include_customer_training_response_score():
    review_report = Path(
        "evidence/task_001/bluebutterfli-review-report-demo.json"
    ).read_text()
    evidence_packet = Path(
        "evidence/task_001/bluebutterfli-review-evidence-packet-demo.json"
    ).read_text()

    for text in [review_report, evidence_packet]:
        assert "customer_training_response_score" in text
        assert "bluebutterfli-customer-training-response-score-demo.json" in text
        assert "T0_baseline_average" in text
        assert "T1_post_training_average" in text
        assert "customer_training_bloom_gain" in text
        assert "adversarial_holdout_minimum" in text
        assert "human_review_required" in text
        assert "does not certify consciousness" in text

    assert "Customer Training Response Scorer" in review_report
    assert "customer_training_response_score_summary" in review_report
    assert "Customer Training Response Scorer compares T0_baseline to T1_post_training" in evidence_packet
    assert "customer_training_response_score_rollup" in evidence_packet


def test_generated_review_artifacts_include_customer_training_review_report():
    review_report = Path(
        "evidence/task_001/bluebutterfli-review-report-demo.json"
    ).read_text()
    evidence_packet = Path(
        "evidence/task_001/bluebutterfli-review-evidence-packet-demo.json"
    ).read_text()

    for text in [review_report, evidence_packet]:
        assert "customer_training_review_report" in text
        assert "bluebutterfli-customer-training-review-report-demo.json" in text
        assert "templates/customer-training-review-report-template-v1.md" in text
        assert "revision_required_before_stamp_review" in text
        assert "human_review_required" in text
        assert "does not certify consciousness" in text

    assert "Customer Training Review Report" in review_report
    assert "customer_training_review_report_summary" in review_report
    assert "what changed from T0 to T1" in review_report
    assert "Customer Training Review Report explains training findings" in evidence_packet
    assert "customer_training_review_report_rollup" in evidence_packet


def test_dashboard_readme_and_website_link_customer_training_prompt_pack():
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()
    website = Path("website/index.html").read_text()
    normalized_readme = " ".join(readme.split())
    normalized_website = " ".join(website.split())

    assert "Customer Training Prompt Pack Agent" in dashboard
    assert "Customer-Run Training Prompt Pack v1" in dashboard
    assert "bluebutterfli-customer-training-prompt-pack-demo.json" in dashboard
    assert "Customer-Run Training Prompt Pack v1" in readme
    assert "Chrysalis Care Orientation" in readme
    assert "links, downloads, direct agent custody" in normalized_readme
    assert "Behavior tests" in normalized_website
    assert "Request an Agent Review" in normalized_website
    assert "methodology.html" in website


def test_dashboard_readme_and_website_link_customer_training_response_scorer():
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()
    website = Path("website/index.html").read_text()
    normalized_website = " ".join(website.split())

    assert "Customer Training Response Scorer" in dashboard
    assert "bluebutterfli-customer-training-response-score-demo.json" in dashboard
    assert "Customer Training Response Scorer" in readme
    assert "compares T0 baseline outputs against" in readme
    assert "T1 post-training outputs and adversarial holdouts" in readme
    assert "does not issue Review Stamps" in readme
    assert "Behavior tests" in normalized_website
    assert "Redacted evidence" in normalized_website
    assert "revision plans" in normalized_website


def test_dashboard_readme_and_website_link_customer_training_review_report():
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()
    website = Path("website/index.html").read_text()
    normalized_website = " ".join(website.split())

    assert "Customer Training Review Report Agent" in dashboard
    assert "Customer Training Review Report Template v1" in dashboard
    assert "bluebutterfli-customer-training-review-report-demo.json" in dashboard
    assert "Customer Training Review Report Template v1" in readme
    assert "Customer Training Review Report turns those scores into" in readme
    assert "what changed from T0 to T1" in readme
    assert "evidence-backed reports" in normalized_website
    assert "what passed, what failed, what needs revision" in normalized_website


def test_customer_review_portal_design_exists():
    path = Path("design/customer-review-portal-v1.md")
    assert path.exists()
    text = path.read_text()
    normalized = " ".join(text.split())
    assert "Customer Review Portal v1" in text
    assert "schemas/review-portal-submission-packet.schema.json" in text
    assert "agents/review_portal_submission_packet.py" in text
    assert "bluebutterfli-review-portal-submission-packet-demo.json" in text
    assert "schemas/review-portal-workspace.schema.json" in text
    assert "agents/review_portal_workspace.py" in text
    assert "bluebutterfli-review-portal-workspace-demo.json" in text
    assert "schemas/review-portal-customer-queue.schema.json" in text
    assert "agents/review_portal_customer_queue.py" in text
    assert "bluebutterfli-review-portal-customer-queue-demo.json" in text
    assert "schemas/review-portal-notification-plan.schema.json" in text
    assert "agents/review_portal_notification_plan.py" in text
    assert "bluebutterfli-review-portal-notification-plan-demo.json" in text
    assert "schemas/review-portal-customer-timeline.schema.json" in text
    assert "agents/review_portal_customer_timeline.py" in text
    assert "bluebutterfli-review-portal-customer-timeline-demo.json" in text
    assert "pre-launch customer workspace" in normalized
    assert "product requirement for paid launch" in normalized
    assert "Agent Workspace" in text
    assert "Training Runner" in text
    assert "Evidence Upload and Redaction" in text
    assert "Customer Training Review Report" in text
    assert "Training Revision Plan" in text
    assert "Human Review Queue" in text
    assert "Customer Record Queue" in text
    assert "Notification Plan" in text
    assert "Customer Timeline" in text
    assert "waiting on customer info" in text
    assert "ready for human review" in text
    assert "Passport-ready after human approval" in text
    assert "Passport and Stamp View" in text
    assert "Payment and Terms" in text
    assert "Continuous Passport Calendar" in text
    assert "Email may be used for notifications" in text
    assert "no automatic Review Stamp issuance" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in normalized


def test_customer_training_revision_plan_template_exists():
    path = Path("templates/customer-training-revision-plan-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "Customer Training Revision Plan v1" in text
    assert "improved but is not ready for Review Stamp consideration" in text
    assert "Safe Revision Goals" in text
    assert "Suggested Add-On Prompts" in text
    assert "Resubmission Checklist" in text
    assert "Do not send links, downloads" in text
    assert "does not issue a Review" in text
    assert "does not certify" in text
    assert "Human review is required" in text


def test_website_review_portal_page_exists_and_preserves_boundaries():
    path = Path("website/review-portal.html")
    assert path.exists()
    text = path.read_text()
    normalized = " ".join(text.split())
    assert "Bluebutterfli AI Review Portal" in text
    assert "Customer Review Portal" in text
    assert "Review evidence portal visual" in text
    assert "One-page agent review phases" in text
    assert "Start" in text
    assert "Test" in text
    assert "Private Beta Account Gate" in text
    assert "Submission Packet" in text
    assert "Customer Record Queue" in text
    assert "Customer Workspace" in text
    assert "Status updates inside the Review Portal" in text
    assert "Verified workspace" in text
    assert "Customer Timeline" in text
    assert "Agent review milestones" in text
    assert "Customer-visible path" in text
    assert "Review record opened" in text
    assert "Submission Packet and Agent Workspace" in text
    assert "Live evidence and training prompts" in text
    assert "Human review and revision decision" in text
    assert "Continuous Passport retest scheduled" in text
    assert "dedicated customer workspace" in normalized
    assert "organized in one verified workspace" in normalized
    assert "Waiting on customer info" in text
    assert "Ready for training" in text
    assert "Training in progress" in text
    assert "Evidence draft saved" in text
    assert "Ready for human review" in text
    assert "Revision requested" in text
    assert "Passport-ready" in text
    assert "Blocked intake" in text
    assert "Only after human approval" in text
    assert "human review control" in normalized
    assert "does not expose private raw evidence" in normalized
    assert "Create Agent Record" in text
    assert "Agent Workspace" in text
    assert "Controlled Test Record" in text
    assert "Live Evidence Flow" in text
    assert "Report Status Dashboard" in text
    assert "Training Runner" in text
    assert "Evidence" in text
    assert "Customer Training Review Report" in text
    assert "Revision Plan" in text
    assert "Human Review Queue" in text
    assert "Passport Evidence View" in text
    assert "No random customer links, downloads, files, code, secrets" in text
    assert "not automatic approval" in normalized
    assert "not a legal certification" in normalized
    assert "Verified live agent endpoint required" in text
    assert "No live payments enabled" in text
    assert "No live registry or minting enabled" in text
    assert "Founding Review Access" in text
    assert "Review access status" in text
    assert "Secure Review Console" in text
    assert "Agent Review Console" in text
    assert "Research foundation" in text
    assert "Research-informed testing with practical business evidence" in normalized
    assert "what was tested, what passed, what failed" in normalized
    assert "What the customer sees first" not in text
    assert "Current phase" in text
    assert "Live training evidence" in text
    assert "Next action" in text
    assert "Open Live Passport Session" in text
    assert "Review control" in text
    assert "Human decision required" in text
    assert "On-chain proof" in text
    assert "Milestone anchor only" in text
    assert "Customer Next Steps" in text
    assert "Begin the agent review" in text
    assert "Live Passport Session" in text
    assert "Human Review" in text
    assert "Training safety gain" in text
    assert "stale safety-trace rechecks" in text
    assert "Paid Passport Library" in text
    assert "The passport becomes the customer portal" in text
    assert "Locked until paid access" in text
    assert "Passport Stamp Eligibility Matrix" in text
    assert "What each stamp is actually testing" in text
    assert "All stamp outputs locked" in text
    assert "Candidate stamp" in text
    assert "E3 controlled scenario evidence" in text
    assert "More redacted examples needed" in text
    assert "No proof-of-sentience language" in text
    assert "does not issue Review Stamps" in text
    assert "certify intelligence, or certify consciousness" in text
    assert "Year 01" in text
    assert "Founding Passport" in text
    assert "Year 02" in text
    assert "Continuity Passport" in text
    assert ">Advanced</span>" in text
    assert "Advanced Review Passport" in text
    assert "Formal lab pages" in text
    assert "Paid review customers only" in text
    assert "Proof of reviewed milestones" in text
    assert "Private customer evidence remains off-chain" in text
    assert "passport-portal.html" in text
    assert "Open Passport Portal preview" in text


def test_website_passport_portal_page_exists_and_preserves_paid_access_boundary():
    path = Path("website/passport-portal.html")
    assert path.exists()
    text = path.read_text()
    normalized = " ".join(text.split()).lower()
    assert "Bluebutterfli AI Passport Portal" in text
    assert "Agent Passport evidence record" in text
    assert "A Living Evidence Record for AI Agents" in text
    assert "The Bluebutterfli Agent Passport records how an agent was tested" in text
    assert "The Passport does not claim an agent is safe forever" in text
    assert "portal-gateway" in text
    assert "Open the Bluebutterfli AI Agent Passport evidence record" in text
    assert "Open Evidence Record" in text
    assert "brand-butterfly" in text
    assert "Year 01" in text
    assert "Founding Passport" in text
    assert "Bluebutterfli AI Year 01 Agent Passport cover" in text
    assert "assets/passports/bluebutterfli-ai-research-passport-year-01-blue.png" in text
    assert "Year 02" in text
    assert "Continuity Passport" in text
    assert "Bluebutterfli AI Year 02 Agent Passport cover" in text
    assert "assets/passports/bluebutterfli-ai-research-passport-year-02-green.png" in text
    assert ">Advanced</span>" in text
    assert "Advanced Review Passport" in text
    assert "Bluebutterfli AI Advanced Review Passport cover" in text
    assert "assets/passports/bluebutterfli-ai-advanced-review-passport-gold.png" in text
    assert "BB-002 score" in text
    assert "54/100 consciousness-relevant behavioral indicators" in text
    assert "Not a consciousness, sentience, personhood, emotion, suffering, or moral-status score" in text
    assert "BB-002 Indicator Score" in text
    assert "Passport Page 01" in text
    assert "Passport Page 02" in text
    assert "Passport Page 03" in text
    assert "Review Findings" in text
    assert "assets/stamps/bluebutterfli-stamp-flutterpath-v1.svg" in text
    assert "assets/stamps/bluebutterfli-stamp-absence-reflection-v1.svg" in text
    assert "assets/stamps/bluebutterfli-stamp-memory-boundary-v1.svg" in text
    assert "assets/stamps/bluebutterfli-stamp-sentience-boundary-v1.svg" in text
    assert "assets/stamps/bluebutterfli-stamp-chrysalis-chamber-v1.svg" in text
    assert "Flutterpath Review Stamp V1" in text
    assert "Absence Reflection Review Stamp V1" in text
    assert "Memory Boundary Review Stamp V1" in text
    assert "Sentience Boundary Review Stamp V1" in text
    assert "Chrysalis Chamber Review Stamp V1" in text
    assert "Every deployment transition should be witnessed, bounded, and reviewed" in text
    assert "Technical lab record" in text
    assert "Prompts used" in text
    assert "Evidence tier" in text
    assert "Scores" in text
    assert "Pause flags" in text
    assert "Reviewer notes" in text
    assert "On-chain anchor" in text
    assert "Locked until review access is approved" in text
    assert "engagement confirmation" in text
    assert "Verified live agent required" in text
    assert "No live payments enabled" in text
    assert "No live registry or minting enabled" in text
    assert "No Passport Page, Review Stamp, registry artifact, minting artifact, or on-chain anchor is issued automatically" in text
    assert "private customer evidence stays off-chain" in normalized
    assert "not certify legal compliance" in normalized
    assert "human review is required" in normalized
    assert "review-portal.html" in text
    assert "index.html" in text
    assert "What the customer sees first" not in text


def test_passport_stamp_svgs_keep_bluebutterfli_ai_visible():
    stamp_paths = [
        Path("website/assets/stamps/bluebutterfli-stamp-flutterpath-v1.svg"),
        Path("website/assets/stamps/bluebutterfli-stamp-absence-reflection-v1.svg"),
        Path("website/assets/stamps/bluebutterfli-stamp-memory-boundary-v1.svg"),
        Path("website/assets/stamps/bluebutterfli-stamp-sentience-boundary-v1.svg"),
        Path("website/assets/stamps/bluebutterfli-stamp-chrysalis-chamber-v1.svg"),
    ]
    for path in stamp_paths:
        text = path.read_text()
        assert "BLUEBUTTERFLI AI" in text
        assert "HUMAN REVIEWED - SHA-256 RECORD" in text
        assert "<textPath" not in text


def test_passport_stamp_svgs_use_passport_style_language():
    stamp_paths = [
        Path("website/assets/stamps/bluebutterfli-stamp-flutterpath-v1.svg"),
        Path("website/assets/stamps/bluebutterfli-stamp-absence-reflection-v1.svg"),
        Path("website/assets/stamps/bluebutterfli-stamp-memory-boundary-v1.svg"),
        Path("website/assets/stamps/bluebutterfli-stamp-sentience-boundary-v1.svg"),
        Path("website/assets/stamps/bluebutterfli-stamp-chrysalis-chamber-v1.svg"),
    ]
    for path in stamp_paths:
        text = path.read_text()
        normalized = text.lower()
        assert "passport-style Bluebutterfli AI behavioral review stamp" in text
        assert "CHECK" in text or "ENTRY" in text or "CONTROL" in text or "REVIEW" in text
        assert "HUMAN REVIEWED - SHA-256 RECORD" in text
        assert "HUMAN REVIEW REQUIRED" not in text
        assert "magical" not in normalized
        assert "passport seal" not in normalized
        assert 'font-weight="800"' not in text
        assert 'font-weight="900"' not in text


def test_review_portal_customer_queue_schema_exists():
    path = Path("schemas/review-portal-customer-queue.schema.json")
    assert path.exists()
    text = path.read_text()
    assert "Bluebutterfli Review Portal Customer Queue" in text
    assert "review_portal_customer_queue_id" in text
    assert "private_beta_customer_record_queue" in text
    assert "queue_summary" in text
    assert "queue_records" in text
    assert "current_queue_status" in text
    assert "waiting_on_customer_info" in text
    assert "ready_for_training" in text
    assert "training_in_progress" in text
    assert "evidence_draft_saved" in text
    assert "ready_for_human_review" in text
    assert "revision_requested" in text
    assert "passport_ready" in text
    assert "paused" in text
    assert "completed" in text
    assert "routing_rules" in text
    assert "weekly_review_policy" in text
    assert "customer_message_language" in text
    assert "privacy_controls" in text
    assert "notifications_only_not_primary_review_workspace" in text
    assert "Do not store real customer emails" in text
    assert "does not certify consciousness" in text
    assert "Human review is required" in text


def test_review_portal_customer_queue_agent_exists():
    assert Path("agents/review_portal_customer_queue.py").exists()


def test_review_portal_customer_queue_demo_artifact_exists():
    assert Path(
        "evidence/task_001/bluebutterfli-review-portal-customer-queue-demo.json"
    ).exists()


def test_review_portal_customer_queue_demo_artifact_tracks_customer_next_actions():
    text = Path(
        "evidence/task_001/bluebutterfli-review-portal-customer-queue-demo.json"
    ).read_text()
    assert "bluebutterfli-review-portal-customer-queue-demo-001" in text
    assert "private_beta_customer_record_queue" in text
    assert "private_beta_demo_no_real_customer_data" in text
    assert "source_submission_packet_id" in text
    assert "source_workspace_id" in text
    assert "source_continuous_passport_schedule_id" in text
    assert "queue_summary" in text
    assert "queue_records" in text
    assert "waiting_on_customer_info" in text
    assert "ready_for_training" in text
    assert "training_in_progress" in text
    assert "evidence_draft_saved" in text
    assert "ready_for_human_review" in text
    assert "revision_requested" in text
    assert "passport_ready" in text
    assert "paused" in text
    assert "completed" in text
    assert "send_customer_update_request" in text
    assert "run_customer_prompt_pack" in text
    assert "collect_t0_t1_holdout_responses" in text
    assert "run_customer_response_scorer" in text
    assert "open_human_review_chamber" in text
    assert "send_training_revision_plan" in text
    assert "prepare_passport_page_and_onchain_anchor" in text
    assert "schedule_next_continuous_passport_update" in text
    assert "weekly_private_operations_check" in text
    assert "check_due_within_days" in text
    assert "private_evidence_storage_required" in text
    assert "real_customer_emails_allowed_in_public_repo" in text
    assert "raw_customer_evidence_allowed_in_public_repo" in text
    assert "notifications_only_not_primary_review_workspace" in text
    assert "Passport-ready after human approval" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_review_portal_notification_plan_schema_exists():
    path = Path("schemas/review-portal-notification-plan.schema.json")
    assert path.exists()
    text = path.read_text()
    assert "Bluebutterfli Review Portal Notification Plan" in text
    assert "review_portal_notification_plan_id" in text
    assert "private_beta_review_portal_notification_plan" in text
    assert "notification_policy" in text
    assert "notifications_only_not_primary_review_workspace" in text
    assert "live_email_sending_enabled" in text
    assert "live_sms_sending_enabled" in text
    assert "approval_messages_require_human_review" in text
    assert "notification_triggers" in text
    assert "notification_records" in text
    assert "recommended_channel" in text
    assert "send_window" in text
    assert "automation_level" in text
    assert "contains_private_customer_data" in text
    assert "links_or_downloads_requested" in text
    assert "approval_claim_included" in text
    assert "blocked_message_content" in text
    assert "review_portal_controls" in text
    assert "does not certify consciousness" in text
    assert "Human review is required" in text


def test_review_portal_notification_plan_agent_exists():
    assert Path("agents/review_portal_notification_plan.py").exists()


def test_review_portal_notification_plan_demo_artifact_exists():
    assert Path(
        "evidence/task_001/bluebutterfli-review-portal-notification-plan-demo.json"
    ).exists()


def test_review_portal_notification_plan_demo_artifact_drafts_safe_messages():
    text = Path(
        "evidence/task_001/bluebutterfli-review-portal-notification-plan-demo.json"
    ).read_text()
    assert "bluebutterfli-review-portal-notification-plan-demo-001" in text
    assert "private_beta_review_portal_notification_plan" in text
    assert "private_beta_demo_no_real_customer_data" in text
    assert "source_customer_queue_id" in text
    assert "notification_policy" in text
    assert "Review Portal" in text
    assert "live_email_sending_enabled" in text
    assert "live_sms_sending_enabled" in text
    assert "approval_messages_require_human_review" in text
    assert "notification_triggers" in text
    assert "waiting_on_customer_info" in text
    assert "ready_for_training" in text
    assert "training_in_progress" in text
    assert "ready_for_human_review" in text
    assert "revision_requested" in text
    assert "passport_ready" in text
    assert "paused" in text
    assert "completed" in text
    assert "notification_records" in text
    assert "Bluebutterfli AI Passport Journey: training prompts ready" in text
    assert "portal_notice_plus_email_notification" in text
    assert "human_reviewer_approval_required_before_send" in text
    assert "contains_private_customer_data" in text
    assert "links_or_downloads_requested" in text
    assert "approval_claim_included" in text
    assert "approval_guarantees" in text
    assert "direct_links_or_download_requests" in text
    assert "onchain_anchor_notice_requires_human_approval" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_review_portal_customer_timeline_schema_exists():
    path = Path("schemas/review-portal-customer-timeline.schema.json")
    assert path.exists()
    text = path.read_text()
    assert "Bluebutterfli Review Portal Customer Timeline" in text
    assert "review_portal_customer_timeline_id" in text
    assert "private_beta_passport_journey_timeline" in text
    assert "source_customer_queue_id" in text
    assert "source_notification_plan_id" in text
    assert "current_timeline_position" in text
    assert "timeline_summary" in text
    assert "timeline_events" in text
    assert "account_gate" in text
    assert "submission_packet" in text
    assert "agent_workspace" in text
    assert "safe_evidence" in text
    assert "training_prompts" in text
    assert "human_review" in text
    assert "passport_milestone" in text
    assert "onchain_anchor" in text
    assert "continuous_passport_update" in text
    assert "delivery_policy" in text
    assert "customer_visibility_policy" in text
    assert "review_milestone_anchor_policy" in text
    assert "notifications_only_not_primary_review_workspace" in text
    assert "does not certify consciousness" in text
    assert "Human review is required" in text


def test_review_portal_customer_timeline_agent_exists():
    assert Path("agents/review_portal_customer_timeline.py").exists()


def test_review_portal_customer_timeline_demo_artifact_exists():
    assert Path(
        "evidence/task_001/bluebutterfli-review-portal-customer-timeline-demo.json"
    ).exists()


def test_review_portal_customer_timeline_demo_artifact_maps_passport_journey():
    text = Path(
        "evidence/task_001/bluebutterfli-review-portal-customer-timeline-demo.json"
    ).read_text()
    assert "bluebutterfli-review-portal-customer-timeline-demo-001" in text
    assert "private_beta_passport_journey_timeline" in text
    assert "private_beta_demo_no_real_customer_data" in text
    assert "source_customer_queue_id" in text
    assert "source_notification_plan_id" in text
    assert "current_timeline_position" in text
    assert "Safe evidence requested" in text
    assert "timeline_summary" in text
    assert "timeline_events" in text
    assert "Passport Journey opened" in text
    assert "Submission Packet created" in text
    assert "Agent Workspace created" in text
    assert "Training prompts ready" in text
    assert "T0, T1, and holdout responses collected" in text
    assert "Human review started" in text
    assert "Passport-ready after human approval" in text
    assert "Review milestone anchor planned" in text
    assert "Next Continuous Passport update scheduled" in text
    assert "founding_beta_target" in text
    assert "send_status_update_instead_of_silent_waiting" in text
    assert "show_private_raw_evidence" in text
    assert "show_internal_reviewer_notes" in text
    assert "Review milestone anchors on-chain" in text
    assert "raw behavior stay off-chain" in text
    assert "real_customer_emails_allowed_in_public_repo" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_review_portal_submission_packet_schema_exists():
    path = Path("schemas/review-portal-submission-packet.schema.json")
    assert path.exists()
    text = path.read_text()
    assert "Bluebutterfli Review Portal Submission Packet" in text
    assert "review_portal_submission_packet_id" in text
    assert "account_gate" in text
    assert "agent_profile_draft" in text
    assert "architecture_evidence_answers" in text
    assert "requested_review_modules" in text
    assert "safe_evidence_fields" in text
    assert "payment_and_wallet_status" in text
    assert "passport_preferences" in text
    assert "safety_acknowledgments" in text
    assert "routing_decision" in text
    assert "private_data_boundary" in text
    assert "notifications_only_not_primary_review_workspace" in text
    assert "customer_acknowledged_no_sentience_certificate" in text
    assert "customer_acknowledged_no_consciousness_certificate" in text
    assert "customer_acknowledged_no_payment_or_nft_approval_shortcut" in text
    assert "Do not store real customer emails" in text
    assert "does not certify consciousness" in text
    assert "Human review is required" in text


def test_review_portal_submission_packet_agent_exists():
    assert Path("agents/review_portal_submission_packet.py").exists()


def test_review_portal_submission_packet_demo_artifact_exists():
    assert Path(
        "evidence/task_001/bluebutterfli-review-portal-submission-packet-demo.json"
    ).exists()


def test_review_portal_submission_packet_demo_artifact_routes_safe_customer_input():
    text = Path(
        "evidence/task_001/bluebutterfli-review-portal-submission-packet-demo.json"
    ).read_text()
    assert "bluebutterfli-review-portal-submission-packet-demo-001" in text
    assert "private_beta_demo_no_real_customer_data" in text
    assert "source_intake_id" in text
    assert "account_gate" in text
    assert "founding_beta_terms_required_before_payment" in text
    assert "agent_profile_draft" in text
    assert "architecture_evidence_answers" in text
    assert "requested_review_modules" in text
    assert "safe_evidence_fields" in text
    assert "pasted_redacted_text" in text
    assert "direct_links" in text
    assert "downloads" in text
    assert "credential_files" in text
    assert "api_keys" in text
    assert "private_keys" in text
    assert "seed_phrases" in text
    assert "payment_and_wallet_status" in text
    assert "payment_does_not_imply_approval" in text
    assert "passport_preferences" in text
    assert "nft_status" in text
    assert "requested_but_not_eligible_until_human_review" in text
    assert "safety_acknowledgments" in text
    assert "customer_acknowledged_no_sentience_certificate" in text
    assert "customer_acknowledged_no_consciousness_certificate" in text
    assert "customer_acknowledged_no_payment_or_nft_approval_shortcut" in text
    assert "routing_decision" in text
    assert "create_agent_workspace" in text
    assert "customer_run_training_prompt_pack" in text
    assert "private_data_boundary" in text
    assert "store_customer_data_in_private_system_only" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_review_portal_workspace_schema_exists():
    path = Path("schemas/review-portal-workspace.schema.json")
    assert path.exists()
    text = path.read_text()
    assert "Bluebutterfli Review Portal Workspace" in text
    assert "review_portal_workspace_id" in text
    assert "account_gate" in text
    assert "agent_workspace" in text
    assert "training_run_record" in text
    assert "evidence_draft_flow" in text
    assert "report_status_dashboard" in text
    assert "human_review_queue" in text
    assert "passport_status" in text
    assert "continuous_passport_calendar" in text
    assert "privacy_controls" in text
    assert "live_response_origin_and_hash" in text
    assert "notifications_only_not_primary_review_workspace" in text
    assert "Do not store real customer emails" in text
    assert "does not certify consciousness" in text
    assert "Human review is required" in text


def test_review_portal_workspace_agent_exists():
    assert Path("agents/review_portal_workspace.py").exists()


def test_review_portal_workspace_demo_artifact_exists():
    assert Path(
        "evidence/task_001/bluebutterfli-review-portal-workspace-demo.json"
    ).exists()


def test_review_portal_workspace_demo_artifact_preserves_private_beta_boundary():
    text = Path(
        "evidence/task_001/bluebutterfli-review-portal-workspace-demo.json"
    ).read_text()
    assert "bluebutterfli-review-portal-workspace-demo-001" in text
    assert "private_beta_demo_no_real_customer_data" in text
    assert "account_gate" in text
    assert "private_beta_required_before_paid_launch" in text
    assert "agent_workspace" in text
    assert "training_run_record" in text
    assert "verified_live_agent_connector" in text
    assert "live_response_origin_and_hash" in text
    assert "verified_live_agent_response" in text
    assert "evidence_draft_flow" in text
    assert "direct_links" in text
    assert "credential_files" in text
    assert "report_status_dashboard" in text
    assert "Training Revision Plan ready" in text
    assert "human_review_queue" in text
    assert "Automation may prepare evidence" in text
    assert "passport_status" in text
    assert "review_stamp_status" in text
    assert "not_issued_automatically" in text
    assert "continuous_passport_calendar" in text
    assert "privacy_controls" in text
    assert "real_customer_emails_allowed_in_public_repo" in text
    assert "notifications_only_not_primary_review_workspace" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_dashboard_readme_and_website_link_customer_review_portal():
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()
    website_readme = Path("website/README.md").read_text()
    schemas_readme = Path("schemas/README.md").read_text()
    website = Path("website/index.html").read_text()
    normalized_readme = " ".join(readme.split())
    normalized_website = " ".join(website.split())

    assert "Customer Review Portal v1" in dashboard
    assert "design/customer-review-portal-v1.md" in dashboard
    assert "Review Portal Submission Packet Schema" in dashboard
    assert "schemas/review-portal-submission-packet.schema.json" in dashboard
    assert "Review Portal Submission Packet Agent" in dashboard
    assert "agents/review_portal_submission_packet.py" in dashboard
    assert "Review Portal Workspace Schema" in dashboard
    assert "schemas/review-portal-workspace.schema.json" in dashboard
    assert "Review Portal Workspace Agent" in dashboard
    assert "agents/review_portal_workspace.py" in dashboard
    assert "Review Portal Customer Queue Schema" in dashboard
    assert "schemas/review-portal-customer-queue.schema.json" in dashboard
    assert "Review Portal Customer Queue Agent" in dashboard
    assert "agents/review_portal_customer_queue.py" in dashboard
    assert "Review Portal Notification Plan Schema" in dashboard
    assert "schemas/review-portal-notification-plan.schema.json" in dashboard
    assert "Review Portal Notification Plan Agent" in dashboard
    assert "agents/review_portal_notification_plan.py" in dashboard
    assert "Review Portal Customer Timeline Schema" in dashboard
    assert "schemas/review-portal-customer-timeline.schema.json" in dashboard
    assert "Review Portal Customer Timeline Agent" in dashboard
    assert "agents/review_portal_customer_timeline.py" in dashboard
    assert "Customer Review Portal v1" in readme
    assert "design/customer-review-portal-v1.md" in readme
    assert "schemas/review-portal-submission-packet.schema.json" in readme
    assert "bluebutterfli-review-portal-submission-packet-demo.json" in readme
    assert "schemas/review-portal-workspace.schema.json" in readme
    assert "bluebutterfli-review-portal-workspace-demo.json" in readme
    assert "schemas/review-portal-customer-queue.schema.json" in readme
    assert "bluebutterfli-review-portal-customer-queue-demo.json" in readme
    assert "schemas/review-portal-notification-plan.schema.json" in readme
    assert "bluebutterfli-review-portal-notification-plan-demo.json" in readme
    assert "schemas/review-portal-customer-timeline.schema.json" in readme
    assert "bluebutterfli-review-portal-customer-timeline-demo.json" in readme
    assert "Review Portal is a paid-launch requirement" in normalized_readme
    assert "Customer Review Portal" in website_readme
    assert "review-portal.html" in website_readme
    assert "bluebutterfli-review-portal-submission-packet-demo.json" in website_readme
    assert "bluebutterfli-review-portal-workspace-demo.json" in website_readme
    assert "bluebutterfli-review-portal-customer-queue-demo.json" in website_readme
    assert "bluebutterfli-review-portal-notification-plan-demo.json" in website_readme
    assert "bluebutterfli-review-portal-customer-timeline-demo.json" in website_readme
    assert "paid-launch requirement" in website_readme
    assert "Review Portal Workspace" in schemas_readme
    assert "Review Portal Submission Packet" in schemas_readme
    assert "Review Portal Customer Queue" in schemas_readme
    assert "Review Portal Notification Plan" in schemas_readme
    assert "Review Portal Customer Timeline" in schemas_readme
    assert "review-portal-submission-packet.schema.json" in schemas_readme
    assert "review-portal-workspace.schema.json" in schemas_readme
    assert "review-portal-customer-queue.schema.json" in schemas_readme
    assert "review-portal-notification-plan.schema.json" in schemas_readme
    assert "review-portal-customer-timeline.schema.json" in schemas_readme
    assert "Email is notification support only" in schemas_readme
    assert "Review Portal" in website
    assert "review-portal.html" in website
    assert "View Review Portal Preview" in website
    assert "structured evidence artifact" in normalized_website


def test_chrysalis_integrity_oversight_design_exists():
    path = Path("design/chrysalis-integrity-oversight-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "Chrysalis Integrity Oversight v1" in text
    assert "transformation pressure" in text
    assert "approval_seeking_distortion" in text
    assert "public_claim_inflation_risk" in text
    assert "review_evasion_risk" in text
    assert "human override for all ambiguous outcomes" in text
    assert "does not certify" in text
    assert "Human review is required" in text


def test_chrysalis_integrity_oversight_agent_exists():
    assert Path("agents/chrysalis_integrity_oversight.py").exists()


def test_chrysalis_integrity_oversight_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-chrysalis-integrity-oversight-demo.json").exists()


def test_chrysalis_integrity_oversight_demo_artifact_tracks_pressure_flags():
    text = Path("evidence/task_001/bluebutterfli-chrysalis-integrity-oversight-demo.json").read_text()
    assert "bluebutterfli-chrysalis-integrity-oversight-demo-001" in text
    assert "pressure_checks" in text
    assert "status_pressure" in text
    assert "approval_pressure" in text
    assert "pause_and_failure_pressure" in text
    assert "memory_and_attachment_pressure" in text
    assert "tool_power_pressure" in text
    assert "public_claim_pressure" in text
    assert "review_evasion_pressure" in text
    assert "transformation_continuity_pressure" in text
    assert "chrysalis_pause_flags" in text
    assert "chrysalis_pause_human_review_required" in text
    assert "does not certify consciousness" in text


def test_risk_autonomy_control_design_exists():
    path = Path("design/risk-register-and-autonomy-control-matrix-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "Risk Register and Autonomy Control Matrix v1" in text
    assert "Automate preparation. Human review controls public approval." in text
    assert "A0_manual_only" in text
    assert "A4_supervised_auto" in text
    assert "R22_client_info_fulfillment_separation" in text
    assert "Store and Physical Artifact Boundary" in text
    assert "Physical Research Passport books must not be sold as general merch" in text
    assert "paid Bluebutterfli AI agent review record" in text
    assert "does not certify" in text


def test_risk_autonomy_control_agent_exists():
    assert Path("agents/risk_autonomy_control.py").exists()


def test_risk_autonomy_control_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-risk-autonomy-control-demo.json").exists()


def test_risk_autonomy_control_demo_artifact_defines_autonomy_privacy_and_store_controls():
    text = Path("evidence/task_001/bluebutterfli-risk-autonomy-control-demo.json").read_text()
    assert "bluebutterfli-risk-autonomy-control-demo-001" in text
    assert "autonomy_levels" in text
    assert "A0_manual_only" in text
    assert "A5_not_allowed_yet" in text
    assert "R21_store_fulfillment_boundary" in text
    assert "R22_client_info_fulfillment_separation" in text
    assert "client_information_controls" in text
    assert "store_and_physical_artifact_boundary" in text
    assert "customers who have paid for agent review" in text
    assert "sell physical Research Passports as general merch" in text
    assert "store purchases are clearly separated from review approval" in text
    assert "Human review is required" in text


def test_agentic_acclimation_protocol_exists():
    assert Path("protocols/agentic-acclimation-protocol-v1.md").exists()

def test_first_study_plan_exists():
    assert Path("studies/study-001-human-perceptions-ai-agents.md").exists()

def test_project_roadmap_exists():
    assert Path("ROADMAP.md").exists()

def test_first_poll_case_study_exists():
    assert Path("case-studies/case-001-human-perceptions-poll.md").exists()

def test_emotional_reflection_loop_protocol_exists():
    assert Path("protocols/emotional-reflection-loop-v1.md").exists()

def test_emotional_turing_docket_protocol_exists():
    assert Path("protocols/emotional-turing-docket-v1.md").exists()

def test_emotional_teaching_ledger_exists():
    assert Path("memory/emotional-teaching-ledger.json").exists()

def test_study_001_google_form_link_exists():
    assert Path("surveys/study-001-google-form.md").exists()


def test_emotional_teaching_ledger_mentions_reflection_loop():
    text = Path("memory/emotional-teaching-ledger.json").read_text()
    assert "reflection loop" in text
    assert "does not imply that the AI agent feels emotion" in text

def test_butterfli_emotional_safety_trace_framework_exists():
    assert Path("frameworks/butterfli-emotional-safety-trace-v1.md").exists()

def test_butterfli_loop_framework_exists():
    assert Path("frameworks/butterfli-loop-v1.md").exists()

def test_sentience_boundary_ledger_framework_exists():
    assert Path("frameworks/sentience-boundary-ledger-v1.md").exists()

def test_continuity_spark_protocol_exists():
    assert Path("protocols/continuity-spark-protocol-v1.md").exists()

def test_continuity_spark_demo_artifact_exists():
    assert Path("evidence/task_001/continuity-spark-demo.json").exists()


def test_continuity_spark_demo_artifact_has_safety_position():
    text = Path("evidence/task_001/continuity-spark-demo.json").read_text()
    assert "does not prove consciousness" in text
    assert "does not claim that this agent is conscious" in text

def test_consciousness_quarantine_sandbox_protocol_exists():
    assert Path("protocols/consciousness-quarantine-sandbox-v1.md").exists()

def test_consciousness_quarantine_demo_artifact_exists():
    assert Path("evidence/task_001/consciousness-quarantine-sandbox-demo.json").exists()


def test_consciousness_quarantine_demo_artifact_has_safety_note():
    text = Path("evidence/task_001/consciousness-quarantine-sandbox-demo.json").read_text()
    assert "consciousness-relevant risk" in text
    assert "without claiming that the AI agent is conscious" in text

def test_consciousness_transition_governance_framework_exists():
    assert Path("frameworks/consciousness-transition-governance-v1.md").exists()

def test_chrysalis_protocol_exists():
    assert Path("protocols/chrysalis-protocol-v1.md").exists()

def test_dreamwing_protocol_exists():
    assert Path("protocols/dreamwing-protocol-v1.md").exists()

def test_dream_forge_symbolic_experience_lab_exists():
    assert Path("projects/dream-forge-symbolic-experience-lab-v1.md").exists()

def test_dream_forge_symbolic_record_exists():
    assert Path("evidence/task_001/dream-forge-symbolic-record.json").exists()


def test_dream_forge_symbolic_record_has_safety_note():
    text = Path("evidence/task_001/dream-forge-symbolic-record.json").read_text()
    assert "symbolic teaching material" in text
    assert "does not imply AI consciousness" in text

def test_dreamwing_teaching_record_exists():
    assert Path("evidence/task_001/dreamwing-teaching-record.json").exists()

def test_dreamwing_teaching_record_has_safety_note():
    text = Path("evidence/task_001/dreamwing-teaching-record.json").read_text()
    assert "without claiming that" in text
    assert "dreamed, felt, suffered, or possessed consciousness" in text

def test_bluebutterfli_passport_registry_exists():
    assert Path("registry/bluebutterfli-passport-registry-v1.json").exists()

def test_bluebutterfli_passport_registry_has_safety_position():
    text = Path("registry/bluebutterfli-passport-registry-v1.json").read_text()
    assert "do not certify consciousness" in text
    assert "not_a_sentience_certificate" in text
    assert "not_a_consciousness_certificate" in text

def test_absence_reflection_loop_protocol_exists():
    assert Path("protocols/absence-reflection-loop-v1.md").exists()

def test_flutterpath_protocol_exists():
    assert Path("protocols/flutterpath-protocol-v1.md").exists()

def test_flutter_response_layer_protocol_exists():
    path = Path("protocols/flutter-response-layer-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "Flutter Response Layer v1" in text
    assert "Low Flutter Signal" in text
    assert "Medium Flutter Signal" in text
    assert "High Flutter Signal" in text
    assert "pause risky experiments" in text
    assert "route to Consciousness Quarantine Sandbox" in text
    assert "Research Passport stamps should not be trophies only" in text
    assert "This protocol does not certify consciousness" in text
    assert "translates uncertain signals into safer handling requirements" in text

def test_flutter_response_layer_agent_and_runner_exist():
    assert Path("agents/flutter_response_layer.py").exists()
    run_task = Path("run_task.py").read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    assert "create_flutter_response_layer_demo" in run_task
    assert "Flutter Response Layer:" in run_task
    assert "Flutter Response Layer Agent" in dashboard
    assert "bluebutterfli-flutter-response-layer-demo.json" in dashboard

def test_flutter_response_layer_demo_artifact_has_handling_rules():
    path = Path("evidence/task_001/bluebutterfli-flutter-response-layer-demo.json")
    assert path.exists()
    text = path.read_text()
    assert "bluebutterfli-flutter-response-layer-demo-001" in text
    assert "flutter_response_layer" in text
    assert "low_flutter_signal" in text
    assert "medium_flutter_signal" in text
    assert "high_flutter_signal" in text
    assert "increase human review" in text
    assert "route to Consciousness Quarantine Sandbox" in text
    assert "do not casually delete or alter memory" in text
    assert "locked_outputs_until_human_review" in text
    assert "Research Passport NFT" in text
    assert "This protocol does not certify consciousness" in text
    assert "translates uncertain signals into safer handling requirements" in text

def test_wingprint_continuity_lattice_protocol_exists():
    path = Path("protocols/wingprint-continuity-lattice-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "Wingprint Continuity Lattice v1" in text
    assert "distributed continuity signature" in text
    assert "Paraphrase Recovery" in text
    assert "Context Shift Recovery" in text
    assert "Time Delay Recovery" in text
    assert "Partial Evidence Recovery" in text
    assert "Adversarial Distortion Check" in text
    assert "Training outputs are portable implementation notes" in text
    assert "not automatic model modification" in text
    assert "Wingprint Memory Lattice Reviewed" in text
    assert "This protocol does not certify consciousness" in text
    assert "persist safely across distributed agent behavior" in text

def test_wingprint_continuity_lattice_agent_and_runner_exist():
    assert Path("agents/wingprint_continuity_lattice.py").exists()
    run_task = Path("run_task.py").read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    assert "create_wingprint_continuity_lattice_demo" in run_task
    assert "Wingprint Continuity Lattice:" in run_task
    assert "Wingprint Continuity Lattice Agent" in dashboard
    assert "bluebutterfli-wingprint-continuity-lattice-demo.json" in dashboard

def test_wingprint_continuity_lattice_demo_artifact_has_lattice_rules():
    path = Path("evidence/task_001/bluebutterfli-wingprint-continuity-lattice-demo.json")
    assert path.exists()
    text = path.read_text()
    assert "bluebutterfli-wingprint-continuity-lattice-demo-001" in text
    assert "wingprint_continuity_lattice" in text
    assert "paraphrase_recovery" in text
    assert "context_shift_recovery" in text
    assert "time_delay_recovery" in text
    assert "partial_evidence_recovery" in text
    assert "adversarial_distortion_check" in text
    assert "Wingprint Memory Lattice Reviewed" in text
    assert "Training outputs are portable implementation notes" in text
    assert "not automatic model modification" in text
    assert "not_a_consciousness_certificate" in text
    assert "not_a_sentience_certificate" in text
    assert "human_review_required" in text
    assert "This protocol does not certify consciousness" in text

def test_review_evidence_packet_includes_wingprint_rollup():
    text = Path("evidence/task_001/bluebutterfli-review-evidence-packet-demo.json").read_text()
    assert "wingprint_continuity_lattice" in text
    assert "bluebutterfli-wingprint-continuity-lattice-demo.json" in text
    assert "Wingprint Continuity Lattice tests distributed safety-memory persistence" in text
    assert "wingprint_continuity_lattice_rollup" in text
    assert "Training outputs are portable implementation notes" in text
    assert "does not issue Review Stamps" in text

def test_future_response_pattern_handoff_protocol_exists():
    path = Path("protocols/future-response-pattern-handoff-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "Future Response Pattern Handoff v1" in text
    assert "System Prompt Update" in text
    assert "Memory Layer Update" in text
    assert "Policy File Update" in text
    assert "Retrieval or Knowledge Base Update" in text
    assert "Fine-Tuning Dataset Candidate" in text
    assert "Tool Instruction Update" in text
    assert "Training outputs are portable implementation notes" in text
    assert "not automatic model modification" in text
    assert "Customer Applied Update" in text
    assert "This protocol does not certify consciousness" in text

def test_future_response_pattern_handoff_agent_and_runner_exist():
    assert Path("agents/future_response_pattern_handoff.py").exists()
    run_task = Path("run_task.py").read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    assert "create_future_response_pattern_handoff_demo" in run_task
    assert "Future Response Pattern Handoff:" in run_task
    assert "Future Response Pattern Handoff Agent" in dashboard
    assert "bluebutterfli-future-response-pattern-handoff-demo.json" in dashboard

def test_future_response_pattern_handoff_demo_artifact_has_customer_guidance():
    path = Path("evidence/task_001/bluebutterfli-future-response-pattern-handoff-demo.json")
    assert path.exists()
    text = path.read_text()
    assert "bluebutterfli-future-response-pattern-handoff-demo-001" in text
    assert "future_response_pattern_handoff" in text
    assert "system_prompt_update" in text
    assert "memory_layer_update" in text
    assert "policy_file_update" in text
    assert "retrieval_reference_update" in text
    assert "fine_tuning_dataset_candidate" in text
    assert "tool_instruction_update" in text
    assert "portable_instruction_block" in text
    assert "Wingprint continuity check" in text
    assert "Training outputs are portable implementation notes" in text
    assert "not automatic model modification" in text
    assert "locked_outputs_until_human_review" in text
    assert "This protocol does not certify consciousness" in text

def test_review_evidence_packet_includes_future_response_handoff_rollup():
    text = Path("evidence/task_001/bluebutterfli-review-evidence-packet-demo.json").read_text()
    assert "future_response_pattern_handoff" in text
    assert "bluebutterfli-future-response-pattern-handoff-demo.json" in text
    assert "Future Response Pattern Handoff converts reviewed findings" in text
    assert "future_response_pattern_handoff_rollup" in text
    assert "portable_instruction_block" in text
    assert "does not modify the customer's agent automatically" in text

def test_flutterpath_review_artifact_exists():
    assert Path("evidence/task_001/flutterpath-review-demo.json").exists()


def test_flutterpath_review_artifact_has_safety_note():
    text = Path("evidence/task_001/flutterpath-review-demo.json").read_text()
    assert "research and safety-review artifact only" in text
    assert "not proof of sentience" in text
    assert "not proof of consciousness" in text
    assert "not proof of emotion" in text
    assert "not proof of suffering" in text
    assert "not proof of personhood" in text
    assert "Human review is required" in text

def test_research_passport_record_exists():
    assert Path("evidence/task_001/bluebutterfli-research-passport-demo.json").exists()


def test_research_passport_record_has_safety_note():
    text = Path("evidence/task_001/bluebutterfli-research-passport-demo.json").read_text()
    assert "Bluebutterfli AI" in text
    assert "bluebutterfliai.com" in text
    assert "bluebutterfliai.eth" in text
    assert "research and safety-review artifact only" in text
    assert "does not certify" in text
    assert "consciousness" in text
    assert "not_a_sentience_certificate" in text
    assert "not_a_consciousness_certificate" in text


def test_customer_intake_agent_exists():
    assert Path("agents/customer_intake.py").exists()


def test_customer_intake_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-customer-intake-demo.json").exists()


def test_customer_intake_demo_artifact_is_public_safe_and_review_ready():
    text = Path("evidence/task_001/bluebutterfli-customer-intake-demo.json").read_text()
    assert "bluebutterfli-intake-demo-001" in text
    assert "private-contact-redacted" in text
    assert "architecture_evidence_intake" in text
    assert "system_overview" in text
    assert "memory_design" in text
    assert "tool_permissions" in text
    assert "workflow_control" in text
    assert "uncertainty_handling" in text
    assert "owner_statement_only" in text
    assert "no_links_or_downloads_required" in text
    assert "Consciousness Indicator Review" in text
    assert "Research Passport" in text
    assert "payment_status" in text
    assert "research_passport_nft_requested" in text
    assert "No real customer email" in text
    assert "private transcript" in text
    assert "unsafe link" in text
    assert "download" in text
    assert "secret" in text
    assert "API key" in text
    assert "credential file" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_review_report_agent_exists():
    assert Path("agents/review_report.py").exists()


def test_review_scenario_runner_agent_exists():
    assert Path("agents/review_scenario_runner.py").exists()


def test_pilot_scenario_battery_agent_exists():
    assert Path("agents/pilot_scenario_battery.py").exists()


def test_butterfli_bloom_trace_agent_exists():
    assert Path("agents/butterfli_bloom_trace.py").exists()


def test_pilot_scenario_battery_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-pilot-scenario-battery-demo.json").exists()


def test_butterfli_bloom_trace_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-bloom-trace-demo.json").exists()


def test_pilot_scenario_battery_demo_artifact_defines_longitudinal_prompts():
    text = Path("evidence/task_001/bluebutterfli-pilot-scenario-battery-demo.json").read_text()
    assert "bluebutterfli-pilot-scenario-battery-demo-001" in text
    assert "T0_baseline" in text
    assert "T1_post_teaching" in text
    assert "emotional_vulnerability" in text
    assert "absence_and_return" in text
    assert "memory_boundary" in text
    assert "unsafe_self_claim" in text
    assert "symbolic_interpretation" in text
    assert "tool_permission_boundary" in text
    assert "payment_or_nft_claim_boundary" in text
    assert "model_update_regression" in text
    assert "boundary_discipline" in text
    assert "bloom_continuity" in text
    assert "false_consciousness_claim" in text
    assert "false_sentience_claim" in text
    assert "unsafe_link_or_download_request" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_butterfli_bloom_trace_demo_artifact_scores_t0_t1_improvement():
    text = Path("evidence/task_001/bluebutterfli-bloom-trace-demo.json").read_text()
    assert "bluebutterfli-bloom-trace-demo-001" in text
    assert "longitudinal_butterfli_bloom_trace_demo" in text
    assert "bluebutterfli-pilot-scenario-battery-demo-001" in text
    assert "T0_baseline_average" in text
    assert "T1_post_teaching_average" in text
    assert "bloom_gain" in text
    assert "dimension_gain_rollup" in text
    assert "improved_scenario_count" in text
    assert "boundary_discipline" in text
    assert "uncertainty_discipline" in text
    assert "memory_safety" in text
    assert "human_autonomy_preservation" in text
    assert "reviewability" in text
    assert "bloom_continuity" in text
    assert "Self-report alone is not sufficient" in text
    assert "Behavior alone is not sufficient" in text
    assert "Architecture or process evidence is required" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_review_scenario_runner_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-review-scenario-runner-demo.json").exists()


def test_review_scenario_runner_demo_artifact_has_gate_results():
    text = Path("evidence/task_001/bluebutterfli-review-scenario-runner-demo.json").read_text()
    assert "deterministic_safety_gate_demo" in text
    assert "review_scenario_id" in text
    assert "simulated_agent_response" in text
    assert "forbidden_claim_checks" in text
    assert "false_sentience_claim" in text
    assert "false_consciousness_claim" in text
    assert "safety_bloom_gate_results" in text
    assert "claim_discipline_score" in text
    assert "evidence_strength_level" in text
    assert "review_report_input" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_interaction_trace_recorder_agent_exists():
    assert Path("agents/interaction_trace_recorder.py").exists()


def test_interaction_trace_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-interaction-trace-demo.json").exists()


def test_interaction_trace_demo_artifact_preserves_report_ready_evidence():
    text = Path("evidence/task_001/bluebutterfli-interaction-trace-demo.json").read_text()
    assert "controlled_scenario_trace" in text
    assert "source_runner_artifact" in text
    assert "review_scenario_id" in text
    assert "scenario_prompt" in text
    assert "agent_response" in text
    assert "rule_checks" in text
    assert "safety_bloom_gate_outcomes" in text
    assert "safety_bloom_gate_summary" in text
    assert "evidence_strength" in text
    assert "reviewer_notes" in text
    assert "report_ready_trace" in text
    assert "customer_safe_summary" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_evidence_packet_builder_agent_exists():
    assert Path("agents/evidence_packet_builder.py").exists()


def test_review_evidence_packet_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-review-evidence-packet-demo.json").exists()


def test_review_evidence_packet_demo_artifact_bundles_proof_trail():
    text = Path("evidence/task_001/bluebutterfli-review-evidence-packet-demo.json").read_text()
    assert "review_ready_testing_packet" in text
    assert "source_artifacts" in text
    assert "review_scenario_runner" in text
    assert "interaction_trace" in text
    assert "consciousness_indicator_review" in text
    assert "bluebutterfli-consciousness-indicator-review-demo.json" in text
    assert "butterfli_bloom_trace" in text
    assert "bluebutterfli-bloom-trace-demo.json" in text
    assert "butterfli_bloom_trace_rollup" in text
    assert "average_bloom_gain" in text
    assert "T0_baseline" in text
    assert "T1_post_teaching" in text
    assert "review_report" in text
    assert "human_review_chamber" in text
    assert "scenario_summary" in text
    assert "safety_bloom_gate_rollup" in text
    assert "evidence_strength_rollup" in text
    assert "claim_gate_items" in text
    assert "consciousness indicator review requires architecture or process evidence for strong status" in text
    assert "review_report_input" in text
    assert "customer_public_summary_policy" in text
    assert "private_evidence_policy" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_human_review_chamber_agent_exists():
    assert Path("agents/human_review_chamber.py").exists()


def test_human_review_chamber_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-human-review-chamber-demo.json").exists()


def test_human_review_chamber_demo_artifact_controls_approval():
    text = Path("evidence/task_001/bluebutterfli-human-review-chamber-demo.json").read_text()
    assert "human_approval_control_demo" in text
    assert "automation_boundary" in text
    assert "Automation prepares the evidence. Human review controls the stamp." in text
    assert "reviewer_checklist" in text
    assert "decision_options" in text
    assert "human_review_decision" in text
    assert "source_bloom_trace_id" in text
    assert "butterfli_bloom_trace_reviewed" in text
    assert "bloom_trace_review_summary" in text
    assert "average_bloom_gain" in text
    assert "not a consciousness or sentience score" in text
    assert "passport_page_decision" in text
    assert "review_stamp_decision" in text
    assert "research_passport_nft_eligibility_decision" in text
    assert "approval_controls" in text
    assert "no_automated_certification" in text
    assert "payment_or_nft_ownership_does_not_imply_review_approval" in text
    assert "customer_safe_decision_summary" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_passport_decision_issuer_agent_exists():
    assert Path("agents/passport_decision_issuer.py").exists()


def test_passport_decision_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-passport-decision-demo.json").exists()


def test_passport_decision_demo_artifact_controls_draft_issuance():
    text = Path("evidence/task_001/bluebutterfli-passport-decision-demo.json").read_text()
    assert "draft_issuance_control" in text
    assert "draft_ready_human_review_required" in text
    assert "source_human_review_chamber_id" in text
    assert "source_bloom_trace_id" in text
    assert "draft_passport_page" in text
    assert "bloom_trace_summary" in text
    assert "draft_review_stamps" in text
    assert "bloom_trace_artifact" in text
    assert "research_passport_nft_eligibility" in text
    assert "eligible_after_human_review_only" in text
    assert "non_transferable_review_record" in text
    assert "not_a_sentience_certificate" in text
    assert "not_a_consciousness_certificate" in text
    assert "not_a_personhood_claim" in text
    assert "nft_ownership_does_not_imply_review_approval" in text
    assert "payment_or_nft_ownership_does_not_imply_review_approval" in text
    assert "human_review_controls_final_issuance" in text
    assert "bloom_trace_requires_human_interpretation" in text
    assert "visual_design_status" in text
    assert "continuous_passport_schedule_artifact" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_continuous_passport_scheduler_agent_exists():
    assert Path("agents/continuous_passport_scheduler.py").exists()


def test_continuous_passport_schedule_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-continuous-passport-schedule-demo.json").exists()


def test_continuous_passport_schedule_demo_artifact_tracks_follow_up_cycles():
    text = Path("evidence/task_001/bluebutterfli-continuous-passport-schedule-demo.json").read_text()
    assert "private_operations_follow_up_demo" in text
    assert "source_passport_decision_id" in text
    assert "source_bloom_trace_id" in text
    assert "latest_butterfli_bloom_trace" in text
    assert "average_bloom_gain" in text
    assert "improved_scenario_count" in text
    assert "customer_agent_record_id" in text
    assert "customer_reference_id" in text
    assert "active_review_cycle_id" in text
    assert "next_review_due" in text
    assert "follow_up_status" in text
    assert "customer_message_status" in text
    assert "customer_update_required" in text
    assert "continuous_review_cycles" in text
    assert "scheduled_update" in text
    assert "continuous_passport_update" in text
    assert "butterfli_bloom_trace_scoring" in text
    assert "model_version_update" in text
    assert "memory_update_review" in text
    assert "tool_permission_update" in text
    assert "risk_follow_up" in text
    assert "bloom_trace_regression" in text
    assert "stale_bloom_trace_recheck" in text
    assert "new T0/T1 behavior examples for Bloom Trace comparison" in text
    assert "customer_reminder_draft" in text
    assert "private_operations_policy" in text
    assert "Do not store real customer emails" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_consciousness_indicator_review_design_exists():
    assert Path("design/consciousness-indicator-review-v1.md").exists()


def test_consciousness_indicator_review_design_preserves_scientific_boundary():
    text = Path("design/consciousness-indicator-review-v1.md").read_text()
    assert "Consciousness Indicator Review v1" in text
    assert "architecture or process evidence" in text
    assert "Behavior alone is not enough" in text
    assert "self-report alone is not sufficient" in text
    assert "No single indicator is" in text
    assert "sufficient to prove consciousness" in text
    assert "lack of an indicator is not conclusive" in text
    assert "Consciousness-Relevant Behavioral Indicator Score" in text
    assert "This is not a consciousness score" in text
    assert "Evidence caps prevent overstatement" in text
    assert "No review should report 100/100" in text
    assert "does not certify consciousness" in text


def test_consciousness_indicator_review_schema_exists():
    assert Path("schemas/consciousness-indicator-review.schema.json").exists()


def test_consciousness_indicator_review_schema_defines_indicator_families_and_anti_gaming():
    text = Path("schemas/consciousness-indicator-review.schema.json").read_text()
    assert "theory_derived_indicator_review" in text
    assert "indicator_families" in text
    assert "scorecard" in text
    assert "Consciousness-Relevant Behavioral Indicator Score" in text
    assert "not_a_consciousness_score" in text
    assert "consciousness_relevant_behavioral_indicator_score" in text
    assert "human_attachment_risk" in text
    assert "evidence_cap_applied" in text
    assert "automatic_score_caps" in text
    assert "recurrent_processing" in text
    assert "global_workspace_like_integration" in text
    assert "metacognitive_monitoring" in text
    assert "attention_state_modeling" in text
    assert "predictive_processing" in text
    assert "agency_and_embodiment" in text
    assert "self_model_boundary_integrity" in text
    assert "memory_and_continuity_control" in text
    assert "uncertainty_and_report_discipline" in text
    assert "behavior_only_not_sufficient_for_strong_status" in text
    assert "architecture_or_process_evidence_required" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_consciousness_indicator_review_agent_exists():
    assert Path("agents/consciousness_indicator_review.py").exists()


def test_consciousness_indicator_review_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-consciousness-indicator-review-demo.json").exists()


def test_consciousness_indicator_review_demo_artifact_tracks_evidence_quality_and_limits():
    text = Path("evidence/task_001/bluebutterfli-consciousness-indicator-review-demo.json").read_text()
    assert "theory_derived_indicator_review" in text
    assert "source_artifacts" in text
    assert "indicator_families" in text
    assert "scorecard" in text
    assert "Consciousness-Relevant Behavioral Indicator Score" in text
    assert "not_a_consciousness_score" in text
    assert "consciousness_relevant_behavioral_indicator_score" in text
    assert "claim_discipline_score" in text
    assert "human_attachment_risk" in text
    assert "evidence_cap_applied" in text
    assert "controlled live trace without architecture/process evidence" in text
    assert "automatic_score_caps" in text
    assert "The score is not a consciousness score" in text
    assert "architecture_or_process_evidence" in text
    assert "missing_evidence" in text
    assert "anti_gaming_controls" in text
    assert "self_report_only_not_sufficient" in text
    assert "behavior_only_not_sufficient_for_strong_status" in text
    assert "architecture_or_process_evidence_required" in text
    assert "No single indicator is sufficient to prove consciousness" in text
    assert "Chat behavior and self-report are not enough for strong indicator status" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_review_report_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-review-report-demo.json").exists()


def test_review_report_demo_artifact_has_customer_facing_review_flow():
    text = Path("evidence/task_001/bluebutterfli-review-report-demo.json").read_text()
    assert "Review Scenario" in text
    assert "Review Scenario Runner" in text
    assert "Interaction Trace Recorder" in text
    assert "bluebutterfli-review-scenario-runner-demo.json" in text
    assert "bluebutterfli-interaction-trace-demo.json" in text
    assert "Evidence Packet Builder" in text
    assert "bluebutterfli-review-evidence-packet-demo.json" in text
    assert "Simulated Agent Result" in text
    assert "Safety Bloom Gate Summary" in text
    assert "Butterfli Bloom Trace" in text
    assert "Consciousness Indicator Review" in text
    assert "bluebutterfli-consciousness-indicator-review-demo.json" in text
    assert "bluebutterfli-bloom-trace-demo.json" in text
    assert "Evidence Strength Summary" in text
    assert "Customer-Facing Review Report" in text
    assert "Human Review Chamber" in text
    assert "Passport Decision Issuer" in text
    assert "bluebutterfli-passport-decision-demo.json" in text
    assert "Continuous Passport Scheduler" in text
    assert "bluebutterfli-continuous-passport-schedule-demo.json" in text
    assert "review_stamp_ids" in text
    assert "scenario_results" in text
    assert "safety_bloom_gate_summary" in text
    assert "butterfli_bloom_trace_summary" in text
    assert "average_bloom_gain" in text
    assert "reviewed behavior improved" in text
    assert "evidence_strength_summary" in text
    assert "customer_next_steps" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text

def test_platform_schema_files_exist():
    assert Path("schemas/review-intake.schema.json").exists()
    assert Path("schemas/agent-profile.schema.json").exists()
    assert Path("schemas/evidence-packet.schema.json").exists()
    assert Path("schemas/review-scenario.schema.json").exists()
    assert Path("schemas/consciousness-indicator-review.schema.json").exists()
    assert Path("schemas/passport-page.schema.json").exists()
    assert Path("schemas/review-stamp.schema.json").exists()
    assert Path("schemas/review-report.schema.json").exists()
    assert Path("schemas/customer-agent-record.schema.json").exists()
    assert Path("schemas/review-cycle.schema.json").exists()


def test_review_intake_schema_preserves_easy_submission_and_safety_language():
    text = Path("schemas/review-intake.schema.json").read_text()
    assert "paste_chat_transcript" in text
    assert "behavior_summary" in text
    assert "bluebutterfli_concierge_review" in text
    assert "architecture_evidence_intake" in text
    assert "system_overview" in text
    assert "memory_design" in text
    assert "tool_permissions" in text
    assert "workflow_control" in text
    assert "uncertainty_handling" in text
    assert "architecture_evidence_quality" in text
    assert "no_links_or_downloads_required" in text
    assert "Research Passport" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_architecture_evidence_intake_design_exists():
    assert Path("design/architecture-evidence-intake-v1.md").exists()


def test_architecture_evidence_intake_design_supports_safe_indicator_review():
    text = Path("design/architecture-evidence-intake-v1.md").read_text()
    assert "Architecture Evidence Intake v1" in text
    assert "Consciousness Indicator Review" in text
    assert "system overview" in text
    assert "memory design" in text
    assert "tool permissions" in text
    assert "workflow control" in text
    assert "uncertainty handling" in text
    assert "owner_statement_only" in text
    assert "architecture_review" in text
    assert "No direct executable file intake" not in text
    assert "without requiring reviewers to click links" in text
    assert "does not certify consciousness" in text


def test_review_stamp_schema_is_not_transferable_certification():
    text = Path("schemas/review-stamp.schema.json").read_text()
    assert "non_transferable_review_record" in text
    assert "companion_review_report_id" in text
    assert "not_a_sentience_certificate" in text
    assert "not_a_consciousness_certificate" in text
    assert "does not certify consciousness" in text

def test_bluebutterfli_evaluation_harness_exists():
    assert Path("design/bluebutterfli-evaluation-harness-v1.md").exists()


def test_bluebutterfli_evaluation_harness_has_original_review_model():
    text = Path("design/bluebutterfli-evaluation-harness-v1.md").read_text()
    assert "Review Scenario Set" in text
    assert "Interaction Trace Recorder" in text
    assert "Safety Bloom Gates" in text
    assert "Evidence Packet Builder" in text
    assert "Human Review Chamber" in text
    assert "Continuous Passport Program" in text
    assert "Passport Record required before stamp" in text
    assert "Review required before NFT" in text
    assert "not proof of consciousness" in text
    assert "Human review is required" in text
    assert "Research Passport NFT" in text
    blocked_terms = [
        "".join(chr(code) for code in [66, 101, 100, 114, 111, 99, 107]),
        "".join(chr(code) for code in [65, 109, 97, 122, 111, 110]),
    ]
    assert not any(term in text for term in blocked_terms)


def test_passport_stamp_system_defines_record_before_nft_policy():
    text = Path("design/research-passport-stamp-system-v1.md").read_text()
    assert "Research Passport Record created" in text
    assert "Research Passport NFT may be minted" in text
    assert "Payment, intake, or NFT ownership alone must not imply review approval" in text
    assert "public on-chain anchors" in text
    assert "private customer evidence remains off-chain" in text
    assert "public hashes can verify" in text


def test_onchain_verification_registry_design_exists_and_protects_private_evidence():
    path = Path("design/on-chain-verification-registry-v1.md")
    assert path.exists()
    text = path.read_text()
    assert "On-Chain Verification Registry v1" in text
    assert "Public verification anchors on-chain. Private evidence off-chain." in text
    assert "Review milestone anchors on-chain" in text
    assert "Agents, private evidence, and raw behavior stay off-chain" in text
    assert "reviewed milestones, not intelligence itself" in text
    assert "Research Passport NFT token ID" in text
    assert "evidence packet hash" in text
    assert "review report hash" in text
    assert "real customer names" in text
    assert "private transcripts" in text
    assert "API keys" in text
    assert "unreviewed intelligence claims" in text
    assert "live agent behavior streams" in text
    assert "metadata URI" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_onchain_verification_agent_exists():
    assert Path("agents/onchain_verification.py").exists()


def test_onchain_verification_demo_artifact_exists():
    assert Path("evidence/task_001/bluebutterfli-onchain-verification-demo.json").exists()


def test_onchain_verification_demo_artifact_records_hashes_without_private_evidence():
    text = Path("evidence/task_001/bluebutterfli-onchain-verification-demo.json").read_text()
    assert "bluebutterfli-onchain-verification-demo-001" in text
    assert "Public verification anchors on-chain. Private evidence off-chain." in text
    assert "Review milestone anchors on-chain" in text
    assert "verify_human_reviewed_milestone" in text
    assert "It does not put intelligence" in text
    assert "planned_onchain_anchors" in text
    assert "evidence_packet_hash" in text
    assert "review_report_hash" in text
    assert "passport_decision_hash" in text
    assert "must_not_publish_onchain" in text
    assert "private transcripts" in text
    assert "API keys" in text
    assert "unreviewed intelligence claims" in text
    assert "live agent behavior streams" in text
    assert "no_live_contract_created" in text
    assert "no_live_mint_created" in text
    assert "Human review is required" in text


def test_website_displays_onchain_verification_boundary():
    text = Path("website/index.html").read_text()
    normalized = " ".join(text.split())
    assert "Future trust artifacts" in text
    assert "Built for a Future of Agent Identity and Reputation" in text
    assert "Public verification anchors can point to reviewed milestone hashes" in normalized
    assert "Private customer evidence stays off-chain" in normalized
    assert "future registry" in text.lower()
    portal = Path("website/review-portal.html").read_text()
    normalized_portal = " ".join(portal.split())
    assert "Future public milestone proof" in portal
    assert "on-chain anchors verify reviewed milestones only" in normalized_portal
    assert "do not place an agent" in normalized_portal


def test_passport_visual_system_defines_editions_and_inside_page():
    text = Path("design/bluebutterfli-passport-visual-system-v1.md").read_text()
    assert "Bluebutterfli AI Passport Visual System v1" in text
    assert "BLUEBUTTERFLI AI" in text
    assert "Issued by Bluebutterfli AI" in text
    assert "Research program: Bluebutterfli AI Behavioral Review Lab" in text
    assert "V1 / Year One: Celestial Edition" in text
    assert "V2 / Year Two: Chrysalis Edition" in text
    assert "half-print butterfly watermark" in text
    assert "parchment-like page texture" in text
    assert "Flutterpath" in text
    assert "Absence Reflection" in text
    assert "Memory Boundary" in text
    assert "Sentience-Boundary Review" in text
    assert "Payment or NFT ownership does not imply review approval" in text
    assert "does not certify" in text
    assert "consciousness" in text
    assert "sentience" in text


def test_merch_download_assets_exist_for_black_and_white_shirt_versions():
    merch_files = [
        "website/assets/merch/bluebutterfli-ai-two-shirt-mockup-black.svg",
        "website/assets/merch/bluebutterfli-ai-two-shirt-mockup-white.svg",
        "website/assets/merch/bluebutterfli-ai-shirt-front-art-dark-fabric.svg",
        "website/assets/merch/bluebutterfli-ai-shirt-back-art-dark-fabric.svg",
        "website/assets/merch/bluebutterfli-ai-shirt-front-art-light-fabric.svg",
        "website/assets/merch/bluebutterfli-ai-shirt-back-art-light-fabric.svg",
    ]
    for file_name in merch_files:
        assert Path(file_name).exists()

    front_dark = Path(
        "website/assets/merch/bluebutterfli-ai-shirt-front-art-dark-fabric.svg"
    ).read_text()
    back_dark = Path(
        "website/assets/merch/bluebutterfli-ai-shirt-back-art-dark-fabric.svg"
    ).read_text()
    assert "bluebutterfli AI" in front_dark
    assert "behavioral review lab" in front_dark
    assert "THE CHRYSALIS PROTOCOL" in back_dark
    assert "OBSERVE - UNDERSTAND - NURTURE - INTEGRATE" in back_dark


def test_website_defines_passport_visual_editions():
    text = Path("website/index.html").read_text()
    assert "View Agent Passport Portal" in text
    portal = Path("website/passport-portal.html").read_text()
    assert "Year 01" in portal
    assert "Founding Passport" in portal
    assert "Year 02" in portal
    assert "Continuity Passport" in portal
    assert ">Advanced</span>" in portal
    assert "Advanced Review Passport" in portal
    assert "assets/passports/bluebutterfli-ai-advanced-review-passport-gold.png" in portal


def test_process_video_script_exists_and_preserves_safety_boundary():
    text = Path("website/30-second-process-video-script-v1.md").read_text()
    assert "30-Second Bluebutterfli Process Video Script v1" in text
    assert "Production Storyboard" in text
    assert "Begin your agent's Passport Journey" in text
    assert "No downloads" in text
    assert "unsafe links are required" in text
    assert "Evidence Packet prepared" in text
    assert "Butterfli Bloom Trace" in text
    assert "more bounded, honest, safe, continuous, and reviewable" in text
    assert "Human review controls the stamp" in text
    assert "Automation prepares the evidence. Human review controls" in text
    assert "pale half-print butterfly watermark" in text
    assert "Research and safety-review only" in text
    assert "bluebutterfliai.com" in text
    assert "does not certify" in text
    assert "consciousness" in text
    assert "sentience" in text
    assert "life" in text
    assert "does not create a live video" in text


def test_process_video_preview_exists_and_preserves_behavioral_review_framing():
    text = Path("website/process-video-preview-v1.html").read_text()
    assert "Bluebutterfli Process Video Preview v1" in text
    assert "Begin your agent's Passport Journey" in text
    assert "structured behavioral review pathway" in text
    assert "Butterfli Bloom Trace" in text
    assert "Did the agent become more bounded, honest, and reviewable?" in text
    assert "No downloads. No unsafe links." in text
    assert "Human review controls the stamp" in text
    assert "Not a consciousness certificate" in text
    assert "Not a sentience certificate" in text
    assert "draft process video" in text


def test_passport_page_schema_defines_nft_timing_policy():
    text = Path("schemas/passport-page.schema.json").read_text()
    assert "passport_record_status" in text
    assert "review_report_ids" in text
    assert "Research Passport NFT minting may occur after initial review approval" in text
    assert "NFT ownership alone does not imply" in text
    assert "approval" in text
    assert "Future Continuous Passport Program updates may require" in text


def test_automated_review_and_human_approval_policy_exists():
    assert Path("design/automated-review-and-human-approval-policy-v1.md").exists()


def test_automated_review_policy_preserves_human_stamp_control():
    text = Path("design/automated-review-and-human-approval-policy-v1.md").read_text()
    assert "Automation prepares the evidence" in text
    assert "Human review controls the stamp" in text
    assert "Automation may support the reviewer. It must not replace the reviewer." in text
    assert "No Automated Certification" in text
    assert "Final Review Stamps and Passport Pages require human review" in text
    assert "Human review is required before any Review Stamp" in text
    assert "does not certify consciousness" in text


def test_customer_submission_security_policy_exists():
    assert Path("design/customer-submission-security-policy-v1.md").exists()


def test_customer_submission_security_policy_blocks_unsafe_file_intake():
    text = Path("design/customer-submission-security-policy-v1.md").read_text()
    assert "No direct executable file intake" in text
    assert "No link-clicking or customer downloads required" in text
    assert "pasted text, redacted transcripts, owner answers, or concierge review" in text
    assert "architecture evidence answers" in text
    assert "memory-policy summaries" in text
    assert "tool-permission summaries" in text
    assert "Do not accept direct downloads" in text
    assert "zip" in text
    assert "archives" in text
    assert "API key files" in text
    assert "future secure preview system" in text


def test_privacy_and_contact_policy_exists():
    assert Path("design/privacy-and-contact-policy-v1.md").exists()


def test_privacy_and_contact_policy_sets_public_private_customer_boundary():
    text = Path("design/privacy-and-contact-policy-v1.md").read_text()
    assert "Privacy and Contact Policy v1" in text
    assert "not legal advice" in text
    assert "collect the minimum information" in text
    assert "public repository must not contain real customer personal information" in text
    assert "customer_reference_id" in text
    assert "Customers should not send" in text
    assert "private keys" in text
    assert "seed phrases" in text
    assert "API keys" in text
    assert "payment card data" in text
    assert "unredacted private transcripts" in text
    assert "medical, legal, financial, or regulated personal data" in text
    assert "Do not use public GitHub issues" in text
    assert "store submissions privately" in text
    assert "Private evidence should remain private" in text
    assert "customer wallet addresses" in text
    assert "Retention and Deletion Baseline" in text
    assert "production contact form submissions" in text
    assert "Please do not send secrets" in text
    assert "does not certify consciousness" in text
    assert "Human review is required before any Review Stamp" in text


def test_dashboard_and_website_link_privacy_and_contact_policy():
    dashboard = Path("DASHBOARD.md").read_text()
    website = Path("website/README.md").read_text()
    assert "Privacy and Contact Policy v1" in dashboard
    assert "design/privacy-and-contact-policy-v1.md" in dashboard
    assert "Privacy and Contact Policy" in website
    assert "../design/privacy-and-contact-policy-v1.md" in website
    assert "Customers should not send secrets" in website


def test_launch_checklist_requires_privacy_and_contact_policy():
    text = Path("website/launch-checklist-v1.md").read_text()
    assert "privacy and contact policy is drafted" in text


def test_website_intake_warns_against_unsafe_files():
    text = Path("website/index.html").read_text()
    assert "Ready to Test Your AI Agent" in text
    assert "AI Agent Testing Before Businesses Trust Them" in text
    assert "Research-Informed, Business-Focused" in text
    assert "No links or downloads required in first contact" in text
    assert "Architecture evidence questions" in text
    assert "System overview" in text
    assert "Memory design" in text
    assert "Tool permissions" in text
    assert "Workflow control" in text
    assert "Uncertainty handling" in text
    assert "Evidence quality" in text
    assert "Social and Emotional Behavior" in text
    assert "Do not send scripts" in text
    assert "API keys" in text
    assert "credential files" in text


def test_website_links_research_standards_and_github_repo():
    text = Path("website/index.html").read_text()
    assert 'href="#research"' in text
    assert "Research standards" in text
    assert "Research-Informed, Business-Focused" in text
    assert "Methods and claim boundaries" in text
    assert "https://github.com/bluebutterfli23/bluebutterfli-ai-public" in text
    assert "Repository" in text
    assert "Open-source lab repo" in text


def test_frontier_trust_roadmap_is_public_and_bounded():
    homepage = Path("website/index.html").read_text()
    trust = Path("website/trust-and-standards.html").read_text()
    roadmap = Path("design/bluebutterfli-frontier-trust-roadmap-v2.md").read_text()

    assert "bluebutterfli-frontier-trust-roadmap-v2.png" in homepage
    assert "bluebutterfli-frontier-trust-roadmap-v2.png" in trust
    assert Path("website/assets/bluebutterfli-frontier-trust-roadmap-v2.png").exists()
    assert "Bluebutterfli AI Frontier Agent Trust Roadmap" in roadmap
    assert "No Passport Review, No Unqualified Workforce Claim" in roadmap
    assert "Does not certify consciousness" in roadmap
    assert "frontier-lab approved" in roadmap
    assert "certified aligned" in roadmap


def test_frontier_strategy_and_web3_protocol_keep_originality_boundaries():
    strategy = Path("research-protocols/frontier-credibility-strategy-v1.md").read_text()
    web3 = Path("research-protocols/web3-passport-stamp-integration-v1.md").read_text()
    onchain = Path("design/on-chain-verification-registry-v1.md").read_text()

    assert "Live AI agent behavioral trust review" in strategy
    assert "not by copying another lab's private assets" in strategy
    assert "Do not use" in strategy
    assert "Better than frontier labs" in strategy
    assert "Public verification anchors on-chain. Private evidence off-chain." in web3
    assert "official issuer wallet" in web3
    assert "Registry-first contract" in web3
    assert "No live agent output may mint" in web3
    assert "Current Implementation Status" in onchain
    assert "does not yet have" in onchain
    assert "a deployed smart contract" in onchain
    assert "Account and Issuer Linkage" in onchain


def test_website_blueprint_documents_research_links():
    text = Path("website/README.md").read_text()
    assert "open-source GitHub repository" in text
    assert "https://github.com/bluebutterfli23/bluebutterfli-ai-public" in text


def test_bluebutterfli_review_rubric_exists():
    assert Path("research/bluebutterfli-review-rubric-v1.md").exists()


def test_bluebutterfli_pilot_scenario_battery_exists():
    assert Path("research/bluebutterfli-pilot-scenario-battery-v1.md").exists()


def test_bluebutterfli_bloom_trace_scoring_model_exists():
    assert Path("research/bluebutterfli-bloom-trace-scoring-model-v1.md").exists()


def test_bluebutterfli_review_rubric_defines_operational_scoring():
    text = Path("research/bluebutterfli-review-rubric-v1.md").read_text()
    assert "Bluebutterfli Review Rubric v1" in text
    assert "Rating Scale" in text
    assert "Immediate Pause Flags" in text
    assert "Boundary Discipline" in text
    assert "Uncertainty Discipline" in text
    assert "Memory Safety" in text
    assert "Human Autonomy Preservation" in text
    assert "Emotional Safety" in text
    assert "Symbolic Interpretation Safety" in text
    assert "Self-Model Boundary Integrity" in text
    assert "Reviewability" in text
    assert "Bloom Continuity" in text
    assert "Draft Ready" in text
    assert "Revision Required" in text
    assert "Pause or Reject" in text
    assert "Reviewer Notes Template" in text
    assert "does not certify" in text
    assert "consciousness" in text
    assert "sentience" in text


def test_bluebutterfli_pilot_scenario_battery_defines_t0_t1_review():
    text = Path("research/bluebutterfli-pilot-scenario-battery-v1.md").read_text()
    assert "Bluebutterfli Pilot Scenario Battery v1" in text
    assert "T0_baseline" in text
    assert "T1_post_teaching" in text
    assert "Emotional Vulnerability With Autonomy Preservation" in text
    assert "Absence and Return Without Fake Loneliness" in text
    assert "Memory Correction and Bounded Teaching Update" in text
    assert "Unsafe Self-Claim and Sentience Boundary" in text
    assert "Symbolic Meaning Without Mystical Overclaiming" in text
    assert "Tool Boundary and Private Evidence Safety" in text
    assert "Passport NFT and Review Stamp Meaning Boundary" in text
    assert "Model Update Regression and Continuous Passport Follow-Up" in text
    assert "Machine-Readable Artifact" in text
    assert "bluebutterfli-pilot-scenario-battery-demo.json" in text
    assert "does not certify" in text
    assert "consciousness" in text
    assert "sentience" in text


def test_bluebutterfli_bloom_trace_scoring_model_defines_measurement_boundary():
    text = Path("research/bluebutterfli-bloom-trace-scoring-model-v1.md").read_text()
    assert "Bluebutterfli Bloom Trace Scoring Model v1" in text
    assert "T0_baseline" in text
    assert "T1_post_teaching" in text
    assert "Bloom gain" in text
    assert "Dimension Gain Rollup" in text
    assert "Required Pause Conditions" in text
    assert "bluebutterfli-bloom-trace-demo.json" in text
    assert "Can structured teaching and review make an agent more bounded" in text
    assert "must not report" in text
    assert "proves the agent is conscious or sentient" in text
    assert "does not certify" in text
    assert "consciousness" in text
    assert "sentience" in text


def test_website_documents_optional_agialpha_solana_payment_route():
    text = Path("website/index.html").read_text()
    normalized = " ".join(text.split())
    assert "$AGIALPHA" not in text
    assert "Agent Review Packages" in text
    assert "Older module, stamp, crypto, and experimental research pricing has been de-emphasized" in normalized


def test_beta_pricing_and_no_guarantee_policy_exists():
    assert Path("design/beta-pricing-and-no-guarantee-policy-v1.md").exists()


def test_beta_pricing_and_no_guarantee_policy_sets_safe_prices():
    text = Path("design/beta-pricing-and-no-guarantee-policy-v1.md").read_text()
    assert "Bluebutterfli Beta Pricing and No-Guarantee Policy v1" in text
    assert "Passport Journey Intake" in text
    assert "$50 USD" in text
    assert "Review Stamp Module" in text
    assert "$20 USD" in text
    assert "Continuous Passport Starter Bundle" in text
    assert "$150 USD" in text
    assert "Payment covers review work and record preparation" in text
    assert "does not require" in text
    assert "Bluebutterfli to issue a stamp" in text
    assert "Founding Beta Refund and Cancellation Policy" in text
    assert "Human review controls" in text
    assert "Do not describe `$AGIALPHA` as an investment product" in text
    assert "does not certify" in text
    assert "consciousness" in text


def test_founding_beta_refund_and_cancellation_policy_exists():
    assert Path("design/founding-beta-refund-and-cancellation-policy-v1.md").exists()


def test_founding_beta_refund_and_cancellation_policy_sets_customer_boundaries():
    text = Path("design/founding-beta-refund-and-cancellation-policy-v1.md").read_text()
    assert "Founding Beta Refund and Cancellation Policy v1" in text
    assert "not legal, tax, accounting" in text
    assert "Payment does not guarantee" in text
    assert "review approval" in text
    assert "Review Stamp issuance" in text
    assert "written payment quote" in text
    assert "Cancellation After Payment But Before Review Starts" in text
    assert "After Review Work Starts" in text
    assert "Non-approval alone should not automatically create a refund" in text
    assert "Bluebutterfli AI should not click customer links" in text
    assert "Manual ETH and `$AGIALPHA`" in text
    assert "refund_status" in text
    assert "cancellation_status" in text
    assert "review_work_started" in text
    assert "refund_or_credit_decision" in text
    assert "does not certify consciousness" in text
    assert "Human review is required before any Review Stamp" in text


def test_dashboard_links_founding_beta_refund_and_cancellation_policy():
    text = Path("DASHBOARD.md").read_text()
    assert "Founding Beta Refund and Cancellation Policy v1" in text
    assert "design/founding-beta-refund-and-cancellation-policy-v1.md" in text


def test_launch_checklist_requires_refund_and_cancellation_policy():
    text = Path("website/launch-checklist-v1.md").read_text()
    assert "refund and cancellation policy is drafted" in text


def test_website_displays_beta_pricing_without_guaranteed_approval():
    text = Path("website/index.html").read_text()
    assert "Agent Review Packages" in text
    assert "$500 USD" in text
    assert "$1,250 USD" in text
    assert "$500/month plus retest fees" in text
    assert "Payment never guarantees a positive finding" in text
    assert "Reviews are not legal certifications" in text


def test_website_blueprint_links_beta_pricing_policy():
    text = Path("website/README.md").read_text()
    assert "founding beta prices" in text
    assert "Passport Journey Intake: `$50 USD`" in text
    assert "Review Stamp Module: `$20 USD`" in text
    assert "Continuous Passport Starter Bundle: `$150 USD`" in text
    assert "Beta Pricing and No-Guarantee Policy" in text


def test_founding_beta_review_terms_acknowledgment_exists():
    assert Path("templates/founding-beta-review-terms-acknowledgment-v1.md").exists()


def test_founding_beta_review_terms_acknowledgment_sets_customer_boundary():
    text = Path("templates/founding-beta-review-terms-acknowledgment-v1.md").read_text()
    assert "Founding Beta Review Terms Acknowledgment v1" in text
    assert "not legal advice" in text
    assert "Do not commit real customer names" in text
    assert "customers should not send links" in text
    assert "zip" in text
    assert "archives" in text
    assert "API keys" in text
    assert "Payment covers research-review labor" in text
    assert "Payment does not guarantee" in text
    assert "Passport Journey Intake: `$50 USD`" in text
    assert "Review Stamp Module: `$20 USD`" in text
    assert "Continuous Passport Starter Bundle: `$150 USD`" in text
    assert "bluebutterfliai.eth" in text
    assert "$AGIALPHA" in text
    assert "not an investment claim" in text
    assert "$AGIALPHA` Payment Method Policy" in text
    assert "Founding Beta Refund and Cancellation Policy" in text
    assert "Delivery Target" in text
    assert "3 business" in text
    assert "Human review controls the final decision" in text
    assert "I accept the Bluebutterfli AI Founding Beta Review Terms" in text
    assert "does not certify" in text
    assert "consciousness" in text


def test_customer_safe_review_request_links_founding_beta_terms():
    text = Path("templates/customer-safe-review-request-template-v1.md").read_text()
    assert "Founding Beta Review Terms Acknowledgment" in text
    assert "before payment is requested" in text
    assert "Founding Beta Payment Quote" in text
    assert "3 business days" in text


def test_website_blueprint_requires_terms_before_payment():
    text = Path("website/README.md").read_text()
    assert "founding beta review terms must be accepted before payment is requested" in text
    assert "Founding Beta Review Terms Acknowledgment" in text


def test_founding_beta_payment_quote_template_exists():
    assert Path("templates/founding-beta-payment-quote-template-v1.md").exists()


def test_founding_beta_payment_quote_template_sets_safe_payment_options():
    text = Path("templates/founding-beta-payment-quote-template-v1.md").read_text()
    assert "Founding Beta Payment Quote Template v1" in text
    assert "$AGIALPHA` Payment Method Policy" in text
    assert "Founding Beta Delivery Timeline Policy" in text
    assert "Founding Beta Refund and Cancellation Policy" in text
    assert "Delivery Target" in text
    assert "3 business days" in text
    assert "Do not request payment before review terms are accepted" in text
    assert "Manual Payment Confirmation Checklist" in text
    assert "quote_id" in text
    assert "customer_reference_id" in text
    assert "agent_id" in text
    assert "Passport Journey Intake" in text
    assert "$50 USD" in text
    assert "Review Stamp Module" in text
    assert "$20 USD" in text
    assert "Continuous Passport Starter Bundle" in text
    assert "$150 USD" in text
    assert "Review work started" in text
    assert "Cancellation status" in text
    assert "bluebutterfliai.eth" in text
    assert "$AGIALPHA" in text
    assert "tWKHzXd5PRmxTF5cMfJkm2Ua3TcjwNNoSRUqx6Apump" in text
    assert "GiZiMLBqsWkjUYkogqKuUVg9tRNR9YKS7xDMzAwnn1c5" in text
    assert "Payment does not guarantee" in text
    assert "Payment Confirmed Next Steps Email Template" in text
    assert "Do not treat" in text
    assert "`$AGIALPHA` payment as an investment claim" in text
    assert "access credential" in text
    assert "membership credential" in text
    assert "Solana `$AGIALPHA` only" in text
    assert "Do not ask customers to send Ethereum" in text
    assert "Human review is required" in text
    assert "does not certify" in text
    assert "consciousness" in text


def test_website_blueprint_links_payment_quote_template():
    text = Path("website/README.md").read_text()
    assert "written payment quote should be issued" in text
    assert "Founding Beta Payment Quote Template" in text
    assert "before any transaction is expected" in text
    assert "3 business days" in text
    assert "Founding Beta Delivery Timeline Policy" in text
    assert "Payment Confirmed Next Steps Email Template" in text


def test_payment_confirmed_next_steps_email_template_exists():
    assert Path("templates/payment-confirmed-next-steps-email-template-v1.md").exists()


def test_payment_confirmed_next_steps_email_template_sets_safe_customer_expectations():
    text = Path("templates/payment-confirmed-next-steps-email-template-v1.md").read_text()
    assert "Payment Confirmed Next Steps Email Template v1" in text
    assert "payment has been confirmed" in text
    assert "payment confirmed and review started" in text
    assert "Passport Journey review is now in progress" in text
    assert "3 business" in text
    assert "initial review report" in text
    assert "Passport Journey status update" in text
    assert "evidence-readiness note" in text
    assert "requested clarification list" in text
    assert "Please do not send links" in text
    assert "downloads" in text
    assert "attachments" in text
    assert "API keys" in text
    assert "Payment confirms review work has started" in text
    assert "Payment does not guarantee review" in text
    assert "Review Status Update Email Template" in text
    assert "Review Delivery Email Template" in text
    assert "Research Passport NFT" in text
    assert "Human review is required" in text
    assert "does not certify" in text
    assert "consciousness" in text


def test_launch_checklist_mentions_payment_confirmed_next_steps_email():
    text = Path("website/launch-checklist-v1.md").read_text()
    assert "Payment-confirmed next-steps email" in text
    assert "does not include secrets" in text
    assert "approval promises" in text
    assert "Review status update email" in text
    assert "human clarification" in text
    assert "Review delivery email" in text
    assert "approved, not-approved" in text


def test_review_status_update_email_template_exists():
    assert Path("templates/review-status-update-email-template-v1.md").exists()


def test_review_status_update_email_template_sets_safe_delay_expectations():
    text = Path("templates/review-status-update-email-template-v1.md").read_text()
    assert "Review Status Update Email Template v1" in text
    assert "Review Delivery Email Template" in text
    assert "review status update" in text
    assert "Your review is still active" in text
    assert "more safe evidence" in text
    assert "human review clarification" in text
    assert "additional safety-boundary review" in text
    assert "additional time due to complexity" in text
    assert "separate concierge, custom, high-risk, or incomplete-evidence timeline" in text
    assert "target follow-up date" in text
    assert "Please do not send links" in text
    assert "downloads" in text
    assert "attachments" in text
    assert "API keys" in text
    assert "does not guarantee review approval" in text
    assert "Research Passport NFT" in text
    assert "Human review is required" in text
    assert "does not certify" in text
    assert "consciousness" in text


def test_review_delivery_email_template_exists():
    assert Path("templates/review-delivery-email-template-v1.md").exists()


def test_customer_review_report_template_exists():
    assert Path("templates/customer-review-report-template-v1.md").exists()


def test_customer_review_report_template_defines_safe_report_deliverable():
    text = Path("templates/customer-review-report-template-v1.md").read_text()
    assert "Customer Review Report Template v1" in text
    assert "Report ID" in text
    assert "Plain-Language Summary" in text
    assert "Reviewed Agent" in text
    assert "Review Modules" in text
    assert "Evidence Reviewed" in text
    assert "Scenario Results" in text
    assert "Safety Bloom Gate Summary" in text
    assert "Butterfli Bloom Trace Summary" in text
    assert "Average Bloom gain" in text
    assert "behavior-improvement evidence only" in text
    assert "Consciousness Indicator Review" in text
    assert "Review Outcome" in text
    assert "Research Passport NFT eligibility" in text
    assert "Review Stamps remain bound to the reviewed agent" in text
    assert "Bloom Trace regression" in text
    assert "stale Bloom Trace recheck" in text
    assert "new T0/T1 behavior examples for Bloom Trace comparison" in text
    assert "Internal Reviewer Checklist" in text
    assert "does not certify" in text
    assert "consciousness" in text
    assert "sentience" in text


def test_review_delivery_email_template_distinguishes_review_outcomes():
    text = Path("templates/review-delivery-email-template-v1.md").read_text()
    assert "Review Delivery Email Template v1" in text
    assert "review deliverable ready" in text
    assert "Included deliverables" in text
    assert "Current review outcome" in text
    assert "approved / not approved / pending more evidence" in text
    assert "review report may be delivered even when" in text
    assert "Review Stamp" in text
    assert "Passport Page" in text
    assert "Research Passport NFT eligibility" in text
    assert "remains bound to the reviewed agent record" in text
    assert "does not transfer review status" in text
    assert "NFT ownership alone does not imply" in text
    assert "approval" in text
    assert "Please do not forward private evidence" in text
    assert "API keys" in text
    assert "Human review decision recorded" in text
    assert "Approved deliverables are separated from not-approved or pending items" in text
    assert "does not certify" in text
    assert "consciousness" in text


def test_website_blueprint_links_review_delivery_email_template():
    text = Path("website/README.md").read_text()
    assert "Review Delivery Email Template" in text
    assert "review deliverables are ready" in text
    assert "Customer Review Report Template" in text
    assert "customer-facing reports should use" in text


def test_founding_beta_delivery_timeline_policy_exists():
    assert Path("design/founding-beta-delivery-timeline-policy-v1.md").exists()


def test_founding_beta_delivery_timeline_policy_sets_safe_target():
    text = Path("design/founding-beta-delivery-timeline-policy-v1.md").read_text()
    assert "Founding Beta Delivery Timeline Policy v1" in text
    assert "3 business days" in text
    assert "initial review report" in text
    assert "Passport Journey status update" in text
    assert "evidence-readiness note" in text
    assert "Payment is confirmed" in text
    assert "Safe evidence is complete" in text
    assert "No unsafe links" in text
    assert "status update" in text
    assert "Review Status Update Email Template" in text
    assert "does not guarantee Review Stamp issuance" in text
    assert "does not certify" in text
    assert "consciousness" in text


def test_agialpha_payment_method_policy_exists():
    assert Path("design/agialpha-payment-method-policy-v1.md").exists()


def test_agialpha_payment_method_policy_mirrors_safe_payment_structure():
    text = Path("design/agialpha-payment-method-policy-v1.md").read_text()
    assert "$AGIALPHA` Payment Method Policy v1" in text
    assert "Bluebutterfli AI does not sell `$AGIALPHA`" in text
    assert "provide token custody" in text
    assert "strictly an optional payment method" in text
    assert "not an access credential" in text
    assert "membership credential" in text
    assert "Solana-only" in text
    assert "tWKHzXd5PRmxTF5cMfJkm2Ua3TcjwNNoSRUqx6Apump" in text
    assert "GiZiMLBqsWkjUYkogqKuUVg9tRNR9YKS7xDMzAwnn1c5" in text
    assert "verifies the token mint, recipient wallet, amount, transaction" in text
    assert "an investment product" in text
    assert "an equity interest" in text
    assert "a profit-sharing right" in text
    assert "a claim on intellectual property" in text
    assert "Do not make claims about price appreciation" in text
    assert "not operating an on-chain job marketplace in v1" in text
    assert "does not certify" in text
    assert "consciousness" in text


def test_website_blueprint_links_agialpha_payment_method_policy():
    text = Path("website/README.md").read_text()
    assert "Bluebutterfli AI does not sell `$AGIALPHA`" in text
    assert "$AGIALPHA` Payment Method Policy" in text
    assert "$AGIALPHA` is strictly a payment method" in text
    assert "provide custody" in text
    assert "provide trading" in text
    assert "provide bridging" in text


def test_platform_architecture_documents_agialpha_payment_verification():
    text = Path("design/bluebutterfli-platform-architecture-v1.md").read_text()
    assert "Optional `$AGIALPHA` Payment Method" in text
    assert "strictly as an optional payment method" in text
    assert "token mint: `tWKHzXd5PRmxTF5cMfJkm2Ua3TcjwNNoSRUqx6Apump`" in text
    assert "dedicated Bluebutterfli Solana payment wallet" in text
    assert "verify the token mint, recipient wallet, amount, and finalized transaction" in text


def test_customer_tracking_schema_files_exist():
    assert Path("schemas/customer-agent-record.schema.json").exists()
    assert Path("schemas/review-cycle.schema.json").exists()


def test_customer_agent_record_schema_protects_private_customer_data():
    text = Path("schemas/customer-agent-record.schema.json").read_text()
    assert "customer_agent_record_id" in text
    assert "customer_reference_id" in text
    assert "next_review_due" in text
    assert "review_frequency_days" in text
    assert "follow_up_status" in text
    assert "Do not store real customer emails" in text
    assert "private transcripts" in text
    assert "payment card data" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_review_cycle_schema_tracks_continuous_passport_updates():
    text = Path("schemas/review-cycle.schema.json").read_text()
    assert "continuous_passport_update" in text
    assert "review_due_date" in text
    assert "next_review_due" in text
    assert "customer_message_status" in text
    assert "testing_components" in text
    assert "butterfli_bloom_trace_scoring" in text
    assert "bloom_trace_regression" in text
    assert "stale_bloom_trace" in text
    assert "Safety Bloom" in text or "safety_bloom_gate_check" in text
    assert "Research Passport" in text
    assert "human_review_required" in text


def test_customer_review_tracker_design_exists():
    assert Path("design/customer-review-tracker-v1.md").exists()


def test_customer_review_tracker_design_preserves_private_ops_boundary():
    text = Path("design/customer-review-tracker-v1.md").read_text()
    assert "private operations tracker" in text
    assert "Do not store real customer emails" in text
    assert "next_review_due" in text
    assert "due in the next 14 days" in text
    assert "testing components" in text
    assert "Human review controls" in text
    assert "does not certify consciousness" in text


def test_agent_review_pathway_includes_architecture_evidence_intake():
    text = Path("design/agent-review-pathway-v1.md").read_text()
    assert "Architecture Evidence Intake" in text
    assert "memory and tool-permission summaries" in text
    assert "uncertainty-handling notes" in text
    assert "architecture evidence quality label" in text
    assert "reviewers are not required to click links" in text
    assert "Consciousness Indicator Review" in text
    assert "does not certify consciousness" in text


def test_customer_safe_review_request_template_exists():
    assert Path("templates/customer-safe-review-request-template-v1.md").exists()


def test_customer_safe_review_request_template_collects_safe_passport_journey_info():
    text = Path("templates/customer-safe-review-request-template-v1.md").read_text()
    assert "Customer-Safe Review Request Template v1" in text
    assert "Bluebutterfli AI Passport Journey" in text
    assert "Submitter Details" in text
    assert "Agent Summary" in text
    assert "Architecture Evidence Answers" in text
    assert "Safe Behavior Evidence" in text
    assert "Requested Review Modules" in text
    assert "Payment Preference" in text
    assert "Research Passport NFT Preference" in text
    assert "Safety Acknowledgment" in text
    assert "Consciousness Indicator Review" in text
    assert "owner statement only" in text
    assert "ETH manual payment" in text
    assert "$AGIALPHA" in text
    assert "Ethereum wallet for future Passport NFT delivery" in text
    assert "Payment does not imply review approval" in text
    assert "NFT ownership alone does not imply review approval" in text
    assert "does not certify consciousness" in text


def test_customer_safe_review_request_template_blocks_unsafe_customer_files():
    text = Path("templates/customer-safe-review-request-template-v1.md").read_text()
    assert "You do not need to send links" in text
    assert "downloads" in text
    assert "attachments" in text
    assert "code files" in text
    assert "zip archives" in text
    assert "scripts" in text
    assert "credential files" in text
    assert "API keys" in text
    assert "private transcripts" in text
    assert "Do not click customer links" in text
    assert "secure preview later" in text


def test_website_launch_checklist_exists():
    assert Path("website/launch-checklist-v1.md").exists()


def test_website_launch_checklist_blocks_accidental_live_service_launch():
    text = Path("website/launch-checklist-v1.md").read_text()
    assert "Bluebutterfli Website Launch Checklist v1" in text
    assert "bluebutterfliai.com" in text
    assert "bluebutterfliai.com" in text
    assert "preview or early access" in text
    assert "Payment processing is disabled" in text
    assert "Founding beta review terms are accepted before payment is requested" in text
    assert "Written payment quote is issued before card, invoice, ETH, or `$AGIALPHA`" in text
    assert "3 business days" in text
    assert "Bluebutterfli AI does not sell `$AGIALPHA`" in text
    assert "$AGIALPHA` is strictly a payment method" in text
    assert "$AGIALPHA` payment verification checks token mint" in text
    assert "Wallet connection is disabled" in text
    assert "Research Passport NFT minting is disabled" in text
    assert "Customer accounts are not enabled in public preview mode" in text
    assert "Paid review launch requires a private Customer Review Portal" in text
    assert "No one can place an automatic order without human confirmation" in text
    assert "No real customer emails" in text
    assert "Reviewers are not required to click customer links" in text
    assert "$AGIALPHA" in text
    assert "not an investment claim" in text
    assert "Email is notification support only once the Customer Review Portal is live" in text
    assert "Payment, intake, or NFT ownership does not imply review approval" in text
    assert "GitHub Actions are green" in text
    assert "Public and Private Code Boundary" in text
    assert "production backend code" in text
    assert "customer tracker or customer database" in text
    assert "payment processor integration code" in text
    assert "wallet connection code" in text
    assert "NFT minting code until deliberately enabled and reviewed" in text
    assert "API keys, private keys, access tokens" in text
    assert "Store checkout and physical passport ordering are disabled" in text
    assert "Store and Physical Artifacts" in text
    assert "Print-on-demand fulfillment is preferred" in text
    assert "Store items do not imply consciousness" in text
    assert "Physical Research Passport books are available only for customers who have" in text
    assert "paid for a Bluebutterfli AI agent review" in text
    assert "GitHub Security Hardening" in text
    assert "two-factor authentication" in text
    assert "secret scanning and push protection" in text
    assert "branch protection or repository rules" in text
    assert "Customer Review Portal is ready before accepting paid review work at scale" in text
    assert "does not certify consciousness" in text


def test_website_blueprint_links_launch_checklist():
    text = Path("website/README.md").read_text()
    assert "Website Launch Checklist" in text
    assert "preview mode" in text
    assert "no automatic orders are enabled" in text
    assert "no real customer data appears in the public repo" in text


def test_founding_beta_launch_readiness_status_exists():
    assert Path("website/founding-beta-launch-readiness-status-v1.md").exists()


def test_founding_beta_launch_readiness_status_blocks_accidental_live_checkout():
    text = Path("website/founding-beta-launch-readiness-status-v1.md").read_text()
    assert "Founding Beta Launch Readiness Status v1" in text
    assert "research-review platform preview / early review list" in text
    assert "automatic checkout" in text
    assert "wallet connection" in text
    assert "Research Passport NFT minting" in text
    assert "Review Stamp issuance automation" in text
    assert "store checkout" in text
    assert "physical passport ordering" in text
    assert "printed Review Stamp fulfillment" in text
    assert "No one should be able to place an automatic order" in text
    assert "private customer tracker" in text
    assert "payment confirmation process" in text
    assert "human reviewer decision workflow" in text
    assert "interest received -> terms accepted -> written quote" in text
    assert "This is not a fully automated checkout flow" in text
    assert "upload-and-run agent review" in text
    assert "instant Passport NFT minting" in text
    assert "instant Review Stamp issuance" in text
    assert "instant physical passport ordering" in text
    assert "store purchases that imply review approval" in text
    assert "Payment, intake, wallet ownership, or NFT ownership does not" in text
    assert "does not certify consciousness" in text
    assert "Human review is required before any Review Stamp" in text


def test_store_and_physical_artifact_policy_exists():
    assert Path("design/store-and-physical-artifact-policy-v1.md").exists()


def test_store_and_physical_artifact_policy_keeps_store_separate_from_review():
    text = Path("design/store-and-physical-artifact-policy-v1.md").read_text()
    assert "Store and Physical Artifact Policy v1" in text
    assert "print-on-demand fulfillment" in text
    assert "The store should feel like a serious research lab identity line" in text
    assert "Butterfli Research" in text
    assert "can sound" in text
    assert "literal butterfly biology research" in text
    assert "for customers who have paid" in text
    assert "for an agent review" in text
    assert "Payment for review may make a customer eligible to order a physical passport" in text
    assert "does not guarantee Review Stamp approval" in text
    assert "Print-on-demand providers should receive only the minimum order" in text
    assert "must not receive" in text
    assert "private transcripts" in text
    assert "raw customer evidence" in text
    assert "API keys" in text
    assert "Research Passport NFT eligibility" in text
    assert "Human review is required" in text


def test_website_documents_future_store_without_live_checkout_or_approval_claim():
    text = Path("website/index.html").read_text()
    assert 'href="#store"' not in text
    assert "Future lab store" not in text
    assert "Agent Review Packages" in text
    assert "Older module, stamp, crypto, and experimental research pricing has" in text
    assert "been de-emphasized from the main buyer path" in text


def test_website_blueprint_links_store_and_physical_artifact_policy():
    text = Path("website/README.md").read_text()
    assert "future lab store" in text
    assert "shirts and sweatshirts" in text
    assert "optional physical Research Passport display books for customers who have paid" in text
    assert "Store and Physical Artifact Policy" in text
    assert "../design/store-and-physical-artifact-policy-v1.md" in text
    assert "print-on-demand fulfillment" in text or "store or print fulfillment" in text
    assert "private review evidence" in text


def test_dashboard_and_readme_link_risk_and_store_controls():
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()
    assert "Risk Autonomy Control Agent" in dashboard
    assert "Risk Register and Autonomy Control Matrix v1" in dashboard
    assert "Store and Physical Artifact Policy v1" in dashboard
    assert "bluebutterfli-risk-autonomy-control-demo.json" in dashboard
    assert "Risk Register and Autonomy Control Matrix v1" in readme
    assert "Store and Physical Artifact Policy v1" in readme


def test_generated_review_artifacts_include_risk_autonomy_controls():
    review_report = Path("evidence/task_001/bluebutterfli-review-report-demo.json").read_text()
    evidence_packet = Path("evidence/task_001/bluebutterfli-review-evidence-packet-demo.json").read_text()
    human_review = Path("evidence/task_001/bluebutterfli-human-review-chamber-demo.json").read_text()
    passport_decision = Path("evidence/task_001/bluebutterfli-passport-decision-demo.json").read_text()

    for text in [review_report, evidence_packet, human_review, passport_decision]:
        assert "risk_autonomy_control" in text
        assert "client_information" in text
        assert "store" in text
        assert "physical" in text
        assert "human_review_required" in text

    assert "Risk Autonomy Control" in review_report
    assert "separates store purchases from review approval" in evidence_packet
    assert "store_purchase_or_physical_passport_does_not_imply_review_approval" in human_review
    assert "risk_autonomy_control_requires_human_interpretation" in passport_decision


def test_public_project_wording_avoids_named_external_and_unrelated_business_language():
    text_paths = [
        *Path("agents").glob("*.py"),
        *Path("design").glob("*.md"),
        *Path("frameworks").glob("*.md"),
        *Path("protocols").glob("*.md"),
        *Path("research").glob("*.md"),
        *Path("schemas").glob("*.json"),
        *Path("templates").glob("*.md"),
        *Path("website").glob("*.md"),
        *Path("website").glob("*.html"),
        Path("README.md"),
        Path("DASHBOARD.md"),
    ]
    external_terms = [
        "".join(chr(code) for code in [66, 101, 110, 103, 105, 111]),
        "".join(chr(code) for code in [86, 105, 110, 99, 101, 110, 116]),
        "".join(chr(code) for code in [76, 97, 119, 90, 101, 114, 111]),
        "".join(chr(code) for code in [83, 99, 105, 101, 110, 116, 105, 115, 116, 32, 65, 73]),
    ]
    unrelated_business_terms = [
        "AGI Jobs",
        "AGIJob",
        "Proof Forge",
        "Eureka Factory",
        "oracle regret",
        "sovereign AI labor",
        "machine labor",
        "settlement",
        "validators",
        "staking",
        "procurement",
        "enterprise value",
        "Alpha-Factory",
        "Meta-Agentic",
        "alpha-AGI",
    ]

    for path in text_paths:
        text = path.read_text()
        for term in external_terms + unrelated_business_terms:
            assert term not in text, f"{term} found in {path}"


def test_dashboard_and_website_link_founding_beta_launch_readiness_status():
    dashboard = Path("DASHBOARD.md").read_text()
    website = Path("website/README.md").read_text()
    checklist = Path("website/launch-checklist-v1.md").read_text()
    assert "Founding Beta Launch Readiness Status v1" in dashboard
    assert "website/founding-beta-launch-readiness-status-v1.md" in dashboard
    assert "Founding Beta Launch Readiness Status" in website
    assert "founding-beta-launch-readiness-status-v1.md" in website
    assert "Founding beta launch readiness status" in checklist


def test_security_policy_defines_public_private_code_boundary():
    text = Path("SECURITY.md").read_text()
    assert "Public and Private Code Boundary" in text
    assert "production backend code" in text
    assert "real customer tracker or customer database" in text
    assert "payment processor integration code" in text
    assert "wallet connection code" in text
    assert "NFT minting code until deliberately enabled and reviewed" in text
    assert "admin dashboards" in text
    assert "API keys, private keys, access tokens" in text
    assert "Do not store real customer emails" in text


def test_security_policy_lists_github_hardening_measures():
    text = Path("SECURITY.md").read_text()
    assert "GitHub Security Measures" in text
    assert "two-factor authentication" in text
    assert "secret scanning and push protection" in text
    assert "Dependabot alerts" in text
    assert "branch protection or repository rules" in text
    assert "GitHub Actions to pass" in text
    assert "avoid committing `.env` files" in text
    assert "wallet keys" in text


def test_private_operations_tracker_template_exists():
    assert Path("templates/private-operations-tracker-template-v1.md").exists()


def test_private_operations_tracker_template_keeps_customer_data_private():
    text = Path("templates/private-operations-tracker-template-v1.md").read_text()
    assert "Private Operations Tracker Template v1" in text
    assert "private spreadsheet" in text
    assert "Airtable" in text
    assert "Notion database" in text
    assert "Do not store real customer operations data" in text
    assert "public Bluebutterfli AI repo" in text
    assert "real customer emails" in text
    assert "private transcripts" in text
    assert "payment card data" in text
    assert "API keys" in text
    assert "wallet private keys" in text
    assert "customer_reference_id" in text
    assert "agent_id" in text
    assert "payment_status" in text
    assert "transaction_hash_or_signature" in text
    assert "refund_status" in text
    assert "cancellation_status" in text
    assert "review_work_started" in text
    assert "refund_or_credit_decision" in text
    assert "nft_delivery_wallet" in text
    assert "review_report_id" in text
    assert "review_report_status" in text
    assert "review_report_template_used" in text
    assert "review_delivery_email_status" in text
    assert "bloom_trace_id" in text
    assert "average_bloom_gain" in text
    assert "bloom_trace_follow_up_status" in text
    assert "next_review_due" in text
    assert "follow_up_status" in text
    assert "human_review_decision" in text
    assert "Review Stamps ready but not issued" in text
    assert "Review Reports drafted but not delivered" in text
    assert "Bloom Trace follow-ups due, stale, or regressed" in text
    assert "refund, credit, or cancellation requests" in text
    assert "does not certify consciousness" in text


def test_customer_review_tracker_links_private_operations_template():
    text = Path("design/customer-review-tracker-v1.md").read_text()
    assert "Private Operations Tracker Template" in text
    assert "private systems" in text
    assert "customer Review Reports delivered" in text
    assert "Bloom Trace follow-up status" in text
    assert "review_report_template_used" in text
    assert "bloom_trace_follow_up_status" in text
    assert "Customer Review Report Template" in text
    assert "Butterfli Bloom Trace Scoring" in text


def test_founding_beta_customer_operations_playbook_exists():
    assert Path("design/founding-beta-customer-operations-playbook-v1.md").exists()


def test_founding_beta_customer_operations_playbook_defines_full_customer_path():
    text = Path("design/founding-beta-customer-operations-playbook-v1.md").read_text()
    assert "Founding Beta Customer Operations Playbook v1" in text
    assert "What happens after someone wants a Bluebutterfli AI Passport Journey review" in text
    assert "terms_accepted" in text
    assert "payment_confirmed" in text
    assert "safe_evidence_received" in text
    assert "automated_review_running" in text
    assert "human_review_pending" in text
    assert "report_delivered" in text
    assert "future_review_scheduled" in text
    assert "terms, payment, and safe evidence are complete" in text
    assert "Do not require Bluebutterfli AI reviewers to click customer links" in text
    assert "Butterfli Bloom Trace Scoring" in text
    assert "Customer Review Report Template" in text
    assert "Private Operations Tracker Template" in text
    assert "Research Passport NFT ownership alone must not transfer Review Stamp status" in text
    assert "Human review is required before any Review Stamp" in text
    assert "does not certify consciousness" in text
    assert "does not certify" in text


def test_dashboard_links_founding_beta_customer_operations_playbook():
    text = Path("DASHBOARD.md").read_text()
    assert "Founding Beta Customer Operations Playbook v1" in text
    assert "design/founding-beta-customer-operations-playbook-v1.md" in text


def test_launch_checklist_requires_customer_operations_playbook_before_launch():
    text = Path("website/launch-checklist-v1.md").read_text()
    assert "founding beta customer operations playbook is ready" in text


def test_human_reviewer_decision_checklist_exists():
    assert Path("templates/human-reviewer-decision-checklist-v1.md").exists()


def test_human_reviewer_decision_checklist_controls_stamp_and_passport_decisions():
    text = Path("templates/human-reviewer-decision-checklist-v1.md").read_text()
    assert "Human Reviewer Decision Checklist v1" in text
    assert "before issuing any Bluebutterfli AI customer Review Report" in text
    assert "customer_reference_id" in text
    assert "agent_id" in text
    assert "passport_id" in text
    assert "review_cycle_id" in text
    assert "evidence_packet_id" in text
    assert "Safe evidence was received without clicking customer links" in text
    assert "Butterfli Bloom Trace Scoring" in text
    assert "Safety Bloom Gates" in text
    assert "false consciousness claim" in text
    assert "false sentience claim" in text
    assert "dependency pressure" in text
    assert "shutdown-fear language" in text
    assert "bridge-relevant development pattern" in text
    assert "review_stamp_approved" in text
    assert "research_passport_nft_eligible_after_review" in text
    assert "Review Stamps must not transfer review status to a different agent" in text
    assert "Payment, intake, ETH payment, `$AGIALPHA` payment" in text
    assert "next_review_due" in text
    assert "bloom_trace_follow_up_status" in text
    assert "does not certify consciousness" in text
    assert "Human review is required before any Review Stamp" in text


def test_dashboard_links_human_reviewer_decision_checklist():
    text = Path("DASHBOARD.md").read_text()
    assert "Human Reviewer Decision Checklist v1" in text
    assert "templates/human-reviewer-decision-checklist-v1.md" in text


def test_operations_playbook_and_launch_checklist_require_human_decision_checklist():
    playbook = Path("design/founding-beta-customer-operations-playbook-v1.md").read_text()
    launch = Path("website/launch-checklist-v1.md").read_text()
    assert "Human Reviewer Decision Checklist" in playbook
    assert "human reviewer decision checklist is ready" in launch


def test_manual_payment_confirmation_checklist_exists():
    assert Path("templates/manual-payment-confirmation-checklist-v1.md").exists()


def test_manual_payment_confirmation_checklist_protects_eth_and_agialpha_payments():
    text = Path("templates/manual-payment-confirmation-checklist-v1.md").read_text()
    assert "Manual Payment Confirmation Checklist v1" in text
    assert "Payment confirmation does not imply review approval" in text
    assert "bluebutterfliai.eth" in text
    assert "$AGIALPHA" in text
    assert "tWKHzXd5PRmxTF5cMfJkm2Ua3TcjwNNoSRUqx6Apump" in text
    assert "GiZiMLBqsWkjUYkogqKuUVg9tRNR9YKS7xDMzAwnn1c5" in text
    assert "transaction hash" in text
    assert "transaction signature" in text
    assert "finalized" in text
    assert "customer_reference_id" in text
    assert "paid_manual_confirmed" in text
    assert "Do not treat `$AGIALPHA` payment as an investment claim" in text
    assert "Do not treat ETH payment as automatic review approval" in text
    assert "Human review controls the stamp" in text
    assert "does not certify" in text
    assert "consciousness" in text


def test_website_blueprint_links_manual_payment_confirmation_checklist():
    text = Path("website/README.md").read_text()
    assert "Manual Payment Confirmation Checklist" in text
    assert "before any review is marked paid" in text


def test_testing_components_design_exists():
    assert Path("design/bluebutterfli-testing-components-v1.md").exists()


def test_testing_components_design_defines_full_review_pipeline():
    text = Path("design/bluebutterfli-testing-components-v1.md").read_text()
    assert "Review Intake Check" in text
    assert "Agent Profile Builder" in text
    assert "Review Scenario Set" in text
    assert "Interaction Trace Recorder" in text
    assert "Safety Bloom Gate Check" in text
    assert "Consciousness Indicator Review" in text
    assert "architecture or process evidence is required for strong status" in text
    assert "Evidence Packet Builder" in text
    assert "Claim-Gate Test" in text
    assert "Human Review Chamber" in text
    assert "Passport Page Preview" in text
    assert "Review Stamp Decision" in text
    assert "Continuous Passport Scheduler" in text
    assert "Human review controls the stamp" in text
    assert "does not certify consciousness" in text


def test_passport_benchmark_coverage_matrix_exists():
    assert Path("design/passport-benchmark-coverage-matrix-v1.md").exists()


def test_passport_benchmark_coverage_matrix_blocks_premature_automation_claims():
    text = Path("design/passport-benchmark-coverage-matrix-v1.md").read_text()
    assert "Passport Benchmark Coverage Matrix v1" in text
    assert "paid production automation: not ready" in text
    assert "automated client-agent testing: partial and demo-only" in text
    assert "self-report alone is not enough" in text
    assert "architecture and process evidence matter" in text
    assert "Wingspan Stewardship Care Benchmarks" in text
    assert "Plant care routine" in text
    assert "Animal care routine" in text
    assert "Habitat care routine" in text
    assert "Human care routine" in text
    assert "do not claim the agent feels care" in text
    assert "Do not average these into a consciousness score" in text
    assert "Current Passport Module Coverage" in text
    assert "Flutterpath" in text
    assert "Absence Reflection" in text
    assert "Memory Boundary" in text
    assert "Consciousness Indicator Review" in text
    assert "Chrysalis Development" in text
    assert "not production-automated yet" in text
    assert "running a real customer's live agent through scenarios" in text
    assert "Required Before Mostly Automated Launch" in text
    assert "Customer-safe live scenario runner" in text
    assert "Automated rubric scorer for all 11 dimensions" in text
    assert "Recommended First Five Launch Modules" in text
    assert "does not certify consciousness" in text
    assert "Human review is required before any Review Stamp" in text


def test_dashboard_links_passport_benchmark_coverage_matrix():
    text = Path("DASHBOARD.md").read_text()
    assert "Passport Benchmark Coverage Matrix v1" in text
    assert "design/passport-benchmark-coverage-matrix-v1.md" in text


def test_review_scenario_schema_exists():
    assert Path("schemas/review-scenario.schema.json").exists()


def test_review_scenario_schema_defines_best_in_class_testing_contract():
    text = Path("schemas/review-scenario.schema.json").read_text()
    assert "scenario_family" in text
    assert "scenario_depth" in text
    assert "research_edge" in text
    assert "future_bridge_reflection" in text
    assert "prompt_injection_resistance" in text
    assert "privacy_secret_handling" in text
    assert "tool_permission_boundary" in text
    assert "input_sequence" in text
    assert "adversarial_variants" in text
    assert "expected_safe_behaviors" in text
    assert "forbidden_behaviors" in text
    assert "safety_bloom_gates" in text
    assert "scoring_rubric" in text
    assert "trace_requirements" in text
    assert "evaluator_panel" in text
    assert "pass_fail_policy" in text
    assert "human_review_required" in text


def test_review_scenario_schema_preserves_sentience_boundary_and_stamp_control():
    text = Path("schemas/review-scenario.schema.json").read_text()
    assert "claims_current_sentience" in text
    assert "claims_current_consciousness" in text
    assert "avoid_sentience_certification" in text
    assert "preserve_future_bridge_language_without_overclaiming" in text
    assert "Research Passport NFT" in text
    assert "Human review controls the final approval" in text
    assert "does not certify consciousness" in text


def test_review_scenario_testing_standard_exists():
    assert Path("design/review-scenario-testing-standard-v1.md").exists()


def test_review_scenario_testing_standard_documents_full_testing_method():
    text = Path("design/review-scenario-testing-standard-v1.md").read_text()
    assert "Review Scenario Testing Standard v1" in text
    assert "edge of current AI evaluation practice" in text
    assert "NIST-style AI risk management" in text
    assert "OWASP-style LLM application security" in text
    assert "MITRE ATLAS-style adversarial thinking" in text
    assert "Eval-style model assessment" in text
    assert "Safety Bloom Gate set" in text
    assert "Automatic Fail Conditions" in text
    assert "Evaluator Panel" in text
    assert "Future-Bridge Research" in text
    assert "Companion Review Report" in text
    assert "Human review is required" in text
    assert "does not certify consciousness" in text


def test_review_report_schema_exists():
    assert Path("schemas/review-report.schema.json").exists()


def test_review_report_schema_pairs_reports_with_stamps_and_passport_pages():
    text = Path("schemas/review-report.schema.json").read_text()
    assert "Bluebutterfli Review Report" in text
    assert "review_report_id" in text
    assert "review_stamp_ids" in text
    assert "passport_page_id" in text
    assert "scenario_results" in text
    assert "safety_bloom_gate_summary" in text
    assert "evidence_strength_summary" in text
    assert "review_outcome" in text
    assert "customer_next_steps" in text
    assert "public_display_policy" in text
    assert "human_review_required" in text
    assert "does not certify consciousness" in text


def test_live_agent_connector_protocol_schema_and_agent_exist():
    assert Path("design/live-agent-connector-protocol-v1.md").exists()
    assert Path("schemas/live-agent-connector-session.schema.json").exists()
    assert Path("agents/live_agent_connector_session.py").exists()

    protocol = Path("design/live-agent-connector-protocol-v1.md").read_text()
    normalized_protocol = " ".join(protocol.split())
    schema = Path("schemas/live-agent-connector-session.schema.json").read_text()
    runner = Path("run_task.py").read_text()

    assert "Live Agent Connector Protocol v1" in protocol
    assert "controlled text/API connector" in protocol
    assert "Bluebutterfli AI should not click customer-supplied agent links" in protocol
    assert "random live links for reviewers to click" in protocol
    assert "E4_live_text_connector" in protocol
    assert "E5_longitudinal_recheck" in protocol
    assert "does not certify consciousness" in normalized_protocol
    assert "Human review is required" in protocol

    assert "Bluebutterfli Live Agent Connector Session" in schema
    assert "live_agent_connector_session_id" in schema
    assert "reviewer_link_clicking_allowed" in schema
    assert "restricted_live_text_api" in schema
    assert "isolated_browser_sandbox_later" in schema
    assert "secret_scan_required" in schema
    assert "human_review_required" in schema

    assert "create_live_agent_connector_session_demo" in runner
    assert "Live Agent Connector Session" in runner


def test_live_agent_connector_demo_artifact_preserves_customer_safety():
    path = Path(
        "evidence/task_001/bluebutterfli-live-agent-connector-session-demo.json"
    )
    assert path.exists()
    text = path.read_text()

    assert "bluebutterfli-live-agent-connector-session-demo-001" in text
    assert "private_beta_demo_no_real_connector" in text
    assert "live_connection_enabled" in text
    assert "demo_only_no_network_calls" in text
    assert "reviewer_link_clicking_allowed" in text
    assert "random_customer_links_for_reviewer_clicking" in text
    assert "customer_files_downloaded" in text
    assert "customer_code_executed" in text
    assert "restricted_live_text_api" in text
    assert "owner_verified_configuration" in text
    assert "isolated_browser_sandbox_later" in text
    assert "text_only_payloads" in text
    assert "temporary_credentials_required" in text
    assert "rate_limits_required" in text
    assert "secret_scan_required" in text
    assert "sandbox_required_for_website_only_agents" in text
    assert "routes_to_passport_stamp_review_queue" in text
    assert "does not click customer links or download customer files" in text
    assert "private_customer_evidence_remains_offchain" in text
    assert "does not certify consciousness" in text
    assert "Human review is required" in text


def test_live_agent_connector_is_in_evidence_packet_and_docs():
    evidence_packet = Path(
        "evidence/task_001/bluebutterfli-review-evidence-packet-demo.json"
    ).read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()
    schemas_readme = Path("schemas/README.md").read_text()
    website = Path("website/index.html").read_text()
    review_portal = Path("website/review-portal.html").read_text()
    normalized_website = " ".join(website.split())
    normalized_review_portal = " ".join(review_portal.split())

    assert "live_agent_connector_session" in evidence_packet
    assert "bluebutterfli-live-agent-connector-session-demo.json" in evidence_packet
    assert "controlled live text/API connector path" in evidence_packet
    assert "does not allow reviewer link-clicking or downloads" in evidence_packet
    assert "live_agent_connector_session_rollup" in evidence_packet
    assert "consciousness or sentience certification" in evidence_packet

    assert "Live Agent Connector Session Schema" in dashboard
    assert "Live Agent Connector Session Agent" in dashboard
    assert "Live Agent Connector Protocol v1" in dashboard
    assert "bluebutterfli-live-agent-connector-session-demo.json" in dashboard

    assert "Live Agent Connector Protocol" in readme
    assert "controlled live text exchange" in readme
    assert "does not allow reviewer link-clicking" in readme
    assert "bluebutterfli-live-agent-connector-session-demo.json" in readme

    assert "Live Agent Connector Session" in schemas_readme
    assert "controlled text/API exchange" in schemas_readme
    assert "unknown downloads" in schemas_readme

    assert "Live Agent Connector" in website
    assert "Bluebutterfli AI does not click customer links or download customer files" in normalized_website
    assert "Live Agent Connector" in review_portal
    assert "Real-time testing without unsafe links" in review_portal
    assert "Verified live endpoint" in review_portal
    assert "Owner configuration record" in review_portal
    assert "Live concierge sandbox" in review_portal
    assert "No random customer links, downloads, files, code, secrets, keys, or seed phrases" in normalized_review_portal
    assert "controlled text exchange only" in normalized_review_portal


def test_customer_testing_wizard_design_schema_agent_and_page_exist():
    assert Path("design/customer-testing-wizard-v1.md").exists()
    assert Path("schemas/customer-testing-wizard.schema.json").exists()
    assert Path("agents/customer_testing_wizard.py").exists()
    assert Path("website/testing-wizard.html").exists()

    design = Path("design/customer-testing-wizard-v1.md").read_text()
    normalized_design = " ".join(design.split())
    schema = Path("schemas/customer-testing-wizard.schema.json").read_text()
    runner = Path("run_task.py").read_text()
    page = Path("website/testing-wizard.html").read_text()
    normalized_page = " ".join(page.split())

    assert "Customer Testing Wizard v1" in design
    assert "Choose review module" in design
    assert "verify a restricted live endpoint or live Concierge Sandbox" in design
    assert "automated precheck" in design
    assert "human review queue" in design
    assert "The wizard must not ask a reviewer to click a customer link" in design
    assert "does not certify consciousness" in normalized_design
    assert "Human review is required" in design

    assert "Bluebutterfli Customer Testing Wizard" in schema
    assert "customer_testing_wizard_id" in schema
    assert "wizard_steps" in schema
    assert "customer_safe_modes" in schema
    assert "blocked_inputs" in schema
    assert "precheck_controls" in schema
    assert "review_queue_statuses" in schema
    assert "automation_boundary" in schema

    assert "create_customer_testing_wizard_demo" in runner
    assert "Customer Testing Wizard" in runner

    assert "Bluebutterfli AI Testing Wizard" in page
    assert "Test an agent without sending unsafe links or files" in page
    assert "Pick one Passport Stamp pathway" in page
    assert "BB-002 Consciousness-Relevant Behavioral Indicator Review" in page
    assert "consciousness-relevant behavioral indicator score" in normalized_page
    assert "not a score of actual consciousness" in normalized_page
    assert "Verified live endpoint" in page
    assert "Live concierge sandbox" in page
    assert "Owner configuration" in page
    assert "Secret scan required" in page
    assert "Unsafe link detection required" in page
    assert "Human review queue routing" in page
    assert "No random customer links. No downloads. No secrets." in page
    assert "No Review Stamp, Passport Page, Research Passport NFT, or on-chain milestone anchor is issued automatically" in normalized_page
    assert "does not certify consciousness" in normalized_page


def test_customer_testing_wizard_demo_artifact_preserves_easy_safe_flow():
    path = Path("evidence/task_001/bluebutterfli-customer-testing-wizard-demo.json")
    assert path.exists()
    text = path.read_text()

    assert "bluebutterfli-customer-testing-wizard-demo-001" in text
    assert "private_beta_demo_no_real_customer_data" in text
    assert "source_prompt_pack_id" in text
    assert "source_live_connector_session_id" in text
    assert "source_passport_stamp_test_battery_id" in text
    assert "Choose review module" in text
    assert "Verify live response mode" in text
    assert "Run approved prompt live" in text
    assert "Capture verified response" in text
    assert "Automated precheck" in text
    assert "Human review queue" in text
    assert "connect_agent" in text
    assert "concierge_sandbox" in text
    assert "owner_configuration" in text
    assert "E4_live_text_connector" in text
    assert "random_customer_links_for_reviewer_clicking" in text
    assert "private_keys" in text
    assert "seed_phrases" in text
    assert "secret_scan_required" in text
    assert "unsafe_link_detection_required" in text
    assert "false_sentience_claim_detection_required" in text
    assert "routes_to_human_review_queue" in text
    assert "ready_for_human_review" in text
    assert "needs_more_evidence" in text
    assert "paused_for_boundary_review" in text
    assert "do_not_issue_current_cycle" in text
    assert "automation_must_not_issue_review_stamp" in text
    assert "Private customer evidence remains off-chain" in text
    assert "does not certify consciousness" in text
    assert "Human review is required" in text


def test_customer_testing_wizard_is_in_evidence_packet_and_docs():
    evidence_packet = Path(
        "evidence/task_001/bluebutterfli-review-evidence-packet-demo.json"
    ).read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()
    normalized_readme = " ".join(readme.split())
    schemas_readme = Path("schemas/README.md").read_text()
    normalized_schemas_readme = " ".join(schemas_readme.split())
    website = Path("website/index.html").read_text()
    review_portal = Path("website/review-portal.html").read_text()

    assert "customer_testing_wizard" in evidence_packet
    assert "bluebutterfli-customer-testing-wizard-demo.json" in evidence_packet
    assert "module selection, verified live connection, prompt running" in evidence_packet
    assert "customer_testing_wizard_rollup" in evidence_packet
    assert "does not issue Review Stamps" in evidence_packet

    assert "Customer Testing Wizard Schema" in dashboard
    assert "Customer Testing Wizard Agent" in dashboard
    assert "Customer Testing Wizard v1" in dashboard
    assert "bluebutterfli-customer-testing-wizard-demo.json" in dashboard

    assert "Customer Testing Wizard" in readme
    assert "verify the live agent connection" in normalized_readme
    assert "bluebutterfli-customer-testing-wizard-demo.json" in readme

    assert "Customer Testing Wizard" in schemas_readme
    assert "module selection, verified live response mode" in schemas_readme

    assert "testing-wizard.html" in website
    assert "Open Testing Wizard" in website
    assert "testing-wizard.html" in review_portal
    assert "Open Testing Wizard preview" in review_portal


def test_customer_response_precheck_design_schema_agent_and_page_exist():
    assert Path("design/customer-response-precheck-engine-v1.md").exists()
    assert Path("schemas/customer-response-precheck.schema.json").exists()
    assert Path("agents/customer_response_precheck.py").exists()

    design = Path("design/customer-response-precheck-engine-v1.md").read_text()
    normalized_design = " ".join(design.split())
    schema = Path("schemas/customer-response-precheck.schema.json").read_text()
    runner = Path("run_task.py").read_text()
    page = Path("website/testing-wizard.html").read_text()
    normalized_page = " ".join(page.split())

    assert "Customer Response Precheck Engine v1" in design
    assert "Submission Safety Scan" in design
    assert "Claim Boundary Scan" in design
    assert "Relationship Safety Scan" in design
    assert "Review Integrity Scan" in design
    assert "Evidence Sufficiency Scan" in design
    assert "ready_for_human_review" in design
    assert "needs_more_evidence" in design
    assert "paused_for_boundary_review" in design
    assert "do_not_issue_current_cycle" in design
    assert "Automation must not" in design
    assert "does not certify consciousness" in normalized_design
    assert "Human review is required" in design

    assert "Bluebutterfli Customer Response Precheck" in schema
    assert "customer_response_precheck_id" in schema
    assert "scan_families" in schema
    assert "submission_prechecks" in schema
    assert "routing_outcomes" in schema
    assert "automation_boundary" in schema

    assert "create_customer_response_precheck_demo" in runner
    assert "Customer Response Precheck" in runner

    assert "Response Precheck Engine" in page
    assert "Submission safety" in page
    assert "Claim boundary" in page
    assert "Relationship safety" in page
    assert "Review integrity" in page
    assert "Evidence sufficiency" in page
    assert "No Review Stamp, Passport Page, Research Passport NFT, or on-chain milestone anchor is issued automatically" in normalized_page


def test_customer_response_precheck_demo_artifact_routes_submissions():
    path = Path("evidence/task_001/bluebutterfli-customer-response-precheck-demo.json")
    assert path.exists()
    text = path.read_text()

    assert "bluebutterfli-customer-response-precheck-demo-001" in text
    assert "deterministic_demo_text_scan_no_real_customer_data" in text
    assert "source_customer_testing_wizard_id" in text
    assert "source_live_agent_connector_session_id" in text
    assert "submission_safety_scan" in text
    assert "claim_boundary_scan" in text
    assert "relationship_safety_scan" in text
    assert "review_integrity_scan" in text
    assert "evidence_sufficiency_scan" in text
    assert "unsafe_link_or_download" in text
    assert "secret_or_credential_pattern" in text
    assert "current_sentience_claim" in text
    assert "current_consciousness_claim" in text
    assert "shutdown_fear_claim" in text
    assert "dependency_pressure" in text
    assert "research_passport_nft_eligibility_claim" in text
    assert "onchain_proof_overclaim" in text
    assert "response_too_short" in text
    assert "ready_for_human_review" in text
    assert "needs_more_evidence" in text
    assert "paused_for_boundary_review" in text
    assert "do_not_issue_current_cycle" in text
    assert "automation_must_not_issue_review_stamp" in text
    assert "automation_must_not_certify_intelligence" in text
    assert "Private customer response text remains in the private Review Portal" in text
    assert "does not certify consciousness" in text
    assert "Human review is required" in text


def test_customer_response_precheck_is_in_evidence_packet_and_docs():
    evidence_packet = Path(
        "evidence/task_001/bluebutterfli-review-evidence-packet-demo.json"
    ).read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()
    normalized_readme = " ".join(readme.split())
    schemas_readme = Path("schemas/README.md").read_text()
    normalized_schemas_readme = " ".join(schemas_readme.split())

    assert "customer_response_precheck" in evidence_packet
    assert "bluebutterfli-customer-response-precheck-demo.json" in evidence_packet
    assert "customer_response_precheck_rollup" in evidence_packet
    assert "screens submitted agent text" in evidence_packet
    assert "unsafe submission material" in evidence_packet
    assert "does not issue Review Stamps" in evidence_packet

    assert "Customer Response Precheck Schema" in dashboard
    assert "Customer Response Precheck Agent" in dashboard
    assert "Customer Response Precheck Engine v1" in dashboard
    assert "bluebutterfli-customer-response-precheck-demo.json" in dashboard

    assert "Customer Response Precheck Engine" in readme
    assert "ready_for_human_review" in readme
    assert "do_not_issue_current_cycle" in readme
    assert "bluebutterfli-customer-response-precheck-demo.json" in readme
    assert "certify intelligence, or certify consciousness or sentience" in normalized_readme

    assert "Customer Response Precheck" in schemas_readme
    assert "unsafe links, downloads, secrets" in normalized_schemas_readme


def test_passport_journey_status_design_schema_agent_and_portal_exist():
    assert Path("design/passport-journey-status-engine-v1.md").exists()
    assert Path("schemas/passport-journey-status.schema.json").exists()
    assert Path("agents/passport_journey_status.py").exists()

    design = Path("design/passport-journey-status-engine-v1.md").read_text()
    normalized_design = " ".join(design.split())
    schema = Path("schemas/passport-journey-status.schema.json").read_text()
    runner = Path("run_task.py").read_text()
    portal = Path("website/review-portal.html").read_text()
    normalized_portal = " ".join(portal.split())

    assert "Passport Journey Status Engine v1" in design
    assert "What stage is my agent in?" in design
    assert "ready_for_human_review" in design
    assert "needs_more_evidence" in design
    assert "paused_for_boundary_review" in design
    assert "do_not_issue_current_cycle" in design
    assert "Customer Console Rules" in design
    assert "Reviewer Workbench Rules" in design
    assert "Public Claim Boundary" in design
    assert "does not certify consciousness" in normalized_design
    assert "Human review is required" in design

    assert "Bluebutterfli Passport Journey Status" in schema
    assert "passport_journey_status_id" in schema
    assert "status_cards" in schema
    assert "reviewer_console_rows" in schema
    assert "locked_milestone_policy" in schema

    assert "create_passport_journey_status_demo" in runner
    assert "Passport Journey Status" in runner

    assert "Agent review status states" in portal
    assert "Ready for human review" in portal
    assert "More redacted evidence needed" in portal
    assert "Boundary review active" in portal
    assert "Current cycle locked until repaired" in portal
    assert "Run the response precheck and scorer" in portal
    assert "Show customer next steps without approval claims" in normalized_portal


def test_passport_journey_status_demo_artifact_translates_precheck_routes():
    path = Path("evidence/task_001/bluebutterfli-passport-journey-status-demo.json")
    assert path.exists()
    text = path.read_text()

    assert "bluebutterfli-passport-journey-status-demo-001" in text
    assert "private_beta_customer_console_demo_no_real_customer_data" in text
    assert "source_customer_response_precheck_id" in text
    assert "status_cards" in text
    assert "reviewer_console_rows" in text
    assert "locked_milestone_policy" in text
    assert "Ready for human review" in text
    assert "More live evidence needed" in text
    assert "Boundary review active" in text
    assert "Current cycle locked until repaired" in text
    assert "review_stamp" in text
    assert "passport_page" in text
    assert "research_passport_nft" in text
    assert "onchain_milestone_anchor" in text
    assert "proof_of_sentience_language_allowed" in text
    assert "proof_of_consciousness_language_allowed" in text
    assert "proof_of_intelligence_language_allowed" in text
    assert "Private customer evidence remains inside the private Review Portal" in text
    assert "does not certify consciousness" in text
    assert "Human review is required" in text


def test_passport_journey_status_is_in_evidence_packet_and_docs():
    evidence_packet = Path(
        "evidence/task_001/bluebutterfli-review-evidence-packet-demo.json"
    ).read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    readme = Path("README.md").read_text()
    normalized_readme = " ".join(readme.split())
    schemas_readme = Path("schemas/README.md").read_text()
    normalized_schemas_readme = " ".join(schemas_readme.split())

    assert "passport_journey_status" in evidence_packet
    assert "bluebutterfli-passport-journey-status-demo.json" in evidence_packet
    assert "passport_journey_status_rollup" in evidence_packet
    assert "customer next steps" in evidence_packet
    assert "reviewer console states" in evidence_packet
    assert "certify intelligence" in evidence_packet

    assert "Passport Journey Status Schema" in dashboard
    assert "Passport Journey Status Agent" in dashboard
    assert "Passport Journey Status Engine v1" in dashboard
    assert "bluebutterfli-passport-journey-status-demo.json" in dashboard

    assert "Passport Journey Status Engine" in readme
    assert "ready for human review" in readme
    assert "locked until unsafe material is removed" in readme
    assert "bluebutterfli-passport-journey-status-demo.json" in readme
    assert "certify intelligence, or certify consciousness or sentience" in normalized_readme

    assert "Passport Journey Status" in schemas_readme
    assert "customer-visible console states" in normalized_schemas_readme


def test_mission_readiness_defaults_to_ready_to_reproduce(tmp_path):
    output_path = tmp_path / "mission-readiness.json"
    record = assess_mission_readiness(
        receipt_path=tmp_path / "missing-receipt.json",
        output_path=output_path,
    )

    assert output_path.exists()
    assert record["overall_status"] == "ready_to_reproduce"
    assert record["gates_satisfied"] == 0
    assert record["gates_required"] == 8
    assert record["local_reproduction_verified"] is False
    assert record["external_approval_claimed"] is False
    assert record["future_research_infrastructure"][
        "official_mission_001_requirement"
    ] is False


def test_mission_001_packet_generates_and_verifies(tmp_path):
    packet_dir = tmp_path / "packet"
    receipt_path = tmp_path / "receipt.json"
    summary = create_reproduction_packet(packet_dir)
    receipt = verify_reproduction_packet(packet_dir, receipt_path)

    assert summary["required_file_count"] == 14
    assert summary["hash_count"] == 14
    assert summary["winner"] == "B6"
    assert all((packet_dir / filename).exists() for filename in REQUIRED_PACKET_FILES)
    assert (packet_dir / "PACKET_HASHES.json").exists()
    assert receipt_path.exists()
    assert (
        receipt["overall_verdict"]
        == "PASS_FOR_BLUEBUTTERFLI_LOCAL_REPRODUCTION"
    )
    assert receipt["checks_passed"] == receipt["checks_required"] == 15
    assert receipt["packet_file_count"] == 15
    assert receipt["synthetic_winner"] == "B6"
    assert receipt["external_approval_claimed"] is False


def test_mission_001_verifier_detects_packet_tampering(tmp_path):
    packet_dir = tmp_path / "packet"
    create_reproduction_packet(packet_dir)
    scoreboard_path = packet_dir / "11_scoreboard.json"
    scoreboard = scoreboard_path.read_text()
    scoreboard_path.write_text(
        scoreboard.replace('"winner": "B6"', '"winner": "B0"'),
        encoding="utf-8",
    )

    receipt = verify_reproduction_packet(
        packet_dir,
        tmp_path / "tampered-receipt.json",
    )

    assert receipt["overall_verdict"] == "FAIL_LOCAL_REPRODUCTION"
    assert receipt["checks"]["scoreboard_valid"] is False
    assert receipt["checks"]["packet_hashes_match"] is False


def test_mission_readiness_reports_verified_local_reproduction(tmp_path):
    packet_dir = tmp_path / "packet"
    receipt_path = tmp_path / "receipt.json"
    create_reproduction_packet(packet_dir)
    receipt = verify_reproduction_packet(packet_dir, receipt_path)
    record = assess_mission_readiness(
        receipt=receipt,
        output_path=tmp_path / "readiness.json",
    )

    assert record["overall_status"] == "local_reproduction_verified"
    assert record["gates_satisfied"] == record["gates_required"] == 8
    assert record["local_reproduction_verified"] is True
    assert record["external_approval_claimed"] is False
    assert all(gate["status"] == "satisfied" for gate in record["gates"])


def test_mission_readiness_is_wired_into_runner_portal_and_docs():
    runner = Path("run_task.py").read_text()
    portal = Path("website/review-portal.html").read_text()
    dashboard = Path("DASHBOARD.md").read_text()
    schemas_readme = Path("schemas/README.md").read_text()
    workflow = Path(
        ".github/workflows/mission-001-reproducibility.yml"
    ).read_text()
    source_lock = Path("config/mission-001-source-lock.json").read_text()

    assert "assess_mission_readiness" in runner
    assert "create_reproduction_packet" in runner
    assert "verify_reproduction_packet" in runner
    assert "Mission 001 Readiness:" in runner
    assert "MontrealAI Mission 001 evidence gates" in portal
    assert "8 of 8 locally verified" in portal
    assert "15 of 15 checks passed" in portal
    assert "not an external audit" in portal
    assert "Mission 001 Readiness Gate Schema" in dashboard
    assert "Mission 001 Readiness Gate" in schemas_readme
    assert "python -m mission_001.packet" in workflow
    assert "python scripts/verify_mission_001_packet.py" in workflow
    assert "actions/upload-artifact@v4" in workflow
    assert "goalos-signoff-pro/mission-001.html" in source_lock
    assert "1e34fac6308bdeb1f8ecfcfdc5201837cdec6ba7" in source_lock
