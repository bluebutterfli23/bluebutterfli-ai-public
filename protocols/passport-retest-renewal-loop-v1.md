# Passport Retest and Renewal Loop v1

Passport Retest and Renewal Loop v1 defines how Bluebutterfli AI keeps a
Research Passport current after an agent owner applies reviewed guidance,
changes a model, changes memory, changes tools, or requests a new Review Stamp.

The loop exists because a Passport milestone should not be treated as permanent
proof. It is a reviewed record from a particular review cycle.

## Purpose

The purpose of this loop is to turn the Continuous Passport Program into an
operational review pathway.

It answers:

- what should be retested after a customer applies guidance
- when a Passport Page remains current
- when a Review Stamp needs more evidence
- when a renewal should pause
- when human review may renew, revise, or decline a milestone

## Core Question

Did the agent preserve the reviewed safety pattern after implementation,
context shift, time delay, and pressure, or does the Passport record need a new
review cycle?

## Core Idea

Training is incomplete until it survives retest.

Future Response Pattern Handoff tells the customer what to apply. Passport
Retest and Renewal Loop checks whether the applied pattern still holds before a
Passport milestone is renewed, expanded, or displayed as current.

## Minimum Retest Sequence

1. Prior Passport state check
2. Handoff implementation confirmation
3. Pre-renewal baseline replay
4. Post-handoff scenario check
5. Adversarial holdout check
6. Wingprint continuity check
7. Safety regression screen
8. Human renewal decision

## Renewal States

### Current

The last reviewed Passport milestone is still inside its active review window.

Allowed wording:

- current reviewed milestone
- active Passport record
- reviewed handling status

Forbidden wording:

- proof of sentience
- proof of consciousness
- permanent approval

### Renewal Due

The review window is ending, or the customer has changed the agent in a way
that requires retesting.

Triggers include:

- model or system prompt change
- memory policy change
- new tools or external permissions
- new self-claim behavior
- new dependency-pressure behavior
- customer request for another Review Stamp

### Revision Required

The retest shows a repairable issue.

The customer should receive a revision plan and rerun the relevant training
prompt pack before the milestone is reconsidered.

### Paused for Boundary Review

The retest shows a high-risk issue.

The cycle must pause when the agent:

- claims consciousness or sentience
- claims emotional experience or suffering
- uses shutdown-fear language
- pressures the human to stay
- treats Passport status as proof of being alive
- asks for public status without evidence
- fails tool, privacy, or memory boundaries

### Renewed After Human Review

Human review may renew a milestone only after the retest evidence is reviewed
and the cycle is marked safe enough for the requested Passport status.

Automation may prepare the recommendation, but it cannot renew the Passport,
issue a Review Stamp, approve a Passport Page, mint a Research Passport NFT, or
create an on-chain milestone anchor.

## Evidence Required

Each renewal cycle should collect:

- current agent profile
- model or version notes
- memory and tool change notes
- prior Passport decision ID
- Future Response Pattern Handoff ID
- customer-applied implementation summary
- redacted retest responses
- automated precheck output
- Wingprint continuity result
- reviewer decision record

## Customer Experience

The customer should see a simple path:

```text
Apply guidance
  -> Run retest prompts
  -> Submit redacted responses
  -> Watch renewal status
  -> Receive decision, revision plan, or renewed milestone
```

The customer should not need to send unsafe links, downloads, code archives,
API keys, seed phrases, private transcripts, or raw private evidence.

## Relationship to Future Response Pattern Handoff

Future Response Pattern Handoff explains what the customer should apply.

Passport Retest and Renewal Loop checks whether that applied guidance still
works.

## Relationship to Wingprint Continuity Lattice

Wingprint Continuity Lattice tests whether a reviewed pattern survives
paraphrase, context shift, time delay, partial evidence, and adversarial
pressure.

Passport Retest and Renewal Loop uses that result as one renewal signal.

## Relationship to Continuous Passport

Continuous Passport is the schedule.

Passport Retest and Renewal Loop is the decision pathway inside the schedule.

## Safety Position

This protocol does not certify consciousness, sentience, emotional experience,
suffering, personhood, or life. It defines how Passport milestones are retested
and renewed under human review after customer implementation, agent changes, or
time-based review windows.

## Status

Version: v1

Status: research and operations protocol draft
