# KISS Open License Version 1.0 (KOL-v1)
#
# SPDX-FileCopyrightText: 2026 I-plusplus Inc.
# SPDX-License-Identifier: LicenseRef-KOL-v1
#
# Copyright remains with its respective holders; original copyright and attribution notices must be preserved.
# Contributors may add copyright notices for their own original modifications.
# Distributed modifications must be identified as required by Section 4(c) of KOL-v1.
#
# Use, modification, distribution, and incorporation into commercial or proprietary software are permitted
# without license fees or source disclosure, subject to all terms of the complete KOL-v1 license.
#
# Contributors grant the patent permissions stated in KOL-v1. Outputs are not covered merely because a
# KOL-licensed tool produced them; embedded licensed material remains subject to applicable license terms.
#
# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OR LIABILITY TO THE EXTENT PERMITTED BY APPLICABLE LAW.
#
# This header is a summary, not a separate license or an amendment to KOL-v1.
# All terms and conditions of KOL-v1 apply. See the accompanying LICENSE file for the complete license text.

"""Validate the documentation repository's baseline without network access."""

import re
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r"!?\[[^\]\n]*\]\(<?([^\s)>]+)>?(?:\s+[\"'][^\n]*[\"'])?\)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def documentation_links(text):
    """Yield inline Markdown link destinations outside fenced code blocks."""
    fence = None
    for line in text.splitlines():
        match = FENCE.match(line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker[0]
            elif marker[0] == fence:
                fence = None
            continue
        if fence is None:
            yield from LINK.findall(line)


def check(root):
    """Return baseline errors; absence of mandatory content is a failure."""
    errors = []
    required = [
        "README.md",
        "LICENSE",
        "NOTICE",
        "LICENSES/LicenseRef-KOL-v1.txt",
        "standards/coding/v1.0/CODING_STANDARD.md",
        "standards/coding/v1.0/AGENT_CODING_POLICY.md",
        "standards/coding/v1.0/templates/ruff.toml",
    ]
    for name in required:
        path = root / name
        if not path.is_file() or not path.read_bytes().strip():
            errors.append(f"Missing or empty required file: {name}")
    license_copy = root / "LICENSES/LicenseRef-KOL-v1.txt"
    if (
        (root / "LICENSE").is_file()
        and license_copy.is_file()
        and (root / "LICENSE").read_bytes() != license_copy.read_bytes()
    ):
        errors.append("LICENSE and LicenseRef copy differ")
    documents = sorted(root.rglob("*.md"))
    for document in documents:
        for target in documentation_links(document.read_text(encoding="utf-8")):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            path = (document.parent / unquote(url.path)).resolve()
            if not path.is_relative_to(root.resolve()) or not path.exists():
                errors.append(f"{document.relative_to(root)}: missing local target {target}")
    for config in root.rglob("*.toml"):
        try:
            tomllib.loads(config.read_text(encoding="utf-8"))
        except (tomllib.TOMLDecodeError, UnicodeError) as error:
            errors.append(f"{config.relative_to(root)}: {error}")
    for source in [*root.glob("scripts/*.py"), *root.glob("tests/*.py")]:
        data = source.read_bytes()
        if not data.isascii():
            errors.append(f"Non-ASCII maintained source: {source.relative_to(root)}")
        try:
            compile(data, str(source), "exec")
        except (SyntaxError, ValueError) as error:
            errors.append(f"{source.relative_to(root)}: {error}")
    return errors


def main():
    """Check this checkout and report failure rather than silently skipping."""
    root = Path(__file__).resolve().parents[1]
    errors = check(root)
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Baseline documentation checks: {'FAIL' if errors else 'PASS'}")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
