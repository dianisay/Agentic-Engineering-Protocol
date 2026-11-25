# Contributing

This repository contains portable instructions, not a hosted service. Before
contributing, establish that you are authorized to share the material and that
the project owner accepts its [MIT license](LICENSE). Never include private
transcripts, credentials, personal paths, customer information, or copyrighted
material without permission.

1. Describe the problem, intended users, threat and privacy boundaries, and
   evidence that the existing protocol does not already solve it.
2. Place each new rule in its authoritative protocol document and link to it;
   avoid duplicating policy across role instructions and templates.
3. Preserve reduced-capability workflows for hosts without session tools.
   Avoid assumptions about language, infrastructure, or project priorities.
4. Test example workflows and relative Markdown links. Parse each custom-agent
   YAML header and check host compatibility; tests must not touch real users'
   work or execute untrusted repository content.
5. Report what you checked, which tool/host versions you used, failures, and
   remaining uncertainty. Clearly distinguish a citation from a verified claim
   and a template example from an executed system.
6. Request review for changes to approvals, session routing, validation,
   persistence, or privacy boundaries. Do not merge or publish without the
   maintainer's explicit authorization.

For research claims, cite original sources and dates, characterize scope and
limitations, and avoid asserting that more agents or fewer tokens guarantee
better results. See [research guidance](docs/research.md).
