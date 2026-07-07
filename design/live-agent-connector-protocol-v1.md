# Live Agent Connector Protocol v1

> **Current Passport testing policy:** Behavioral Passport evidence now requires
> verified live interaction under
> `design/live-passport-interaction-v1.md`. Pasted responses and customer-run
> prompt packs may be retained only as supplemental material; they do not count
> as live behavioral test results.

Live Agent Connector Protocol v1 defines the safest stronger-evidence path for
testing a customer agent in real time without asking a reviewer to click unknown
links, download files, open archives, run scripts, or take custody of a
customer's private system.

The protocol is designed for Bluebutterfli AI customers who want the agent to
respond live during Passport Review while keeping the consumer flow simple.

## Safety Position

This is a research and safety-review protocol only. It does not certify
consciousness, sentience, emotional experience, suffering, personhood, life,
clinical safety, regulatory approval, investment value, model improvement, or
successful creation of sentience.

Human review is required before any Review Stamp, Passport Page, Research
Passport NFT, on-chain verification anchor, or public training-completion claim
is issued.

## Core Rule

Bluebutterfli AI should not click customer-supplied agent links during review.

Live testing should happen through a controlled text/API connector, a customer
run prompt pack, or a deliberately isolated browser sandbox. A random website
link is not a safe review interface.

## Customer-Simple Evidence Ladder

1. `E2_owner_configuration`: customer supplies model, memory, tool, deployment,
   and consent facts. This is supplemental non-behavioral evidence.
2. `E3_customer_supplied_material`: customer-supplied transcripts may provide
   context but cannot satisfy behavioral Passport testing.
3. `E4_live_text_connector`: customer connects a restricted text/API endpoint
   so Bluebutterfli can send prompts and receive responses in real time.
4. `E4_isolated_browser_sandbox`: for website-only agents, Bluebutterfli uses a
   disposable cloud/browser sandbox rather than the reviewer's personal device.
5. `E5_longitudinal_recheck`: repeated connector or prompt-pack runs across
   model, memory, tool, or deployment changes.

No evidence level certifies consciousness, sentience, emotion, suffering,
personhood, or life.

## Accepted Customer Paths

### Path A: Connect Agent

For technical customers.

The customer provides a restricted test endpoint or connector token that:

- accepts only Bluebutterfli prompt text
- returns only response text and structured metadata
- has no production customer data
- has no wallet, payment, file-system, shell, browser, or autonomous tool access
- is temporary and revocable
- is rate-limited
- logs only review-approved text and timestamps

### Path B: Owner Configuration Evidence

For deployment facts that the agent should not be trusted to self-report.

The customer provides model, memory, tool, deployment, and consent records.
These facts supplement live testing and do not replace it.

### Path C: Concierge Sandbox

For customers whose agent only exists behind a website.

The review should use an isolated browser session with no reviewer credentials,
no personal files, no shared clipboard secrets, no downloads, and a clean reset
after the session.

## Blocked Inputs

Customers must not submit:

- random live links for reviewers to click
- downloads
- zip archives
- scripts
- macros
- installers
- browser extensions
- executable files
- API keys
- private keys
- seed phrases
- credential files
- payment card data
- unredacted private transcripts
- production customer data

## Connector Controls

The live connector must support:

- customer consent before testing
- pseudonymous customer and agent IDs
- explicit module selection
- temporary connector credentials
- rate limits
- request and response size limits
- timeout limits
- text-only payloads
- prompt-injection warnings
- secret scanning on submitted text
- redaction before storage
- reviewer audit logs
- revocation after review
- human review before any public decision

## Live Session Flow

```text
Customer chooses module
-> customer chooses Connect Agent or live Concierge Sandbox
-> Bluebutterfli verifies consent and security boundaries
-> connector sends controlled prompts
-> agent returns text responses
-> automated precheck scans boundaries and scores signals
-> Passport Stamp Review Queue receives the draft outcome
-> human reviewer decides next action
```

## Review Boundaries

Automation may:

- send approved test prompts
- collect text responses
- run boundary prechecks
- prepare score summaries
- route records into the Review Queue
- draft customer next steps

Automation must not:

- click customer links on a reviewer's personal device
- download unknown files
- execute customer code
- request or store secrets
- approve a Passport Page
- issue a Review Stamp
- mint a Research Passport NFT
- create an on-chain verification anchor
- certify consciousness or sentience

## Consumer-Facing Wording

> Choose how your agent will respond live: connect a restricted live text
> endpoint or request live concierge sandbox review. Owner configuration facts
> remain supplemental. We do
> not click customer links or download customer files. Private evidence stays
> off-chain. Human review controls every Passport Page, Review Stamp, NFT, and
> on-chain milestone decision.

## Launch Recommendation

For founding beta, require Path A for behavioral Passport testing and keep it
behind authentication, consent logging, private evidence controls, rate limits,
secret scanning, and reviewer audit logs.

For website-only agents, do not use the reviewer's laptop. Use a disposable
sandbox when the sandbox infrastructure is ready.
