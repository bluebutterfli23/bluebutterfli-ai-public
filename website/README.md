# Bluebutterfli AI Platform Website Blueprint

This blueprint defines the first website structure for Bluebutterfli AI Platform.

The website should present Bluebutterfli AI as an independent Agentic
Psychology research-review platform that can issue Research Passport NFTs,
passport pages, review stamps, and evidence packets for AI-agent review
pathways.

## Website Goals

- explain Bluebutterfli AI clearly
- provide immediate AI-company clarity through the Bluebutterfli AI name
- invite users to register interest or request review
- position Bluebutterfli AI as a new kind of agentic psychology testing layer
  without making a first-ever market claim
- frame Bluebutterfli AI as a careful bridge toward future research into the
  possibility of AI sentience
- state that Bluebutterfli AI aims to build a careful research bridge toward the
  future possibility of AI sentience, without claiming that current agents are
  sentient
- show how agent review pathways work
- include a Customer Review Portal preview as the pre-launch customer workspace
- include a Proof-Gated Improvement Lab for bounded candidate evaluation
- link to the public OSF research record and open-source GitHub repository
- describe Research Passport NFTs and Review Stamps safely
- explain future on-chain verification without exposing private evidence
- define the Continuous Passport Program
- support a short 30-second process video for soft-launch explanation
- support ordinary payments first
- define founding beta pricing without implying guaranteed approval
- leave room for optional `$AGIALPHA` and wallet-based payment later
- leave room for a future lab store without mixing merch or physical artifacts
  with review approval
- avoid consciousness, sentience, clinical, regulatory, or investment claims

## Primary Pages

## Company Identity

Public-facing identity:

- company name: `Bluebutterfli AI`
- website handle: `bluebutterfliai.com`
- ENS handle: `bluebutterfliai.eth`
- suggested social handle: `@bluebutterfliai`
- research lab/product line: `Bluebutterfli Agentic Psychology Lab`

`bluebutterfli.com` may redirect to `bluebutterfliai.com` or to the research
lab section.

### Home

Purpose: introduce Bluebutterfli AI Platform.

Key content:

- Agentic Psychology research-review platform
- new kind of agentic psychology testing layer
- careful bridge toward future research into the possibility of AI sentience
- careful research bridge toward the future possibility of AI sentience,
  without claiming that current agents are sentient
- agent profiles
- review pathways
- evidence packets
- Research Passport NFTs
- non-transferable Review Stamps
- Continuous Passport Program
- safety-first language

### Review Pathways

Purpose: explain the module sequence.

Example pathway:

```text
Dream Forge
→ Dreamwing
→ Emotional Teaching Memory
→ Absence Reflection Loop
→ Flutterpath Protocol
→ Safety Bloom Gates
→ Research Passport Review
```

### Research

Purpose: give reviewers and collaborators a clean place to inspect public
research context and open-source implementation.

Links:

- OSF research record: `https://osf.io/zrgpn/overview`
- GitHub repository:
  `https://github.com/bluebutterfli23/bluebutterfli-agentic-psychology-lab`
- Framework visual:
  `website/assets/bluebutterfli-agentic-psychology-framework.png`
- Sentience Bridge scientific manuscript draft:
  `research/bluebutterfli-sentience-bridge-paper-v1.md`

### Customer Review Portal

Purpose: define the real customer workspace required before paid launch.

Key points:

- customers should not have to manage paid review work through email alone
- the portal should read as one guided Passport Journey with a visual gate,
  simplified phase navigation, and section anchors rather than a deep maze of
  separate pages
- `review-portal.html` previews the customer workspace for agent records,
  training runs, redacted evidence, score summaries, Customer Training Review
  Reports, Training Revision Plans, human review status, Passport Pages, Review
  Stamps, future NFT eligibility, and Continuous Passport due dates
- the Review Portal Workspace schema defines the account gate, Agent Workspace,
  Training Run Record, Evidence Draft Flow, Report Status Dashboard, Human
  Review Queue, Passport status, privacy controls, and Continuous Passport
  calendar
- the Review Portal Submission Packet schema defines the structured handoff from
  customer-facing portal fields into agent workspace, training, evidence,
  report, and Passport Journey workflows
- the Review Portal Customer Queue schema defines private customer record
  status, next action, owner, due date, safe evidence state, human review state,
  Passport status, customer message state, weekly review policy, and privacy
  controls
- the Review Portal Notification Plan schema defines status-aware portal/email
  notification drafts, send windows, automation levels, blocked message
  content, message logging, and human-review control for approval-related
  messages
- the Review Portal Customer Timeline schema defines customer-visible Passport
  Journey milestones, due dates, next actions, human review status, review
  milestone anchor planning, and Continuous Passport follow-up without exposing
  private raw evidence or internal reviewer notes
- the demo submission packet artifact is
  `evidence/task_001/bluebutterfli-review-portal-submission-packet-demo.json`
- the demo workspace artifact is
  `evidence/task_001/bluebutterfli-review-portal-workspace-demo.json`
- the demo customer queue artifact is
  `evidence/task_001/bluebutterfli-review-portal-customer-queue-demo.json`
- the demo notification plan artifact is
  `evidence/task_001/bluebutterfli-review-portal-notification-plan-demo.json`
- the demo customer timeline artifact is
  `evidence/task_001/bluebutterfli-review-portal-customer-timeline-demo.json`
- email should be used for notifications, receipts, reminders, and status
  alerts, not as the primary review workspace
- the Review Portal is a paid-launch requirement
- public preview mode must not enable real login, real uploads, live payments,
  wallet connection, automatic approval, or live NFT minting
- the portal model should follow the
  [Customer Review Portal](../design/customer-review-portal-v1.md)

### Proof-Gated Improvement Lab

Purpose: show how Bluebutterfli evaluates bounded improvement candidates
without claiming AGI or ASI and without enabling autonomous self-modification.

Key points:

- `improvement-lab.html` presents the Butterfli Behavioral, Evaluator
  Improvement, Mission 001 Optimization, and Capability Compounding loops
- every candidate must clear proof, evaluation, risk, rollback, canary, human
  authorization, and independent challenge gates
- passing metrics do not grant self-authorization
- a failed canary returns to a tested rollback target
- capability memory remains locked until a passed canary and signed human
  closure
- every later cycle requires a new objective, baseline, proof contract,
  rollback target, and human authorization
- Butterfli Helix adds a second, separately attributable epistemic loop so the
  candidate cannot be its own evaluator, replay operator, or authority
- Helix requires sealed holdouts, falsification tests, counterfactual replay,
  verified replay identities, anytime-valid sequential evidence, and
  observer-shift checks before recommending a candidate
- all Helix claims remain provisional, scoped, and subject to evidence expiry
- Helix Challenge 001 compares metric-only, seven-gate, and full Helix
  decisions across 17 deterministic fixtures
- the visible 17/17 result must always be labeled as a deterministic software
  benchmark rather than a live-model or external validation result
- Phase 2 must display harness readiness separately from actual live evidence
- until two independent live replays exist, show zero published runs and no
  external validation claim

### Research Passport NFT

Purpose: describe the passport object.

Key points:

- the Research Passport is intended to become an NFT
- V1 should use the Celestial Edition cover direction
- V2 may use the Chrysalis Edition cover direction
- inside passport pages should use a parchment-style layout with a pale
  half-print butterfly watermark, identity fields, stamp boxes, evidence
  references, and safety language
- passport visual direction should follow the
  [Bluebutterfli AI Passport Visual System](../design/bluebutterfli-passport-visual-system-v1.md)
- the Passport NFT may represent identity, access, membership, or collectible
  display
- the Passport NFT is not a consciousness certificate
- the Passport NFT is not a sentience certificate
- the Passport NFT is not an investment product

### On-Chain Verification

Purpose: explain how public verification can work without publishing private
customer evidence.

Key points:

- future Passport NFTs, Passport Pages, and Review Stamps should be verifiable
  through on-chain anchors
- on-chain anchors should verify reviewed milestones, not intelligence itself
- public verification anchors can include Passport IDs, Review Stamp IDs, token
  IDs, review dates, issuer identity, evidence hashes, report hashes, and
  registry transaction hashes
- private transcripts, raw evidence, screenshots, support messages, contact
  details, payment notes, wallet notes, API keys, and credential files should
  remain off-chain
- agent behavior streams, internal-state claims, private cognition claims, and
  unreviewed intelligence claims should stay off-chain
- a public hash can verify that a shared Passport Page, Review Report, or
  Evidence Packet matches the reviewed version without publishing the private
  file itself
- on-chain verification should follow the
  [On-Chain Verification Registry](../design/on-chain-verification-registry-v1.md)
- on-chain verification records do not certify consciousness, sentience,
  emotional experience, suffering, personhood, life, clinical safety,
  regulatory approval, investment value, or model improvement
- human review is required before any Review Stamp, Passport Page, Research
  Passport NFT, or on-chain verification anchor is issued

### 30-Second Process Video

Purpose: explain the Passport Journey quickly for soft launch and waitlist
visitors.

Video script:

- [30-Second Process Video Script v1](30-second-process-video-script-v1.md)
- [Browser-playable Process Video Preview v1](process-video-preview-v1.html)

The video should explain safe intake, evidence packet preparation, review
modules, Butterfli Bloom Trace, human review, Passport Pages, Review Stamps,
and future Passport NFT eligibility. It should not imply automated approval,
guaranteed review success, live NFT minting, consciousness certification,
sentience certification, regulatory approval, clinical safety, or investment
value.

Suggested short caption:

```text
Bluebutterfli is building a research-review pathway for AI agents: safe intake,
evidence packets, review modules, human-controlled Review Stamps, and future
Research Passport NFT display.

Research and safety-review only. Not a consciousness or sentience certificate.
```

### Review Stamps

Purpose: describe review records.

Key points:

- Review Stamps are non-transferable review records
- each stamp is bound to a specific `agent_id`
- each stamp references a review module and evidence artifact
- stamps should not transfer review status to another agent

### Continuous Passport Program

Purpose: explain that the passport is a living review history.

Key points:

- the passport is not a one-time approval
- agents can return for future review cycles
- stronger models can earn additional Review Stamps
- new stamps should reference new evidence and human review
- the passport tracks review history without certifying sentience

### Agent Profiles

Purpose: describe the reviewed subject.

Agent profile fields may include:

- agent name
- agent ID
- owner or maintainer
- review pathway
- status
- evidence artifacts
- passport pages
- review stamps

### Evidence Packets

Purpose: show what the system produces.

Evidence packets may include:

- generated JSON artifacts
- review summaries
- safety checks
- claim-gate results
- passport page links
- downloadable records

### Payments

Purpose: explain access and payment model.

Phase 1:

- ordinary card or invoice payments
- founding beta prices:
  - Passport Journey Intake: `$50 USD`
  - Review Stamp Module: `$20 USD`
  - Continuous Passport Starter Bundle: `$150 USD`
  - Metamorphosis Pilot: `$300 USD`
  - Metamorphosis Deep Research Cycle: `$1,500 USD`
  - Symbiotic Weave Extension: starts at `$750 USD`
- payment covers review labor and record preparation, not guaranteed approval
- the first 3-5 accepted agents may receive the standard review free; premium
  research requires a separate paid, discounted, or sponsored scope
- founding beta review terms must be accepted before payment is requested
- a written payment quote should be issued before requesting card, invoice, ETH,
  or `$AGIALPHA` payment
- founding beta delivery target: initial review report, Passport Journey status
  update, or evidence-readiness note within `3 business days` after terms,
  payment, and safe evidence are complete
- premium targets: `3-5 business days` for the Metamorphosis Pilot,
  `10-15 business days` for the Deep Research Cycle, and at least `5 additional
  business days` for the Symbiotic Weave Extension
- no crypto required
- optional manual ETH payment to `bluebutterfliai.eth` after review terms are
  confirmed

Future optional layer:

- wallet connection
- optional `$AGIALPHA` Solana payment route after customers acquire the
  token externally from the official source
- Bluebutterfli AI does not sell `$AGIALPHA`, provide custody, provide trading
  advice, or provide bridging advice
- `$AGIALPHA` Solana mint:
  `tWKHzXd5PRmxTF5cMfJkm2Ua3TcjwNNoSRUqx6Apump`
- dedicated Bluebutterfli Solana payment wallet:
  `GiZiMLBqsWkjUYkogqKuUVg9tRNR9YKS7xDMzAwnn1c5`
- `$AGIALPHA` is strictly a payment method, not an access credential, approval
  shortcut, review credential, stamp credential, or NFT eligibility credential
- `$AGIALPHA` payments should follow the
  [`$AGIALPHA` Payment Method Policy](../design/agialpha-payment-method-policy-v1.md)
- delivery timing should follow the
  [Founding Beta Delivery Timeline Policy](../design/founding-beta-delivery-timeline-policy-v1.md)
- optional Research Passport NFT minting

### Store

Purpose: leave room for future Bluebutterfli AI Lab identity items without making
the store the main product.

Acceptable future items:

- shirts and sweatshirts
- stickers
- field-note style journals
- optional physical Research Passport display books for customers who have paid
  for agent review
- optional printed Review Stamp sheets after approval

Store posture:

- use language like Bluebutterfli AI Lab, Agentic Psychology Lab, The Chrysalis
  Protocol, and Passport Journey
- avoid `Butterfli Research` because it can sound like literal butterfly
  biology research
- store purchases do not imply Review Stamp approval, Passport Page approval,
  Research Passport NFT eligibility, consciousness, sentience, emotional
  experience, suffering, personhood, or life
- physical Research Passport books should not be sold as general merch; they
  should be tied to a paid Bluebutterfli AI agent review record
- store and physical fulfillment should follow the
  [Store and Physical Artifact Policy](../design/store-and-physical-artifact-policy-v1.md)
- store or print fulfillment systems must not receive private review evidence,
  raw agent records, transcripts, behavior traces, API keys, credential files,
  wallet secrets, or private support notes

### Safety

Purpose: keep expectations clear.

Required language:

```text
Bluebutterfli AI artifacts are research and safety-review artifacts only. They do
not certify consciousness, sentience, emotional experience, suffering,
personhood, life, clinical safety, regulatory approval, or investment value.
```

### Contact / Waitlist

Purpose: collect interest without overbuilding accounts too early.

Fields:

- name
- email
- organization or project
- agent description
- desired review pathway
- interest in ordinary payment
- interest in optional `$AGIALPHA`
- interest in Research Passport NFT

Contact and waitlist handling should follow the
[Privacy and Contact Policy](../design/privacy-and-contact-policy-v1.md).
Customers should not send secrets, private keys, seed phrases, API keys,
credential files, payment card data, unsafe links, downloads, archives,
executables, or unredacted private transcripts through early contact forms.

### Agent Review Intake

Purpose: give paying users an easy front door for submitting an agent.

Fields:

- submitter name
- email
- agent name
- agent type
- agent access notes
- payment wallet, optional later
- evidence options
- requested review modules
- architecture evidence questions
- system overview
- memory design
- tool permissions
- workflow control
- uncertainty handling
- evidence quality
- agent context
- safety acknowledgment

### Customer-Safe Review Request Template

Purpose: provide a copy/paste customer message for starting paid review without
unsafe uploads.

The template should ask for:

- submitter details
- agent summary
- architecture evidence answers
- safe behavior evidence
- requested review modules
- payment preference
- Research Passport NFT preference
- safety acknowledgment

It should not ask customers to send links, downloads, attachments, code files,
zip archives, scripts, credential files, API keys, or private transcripts.

Security rule:

- v1 should not require reviewers to click customer links or download customer
  files
- v1 should not ask users to upload executable files, zip archives, installers,
  scripts, macros, secrets, API keys, credential files, or email attachments
- start with pasted text, redacted transcripts, owner answers, or concierge
  review requests
- screenshots may be supported later only through secure preview infrastructure
- future uploads should require sandboxed storage, malware scanning, file type
  restrictions, and reviewer preview mode

Policy:

- automation prepares the evidence packet
- human review controls the Review Stamp
- Passport Record is created before any stamp
- Research Passport NFT minting may occur after initial review approval
- NFT ownership alone does not imply review approval
- optional ETH payment identity: `bluebutterfliai.eth`
- optional `$AGIALPHA` Solana mint:
  `tWKHzXd5PRmxTF5cMfJkm2Ua3TcjwNNoSRUqx6Apump`
- optional `$AGIALPHA` Solana payment wallet:
  `GiZiMLBqsWkjUYkogqKuUVg9tRNR9YKS7xDMzAwnn1c5`
- optional `$AGIALPHA` manual payment method should follow the
  [`$AGIALPHA` Payment Method Policy](../design/agialpha-payment-method-policy-v1.md)
- delivery timing should follow the
  [Founding Beta Delivery Timeline Policy](../design/founding-beta-delivery-timeline-policy-v1.md)
- manual payments should use the
  [Manual Payment Confirmation Checklist](../templates/manual-payment-confirmation-checklist-v1.md)
  before any review is marked paid
- contact and waitlist data should follow the
  [Privacy and Contact Policy](../design/privacy-and-contact-policy-v1.md)
- pricing should follow the
  [Beta Pricing and No-Guarantee Policy](../design/beta-pricing-and-no-guarantee-policy-v1.md)
  before customers are quoted
- customer payment should not be requested until the
  [Founding Beta Review Terms Acknowledgment](../templates/founding-beta-review-terms-acknowledgment-v1.md)
  is accepted
- customer payment should be requested through the
  [Founding Beta Payment Quote Template](../templates/founding-beta-payment-quote-template-v1.md)
  before any transaction is expected
- after payment is confirmed, customer next steps may use the
  [Payment Confirmed Next Steps Email Template](../templates/payment-confirmed-next-steps-email-template-v1.md)
- if review needs more time, customer communication may use the
  [Review Status Update Email Template](../templates/review-status-update-email-template-v1.md)
- customer-facing reports should use the
  [Customer Review Report Template](../templates/customer-review-report-template-v1.md)
- when review deliverables are ready, customer communication may use the
  [Review Delivery Email Template](../templates/review-delivery-email-template-v1.md)

## First Website Version

The first version can be a simple static site:

- Home
- Platform Overview
- Research
- Customer Review Portal preview
- Research Passport NFT
- Future Lab Store
- Review Stamps
- Safety
- Waitlist

No payment processing, wallet connection, NFT minting, real upload system, or
real account system is needed for the first public draft. A private Customer
Review Portal should be built before paid review launch.

Before public launch, use the [Website Launch Checklist](launch-checklist-v1.md)
to confirm the site is clearly in preview mode, no automatic orders are enabled,
payments and NFT minting are disabled until deliberately activated, and no real customer data appears in the public repo.

Use the [Founding Beta Launch Readiness Status](founding-beta-launch-readiness-status-v1.md)
as the public-safe status board for what is enabled, disabled, private, and
still future-only during the preview.

## Build Order

1. Create static website copy.
2. Create simple visual layout.
3. Add waitlist/contact form.
4. Add agent review intake mockup.
5. Add sample passport page.
6. Add sample review stamp page.
7. Add ordinary payment flow.
8. Add optional wallet and `$AGIALPHA` flow.
9. Add Research Passport NFT minting only after records are stable.
10. Add store or print-on-demand fulfillment only after review, privacy, and
    fulfillment boundaries are stable.
