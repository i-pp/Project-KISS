<!--
SPDX-FileCopyrightText: 2026 I-plusplus Inc.
SPDX-License-Identifier: LicenseRef-KOL-v1
-->

# Baseline CI

The root workflow runs on every pull request, every push to main, merge groups,
and manual dispatch. It does not use path filters or ignore failing commands.
The stable job name is **Baseline checks**. Adding this workflow does not
configure branch protection or make that check mandatory.

Run the same checks locally with Python 3.11 or newer:

```sh
python3 -B tests/test_baseline.py
python3 -B scripts/check_baseline.py
```

The minimum gate verifies required documentation, identical license copies,
local inline Markdown link targets outside fenced examples, TOML syntax, and
ASCII/Python syntax for the checker and its tests. Negative fixtures verify that
missing files, mismatched licenses, broken links, invalid configuration, and
invalid source fail validation. CI uses the Python supplied by Ubuntu 24.04;
the first step reports its actual version.

This is a documentation-repository baseline, not compiler testing, structural
coverage, complete Markdown parsing, external URL checking, or full enforcement
of the coding norm. Reference-style links, raw HTML links, and fragment anchors
are outside this first check. The workflow under
[the coding standard](../standards/coding/v1.0/ci/coding-quality.yml) remains a
starter for implementation repositories, not this repository's active CI.

