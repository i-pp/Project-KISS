# AceIS Design Update: acc, Native Sysroot, and Ace-Core

- **Reference date:** 2026-11-07
- **Status:** Design draft, not an implementation or performance claim
- **Baseline:** [Version 5 English translation](Project-KISS_design_v5_draft.en.md)
- **Scope:** Later compiler, runtime, compatibility, and verification directions

This update records the directions discussed after Version 5. It takes precedence only where it explicitly updates that draft. All other Version 5 content remains in place. The preserved fifth-edition source and its English translation remain unchanged.

**[Policy]** identifies a direction stated by the designer, **[Proposal]** identifies a validation or implementation approach still to review, **[Open]** identifies an unresolved contract, and **[Unverified goal]** identifies an outcome requiring evidence. None of these labels means a feature has been implemented.

## Current Priorities

1. Advance acc toward a working C/C++ compiler implementation on a Linux host, generating AIR and then a SIMD-native binary for one selected target.
2. Define the minimum AceIS-native sysroot and component contract before expanding Linux compatibility.
3. Explore Ace-Core as a Linux-hosted PoC with a minimal dynamic loader and a project-owned initial memory-mapping implementation.
4. Include automated tests, measured coverage, and CI with every new development item. The goal is 100% for each project-defined C1-C4 metric, once definitions and measurement feasibility are established.

These are development priorities, not evidence that a complete compiler, native sysroot, runtime, or compatibility layer already exists. Implementation and experiment records belong in their designated repositories, not this documentation-only repository.

## 1. acc: Driver, AIR, and Target Shared Objects

### 1.1 Responsibilities

**[Policy]** Use ace-cc / acc for the compiler direction. The acc executable selects the target and generates AIR. Target-dependent parts are managed as shared-object components (SOs) and dynamically loaded, so those parts can be versioned and upgraded separately.

The PAUL / GENE / PETER responsibilities in Version 5 remain useful functional boundaries. Having acc own the AIR-generation path does not require all parsing and lowering code to be a single inseparable module. **[Open]** Whether AIR generation is linked into acc or exposed as a development-friendly SO remains undecided.

**[Policy]** The driver accepts CPU and architecture selection for cross compilation and selects corresponding target components to produce SIMD-native output. Linux as a target environment is an option; it is not the definition of the AceIS-native target. Do not confuse the Linux host running acc with the environment in which its generated binary will run.

**[Open]** Target identity and command-line syntax need definition. The suggested `x86_64-kiss-aceis-unknown` spelling was exploratory, not an adopted triple or public interface. Architecture, ISA features, ABI, output format, and sysroot must be unambiguous even if the project chooses a representation other than a conventional triple.

**[Proposal]** Test that a target backend loaded by acc is compatible with the host executable, while its generated code obeys the selected target contract. For example, an AArch64 code generator loaded by an amd64 Linux acc is a host-loadable SO; it does not become an AArch64 host library merely because it emits AArch64 code.

### 1.2 Repository and Build Direction

**[Policy]** Plan component submodules and separately managed target repositories, with granularity such as amd64, AArch64, armv8-a, and armv8.1-a. The selected repositories build into the SOs used by the driver. Target-specific linker scripts are part of the toolchain inputs.

**[Open]** The repository matrix, shared ISA-family code, manifest format, dependency pinning, and workspace selection tool remain to be specified. The desired workflow downloads and builds only the repositories needed for a selected target. No particular `repo`-style tool or other workspace manager is mandated by this update, and this document does not create empty repositories or submodules.

**[Policy]** First aim for Linux-hosted acc -> AIR -> amd64 SIMD-native output. AArch64 is an acceptable first alternative if it makes the initial implementation and verification easier. Choose one target for the first milestone; do not turn support for both into a prerequisite. QEMU is an available validation candidate when the target differs from the host.

**[Open]** An SO boundary alone does not define independent upgrade safety. Before independently versioned components are used, specify plugin entry points, AIR and API/ABI compatibility, resource ownership, error handling, dependency resolution, and rejection of incompatible versions. The exact ABI and versioning scheme remain undecided.

The [shared development policy](development-policy.md) continues to govern C/C++ implementation, the distinction between a local Python PoC and project compiler source, English communication, and ASCII-only source. The local-LLM implementation experiment in Version 5 Section 10.9 also remains in effect.

## 2. AceIS-Native Sysroot Before Compatibility Expansion

**[Policy]** Treat the AceIS-native sysroot as the foundation for native development. Define the native API/ABI and SIMD-native runtime on their own terms. POSIX and Linux interfaces are compatibility facilities that must remain removable, rather than requirements imposed on every native component.

**[Policy]** Native builds and eventual self-builds on an AceIS host are goals for the components. The current starting point is a Linux development host, not a completed self-hosting system.

**[Proposal]** Start the sysroot contract with only what the first native component needs: ABI and interface definitions, minimum startup and compiler-support code, runtime entry points, and link/load metadata. Keep compile-time sysroot contents distinct from runtime SO placement and update management.

**[Open]** Specify the first target's calling convention, data layout, object format, public SIMD value representation, memory ownership, entry points, and minimum service interfaces. The native libc surface and implementation are not decided. Do not silently substitute the host's glibc ABI for the native ABI.

**[Policy]** A future compatibility development surface may include POSIX/Linux headers and thin `libposix.so` / `liblinux.so` wrappers. Keep those clearly separate from the native contract and optional to native builds. Removing compatibility must not require native code to acquire a POSIX dependency.

**[Unverified goal]** A native SIMD runtime should avoid compatibility overhead. This is a performance objective requiring measurements, not a promise of zero overhead for arbitrary programs.

## 3. Ace-Core: Minimal Loader and Startup Mapping

### 3.1 Core and Optional Services

**[Policy]** Ace-Core is to be kept as small as possible, with the dynamic loader as its core mechanism. Map the native startup SOs that make up AceIS ahead of their use during startup. Load compatibility facilities later, only when needed.

**[Policy]** Put the compatibility ELF loader, compatibility dynamic linker, Linux syscall wrappers, and glibc-compatible ABI support in external SO components rather than incorporating all of them into the minimal Core. These components can be loaded and shared as required. Their exact SO grouping and sharing model are still open.

This refines the implementation direction without turning the loader into the ACE reasoning component. **[Open]** The mapping from the name Ace-Core to Version 5's logical AceIS Core / A-Nexus / Abiss layers, and the placement of observation, reasoning, and system-control services, still need an explicit contract. Do not infer that the minimal loader must embed all those higher-level services.

**[Open]** Define the bootstrap boundary: the minimum mapping, relocation, symbol resolution, and initialization support that must exist before external SOs can provide services. Pre-mapping a component is not sufficient evidence that its dependencies, relocations, permissions, or startup order are correct.

### 3.2 Initial Linux-Hosted PoC

**[Policy]** Explore a Linux application implementing the smallest useful dynamic loader together with a project-owned initial mmap facility for that loader. This is an early Ace-Core PoC, not a replacement kernel or a completed native memory subsystem.

**[Open]** Specify whether the initial mmap facility manages a reserved region, wraps Linux mapping primitives, or uses another explicitly bounded mechanism. While it is a Linux application, virtual-memory protection and backing still depend on the host or guest Linux kernel. Do not present a wrapper or allocator as a completed independent VM implementation.

**[Proposal]** Make the first observable outcome loading one controlled test component, resolving an entry point, calling it through the defined interface, and verifying the returned result and resource cleanup. Include mapping failures, invalid images, alignment and size checks, dependency failures, and initialization failures in its test plan. Keep Linux compatibility, live state migration, and full self-hosting outside this first outcome.

**[Policy]** QEMU or Renode may be used to make trials safer and repeatable where the selected machine model supports the PoC. **[Open]** Choose and document the actual supported execution mode and guest or machine configuration. A simulator name alone is not an isolation guarantee, and neither simulator is a mandatory dependency for every host unit test.

## 4. Linux ELF Compatibility and Future Windows Support

### 4.1 Routing Boundary

**[Policy]** Distinguish AceIS-native images from supported Linux ELF images at the load boundary. Route Linux application operations to the compatibility side, including the appropriate Linux syscall-number interpretation. Non-native ELF from other operating-system ABIs is outside scope and should be reported as unsupported.

**[Open]** Define the native image marker, accepted Linux image profiles, machine/ABI checks, interpreter and version requirements, and behavior for malformed or ambiguous inputs. Do not assume one ELF header field proves that every non-native ELF is Linux. Recognition must be defined and tested before accepting an image.

**[Open]** The mechanism that redirects Linux syscalls is not implemented or selected by this design update. Loading a wrapper SO alone does not redirect a binary's direct syscall instructions. The Linux-hosted PoC must distinguish actual compatibility routing from a test program simply using the host Linux kernel's syscall path.

### 4.2 Compatibility Targets and Limits

**[Policy]** Retain the goal of using existing Linux/glibc binaries without rebuilding them for AceIS. An Ubuntu-targeted Steam application and its games illustrate the desired user experience, not an acceptance claim or the first PoC's required workload.

**[Open]** Existing binaries also depend on the supported syscall set and semantics, dynamic-linker behavior, symbol versions, TLS, threading, signals, and other ABI contracts. Graphics, drivers, launchers, and game-specific requirements need separate validation. Thin-wrapper terminology does not establish that this work is already small or complete.

Version 5's staged static/dynamic Linux ELF plan remains a proposal for compatibility implementation. The current priority is the native foundation and acc, before expanding that compatibility scope.

**[Policy]** Windows application support remains a future goal. Wine is the designer's preferred candidate for that path. **[Open]** Its integration requirements, dependencies, licensing, and supported workloads need evaluation. It is not an initial acc or Ace-Core PoC requirement, and this update does not commit to a new in-Core PE implementation.

## 5. SO Replacement and Self-Migration

**[Open]** Self-migration during SO replacement is an acknowledged difficult problem. Dynamic loading and separate versioning do not by themselves preserve live state, outstanding calls, pointers, callbacks, threads, or memory ownership across replacement.

**[Proposal]** Separate startup selection and restart-based upgrades from live replacement. Before claiming live replacement, define quiescence, old/new coexistence, state schema and conversion, reference lifetime, rollback, failure recovery, and any real-time constraints. A future experiment may first replace a component only after all calls have completed, but that does not settle general self-migration.

No migration protocol, hot-update guarantee, or automatic deployment permission is established here. Track self-migration as unresolved while continuing the initial compiler and loader work.

## 6. Testing, Coverage, and CI

### 6.1 Repeatable Tests and Defined Coverage

**[Policy]** Every new development item must include repeatable tests and coverage measurement, with tests orchestrated by CTest. Use appropriate C/C++ testing tools such as GoogleTest / GoogleMock or Boost.Test. The requirement is effective test coverage and CI execution, not using all frameworks in every component.

CTest schedules and reports tests; unit-test frameworks provide assertions and mocks. **[Open]** Choose separate coverage instrumentation and reporting tools appropriate to each compiler and execution environment. A passing CTest run does not establish a coverage percentage.

**[Policy]** Aim for 100% for each of C1-C4. The project has not yet defined those labels, their measured scope, or a feasible toolchain for every level. Do not equate them with another standard's numbered criteria or claim C1-C4 compliance from line/branch coverage alone. Version 5's MC/DC reference remains a candidate, not an adopted mapping.

Before a C1-C4 gate is enforceable, record:

1. The formal definition and denominator for each metric.
2. Instrumentation, tool versions, build flags, and treatment of optimized code.
3. In-scope source, generated code, dependencies, and reviewed exclusions.
4. How infeasible or unreachable cases are justified, and who approves exceptions.
5. Evidence from the exact commit, including test discovery counts and reports.
6. CI failure conditions and retention of raw coverage data and readable summaries.

**[Policy]** Make the build, CTest suite, and supported coverage collection executable in CI. **[Proposal]** Until C1-C4 definitions are adopted, report the exact metrics available, their values and gaps, and any unmeasured criteria as unmeasured. Do not postpone all tests until every metric is settled or label unavailable coverage as 100%.

The common policy is maintained in [development-policy.md](development-policy.md#tests-coverage-and-ci). Each implementation repository must supply its working build/test/coverage commands and CI configuration. This documentation update does not install frameworks, introduce placeholder CMake projects, or claim that those implementation gates already run.

### 6.2 High-Assurance Engineering Direction

**[Policy]** Design testing from the outset with the rigor expected in automotive, aviation, and space engineering. This is an engineering objective, not a statement that the project is certified, qualifies for a safety level, or has already passed such verification. Claims about strict testing must identify the scope and evidence actually available.

**[Proposal]** Scale assurance work to the component and its failure consequences, starting with the first acc and Ace-Core milestones:

- Give requirements and interface contracts stable identifiers. Trace each requirement to its implementation, tests, results, and unresolved deviations for the exact revision.
- Analyze hazards, failure modes, trust boundaries, and required safe behavior. Include invalid input, allocation and mapping failure, permission errors, resource exhaustion, ABI/version mismatch, and partial initialization or cleanup. Address concurrency and timing where those are in scope.
- Use independent technical verification and editorial review of claims. A generator's tests and coverage numbers need review against requirements, failure analyses, and an independent expected-result source where practical.
- Retain reproducible toolchain and environment identifiers, test discovery/execution results, coverage data, review findings, and the disposition of failures and exclusions. Report incomplete checks and known limitations before accepting a milestone.
- Define applicable standards, assurance levels, tool qualification, and certification activities only if a later application requires them, with domain expertise. Do not infer any of them from a C1-C4 label or a 100% structural-coverage result.

Begin with a bounded requirements/test matrix and failure analysis for the selected PoC, and expand the evidence with the implementation. This approach supports progress without presenting a passing smoke test or a coverage target as a safety guarantee.

## 7. Next Design Decisions and Evidence

- **acc milestone:** Select one target; define its minimum language/AIR scope, plugin boundary, output and execution contract, and a reproducible test result. Preserve the scalar comparison and crash-analysis directions from Version 5.
- **Native sysroot:** Record the smallest versioned native interface and component calling contract without making Linux compatibility mandatory.
- **Ace-Core milestone:** Document the initial mmap semantics and controlled SO format, then demonstrate mapping, load, call, failure handling, and cleanup on a declared host or guest configuration.
- **Verification baseline:** Define C1-C4 and feasible measurements; add CTest, CI, requirements traceability, failure analysis, and independent verification alongside implementation, recording gaps honestly.
- **Later work:** Linux compatibility syscall routing and ABI coverage, Windows/Wine evaluation, and live SO self-migration stay separate from initial milestone completion.

## Revision Record

- 2026-11-07: Record the later acc target-SO design, native-sysroot priority, minimal loader/startup mapping direction, Linux-only compatibility routing, future Wine candidate, unresolved self-migration, and CTest/coverage/CI goals with a high-assurance engineering direction. Preserve Version 5 and its translation for provenance.
