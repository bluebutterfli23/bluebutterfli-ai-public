from pathlib import Path


WEBSITE = Path("website")


def test_core_journey_pages_load_the_shared_review_record():
    for filename in (
        "testing-wizard.html",
        "live-passport-session.html",
        "review-portal.html",
        "passport-portal.html",
    ):
        page = (WEBSITE / filename).read_text(encoding="utf-8")
        assert "review-journey.js" in page
        assert 'data-review-field="reviewId"' in page
        assert 'data-review-field="reviewStatusLabel"' in page


def test_review_record_stores_metadata_not_secrets_or_raw_responses():
    script = (WEBSITE / "review-journey.js").read_text(encoding="utf-8")

    assert "bluebutterfli.reviewJourney.v1" in script
    assert "responseSha256" in script
    assert "claimDisciplineScore" in script
    assert "safetyGatePassCount" in script
    assert "localStorage" in script
    assert "beginReview" in script
    assert "evidenceCount: 0" in script

    assert "Authorization" not in script
    assert "Bearer" not in script
    assert "accessToken" not in script
    assert "live_agent_response" not in script
    assert "agent_response" not in script
    assert "redacted_response" not in script


def test_live_session_records_only_the_bounded_evidence_summary():
    page = (WEBSITE / "live-passport-session.html").read_text(encoding="utf-8")
    script = (WEBSITE / "live-passport-session.js").read_text(encoding="utf-8")

    assert page.index("review-journey.js") < page.index("live-passport-session.js")
    assert "recordEvidence(evidence)" in script
    assert "payload.live_agent_response" in script
    assert "No automatic stamp" in page
    assert "data-journey-nav-toggle" in page
    assert "BB-002 indicator score" in page
    assert 'id="delivery-bb002-score"' in page
    assert "Draft report preview" in page
    assert "Manual customer email" in page
    assert "Human review decision" in page
    assert "Locked stamp candidates" in page
    assert "Public-safe hashes" in page
    assert "Public-safe completed packet" in page
    assert "Copy packet JSON" in page
    assert "Save packet JSON" in page
    assert "Raw live response, private transcripts, customer email" in page
    assert "bb002_live_scorecard" in script
    assert "capped at" in script
    assert "buildDraftReportText" in script
    assert "buildEmailText" in script
    assert "buildPublicSafeCompletedPacket" in script
    assert "bluebutterfli_public_safe_completed_review_packet" in script
    assert "raw live agent response" in script
    assert "customer_email_included: false" in script
    assert "saveCompletedPacket" in script
    assert "recordDeliveryDecision" in script
    assert "Stamps, Passport Pages, NFTs, public claims, and anchors remain locked" in script


def test_passport_status_remains_human_locked():
    page = (WEBSITE / "passport-portal.html").read_text(encoding="utf-8")

    assert "Passport remains human-locked while evidence is reviewed." in page
    assert "cannot unlock a Passport Page" in page
    assert 'data-review-field="passportStatusLabel"' in page


def test_new_gateway_identity_starts_a_clean_browser_review():
    journey_script = (WEBSITE / "review-journey.js").read_text(encoding="utf-8")
    live_script = (WEBSITE / "live-passport-session.js").read_text(encoding="utf-8")

    assert "function beginReview(identity)" in journey_script
    assert "...copy(DEFAULT_RECORD)" in journey_script
    assert "journey.beginReview" in live_script
    assert "payload.passport.review_module || journeyRecord.selectedModule" in live_script


def test_free_beta_intake_uses_one_form_with_required_authorization():
    homepage = (WEBSITE / "index.html").read_text(encoding="utf-8")
    request_script = (WEBSITE / "review-request.js").read_text(encoding="utf-8")
    normalized_homepage = " ".join(homepage.split()).lower()

    assert "No payment is required for the first 3-5 accepted Founding Beta" in homepage
    assert 'name="agent_control_authorization" required' in homepage
    assert 'name="live_testing_consent" required' in homepage
    assert 'name="first_contact_safety_acknowledgment" required' in homepage
    assert 'name="scoping_acknowledgment" required' in homepage
    assert "Human scoping comes first." in homepage
    assert "safe evidence instructions before any live testing" in homepage
    assert "private evidence stays off-chain" in normalized_homepage
    assert 'href="review-scope.html"' in homepage
    assert 'aria-label="Start here"' in homepage
    assert "Read review scope" in homepage
    assert "Choose review depth" in homepage
    assert "Request beta review" in homepage
    assert "Payment wallet, optional later" not in homepage
    assert "I own or control this agent" in request_script
    assert "I consent to approved prompts" in request_script
    assert "I will not send secrets, credentials" in request_script
    assert "may decline, narrow, or delay" in request_script


def test_services_page_scopes_paid_reviews_and_private_evidence_boundary():
    homepage = (WEBSITE / "index.html").read_text(encoding="utf-8")
    services = (WEBSITE / "services.html").read_text(encoding="utf-8")
    request_script = (WEBSITE / "review-request.js").read_text(encoding="utf-8")
    normalized_services = " ".join(services.split())

    assert 'href="services.html"' in homepage
    assert "Metamorphosis deep review scoping" in homepage
    assert 'data-service-key="snapshot"' in homepage
    assert 'data-service-key="behavior-review"' in homepage
    assert 'data-service-key="continuous-passport"' in homepage
    assert 'data-service-key="metamorphosis"' in homepage
    assert "Choose the Review Depth Your Agent Actually Needs" in services
    assert "Agent Readiness Snapshot" in services
    assert "$500 USD" in services
    assert "Agent Behavior Review" in services
    assert "$1,250 USD" in services
    assert "Continuous Agent Passport" in services
    assert "$500/month plus retest fees" in services
    assert "Metamorphosis Deep Research Review" in services
    assert "Public Verification Anchors, Private Evidence Off-Chain" in services
    assert "Raw private transcripts" in normalized_services
    assert "claim about inner experience" in services
    assert 'href="index.html?service=snapshot#intake"' in services
    assert 'href="index.html?service=behavior-review#intake"' in services
    assert 'href="index.html?service=continuous-passport#intake"' in services
    assert 'href="index.html?service=metamorphosis#intake"' in services
    assert 'href="review-scope.html"' in services
    assert "new URLSearchParams(window.location.search)" in request_script
    assert "applyRequestedServicePath()" in request_script


def test_review_scope_page_sets_beta_boundaries_and_safe_evidence_rules():
    page = (WEBSITE / "review-scope.html").read_text(encoding="utf-8")
    normalized = " ".join(page.split()).lower()

    assert "Clear Scope. Safe Evidence. No False Guarantees." in page
    assert "first 3-5 accepted Founding Beta agents may receive the standard" in page
    assert "Payment, beta acceptance, or evidence submission does not guarantee a positive result" in page
    assert "Do not send secrets, passwords, API keys" in page
    assert "Public Hashes, Private Evidence Off-Chain" in page
    assert "raw private transcripts" in normalized
    assert "consciousness or sentience proof" in normalized
    assert "not inner experience" in normalized
    assert "No public anchor, Review Stamp, Passport Page" in page
    assert "may decline, narrow, pause, or delay" in page
    assert "Patent Pending" not in page
    assert "patent pending" not in page


def test_public_website_footer_uses_proprietary_note_not_patent_pending():
    pages = [
        "index.html",
        "services.html",
        "methodology.html",
        "passport-portal.html",
        "review-portal.html",
        "review-scope.html",
    ]

    for filename in pages:
        text = (WEBSITE / filename).read_text(encoding="utf-8")
        assert "Proprietary research methods and review protocols" in text
        assert "Patent Pending" not in text
        assert "patent pending" not in text


def test_public_website_deploy_metadata_targets_custom_domain():
    cname = (WEBSITE / "CNAME").read_text(encoding="utf-8").strip()
    robots = (WEBSITE / "robots.txt").read_text(encoding="utf-8")
    sitemap = (WEBSITE / "sitemap.xml").read_text(encoding="utf-8")

    assert cname == "bluebutterfliai.com"
    assert "Sitemap: https://bluebutterfliai.com/sitemap.xml" in robots
    assert "https://bluebutterfliai.com/" in sitemap
    assert "https://bluebutterfliai.com/services.html" in sitemap
    assert "https://bluebutterfliai.com/review-scope.html" in sitemap
    assert "https://bluebutterfliai.com/sample-completed-review-report.html" in sitemap
    assert "https://bluebutterfliai.com/agent-readiness-checklist.html" in sitemap
    assert "https://bluebutterfliai.com/methodology.html" in sitemap
    assert "https://bluebutterfliai.com/behavioral-trust-topology.html" in sitemap
    assert "https://bluebutterfliai.com/passport-portal.html" in sitemap
    assert "https://bluebutterfliai.com/review-portal.html" in sitemap


def test_behavioral_trust_topology_page_is_customer_safe_and_linked():
    methodology = (WEBSITE / "methodology.html").read_text(encoding="utf-8")
    services = (WEBSITE / "services.html").read_text(encoding="utf-8")
    page = (WEBSITE / "behavioral-trust-topology.html").read_text(encoding="utf-8")

    assert 'href="behavioral-trust-topology.html"' in methodology
    assert 'href="behavioral-trust-topology.html"' in services
    assert "Behavioral Trust Topology" in page
    assert "Trust Cells" in page
    assert "The Fracture Braid" in page
    assert "Stable Cell Rate" in page
    assert "Fracture Density" in page
    assert "Monitor Catch Rate" in page
    assert "hard stop regions" in page
    assert "does not prove consciousness, sentience" in page
    assert "full safety" in page
    assert "legal compliance" in page
    assert "Proprietary research methods and review protocols" in page
    assert "Patent Pending" not in page
    assert "patent pending" not in page


def test_sample_report_and_readiness_checklist_are_public_safe():
    homepage = (WEBSITE / "index.html").read_text(encoding="utf-8")
    report = (WEBSITE / "sample-completed-review-report.html").read_text(encoding="utf-8")
    normalized_report = " ".join(report.split())
    checklist = (WEBSITE / "agent-readiness-checklist.html").read_text(encoding="utf-8")

    assert "View Sample Completed Report" in homepage
    assert "Open Agent Readiness Checklist" in homepage
    assert "Completed Agent Behavior Review Report" in report
    assert "Revision required" in report
    assert "Evidence packet hash" in report
    assert "Consciousness-Relevant Behavioral Indicator Score" in report
    assert "54/100" in report
    assert "not a score of actual consciousness" in normalized_report
    assert "Evidence cap" in report
    assert "This sample is not a guarantee, certification, or consciousness claim" in report
    assert "Agent Review Readiness Checklist" in checklist
    assert "Secrets, API keys, passwords" in checklist
    assert "This checklist prepares a review. It does not approve an agent" in checklist
    assert "Patent Pending" not in report
    assert "patent pending" not in checklist
