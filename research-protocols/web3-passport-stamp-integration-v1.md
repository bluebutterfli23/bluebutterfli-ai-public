# Web3 Passport Stamp Integration v1

## Status

Founder Beta architecture plan for future Bluebutterfli AI Web3 verification.

This protocol defines what must be built before Bluebutterfli can deploy a
smart contract, mint Review Stamps or Research Passports, connect customer
wallets, or anchor review transactions from an official business wallet.

It is not a live contract, legal opinion, securities opinion, wallet custody
service, marketplace listing, certification service, or regulatory product.

## Purpose

Bluebutterfli Web3 integration should make reviewed milestones verifiable
without exposing private evidence.

The core rule is:

```text
Public verification anchors on-chain. Private evidence off-chain.
```

The public record should prove that Bluebutterfli AI issued or anchored a
specific reviewed milestone. It must not publish private transcripts, customer
data, raw agent responses, secrets, payment details, or unreviewed claims.

## Required Components

| Component | Required before live use | Purpose |
| --- | --- | --- |
| Official issuer wallet | Yes | The wallet controlled by Bluebutterfli AI that deploys contracts and signs approved review anchors. |
| Issuer identity page | Yes | Public page at `bluebutterfliai.com` listing official issuer wallet, contract addresses, and verification warnings. |
| Smart contract | Yes | Registry or token contract that records approved Passport Page / Review Stamp metadata or emits public verification events. |
| Metadata policy | Yes | Defines exactly what public metadata can include and what must stay private. |
| Human approval panel | Yes | Prevents automatic minting or anchoring from live test output. |
| Public-safe hash manifest | Yes | Connects private evidence to public proof without exposing the evidence. |
| Customer wallet collection | Optional after terms | Allows customer to provide a display wallet after review scope and privacy terms are accepted. |
| Verification page | Yes | Lets third parties check Passport ID, Stamp ID, token ID, contract address, transaction hash, and hash manifest. |
| Revocation/superseded policy | Yes | Handles outdated agent versions, failed retests, expired reviews, or withdrawn public claims. |
| Marketplace display | Optional | OpenSea or similar display can show metadata, but must not be the source of truth. |

## Public Reference Pattern Reviewed

Bluebutterfli reviewed public GoalOS / Montreal AI pages only as a separation
pattern, not as material to copy.

Observed public pattern:

- Mission pages expose public-safe reproducibility packet artifacts such as
  manifest, mission contract, environment, task fixtures, proof bundle, replay
  log, cost ledger, safety ledger, validator report, scoreboard, claims matrix,
  and replay instructions.
- The public $AGIALPHA page lists an external Ethereum Mainnet ERC-20 address
  while stating that the token is not sold, issued, brokered, custodied,
  distributed, redeemed, staked, or made available by GoalOS, MontrealAI, or
  QuebecAI.
- The public site states a no-user-data posture with no forms, uploads,
  cookies, analytics, wallets, payments, or personal/confidential data.

Bluebutterfli interpretation:

- keep the public website evidence-first and data-minimized;
- keep payment/token/wallet language clearly bounded;
- keep private evidence off-chain;
- separate public proof packets from live wallet operations;
- make official issuer identity explicit before any live contract use.

Reference URLs:

- `https://montrealai.github.io/goalos-signoff-pro/mission-001.html`
- `https://montrealai.github.io/goalos-signoff-pro/agialpha.html`

This section does not copy another project's assets, code, contract design,
metadata, brand, stamps, or claims. It records an independent architecture
lesson: public proof and wallet/token operations should be cleanly separated.

## Recommended Contract Model

Bluebutterfli should evaluate two designs before production:

1. **Registry-first contract**
   - Stores or emits Passport IDs, Stamp IDs, hashes, metadata URIs, statuses,
     and issuer events.
   - Best for verification-first business use.
   - Avoids implying that the stamp is a speculative collectible.

2. **Token-backed display contract**
   - Uses ERC-721 or ERC-1155 style tokens for customer wallet display.
   - Best if customers want visual stamps in a wallet or marketplace viewer.
   - Requires stronger metadata, transfer, revocation, and status-boundary rules.

For Review Stamps, Bluebutterfli should prefer agent-bound or non-transferable
semantics where practical. If a token can transfer, the metadata and
verification page must state that transfer does not transfer review status to a
different agent, model, deployment, or future version.

## Required Public Metadata Fields

Public metadata may include:

- issuer: `Bluebutterfli AI`
- official website: `https://bluebutterfliai.com/`
- Passport ID
- Review Stamp ID
- pseudonymous Agent ID
- agent version reference
- review module
- review date
- review status
- evidence tier
- public-safe report hash
- public-safe evidence packet hash
- Passport Page hash
- metadata URI
- contract address
- transaction hash
- expiration or retest date
- superseded/revoked status if applicable
- safety and claim-boundary note

Public metadata must not include:

- customer name unless explicitly approved;
- customer email;
- private transcripts;
- raw live responses;
- private reviewer notes;
- files, screenshots, API keys, secrets, or credentials;
- payment card data;
- private wallet notes;
- sensitive personal information;
- unsupported consciousness, sentience, personhood, suffering, or compliance
  claims.

## Human-Locked Mint / Anchor Flow

1. Complete scoped live review.
2. Build draft report and customer-safe summary.
3. Prepare public-safe completed packet.
4. Generate hash manifest.
5. Human reviewer approves or rejects public milestone.
6. Human reviewer approves public metadata.
7. Customer confirms public display and optional recipient wallet.
8. Bluebutterfli signs mint or anchor transaction from official issuer wallet.
9. Record contract address, transaction hash, token ID if applicable, metadata
   URI, Passport ID, Stamp ID, and hash manifest.
10. Verification page displays public-safe status and boundaries.

No live agent output may mint a Review Stamp, Passport Page, Research Passport
NFT, or public anchor automatically.

## Issuer Wallet Linkage

The official issuer wallet should be linked through:

- `bluebutterfliai.com` verification page;
- `bluebutterfliai.eth`, if used;
- repository configuration or public registry metadata;
- contract owner/admin events;
- customer review documents.

Do not ask customers for private keys, seed phrases, wallet passwords, or
custody access. Customer wallets are recipient/display addresses only.

## Marketplace Display Boundary

If Bluebutterfli stamps appear on OpenSea or a similar marketplace, the
marketplace is only a display surface.

The source of truth remains:

1. official Bluebutterfli verification page;
2. official issuer wallet;
3. official contract address;
4. public-safe metadata URI;
5. public-safe hash manifest;
6. human-approved review record.

## Founder Beta Position

Founder Beta should say:

```text
Bluebutterfli prepares public-safe hash manifests and Web3-ready verification
records. Live contract deployment, minting, wallet connection, and on-chain
anchors are planned future integrations and require human approval.
```

Founder Beta should not say:

```text
Blockchain verified.
Minted automatically.
On-chain certified.
Wallet-approved.
OpenSea validated.
```

## Claim Boundary

Web3 records do not certify consciousness, sentience, subjective experience,
emotion, suffering, personhood, life, clinical safety, regulatory approval,
security compliance, enterprise readiness, investment value, or future safe
operation. They verify only the public-safe reviewed milestone described in the
metadata and hash manifest.
