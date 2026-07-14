from pathlib import Path


PROFILE_PATH = Path("research/bluebutterfli-agi-business-profile-v1.md")


def test_business_profile_defines_the_independent_business_and_buyer():
    text = " ".join(PROFILE_PATH.read_text().split())

    assert "independently owned AI-agent behavioral review business" in text
    assert "target first-adopter profile" in text
    assert "founder-led AI-agent team" in text
    assert "does not disclose or imply a signed customer" in text


def test_business_profile_keeps_core_review_work_inside_bluebutterfli():
    text = " ".join(PROFILE_PATH.read_text().split())

    assert "Always Kept Inside Bluebutterfli" in text
    assert "customer identity, communications, and raw evidence" in text
    assert "unpublished scenarios, holdouts, scoring weights" in text
    assert "final decision authority" in text
    assert "Only public, synthetic, non-confidential, and reversible work" in text


def test_business_profile_states_current_agent_and_ecosystem_boundaries():
    text = " ".join(PROFILE_PATH.read_text().split())

    assert "operates Bluebutterfli Evidence Agent 001" in text
    assert "privately controlled local MVP" in text
    assert "requires human review for every output" in text
    assert "cannot access customer, personal, confidential" in text
    assert "Codex remains a work-support tool" in text
    assert "It is separate from Bluebutterfli Evidence Agent 001" in text
    assert "is not currently affiliated with, endorsed by" in text
    assert "No namespace, wallet, token transaction" in text
    assert "do not imply affiliation, endorsement" in text


def test_business_profile_references_only_public_readiness_evidence():
    text = " ".join(PROFILE_PATH.read_text().split())

    assert "AGI Business Readiness Pilot" in text
    assert "execution packet" in text
    assert "internally documented functional validation" in text
    assert "private implementation and generated draft are intentionally not published" in text
    assert "confidential beta evidence record" not in text
    assert "private review result" in text
