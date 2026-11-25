# Fictional dependency message and acknowledgement

**Illustration only:** nothing was sent or received. Message identifiers,
times, datasets and receipts below are invented. All real-world delivery and
capability claims remain `UNVERIFIED`. Use the
[message template](../../templates/message-record.md) for a real exchange.

## Request

- ID `MSG-1`; type `request`; sender Indexer; recipient Validator.
- Work `SEARCH`; contract `SEARCH-C1`; baseline `MANUAL-v1`; creation T0+5 minutes.
- Mode `MANUAL`: Coordinator would relay the unchanged message and retain
  attribution. No direct session tool or delivery guarantee is assumed.
- Content: "Is `HELD-v1` ready for gate `G1`? Confirm its version and your ability
  to evaluate a frozen candidate; do not send the held-aside query judgments."
- Requested action: readiness confirmation by the judgment owner, not permission
  to change the evaluation set or expand Indexer's access.
- Sharing: authorized project roles only; no manual text or private data copied.
- Acknowledgement required before candidate submission; response deadline is the
  next bounded checkpoint under C1. Evidence link in real use would identify
  accessible readiness records; none exists in this fictional example.

## Imagined receipt and response

| ID / relation | Event and fictional time | Meaning |
|---|---|---|
| `MSG-1` | Received, T0+6 minutes | Receipt only; not agreement to perform additional work. |
| `MSG-2`, reply to `MSG-1` | Understood and accepted in scope, T0+7 minutes | Validator has sole judgment ownership and can check a frozen candidate against G1. Queries and judgments stay withheld. |
| `MSG-3`, reply to `MSG-2` | Readiness dependency resolved, T0+8 minutes | Indexer acknowledges version HELD-v1 and submits no request for restricted labels. |

Coordinator records the dependency as ready within the imagined narrative.
A readiness answer is not evidence that candidate quality passed.
No message changes the contract, ownership, budget, or publication authority.

If a relay delivered MSG-1 twice, the recipient would deduplicate its ID and not
repeat side effects. Without a response, the bounded unit pauses at the next
checkpoint and escalates under C1; silence does not justify a duplicate worker.
The candidate then follows the [validation story](sample-validation.md).
