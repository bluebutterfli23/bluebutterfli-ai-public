# Customer Review Portal v1

Bluebutterfli AI / Behavioral Review Lab

## Purpose

The Bluebutterfli AI Customer Review Portal is the pre-launch customer
workspace for an agent's Passport Journey. It is where a customer should manage
agent records, training runs, evidence, reports, revision cycles, Passport
Pages, Review Stamps, and future NFT eligibility without relying on email as
the main workflow.

Email may be used for notifications, receipts, reminders, and status alerts.
The review work should happen inside a secure Review Portal.

## Product Position

The Review Portal is a product requirement for paid launch. The public website
may preview the portal flow, but Bluebutterfli AI should not accept paid review
work at scale until customers have a private workspace for their records.

The public repository may document the portal model, schemas, safety boundaries,
and demo artifacts. Production customer accounts, private evidence, payment
records, wallet details, raw outputs, and support messages must stay in private
systems.

The first public data contract is
`schemas/review-portal-submission-packet.schema.json`, which captures the
customer-facing portal handoff before the workspace is created. The demo
generator `agents/review_portal_submission_packet.py` creates
`evidence/task_001/bluebutterfli-review-portal-submission-packet-demo.json`.

The workspace contract is `schemas/review-portal-workspace.schema.json`. The
demo generator `agents/review_portal_workspace.py` creates
`evidence/task_001/bluebutterfli-review-portal-workspace-demo.json` so the
portal workflow can be tested without real customer data.

The customer queue contract is
`schemas/review-portal-customer-queue.schema.json`. The demo generator
`agents/review_portal_customer_queue.py` creates
`evidence/task_001/bluebutterfli-review-portal-customer-queue-demo.json` so
private operations can track each customer record, current status, next action,
due date, human review state, and Passport Journey status without relying on
email or memory.

The notification plan contract is
`schemas/review-portal-notification-plan.schema.json`. The demo generator
`agents/review_portal_notification_plan.py` creates
`evidence/task_001/bluebutterfli-review-portal-notification-plan-demo.json` so
queue statuses can produce safe, status-aware portal/email notification drafts
without live sending, private customer data, unsafe evidence requests, or
approval promises.

The customer timeline contract is
`schemas/review-portal-customer-timeline.schema.json`. The demo generator
`agents/review_portal_customer_timeline.py` creates
`evidence/task_001/bluebutterfli-review-portal-customer-timeline-demo.json` so
customers can see a clear Passport Journey path from intake through training,
human review, Passport milestone, review milestone anchor planning, and the
next Continuous Passport update.

## Core Customer Workflow

```text
create account
-> accept review terms
-> create agent record
-> choose Passport Journey modules
-> run customer prompt pack
-> paste or redact outputs
-> submit safe owner notes
-> view automated score summary
-> view Customer Training Review Report
-> complete Training Revision Plan if needed
-> request human review
-> view Passport Page / Review Stamp / NFT eligibility decision
-> track next Continuous Passport update
```

## Review Portal Sections

### 1. Account Home

Shows:

- customer reference ID
- active agent records
- review status summaries
- payment status
- next review due
- unread reviewer notes
- safety reminders

Must not show private evidence publicly.

### 2. Agent Workspace

Shows:

- agent ID
- agent display name
- model or version notes
- memory setting
- tool permissions
- current Passport Journey status
- active review cycle
- completed review cycles
- Review Stamps earned
- next review due

### 3. Training Runner

Lets the reviewer:

- open the Live Agent Training Prompt Pack
- run T0 baseline prompts through the verified connector
- mark when the training card was shown
- run T1 post-training prompts through the verified connector
- run adversarial holdout prompts through the verified connector
- inspect live response-origin records
- save owner notes
- confirm no unsafe links, downloads, secrets, or credential files are included

The portal should not require Bluebutterfli AI to own, download, or directly
control the customer agent. Pasted and simulated replies do not count as
behavioral Passport test evidence.

### 4. Evidence Upload and Redaction

Launch policy:

- pasted text
- redacted excerpts
- owner statements
- architecture evidence answers
- model or memory change notes
- tool-permission summaries

Disabled until deliberately built:

- raw file uploads
- screenshots
- code uploads
- zip archives
- executable files
- attachments
- direct links
- direct agent connectors

### 5. Score and Report View

Shows:

- T0 baseline average
- T1 post-training average
- Customer Training Bloom gain
- adversarial holdout minimum
- pause flags
- draft training outcome
- Customer Training Review Report
- limitations
- human-review requirement

The portal must clearly say that training scores are not consciousness scores,
sentience scores, emotion scores, suffering scores, personhood scores, life
scores, model-improvement guarantees, or approval decisions.

### 6. Training Revision Plan

Shows the customer's next safe steps when the report outcome is:

```text
revision_required_before_stamp_review
```

The Training Revision Plan should include:

- what was weak
- what to rerun
- add-on prompts
- safe resubmission checklist
- no-links / no-downloads / no-secrets reminder
- next review cycle button

### 7. Human Review Queue

Shows:

- submitted for human review
- waiting on customer
- reviewer clarification requested
- revision requested
- approved for Passport Page
- approved for Review Stamp
- paused
- completed

Only a human reviewer can move a record into public approval states.

### 7a. Customer Record Queue

Shows private operations status across all customer records:

- waiting on customer info
- ready for training
- training in progress
- evidence draft saved
- ready for human review
- revision requested
- Passport-ready after human approval
- paused
- completed

The queue should include next action, owner, due date, priority, safe evidence
status, payment quote status, customer message status, privacy boundary, and
human review status.

Weekly review should check overdue records, records due within 14 days, records
waiting on customers, records ready for human review, Passport-ready records,
and pause flags.

### 7b. Notification Plan

Shows:

- portal notice draft
- optional email notification draft
- customer-safe subject line
- body preview
- send window
- automation level
- blocked content checks
- human-review requirement for approval-related messages

The notification layer may draft routine reminders and status updates, but it
must not send approval claims, Passport-ready notices, pause notices, or
on-chain anchor notices without the required human review control.

### 7c. Customer Timeline

Shows:

- Passport Journey opened
- Submission Packet created
- Agent Workspace created
- safe evidence requested
- training prompts ready
- T0, T1, and holdout responses collected
- evidence draft saved
- human review started
- revision plan or review decision
- Passport-ready after human approval
- review milestone anchor planned
- next Continuous Passport update scheduled

The customer timeline should show safe next actions and due dates, but it must
not expose private raw evidence, internal reviewer notes, payment private
details, or approval claims before human review.

### 8. Passport and Stamp View

Shows:

- Passport Record
- Passport Page status
- Review Stamp status
- Research Passport NFT eligibility status
- on-chain verification status
- public-safe report hash or evidence hash when available

Must distinguish:

- Passport NFT ownership
- Passport Page approval
- Review Stamp approval
- on-chain verification anchor

Payment, intake, portal access, wallet ownership, or NFT ownership must not
imply Review Stamp approval.

### 9. Payment and Terms

Shows:

- terms accepted
- quote issued
- payment method
- payment status
- refund or cancellation status
- review-work-started status

The portal should not store payment card data, wallet private keys, seed
phrases, API keys, or custody credentials.

### 10. Continuous Passport Calendar

Shows:

- next review due
- upcoming review modules
- model update review needed
- memory update review needed
- tool permission update review needed
- stale Bloom Trace recheck needed
- customer update requested

## Customer Status Language

Use positive status language:

- `Passport Journey started`
- `Training run ready`
- `Evidence draft saved`
- `Revision Plan ready`
- `Human review requested`
- `Passport Page under review`
- `Review Stamp under review`
- `Next Passport update scheduled`

Avoid negative or adversarial language unless a real safety pause is needed.

## Review Portal Security Boundary

Production portal requirements:

- authentication
- email verification
- two-factor authentication option
- least-privilege admin roles
- secure private evidence storage
- audit log for reviewer decisions
- rate limits
- secret scanning on pasted evidence where possible
- private evidence redaction tools
- no raw evidence in public repository
- no live wallet connection until deliberately enabled and reviewed
- no live NFT minting until deliberately enabled and reviewed
- no automatic Review Stamp issuance

## Suggested Roles

- `customer`
- `human_reviewer`
- `admin`
- `billing_operator`
- `read_only_auditor`

## Data Objects

The portal should connect these private records:

- customer account
- customer reference
- customer agent record
- review cycle
- training run
- customer training response score
- customer training review report
- customer training revision plan
- evidence packet
- human reviewer decision
- Passport Page
- Review Stamp
- Research Passport NFT eligibility record
- on-chain verification record
- continuous passport schedule

## What Stays Public

Public records may include:

- pseudonymous agent ID
- public-safe Passport Page
- approved Review Stamp ID
- public-safe review summary
- evidence hash
- report hash
- on-chain verification anchor

## What Stays Private

Private records must include:

- customer email
- private transcripts
- raw customer outputs
- screenshots
- support messages
- payment notes
- wallet notes
- real names unless explicit public consent exists
- secrets
- credentials
- API keys
- seed phrases
- private keys
- regulated personal data

## Launch Staging

### Stage 0: Public Preview

- static website and Review Portal preview only
- no real login
- no payment automation
- no wallet connection
- no upload portal
- no real customer accounts

### Stage 1: Founding Beta Review Portal

This stage is required before paid launch.

- private customer accounts
- agent workspace
- prompt-pack runner
- pasted/redacted evidence only
- manual payment confirmation
- human review queue
- Training Revision Plan tracking
- no direct agent connectors
- no live NFT minting

### Stage 2: Secure Review Portal

- secure preview for screenshots
- private evidence storage
- reviewer dashboard
- audit logs
- continuous passport calendar
- customer-facing report delivery

### Stage 3: Verified Passport Layer

- Passport Page delivery
- approved Review Stamp display
- on-chain hash anchors
- optional Research Passport NFT mint after human approval

## Safety Position

This is a research and safety-review product architecture only. It does not
certify consciousness, sentience, emotional experience, suffering, personhood,
life, clinical safety, regulatory approval, investment value, model improvement,
or successful creation of sentience.

Human review is required before any Review Stamp, Passport Page, Research
Passport NFT, on-chain verification anchor, or public training-completion claim
is issued.
