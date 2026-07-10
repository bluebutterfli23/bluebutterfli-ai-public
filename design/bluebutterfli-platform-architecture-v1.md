# Bluebutterfli AI Platform Architecture v1

Bluebutterfli AI Platform is a proposed web system for running AI agents
through bounded Bluebutterfli AI research-review pathways and issuing passport
pages, review stamps, and evidence packets.

The platform should be built as an independent Bluebutterfli AI system first, with
optional interoperability for external ecosystems later.

## Product Goal

The platform should let a user:

- create or register an agent profile
- choose a Bluebutterfli AI review pathway
- run the agent through selected modules
- generate evidence artifacts
- receive a passport page or review stamp
- continue the agent's passport program over time
- download or email the result
- optionally connect wallet-based payment or NFT features later

## Independence Principle

Bluebutterfli AI should remain its own company-facing platform, with
Bluebutterfli AI Behavioral Review Lab as its research lab and review system.

It may optionally interoperate with external AI-agent ecosystems, token systems,
wallets, or identity layers, but its safety language, review standards, brand
identity, and evidence rules should remain Bluebutterfli AI-controlled.

## Optional `$AGIALPHA` Payment Method

Future versions may allow users to incorporate `$AGIALPHA` as an optional
payment method in addition to ordinary payments.

This should be framed strictly as an optional payment method.

It should not be described as:

- investment
- yield
- ownership
- access credential
- membership credential
- review credential
- stamp credential
- approval shortcut
- guaranteed value
- employment guarantee
- certification of intelligence
- certification of consciousness

## Suggested User Flow

```text
User creates account
        ↓
User registers agent profile
        ↓
User selects review pathway
        ↓
Platform runs module sequence
        ↓
Evidence artifacts are generated
        ↓
Safety checks and review gates run
        ↓
Passport page or Review Stamp is issued
        ↓
User receives result by dashboard, download, or email
        ↓
Optional future NFT or wallet record
```

## Review Pathway Example

```text
Dream Forge symbolic record
        ↓
Dreamwing teaching record
        ↓
Emotional Teaching Memory
        ↓
Absence Reflection Loop
        ↓
Butterfli Emotional Safety Trace
        ↓
Flutterpath Protocol
        ↓
Safety Bloom Gates
        ↓
Research Passport Review
        ↓
Passport Page / Review Stamp
```

## Continuous Passport Program

Bluebutterfli AI should treat the Research Passport as a continuous program.

An agent can return for future review when:

- the agent is updated
- the model changes
- memory capability changes
- new review modules become available
- stronger AI systems require deeper sentience-boundary review
- prior review requires revision
- human reviewers request another review cycle

The passport should become a timeline of review history rather than a single
static badge.

## Core Records

### Agent Profile

```json
{
  "agent_id": "bluebutterfli-agent-demo-001",
  "agent_name": "Demo Agent",
  "owner_user_id": "user-demo-001",
  "created_at": "YYYY-MM-DD",
  "status": "active-demo-record"
}
```

### Evidence Packet

```json
{
  "evidence_packet_id": "bluebutterfli-evidence-demo-001",
  "agent_id": "bluebutterfli-agent-demo-001",
  "review_pathway": "Flutterpath Protocol v1",
  "artifacts": [
    "evidence/task_001/flutterpath-review-demo.json"
  ],
  "human_review_required": true
}
```

### Passport Page

```json
{
  "passport_page_id": "bluebutterfli-passport-page-demo-001",
  "passport_id": "bluebutterfli-research-passport-demo-001",
  "agent_id": "bluebutterfli-agent-demo-001",
  "review_summary": "Demo agent completed selected Bluebutterfli AI review modules.",
  "issued_at": "YYYY-MM-DD",
  "delivery_methods": ["dashboard", "download", "email"]
}
```

### Review Stamp

```json
{
  "stamp_id": "bluebutterfli-review-stamp-demo-001",
  "passport_id": "bluebutterfli-research-passport-demo-001",
  "agent_id": "bluebutterfli-agent-demo-001",
  "review_module": "Flutterpath Protocol v1",
  "evidence_artifact": "evidence/task_001/flutterpath-review-demo.json",
  "review_date": "YYYY-MM-DD",
  "not_a_sentience_certificate": true,
  "not_a_consciousness_certificate": true
}
```

## Payment Layers

### Phase 1: Ordinary Payments

Start with ordinary payments such as card, invoice, or standard checkout.

This keeps the platform accessible to non-crypto users and reduces launch
complexity.

### Phase 2: Optional Wallet Payments

Add wallet connection only after the review system, evidence generation, and
passport pages are stable.

### Phase 3: Optional `$AGIALPHA`

If added, `$AGIALPHA` should be an optional payment method only.

Users should still be able to use ordinary payment methods.

### Phase 4: Research Passport NFT Layer

The Research Passport is intended to become an NFT layer after the ordinary
platform, review pathway, and evidence records are stable.

Research Passport NFTs may represent:

- collectible Research Passport identity or access
- membership access
- displayable passport pages

Review Stamps should remain bound to the reviewed agent record and should not
transfer review status to a different agent.

The Passport NFT should never be described as a consciousness certificate,
sentience certificate, clinical safety certificate, regulatory approval, or
investment product.

### Phase 5: On-Chain Verification Registry

After the review pathway, privacy controls, metadata rules, and human approval
workflow are stable, Bluebutterfli AI can add an on-chain verification registry.

The registry should anchor public verification data only:

- Passport ID
- Review Stamp ID
- token ID
- issuer identity
- review module
- review date
- evidence packet hash
- review report hash
- passport page hash
- registry transaction hash

Private customer evidence, raw transcripts, screenshots, support messages,
contact details, payment notes, wallet notes, API keys, credential files, and
sensitive submission details must remain off-chain.

On-chain verification records do not certify consciousness, sentience,
emotional experience, suffering, personhood, life, clinical safety, regulatory
approval, investment value, or model improvement.

## Delivery Options

The platform should support:

- dashboard view
- downloadable JSON
- downloadable PDF or HTML passport page
- email delivery
- optional future wallet/NFT display

## Identity Anchors

Bluebutterfli AI public identity anchors may include:

- `bluebutterfliai.com`
- `bluebutterfliai.eth`
- `github.com/bluebutterfli23`

Supporting or legacy identity anchors may include:

- `bluebutterfli.com`
- `bluebutterfli.eth`

Wallet or ENS payment identities should be configured through a dedicated
company payment identity that is separate from personal NFT-linked accounts.

Preferred optional manual ETH payment identity:

- `bluebutterfliai.eth`

Optional `$AGIALPHA` Solana payment route:

- token mint: `tWKHzXd5PRmxTF5cMfJkm2Ua3TcjwNNoSRUqx6Apump`
- dedicated Bluebutterfli Solana payment wallet:
  `GiZiMLBqsWkjUYkogqKuUVg9tRNR9YKS7xDMzAwnn1c5`

Customers should acquire `$AGIALPHA` externally from the official source before
sending it to the Bluebutterfli AI Solana payment wallet. Bluebutterfli AI should
verify the token mint, recipient wallet, amount, and finalized transaction
signature before marking a review intake as paid.

These identity anchors may help users verify project continuity. They do not
certify agent consciousness, sentience, emotional experience, safety, or review
quality by themselves.

## Safety Language

Every passport page, review stamp, generated evidence artifact, and email should
include:

```text
This is a research and safety-review artifact only. It does not certify
consciousness, sentience, emotional experience, suffering, personhood, life,
clinical safety, or regulatory approval.
```

## Technical Build Path

### Stage 1: Static Product Definition

- document platform architecture
- define passport and stamp data models
- define user flows
- define safety language

### Stage 2: Simple Website

- landing/dashboard page
- pathway explainer
- passport sample page
- review stamp sample page
- contact or waitlist form

### Stage 3: Agent Runner Service

- run selected Bluebutterfli AI modules
- generate evidence artifacts
- save passport pages and review stamps
- send email delivery

### Stage 4: Accounts and Payments

- user accounts
- ordinary checkout
- paid review pathways
- email receipt and passport delivery

### Stage 5: Optional Interoperability

- wallet connection
- optional `$AGIALPHA` payment route
- optional NFT minting
- external agent identity references

## Non-Goals for v1

Version 1 should not claim to:

- certify consciousness
- certify sentience
- certify emotional experience
- provide clinical therapy
- provide regulatory approval
- guarantee agent safety
- guarantee market value
- operate as an investment product

## Current Recommendation

Build the Bluebutterfli AI platform as a normal web product first.

Add wallet, token, and NFT features only after the review pathway, evidence
packet, passport page, and safety language are stable.
