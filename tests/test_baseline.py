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

"""Exercise baseline validation against independent temporary repositories."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts/check_baseline.py"
SPEC = importlib.util.spec_from_file_location("baseline", MODULE)
baseline = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(baseline)


class BaselineTests(unittest.TestCase):
    """Verify positive and negative paths without changing repository content."""

    def setUp(self):
        """Create the minimum valid fixture."""
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for name, text in {
            "README.md": "[Policy](standards/coding/v1.0/CODING_STANDARD.md)",
            "LICENSE": "sample license\n",
            "LICENSES/LicenseRef-KOL-v1.txt": "sample license\n",
            "NOTICE": "sample attribution",
            "standards/coding/v1.0/CODING_STANDARD.md": "# Coding",
            "standards/coding/v1.0/AGENT_CODING_POLICY.md": "# Agent",
            "standards/coding/v1.0/templates/ruff.toml": "line-length = 100",
        }.items():
            self.write(name, text)

    def write(self, name, text):
        """Write a fixture file, creating its parent directory."""
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_valid(self):
        self.assertEqual(baseline.check(self.root), [])

    def test_empty_repository(self):
        with tempfile.TemporaryDirectory() as empty:
            self.assertTrue(baseline.check(Path(empty)))

    def test_missing_required_file(self):
        (self.root / "NOTICE").unlink()
        self.assertTrue(baseline.check(self.root))

    def test_empty_required_file(self):
        self.write("NOTICE", "  ")
        self.assertTrue(baseline.check(self.root))

    def test_license_mismatch(self):
        self.write("LICENSE", "different")
        self.assertIn("LICENSE and LicenseRef copy differ", baseline.check(self.root))

    def test_missing_link(self):
        self.write("README.md", "[Broken](absent.md)")
        self.assertTrue(baseline.check(self.root))

    def test_parent_escape(self):
        self.write("README.md", "[Outside](../outside.md)")
        self.assertTrue(baseline.check(self.root))

    def test_external_and_fragment(self):
        self.write("README.md", "[Web](https://example.com) [Section](#section)")
        self.assertEqual(baseline.check(self.root), [])

    def test_fenced_example(self):
        self.write("README.md", "```text\n[x](missing.md)\n```")
        self.assertEqual(baseline.check(self.root), [])

    def test_encoded_local_link(self):
        self.write("a b.md", "# Target")
        self.write("README.md", "[Space](a%20b.md)")
        self.assertEqual(baseline.check(self.root), [])

    def test_invalid_toml(self):
        self.write("bad.toml", "[invalid")
        self.assertTrue(baseline.check(self.root))

    def test_invalid_python(self):
        self.write("scripts/bad.py", "if")
        self.assertTrue(baseline.check(self.root))

    def test_non_ascii_python(self):
        self.write("scripts/bad.py", "# " + chr(0x3042))
        self.assertTrue(baseline.check(self.root))


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(BaselineTests)
    if suite.countTestCases() == 0:
        raise SystemExit("No tests discovered")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(not result.wasSuccessful() or bool(result.skipped))
