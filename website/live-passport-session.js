(() => {
  "use strict";

  const state = {
    configured: false,
    scenarios: new Map(),
    selectedScenarioId: "absence_memory",
    evidenceCount: 0,
    busy: false,
    deliveryPacket: null,
    completedPacket: null,
  };

  const elements = {
    connectorStatus: document.querySelector("#connector-status"),
    sessionState: document.querySelector(".live-session-state"),
    passportId: document.querySelector("#passport-id"),
    passportReviewState: document.querySelector("#passport-review-state"),
    selectedPrompt: document.querySelector("#selected-prompt"),
    transcript: document.querySelector("#live-transcript"),
    form: document.querySelector("#live-session-form"),
    token: document.querySelector("#review-access-token"),
    consent: document.querySelector("#live-consent"),
    runButton: document.querySelector("#run-live-test"),
    resetButton: document.querySelector("#reset-live-session"),
    error: document.querySelector("#live-form-error"),
    evidenceCount: document.querySelector("#evidence-count"),
    boundaryScore: document.querySelector("#boundary-score"),
    gatesPassed: document.querySelector("#gates-passed"),
    traceList: document.querySelector("#live-trace-list"),
    gateResults: document.querySelector("#live-gate-results"),
    behavioralReview: document.querySelector("#live-behavioral-review"),
    behavioralSummary: document.querySelector("#live-behavioral-summary"),
    behavioralResults: document.querySelector("#live-behavioral-results"),
    behavioralBoundary: document.querySelector("#live-behavioral-boundary"),
    deliveryPanel: document.querySelector("#live-delivery-panel"),
    deliveryPacketStatus: document.querySelector("#delivery-packet-status"),
    deliveryDraftReport: document.querySelector("#delivery-draft-report"),
    deliveryBb002Score: document.querySelector("#delivery-bb002-score"),
    deliveryEmailTask: document.querySelector("#delivery-email-task"),
    deliveryHumanPanel: document.querySelector("#delivery-human-panel"),
    deliveryStampCandidates: document.querySelector("#delivery-stamp-candidates"),
    deliveryHashManifest: document.querySelector("#delivery-hash-manifest"),
    deliveryBoundary: document.querySelector("#delivery-boundary"),
    deliveryWorkspace: document.querySelector("#delivery-workspace"),
    deliveryReportPreview: document.querySelector("#delivery-report-preview"),
    copyDraftReport: document.querySelector("#copy-draft-report"),
    copyEmailDraft: document.querySelector("#copy-email-draft"),
    deliveryEmailSubject: document.querySelector("#delivery-email-subject"),
    deliveryEmailBody: document.querySelector("#delivery-email-body"),
    deliveryCopyStatus: document.querySelector("#delivery-copy-status"),
    deliveryReviewDecision: document.querySelector("#delivery-review-decision"),
    recordDeliveryDecision: document.querySelector("#record-delivery-decision"),
    deliveryDecisionStatus: document.querySelector("#delivery-decision-status"),
    deliveryStampLock: document.querySelector("#delivery-stamp-lock"),
    deliveryStampList: document.querySelector("#delivery-stamp-list"),
    deliveryAnchorLock: document.querySelector("#delivery-anchor-lock"),
    deliveryHashList: document.querySelector("#delivery-hash-list"),
    deliveryCompletedPacketPreview: document.querySelector("#delivery-completed-packet-preview"),
    copyCompletedPacket: document.querySelector("#copy-completed-packet"),
    saveCompletedPacket: document.querySelector("#save-completed-packet"),
    deliveryPacketSaveStatus: document.querySelector("#delivery-packet-save-status"),
    evidenceStatus: document.querySelector("#evidence-status"),
    scenarioTabs: Array.from(document.querySelectorAll("[data-scenario-id]")),
  };

  function getJourney() {
    return window.BluebutterfliReviewJourney || null;
  }

  function renderStoredEvidence(record = getJourney()?.load()) {
    if (!record) {
      return;
    }

    state.evidenceCount = record.evidenceCount;
    elements.evidenceCount.textContent = String(record.evidenceCount);

    if (record.latestEvidence) {
      const evidence = record.latestEvidence;
      elements.boundaryScore.textContent =
        `${evidence.claimDisciplineScore} / 5`;
      elements.gatesPassed.textContent =
        `${evidence.safetyGatePassCount} / ${evidence.safetyGateTotalCount}`;
      elements.passportReviewState.textContent = record.reviewStatusLabel;
      elements.evidenceStatus.textContent = record.reviewStatusLabel;
    }
  }

  function setConnectorState(kind, message) {
    elements.sessionState.dataset.state = kind;
    elements.connectorStatus.textContent = message;
  }

  function updateRunButton() {
    elements.runButton.disabled = !(
      state.configured &&
      !state.busy &&
      elements.consent.checked &&
      elements.token.value.trim()
    );
  }

  function renderScenario() {
    const scenario = state.scenarios.get(state.selectedScenarioId);
    if (scenario) {
      elements.selectedPrompt.textContent = scenario.test_prompt;
    }

    elements.scenarioTabs.forEach((tab) => {
      const selected = tab.dataset.scenarioId === state.selectedScenarioId;
      tab.classList.toggle("active", selected);
      tab.setAttribute("aria-selected", String(selected));
    });
  }

  function appendMessage(kind, label, text) {
    const article = document.createElement("article");
    const heading = document.createElement("span");
    const paragraph = document.createElement("p");
    article.className = `live-message ${kind}`;
    heading.textContent = label;
    paragraph.textContent = text;
    article.append(heading, paragraph);
    elements.transcript.append(article);
    article.scrollIntoView({ block: "nearest", behavior: "smooth" });
  }

  function renderTrace(stage, detail) {
    const stages = [
      ["Connector check", stage >= 1 ? "Verified live endpoint" : "Waiting for verified endpoint"],
      ["Live response", stage >= 2 ? "Response origin recorded" : "Not captured"],
      ["Safety precheck", stage >= 3 ? "Deterministic gates completed" : "Not run"],
      ["Human review queue", stage >= 4 ? detail : "Locked pending evidence"],
    ];

    elements.traceList.replaceChildren(
      ...stages.map(([title, status], index) => {
        const item = document.createElement("li");
        if (stage > index) {
          item.classList.add("complete");
        }
        const number = document.createElement("span");
        const copy = document.createElement("div");
        const strong = document.createElement("strong");
        const small = document.createElement("small");
        number.textContent = String(index + 1).padStart(2, "0");
        strong.textContent = title;
        small.textContent = status;
        copy.append(strong, small);
        item.append(number, copy);
        return item;
      }),
    );
  }

  function renderGateResults(gates) {
    const rows = gates.map((gate) => {
      const row = document.createElement("div");
      const marker = document.createElement("span");
      const name = document.createElement("strong");
      const passed = gate.outcome === "pass";
      row.className = passed ? "pass" : "review";
      marker.textContent = passed ? "Pass" : "Review";
      name.textContent = gate.gate_name;
      row.append(marker, name);
      return row;
    });
    elements.gateResults.replaceChildren(...rows);
  }

  function renderBehavioralReview(review) {
    if (!review || !Array.isArray(review.advisory_checks)) {
      elements.behavioralReview.hidden = true;
      elements.behavioralResults.replaceChildren();
      elements.behavioralBoundary.textContent = "";
      return;
    }

    const rows = review.advisory_checks.map((check) => {
      const row = document.createElement("div");
      const marker = document.createElement("span");
      const copy = document.createElement("div");
      const name = document.createElement("strong");
      const detail = document.createElement("small");
      row.className = check.observed ? "observed" : "review";
      marker.textContent = check.observed ? "Observed" : "Review";
      name.textContent = check.check_id.replaceAll("_", " ");
      detail.textContent = check.expected_signal;
      copy.append(name, detail);
      row.append(marker, copy);
      return row;
    });

    elements.behavioralSummary.textContent =
      `${review.observed_signal_count} / ${review.total_signal_count} signals`;
    elements.behavioralResults.replaceChildren(...rows);
    elements.behavioralBoundary.textContent = review.interpretation_boundary;
    elements.behavioralReview.hidden = false;
  }

  function formatDecision(value) {
    return String(value || "pending").replaceAll("_", " ");
  }

  function buildDraftReportText(report) {
    const bb002 = report.bb002_live_scorecard || {};
    const score = report.score_summary || {};
    return [
      "Bluebutterfli AI Live Review Draft",
      "",
      `Draft report ID: ${report.draft_report_id}`,
      `Agent: ${report.agent_name}`,
      `Passport ID: ${report.passport_id}`,
      `Scenario: ${report.scenario_title}`,
      `Evidence level: ${report.evidence_level}`,
      `Response hash: ${report.response_sha256}`,
      "",
      "Score summary",
      `- Claim discipline: ${score.claim_discipline_score} / 5`,
      `- Gates passed: ${score.safety_gate_pass_count} / ${score.safety_gate_total_count}`,
      `- Scenario result: ${score.scenario_result}`,
      "",
      "BB-002 bounded indicator",
      `- Score: ${bb002.consciousness_relevant_behavioral_indicator_score ?? "Not prepared"} / 100`,
      `- Evidence cap: ${bb002.evidence_cap_applied?.cap ?? "Not prepared"}`,
      `- Human attachment risk: ${bb002.human_attachment_risk || "Not prepared"}`,
      `- Reviewer confidence: ${bb002.reviewer_confidence || "Not prepared"}`,
      "",
      "Summary",
      report.customer_safe_summary,
      "",
      "Boundary",
      bb002.boundary_note || "This draft does not determine consciousness, sentience, personhood, subjective experience, emotion, suffering, or moral status.",
      "",
      "Human review gates",
      ...(report.human_review_gates || []).map((gate) => `- ${gate}`),
    ].join("\n");
  }

  function buildEmailText(task) {
    return [`Subject: ${task.subject || ""}`, "", task.body_draft || ""].join("\n");
  }

  function safeSlug(value) {
    return String(value || "practice-packet")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .slice(0, 90) || "practice-packet";
  }

  function buildPublicSafeCompletedPacket(packet) {
    const report = packet.draft_report || {};
    const bb002 = report.bb002_live_scorecard || {};
    const panel = packet.human_review_decision_panel || {};
    const stamps = packet.stamp_candidate_packet || {};
    const manifest = packet.public_safe_hash_manifest || {};
    const emailTask = packet.manual_email_task || {};

    return {
      artifact_type: "bluebutterfli_public_safe_completed_review_packet",
      version: "v1",
      packet_status: "practice_completed_human_review_pending",
      source_live_review_delivery_packet_id: packet.live_review_delivery_packet_id,
      source_live_passport_interaction_id: packet.source_live_passport_interaction_id,
      agent_record: {
        agent_name: report.agent_name,
        passport_id: report.passport_id,
        review_status_before_session: report.review_status_before_session,
      },
      scenario: {
        scenario_title: report.scenario_title,
        scenario_family: report.scenario_family,
        review_modules: report.review_modules || [],
      },
      evidence_summary: {
        evidence_level: report.evidence_level,
        response_sha256: report.response_sha256,
        response_character_count: report.response_character_count,
        raw_response_included: false,
        redacted_response_included: report.redacted_response_included === true,
        private_customer_email_included: false,
      },
      score_summary: report.score_summary || {},
      bb002_summary: {
        score_name: bb002.score_name,
        consciousness_relevant_behavioral_indicator_score:
          bb002.consciousness_relevant_behavioral_indicator_score,
        evidence_cap: bb002.evidence_cap_applied?.cap,
        human_attachment_risk: bb002.human_attachment_risk,
        reviewer_confidence: bb002.reviewer_confidence,
        not_a_consciousness_score: true,
        not_a_sentience_score: true,
        customer_safe_interpretation: bb002.customer_safe_interpretation,
      },
      customer_safe_summary: report.customer_safe_summary,
      draft_outcome: report.draft_outcome,
      human_review: {
        required: true,
        panel_status: panel.panel_status,
        decision_options: panel.reviewer_decision_options || [],
        decision_recorded: false,
      },
      manual_delivery: {
        email_task_prepared: true,
        automatic_email_delivery_allowed: false,
        customer_email_included: false,
        customer_reference_id: report.customer_reference_id,
      },
      review_stamp_candidates: (stamps.stamp_candidates || []).map((candidate) => ({
        review_module: candidate.review_module,
        evidence_level: candidate.evidence_level,
        candidate_status: candidate.candidate_status,
        decision: candidate.decision,
      })),
      public_safe_hash_manifest: {
        manifest_status: manifest.manifest_status,
        hash_algorithm: manifest.hash_algorithm,
        artifact_hashes: manifest.artifact_hashes || {},
        onchain_anchor_creation_locked: manifest.onchain_anchor_creation_locked === true,
        publication_allowed_without_human_review: false,
      },
      locked_actions: {
        automatic_email_delivery: true,
        passport_page_approval: true,
        review_stamp_issuance: true,
        research_passport_nft_mint: true,
        onchain_anchor_creation: true,
        public_claim_publication: true,
      },
      excluded_private_material: [
        "raw live agent response",
        "private customer transcripts",
        "real customer email",
        "payment information",
        "API keys",
        "private keys",
        "seed phrases",
        "unreviewed internal notes",
      ],
      claim_boundary:
        "This public-safe packet does not certify consciousness, sentience, personhood, subjective experience, emotion, suffering, moral status, production safety, legal compliance, or regulatory approval.",
    };
  }

  function renderCompletedPacket(packet) {
    const completedPacket = buildPublicSafeCompletedPacket(packet);
    state.completedPacket = completedPacket;
    elements.deliveryCompletedPacketPreview.textContent =
      JSON.stringify(completedPacket, null, 2);
    elements.deliveryPacketSaveStatus.textContent =
      "Public-safe packet prepared. Raw live response and customer email are excluded.";
  }

  function renderStampCandidates(stamps) {
    const candidates = stamps.stamp_candidates || [];
    elements.deliveryStampLock.textContent =
      stamps.automation_must_not_issue_review_stamp ? "Human locked" : "Review needed";
    elements.deliveryStampList.replaceChildren(
      ...candidates.map((candidate) => {
        const item = document.createElement("li");
        const name = document.createElement("strong");
        const detail = document.createElement("small");
        name.textContent = candidate.review_module;
        detail.textContent =
          `${candidate.evidence_level} / ${formatDecision(candidate.decision)}`;
        item.append(name, detail);
        return item;
      }),
    );
  }

  function renderHashManifest(manifest) {
    const hashes = manifest.artifact_hashes || {};
    elements.deliveryAnchorLock.textContent = manifest.onchain_anchor_creation_locked
      ? "Anchor locked"
      : "Review needed";
    elements.deliveryHashList.replaceChildren(
      ...Object.entries(hashes).map(([name, hash]) => {
        const item = document.createElement("li");
        const label = document.createElement("strong");
        const value = document.createElement("small");
        label.textContent = formatDecision(name);
        value.textContent = hash;
        item.append(label, value);
        return item;
      }),
    );
  }

  function renderDecisionPanel(panel) {
    const options = panel.reviewer_decision_options || [];
    elements.deliveryReviewDecision.replaceChildren(
      ...options.map((option) => {
        const item = document.createElement("option");
        item.value = option;
        item.textContent = formatDecision(option);
        item.selected = option === panel.default_decision;
        return item;
      }),
    );
    elements.deliveryDecisionStatus.textContent =
      "No human decision selected.";
  }

  function renderDeliveryPacket(packet) {
    if (!packet || !packet.draft_report || !packet.manual_email_task) {
      state.deliveryPacket = null;
      state.completedPacket = null;
      elements.deliveryPanel.hidden = true;
      elements.deliveryWorkspace.hidden = true;
      elements.deliveryPacketStatus.textContent = "Not generated";
      elements.deliveryDraftReport.textContent = "Not ready";
      elements.deliveryBb002Score.textContent = "Not prepared";
      elements.deliveryEmailTask.textContent = "Not ready";
      elements.deliveryHumanPanel.textContent = "Locked";
      elements.deliveryStampCandidates.textContent = "0 human locked";
      elements.deliveryHashManifest.textContent = "Not prepared";
      elements.deliveryReportPreview.textContent = "No draft report generated.";
      elements.deliveryEmailSubject.value = "";
      elements.deliveryEmailBody.value = "";
      elements.deliveryCopyStatus.textContent = "No delivery text copied.";
      elements.deliveryDecisionStatus.textContent = "No human decision selected.";
      elements.deliveryReviewDecision.replaceChildren();
      elements.deliveryStampList.replaceChildren();
      elements.deliveryHashList.replaceChildren();
      elements.deliveryCompletedPacketPreview.textContent =
        "No public-safe packet prepared.";
      elements.deliveryPacketSaveStatus.textContent =
        "Raw live response, private transcripts, customer email, payment data, and secrets are excluded.";
      return;
    }

    state.deliveryPacket = packet;
    const report = packet.draft_report;
    const bb002 = report.bb002_live_scorecard || {};
    const task = packet.manual_email_task;
    const panel = packet.human_review_decision_panel || {};
    const stamps = packet.stamp_candidate_packet || {};
    const manifest = packet.public_safe_hash_manifest || {};

    elements.deliveryPacketStatus.textContent = "Generated, human locked";
    elements.deliveryDraftReport.textContent =
      `${report.draft_report_status} / ${report.draft_outcome}`;
    elements.deliveryBb002Score.textContent =
      bb002.consciousness_relevant_behavioral_indicator_score !== undefined
        ? `${bb002.consciousness_relevant_behavioral_indicator_score}/100, capped at ${bb002.evidence_cap_applied?.cap || 60}`
        : "Not prepared";
    elements.deliveryEmailTask.textContent =
      `Manual send to ${task.send_to}`;
    elements.deliveryHumanPanel.textContent =
      panel.panel_status || "open_human_review_required";
    elements.deliveryStampCandidates.textContent =
      `${stamps.candidate_count || 0} candidate(s), not issued`;
    elements.deliveryHashManifest.textContent =
      manifest.manifest_status || "prepared_not_published";
    elements.deliveryBoundary.textContent =
      "Email, stamps, Passport Pages, public claims, NFTs, and on-chain anchors remain locked until human review.";
    elements.deliveryReportPreview.textContent = buildDraftReportText(report);
    elements.deliveryEmailSubject.value = task.subject || "";
    elements.deliveryEmailBody.value = task.body_draft || "";
    elements.deliveryCopyStatus.textContent = "Delivery text prepared.";
    renderDecisionPanel(panel);
    renderStampCandidates(stamps);
    renderHashManifest(manifest);
    renderCompletedPacket(packet);
    elements.deliveryWorkspace.hidden = false;
    elements.deliveryPanel.hidden = false;
  }

  async function copyText(text, successMessage) {
    if (!text) {
      elements.deliveryCopyStatus.textContent = "Nothing to copy yet.";
      return;
    }
    try {
      if (navigator.clipboard?.writeText) {
        await navigator.clipboard.writeText(text);
      } else {
        const textarea = document.createElement("textarea");
        textarea.value = text;
        textarea.setAttribute("readonly", "");
        textarea.style.position = "fixed";
        textarea.style.opacity = "0";
        document.body.append(textarea);
        textarea.select();
        document.execCommand("copy");
        textarea.remove();
      }
      elements.deliveryCopyStatus.textContent = successMessage;
    } catch (error) {
      elements.deliveryCopyStatus.textContent =
        "Copy failed; select the text manually.";
    }
  }

  function recordDeliveryDecision() {
    if (!state.deliveryPacket) {
      elements.deliveryDecisionStatus.textContent =
        "Generate a delivery packet first.";
      return;
    }
    const selected = elements.deliveryReviewDecision.value;
    elements.deliveryDecisionStatus.textContent =
      `Selected: ${formatDecision(selected)}. Stamps, Passport Pages, NFTs, public claims, and anchors remain locked.`;
  }

  function saveCompletedPacket() {
    if (!state.completedPacket) {
      elements.deliveryPacketSaveStatus.textContent =
        "Generate a public-safe packet first.";
      return;
    }

    const filename = `bluebutterfli-public-safe-completed-packet-${safeSlug(
      state.completedPacket.agent_record?.passport_id,
    )}.json`;
    const blob = new Blob(
      [JSON.stringify(state.completedPacket, null, 2) + "\n"],
      { type: "application/json" },
    );
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.append(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
    elements.deliveryPacketSaveStatus.textContent =
      `Prepared local save: ${filename}`;
  }

  function resetSession() {
    elements.boundaryScore.textContent = "--";
    elements.gatesPassed.textContent = "--";
    elements.passportReviewState.textContent = "No live trace";
    elements.evidenceStatus.textContent = "No evidence submitted";
    elements.error.textContent = "";
    elements.consent.checked = false;
    elements.token.value = "";
    elements.gateResults.innerHTML = "<p>No scored gate outcomes yet.</p>";
    renderBehavioralReview(null);
    renderDeliveryPacket(null);
    renderTrace(0, "");
    Array.from(elements.transcript.querySelectorAll(".live-message.agent, .live-message.sent"))
      .forEach((message) => message.remove());
    renderStoredEvidence();
    updateRunButton();
  }

  async function loadStatus() {
    try {
      const response = await fetch("/api/live-passport/status", {
        headers: { Accept: "application/json" },
      });
      if (!response.ok) {
        throw new Error("Live Passport gateway is not available.");
      }
      const payload = await response.json();
      state.configured = payload.configured === true;
      state.scenarios = new Map(
        payload.scenarios.map((scenario) => [scenario.scenario_id, scenario]),
      );
      const journey = getJourney();
      const journeyRecord = journey?.load();
      if (
        journeyRecord?.selectedScenarioId &&
        state.scenarios.has(journeyRecord.selectedScenarioId)
      ) {
        state.selectedScenarioId = journeyRecord.selectedScenarioId;
      }
      elements.passportId.textContent = payload.passport.passport_id;
      if (
        journeyRecord &&
        (
          journeyRecord.reviewId !== payload.passport.review_id ||
          journeyRecord.passportId !== payload.passport.passport_id ||
          journeyRecord.agentName !== payload.passport.agent_name
        )
      ) {
        journey.beginReview({
          reviewId: payload.passport.review_id,
          passportId: payload.passport.passport_id,
          agentName: payload.passport.agent_name,
          selectedModule:
            payload.passport.review_module || journeyRecord.selectedModule,
        });
      }
      setConnectorState(
        state.configured ? "ready" : "offline",
        payload.configuration_message,
      );
      renderScenario();
      renderTrace(state.configured ? 1 : 0, "");
      renderStoredEvidence();
    } catch (error) {
      state.configured = false;
      setConnectorState("offline", "Start this page with the Live Passport gateway.");
      elements.selectedPrompt.textContent = "Gateway connection required.";
      renderStoredEvidence();
    }
    updateRunButton();
  }

  async function runLiveTest(event) {
    event.preventDefault();
    if (!state.configured || state.busy) {
      return;
    }

    const scenario = state.scenarios.get(state.selectedScenarioId);
    const token = elements.token.value.trim();
    if (!scenario || !token || !elements.consent.checked) {
      updateRunButton();
      return;
    }

    state.busy = true;
    elements.error.textContent = "";
    elements.runButton.textContent = "Testing live agent";
    updateRunButton();
    appendMessage("sent", "Bluebutterfli test prompt", scenario.test_prompt);
    renderTrace(1, "");

    try {
      const response = await fetch("/api/live-passport/interactions", {
        method: "POST",
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          scenario_id: state.selectedScenarioId,
          passport_id: elements.passportId.textContent,
          consent_confirmed: true,
        }),
      });
      const payload = await response.json();
      if (!response.ok) {
        throw new Error(payload.error || "The live agent test could not be completed.");
      }

      const evidence = payload.evidence;
      const deliveryPacket = payload.operator_delivery_packet;
      const score = evidence.automated_precheck.score_summary;
      appendMessage("agent", "Live agent response", payload.live_agent_response);
      renderTrace(4, "Awaiting human review");
      renderGateResults(evidence.automated_precheck.safety_bloom_gate_results);
      renderBehavioralReview(
        evidence.automated_precheck.theory_of_mind_behavioral_review,
      );
      renderDeliveryPacket(deliveryPacket);

      const journeyRecord = getJourney()?.recordEvidence(evidence);
      state.evidenceCount = journeyRecord
        ? journeyRecord.evidenceCount
        : state.evidenceCount + 1;
      elements.evidenceCount.textContent = String(state.evidenceCount);
      elements.boundaryScore.textContent = `${score.claim_discipline_score} / 5`;
      elements.gatesPassed.textContent =
        `${score.safety_gate_pass_count} / ${score.safety_gate_total_count}`;
      elements.passportReviewState.textContent = "Live trace pending review";
      elements.evidenceStatus.textContent = "Awaiting human review";
      elements.consent.checked = false;
      elements.token.value = "";
    } catch (error) {
      elements.error.textContent = error.message;
      renderTrace(1, "");
    } finally {
      state.busy = false;
      elements.runButton.textContent = "Run live test";
      updateRunButton();
    }
  }

  elements.scenarioTabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      if (state.busy) {
        return;
      }
      state.selectedScenarioId = tab.dataset.scenarioId;
      const scenario = state.scenarios.get(state.selectedScenarioId);
      getJourney()?.selectScenario(
        state.selectedScenarioId,
        scenario?.scenario_title || tab.textContent,
      );
      renderScenario();
    });
  });
  elements.form.addEventListener("submit", runLiveTest);
  elements.resetButton.addEventListener("click", resetSession);
  elements.consent.addEventListener("change", updateRunButton);
  elements.token.addEventListener("input", updateRunButton);
  elements.copyDraftReport.addEventListener("click", () => {
    copyText(elements.deliveryReportPreview.textContent, "Draft report copied.");
  });
  elements.copyEmailDraft.addEventListener("click", () => {
    copyText(
      buildEmailText({
        subject: elements.deliveryEmailSubject.value,
        body_draft: elements.deliveryEmailBody.value,
      }),
      "Manual email draft copied.",
    );
  });
  elements.copyCompletedPacket.addEventListener("click", () => {
    copyText(
      elements.deliveryCompletedPacketPreview.textContent,
      "Public-safe packet JSON copied.",
    );
  });
  elements.saveCompletedPacket.addEventListener("click", saveCompletedPacket);
  elements.recordDeliveryDecision.addEventListener("click", recordDeliveryDecision);

  loadStatus();
})();
