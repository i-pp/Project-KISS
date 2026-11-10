<!--
SPDX-FileCopyrightText: 2026 I-plusplus Inc.
SPDX-License-Identifier: LicenseRef-KOL-v1
-->

# Project-KISS Coding Standard v1.0

Status: **Proposed** (not yet repository-validated)

## 1. Purpose and principles

- **KISS**: avoid complexity without a demonstrated requirement.
- **Single responsibility**: functions, types, and files have clear responsibilities.
- **Readability**: optimize for maintenance and review, not typing speed.
- **Testability**: isolate external dependencies and verify behavior independently.
- **Determinism**: builds and generated artifacts should be reproducible where practical.
- **Traceability**: relate source, tests, generated outputs, commits, and CI evidence.
- **Portability**: isolate platform-specific code and declare supported targets.
- **AI accountability**: AI-produced changes meet the same standard as human changes.

MUST = required for new/changed code; SHOULD = preferred unless justified; MAY = optional.

## 2. Architecture

- MUST respect documented dependency direction; do not introduce cyclic dependencies.
- MUST search for existing implementations before introducing duplicates.
- MUST keep generated files separate from handwritten sources, with provenance and regeneration instructions.
- SHOULD keep files <= 500 lines, functions <= 60 lines, nesting <= 4 levels, and parameters <= 5.
- SHOULD target cyclomatic complexity <= 15. These are review triggers, not automatic proof of defects.
- Files over 1000 lines require a documented decomposition decision for substantial changes; avoid mechanical splitting.
- Exceptions (e.g., instruction tables, ABI adapters) MUST include rationale and owner.

## 3. C and C++

- MUST use the repository-pinned clang-format version and `.clang-format`.
- Style: 4 spaces, LF, UTF-8, 100-column target, Allman braces, type-attached pointer/reference syntax.
- Naming: `PascalCase` for types, `snake_case` for functions/variables, `kPascalCase` for constants, `UPPER_SNAKE_CASE` for macros.
- MUST document ABI, ownership, lifetime, alignment, and error contracts at C/C++ boundaries.
- SHOULD prefer RAII and explicit ownership in C++; avoid unexplained owning raw pointers.
- MUST distinguish C-specific from C++-specific analysis checks.

## 4. Python and scripts

- MUST run Ruff format/lint on maintained Python sources, using the pinned version.
- SHOULD use Python for tooling, fixtures, build orchestration, and verification, not silently relocate compiler core logic into scripts.
- Generation scripts MUST declare input, output, invocation, and determinism constraints.

## 5. JSON, fixtures, goldens, and generated files

- Configuration JSON: validate against a schema where a stable contract exists.
- Fixtures: record the behavior or failure they are designed to exercise.
- Goldens: MUST NOT be regenerated merely to make a failing test pass. Changes require specification or defect rationale, meaningful diff, and independent verification.
- Generated artifacts: MUST identify generator, source inputs, regeneration command, and relevant tool version.
- Serialization contracts MUST define key ordering, numeric representation, whitespace, and newline behavior where byte-for-byte comparisons matter; never reorder semantically ordered arrays.

## 6. Tests and evidence

- MUST cover new behavior with positive, negative, and boundary cases as appropriate.
- MUST avoid deriving expected results from the same implementation logic under test.
- SHOULD use independent oracles, property tests, fuzzing, and regression cases where valuable.
- SHOULD run sanitizers (ASan/UBSan) on applicable native code.
- Coverage terms C1/C2/C3/C4 and MC/DC require explicit definitions and scoped evidence before claiming compliance.
- CI evidence SHOULD identify commit, environment, tools, test outcomes, and artifact digests.

## 7. Change management

- MUST avoid unrelated bulk reformatting in feature or bug-fix PRs.
- MUST disclose untested paths, limitations, and residual risks.
- MUST not report checks as passed unless executed and observed.
- MUST record exceptions in the PR or a tracked decision.

## 8. Enforcement and migration

- **Blocker**: security/correctness/ABI regression, unsubstantiated golden replacement, broken required tests.
- **Required**: new-code formatting, lint, and test violations once a gate is activated.
- **Advisory**: legacy complexity and structural debt captured in a baseline.
- Phase 1: establish tool versions and baseline; Phase 2: enforce new/changed-code checks; Phase 3: pay down existing debt and publish monitorable evidence.
- Existing violations alone do not block unrelated work. Exception: a critical risk directly affected by the change.

## 9. Repository-specific supplements

Compiler-specific IR, diagnostic, ABI, code-generation, and golden requirements belong in a separately versioned ace-cc supplement. Do not assert certification or compliance without scope and evidence.
