<!--
SPDX-FileCopyrightText: 2026 I-plusplus Inc.
SPDX-License-Identifier: LicenseRef-KOL-v1
-->

# Project-KISS Agent Coding Policy v1.0

Applies to Codex and other coding agents.

1. Inspect architecture, dependencies, ownership, and nearby tests before editing.
2. Search for reusable code and follow the applicable coding standard and repository supplement.
   Read the KISS philosophy before applying individual syntax rules. Prefer
   understandable purpose, control flow, data changes, and side effects over
   shorter code or clever abstraction.
3. Keep changes scoped; do not bundle unrelated formatting or refactors.
4. Add or update independent tests for changed behavior, including failure paths.
5. Never blindly accept regenerated goldens; explain the change and review diffs.
6. Preserve existing contracts and do not modify security/ABI/public interfaces without explicit justification.
7. Run available format, lint, build, and test checks; report exact commands and results.
   A formatter diff alone is not a violation of policy-permitted mixed control
   braces or simple single-line controls. Review the function-brace, single-line
   action, conditional-operator, comma-operator, and one-action-per-line rules
   directly until a validated KISS Lint exists. Do not claim that it ran.
8. Distinguish facts, assumptions, and unverified conditions. Never claim unrun checks passed.
9. Summarize changed files, risks, evidence, and follow-up issues in the PR.
10. Treat legacy warnings as baseline debt unless directly introduced or worsened; do not stop unrelated work.
    Complexity thresholds trigger design review, not mechanical splitting.

If code is complex, reconsider the algorithm, data structures, and responsibility
boundaries before adding another abstraction. Record the reason and verification
results when necessary complexity or a rule exception remains.

No secrets, tokens, or credentials in source, logs, fixtures, or PR descriptions.
