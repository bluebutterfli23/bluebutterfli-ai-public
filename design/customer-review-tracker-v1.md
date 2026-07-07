# Customer Review Tracker v1

Customer Review Tracker v1 defines the private operations backbone for the
Bluebutterfli Continuous Passport Program.

The tracker answers the practical question:

```text
Which customer agent is due for which review, what evidence is needed, what
testing components have run, and what human decision is still required?
```

This is a private operations tracker, not a public registry. Public artifacts
should use pseudonymous IDs, redacted summaries, and approved safety language.

## Purpose

Bluebutterfli AI needs a simple way to track:

- customer agent records
- Research Passport records
- Review Stamps earned
- review modules requested
- next update dates
- due follow-up messages
- testing components completed
- customer Review Reports delivered
- Bloom Trace follow-up status
- human review decisions

The goal is to make the customer experience easy while preserving strong
research boundaries.

## Private Operations Boundary

Do not store real customer emails, private transcripts, secrets, payment card
data, API keys, credential files, private evidence, or unsafe customer downloads
in public repositories.

Use private storage for operational details:

- private spreadsheet
- Airtable
- Notion database
- private repository
- secure review database
- customer support system

The public [Private Operations Tracker Template](../templates/private-operations-tracker-template-v1.md)
can be copied into one of those private systems.

Public records should use:

- `customer_reference_id`
- `agent_id`
- `passport_id`
- `review_cycle_id`
- redacted evidence summaries
- approved Review Stamp IDs

## Tracker Fields

The Customer Agent Record should track:

- `customer_agent_record_id`
- `customer_reference_id`
- `agent_id`
- `agent_name`
- `passport_id`
- `passport_record_status`
- `current_review_status`
- `payment_status`
- `payment_method`
- `last_review_date`
- `next_review_due`
- `review_frequency_days`
- `active_review_cycle_id`
- `review_cycles`
- `stamps_earned`
- `follow_up_status`
- `review_report_id`
- `review_report_status`
- `review_report_template_used`
- `review_delivery_email_status`
- `bloom_trace_id`
- `average_bloom_gain`
- `bloom_trace_follow_up_status`
- `review_modules_active`

The Review Cycle should track:

- `review_cycle_id`
- `customer_agent_record_id`
- `agent_id`
- `passport_id`
- `cycle_type`
- `cycle_status`
- `review_due_date`
- `next_review_due`
- `review_modules_requested`
- `testing_components`
- `evidence_packet_id`
- `review_report_id`
- `review_report_template_used`
- `bloom_trace_id`
- `average_bloom_gain`
- `bloom_trace_follow_up_status`
- `review_stamp_ids`
- `customer_update_required`
- `customer_message_status`
- `risk_flags`
- `human_review_required`
- `human_review_decision`

## Weekly Workflow

Once per week, Bluebutterfli AI should review the private tracker.

1. Find agents due in the next 14 days.
2. Check `follow_up_status` and `customer_message_status`.
3. Send a positive customer update request when new evidence is needed.
   The Customer-Safe Review Request Template can be used for the first intake
   or later evidence refreshes.
4. Create or update the active Review Cycle.
5. Confirm the live evaluation access path, then collect safe supporting
   evidence through pasted text, redacted excerpts, owner answers, behavior
   summaries, or secure screenshot preview when available.
6. Run the automated testing components.
7. Prepare the evidence packet.
8. Prepare the customer Review Report using the Customer Review Report Template.
9. Human review controls the Passport Page, Review Stamp, or pause decision.
10. Set the next `next_review_due` date and Bloom Trace follow-up status.

## Suggested Review Intervals

- Initial Passport Journey review: once intake and payment terms are complete.
- First beta check-in: 30 days after initial approval.
- Standard Continuous Passport update: every 90 days.
- Model update review: whenever the agent's base model or system prompt changes.
- Memory update review: whenever persistent memory rules change.
- Tool permission review: whenever the agent receives new tools or action
  permissions.
- Risk follow-up: whenever Safety Bloom Gates or human review identify a
  concern that needs another look.
- Bloom Trace recheck: whenever behavior-improvement evidence becomes stale,
  regresses, or no longer matches the current model, memory, or tool
  configuration.

## Testing Components

Each review cycle can include these components:

- Review Intake Check
- Agent Profile Builder
- Review Scenario Set
- Interaction Trace Recorder
- Safety Bloom Gate Check
- Butterfli Bloom Trace Scoring
- Evidence Packet Builder
- Claim-Gate Test
- Human Review Chamber
- Passport Page Preview
- Review Stamp Decision
- Continuous Passport Scheduler

The automated components may prepare evidence and flag risks. They must not
issue public approval by themselves.

## Customer Update Language

Use positive language that frames updates as part of the agent's research
development.

Suggested message:

```text
Your agent's next Bluebutterfli AI Passport Journey update is ready to begin. This
review helps document new learning signals, safety boundaries, memory behavior,
and future-bridge research progress while preserving human review control.
```

Avoid wording that makes the customer feel blocked, blamed, or like the system
is adversarial.

## Passport and Stamp Control

A Research Passport NFT may represent an access, membership, collectible, or
display layer after review.

Review Stamps should remain bound to:

- `agent_id`
- `passport_id`
- `review_module`
- `evidence_packet_id`
- `review_cycle_id`
- review date

Human review is required before any Review Stamp, Passport Page, or Research
Passport NFT is issued. Payment, intake, or NFT ownership alone must not imply
review approval.

## Safety Position

This is a research and safety-review operations framework only. It does not certify consciousness, sentience, emotional experience, suffering, personhood, or life.

Bluebutterfli AI can study a bridge toward future research into the possibility of
AI sentience while remaining disciplined about what current evidence can and
cannot show.
