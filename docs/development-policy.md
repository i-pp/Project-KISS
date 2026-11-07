# Shared development policy

This policy applies to work under Project-KISS and Project-AceIS, including the `Project-KISS`, `AceIS`, `ace`, `paul`, `gene`, and `peter` repositories in the `i-pp` organization.

## English project communication

Use English for project and repository descriptions, documentation, issue and pull request titles and bodies, review comments, and commit messages. A Japanese version is not required.

Existing design sources may be retained for provenance while an English translation is reviewed. New contributions and the default reading path should be in English. Preserve the meaning of historical design decisions and the distinction between policy, proposal, deferred work, and verified implementation when translating.

Do not rewrite published commit history to change its language. Use English for new commits, including merge and squash commit messages.

## Current compiler implementation direction

Implement the project compiler in C/C++. Python is acceptable for the current local PoC, but only the C/C++ compiler implementation is to be pushed as project compiler source. This distinction does not turn a successful Python prototype into a completed C/C++ implementation.

A compiler for Rust is also in scope. Rust is a language to compile, not a change to the C/C++ implementation-language decision. Define the supported Rust features and validation stages separately; inclusion in scope is not a claim of completed Rust support.

These are current development directions. Keep the preserved fifth-edition design source and its English translation faithful to their historical content rather than silently inserting later decisions into the translation.

## ASCII-only code

### Project-maintained source

Source maintained by this project must contain ASCII bytes only. This includes identifiers, comments, docstrings, string literals, executable scripts, tests, and code examples. Write human-readable text in English. AI-generated code accepted into project-maintained source follows the same rule; its origin is not an exemption.

### External dependencies and generated files

Keep external dependencies and vendored material identifiable and preserve their provenance and licensing. Do not directly rewrite upstream source or generated files merely to force an ASCII scan to pass. Correct project-controlled generators or their inputs and regenerate outputs where appropriate. Generated source maintained as part of the project must still meet the ASCII rule.

Material outside the project-maintained source scope must be explicitly identified, not silently skipped. Record the paths, origin or generator, reason, responsible maintainer, and update or regeneration procedure for each exclusion. An exclusion must not be used to relabel first-party source and evade this rule. Any exception for non-ASCII project-maintained source requires a separate explicit decision; this policy grants none.

### Unicode behavior and test data

The restriction is on source text, not runtime behavior. Unicode processing remains allowed. In source code, represent non-ASCII characters using ASCII escape sequences or numeric code points appropriate to the language, including tests for Unicode behavior.

Separately identified fixture files may contain the exact Unicode bytes that a test needs because they are data, not source code. Do not normalize or transliterate those bytes, binary assets, or user data to satisfy the source-text check. A fixture designation does not exempt non-ASCII literals embedded in source code.

### Documentation

Use English for documentation and ASCII-only text inside code examples. The source-code rule does not impose an ASCII byte restriction on every prose document. Historical design originals may be retained for provenance while the English version is the default reading path.

## Verification

Before opening or updating a pull request:

1. Check the title, body, proposed commit messages, and any changed project metadata for English.
2. Scan every changed project-maintained source file for non-ASCII bytes, including comments and string literals. Include new languages and extensionless scripts; an extension-only scan is not sufficient by itself. Review any exclusion records alongside the change.
3. Run the repository's normal technical checks. An ASCII scan does not establish correctness, security, or test coverage.
4. Review technical meaning and editorial clarity separately when preparing technical articles. Passing a technical check does not by itself make prose useful or ready to publish.

The following command checks explicitly selected, repository-relative source files and rejects an empty file list. It is a manual source-text check, not automatic file discovery, a build command, or a Quick Start. Replace the example paths with the full source-file scope of the change; omitted files are not checked:

```sh
python3 - src/example.c tests/test_example.py <<'PY'
from pathlib import Path
import sys

if len(sys.argv) < 2:
    print("error: provide at least one source file", file=sys.stderr)
    raise SystemExit(2)

failed = False
for name in sys.argv[1:]:
    path = Path(name)
    for line_number, line in enumerate(path.read_bytes().splitlines(), 1):
        if any(byte > 127 for byte in line):
            print(f"{path}:{line_number}: non-ASCII source text")
            failed = True
raise SystemExit(1 if failed else 0)
PY
```

## Follow-up: automated source selection and CI

Automatic enforcement belongs in each implementation repository when source code is introduced. It is not implemented by this document or its manual command. The follow-up must:

- Derive changed paths from Git, including added, modified, and renamed files, using a defined comparison base and filename-safe handling.
- Classify project-maintained source, extensionless scripts, code examples, dependencies, generated files, and fixtures using an explicit reviewed scope. New or unclassified file types must not silently escape review.
- Record and check exclusions, and distinguish a confirmed source-free change from a failure to discover source files.
- Run the source-text check in CI and test ASCII source, non-ASCII comments and literals, escaped Unicode, Unicode fixtures, missing inputs, and an empty selection.

Adding this CI is follow-up work, not a prerequisite for reviewing this documentation-only PR. Empty repositories do not need placeholder implementations or duplicate policy documents.

Project-KISS remains a documentation-only repository. Implementations and experiment logs belong in their designated repositories.
