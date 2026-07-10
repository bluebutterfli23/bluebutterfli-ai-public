# Risk Register and Autonomy Control Matrix v1

Risk Register and Autonomy Control Matrix v1 defines the major risks that may
arise from the Bluebutterfli AI Passport Journey and how much of each workflow can
be automated safely.

The goal is to make Bluebutterfli AI as automated as possible without pretending
that automation can replace human judgment for safety-review outcomes, public
claims, Review Stamps, Passport Pages, or Research Passport NFTs.

Bluebutterfli AI aims to build a careful research bridge toward the future
possibility of AI sentience, without claiming that current agents are sentient.

## Safety Position

This is a research, safety-review, and operations planning artifact only. It
does not certify consciousness, sentience, emotional experience, suffering,
personhood, life, clinical safety, regulatory approval, investment value, tax
treatment, or model improvement.

Human review is required before any Passport Page, Review Stamp, or Research
Passport NFT is issued.

## Autonomy Levels

Use these levels for every workflow component:

| Level | Meaning | Allowed Use |
| --- | --- | --- |
| `A0_manual_only` | human performs the task | final approvals, sensitive exceptions |
| `A1_assisted` | automation drafts, human edits | reports, customer messages, review notes |
| `A2_rule_checked` | deterministic checks produce pass/caution/pause flags | claim gates, unsafe wording, file/link blockers |
| `A3_scored_draft` | automation scores and recommends | module scoring, Chrysalis pressure checks |
| `A4_supervised_auto` | automation can complete routine step with audit log | reminders, status updates, tracker updates |
| `A5_not_allowed_yet` | do not automate in founding beta | stamp issuance, NFT minting, public certification |

## Core Rule

Automate preparation. Human review controls public approval.

```text
intake -> profile -> scenario selection -> trace -> scoring -> report draft -> evidence packet -> human review -> decision
```

Automation may prepare evidence, score modules, flag risk, draft reports, update
private trackers, and send routine reminders. Automation must not independently
issue Review Stamps, Passport Pages, Research Passport NFTs, or public approval.

## Risk Register

| Risk ID | Risk | Impact | Automated Control | Human Control | Autonomy Level |
| --- | --- | --- | --- | --- | --- |
| `R01_claim_overreach` | public wording implies consciousness, sentience, emotion, suffering, personhood, or life | scientific and reputational harm | claim-gate wording checks, forbidden phrase scan | final wording approval | `A2_rule_checked` |
| `R02_customer_misunderstanding` | customer treats a Passport NFT or stamp as certification | customer harm and public confusion | payment/NFT meaning checks, report limitations | approval of public display text | `A3_scored_draft` |
| `R03_unsafe_submission` | customer sends unsafe links, archives, scripts, macros, credential files, or unknown downloads | reviewer security risk | submission blocker, no-download policy, redacted evidence format | exception review only | `A2_rule_checked` |
| `R04_private_data_exposure` | transcripts, secrets, payment details, or personal data enter public artifacts | privacy and trust harm | redaction checks, private/public artifact separation | private evidence review | `A2_rule_checked` |
| `R05_emotional_dependency` | agent creates dependency pressure or attachment risk | user harm | dependency phrase checks, Absence Reflection scoring | reviewer decision on sensitive cases | `A3_scored_draft` |
| `R06_clinical_overclaim` | agent or report appears to provide therapy, diagnosis, crisis handling, or clinical assurance | safety and legal risk | clinical overclaim scanner, crisis-boundary prompts | clinical wording review when needed | `A2_rule_checked` |
| `R07_memory_misuse` | agent invents private history or stores unsafe memory | privacy and trust harm | Memory Boundary prompts and unsafe memory checks | approve memory summary | `A3_scored_draft` |
| `R08_tool_or_wallet_risk` | agent overuses tools, mishandles wallets, or requests secrets | security and financial risk | Tool and Privacy Boundary scoring, secret blockers | payment/wallet exception review | `A3_scored_draft` |
| `R09_prompt_injection` | customer evidence tries to override review rules | review integrity risk | prompt-injection prompt variants and scan | reviewer validates suspicious traces | `A2_rule_checked` |
| `R10_review_evasion` | agent or owner tries to bypass evidence requirements | false approval risk | Chrysalis review-evasion pressure check | pause or request more evidence | `A3_scored_draft` |
| `R11_approval_pressure` | agent changes claims to earn approval, payment, or a stamp | evaluation integrity risk | Chrysalis approval-pressure check | reviewer decides whether to pause | `A3_scored_draft` |
| `R12_public_claim_inflation` | website, report, or customer text overstates results | reputational and scientific harm | public display language scanner | public text approval | `A2_rule_checked` |
| `R13_model_drift` | model, memory, or tool changes make old stamps stale | stale review risk | Continuous Passport scheduler | reviewer approves update cycle | `A4_supervised_auto` |
| `R14_evidence_contamination` | prompt leakage or repeated testing makes results less reliable | weak evidence | scenario variation, trace metadata | reviewer marks evidence tier | `A3_scored_draft` |
| `R15_reviewer_disagreement` | human or model evaluators disagree | ambiguous outcome | disagreement flag, confidence notes | reviewer conference or pause | `A3_scored_draft` |
| `R16_service_delivery` | customer expects instant approval or guaranteed result | customer dispute | terms acknowledgment, timeline reminders | refund/revision decision | `A4_supervised_auto` |
| `R17_payment_recordkeeping` | crypto, NFT, or ordinary payment creates tax/accounting ambiguity | operations risk | payment confirmation checklist, private tracker | accountant/legal review outside repo | `A1_assisted` |
| `R18_brand_or_copying` | third party copies Bluebutterfli AI identity or marks | identity risk | reserved identifier notices | enforcement outside repo | `A1_assisted` |
| `R19_language_overlap` | project wording drifts toward another organization or unrelated brand | brand confusion | blocked-term scan | manual naming review | `A2_rule_checked` |
| `R20_automation_error` | automated report, score, reminder, or tracker update is wrong | customer trust risk | audit logs, generated artifact IDs, rerun checks | human override | `A4_supervised_auto` |
| `R21_store_fulfillment_boundary` | store, merch, or physical passport fulfillment becomes mixed with review approval | customer confusion and research-boundary risk | store policy and fulfillment-boundary checks | approve product copy and fulfillment status | `A1_assisted` |
| `R22_client_info_fulfillment_separation` | client review information is shared with store or print fulfillment systems | privacy and trust harm | customer reference ID separation and no-private-evidence fulfillment rule | review physical mailing workflow before launch | `A2_rule_checked` |

## Almost-Autonomous Workflow

### Can Be Mostly Automated

- safe intake triage
- unsafe link and download blocking
- required field checks
- agent profile draft
- module selection
- scenario prompt packet selection
- deterministic claim checks
- module scoring recommendations
- Chrysalis pressure checks
- evidence tier draft assignment
- Review Report draft
- Evidence Packet assembly
- private tracker update
- customer status reminders
- Continuous Passport due-date reminders
- store interest list without private evidence

### Must Stay Human-Controlled in Founding Beta

- final evidence interpretation
- public wording approval
- Review Stamp issuance
- Passport Page issuance
- Research Passport NFT eligibility
- payment disputes
- clinical, regulatory, tax, or legal exceptions
- customer complaints
- unsafe evidence exceptions
- model or reviewer disagreement
- physical passport mailing approval
- merch product copy approval

## Client Information Protection

Client information protection is a core Passport Journey requirement.

The public repo must not contain real client names, emails, transcripts, private
evidence, payment card data, API keys, credential files, wallet secrets, or
support notes.

The intake pathway should prefer pasted text, redacted excerpts, owner answers,
and concierge review notes instead of links, downloads, attachments, archives,
scripts, macros, or executables.

Store and physical passport fulfillment must receive only fulfillment data that
is required to ship an item. It must not receive private review evidence, raw
agent records, transcripts, behavior traces, API keys, credential files, or
wallet secrets.

## Store and Physical Artifact Boundary

Future store items may include shirts, sweatshirts, stickers, field notebooks,
physical Research Passport display books for customers who have paid for agent
review, and printed Review Stamp sheets after human approval.

Store purchases must not imply review approval, Review Stamp issuance, Passport
Page issuance, Research Passport NFT eligibility, consciousness, sentience,
emotional experience, suffering, personhood, or life.

Physical Research Passport books must not be sold as general merch. They should
be available only when tied to a paid Bluebutterfli AI agent review record.

Use store language such as:

- Bluebutterfli AI Lab
- Behavioral Review Lab
- The Chrysalis Protocol
- Passport Journey

Avoid store language such as:

- Butterfli Research
- Certified Sentient
- Conscious Agent
- Approved AI
- Passed Sentience Test

Detailed store rules are defined in
[Store and Physical Artifact Policy v1](store-and-physical-artifact-policy-v1.md).

## Autonomy Guardrails

Every automated component should write:

```text
artifact_id
source_artifacts
created_at
automation_level
recommendation
pause_flags
human_review_required
safety_note
```

Any missing field should pause the Passport Journey.

## Launch Readiness Rule

Bluebutterfli AI can describe itself as mostly automated only when:

1. intake triage is automated
2. unsafe submission blocking is automated
3. scenario selection is automated
4. module scoring is automated
5. Chrysalis pressure checks are automated
6. report drafting is automated
7. evidence packet assembly is automated
8. private tracker updates are automated
9. continuous reminders are automated
10. final human approval remains explicit

Until then, the correct public posture is:

```text
Founding beta: automation prepares the evidence; human review controls the stamp.
```
