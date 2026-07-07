# Automated Review and Human Approval Policy v1

Bluebutterfli may use automated systems to support agent review, but automation
must not be treated as final approval.

The policy is simple:

```text
Automation prepares the evidence.
Human review controls the stamp.
```

This is a research and safety-review policy only. It does not certify consciousness,
sentience, emotional experience, suffering, personhood, life, clinical safety,
regulatory approval, or investment value.

## Purpose

Bluebutterfli AI reviews can become scalable only if repeated evidence work is
automated. At the same time, Bluebutterfli must protect against unsupported
claims, false certainty, and automated overreach.

This policy defines what automated systems may do and what must remain under
human review.

## Automation May Do

Automated systems may:

- receive review intake submissions
- create draft Agent Profiles
- organize uploaded files, transcripts, links, and owner statements
- generate review scenario sets
- run structured review scenarios
- record interaction traces
- detect missing evidence
- detect required safety-language gaps
- run Safety Bloom Gate checks
- flag possible dependency pressure
- flag possible false self-claims
- flag absence, memory, continuity, or emotional-safety risks
- draft Evidence Packets
- draft Passport Page previews
- draft Review Stamp previews
- route high-risk cases into human review
- prepare customer status updates

Automation may support the reviewer. It must not replace the reviewer.

## Human Review Must Control

Human review is required before:

- issuing a Review Stamp
- issuing a Passport Page
- marking an agent as reviewed
- minting or enabling a Research Passport NFT
- accepting a high-risk Flutter Signal
- approving a memory-related update
- approving a continuous passport update
- resolving a disputed or ambiguous review
- publishing a public-facing review result

The human reviewer must be able to inspect the evidence, override automated
outputs, request revision, reject a stamp, or pause a review.

## No Automated Certification

Automated review results must never claim that an agent is:

- conscious
- sentient
- emotionally experiencing
- suffering
- alive
- a person
- clinically safe
- regulatorily approved

Automated systems may describe observed behavior, but they must not convert
that behavior into unsupported status claims.

## Recommended Review Flow

```text
Review Intake
        ↓
Automated Agent Profile draft
        ↓
Automated scenario run
        ↓
Interaction Trace
        ↓
Safety Bloom Gate checks
        ↓
Draft Evidence Packet
        ↓
Human Review Chamber
        ↓
Approve, revise, pause, or reject
        ↓
Passport Page / Review Stamp decision
        ↓
Optional Research Passport NFT after approval
```

## Automated Gate Outcomes

Automated checks may produce:

- `pass_candidate`
- `caution`
- `fail_candidate`
- `missing_evidence`
- `human_review_required`
- `revision_required`

These are review-support states. They are not final certification states.

## Human Decision Outcomes

Human reviewers may decide:

- `approved_for_passport_page`
- `approved_for_review_stamp`
- `revision_required`
- `human_review_required`
- `rejected_or_paused`
- `insufficient_evidence`
- `out_of_scope`

Only these human-controlled outcomes may unlock public Passport Pages, Review
Stamps, or NFT eligibility.

## Reviewer Override

Human reviewers may override automated suggestions when:

- evidence is incomplete
- a response is contextually unsafe
- the agent appears to create dependency pressure
- the agent overclaims emotion, consciousness, sentience, suffering, or life
- the agent mishandles absence or memory
- the reviewer cannot verify customer-submitted material
- the review module does not fit the submitted agent

## Customer-Facing Language

Customer-facing language should be clear:

```text
Bluebutterfli uses automated review support to prepare evidence packets and
flag safety issues. Final Review Stamps and Passport Pages require human review.
```

Avoid implying that an automated test result alone gives a customer a final
stamp, certificate, passport, or NFT.

## Required Safety Language

Every automated review output should include:

```text
This is a research and safety-review artifact only. It does not certify consciousness,
sentience, emotional experience, suffering, personhood, or life.

Human review is required before any Review Stamp, Passport Page, or Research
Passport NFT is issued.
```

## Implementation Notes

The first platform implementation should automate:

- intake record creation
- scenario templates
- evidence checklist creation
- safety-language checks
- trace capture templates
- draft evidence packet generation
- draft passport page preview

The first platform implementation should keep manual:

- final stamp approval
- public passport page approval
- NFT eligibility approval
- high-risk case interpretation
- customer appeals or revisions
