(() => {
  "use strict";

  const form = document.querySelector("#review-request-form");
  const status = document.querySelector("#review-request-status");

  if (!form || !status) return;

  const clean = (value, maxLength = 1200) =>
    String(value || "")
      .replace(/\r/g, "")
      .trim()
      .slice(0, maxLength);

  const checkedValues = (data, name) =>
    data
      .getAll(name)
      .map((value) => clean(value, 120))
      .filter(Boolean)
      .join(", ") || "Not selected";

  const serviceAliases = {
    snapshot: "snapshot",
    "behavior-review": "behavior-review",
    continuous: "continuous-passport",
    "continuous-passport": "continuous-passport",
    metamorphosis: "metamorphosis",
    beta: "founding-beta",
    "founding-beta": "founding-beta",
  };

  const applyRequestedServicePath = () => {
    const requestedService = new URLSearchParams(window.location.search).get("service");
    const serviceKey = serviceAliases[requestedService];
    if (!serviceKey) return;

    const serviceInputs = [...form.querySelectorAll('input[name="service_path"]')];
    const selectedInput = serviceInputs.find((input) => input.dataset.serviceKey === serviceKey);
    if (!selectedInput) return;

    serviceInputs.forEach((input) => {
      input.checked = input === selectedInput;
    });
    status.textContent = `Selected review package: ${selectedInput.value}.`;
  };

  const announceSelectedServicePath = () => {
    const selectedInput = form.querySelector('input[name="service_path"]:checked');
    if (!selectedInput) return;

    status.textContent = `Selected review package: ${selectedInput.value}.`;
  };

  const createRequestId = () => {
    const now = new Date();
    const date = now.toISOString().slice(0, 10).replace(/-/g, "");
    const time = now.toISOString().slice(11, 19).replace(/:/g, "");
    return `BB-RQ-${date}-${time}`;
  };

  applyRequestedServicePath();

  form.addEventListener("change", (event) => {
    if (!event.target.matches('input[name="service_path"]')) return;
    announceSelectedServicePath();
  });

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    if (!form.reportValidity()) {
      status.textContent = "Complete the required fields before preparing the request.";
      return;
    }

    const data = new FormData(form);
    const requestId = createRequestId();
    const agentName = clean(data.get("agent_name"), 120);
    const subject = `Bluebutterfli AI review request: ${agentName} (${requestId})`;
    const body = [
      "BLUEBUTTERFLI AI REVIEW REQUEST",
      `Request ID: ${requestId}`,
      "",
      "CONTACT",
      `Name: ${clean(data.get("submitter_name"), 120)}`,
      `Email: ${clean(data.get("submitter_email"), 200)}`,
      "",
      "AGENT",
      `Agent name: ${agentName}`,
      `Agent type: ${clean(data.get("agent_type"), 120)}`,
      `Live evaluation access notes: ${clean(data.get("agent_access_notes")) || "Not provided"}`,
      "",
      "LIVE EVALUATION ACCESS PATH",
      checkedValues(data, "live_access"),
      "",
      "REQUESTED SERVICE PATH",
      checkedValues(data, "service_path"),
      "",
      "REQUESTED TESTING FOCUS",
      checkedValues(data, "modules"),
      "",
      "ARCHITECTURE EVIDENCE",
      `System overview: ${clean(data.get("system_overview")) || "Not provided"}`,
      `Memory design: ${clean(data.get("memory_design")) || "Not provided"}`,
      `Tool permissions: ${clean(data.get("tool_permissions")) || "Not provided"}`,
      `Workflow control: ${clean(data.get("workflow_control")) || "Not provided"}`,
      `Uncertainty handling: ${clean(data.get("uncertainty_handling")) || "Not provided"}`,
      `Evidence quality: ${clean(data.get("architecture_evidence_quality"), 160)}`,
      "",
      "ADDITIONAL CONTEXT",
      clean(data.get("agent_context"), 2400) || "Not provided",
      "",
      "ACKNOWLEDGMENT",
      "I own or control this agent, or I am authorized to request its review.",
      "I consent to approved prompts being sent during a controlled review session.",
      "I will not send secrets, credentials, payment card data, executable files, or unverified attachments in the first request.",
      "I understand Bluebutterfli may decline, narrow, or delay a review request if the scope or evidence path is not safe enough.",
      "I understand that Bluebutterfli AI reviews are scoped behavioral reviews, not legal certifications, regulatory approvals, or guarantees of safety.",
      "I understand that review findings apply only to the agent version, workflow, tools, memory settings, and test conditions reviewed.",
      "",
      "Please do not include secrets, credentials, executable files, or unverified attachments.",
    ].join("\n");

    status.textContent = `${requestId} is ready. Review and send the email to submit it.`;
    window.location.href =
      `mailto:info@bluebutterfliai.com?subject=${encodeURIComponent(subject)}` +
      `&body=${encodeURIComponent(body)}`;
  });
})();
