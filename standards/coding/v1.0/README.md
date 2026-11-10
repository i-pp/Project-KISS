<!--
SPDX-FileCopyrightText: 2026 I-plusplus Inc.
SPDX-License-Identifier: LicenseRef-KOL-v1
-->

# Project-KISS Coding Standard v1.0

Use [CODING_STANDARD.md](CODING_STANDARD.md) and
[AGENT_CODING_POLICY.md](AGENT_CODING_POLICY.md) when preparing code changes.
The policy text is preserved as supplied, including its Proposed status.
Storing this package does not activate tools or CI in any implementation repository.

## Read this first

- Follow the existing [shared development policy](../../../docs/development-policy.md)
  alongside this standard. English communication, ASCII-only maintained source,
  tests, coverage evidence, and existing repository requirements still apply.
  UTF-8 in the formatting templates does not permit non-ASCII source.
- Review each target repository's architecture, instructions, toolchain, current
  configuration, and baseline before adopting templates.
- The workflow is an advisory whole-tree baseline starter. It does not implement
  changed-code enforcement, clang-tidy, builds, tests, coverage, or automatic
  ASCII source discovery. A green workflow is not evidence that these ran.
- Project-KISS remains documentation-only. No root tool configurations or active
  `.github/workflows` files are installed here.

## Check the templates locally

From the Project-KISS root, these commands install isolated reference tools and
validate the Clang configuration syntax:

```sh
python3 -m venv /tmp/kiss-coding-tools
/tmp/kiss-coding-tools/bin/python -m pip install \
    clang-format==18.1.8 clang-tidy==18.1.8 ruff==0.8.6

/tmp/kiss-coding-tools/bin/clang-format \
    --style=file:standards/coding/v1.0/templates/.clang-format --dump-config
/tmp/kiss-coding-tools/bin/clang-tidy \
    --config-file=standards/coding/v1.0/templates/.clang-tidy --verify-config
```

These are configuration checks, not a project build or Quick Start. The reference
versions are validated together for this package; they are not a new universal
toolchain requirement. Review and record a target repository's exact versions
before applying formatting changes.

## Integrate in a target repository

1. Review both policy documents and the target repository's supplement. Resolve
   conflicts before changing existing source or configuration.
2. Compare the four files in `templates/` with existing root configuration.
   Copy or merge only the approved settings. Do not overwrite local changes.
3. Select the actual maintained source paths, including extensionless scripts.
   Identify dependencies, generated files, fixtures, exclusions, and ownership.
   The starter's extension lists are not a complete source-scope classifier.
4. Check format/lint locally with the selected files and root configurations.
   Record failures as a baseline before making checks mandatory.
5. Copy `ci/coding-quality.yml` to `.github/workflows/coding-quality.yml` only
   after adapting paths, tool versions, supported Python version, and exclusions.
   It expects `.clang-format` and `ruff.toml` at the target repository root.
   Installation or configuration failures remain blocking; formatting and lint
   findings are advisory and retained in logs and the job summary.
6. Add repository-specific compilation database generation and separate C/C++
   translation-unit selection before integrating clang-tidy. Define changed-code
   selection, baseline handling, required checks, and exception review before
   enabling a mandatory quality gate.

The workflow selects the GitHub-hosted Ubuntu 26.04 image and explicitly selects
Python 3.14 with `actions/setup-python`. This selection is independent of the OS
default interpreter. The Ruff template retains `target-version = "py311"` as its
minimum source-compatibility target; it does not select the interpreter running
Ruff or require CI to run on Python 3.11. This target is a supplied starter
assumption, not a minimum Python version established by the standard. Ruff 0.8.6
does not accept `py314` as a target, so changing the compatibility target would
require a separate tooling and source-support decision.

The workflow runs Ruff only on tracked `.py` files. It reports empty Python and
native selections as checks not run. An empty result is not source-policy compliance.

## What the templates do not establish

- clang-tidy is a C++ starter. Its header filter recognizes the named directories
  in relative and absolute paths, but target layouts must be reviewed. Language
  extensions and C-specific checks need repository decisions.
- The cognitive-complexity check at 15 is an advisory supplied setting. It does
  not measure or enforce the policy's cyclomatic-complexity target of 15.
- Naming checks cover only the categories configured in `.clang-tidy`; they do
  not enforce every type, constant, or macro rule in the policy.
- EditorConfig encoding is not an ASCII source scanner. Ruff formatting is not
  a guarantee that every line is at most 100 columns.
- No compiler supplement, C1-C4 definitions, safety certification, or standards
  compliance is created by this package. The ace-cc supplement mentioned in the
  supplied standard is not included here.

## Source and integration changes

Source: user-supplied `Project-KISS-coding-standard-v1.0.tgz`, SHA-256
`c31a243584a8e9b57a8e30f39b681dce2a6dd89da93976c278a81d4ea2221391`.

All eight supplied files were already English and ASCII. No Japanese translation
was needed. `CODING_STANDARD.md`, `AGENT_CODING_POLICY.md`, `.editorconfig`, and
`ruff.toml` retain their supplied content after the authorized KOL headers.
Integration changes are:

- Remove unsupported `AlignAfterOperator` from `.clang-format`; preserve
  `AlignOperands`. clang-format 18.1.8 rejects the original key.
- Adjust the clang-tidy header filter to recognize absolute paths, and label the
  C++ scope and cognitive-complexity distinction in comments.
- Pin reference formatter/linter versions in CI, check root configuration,
  select tracked files safely, make format/lint findings advisory, and report
  empty selections and missing analysis stages explicitly. clang-tidy is not
  installed by a job that does not run it.
- Select Ubuntu 26.04 and Python 3.14 explicitly for the workflow while retaining
  the supplied Ruff source-compatibility target.
- Expand this README with integration commands, compatibility notes, and limits.

The supplied package had no copyright or license declaration. KOL v1 application
and I-plusplus Inc. copyright identification were authorized for this first-party
package. Each file now carries the appropriate SPDX comment header. The
[licensing scope](../../../docs/licensing/README.md) lists the exact paths, and
NOTICE identifies the added policies and templates. Both complete license copies
remain unchanged. This authorization does not license external tools, actions,
dependencies, or other third-party material.

## Scope

Common policy applies to Project-KISS projects. Repository-specific ABI,
compiler, and safety rules belong in supplements. Existing technical debt is not
automatically a blocker.
