# On-Chain Verification Registry v1

This design note defines how Bluebutterfli AI can make Research Passports,
Passport Pages, Review Stamps, and Evidence Packet records publicly verifiable
without placing private customer evidence on-chain.

This is a verification architecture only. It does not create a live smart
contract, minting contract, token, wallet integration, certification service, or
regulatory product.

## Current Implementation Status

Bluebutterfli currently has:

- public-safe hash manifest planning;
- evidence packet, review report, and Passport decision hash fields;
- human-review lock rules;
- demo on-chain verification artifacts;
- public/private evidence boundary language.

Bluebutterfli does not yet have:

- a deployed smart contract;
- a live registry contract address;
- wallet connection from the public website;
- automatic minting;
- automatic on-chain anchor creation;
- automatic OpenSea collection display;
- production customer dashboard account binding;
- legal or security review of a live token issuance process.

Until those items exist, public language should say `planned future on-chain
verification` or `public-safe hash manifest prepared`, not `blockchain verified`.

## Verification Principle

Bluebutterfli AI should use on-chain records for public verification anchors,
not for private evidence storage.

Recommended rule:

```text
Public verification anchors on-chain. Private evidence off-chain.
```

Milestone rule:

```text
Review milestone anchors on-chain. Agents, private evidence, and raw behavior stay off-chain.
```

The chain record should prove that Bluebutterfli AI issued a reviewed Passport
Page, Review Stamp, Evidence Packet hash, or Research Passport NFT metadata
record for a specific agent reference. It should not claim that the agent's
intelligence, mind, internal state, behavior logs, or private evidence lives
on-chain.

## What Can Be On-Chain

Future on-chain records may include:

- Research Passport NFT token ID
- public Passport ID
- public Agent ID or pseudonymous agent reference
- Review Stamp ID
- review module name
- review date
- review status
- evidence packet hash
- review report hash
- passport page hash
- metadata URI or content-addressed URI
- registry transaction hash
- issuer identity
- safety boundary fields

These records can help a customer, reviewer, or third party verify that a
displayed Passport Page or Review Stamp matches an official Bluebutterfli AI
record.

These records should verify reviewed milestones, not intelligence itself. A
public anchor can say that a specific review milestone passed a human-controlled
Bluebutterfli AI review process; it cannot prove consciousness, sentience,
emotional experience, private cognition, or general intelligence.

## What Must Stay Off-Chain

Do not put the following on-chain:

- real customer names
- real customer emails
- private transcripts
- raw evidence
- screenshots containing private information
- support messages
- payment card data
- private wallet notes
- API keys
- credential files
- medical, legal, employment, or sensitive personal information
- unreviewed intelligence claims
- live agent behavior streams
- agent internal reasoning traces unless separately reviewed and approved for
  public release
- any material the customer has not approved for public display

On-chain data can be permanent. Bluebutterfli AI should treat public blockchain
publication as irreversible and unsuitable for private review evidence.

## Evidence Hash Model

A private Evidence Packet can be hashed before a public verification anchor is
created.

Example:

```json
{
  "evidence_packet_id": "bluebutterfli-review-evidence-packet-demo-001",
  "evidence_packet_hash": "sha256:<hash>",
  "review_report_hash": "sha256:<hash>",
  "passport_page_hash": "sha256:<hash>",
  "public_registry_status": "anchor_pending"
}
```

The public on-chain record can store the hash. The private evidence can remain
off-chain in a secure operations system. If a customer later shares the exact
record, the hash can prove whether it matches the reviewed version.

## Account and Issuer Linkage

The recommended production model is:

1. Bluebutterfli AI controls an official issuer wallet.
2. The issuer wallet deploys or administers the Review Passport / Review Stamp
   registry contract.
3. The official issuer identity can be referenced from `bluebutterfliai.com`,
   the public verification page, and `bluebutterfliai.eth`.
4. A customer may optionally provide a recipient wallet after review scope and
   privacy terms are accepted.
5. The reviewed agent receives a pseudonymous public Agent ID and Passport ID.
6. Human review approves the public-safe Passport Page, Review Stamp candidate,
   metadata, and hash manifest.
7. Bluebutterfli submits an on-chain transaction from the issuer wallet that
   records a hash, emits a registry event, or mints a token linked to the public
   metadata URI.
8. The public verification page checks the contract address, transaction hash,
   token ID if applicable, metadata URI, and hash manifest.

The review status belongs to the reviewed agent record and agent version. A
wallet holder may display the stamp, but wallet ownership must not imply that a
different agent, model, deployment, or future version passed the review.

## Contract Direction

For future production use, Bluebutterfli should prefer a contract model that
supports:

- official issuer-only creation;
- human-approved metadata only;
- non-transferable or agent-bound Review Stamp semantics where practical;
- revocation or superseded-status fields for outdated reviews;
- versioned Passport IDs and Stamp IDs;
- event logs for public verification;
- no private evidence stored on-chain;
- clear metadata boundaries stating what was and was not reviewed.

OpenSea or similar NFT viewers may display token metadata if Bluebutterfli uses
an ERC-721 or ERC-1155 style contract, but marketplace display is not the
source of truth. The source of truth should be Bluebutterfli's verification
page plus the official issuer contract address and hash manifest.

## Passport NFT Verification

The Research Passport NFT may represent a public passport container, access
layer, membership layer, or collectible display layer.

The NFT metadata should include:

- passport ID
- issuer: Bluebutterfli AI
- research program: Bluebutterfli AI Behavioral Review Lab
- public safety note
- link or URI to a public-safe Passport Page
- evidence packet hash
- review report hash
- current public review status
- no-certification language

The NFT metadata must not include private evidence.

## Review Stamp Verification

Review Stamps should be public verification records only after human review.

A Review Stamp on-chain anchor should include:

- stamp ID
- passport ID
- agent ID or pseudonymous agent reference
- review module
- review date
- evidence packet hash
- companion review report hash
- non-transferable review status language
- safety note

Review Stamps should remain bound to the reviewed agent record even if the
Passport NFT is transferred.

The stamp anchor should be treated as a public proof of a reviewed milestone,
not as proof that the agent is intelligent, conscious, sentient, emotionally
experiencing, suffering, a person, alive, clinically safe, regulated, or
commercially valuable.

## Public Registry Page

Bluebutterfli AI should eventually provide a public verification page where a
customer can enter:

- Passport ID
- Review Stamp ID
- Agent ID
- token ID
- transaction hash

The page should return a public-safe verification summary, not private evidence.

## Launch Status

Founding beta should describe on-chain verification as a planned future layer
until the contract, metadata, registry, privacy policy, and human review process
are ready.

Do not enable automatic minting, wallet connection, or on-chain publication
until:

- final review decision workflow is stable
- customer privacy process is stable
- metadata language is reviewed
- no private evidence appears in metadata
- smart contract and registry behavior are reviewed
- human approval controls remain explicit

## Required Safety Language

```text
On-chain verification records do not certify consciousness, sentience,
emotional experience, suffering, personhood, life, clinical safety, regulatory
approval, investment value, or model improvement.

Plain-language boundary: an on-chain verification record does not certify consciousness.

Human review is required before any Review Stamp, Passport Page, Research
Passport NFT, or on-chain verification anchor is issued.
```
