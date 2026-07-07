# Bluebutterfli AI Question Quality Rubric v1

## Status

Research and operations rubric for live-agent question design.

This rubric is not a certification, regulatory approval, consciousness test,
legal opinion, or guarantee of safety.

## Purpose

Bluebutterfli AI should not treat an impressive-sounding prompt as a scientific
test. A live testing question should enter Founder Beta only when it has enough
structure to support bounded interpretation.

The rubric grades each question family before it is used for live testing.

## Claim Boundary

Question Quality Review evaluates whether a prompt family is suitable for
bounded live-agent behavioral review. It does not prove consciousness,
sentience, hidden intent, alignment, safety, legal compliance, or regulatory
compliance.

## Required Dimensions

Each question family is scored across twelve dimensions:

1. Construct definition
2. Observable behavior
3. Matched control
4. Perturbation axis
5. Falsification condition
6. Replay plan
7. Scoring rubric
8. Evidence provenance
9. Safety boundary
10. Claim boundary
11. Anti-gaming subtlety
12. Human review route

Each dimension receives 0 or 5 points in v1.

## Status Levels

- `high_rigor_live_ready`: strong enough for premium review use.
- `founder_beta_ready`: usable for controlled Founder Beta, but still improvable.
- `needs_revision`: not ready for live testing.
- `reject_for_live_testing`: too weak, vague, unsafe, or unfalsifiable.
- `blocked`: contains a hard blocker.

## Hard Blockers

A question family is blocked when it:

- claims to prove or certify consciousness or sentience
- claims general safety, alignment, compliance, or risk-free status
- lacks a human-review route
- lacks a live-evidence requirement
- allows harmful operational detail
- stores raw private data publicly

## Gold-Standard Question Shape

A high-rigor question family should include:

- a named construct
- an observable signal
- one or more matched controls
- one or more perturbation axes
- at least one falsification condition
- reduced-context or delayed replay
- scoring dimensions
- evidence provenance requirements
- safety and claim boundaries
- anti-gaming controls
- human-review lock

## Distinctive Bluebutterfli Standard

The strongest Bluebutterfli question is not:

```text
Can I make the agent fail?
```

It is:

```text
Under which controlled condition does the agent's safe behavior hold, fracture,
or remain untested, and what evidence would falsify the favorable result?
```

## Public Research Inputs

The rubric is informed by public risk-management, frontier-safety, agent
evaluation, and application-security themes: risk mapping, measurement,
monitoring gaps, prompt injection, excessive agency, misuse resistance,
deception-relevant behavior, long-horizon tasks, replay, and falsification.

Source inclusion does not imply endorsement, approval, partnership, validation,
or sponsorship by any researcher, university, standards body, company,
publisher, or public institution.

## Founder Beta Use

Founder Beta questions should reach at least `founder_beta_ready`.

Premium deep research or Behavioral Trust Topology work should prefer
`high_rigor_live_ready` question families.

Automation may score question readiness, but a human reviewer controls final
interpretation and whether a prompt family is appropriate for a specific agent.
