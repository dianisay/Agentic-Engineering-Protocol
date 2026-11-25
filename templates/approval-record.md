# Human approval record

Use the [authority rules](../protocol/01-audit.md#common-authority-and-ownership-rules).
This record documents a decision; filling out a proposal does not grant approval.

- Approval ID and revision: [stable ID; revision]
- Status: [proposed / approved / denied / expired / revoked / superseded]
- Human decision-maker: [authorized role or neutral identity; verification method]
- Decision channel and evidence: [authenticated channel; durable reference;
  access restrictions; do not copy credentials]
- Objective and work/contract references: [scope; IDs and revisions]
- Allowed actions and exact targets: [actions; resources; artifact versions or
  bounded version range]
- Exclusions: [actions and targets not authorized]
- Environment and access: [environment identity; permitted read/write/network scope]
- Ceilings: [aggregate cost, compute, time and other resource bounds; accounting
  method; what constitutes an expensive action in this context]
- Safeguards and preconditions: [checks required before acting; owner]
- Validity: [effective time; expiry or bounded completion condition; time zone]
- Revocation: [authorized channel; recipient; handling of in-flight actions]
- Renewed approval triggers: [scope/version/environment/budget changes or other
  conditions from the authority decision]
- Decision and rationale: [human decision; date or pending; limitations]
- Related records: [prior revision; superseding or revocation record; original
  remains accessible]
