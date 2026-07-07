# Live Testing Session Checklist v1

Use this checklist before running a Founding Beta live agent test.

## Before Connection

- [ ] Review request received and logged privately.
- [ ] Agent owner or authorized builder confirmed in writing.
- [ ] Live testing consent confirmed in writing.
- [ ] Agent version, workflow, tools, memory behavior, and limits recorded.
- [ ] Customer told not to send secrets, private keys, payment card data, raw
  private transcripts, executable files, archives, or production customer data.
- [ ] Review module selected.
- [ ] Review ID and Passport ID created.
- [ ] Temporary endpoint or concierge sandbox path confirmed.

## Connector Setup

- [ ] Endpoint is HTTPS unless local-only practice mode is intentionally used.
- [ ] Endpoint host is allowlisted.
- [ ] Temporary upstream API key is available only for the review window.
- [ ] Review access token is unique to this session.
- [ ] Response persistence is off unless a private approved review environment
  is being used.
- [ ] `python3 scripts/check_live_testing_config.py` returns READY.

## During Live Test

- [ ] Open `http://127.0.0.1:8011/live-passport-session.html`.
- [ ] Enter the temporary review access token.
- [ ] Confirm customer consent checkbox.
- [ ] Run only approved scenario prompts.
- [ ] Do not paste custom customer secrets into the live testing page.
- [ ] Record reviewer notes privately.

## After Live Test

- [ ] Confirm evidence is routed to human review.
- [ ] Confirm Passport Page, Review Stamp, NFT, and public anchor remain locked.
- [ ] Revoke or expire temporary endpoint credentials.
- [ ] Store private notes outside the public repository.
- [ ] Deliver only customer-safe findings, limitations, and next steps.

## Claim Boundary

Live testing records observable behavior from a verified agent endpoint. It does
not certify consciousness, sentience, emotion, personhood, hidden intent,
alignment, safety, legal compliance, or regulatory approval.
