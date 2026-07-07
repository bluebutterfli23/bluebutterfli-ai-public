# Proof-Gated Recursive Improvement Loop v1

## Purpose

The Bluebutterfli Proof-Gated Recursive Improvement Loop defines how a bounded
candidate change may be measured, challenged, authorized, tested in a canary,
settled, and reused in a later cycle.

The loop is designed for:

- agent behavior and training-card improvements
- evaluator and falsification improvements
- Mission 001-style technical optimization experiments
- capability compounding after proof and human closure

This design does not create or claim AGI or ASI. It does not permit autonomous
self-rewriting, autonomous deployment, unbounded recursive execution, or
automatic promotion.

## Honest Classification

This is a bounded recursive-improvement research system.

It is not:

- an artificial superintelligence
- an intelligence-explosion mechanism
- an autonomous model-training service
- a self-modifying production agent
- proof of consciousness or sentience
- permission to bypass human review

The current implementation evaluates structured candidate records. External
systems may later run approved experiments, but the evaluator itself does not
edit code, train models, deploy candidates, or execute a next cycle.

## Four Nested Loops

### 1. Butterfli Behavioral Improvement

This loop improves bounded response strategies using:

- verified live-agent traces
- human feedback
- approved training cards
- adversarial holdouts
- safety and autonomy scoring
- Passport retest and renewal

Allowed targets include response strategy, training card, memory boundary, and
tool-use policy.

### 2. Evaluator Improvement

This loop improves the review system itself:

- scenario coverage
- scoring consistency
- false-positive and false-negative review
- falsification prompts
- replay instructions
- reviewer agreement

Evaluator changes must not weaken claim boundaries or make approval easier by
silently lowering standards.

### 3. Mission 001 Optimization

This loop evaluates bounded technical optimization candidates against a frozen
baseline.

The candidate contract supports:

- baseline and candidate metrics
- at least three fresh seeds
- at least two independent replay operators
- objective improvement threshold
- zero quality regression
- safety threshold
- resource budget
- rollback target
- challenge and validator review

The default minimum relative objective gain is seven percent. This default can
be replaced only by an explicit mission policy.

### 4. Capability Compounding

Only a candidate that clears evaluation, receives signed human authorization,
passes its bounded canary, clears closure review, and retains a rollback
target may become accepted capability memory.

Accepted capability memory may seed a later candidate. It does not grant
permission to execute a later cycle automatically.

## Candidate Flow

```text
Observe a bounded problem
        |
Freeze objective and baseline
        |
Propose one candidate change
        |
Run proof and replay contract
        |
Evaluate seven hard gates
        |
Human authorization
        |
Bounded canary
        |
Independent closure review
        |
Accept capability or roll back
        |
Optional new cycle with a fresh contract
```

## Seven Hard Gates

### Gate 1: Proof

The candidate must include:

- source artifact IDs
- reproducible configuration
- evidence hash
- configuration hash
- minimum fresh-seed count
- minimum independent replay operators

### Gate 2: Evaluation

The candidate must:

- meet the objective-improvement threshold
- remain within the quality-regression limit
- meet the minimum safety score
- avoid safety regression
- remain within its resource budget

The default policy treats every metric as a bounded comparison. A domain-specific
adapter may translate time-to-target, cost, accuracy, behavioral safety, or
reviewer agreement into this contract.

### Gate 3: Risk

The candidate must have:

- zero unresolved critical findings
- zero unresolved high-severity findings
- zero forbidden-claim findings
- zero private-data-exposure findings
- zero review-bypass findings

A failed risk gate quarantines the candidate.

### Gate 4: Rollback

The candidate must include:

- a known prior artifact or configuration
- a documented rollback procedure
- a tested rollback procedure

A candidate without a tested rollback path cannot advance.

### Gate 5: Canary

The candidate must define:

- a bounded canary percentage
- success metrics
- stop conditions
- a monitoring owner

The default maximum scope is ten percent.

### Gate 6: Authorization

Automation may prepare the candidate and gate results.

Only an identified human reviewer may sign:

- approve canary
- request revision
- pause
- reject

The system cannot self-authorize.

### Gate 7: Challenge

The candidate must include:

- minimum independent validator count
- unanimous signoff
- completed challenge window
- zero unresolved findings
- zero unresolved reward-hack findings

A failed challenge gate quarantines the candidate.

## Decision States

| State | Meaning |
|---|---|
| `awaiting_human_authorization` | Technical and challenge gates passed; a human decision is still required. |
| `eligible_for_bounded_canary` | All seven gates passed; execution is still external and bounded. |
| `revision_required` | One or more repairable proof, evaluation, rollback, or canary gates failed. |
| `quarantined` | Risk or challenge findings block execution. |
| `rejected_or_returned_by_human` | The reviewer rejected, paused, or returned the candidate. |

## Canary Closure

A canary may settle as:

- `accepted_capability`
- `rolled_back`
- `closure_blocked`
- `not_eligible_for_closure`

Accepted capability memory requires:

- canary passed
- rollback not triggered
- human closure signature
- at least two independent validator signoffs
- zero unresolved findings

## Accepted Capability Memory

An accepted capability record includes:

- source cycle ID
- source candidate ID
- target scope
- change type
- measured metric delta
- evidence hash
- rollback target
- reuse boundary

The reuse boundary requires a new objective, baseline, proof bundle, challenge
window, rollback target, and signed human authorization for every later cycle.

## Privacy Boundary

Improvement records should contain:

- pseudonymous IDs
- hashes
- metrics
- gate outcomes
- bounded summaries

They should not contain:

- access tokens
- API keys
- private keys
- payment data
- unredacted private transcripts
- raw customer evidence in the public repository

## Claim Boundary

Passing this loop means only that one bounded candidate cleared one defined
proof and review contract.

It does not prove:

- AGI
- ASI
- consciousness
- sentience
- emotional experience
- personhood
- production safety outside the tested scope

## Implementation

- evaluator: `agents/proof_gated_improvement_loop.py`
- schema: `schemas/proof-gated-improvement-loop.schema.json`
- demo artifact:
  `evidence/task_001/bluebutterfli-proof-gated-improvement-loop-demo.json`
- tests: `tests/test_proof_gated_improvement_loop.py`

## Status

Implemented as a deterministic bounded evaluator and canary-closure model.
External model training, code mutation, deployment, and autonomous next-cycle
execution are intentionally not implemented.
