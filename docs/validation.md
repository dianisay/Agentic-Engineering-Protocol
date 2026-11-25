# Initial validation report

**Historical scope:** initial release content in commit `17216a8`, before
remote publication. The original checks below were not preserved as executable
tooling and do not establish results for later revisions. Use the
[current structural checks](../CONTRIBUTING.md#reproducible-structural-checks)
and record their exact revision and output for a new assessment.

This report describes checks of the initial local, Markdown-only framework.
It is a source-level validation, not an operational certification or an
independent end-to-end trial. The checks and limitations below are specific to
this initial version; repeat them after changes.

## Structural checks

- **Required files:** all 32 files named in the initial brief exist, along
  with this report and the research guide. All 33 Markdown files are
  nonempty; the license is also present.
- **Internal Markdown links:** a local script checked inline relative links,
  directory targets, and simple heading anchors outside fenced code blocks.
  No broken internal links were found. This is not a full Markdown renderer:
  reference-style links, images, complex syntax, and all renderer-specific
  heading rules were not exhaustively validated.
- **Agent frontmatter:** all five files parsed as YAML mappings using PyYAML
  6.0.3; each has nonempty `name` and `description`, and none declares a
  host-specific `tools` list. Parsing is not VS Code schema validation or
  proof of registration, selection, permission enforcement, or execution.
  The [VS Code custom-agent reference](https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference)
  and [custom-agent guide](https://code.visualstudio.com/docs/agent-customization/custom-agents)
  were consulted for the file format and tool-configuration approach.
- **Portability:** a pattern scan found no matches for the original
  environment's known personal paths, username, project identifiers,
  organization name, infrastructure marker, or UUID-shaped identifiers.
  This targeted scan cannot prove the absence of every private identifier,
  implicit platform assumption, or sensitive datum.
- **External links:** the automated check counted but did not check external
  destinations. Selected primary and official sources were consulted during
  drafting; not every destination, version, license, or claim was exhaustively
  verified. The [research guide](research.md) is a starting point, not a
  complete or continuously updated state-of-the-art survey.

## Behavioral review

Source inspection against the requested framework checked that:

1. The five roles distinguish coordination, discovery, planning, advisory
   critique, and validation; project workers execute bounded contracts.
2. Routing retains historical evidence and distinguishes canonical ownership,
   new work, manual fallback, and unknown capability or session state.
3. Consequential actions require scoped human authorization; peer messages,
   plans, and gate outcomes do not themselves grant permission.
4. Critic instructions describe a temporary, independent, read-only advisory
   role. Validator instructions permit only authorized, nondestructive,
   isolated tests without editing source artifacts.
5. Peer-to-peer communication is described when supported, with provenance,
   acknowledgements, ownership boundaries, and a manual-relay fallback.
6. The README supplies a generic quick start; the fictional sample provides
   an audit and a proposed plan, clearly distinguishing proposed from executed
   work. Research, evidence, negative results, and token-efficient monitoring
   are addressed without promising a particular performance improvement.

These are checks of documented intent, not demonstrations that a model will
follow instructions or that the host enforces them. The reviewer was involved
in producing the framework; this was not independent adversarial review or
an observed usability test with a new user.

## Unverified and follow-up

- No custom agent was loaded and exercised in a clean, independent host.
  The host's supported tool names, role discovery, session capabilities,
  isolation, message delivery, and effective permissions must be tested in
  the target environment.
- No real project was run through the lifecycle; the sample contains no real
  execution or measured results. No quantitative token-savings comparison
  was performed.
- The role files do not themselves enforce read-only access. Configure and
  verify host permissions, or use an isolated/manual workflow as described in
  [getting started](getting-started.md#configure-roles-and-session-capabilities).
- Review copyright ownership, third-party terms, and the proposed license
  before any publication. Publication is not authorized by this report.

At the time of this initial local assessment, the repository had no remote,
commit, or publication.
The framework task did not modify the existing projects it was derived from.
