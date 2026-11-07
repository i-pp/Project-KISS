# Shared development policy

This policy applies to work under Project-KISS and Project-AceIS, including the `Project-KISS`, `AceIS`, `ace`, `paul`, `gene`, and `peter` repositories in the `i-pp` organization.

## English project communication

Use English for project and repository descriptions, documentation, issue and pull request titles and bodies, review comments, and commit messages. A Japanese version is not required.

Existing design sources may be retained for provenance while an English translation is reviewed. New contributions and the default reading path should be in English. Preserve the meaning of historical design decisions and the distinction between policy, proposal, deferred work, and verified implementation when translating.

Do not rewrite published commit history to change its language. Use English for new commits, including merge and squash commit messages.

## ASCII-only code

Source code must contain ASCII bytes only. This includes identifiers, comments, docstrings, and string literals, as well as executable scripts and code examples. Write human-readable text in English.

The restriction is on source text. It does not prohibit handling Unicode data at runtime. When a test or implementation needs a non-ASCII character, represent it using ASCII escape sequences or numeric code points appropriate to the language.

Do not apply an ASCII conversion to binary assets or user data. The code rule is not a requirement to byte-restrict every document or external dependency. Do not modify vendored material without checking its provenance and update process.

## Verification

Before opening or updating a pull request:

1. Check the title, body, proposed commit messages, and any changed project metadata for English.
2. Scan every changed source file for non-ASCII bytes, including comments and string literals. Include new languages and extensionless scripts; an extension-only scan is not sufficient by itself.
3. Run the repository's normal technical checks. An ASCII scan does not establish correctness, security, or test coverage.
4. Review technical meaning and editorial clarity separately when preparing technical articles. Passing a technical check does not by itself make prose useful or ready to publish.

The following command checks explicitly selected, repository-relative source files. It is a source-text check, not a build command or a Quick Start. Replace the example paths with the full source-file scope of the change:

```sh
python3 - src/example.c tests/test_example.py <<'PY'
from pathlib import Path
import sys

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

When implementation repositories gain source code, include the source-text check in their normal automated checks and keep its file scope explicit. Empty repositories do not need placeholder implementations or duplicate policy documents.

Project-KISS remains a documentation-only repository. Implementations and experiment logs belong in their designated repositories.
