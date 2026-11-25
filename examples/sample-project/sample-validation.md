# Fictional validation: failure, revision, and acceptance

**Illustration only:** no checks ran. Counts, findings, decisions and logs in
this story are invented, not measurements or independent evidence. Real-world
claims remain `UNVERIFIED`; no actual gate is reported as passed. The PASS/FAIL
columns show how a validator would record outcomes **if** the imagined evidence
existed and were confirmed. Use the
[validation template](../../templates/validation-report.md) for real work.

## Frozen scenario

Work `SEARCH`, contract `SEARCH-C1`, gate `G1`, manual `MANUAL-v1`, and
validator-owned query judgments `HELD-v1` come from the
[sample contract](sample-contract.md). The imagined local environment is
`ENV-v1`; candidate identities `INDEX-v1` and `INDEX-v2` are immutable scenario
labels, not actual hashes. A real report must supply verifiable versions/digests,
environment versions, procedures, inputs, and original logs.

Validator is a separate imagined person/context, has no candidate write ownership,
and inspects only permitted local inputs. It verifies frozen versions before and
after each check. The gate was selected before observing either result.

## Candidate v1: imagined report V1

| Criterion | Expected | Invented observation | Illustrative outcome |
|---|---|---|---|
| Scope and ownership | Only Indexer writes candidate partition | Manual and judgment files unchanged | PASS |
| Correctness | Top-five relevant result for all three queries | Q1 and Q2 succeed; Q3 misses: 2/3 | FAIL |
| Reproducibility and provenance | Exact inputs, environment and logs | Scenario assumes logs LOG-v1 identify INDEX-v1, MANUAL-v1, HELD-v1, ENV-v1 | PASS |
| Regression and compatibility | Case and empty-query checks preserved | Both checks succeed | PASS |
| Authority and consequences | C1/A1 bounds honored; no external effects | Local only, within reservations | PASS |
| Operational readiness | Failures, recovery and handoff explicit | Failure Q3 and owner recorded | PASS |

Illustrative overall result: **FAIL**, despite five other gates passing.
The imagined Q3 query contains punctuation that v1 handles incorrectly. Validator
returns finding `F1` and diagnostic evidence to Indexer without editing the
candidate or weakening the required 3/3 threshold.

V1 and INDEX-v1 remain preserved. Coordinator records `REWORK_REQUIRED`; Owner
authorizes the single reserved retry within C1. Indexer corrects token
normalization and freezes INDEX-v2. This diagnosis is fictional, not a verified
implementation or research finding.

## Candidate v2: imagined report V2

Validator reruns correctness and both regression checks on INDEX-v2 under G1.
It rechecks versions, write boundaries, approvals, resource totals and handoff;
V1's passes are not automatically copied to a changed candidate.

| Criterion | Invented observation | Illustrative outcome |
|---|---|---|
| Scope and ownership | Only the candidate partition changed | PASS |
| Correctness | Q1, Q2 and Q3 each return a relevant section in the top five: 3/3 | PASS |
| Reproducibility and provenance | New LOG-v2 identifies INDEX-v2 with unchanged input/environment versions | PASS |
| Regression and compatibility | Case and empty-query checks succeed after normalization change | PASS |
| Authority and consequences | One authorized retry; local effects only; ceilings respected | PASS |
| Operational readiness | Handoff records versions, original failure, usage and next decision | PASS |

Illustrative local acceptance: all mandatory gates pass for INDEX-v2 under G1.
V2 links V1 and F1; it supersedes v1's candidate-readiness claim, not its historical
failure. Owner accepts only the local demonstration. Release remains unauthorized.

Residual risk: three queries do not establish general relevance. Q3 is no longer
untouched held-aside evidence after diagnostic feedback; a broader claim requires
fresh owner-approved evaluation data, a new gate, and independent validation.
The [handoff](sample-handoff.md) records that limitation and the release boundary.
