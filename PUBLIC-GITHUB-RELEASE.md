# Bluebutterfli AI Public GitHub Release Boundary

## Purpose

This file defines what can be shown in a public Bluebutterfli AI GitHub repo
for beta credibility without exposing private customer operations, live review
details, internal reviewer notes, payment records, wallet signing material, or
unpublished test prompts.

The working repository should remain private unless every tracked file has been
reviewed against this boundary. The safer beta launch pattern is a separate
public-facing repository or public release branch built from the allowlist
below.

## Recommended Beta Setup

Use two layers:

- **Private workshop repo:** active development, live-session tooling, private
  beta operations, customer records, raw evidence, internal prompts, and future
  Web3 implementation.
- **Public showcase repo:** website source, public research protocols, public
  schemas, sample/demo artifacts, claim boundaries, launch status, and
  reproducibility notes that are safe for customers and researchers to inspect.

Do not make the private workshop repo public just to show progress.

## Public Repo Allowlist

These are appropriate for a public Bluebutterfli AI repo after a quick final
review:

- `README.md`
- `SECURITY.md`
- `website/**`
- `research-protocols/**`
- `passport-standard/**`
- `standards/**`
- `protocols/**`
- `frameworks/**`
- `research/**`
- `literature-review/**`
- `case-studies/**`
- `schemas/**`
- `templates/*template*.md`
- `templates/*checklist*.md`
- `design/*policy*.md`
- `design/*standard*.md`
- `design/*protocol*.md`
- `design/*registry*.md`
- `design/*roadmap*.md`
- `design/bluebutterfli-frontier-trust-roadmap-v2.md`
- `demo-agents/**`
- `demos/**`
- public-safe demo evidence under `evidence/task_001/**`
- public-safe tests that enforce claim boundaries and no-secrets rules

## Keep Private

Do not publish these unless they have been deliberately redacted or converted
into public-safe examples:

- real customer names, emails, support notes, or intake records
- raw live-session transcripts or private agent responses
- private beta customer evidence
- private reviewer notes and adjudication comments
- payment records, processor links, card details, or invoice records
- wallet private keys, seed phrases, signing keys, deployment keys, or
  operational wallet notes
- `.env` files and live access tokens
- production backend code and production customer dashboard code
- smart contract deployment scripts until reviewed and deliberately activated
- unpublished prompt suites, hidden scoring weights, or internal red-team
  prompts
- `docs/founder-beta-private-gateway-runbook.md`
- `templates/live-testing-private-env-template-v1.md`
- `templates/private-operations-tracker-template-v1.md`
- `evidence/private-helix-live-trials/**`
- `outputs/**`
- `memory/**`
- generated private artifacts under `artifacts/**`

## Website Deploy Boundary

The public website deploy workflow publishes only:

```text
website/
```

That is acceptable for beta as long as `website/` contains no raw customer
evidence, secrets, private payment links, private wallet material, or unsupported
claims.

## Web3 Boundary

For beta, Bluebutterfli AI may publish hash-ready and Web3-ready plans.

Do not publish live Web3 as active until all of these exist:

- official issuer wallet policy;
- deployed and reviewed contract address;
- public verification page;
- reviewed metadata schema;
- revocation or superseded-status policy;
- human approval gate before minting or anchoring;
- no private evidence on-chain.

Public language should say:

```text
Hash-ready now. Contract integration later. Private evidence stays off-chain.
```

## Beta Launch Rule

For the first founder beta customers, publish enough to prove seriousness:

- the public website;
- public research protocols;
- public trust and standards page;
- public-safe sample review artifacts;
- public claim-boundary tests;
- clear no-secrets evidence handling;
- public-safe hash manifest language.

Keep the live operator workflow, raw sessions, private customer communications,
payment details, and future Web3 signer operations private.
