# Project-KISS

**Keep It Simple, Stupid.**

Do not leave people to deal with complexity that the system should handle.

Project-KISS defines the design principles and overall vision for systems that are simple to use, built from replaceable components, and able to keep evolving.

## Design principles

- Put necessary complexity in the appropriate layer to reduce the burden on users, developers, and operators.
- Separate responsibilities and interfaces so that each component can be improved or replaced independently.
- Run the smallest meaningful implementation, then make decisions through observation, measurement, and independent verification.
- Record the reasons for changes and their results so that changes can be reversed when needed.
- Protect users' freedom and control, and make both building and using the system rewarding.

## What we are building

[Project-AceIS](https://github.com/orgs/i-pp/projects/2) is a subproject of Project-KISS. It coordinates the design, implementation, and verification of AceIS and its ACE, PAUL, GENE, and PETER components.

AceIS is the integrated system that contains these components. Its design separates reasoning, verification, self-improvement, program analysis, native code generation, and portability and translation. Detailed specifications and implementation boundaries remain subjects for the draft design document.

## Draft design document

- [Current design update: acc, native sysroot, Ace-Core, and verification](docs/design-update-2026-11-07.md)
- [Integrated design principles and system vision, fifth-edition draft](docs/Project-KISS_design_v5_draft.en.md)
- [Preserved fifth-edition source](docs/Project-KISS_design_v5_draft.md)

This repository contains documentation only. Implementation code and experiment logs belong elsewhere. Directions, proposals, deferred decisions, and unverified ideas in the design document are not completed specifications or performance guarantees.

The legacy name "Project-ACE" in the fifth edition refers to the subproject now managed on GitHub as "Project-AceIS." The original fifth-edition source and its English translation are preserved unchanged for traceability. Read the current update for later directions and the English fifth edition for the baseline design.

AceGeneralPublicLicense is a name under consideration in the design concept. The fifth edition does not replace license terms. Terms of use will be established separately.

## Development policy

Project-KISS and Project-AceIS use English for descriptions, documentation, issues, pull requests, and commit messages. Source code, including comments and string literals, must be ASCII-only. See the [shared development policy](docs/development-policy.md) for scope and verification guidance.

## Project management

- [Project-KISS](https://github.com/orgs/i-pp/projects/1)
- [Project-AceIS](https://github.com/orgs/i-pp/projects/2)

The management relationship between the GitHub Projects is documented through these cross-links and this repository.
