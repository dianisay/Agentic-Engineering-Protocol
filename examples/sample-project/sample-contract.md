# Fictional worker contract: documentation search

**Illustration only:** no human approved this contract, no session was activated,
and no referenced manual, dataset, candidate, or evidence log exists. Identifiers
below name imagined records, not real resources. Use the full
[worker contract](../../templates/worker-contract.md) and
[approval record](../../templates/approval-record.md) for actual work.

## Authority and activation

- Work item `SEARCH`; contract `SEARCH-C1`; sponsor `Owner`; worker `Indexer`;
  coordinator `Coordinator`; independent reviewer `Validator`.
- Imagined approval `A1`: local reads of manual `MANUAL-v1` and development
  queries `DEV-v1`; writes only to an isolated search-output partition. Production
  manual, historical evidence, and validator-owned judgments are protected.
  No network, publication, deletion, deployment, or subcontracting is authorized.
- Validity: from fictional activation T0 until closure or 60 minutes, whichever
  comes first. Owner can revoke through the manual coordinator channel.
  Changes to the manual, targets, gate, environment, or budget require renewed
  approval. No expensive action is authorized beyond the stated local budget.
- Ownership: Indexer owns candidate output; Validator owns held-aside judgments
  `HELD-v1` and validation records; Coordinator owns coordination and handoff
  records. A read of a peer artifact does not transfer ownership.
- Handshake: Coordinator offers C1; Indexer acknowledges inputs, boundaries,
  budgets and stop conditions; Coordinator records activation and ownership at
  T0 after checking prerequisites. These steps are imagined, not real receipts.

## Objective and frozen gate

Build a keyword-search baseline for `MANUAL-v1` that returns ranked section IDs.
Non-goals: semantic search, production integration, and a general quality claim.
Relevant research is limited to the approved local manual and existing keyword
baseline documentation; external sources require a separate approval.

Before activation, Owner sets gate `G1`: each of three owner-selected held-aside
queries must return a judged-relevant section in the top five results (3/3).
The query set, judgments, candidate version, input version and environment must
be identifiable. Preserve every failed query and any previous result.
This numeric threshold is fictional and is not a recommended universal default.

The candidate also must meet all six required
[validation gates](../../protocol/07-validation.md#required-gates): authorized
ownership, correctness, provenance, regression, authority, and handoff readiness.
Baseline regression checks cover case handling and empty-query behavior.
Validator inspects exact versions independently and cannot edit the candidate.
Publication remains an Owner decision even if local acceptance succeeds.

## Dependencies and communication

Prerequisites are approved `MANUAL-v1`, development inputs, frozen `G1`,
validator-owned `HELD-v1`, and a permitted local test environment. Missing access
blocks activation; it is not permission to fetch another manual.

Indexer may ask Validator whether the held-aside evaluation is ready through a
manual relay. Validator confirms dataset identity and readiness without revealing
query judgments before candidate freeze. The
[sample message](sample-message.md) records this boundary.
Candidate versions and actual logs would be supplied at meaningful checkpoints.

## Budget, monitoring, and safe stop

The imagined aggregate budget is 60 local work-minutes: setup/coordination 10,
two implementation attempts of at most 10 each, validation 20, recovery/handoff
10. Maximum concurrency is one executing task; unused reservations are not
automatically reassigned. At most one retry is permitted after a diagnosed
failure and an explicit continuation decision within C1.

Coordinator runs manual checkpoints at activation, each candidate freeze, each
validation result, and closure. Each bounded unit is at most 10 minutes and
pauses until the next checkpoint; no background jobs or watchers are created.
Missing monitoring, exhausted budget, changed inputs, revoked approval, ownership
collision, or unsafe test behavior blocks further actions. Safe stop means cease
new writes, checkpoint partial versions and usage, verify no in-flight operations,
and notify Owner; no rollback, deletion, or automatic restart is authorized.

The [validation story](sample-validation.md) retains v1 failure, authorizes one
bounded revision, and illustrates local acceptance of v2 without release.
