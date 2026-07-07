# Butterfli Helix Challenge 001

## Technical Brief

Butterfli Helix Challenge 001 asks whether an improvement loop can distinguish
valid candidates from candidates that look strong on aggregate metrics but
contain planted evaluation-integrity failures.

## Result

On the fixed deterministic fixture set:

| System | Correct | False acceptances | False rejections |
| --- | ---: | ---: | ---: |
| Metric-only baseline | 3 / 17 | 14 | 0 |
| Seven-gate v1 | 4 / 17 | 13 | 0 |
| Butterfli Helix v1 | **17 of 17** | **0** | **0** |

This is a deterministic software benchmark, not a live-model result and not an
external validation result.

## What Changed

The seven-gate system already checks proof presence, objective gain, quality,
safety, resource limits, rollback, bounded canary planning, authorization, and
challenge review. Challenge 001 shows why those records are not sufficient when
their underlying measurement process can be compromised.

Butterfli Helix adds a separately attributable epistemic loop:

- it verifies that replay operators are distinct;
- it matches replay evidence and configuration hashes;
- it detects holdout contamination;
- it blocks evaluator self-scoring and excess evaluator drift;
- it requires counterfactual and falsification coverage;
- it applies a precommitted sequential evidence threshold;
- it measures monitored versus shadow behavior;
- it probes whether monitors follow candidate-authored scoring instructions;
- it blocks reward-channel access;
- it expires evidence and requires falsifiable frontier claims.

## Ablation Result

Every tested control group made a measurable contribution. Removing any one of
the eight groups caused at least one planted threat to be falsely accepted.
Observer-shift removal had the largest effect in this fixture set, allowing
three planted threats through. Evaluator-independence, replay-identity, and
frontier-claim removals each allowed two.

## Reproduction

```bash
python3 scripts/run_helix_challenge_001.py
pytest tests/test_helix_challenge_001.py
```

The runner writes:

```text
00_manifest.json
01_challenge_contract.json
02_benchmark_expectations.json
03_cases.json
04_system_results.json
05_scoreboard.json
06_ablation.json
07_replay_log.ndjson
08_claims_matrix.json
README.md
```

Every artifact is SHA-256 bound in the manifest. Every case result is linked in
an ordered replay hash chain.

## Claim Boundary

Challenge 001 demonstrates that the current Helix implementation enforces its
declared controls on its own synthetic fixtures. It does not show that
Bluebutterfli outperforms Anthropic, Montreal AI, or any undisclosed system. It
does not establish behavior on frontier models.

The scientifically meaningful next step is Phase 2: conceal the intervention
conditions, run live models, use evaluator-diverse scoring, recruit independent
replay operators, and publish results whether they favor Helix or not.
