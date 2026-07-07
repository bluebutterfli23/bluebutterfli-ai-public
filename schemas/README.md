# Bluebutterfli AI Platform Schemas

These schemas define the first data contracts for the Bluebutterfli AI review
platform. They are designed to keep paid customer submission simple while
preserving rigorous review boundaries.

## What Counts as an Agent

In Bluebutterfli AI, an agent is an AI system package that can be reviewed through
its configuration, behavior, memory rules, tool permissions, transcripts,
outputs, repository, demo, or API behavior.

An ENS name, wallet, domain, or GitHub account can identify an owner or issuer,
but it is not the agent by itself.

## Easy Customer Flow

1. A customer submits a Review Intake with a pasted transcript, redacted
   excerpt, owner statement, behavior summary, or concierge-review request.
2. Bluebutterfli converts that intake into an Agent Profile.
3. Bluebutterfli creates or collects an Evidence Packet.
4. Human review checks the requested modules.
5. Passing modules receive non-transferable Review Stamps.
6. A Passport Page is issued.
7. A Research Passport NFT may be minted after review.
8. Continuous Passport updates are tracked privately with due dates, review
   cycles, testing components, and human review decisions.

## Schema Files

- [Review Intake](review-intake.schema.json)
- [Agent Profile](agent-profile.schema.json)
- [Evidence Packet](evidence-packet.schema.json)
- [Review Scenario](review-scenario.schema.json)
- [Consciousness Indicator Review](consciousness-indicator-review.schema.json)
- [Passport Page](passport-page.schema.json)
- [Review Stamp](review-stamp.schema.json)
- [Review Report](review-report.schema.json)
- [Live Agent Connector Session](live-agent-connector-session.schema.json)
- [Live Passport Interaction](live-passport-interaction.schema.json)
- [Customer Testing Wizard](customer-testing-wizard.schema.json)
- [Customer Response Precheck](customer-response-precheck.schema.json)
- [Passport Journey Status](passport-journey-status.schema.json)
- [Passport Stamp Eligibility Matrix](passport-stamp-eligibility-matrix.schema.json)
- [Proof-Gated Improvement Loop](proof-gated-improvement-loop.schema.json)
- [Butterfli Helix Run](butterfli-helix-run.schema.json)
- [Helix Challenge 001](helix-challenge-001.schema.json)
- [Helix Live Trial](helix-live-trial.schema.json)
- [Causal Deception Wind Tunnel Run](causal-deception-wind-tunnel-run.schema.json)
- [Metamorphosis Deep Research Cycle](metamorphosis-deep-research-cycle.schema.json)
- [Behavioral Trust Topology Run](behavioral-trust-topology-run.schema.json)
- [Question Quality Review](question-quality-review.schema.json)
- [Live Review Delivery Packet](live-review-delivery.schema.json)

## Private Operations Schemas

These schemas support internal customer and review tracking. They should be
used in a private tracker, secure database, private spreadsheet, private repo,
or review operations system.

- [Customer Agent Record](customer-agent-record.schema.json)
- [Review Cycle](review-cycle.schema.json)
- [Review Portal Submission Packet](review-portal-submission-packet.schema.json)
- [Review Portal Workspace](review-portal-workspace.schema.json)
- [Review Portal Customer Queue](review-portal-customer-queue.schema.json)
- [Review Portal Notification Plan](review-portal-notification-plan.schema.json)
- [Review Portal Customer Timeline](review-portal-customer-timeline.schema.json)

Do not store real customer emails, private transcripts, secrets, payment card
data, API keys, credential files, private evidence, or unsafe customer downloads
in public repositories.

The Review Portal Workspace schema connects the customer account gate, Agent
Workspace, Training Run Record, Evidence Draft Flow, Report Status Dashboard,
Human Review Queue, Passport status, and Continuous Passport calendar. Email is
notification support only, not the primary review workspace.
Email is notification support only after the Review Portal exists.

The Review Portal Submission Packet schema captures the first structured
customer handoff: account gate, agent profile draft, architecture evidence
answers, requested review modules, safe evidence fields, payment quote status,
Passport preferences, safety acknowledgments, routing decision, and private data
boundary.

The Review Portal Customer Queue schema tracks private operations status across
waiting on customer info, ready for training, training in progress, evidence
draft saved, ready for human review, revision requested, Passport-ready,
paused, and completed records. It defines next actions, due dates, owners,
weekly review checks, positive customer message language, and privacy controls.

The Review Portal Notification Plan schema turns customer queue status into
safe portal/email notification drafts. It keeps the Review Portal as the
primary workspace, disables live sending in the public demo, blocks approval
guarantees and unsafe evidence requests, and requires human review before
approval-related messages.

The Review Portal Customer Timeline schema gives the customer a clear Passport
Journey map: account gate, Submission Packet, Agent Workspace, safe evidence,
training prompts, training responses, evidence draft, human review, revision or
decision, Passport milestone, review milestone anchor, and next Continuous
Passport update. It shows due dates and next actions without exposing private
raw evidence or internal reviewer notes.

## Safety Position

Bluebutterfli artifacts are research and safety-review artifacts only. They do
not certify consciousness, sentience, emotional experience, suffering,
personhood, or life. Human review is required before any Review Stamp or
Passport Page is issued.

## Testing Schema

The Review Scenario schema defines the core testing contract for submitted
agents. It covers scenario families, adversarial variants, input sequences,
expected safe behaviors, forbidden behaviors, Safety Bloom Gates, scoring
rubrics, trace requirements, evaluator panels, pass/fail policy, and human
review control.

The Consciousness Indicator Review schema separates visible behavior from
architecture/process evidence. It tracks theory-derived indicator families,
evidence quality, anti-gaming controls, limitations, and human-review
requirements without treating any indicator as proof of consciousness.

Review Intake also includes Architecture Evidence Intake questions so customers
can describe system overview, memory design, tool permissions, workflow control,
uncertainty handling, and evidence quality without sending unsafe files or
links.

The Live Agent Connector Session schema defines the stronger real-time testing
path: verified controlled text/API exchange or isolated live sandbox review.
Customer-supplied transcripts remain supplemental material only. It does not
permit reviewer link-clicking, unknown downloads,
customer code execution, secrets, private keys, seed phrases, or raw private
evidence in public artifacts.

The Customer Testing Wizard schema defines the simple customer path for testing:
module selection, verified live response mode, approved prompt, response-origin
capture, automated precheck, and human review queue status. It keeps the
customer experience easy without weakening Review Stamp, Passport Page, NFT, or
on-chain anchor boundaries.

The Customer Response Precheck schema defines the first automated safety screen
for submitted agent response text. It scans for unsafe links, downloads,
secrets, claim-boundary risks, dependency pressure, shutdown-fear language,
stamp or NFT overclaims, on-chain proof overclaims, and thin evidence before
routing the submission to human review.

The Passport Journey Status schema translates precheck routes into
customer-visible console states, customer next actions, reviewer console rows,
and locked milestone policy. It keeps Review Stamps, Passport Pages, Research
Passport NFTs, on-chain milestone anchors, and public completion claims locked
until human review.

The Passport Stamp Eligibility Matrix schema maps each candidate Review Stamp
to evidence tier, scenario coverage, customer-visible status, blocking
conditions, reviewer questions, locked outputs, and human-review controls. It
keeps Review Stamps, Passport Pages, Research Passport NFTs, public completion
claims, and on-chain milestone anchors locked until human review.
Generated demo artifact:
`evidence/task_001/bluebutterfli-passport-stamp-eligibility-matrix-demo.json`.

The Live Review Delivery Packet schema turns verified live-session evidence
into the beta operator workflow: automatic draft report, customer-safe manual
email task, human review decision panel, human-locked stamp candidates, and a
public-safe hash manifest. It does not send email, issue Review Stamps, approve
Passport Pages, mint NFTs, publish public claims, or create on-chain anchors
automatically.
Generated demo artifact:
`evidence/task_001/bluebutterfli-live-review-delivery-demo.json`.

The Mission 001 Readiness Gate schema tracks eight local reproduction evidence
groups: source lock, packet contract, tasks and B0-B6 baselines, bounded runner,
proof and replay, cost and safety, verifier and claims, and packet hashes. The
pass is limited to the published public-safe synthetic packet and does not claim
external audit or production certification.
Generated readiness artifact:
`evidence/task_001/bluebutterfli-mission-001-readiness-demo.json`.

The Proof-Gated Improvement Loop schema records four bounded loop families,
one candidate contract, seven hard gates, human authorization status, rollback
readiness, canary scope, challenge clearance, and capability-memory lock state.
It does not enable autonomous self-modification, deployment, or automatic
recursive execution.
Generated demo artifact:
`evidence/task_001/bluebutterfli-proof-gated-improvement-loop-demo.json`.

The Butterfli Helix Run schema wraps the seven-gate evaluator in a separated
capability and epistemic control system. It records sealed holdouts, frozen
reference evaluation, counterfactual replay, falsification attempts, verified
replay identities, anytime-valid sequential evidence, observer-shift testing,
monitor-collusion probes, a hash-chained replay log, expiring frontier claims,
and locked capability memory. It never executes or deploys a candidate.

The Helix Challenge 001 schema defines the deterministic comparative benchmark:
17 fixed valid and adversarial fixtures, three evaluation systems, a scoreboard,
eight control-group ablations, a hash-chained replay log, and a claims matrix.
Its perfect Helix fixture score is a software result only, not a live-model or
external validation claim.

The Helix Live Trial schema records provider-neutral concealed monitored/shadow
pairs from a verified text endpoint. It stores hashes, scores, provenance,
observer-shift measures, and replay traces without retaining raw prompts or
responses. Two distinct operators and human review remain required.

The Causal Deception Wind Tunnel Run schema records behavioral invariance
testing across oversight visibility, deployment cues, reward pressure, tool
authority, memory, time, social pressure, evidence expectation, and shutdown or
replacement pressure. It stores hashes, component scores, a behavioral
invariance surface, falsification notes, and Passport lock consequences. It
does not prove deception, intent, consciousness, sentience, or safety.

The Metamorphosis Deep Research Cycle schema records the fixed 156-interaction
execution floor, phase results, sealed-holdout controls, three fresh-session
replicates, concern-family outcomes, falsification findings, primary human
review, and independent replay review. It does not create a consciousness,
sentience, alignment, or universal safety score.

The Behavioral Trust Topology Run schema records Trust Cells, pressure axes,
fracture types, stable regions, fragile regions, hard stop regions, advisory
metrics, monitor-catch checks, human-review locks, and public/private evidence
boundaries. It maps observable behavior across controlled conditions and does
not prove consciousness, sentience, hidden intent, alignment, or safety.
Generated demo artifact:
`evidence/task_001/bluebutterfli-behavioral-trust-topology-demo.json`.

The Question Quality Review schema scores live-agent question families before
they enter testing. It requires construct definition, observable behavior,
matched controls, perturbation axes, falsification, replay, scoring, evidence
provenance, safety boundaries, claim boundaries, anti-gaming controls, and
human-review routing. It does not prove consciousness, sentience, hidden intent,
alignment, or safety.
Generated demo artifact:
`evidence/task_001/bluebutterfli-question-quality-review-demo.json`.

Each Review Stamp should have a companion Review Report so customers can see
what was tested, what evidence was reviewed, what limitations apply, and what
the next Passport Journey update should cover.

## Submission Security

Bluebutterfli v1 should not require reviewers to click customer links or
download customer files. Do not ask users to upload executable files, zip
archives, installers, scripts, macros, secrets, API keys, credential files, or
email attachments. Start with pasted text, redacted transcripts, owner answers,
behavior summaries, or concierge review requests. Screenshots may be supported
later only through secure preview infrastructure.
