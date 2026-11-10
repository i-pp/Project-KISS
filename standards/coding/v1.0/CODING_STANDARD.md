<!--
SPDX-FileCopyrightText: 2026 I-plusplus Inc.
SPDX-License-Identifier: LicenseRef-KOL-v1
-->

# Project-KISS Coding Standard

**Version 1.0 - Draft**

**Keep It Simple, Stupid!!**

*Write code to be understood, not to be admired.*

This is the common norm for new and changed Project-KISS code. Automated
enforcement is incomplete and adoption must be verified in each repository.
Follow the [shared development policy](../../../docs/development-policy.md)
and applicable repository supplements alongside it.

MUST means required; SHOULD means preferred unless a reason is recorded; MAY
means permitted. Structural thresholds are review triggers, not absolute limits.

## 1. Philosophy: Keep It Simple, Stupid!!

All Project-KISS code MUST follow the KISS principle. This does not simply mean
writing short code. Complex expressions, packing work onto one line, and
unnecessary abstraction can make shorter code harder to understand.

Simple code lets a reader readily understand its purpose, control flow, data
changes, and side effects. Code is read more often than it is written. Reduce
the burden on readers, reviewers, and maintainers before optimizing for the
writer's convenience.

**Simplicity is not the absence of complexity. It is the deliberate management of complexity.**

When complexity is necessary, separate it into units that can be understood and
verified rather than hiding it.

### 1.1 Simplicity over cleverness

**Write code to be understood, not to be admired.**

- Prefer clarity over brevity and explicit behavior over implicit behavior.
- Avoid unnecessary abstraction and combining unrelated responsibilities.
- Minimize the background knowledge needed to understand the code.
- Make intent and side effects clear.
- Do not express a simple operation in a complicated way.

Before accepting complex code, reconsider its algorithm, data structures, and
separation of responsibilities.

### 1.2 Simplicity is not minimalism

Reducing line count is not a goal in itself. Useful line breaks, explicit
branches, meaningful variables, and separate functions can make longer code
easier to understand. Removing unnecessary code is different from omitting
necessary explanation or structure.

### 1.3 Rules must also be simple

The coding standard itself follows KISS. Rules reduce repeated judgment calls
and help humans and AI agents produce consistent quality.

- Be able to explain each rule's purpose.
- Make compliance objectively assessable where possible.
- Verify automatable rules with tools.
- Keep exceptions to the minimum needed and avoid conflicting rules.

Reconsider a rule if it adds complexity without improving the code.

## 2. Core engineering principles

### 2.1 Single responsibility

Files, functions, classes, and modules each have a clear responsibility. Do not
combine independent responsibilities in one implementation.

### 2.2 Explicit behavior

Make intent, control flow, data ownership, and side effects clear. Avoid implicit
state changes and dependence on an unexpected order of execution.

### 2.3 Readability first

Prioritize readability. Private abbreviations and clever syntax must not force
readers to infer what a straightforward expression would make clear.

### 2.4 Testability by design

Structure code so it can be verified independently where possible. A design
that requires recreating a large environment for a small test warrants a review
of its responsibility boundaries.

### 2.5 Determinism and reproducibility

Aim for reproducible results from the same inputs, configuration, and
toolchain. Where nondeterminism is necessary, state its conditions and how to
verify the behavior.

### 2.6 Traceability

Keep source, tests, generated artifacts, CI results, and commits traceable to one
another. Record why a change was made and the results of verification.

### 2.7 AI accountability

AI-generated code follows the same rules as human-written code. AI generation,
modification, or review does not replace quality assurance.

## 3. C and C++ coding style

### 3.1 Formatting

Project-KISS does not adopt a company's or another project's style wholesale.
This standard is authoritative; formatters are implementation tools.

- Use four spaces for indentation, never tabs.
- Use LF line endings and UTF-8 encoding. Maintained source still MUST be
  ASCII-only under the shared development policy.
- Target 100 columns and prefer meaningful line breaks.
- Do not reformat unrelated code merely to match a formatter.

### 3.2 Function scope

The opening brace of a function definition MUST be on the next line.

Allowed:

```cpp
void process_data(int value)
{
    execute(value);
}
```

Not allowed:

```cpp
void process_data(int value) {
    execute(value);
}
```

### 3.3 Control statement braces

For control statements, Allman placement, K&R placement, and mixtures of the two
are permitted. Indentation and block structure MUST remain clear.

```cpp
void process_data(int value)
{
    if (value > 0)
    {
        execute(value);
    } else if (value == 0) {
        execute(value);
    }
    else execute(value);
}
```

Make control flow easy to see rather than treating one brace placement as the
only acceptable form. These permissions do not weaken the function-brace rule.

### 3.4 Single-line control statements

When a control statement and its body share a line, the body MUST contain only
one simple action. A call, a simple return, an increment, or a simple assignment
can qualify.

Allowed:

```cpp
if (ready) execute();

if (ready) return value;

if (ready) ++count;

if (ready) result = value;
```

Not allowed:

```cpp
if (ready) if (valid) execute();

if (ready) return flag ? a : b;

if (ready) prepare(), execute();
```

Put a compound action on a separate line from the control statement. For
example, the conditional operator is permitted in this form:

```cpp
if (ready)
    return flag ? a : b;
```

### 3.5 Conditional operator

The conditional operator `?:` is permitted, but MUST NOT appear in a body that
shares a line with its control statement.

Allowed:

```cpp
result = flag ? a : b;

if (ready)
    return flag ? a : b;
```

Not allowed:

```cpp
if (ready) return flag ? a : b;
```

Avoid deeply nested conditional operators and expressions that obscure meaning.

### 3.6 Comma operator

The comma operator MUST NOT be used except in a `for` update clause to update
multiple loop variables simply.

Allowed:

```cpp
for (int a = 0, b = 0; a < count; ++a, ++b)
{
    process(a, b);
}
```

Not allowed:

```cpp
++a, ++b;

prepare(), execute();

return (prepare(), result);
```

Commas separating function arguments, declarations, or initializer-list elements
are not comma operators and are outside this rule. If a solution appears to
require another comma operator, reconsider its algorithm or responsibilities.

### 3.7 One action per line

Do not pack independent actions onto one line.

Allowed:

```cpp
prepare();
execute();
cleanup();
```

Not allowed:

```cpp
prepare(); execute(); cleanup();
```

The single-line controls in Section 3.4 and the `for` update in Section 3.6 are
the limited exceptions described above, not permission to compress other work.

## 4. Structural quality

Monitor structural complexity continuously. Initial review thresholds are:

| Metric | Guideline |
| --- | --- |
| File length | At most 500 lines |
| Function length | At most 60 lines |
| Cyclomatic complexity | At most 15 |
| Function parameters | At most 5 |
| Nesting depth | At most 4 levels |

These are design warnings, not absolute limits that require mechanical
splitting. Record the reason, owner, and verification results for exceptions. Retain
the existing requirement to document a decomposition decision when making a
substantial change to a file over 1000 lines, with an owner for the exception.

## 5. Testing and verification

Design tests to detect incorrect implementations, not merely to confirm the
implementation being tested.

- Cover positive, negative, and boundary cases.
- Do not derive expected results from the same logic as the implementation.
- Record a reason and meaningful diff for golden-file changes; never regenerate
  goldens merely to make a failure disappear. Verify the change independently.
- Generate artifacts reproducibly.
- Distinguish coverage from test quality.
- Never describe an unverified condition as verified.

Use independent oracles, property tests, fuzzing, and regression cases where
valuable, and prefer sanitizers such as ASan/UBSan for applicable native code. Follow
the shared CTest, coverage, and evidence requirements. C1-C4 and MC/DC claims
require explicit metric definitions and scoped evidence; no numbering scheme
or certification is established by this standard.

## 6. Automated enforcement

Automate application of the standard where possible. The mechanisms below are
requirements and intended responsibilities, not a claim that every check
already exists.

### 6.1 clang-format

Use `BasedOnStyle: None` and define Project-KISS formatting settings explicitly.
For the reference clang-format 18.1.8 template, `DisableFormat: false` is
essential: the `None` preset otherwise disables formatting.

clang-format alone cannot express every permitted brace arrangement or decide
whether a single-line body is one simple action. The supplied template chooses
one conservative normalization: next-line function braces, attached control
braces, and expanded single-line controls. Other forms permitted by Section 3
remain compliant even when the formatter proposes a change. A formatter diff
alone MUST NOT be treated as a violation of those permissions.

Use the repository-pinned formatter and configuration for its selected scope.
Resolve conflicting local settings before introducing a required gate.

### 6.2 clang-tidy

Use static analysis to find dangerous constructs, complexity, and unused code.
Do not enable a default check without considering whether it contradicts this
standard. In particular, the template does not require braces around every
control body. Distinguish C-specific from C++-specific checks.

### 6.3 KISS Lint

A dedicated KISS Lint is intended to check project-specific syntax:

- Function opening-brace placement.
- Single-line control-body restrictions.
- Comma-operator use.
- Multiple independent actions on one line.
- Inappropriate compression of control flow.

KISS Lint is not implemented in this package. These rules require review until
a validated checker is available. Do not substitute a formatter or a text
pattern for a verified syntax-aware checker and claim full enforcement.

### 6.4 Continuous integration

Detect violations in new and changed code. Track pre-existing violations as a
baseline without demanding unrelated bulk formatting or wholesale rewrites.

The supplied CI file is an advisory whole-tree baseline starter, not a
changed-code gate. It does not run KISS Lint, clang-tidy, builds, tests, coverage,
or automatic ASCII source discovery. Follow the package README before adoption.

## 7. AI development policy

Before making a change, agents MUST understand the existing design and
implementation.

- Prefer reuse and avoid unnecessary abstraction.
- Do not put unrelated responsibilities into one file.
- Add the necessary tests for new code.
- Do not change unrelated files.
- Do not assume a golden update is justified.
- Report the reason for a change, verification results, and residual risks.

When AI produces complex code, first ask whether the complexity is necessary.
The [agent policy](AGENT_CODING_POLICY.md) gives the review and reporting steps.

## 8. Final principle

**Keep It Simple, Stupid!!**

Write simple code. Build simple structures. Use simple, consistent rules. Then
verify them mechanically wherever a validated check exists.

**Complexity must be justified. Simplicity must be intentional.**

## 9. Retained repository requirements

The revised norm does not remove compatible requirements from the earlier v1.0
package:

- Respect documented dependency direction, avoid cycles, and search for reusable
  implementations before introducing duplicates.
- Separate generated files from handwritten sources and record provenance,
  source inputs, outputs, regeneration command, generator version, and determinism
  limits. Generation scripts MUST declare their inputs, outputs, invocation,
  and determinism constraints.
- Isolate platform-specific code and declare supported targets.
- Use `PascalCase` for types, `snake_case` for functions and variables,
  `kPascalCase` for constants, and `UPPER_SNAKE_CASE` for macros. Use
  type-attached pointer and reference syntax.
- Document ABI, ownership, lifetime, alignment, and error contracts at C/C++
  boundaries. Prefer RAII and explicit ownership in C++; avoid unexplained
  owning raw pointers.
- Run pinned Ruff format/lint on maintained Python sources. Use Python for
  tooling, fixtures, build orchestration, and verification without silently
  relocating compiler core logic into scripts.
- Validate configuration JSON against a schema where a stable contract exists.
  Record what each fixture exercises. For byte-compared serialization, define
  key ordering, numeric representation, whitespace, and newlines; do not reorder
  semantically ordered arrays.
- Relate CI evidence to the exact commit, environment, tools, test outcomes, and
  artifact digests. Disclose untested paths and record exceptions in a PR or
  tracked decision.

Security, correctness, and ABI regressions, unsubstantiated golden replacement,
and broken required tests remain blockers. Activate new/changed-code gates only
after establishing tool versions, baseline handling, and reviewed exceptions.
Legacy structural debt is advisory unless it is a critical risk directly
affected by the change. Then pay down debt with traceable evidence.

Repository-specific IR, diagnostics, ABI, code-generation, golden, and safety
requirements belong in separately versioned supplements. The ace-cc supplement
is not supplied here. Do not claim certification or compliance without scope
and evidence.
