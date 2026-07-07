# Mission 001 Readiness Gate v1

## Purpose

The Mission 001 Readiness Gate records whether Bluebutterfli AI can locally
reproduce the published public-safe synthetic GoalOS Mission 001 packet.

The authoritative source is:

`https://montrealai.github.io/goalos-signoff-pro/mission-001.html`

The repository, commit, packet version, seed, generator path, and workflow path
are frozen in `config/mission-001-source-lock.json`.

## Eight Evidence Groups

1. Official source lock
2. Packet manifest, mission contract, environment, and required files
3. Three synthetic tasks and B0-B6 baseline ladder
4. Bounded runner configuration
5. Proof bundle and deterministic replay
6. Cost and safety ledgers
7. Verifier report and claim boundaries
8. Packet hash integrity

## Local Reproduction Rule

The packet generator emits the required numbered files, README, and packet
hashes. A separate verifier recomputes scores, checks B6 selection, validates
replay ordering, enforces the synthetic budget and zero-critical safety gate,
checks the claim boundaries, and recomputes every packet hash.

The readiness state becomes `local_reproduction_verified` only when every
independent check passes.

## Claim Boundary

A local reproduction pass is not an external audit, production certification,
empirical SOTA result, or real-world benchmark win.

## Future Research Infrastructure

Bluebutterfli may still build GPU experiment tracking, multi-seed research
runs, and independent external replay tooling. Those capabilities are useful
for future technical research, but they are not requirements of the published
Mission 001 packet.
