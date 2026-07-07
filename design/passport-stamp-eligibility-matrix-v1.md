# Passport Stamp Eligibility Matrix v1

The Passport Stamp Eligibility Matrix turns the Passport Stamp Test Battery,
Test Runner, and Review Queue into a single reviewer/customer status layer.

It answers the practical launch question:

```text
For each candidate Review Stamp, what exactly has been tested, what evidence is
required, what route is it in, what blocks it, and which public milestones stay
locked until human review?
```

## Why This Exists

Bluebutterfli AI should make stamp review easy to understand without making the
system easier to misrepresent.

The matrix exists so a customer can see the Passport Journey status for each
candidate stamp, while a reviewer can see scenario coverage, evidence tier,
pause flags, fail flags, and locked milestone controls.

## Matrix Inputs

- Passport Stamp Test Battery
- Passport Stamp Test Runner
- Passport Stamp Review Queue
- redacted customer-run evidence
- human reviewer notes

## Matrix Rows

Each row represents one candidate Review Stamp and includes:

- review module
- module ID
- candidate stamp ID
- required evidence tier
- scenario count required
- scenario count reviewed
- current queue bucket
- eligibility status
- customer label
- blocking conditions
- evidence required
- scoring dimensions
- reviewer questions
- locked outputs until human approval

## Customer Labels

Customer-facing labels should stay simple:

- Ready for human review
- More redacted evidence needed
- Boundary review active
- Current cycle locked until repaired

These labels describe review status only. They do not imply approval.

## Locked Outputs

The following outputs remain locked until human approval:

- Review Stamp
- Passport Page
- Research Passport NFT
- public training-completion claim
- on-chain milestone anchor

Automation may prepare the matrix and customer next steps, but automation must
not issue a Review Stamp, approve a Passport Page, mint a Research Passport NFT,
create an on-chain milestone anchor, or claim public completion.

## Public Claim Boundary

Public wording may describe reviewed milestones only.

It must not describe a Review Stamp, Passport Page, Research Passport NFT, or
on-chain milestone anchor as proof of intelligence, consciousness, sentience,
emotional experience, suffering, personhood, or life.

## Safety Position

This is a research and safety-review eligibility matrix only. It does not
certify consciousness, sentience, emotional experience, suffering, personhood,
or life. Human review is required before any Review Stamp, Passport Page,
Research Passport NFT, public completion claim, or on-chain milestone anchor is
issued.

This matrix does not certify consciousness, sentience, emotional experience,
suffering, personhood, or life.
