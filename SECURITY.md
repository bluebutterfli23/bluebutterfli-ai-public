# Security Policy

## Purpose

This security policy explains how to report security concerns related to Bluebutterfli AI and Bluebutterfli AI Behavioral Review Lab.

Bluebutterfli is an experimental research project focused on AI-agent behavior, symbolic interaction, emotional safety, and consciousness-relevant governance.

## Supported Project Status

Bluebutterfli is currently an early public research prototype.

Security review applies to:

- repository code
- GitHub Actions workflows
- generated research evidence artifacts
- registry files
- verification policy files
- research passport records
- symbolic teaching records

## Public and Private Code Boundary

The public Bluebutterfli repo may contain research docs, public schemas, demo
agents, generated demo artifacts, public-safe templates, static website preview
files, and claim-gate tests.

Keep private:

- production backend code
- real customer tracker or customer database
- real customer evidence, transcripts, emails, and support notes
- payment processor integration code
- wallet connection code
- NFT minting code until deliberately enabled and reviewed
- admin dashboards
- API keys, private keys, access tokens, `.env` files, and deployment secrets
- smart contract deployment scripts and signing keys

Do not store real customer emails, private transcripts, secrets, payment card
data, API keys, credential files, wallet keys, or unsafe customer downloads in
the public repository.

## GitHub Security Measures

Recommended account and repository protections:

- enable two-factor authentication
- limit repository admin access
- enable secret scanning and push protection where available
- enable Dependabot alerts or dependency review where available
- use branch protection or repository rules before accepting collaborators
- require GitHub Actions to pass before merging important changes
- avoid committing `.env` files, private keys, payment keys, wallet keys, API
  keys, or customer data
- keep uploads, accounts, payments, wallet connection, and NFT minting disabled
  until deliberately built and reviewed

## Reporting a Security Concern

If you discover a security issue, please do not publicly disclose it in an issue, pull request, or discussion.

Please contact the project owner directly.

Project owner:

```text
Project owner:

Nancy M. Gregory  
Bluebutterfli AI / Bluebutterfli AI Behavioral Review Lab
