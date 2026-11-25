# Dependency message record

Use the [message envelope and reliability rules](../protocol/05-inter-agent-communication.md).
Record a manual relay as such; a receipt is not acceptance or completion.

## Envelope

- Message ID and type: [stable ID; request / clarification / evidence / delta /
  blocker / proposal / acknowledgement / decision]
- Sender and intended recipient: [neutral identities; verified authority and scope]
- Mode and channel: [direct / manual relay; verified capability; relay identity]
- Work item and effective contract: [ID; contract revision]
- Created at: [timestamp and time zone]
- Correlation and predecessor: [request or previous message ID, or none]
- Baseline and affected artifacts: [versions/digests]
- Evidence: [references; labels from the
  [claim contract](../protocol/01-audit.md#common-evidence-and-claim-contract)]
- Sharing restrictions: [permitted readers; classification; redactions]

## Content and requested response

- Question, observation, or delta: [specific change since named baseline]
- Requested action and rightful owner: [bounded action; owner or proposal only]
- Scope and limitations: [what is not established or authorized]
- Urgency and response deadline: [contract-derived deadline or none]
- Acknowledgement required: [yes/no; destination for outcome record]

## Receipt and outcome

| Event | Actor and timestamp | Evidence and understood scope |
|---|---|---|
| Sent / delivery unknown / received | [identity; time] | [receipt or limitation] |
| Understood / rejected / accepted in scope | [recipient; time] | [reply ID; scope; authority] |
| Completed / blocked / unresolved | [owner; time] | [artifact version; evidence; remaining action] |

- Deduplication and ordering: [ID already processed; predecessor checked;
  side effects not repeated]
- Retry or escalation: [contract policy; attempts; next authorized action]
- Coordinator delta: [dependency, scope, ownership, budget or gate impact;
  notification reference or no material change]
