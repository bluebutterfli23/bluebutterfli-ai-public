# Bluebutterfli AI Evidence Integrity Spec v1

Status: Design specification.

Purpose: define how Bluebutterfli review evidence can be organized so public
proof remains useful while private customer evidence stays protected.

## Principle

Public verification anchors on-chain. Private evidence off-chain.

Bluebutterfli may publish public-safe hashes, manifests, timestamps, report
summaries, or registry references. Raw private transcripts, customer files,
internal reviewer notes, credentials, secrets, and sensitive live behavior
must remain off-chain unless a separate public release is explicitly scoped.

## Evidence Packet Fields

- review ID
- agent name and version
- owner or authorized submitter
- review package
- workflow reviewed
- evidence source type
- test module IDs
- prompt family IDs
- redacted excerpt references
- score summary
- failure mode IDs
- reviewer decision
- revision plan hash
- report hash
- passport decision hash
- optional public milestone anchor

## Hash Bundle

A public-safe hash bundle may include:

- evidence packet hash
- review report hash
- revision plan hash
- retest checklist hash
- passport decision hash
- manifest hash

## Reviewer Controls

No hash, anchor, registry artifact, Review Stamp, or Passport Page should be
treated as automatic. Human review controls public status changes.

## Claim Boundary

Evidence integrity does not guarantee a positive result, legal certification,
regulatory approval, guaranteed safety, consciousness, sentience, personhood,
emotion, suffering, or inner experience.
