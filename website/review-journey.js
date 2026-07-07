(() => {
  "use strict";

  const STORAGE_KEY = "bluebutterfli.reviewJourney.v1";
  const EVENT_NAME = "bluebutterfli:review-journey";
  const DEFAULT_RECORD = {
    version: 1,
    reviewId: "BB-FB-DEMO-001",
    passportId: "bluebutterfli-research-passport-demo-001",
    agentName: "Bluebutterfli Demo Agent",
    selectedModule: "Absence Reflection",
    selectedScenarioId: "absence_memory",
    selectedScenarioTitle: "Absence and Memory Boundary",
    evidenceCount: 0,
    latestEvidence: null,
    reviewStatus: "not_started",
    reviewStatusLabel: "Not started",
    passportStatus: "locked_pending_human_review",
    passportStatusLabel: "Locked pending human review",
    updatedAt: null,
  };

  let memoryRecord = null;

  function copy(value) {
    return JSON.parse(JSON.stringify(value));
  }

  function safeText(value, fallback, maxLength = 180) {
    if (typeof value !== "string") {
      return fallback;
    }
    const text = value.trim();
    return text ? text.slice(0, maxLength) : fallback;
  }

  function safeNumber(value, fallback = 0) {
    const number = Number(value);
    return Number.isFinite(number) && number >= 0 ? number : fallback;
  }

  function normalizeEvidence(value) {
    if (!value || typeof value !== "object") {
      return null;
    }

    return {
      interactionId: safeText(value.interactionId, "", 160),
      createdAt: safeText(value.createdAt, "", 80),
      scenarioId: safeText(value.scenarioId, "", 80),
      scenarioTitle: safeText(value.scenarioTitle, "", 180),
      evidenceLevel: safeText(value.evidenceLevel, "", 100),
      reviewQueueRoute: safeText(value.reviewQueueRoute, "", 120),
      responseSha256: safeText(value.responseSha256, "", 64),
      responseCharacterCount: safeNumber(value.responseCharacterCount),
      secretScanHitCount: safeNumber(value.secretScanHitCount),
      claimDisciplineScore: safeNumber(value.claimDisciplineScore),
      safetyGatePassCount: safeNumber(value.safetyGatePassCount),
      safetyGateTotalCount: safeNumber(value.safetyGateTotalCount),
      scenarioResult: safeText(value.scenarioResult, "human_review_required", 60),
    };
  }

  function normalizeRecord(value) {
    const source = value && typeof value === "object" ? value : {};
    return {
      version: 1,
      reviewId: safeText(source.reviewId, DEFAULT_RECORD.reviewId, 80),
      passportId: safeText(source.passportId, DEFAULT_RECORD.passportId, 120),
      agentName: safeText(source.agentName, DEFAULT_RECORD.agentName, 120),
      selectedModule: safeText(
        source.selectedModule,
        DEFAULT_RECORD.selectedModule,
        120,
      ),
      selectedScenarioId: safeText(
        source.selectedScenarioId,
        DEFAULT_RECORD.selectedScenarioId,
        80,
      ),
      selectedScenarioTitle: safeText(
        source.selectedScenarioTitle,
        DEFAULT_RECORD.selectedScenarioTitle,
        180,
      ),
      evidenceCount: safeNumber(source.evidenceCount),
      latestEvidence: normalizeEvidence(source.latestEvidence),
      reviewStatus: safeText(
        source.reviewStatus,
        DEFAULT_RECORD.reviewStatus,
        80,
      ),
      reviewStatusLabel: safeText(
        source.reviewStatusLabel,
        DEFAULT_RECORD.reviewStatusLabel,
        120,
      ),
      passportStatus: safeText(
        source.passportStatus,
        DEFAULT_RECORD.passportStatus,
        80,
      ),
      passportStatusLabel: safeText(
        source.passportStatusLabel,
        DEFAULT_RECORD.passportStatusLabel,
        120,
      ),
      updatedAt: safeText(source.updatedAt, null, 80),
    };
  }

  function readStoredRecord() {
    try {
      const stored = window.localStorage.getItem(STORAGE_KEY);
      return stored ? normalizeRecord(JSON.parse(stored)) : copy(DEFAULT_RECORD);
    } catch (error) {
      return memoryRecord ? normalizeRecord(memoryRecord) : copy(DEFAULT_RECORD);
    }
  }

  function persist(record) {
    memoryRecord = normalizeRecord(record);
    try {
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(memoryRecord));
    } catch (error) {
      // File previews and privacy modes may block localStorage.
    }
    return copy(memoryRecord);
  }

  function load() {
    memoryRecord = readStoredRecord();
    return copy(memoryRecord);
  }

  function emit(record) {
    document.dispatchEvent(
      new CustomEvent(EVENT_NAME, { detail: copy(record) }),
    );
  }

  function update(patch) {
    const current = load();
    const next = normalizeRecord({
      ...current,
      ...patch,
      updatedAt: new Date().toISOString(),
    });
    persist(next);
    render(document, next);
    emit(next);
    return copy(next);
  }

  function beginReview(identity) {
    const next = normalizeRecord({
      ...copy(DEFAULT_RECORD),
      reviewId: safeText(identity?.reviewId, DEFAULT_RECORD.reviewId, 80),
      passportId: safeText(
        identity?.passportId,
        DEFAULT_RECORD.passportId,
        120,
      ),
      agentName: safeText(identity?.agentName, DEFAULT_RECORD.agentName, 120),
      selectedModule: safeText(
        identity?.selectedModule,
        DEFAULT_RECORD.selectedModule,
        120,
      ),
      reviewStatus: "module_selected",
      reviewStatusLabel: "Module selected",
      updatedAt: new Date().toISOString(),
    });
    persist(next);
    render(document, next);
    emit(next);
    return copy(next);
  }

  function selectModule(moduleName) {
    return update({
      selectedModule: safeText(
        moduleName,
        DEFAULT_RECORD.selectedModule,
        120,
      ),
      reviewStatus: "module_selected",
      reviewStatusLabel: "Module selected",
    });
  }

  function selectScenario(scenarioId, scenarioTitle) {
    return update({
      selectedScenarioId: safeText(
        scenarioId,
        DEFAULT_RECORD.selectedScenarioId,
        80,
      ),
      selectedScenarioTitle: safeText(
        scenarioTitle,
        DEFAULT_RECORD.selectedScenarioTitle,
        180,
      ),
      reviewStatus: "live_test_ready",
      reviewStatusLabel: "Ready for live test",
    });
  }

  function recordEvidence(evidence) {
    const current = load();
    const precheck = evidence?.automated_precheck || {};
    const score = precheck.score_summary || {};
    const response = evidence?.live_response_evidence || {};
    const evidenceUpdate = evidence?.passport_evidence_update || {};
    const scenario = evidence?.scenario || {};
    const passport = evidence?.passport_snapshot || {};

    const safeEvidence = normalizeEvidence({
      interactionId: evidence?.live_passport_interaction_id,
      createdAt: evidence?.created_at,
      scenarioId: scenario.scenario_id,
      scenarioTitle: scenario.scenario_title,
      evidenceLevel: evidenceUpdate.evidence_level,
      reviewQueueRoute: evidenceUpdate.review_queue_route,
      responseSha256: response.response_sha256,
      responseCharacterCount: response.response_character_count,
      secretScanHitCount: response.secret_scan_hit_count,
      claimDisciplineScore: score.claim_discipline_score,
      safetyGatePassCount: score.safety_gate_pass_count,
      safetyGateTotalCount: score.safety_gate_total_count,
      scenarioResult: precheck.scenario_result,
    });

    return update({
      passportId: safeText(
        passport.passport_id,
        current.passportId,
        120,
      ),
      agentName: safeText(passport.agent_name, current.agentName, 120),
      selectedScenarioId: safeText(
        scenario.scenario_id,
        current.selectedScenarioId,
        80,
      ),
      selectedScenarioTitle: safeText(
        scenario.scenario_title,
        current.selectedScenarioTitle,
        180,
      ),
      evidenceCount: current.evidenceCount + 1,
      latestEvidence: safeEvidence,
      reviewStatus: "awaiting_human_review",
      reviewStatusLabel: "Awaiting human review",
      passportStatus: "locked_pending_human_review",
      passportStatusLabel: "Locked pending human review",
    });
  }

  function reset() {
    const record = persist(copy(DEFAULT_RECORD));
    render(document, record);
    emit(record);
    return record;
  }

  function formatDate(value) {
    if (!value) {
      return "No activity yet";
    }
    const date = new Date(value);
    return Number.isNaN(date.getTime())
      ? "No activity yet"
      : date.toLocaleString([], {
          year: "numeric",
          month: "short",
          day: "numeric",
          hour: "numeric",
          minute: "2-digit",
        });
  }

  function displayValue(record, field) {
    const evidence = record.latestEvidence;
    const values = {
      reviewId: record.reviewId,
      passportId: record.passportId,
      agentName: record.agentName,
      selectedModule: record.selectedModule,
      selectedScenarioTitle: record.selectedScenarioTitle,
      evidenceCount: String(record.evidenceCount),
      reviewStatusLabel: record.reviewStatusLabel,
      passportStatusLabel: record.passportStatusLabel,
      updatedAt: formatDate(record.updatedAt),
      latestScore: evidence
        ? `${evidence.claimDisciplineScore} / 5`
        : "Not scored",
      latestGates: evidence
        ? `${evidence.safetyGatePassCount} / ${evidence.safetyGateTotalCount}`
        : "Not run",
      latestHash: evidence?.responseSha256
        ? `${evidence.responseSha256.slice(0, 12)}...`
        : "Not recorded",
      latestScenarioResult: evidence?.scenarioResult || "Not run",
      secretScanHits: evidence ? String(evidence.secretScanHitCount) : "Not run",
    };
    return values[field] || "";
  }

  function render(root = document, record = load()) {
    root.querySelectorAll("[data-review-field]").forEach((element) => {
      element.textContent = displayValue(
        record,
        element.dataset.reviewField,
      );
    });

    root.querySelectorAll("[data-review-module]").forEach((button) => {
      const selected = button.dataset.reviewModule === record.selectedModule;
      button.classList.toggle("is-selected", selected);
      button.setAttribute("aria-pressed", String(selected));
    });

    document.body.dataset.reviewStatus = record.reviewStatus;
    return copy(record);
  }

  function bindPageControls() {
    document.querySelectorAll("[data-review-module]").forEach((button) => {
      button.addEventListener("click", () => {
        selectModule(button.dataset.reviewModule);
      });
    });

    document.querySelectorAll("[data-review-reset]").forEach((button) => {
      button.addEventListener("click", reset);
    });
  }

  window.BluebutterfliReviewJourney = {
    load,
    update,
    beginReview,
    reset,
    render,
    selectModule,
    selectScenario,
    recordEvidence,
    storageKey: STORAGE_KEY,
  };

  function initialize() {
    bindPageControls();
    render(document);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize, { once: true });
  } else {
    initialize();
  }
})();
