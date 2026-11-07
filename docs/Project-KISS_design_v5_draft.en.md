# Project-KISS / Project-ACE / AceIS: Integrated Design Philosophy and Concept Document (Version 5 Draft)

> Translation note: This is an English translation of `docs/Project-KISS_design_v5_draft.md` in `i-pp/Project-KISS`, source blob `5ee43501ab0e115be39c58161cae8b8bf05a7aa1`. Historical terminology, including Project-ACE, is preserved; the active management name is now Project-AceIS. This translation does not revise the original design decisions or their status.

-   **Document type:** Integrated document covering concepts, design philosophy, and initial architecture (a working draft for project management)
-   **Reference date:** 2026-11-07
-   **Version:** Version 5 draft (building on Version 4; revision history at the end, ADR candidates in Section 18)
-   **Status:**
    A design draft that builds on the Version 4 draft and adds the compiler PoC, AIR, and debugging directions from 2026-11-07. Implemented items and unverified items are distinguished.
-   **Purpose:**
    Organize design principles, technical concepts, development conventions, and governance previously scattered across discussions into one document framework.
-   **Label legend:**
    **[Policy]** = A direction explicitly stated by the designer during discussions (not a settled specification, because it has not yet been recorded as an ADR).
    **[Proposal]** = An idea raised in review, awaiting the designer's decision.
    **[Deferred]** = An item on which a decision has been deferred.
    Unlabeled statements carry forward content from earlier versions. Where a later version explicitly updates an item, the later wording takes precedence.

> This is not a specification of an implemented system. It preserves the concepts developed so far and provides a shared basis for future design, implementation, and review. Numerical targets and technical candidates that remain undecided must not be treated as settled specifications.

------------------------------------------------------------------------

## 1. Overview

Project-KISS is centered on design philosophy, principles, and a manifesto, rather than being simply a software product or business plan. It aims to have the system absorb complexity instead of imposing it on people or individual applications, through a continuing cycle of observation, verification, regeneration, and optimization.

The overall structure consists of a top-level project, its subproject, an integrated system, and the components that make up that system.

- **Project-KISS:** The top-level project developing AceIS and components such as ACE / PAUL / GENE / PETER.
- **Project-ACE:** A subproject of Project-KISS. It combines the components to design, implement, and verify AceIS.
- **AceIS:** A next-generation integrated system encompassing ACE / PAUL / GENE / PETER and other components. It is positioned as an **IS (Integrated / Intelligence / Individual System)** rather than being limited to the conventional term "OS."

The conceptual relationships are as follows.

```text
Project-KISS
|-- Development of components such as ACE / PAUL / GENE / PETER
`-- Project-ACE (a subproject of Project-KISS)
    `-- AceIS (an integrated IS encompassing ACE / PAUL / GENE / PETER, etc.)
        |-- ACE: intelligent component for reasoning, verification, and self-improvement
        |-- PAUL: Program Analysis & Unification Layer
        |-- GENE: Generative Execution & Native Engine
        |-- PETER: Portable Execution & Translation Environment
        |-- AceIS Core: overall control and decisions for the integrated system
        |-- A-Nexus: shared abstraction, resource mediation, and real-time control foundation
        |-- Abiss (ABISS): minimal hardware boundary / HAL
        `-- Runtime / ABI / API / Compiler / Linker / Toolchain integration
```

**Terminology distinctions**

- **Project-ACE** names the subproject and is distinct from the individual **ACE** component. It does not refer only to developing ACE in isolation; it covers the integration, design, implementation, and verification of AceIS as a whole. **Autonomous Cognitive Evolution** is treated as the conceptual expansion of the Project-ACE project name.
- **ACE** refers to the intelligent component within AceIS, responsible for reasoning, verification, deriving candidate improvements, and related functions.
- **AceIS Core** refers to the system's central element for integrated control and decisions across AceIS. It is not synonymous with ACE's intelligent functions. Detailed APIs, execution placement, and responsibility boundaries between the two remain to be defined.
- **AceIS** is neither the name of an individual component nor another name for Project-ACE. It names the integrated system encompassing the components.
- **IS** denotes a System incorporating the concepts of Integrated, Intelligence, and Individual. Avoid simply calling AceIS itself an "OS." The general concept of an "OS" may still be used where needed, such as for technical classification or comparison with existing operating systems.

This diagram shows conceptual boundaries. The relationship between components and subproject deliverables, process separation, executable formats, communication protocols, and placement of each element are future design matters, not fixed decisions.

## 2. Project-KISS: Design Philosophy

### 2.1 Core Principle

**Do not force people to deal with complexity in its raw form.**

KISS (Keep It Simple, Stupid) is not merely a slogan for reducing lines of code or features. It is a design principle: the appropriate layer should absorb complexity that users, developers, and operators should not need to consider.

-   Do not expose internal details that users do not need.
-   Allow gradual migration without obstructing coexistence with existing assets.
-   Even when system internals are sophisticated, keep usage and the concepts needed to understand the system as simple as possible.
-   Do not confuse convenience with a black box. System behavior must be observable and verifiable.
-   Do not hide failures; make it possible to reproduce, diagnose, and fix them.
-   Avoid operational structures that depend on a particular person continually intervening.

### 2.2 Individual: A System Centered on the Individual

AceIS aims to be a system that individuals can use, control, and develop over the long term, rather than one centered on the convenience of organizations or administrators.

Here, Individual means more than a "product for individuals." It includes preserving users' freedom and control while adapting to each user's environment, devices, and workloads.

### 2.3 Freedom and Coexistence

-   Do not force migration to a new system.
-   Enable coexistence with older products and existing software.
-   Do not make discarding existing assets a condition of progress.
-   Make open development and publication the default, rather than making exclusive secrecy by a particular company central to the project's value.
-   Leave room for users to understand, control, and change their own environments.

### 2.4 New Experiences for People

The design concerns the experience of people using computers, not just performance metrics. Rather than merely stacking an OS, compiler, Runtime, and AI as separate products, design the whole as one system, transferring tuning and maintenance that users previously performed manually to the system itself.

### 2.5 Excitement for Both Builders and Users

**Supporting both engineers' excitement and end users' excitement is an essential design principle of AceIS.** Beyond convenience and performance, both building and using the system should offer discovery, understanding, a sense of accomplishment, and freedom.

- **Engineers:** Can observe startup and internal behavior, try their own changes, compare measurements, and improve the system while understanding how it works.
- **End users:** Can focus on their own goals without being consumed by troublesome configuration or maintenance. The system adapts to their environment, and they can experience the benefits of improvements.
- **The cycle:** Developers' discoveries and improvements are verified and shared, checked for suitability in each environment, and used to improve the user experience. The results inform subsequent development.
- **Non-goals:** Do not equate "excitement" with AI adding features without permission or merely raising numerical benchmark scores. Maintain user control, understandability, safety, and real-time constraints.

The first users are likely to be engineers. From the first HelloWorld, therefore, provide an experience of running, observing, experimenting, and improving. Do not define a minimal implementation by feature count alone; also evaluate whether it makes engineers want to explore further.

### 2.6 Nature of the Manifesto

Project-KISS's external documents emphasize concepts, design philosophy, freedom, Individual, SIMD Native, Minimum AI RTOS, RTOS with Gaming Specs, application areas including robotics and aerospace, and new human experiences, rather than business or revenue plans.

Musical and cultural references may contribute to the brand's atmosphere or appear occasionally in the writing. However, avoid expressions that could create confusion with existing bands' trademarks, logos, or designs, and maintain a distinct identity.

## 3. Project-ACE: Technical Framework

### 3.1 Purpose

Project-ACE is a subproject of Project-KISS that integrates components such as ACE / PAUL / GENE / PETER to design, implement, and verify AceIS.

For the name's expansion and the distinction between Project-ACE and the ACE component, see "Terminology distinctions" in Section 1.

### 3.2 Feedback Loop

The basic cycle is as follows.

1.  **Observation:**
    Record runtime behavior, performance, failures, configuration, and hardware characteristics.
2.  **Analysis:** Extract causes, trends, and candidate improvements from raw logs and execution information.
3.  **Hypotheses and proposed changes:** Define candidate improvements as concrete changes.
4.  **Generation and build:** Implement and build changes using compilers and generation systems.
5.  **Verification:** Verify through testing, coverage, compatibility, performance, and regression checks.
6.  **Application decision:** Decide whether to apply a change based on verification results and risk.
7.  **Observation after application:** Record measured results after application and compare hypotheses with outcomes.

The ability of AI to propose or generate changes is distinct from permission to apply them unconditionally in production. Change authority, verification requirements, rollback methods, and final approval conditions are to be defined according to component risk.

## 4. Component Responsibilities

ACE / PAUL / GENE / PETER are functional components of AceIS. Their role names provide a conceptual model for separating functional responsibilities rather than concentrating all work in one giant agent. Implementation methods, models, and process separation are not fixed.

### 4.1 ACE (Component) --- Reasoning, Verification, and Self-Improvement

-   Reason about problems, constraints, and design intent.
-   Evaluate proposed changes and derive candidate improvements from verification results.
-   Check the correctness of generated artifacts from an independent perspective.
-   Support improvement cycles using observation data and past results.

### 4.2 PAUL --- Program Analysis & Unification Layer

-   Analyze source code, dependencies, build configuration, and API/ABI relationships.
-   Understand consistency across different components.
-   Consolidate analysis results and identify the scope of a change's impact.
-   Provide program analysis functions centered on the compiler and linker.

### 4.3 GENE --- Generative Execution & Native Engine

-   Handle functions related to code generation, execution, and conversion to native code.
-   Integrate with mechanisms for building, running, and measuring generated changes.
-   Return execution results to the verification stage.

### 4.4 PETER --- Portable Execution & Translation Environment

-   Handle porting, translation, and compatibility.
-   Address differences across CPUs, ABIs, and execution environments.
-   Connect existing software assets with the new native environment.

### 4.5 Purpose of Separation

Conceptually separating analysis, generation, verification, and porting clarifies responsibilities, failure locations, and review perspectives. The aim is a structure that preserves each function's contract even when different AI models are used or models are replaced in the future.

This is not a decision to require a separate process or model for every role. Where independence is necessary, what should be shared, and the communication contracts will be decided during implementation.

## 5. AceIS: Integrated IS / Runtime Concept

### 5.1 Positioning

AceIS is an integrated system encompassing components such as ACE / PAUL / GENE / PETER, including Runtime, ABI/API, and compiler integration. **It is positioned through the concept of IS (Integrated / Intelligence / Individual System), not the expansion "ACE Individual System."** "OS" may be used as an existing technical classification where needed, but not as the name for AceIS itself.

For the distinction between the ACE component and AceIS Core, see "Terminology distinctions" in Section 1.

### 5.2 Direction for the System Foundation

-   Use a minimal AI-capable RTOS (Minimum AI RTOS) as one starting point.
-   Consider future applications in general-purpose operating systems, RTOS, gaming, robotics, aerospace, and other areas.
-   Consider a direction in which the kernel provides foundations such as hardware abstraction, protection, and resource management, while the AI core and higher-level intelligent functions reside in userland.
-   Initially use compatibility with existing mechanisms as an entry point, while aiming in the long term for a native environment with its own API/ABI.
-   Provide binary compatibility with existing amd64 Linux / Windows applications and libraries as an early-stage compatibility layer (5.7), packaged separately from the main system. **[Policy]**
-   Compatibility or coexistence with Android and other systems is under consideration, but is not an initial-stage requirement.

### 5.3 From POSIX to a Dedicated API/ABI

Treat POSIX compatibility as an initial entry point for using existing software and development tools. Do not make POSIX an absolute condition of the final design; design the API/ABI to suit AceIS's goals.

During migration, make the boundary between the compatibility layer and the native environment explicit, aiming for a structure that prevents compatibility-related complexity from spreading throughout the kernel. The specific API/ABI specifications, versioning, and compatibility policy remain undecided.

### 5.4 Basic AceIS Layer Structure

The basic structure is **Hardware -> Abiss -> A-Nexus -> AceIS Core**. The arrows indicate the main dependency and control paths, not a requirement that every operation pass through every layer.

#### Abiss (ABISS) --- HAL / Hardware Boundary

Abiss is the software layer closest to the hardware and is to be kept as small as possible. It handles hardware-specific initialization, low-level control, and the minimal functions exposed to higher layers. The name's expansion is a conceptual placeholder; refining its etymology and formal expansion is left for later.

#### A-Nexus --- Shared Abstraction and Resource Mediation Layer

A-Nexus handles shared abstractions, virtualization, resource mediation, ordinary hardware operations, and real-time control. AceIS Core primarily uses A-Nexus functions. However, A-Nexus is not to be a mandatory path for every operation: an explicit direct-access path to Abiss is provided for developers who need low-level or hardware-specific functions.

Direct access does not mean unrestricted authority over MMIO, DMA, interrupt control, or similar functions. Permissions, mutual exclusion, memory protection, safety conditions, and real-time constraints remain in place. Do not confuse bypassing A-Nexus abstractions with bypassing protection mechanisms.

#### AceIS Core --- The Center of Autonomous Reasoning and Self-Development

AceIS Core handles system observation, reasoning, selection of candidate improvements, evaluation of verification results, and decisions on overall direction. AceIS names the entire system; AceIS Core refers to the center of autonomous reasoning and self-development within it.

### 5.5 Startup Order and Layer Responsibilities

The basic startup order is **Abiss -> A-Nexus -> AceIS Core**. Abiss prepares minimal hardware initialization and the execution foundation; A-Nexus initializes shared resource management and control functions; AceIS Core then starts operating. Details of the boot ROM, initial bootloader, verification and recovery mechanisms, and related elements will be defined separately.

Layer names or direct operations alone do not guarantee real-time behavior. Define what is guaranteed and under what measurement conditions, including interrupt paths, scheduling, locks, memory allocation, cache and memory-bandwidth interference, priority inversion, and worst-case execution time. A-Nexus is to be the central control foundation supporting real-time behavior, but timing guarantees must be established through implementation and verification.

### 5.6 Autonomous Configuration Optimization and Self-Improvement

The concept is for AceIS to understand hardware configuration, drivers, execution load, and performance data, and autonomously improve configuration and build artifacts. It may draw on knowledge from the cloud, but transmitting confidential data is not a prerequisite. Local processing, controls on data leaving the system, update verification, and rollback are important design concerns.

Do not treat "can change automatically" as equivalent to "may change without verification." Technically separate authority and verification paths so that AI judgment alone cannot change invariants concerning safety, real-time behavior, or security.

### 5.7 Compatibility Layer

-   **Purpose:** In AceIS's initial stages, enable binary-compatible use of existing assets (amd64 Windows / Linux applications and libraries). **[Policy]**
-   **Structure:** Envision a dynamic loader that interprets or translates existing binaries and runs them through compatibility libraries such as libposix, liblinux, and libwin32. The names and division are provisional. **[Policy]**
-   **Distribution:** Provide it separately from the main system as a runtime users install when needed. Separate it from the outset on the assumption that it will eventually be removed. **[Policy]**
-   **Placement:** Confine it to userland in principle. **[Policy]**
-   **Dependency direction relative to the main system:** Do not create dependencies from the main system to the compatibility layer. The compatibility layer uses only the main system's public API/ABI. This rule is intended to prevent removal from breaking the main system's build. **[Proposal]**
-   **Removal conditions:** Define in an ADR when and by what criteria to remove it (for example, major applications run on the native API, or usage falls below a certain level). **[Proposal]**
-   **Proposed stages:** Because difficulty varies substantially by stage, proceed in this order. **[Proposal]**
    1.  Statically linked Linux ELF (mainly syscall translation)
    2.  Dynamically linked Linux ELF (requires glibc / musl ABI compatibility)
    3.  Windows PE (requires behavior equivalent to kernel32 / ntdll; a large undertaking)
-   **Implementation caution (copyright and licensing):** Writing while consulting source code from implementations such as Wine, ReactOS, or glibc can introduce code contamination or derivative-work issues. Implement from public specifications, documentation, and observed behavior (a clean-room-style process). **[Proposal]**
-   **Relationship to the initial target:** Choosing amd64 initially makes compatibility-layer verification easier because existing x86_64 binaries can run without instruction translation. Choosing aarch64 or RISC-V first requires binary translation (PETER's role) from the start. Consider this when selecting the initial target. **[Proposal]**

### 5.8 Execution Modes and Application Sandboxing

-   Adopt sandboxing when effective execution speed can be maintained. Do not adopt isolation that sacrifices speed. **[Policy]**
-   When speed requires a direct path to a device (something like DMA), handle it through an execution mode. **[Policy]**
-   Make isolation mode the default, with an explicitly selectable performance mode that allows direct paths. Log which mode was selected. **[Proposal]**
-   Consider IOMMU protection (Intel VT-d, ARM SMMU, etc.) for direct paths. Existing examples include VFIO, DPDK / SPDK, and io_uring. **[Proposal]**
-   If the compatibility layer translates syscalls within the same process, overhead is expected to be lower than interception through ptrace or seccomp. Measurement is required. **[Proposal]**
-   Security of compatibility applications (vulnerabilities in the original applications) is the user's responsibility; users concerned about it should build and use native applications. This does not abandon security of the AceIS main system. **[Policy]**
-   Even if a compatibility application is compromised, ensure the boundary with the main system (permissions, address spaces, and file access scope) prevents the compromise from spreading to the main system or native applications. **[Proposal]**

### 5.9 Self-Improvement Sandbox

Rather than continuously running a heavyweight sandbox for ordinary processing, AceIS provides a dedicated sandbox for safely verifying candidate improvements. It is used, for example, when ACE detects an anomaly or an opportunity for improvement, or when a candidate patch arrives from a shared server.

- **Candidate preparation:** Perform time-consuming work such as generating, compiling, and linking candidate changes in advance wherever possible, so an executable candidate is ready at verification time.
- **Verification opportunities:** Use idle time when it can be estimated. When it cannot, understand the target processing deadlines and interference conditions before selecting a safe verification window.
- **Short-duration verification:** Aim for a design that can run prepared tests or check local invariants on the order of microseconds by limiting the verification scope.
- **Comprehensive verification:** Do not assume that arbitrary kernel changes or complex concurrent processing can be completely verified in a few microseconds. Broad testing, race conditions, long-term stability, and similar concerns require separate verification in the background or in a development environment.
- **Separation from production processing:** Prevent the sandbox's CPU time, memory, cache, memory bandwidth, I/O, interrupts, and other resource use from violating production processing deadlines. Making the work interruptible is not sufficient by itself.
- **Acceptance or rejection:** Decide based on verification results, performance, functional correctness, safety constraints, and real-time constraints. Better aggregate benchmarks do not justify violating explicit invariants.
- **On failure:** Discard the candidate and retain the current implementation. Continue observing results after application, and provide a safe recovery path to revert when necessary.

A design that supports verification "on the order of microseconds" is an important target, not a guarantee of complete verification for every change. Design change units, conditions, and tests that can be verified quickly, and use separate verification stages for everything else.

## 6. SIMD Native and Abstracting Hardware Differences

### 6.1 Basic Policy

SIMD Native is a concept aimed at enabling the system and compiler to use SIMD according to CPU capabilities, rather than requiring users to treat it as a special optimization option each time.

-   Absorb differences in instruction sets and features between CPUs on the system side.
-   Have the compiler generate code for the target CPU or feature set.
-   Allow the runtime environment to select an appropriate implementation when needed.
-   Aim to combine portability with native performance.

### 6.2 Unresolved Matters

The precise meaning of always enabling SIMD, the baseline ISA, feature detection, dispatch among multiple implementations, floating-point reproducibility, and binary distribution formats remain unresolved. Even when prioritizing performance, specifications must preserve portability and correctness of results.

## 7. RTOS and Real-Time Design Concerns

Drawing on the designer's embedded OS/RTOS experience, the following issues are important design considerations.

-   The possibility of operation and scheduling that do not assume CPU pinning.
-   Core isolation and resource management for IRQ handling and real-time processing.
-   Observation and diagnosis of deadlocks, priority inversion, interrupt latency, and jitter.
-   Always-on tracing that can track execution state over long periods.
-   Design that accounts for log retention, search, and analysis.
-   Interest in time synchronization and deterministic networking, such as TSN/gPTP.
-   Combining RTOS real-time properties with the performance and responsiveness required for gaming.
-   Keeping AI decisions and large builds off real-time paths, and performing only brief validation of previously prepared candidates at controlled times.
-   Defining the required time granularity, deadlines, and jitter for each target rather than imposing a uniform nanosecond-level requirement. The goal is a microsecond-order local validation path, distinguished from a time guarantee for complete validation of every change.

These are design focus areas, not a claim that everything is implemented or established as a definitive requirement. Any claim of real-time guarantees requires explicit worst-case execution times, interrupt response, scheduling, load conditions, and measurement methods.

## 8. Logs, Observability, and Self-Improvement

### 8.1 Raw Logs as the Primary Record

AI summaries or compressed memory must not be the only source of records. Retain raw logs as primary information, and have AI generate analyses, indexes, and summaries from them. Emphasize a structure that prevents AI from rewriting past records to suit its purposes.

-   Separate original logs from AI-generated derived data.
-   Consider timestamps, origins, target components, event types, correlation IDs, and similar fields.
-   Include missing logs, ordering, clock synchronization, and corruption detection in the design scope.
-   Clarify retention periods, capacity, privacy, and handling of confidential information.
-   Link AI decisions and changes to the logs that supported them.

### 8.2 Long-Term Tracing

Continuous observation over long periods is an area of interest, including a concept for retention of approximately 1-2 months. Log capacity targets and record widths (such as 64/128 bits) are under consideration, not fixed specifications. Determine recording volume, event frequency, compression, ring buffers, external storage, and preservation methods during failures through measurement.

### 8.3 Reproducibility and Auditability

For changes proposed by AI, aim to make inputs, relevant logs, artifacts, test results, approvals, and application results traceable. It is important to be able to return to the original supporting data, not just summaries.

## 9. Security and Threat Model

This section is newly added and did not exist in the first edition. Formalizing the threat model remains an open issue (Section 17).

### 9.1 Basic Stance

-   Since perfect preventive defense does not exist, design on the assumption that intrusions cannot be entirely prevented (assume breach). **[Policy]**
-   AI detects suspicious behavior, isolates and analyzes it, creates countermeasure patches to attempt to neutralize it, and shares reports. Self-improvement and synchronization among instances across detection, countermeasures, and sharing are among the functions handled by the ACE component. **[Policy]**
-   Since AceIS will be entirely public as OSS, assume that it will be targeted. Assume that analysis by attackers, including analysis on other operating systems, cannot be prevented, and do not rely on secrecy. **[Policy]**
-   AI detection is the last line of defense, not the first. Layer it on top of fundamental defenses such as memory-safe languages, least privilege, and privilege separation. **[Proposal]**

### 9.2 Threats Through Compatibility Layers

-   Address malware running through a compatibility layer by revoking its permission to use that layer (prevent it from using the layer or running). **[Policy]**
-   If a legitimate application such as OpenSSH has a vulnerability, even the vulnerable version will run. The countermeasure is to use a fixed version. **[Policy]**
-   Who decides to revoke permission, how signed deny lists are operated, and how users can override false positives remain unresolved. **[Proposal]**
-   For existing binaries whose source is unavailable, apply countermeasures through policies in the compatibility layer or execution environment, rather than in the original application, such as restricting allowed syscalls (so-called virtual patching). **[Proposal]**

### 9.3 Instance Contribution and Trust Ratings

-   Contribution and trust metrics apply to AceIS instances themselves, not to users. Humans do not need to know which instances have high contribution ratings. **[Policy]**
-   Evaluation is based on the value of logs reported by an instance: records of how the system behaved when the user took a particular action. Thus, even an instance belonging to a user who creates crackware may gain a higher contribution rating. **[Policy]**
-   Information from instances with high contribution and reliability ratings receives additional verification sooner, is communicated to all instances (via either push or pull), and leads to automatic updates. **[Policy]**
-   In response to falsified reports, another instance submits a report identifying the falsification. **[Policy]**
-   Trust ratings affect only verification priority, without reducing verification rigor. This guards against attacks that build trust over a long period before spreading false information. **[Proposal]**
-   Measure a report's value by whether it can be reproduced by independent instances or in isolated environments. **[Proposal]**
-   Guard against mass creation of fake instances (Sybil attacks) by preventing instances from the same origin from inflating each other's ratings. **[Proposal]**
-   Even if numerical ratings are not disclosed to humans, preserve the grounds for decisions in tamper-proof audit logs and make them traceable. Align this with the principle of using raw logs as the primary record (Section 8). **[Proposal]**

### 9.4 Updates and the Patch Acceptance Path

-   Updates obtain the minimum necessary differences and incorporate them after building and validating on the AceIS side, rather than distributing completed images over the air (OTA). **[Policy]**
-   The central issue is the path by which patches are accepted, to avoid inadvertently incorporating attacker-created patches. **[Policy]**

The proposed outline of the acceptance path is as follows. **[Proposal]**

1.  Treat all patches as untrusted input, regardless of origin.
2.  Separate evidence (reports and trust ratings) from authority. Trust ratings affect only investigation priority; acceptance authority is granted only to patches that pass the following gates.
3.  Origin-independent gates: reproduce the vulnerability or defect in an isolated environment; confirm that the patch resolves it; pass existing tests; review the diff (by both AI and humans) to ensure there are no changes outside the claimed scope; and compare behavior before and after the patch in a sandbox (recording syscalls and input/output).
4.  Obtain independent validation by instances with different configurations and hardware, and confirm agreement among their results.
5.  Require threshold signatures using multiple keys for system-wide acceptance.
6.  Use staged rollout (distribute to some instances first, verify health, then expand) and rollback (such as an A/B scheme).
7.  Use reproducible builds and compare build-result hashes among instances to detect compromised build environments.
8.  AceIS may automatically apply reversible mitigations contained within an instance (isolation or privilege restrictions) within predefined constraints. Patches that affect all instances must pass all the gates above and require signatures.
9.  Protect the acceptance path itself (code for validation, signing, updating, and trust decisions) through a separate, stricter procedure than the normal acceptance path, such as mandatory human involvement. Prevent the decision-making mechanism from rewriting its own rules on its own.
10. Treat trust in the build environment as a design issue, including bootstrap validation for ace-cc self-hosting and the so-called trusting trust problem.

Other considerations: **[Proposal]**

-   The AI monitoring and isolation mechanism itself will be a target. Place the monitoring mechanism in a separate privilege domain and area from what it monitors.
-   The paths used to share and synchronize reports and countermeasures are also attack surfaces. Include signatures, verification, and provenance tracking from the start.
-   Sophisticated backdoors that pass both testing and review, such as the techniques seen in the xz utils incident, remain a residual risk. Since they cannot be prevented entirely, increase the probability of discovery through a combination of reproducible builds, behavioral diff comparisons, and diverse validators.

### 9.5 Privacy and Consent

The concept of sharing logs among instances describing "how the system behaved in response to user actions" requires decisions about what is collected, how far it is anonymized, and whether users have explicitly consented. It may fall under Japan's Act on the Protection of Personal Information, GDPR, and similar laws, so expert review is required. This also relates to the Individual philosophy of respecting user control. **[Proposal]**

## 10. Compiler/Linker and Development Environment

### 10.1 Dedicated Compiler ace-cc

-   Develop the dedicated compiler ace-cc as an initial implementation for Project-KISS/Project-ACE. **[Policy]**
-   Do not incorporate code from LLVM or existing compilers into generated artifacts. Do not require an LLVM-family runtime as the backend for ace-cc. **[Policy]**
-   Use gcc and clang only until ace-cc is complete, and do not use them afterward. **[Policy]**
-   Use gcc/clang only as host compilers for building ace-cc and as reference implementations (oracles) for differential tests that compare outputs. **[Proposal]**
-   Define bootstrap procedures and validation methods for ace-cc self-hosting. **[Proposal]**

### 10.2 Runtime Library libace_rt

-   Aim to avoid requiring users to think about linker arguments such as `-lc` and `-lgcc`. **[Policy]**
-   If a runtime library is created, name it libace_rt. Only POSIX compatibility requires consideration. **[Policy]**
-   Include functionality equivalent to libgcc/compiler-rt (128-bit integer arithmetic, soft float, memcpy-family functions, stack protection, and similar features) within the scope of the project's own implementation, without depending on existing libraries' license terms. **[Proposal]**

### 10.3 Initial PoC Scope

The initial direction is to start with a small PoC around the ace-cc cross-compiler/linker, rather than implementing the entire OS at once.

-   Host: x86_64/amd64
-   Initial target: narrow the scope to one CPU architecture first
-   Scope: foundations such as the cross-compiler, linker, and target libraries
-   Validation: generated code, assembly, link results, and tests
-   Goal: aim for completion within one minute, including the initial test suite
-   Parallel testing: several hundred tests are under consideration, with approximately 500 as a conceptual target

These are goals and candidates for the initial PoC, not measured performance guarantees. Actual time depends on test content, the host, caches, and the degree of parallelism.

### 10.4 Target Switching

There is a concept for handling target CPU switching through libraries and similar mechanisms, and managing build and test costs as targets increase. The goal is to manage target configuration, including options such as `-mcpu` and `-march`, without scattering it throughout the system.

Rather than completing aarch64, amd64, and RISC-V simultaneously from the outset, first complete the build, test, and artifact-validation workflow for a single target, then add more targets.

### 10.5 Language and Implementation Preferences

-   Focus on C/C++.
-   Include Rust among the candidate languages.
-   Avoid adding more Python-centric implementation layers.
-   Emphasize shells and CLIs; do not make a GUI/WebUI mandatory.
-   Prioritize practical validation environments such as QEMU, Renode, and KVM, without depending on expensive virtual platforms from the outset.

Finalize language and tool choices after evaluating maintainability, artifacts, debuggability, and execution speed in the initial PoC.

### 10.6 Ace Intermediate Representation (AIR) and Responsibility Boundaries

- **[Policy]** Call the project's own target-independent intermediate representation **Ace Intermediate Representation (AIR, pronounced "air")**. Use AIR as a separation boundary instead of rebuilding the entire compiler for each source-language and target-ISA combination.
- **[Policy]** Do not assume a dependency on LLVM IR or an LLVM backend. Treat existing tools such as GCC/Clang as external tools for initial bootstrapping and comparative validation, distinct from the custom compiler's generation path.
- **[Design Clarification]** PAUL primarily handles source parsing, semantic analysis, and conversion to AIR; GENE primarily handles target instruction selection from AIR and SIMD-native code generation; and PETER primarily handles porting, conversion, and compatibility across different ISAs, ABIs, and execution environments. This applies existing conceptual responsibilities to the compiler PoC; module boundaries and APIs remain unresolved.
- **[Proposal]** Make semantics explicit in AIR, including operation widths, signedness, integer overflow, floating-point behavior, memory access, alignment, and vector lane order, so results can be compared across targets.
- **[Proposal]** Limit the first PoC to a single x86-64 target, starting with a minimal generation path such as returning a constant, then progressing to 128-bit SIMD addition, subtraction, and logical operations. Add AArch64 NEON/SVE, RISC-V, and other targets in later stages.

### 10.7 SIMD-Native Defaults and Target Specification

- **[Policy]** Make SIMD-native generation the basic code-generation policy, aiming for a compiler that does not require users to explicitly enable SIMD optimization each time. This does not mean forcing SIMD on processing for which it is inappropriate.
- **[Policy]** Plan an option, `-fforce-scalar`, to explicitly select scalar code generation. Its precise scope, ABI, and handling of cases involving vector types require specification.
- **[Policy]** Include cross-compilation in the basic design. Separate `--target` for the target environment from `-march` for the instruction set. Consider `-mcpu`/`-mtune` later as needed.
- **[Proposal]** Do not allow automatic host CPU detection to affect cross-target instruction selection. Explicitly distinguish it only when introducing options such as `-march=native`.
- **[Unverified]** Measure the performance, code size, and correctness of SIMD-first generation against scalar generation and reference results from existing compilers. Performance parity with existing compilers such as Clang is not guaranteed.

### 10.8 Debugging Policy: Prioritize Crash Analysis

**Design decision: Do not make an interactive SIMD-specific debugger a prerequisite for the initial PoC. Establish Core Dumps and AIR mapping information first, and continue compiler development with failure analysis available.** **[Policy]**

The minimum initial analysis path is as follows.

1. **Execution and failure records:** Record test inputs, compiler and target configuration, build identifiers, artifacts, and exit status.
2. **Core Dump:** For abnormal termination on Linux/ELF, collect a Core Dump after checking OS settings, storage location, capacity limits, and access permissions. A dump may not be obtainable for every abnormal termination.
3. **AIR Mapping:** Store mappings between AIR instructions/functions and generated machine-code address ranges separately from the generated code. Link them to artifact identifiers and support cases where optimization removes a correspondence or creates multiple correspondences. Start with a minimal mapping table in the initial PoC.
4. **Postmortem analysis:** Use existing tools such as GDB to inspect the PC, stack, general-purpose registers, available SIMD extension registers, and disassembly, and cross-reference them with AIR Mapping. Register state included in a Core Dump depends on the OS, CPU, and dump settings.
5. **Evidence retention:** Associate the Core Dump, generated binary, AIR, Mapping, test inputs, and analysis results. Since Core Dumps may contain confidential information, define storage permissions and retention periods, and prohibit external transmission.

**Limitations:** A Core Dump captures the state at the time execution stopped; it does not reconstruct the history of executed instructions. Nor is one normally generated when a program exits normally despite incorrect computation results. Therefore, design differential testing and later arbitrary-point state dumps, instruction stepping, and SIMD lane comparisons as complementary methods.

**Proposed stages:** PoC-0 = Core Dump + minimal AIR Mapping + GDB analysis; PoC-1 = arbitrary-point state dumps; PoC-2 = display of mappings between AIR and physical SIMD registers, plus lane differences; later = an AIR-aware interactive SIMD debugger. GDB Python extensions are a prototyping candidate; a GDB fork or custom debugger implementation is not settled at this stage.

**Completion criteria (PoC-0 debugging path):** Prepare a small generated program that intentionally terminates abnormally, and reproducibly identify the stopped PC, machine code, and corresponding AIR location from the saved Core Dump and artifacts from the same build. If collection fails, retain the cause and alternative diagnostic records.

### 10.9 Local-LLM Compiler PoC Development Experiment

- **[Policy]** Use a local LLM as the primary agent implementing the initial compiler PoC code, and treat this as an experiment to validate its capabilities and limitations. Do not confuse its results with implementation work performed by cloud AI on its behalf.
- **[Proposal]** Chat/dot supports design, task definition, validation criteria, and result review; make inputs, models, generated results, and test results traceable for the local LLM's implementation work.
- **[Proposal]** Manage development-infrastructure improvements, such as NPU-resident orchestration, as independent tasks, not mandatory prerequisites that leave the compiler PoC waiting indefinitely. Prioritize a structure that permits minimal implementation and validation to begin in an available existing local environment.
- **[Unverified]** Measure whether the local LLM can independently complete the PoC, and the extent of constraints on quality, time required, and memory resources.

## 11. Source Code and Test Conventions

### 11.1 Information at the Top of Each File

Aim to make at least the following information available from each source file's header.

-   The file's purpose and responsibilities
-   Related components, APIs, and dependencies
-   Build/compiler commands and required settings
-   Correspondence with tests
-   Generation source or update procedures, when needed

Write comments to explain and justify the code. Avoid adding comments that merely restate obvious code verbosely; document purposes, constraints, and non-obvious reasons.

### 11.2 One Source : One Test

As a rule, maintain a one-to-one correspondence between source and tests. Where reasonable for the project structure, colocating tests at the end of the source file is also an acceptable candidate. Choose based on the language, build system, public APIs, and component structure.

### 11.3 Test Context and Executable

Aim for a structure in which the subject under test can execute in a test context and unit tests can run independently. A condition is that test configuration must not unnecessarily complicate the responsibilities of production code.

### 11.4 Unit Testing with Mocks

Control external dependencies with mocks and similar techniques to validate the target unit's behavior independently. Validate not only normal cases, but also boundary values, failures, error propagation, resource release, and state transitions.

### 11.5 Coverage Criteria

There is a concept for making C1--C4 coverage mandatory. However, which coverage definitions or tool metrics C1--C4 denote within this project is not currently settled. Before adopting them in implementation conventions, document the precise definition of each level, measurement tools, exception conditions, and CI failure conditions. Do not mandate numerical thresholds while leaving their meaning ambiguous.

-   Even before the definitions are settled, define the highest level as the minimum baseline. **[Policy]**
-   Consider MC/DC (the criterion required at the highest level of DO-178C) as the reference criterion for the highest level, and create a mapping to C1--C4. **[Proposal]**
-   Clarify the scope of application. Make it mandatory for the kernel/HAL, validation and acceptance path (9.4), ace-cc, and libace_rt; decide separately for supporting tools and compatibility layers. Estimate the cost of imposing the highest criterion on all code. **[Proposal]**

## 12. Public Development and Licensing Philosophy

### 12.1 Public Development Policy

The policy is to develop in a public repository accessible to anyone, without a private development period. Rather than creating a competitive advantage by keeping the OSS core secret, use public implementations, specifications, and development history as the foundation.

### 12.2 AceGeneralPublicLicense

There is a concept for using the original name **AceGeneralPublicLicense**. Because the abbreviation AGPL may be confused with the existing GNU Affero General Public License, legal documents and distributions need to clearly identify the full name, abbreviation, and applicable provisions. This document is not the license text itself and does not replace legally effective terms of use.

The stated intent is that OSI approval need not be a design premise. Specific provisions, including the license's purpose, copyright notices, source disclosure conditions, use over networks, derivative works, patents, trademarks, disclaimers, and governing law, will be settled when the license text is drafted and reviewed.

### 12.3 Minimize Notices Within Source Files

The preference is to avoid repeating long individual license notices in source code. The direction is to omit in-source license notices where possible, and where needed, limit them to something like the name `AceGeneralPublicLicense`.

At the same time, avoid a structure that prevents users from checking copyright ownership or terms of use. Place the license document and a system of copyright and contribution records at the top level, and make it possible to trace which records correspond to each source file.

### 12.4 Contributor and Copyright History Management

Do not consolidate copyright and contribution scope into one enormous file. Provide a structure that can be found centrally from the top level, while splitting the records themselves and making them traceable over time.

Design requirements:

-   Record who contributed, when, and to which scope.
-   Associate contributor records with their treatment under copyright and licensing.
-   Allow change history to be verified later.
-   Avoid a single large file; consider appropriate divisions by component, period, change unit, or similar criteria.
-   Standardize file names, record formats, revision and correction methods, and handling of personal information.
-   Whether to rely solely on Git history or also maintain separate explicit contribution records remains unresolved.

Treat reducing license notices in source files as a separate issue from weakening the traceability of copyright and contribution history.

### 12.5 Revenue and OSS

Do not center monetization on making source code private; consider support, porting, certification, maintenance, and similar services as needed. This design document does not settle a particular revenue model. Combine an openly available OSS core with a sustainable development and maintenance structure.

### 12.6 Managing Dependency and Reference Licenses

-   Build ace-cc and libace_rt from the project's own code, without incorporating code from existing compilers such as GCC or LLVM. **[Policy]** (derived from 10.1)
-   Treat gcc/clang and similar programs as external tools used only for bootstrapping and as references. They are generally thought not to affect the license of generated artifacts, but confirm this with an expert. **[Proposal]**
-   In Phase 0, compile a license inventory for external tools, libraries, and specifications used or referenced. **[Proposal]**
-   Put compatibility layers in separate repositories and packages so their licenses can be separated from the core. **[Proposal]**
-   Consider making in-source license notices machine-readable with a one-line SPDX-format identifier, using the LicenseRef- prefix for the custom license. **[Proposal]**
-   Establish a provenance-checking step to detect whether AI-generated code includes code closely resembling existing OSS. **[Proposal]**
-   Finalize legal judgments about licensing after expert review.

## 13. Governance and Maintenance

### 13.1 The Founder's Role

The Founder retains the design philosophy, overall direction, and final governance authority, but is not assumed to continue personally handling day-to-day component maintenance.

### 13.2 Component-Level Responsibility

Assign owners and maintainers to each component so that they can make design decisions, review, merge, and reject changes within their responsibilities. Do not concentrate every decision in one person.

### 13.3 Roles of AI and Humans

AI can handle analysis, testing, review assistance, change-proposal generation, and regression detection, but responsibility boundaries and authority must be clear. Do not equate the volume generated by AI with development quality; use verifiable deliverables and accountable owners as the basis for assessment.

### 13.4 Direction for Development Infrastructure

There is a concept of using a GitHub Organization, Pull Requests, CI, CODEOWNERS, and similar mechanisms to clarify each component's scope of responsibility. The specific branching strategy, signature requirements, release authority, and security response procedures remain undecided.

## 14. Application Areas

The envisioned application areas are not limited to a single embedded use case.

-   Next-generation general-purpose OS
-   Minimum AI RTOS
-   RTOS with Gaming Specs
-   Gaming and systems requiring high responsiveness
-   Robotics
-   Aerospace
-   Embedded control and industrial applications
-   Computing environments that make use of SIMD
-   Personal work and development environments
-   A development platform where engineers can enjoy booting, observing, experimenting, measuring, and improving
-   An end-user environment that makes internal system behavior visible to the extent needed and lets users benefit from improvements without having to be conscious of them

These are not all targets for the initial release at the same time. Fields requiring safety certification or real-time guarantees need requirements analysis, verification, and certification plans separate from general-purpose feature development.

## 15. Non-Goals and Designs to Avoid

Under the current philosophy, at least the following directions should be avoided.

-   Exposing complex structures directly to users.
-   Treating AI summaries alone as primary records and losing raw logs.
-   Packing all records or responsibilities into one enormous file.
-   Concentrating all decisions and maintenance in the Founder alone.
-   Trying to complete multiple architectures simultaneously from the outset.
-   Trusting code merely because AI generated it.
-   Claiming quality while leaving definitions of testing and coverage ambiguous.
-   Making the OSS core private as the primary means of monetization.
-   Fixing POSIX compatibility as an absolute requirement for all time.
-   Confusing automatic optimization with automatic changes without verification, auditing, or rollback.
-   Complicating the kernel design to accommodate the compatibility layer. **[Proposal]**
-   Reducing verification rigor on the grounds of high trust. **[Proposal]**
-   Incorporating code of unverified provenance (including AI-generated code) without checking it. **[Proposal]**
-   Permanently sacrificing either the engineer experience or the end-user experience.
-   Claiming that every change can be fully verified on a microsecond timescale.
-   Evaluating the first implementation solely by feature count or commercial completeness, while postponing an experience that developers can explore and learn from hands-on.

## 16. Proposed Development Stages

The following stages organize directions that emerged in discussion and restructuring proposals raised in review; they are not a finalized schedule. First, validate a thin version of the self-improvement feedback loop that includes the ACE component, the central hypothesis, without waiting for the implementation of AceIS as a whole. **[Proposal]**

### Phase 0 --- Define Specifications, Verification Infrastructure, and Licensing

-   Document the responsibility boundaries of Project-KISS / Project-ACE / AceIS / AceIS Core / A-Nexus / Abiss.
-   Define experience requirements for both engineers and end users as initial requirements.
-   Define the policy for separating real-time paths from the self-improvement sandbox.
-   Choose one target CPU for the initial PoC (considering its relationship to the compatibility layer; 5.7).
-   Establish criteria for builds, tests, coverage, and artifact verification, including the definition of the highest level of C1--C4.
-   Evaluate source and test organization conventions through prototypes.
-   Design the documentation structure for licensing and contribution history. Create a license inventory for external tools, libraries, and specifications.
-   Create an outline of the threat model (Section 9).

### Phase 1 --- ace-cc PoC

-   Create minimal AIR semantics and a single x86-64 backend, and verify SIMD generation incrementally.
-   Establish a minimal path for Core Dump capture, AIR Mapping, and GDB postmortem analysis. Completion of a dedicated SIMD debugger is not a prerequisite for starting.

-   Run on an x86_64/amd64 host. Limit the target to one.
-   Use ace-cc to take a small program through compilation, assembly inspection, linking, and execution or simulation.
-   Use gcc/clang only for bootstrapping and as a reference for differential testing of output.
-   Provide a minimal subset of libace_rt.
-   Run tests in parallel and measure against the overall time target.
-   Verify the structure for switching targets.

### Phase 2 --- Execution and Observation Infrastructure, and a Thin ACE Loop

-   Define the format, storage, and search of raw logs.
-   Create reproducible tests and records of execution results.
-   Track the relationships among changes, builds, tests, and measurements.
-   Connect AI analysis separately from primary records.
-   **First, run a minimal loop on the ace-cc PoC in which AI proposes changes, tests and measurements verify them, an application decision is made, and observation is repeated.** No OS is required, so the central hypothesis can be tested early.
-   Prototype a minimal acceptance path (gates and signatures).

### Phase 3 --- Minimal AceIS Execution Infrastructure

-   Define the boundary between the kernel/HAL and the userland Runtime.
-   Decide the initial APIs, execution model, and memory and scheduling requirements.
-   Decide how far to use POSIX compatibility as an initial entry point.
-   Create a minimal configuration that can boot, run, and be tested in the target environment.

### Phase 4 --- Integrate the ACE Feedback Loop into the Main System

-   Separate the responsibilities of analysis, generation, verification, and application.
-   Associate AI proposals with evidence, test results, and diffs.
-   Define automation authority according to risk.
-   Verify re-observation after application and rollback.
-   Implement detection, isolation, analysis, countermeasures, and report sharing on each individual instance, instance trust, and the update path (minimal diffs and local builds), and validate the threat model (Section 9).

### Phase 5 --- Compatibility Layer (Separate Package)

-   Add support incrementally in the order of statically linked Linux ELF, dynamically linked Linux ELF, and Windows PE (5.7).
-   Implement execution modes (isolation/performance) (5.8).
-   Define removal conditions.

### Phase 6 --- Expansion

-   Add target CPUs.
-   Expand SIMD Native and porting.
-   Add specialized features according to RTOS, gaming, robotics, and other requirements.
-   Establish separate measurement and certification plans for areas requiring real-time behavior or safety.

## 17. Open Issues

The following items require explicit decisions in the future, including to maintain the consistency of the concept.

1.  **Deliverable boundaries among Project-KISS / Project-ACE / AceIS and the ACE component:**
    Project-KISS is the top-level project developing the components and AceIS; Project-ACE is the subproject building AceIS; and AceIS is the integrated IS encompassing ACE/PAUL/GENE/PETER and other components. Documents explicitly distinguish "Project-ACE," "ACE component," "AceIS Core," and "AceIS." The intended division is for AceIS Core to handle overall control and decisions for the integrated system, and for the ACE component to handle reasoning, verification, and derivation of improvement candidates. Detailed responsibility contracts, repositories, and deliverable units remain to be decided.
2.  **Kernel structure:**
    This edition provisionally adopts the logical division of responsibilities into Abiss / A-Nexus / AceIS Core. However, the implementation structure, such as microkernel, monolithic, or hybrid, and the privilege levels and process placement of each function remain undecided.
3.  **Initial target:** The first CPU and execution environment to complete. amd64 would make compatibility-layer verification easier; another CPU would require binary translation from the outset (5.7).
4.  **Compiler strategy:**
    The ace-cc policy is described in Section 10.1. Remaining issues are the bootstrap procedure and verification method for ace-cc self-hosting, and the scope of language features targeted by the first PoC.
5.  **API/ABI:** Scope of POSIX compatibility, custom API/ABI, compatibility, and versioning. Scope of the compatibility layer (static/dynamic ELF, PE), rules for dependency direction relative to the main system, and removal conditions.
6.  **AI execution placement:**
    Local models, external models, models by role, and communication protocols.
7.  **Authority for automatic application:**
    Which changes may be applied automatically and which require human or maintainer approval. The boundary between instance-local mitigation and patches propagated system-wide (9.4).
8.  **Log specification:**
    Event format, record width, retention period, capacity targets, and handling of confidential data.
9.  **C1--C4:** Formal definitions of each level, tools, and CI gates. Definition and scope of the highest level (with MC/DC as a candidate) (11.5).
10. **Test organization:**
    Exceptions when a 1:1 correspondence is the default, and criteria for colocating or separating tests and source.
11. **License text:**
    The formal name, text, abbreviation, avoidance of confusion with existing licenses, and SPDX identifier for AceGeneralPublicLicense; a license inventory for external tools and libraries; license separation for the compatibility layer; and legal review.
12. **Copyright and contribution records:**
    Directory structure, file format, chronological units, and relationship to Git history.
13. **Releases and governance:**
    Component authority, release approval, security fixes, and decision procedures in disputes.
14. **Safety and real-time behavior:**
    What is guaranteed, measurement conditions, verification criteria, and scope of certification. The boundary between what short, microsecond-order verification guarantees and what is assigned to comprehensive verification.
15. **Performance targets:**
    Target values and measurement methods for boot time, build time, test time, memory usage, and similar metrics.
16. **Threat model:**
    Formalization of assets, attacker profiles, trust boundaries, and attack surfaces. Configuration of gates and signers in the acceptance path. Calculation and auditing of instance trust. The authority to revoke permission to use the compatibility layer and the user's override path (Section 9).
17. **Privacy and consent:**
    Scope of shared logs, anonymization, user consent, and applicable laws (9.5).
18. **Execution modes:**
    Definition of isolation/performance modes for applications, protection of direct paths using mechanisms such as IOMMU, and methods of measuring speed (5.8).
19. **Self-improvement sandbox:**
    Methods of limiting interference through CPU, cache, memory bandwidth, and I/O; scope of short-duration verification; criteria for comprehensive verification; and application and recovery procedures (5.9).
20. **Developer and user experience:**
    Observation and experimentation features to provide first, starting with HelloWorld, and metrics for evaluating the engineer experience and end-user experience (2.5, 14, 16).

19. **AIR, debugging, and SIMD specifications:** AIR semantics, Mapping format, Core Dump capture conditions, scope of `-fforce-scalar`, and initial scope of SIMD operations.

## 18. Recording Design Decisions

### 18.1 Recording Method

Future decision-making will distinguish and record settled matters, reasons for adoption, rejected alternatives, and unresolved risks. Do not retrospectively reinterpret past discussions as finalized specifications for convenience.

Record at least the following for each design decision.

-   ID and title
-   Status (proposed / under consideration / decided / retired)
-   Date
-   Background and problem
-   Decision
-   Reasons and constraints
-   Alternatives considered
-   Affected components
-   Verification method and conditions for reconsideration

Manage design-philosophy documents separately by role from implementation specifications, ADRs (Architecture Decision Records), API specifications, test conventions, and license documents. This document is an entry point for understanding the overall picture, not a replacement for individual normative documents.

### 18.2 ADR Candidates

This is a list of candidates before they are recorded in the format of 18.1. All have the status "proposed" and are not decided. "Origin" indicates whether an item is a policy explicitly stated by the designer or a proposal raised in review.

| Candidate | Content | Origin |
|------|------|------|
| ADR-A | Develop ace-cc independently, without incorporating existing compilers or LLVM into artifacts. Use gcc/clang until ace-cc is complete | Policy |
| ADR-B | Separate the compatibility layer from the main system, confine it to userland, and eventually remove it | Policy (dependency direction and removal conditions are proposals) |
| ADR-C | Use a sandbox only when effective speed can be ensured. Handle direct paths through modes | Policy (defaults are proposals) |
| ADR-D | Assume breach. Run detection, isolation, analysis, countermeasures, and sharing through cooperation between the ACE component and AceIS | Policy |
| ADR-E | Obtain minimal diffs for updates, then build, verify, and incorporate them locally on the AceIS side (without assuming OTA distribution of completed images) | Policy |
| ADR-F | Assign contribution and trust scores to individual instances and keep them undisclosed to humans | Policy (audit logs are a proposal) |
| ADR-G | Patch acceptance path (gates, threshold signatures, staged rollout, and protection of the acceptance path) | Proposal |
| ADR-H | Make the highest coverage level the minimum baseline (with MC/DC as a candidate) | Policy (MC/DC is a proposal) |

## 19. Overall Direction

With its philosophy and principles of freedom as its foundation, Project-KISS develops ACE/PAUL/GENE/PETER and other components, as well as AceIS. As a subproject of Project-KISS, Project-ACE designs, implements, and verifies AceIS, which is provided to users as an integrated IS encompassing these components.

At its center is not merely the addition of AI to existing software. It is the creation of a structure in which the system itself can observe its own behavior, retain evidence, verify changes, and generate and optimize as needed.

Autonomy, however, does not mean unlimited authority. Self-improvement becomes a trustworthy system function only when verifiability, record integrity, responsibility boundaries, and user freedom are maintained.

**Project-KISS is responsible for the overall concept and principles; Project-ACE for building AceIS; ACE/PAUL/GENE/PETER for functional responsibilities; and AceIS for the integrated user experience.**

AceIS aims to combine the enjoyment engineers find in building with the enjoyment end users find in using. Autonomous self-improvement connects the two, aiming to support not only performance gains but also understanding, experimentation, adaptation, and freedom.


------------------------------------------------------------------------

## Revision History

This section maintains changes by edition in chronological order. Draft-stage updates leading to the fourth edition and changes made during the fourth-edition refinement are both grouped under the fourth edition's history. History previously scattered as appendices at the end of the text has been consolidated here.

### Second Edition (Changes from the First Edition)

-   Added a legend for labels (Policy / Proposal / Deferred) to distinguish matters explicitly stated by the designer from proposals raised in review.
-   Updated 5.2 and added 5.7 (compatibility layer), 5.8 (execution modes and application sandbox), and 5.9 (self-improvement sandbox).
-   Added Section 9 (Security and Threat Model).
-   Added the ace-cc and libace_rt policies to the compiler section (formerly 9, now 10), and revised the description of a "PoC using an existing toolchain."
-   Added to the coverage section (11.5) the policy of making the highest level the minimum baseline, MC/DC as a candidate, and its scope of application.
-   Added 12.6 (Managing Dependency and Reference Licenses) to the licensing section.
-   Added three items to the non-goals (Section 15).
-   Restructured the proposed stages (Section 16), bringing the thin ACE loop forward to Phase 2 and making the compatibility layer a separate Phase 5.
-   Updated the open issues (Section 17) and added items 16--18. Naming and boundaries (1) were deferred.
-   Changed "user" to "designer" in Section 7.
-   With the addition of Section 9, former Section 9 and subsequent sections were renumbered one higher.

### Third Edition (Changes from the Second Edition)

- Updated the reference date and edition information for the third edition.
- Organized the logical structure of AceIS as **Abiss -> A-Nexus -> AceIS Core**, distinguishing AceIS as a whole from AceIS Core.
- Described Abiss as the minimal HAL/hardware boundary and A-Nexus as the infrastructure for common abstraction, resource mediation, and real-time control.
- Added a policy allowing a direct Abiss access path for necessary hardware-specific features while keeping A-Nexus as the normal path. Explicitly stated that direct access does not mean disabling permissions or protection.
- Set the boot order to Abiss -> A-Nexus -> AceIS Core.
- Added a self-improvement sandbox distinct from the application sandbox. Organized pre-building of candidates, use of idle time, short verification at safe times, comprehensive verification, and observation after application.
- Made microsecond-order local verification a design target and clarified that this does not mean arbitrary changes can be fully verified in a few microseconds. Nanosecond timing is not a universal requirement.
- Added the principle of combining excitement for engineers with excitement for end users, and made an experience of enjoying observation, experimentation, and improvement starting with HelloWorld part of the initial implementation's evaluation.
- Updated the development roadmap, open issues, non-goals, and overall direction to reflect the new layer structure and experience principles.

### Fourth Edition (Changes from the Third-Edition Draft and Fourth-Edition Refinements)

#### Fourth-Edition Draft-Stage Updates (2026-10-12)

- Clarified Project-KISS as the top-level project developing ACE/PAUL/GENE/PETER and other components, as well as AceIS.
- Clarified Project-ACE as the Project-KISS subproject that designs, implements, and verifies AceIS.
- Defined AceIS as the integrated system encompassing ACE/PAUL/GENE/PETER and other components, and removed the expansion "ACE Individual System."
- Established that the name AceIS is based on the concept of IS (Integrated / Intelligence / Individual System), rather than OS. The term "OS" is retained as needed as a general technical classification.
- Distinguished the expansion of Project-ACE, "Autonomous Cognitive Evolution," from ACE as an individual component of AceIS.
- Documented the policy of distinguishing the ACE component, responsible for reasoning, verification, and self-improvement, from AceIS Core, responsible for overall control and decisions for the integrated system. Detailed APIs, execution placement, and responsibility contracts between the two remain open issues.
- Changed the description of ace-cc's initial implementation from "ACE's first phase" to the initial implementation of Project-KISS/Project-ACE to avoid ambiguity in the term ACE.

#### Organization as the Fourth Edition (2026-10-12)

- Updated the document title, edition information, and status description to the fourth-edition draft.
- Explicitly stated at the beginning of the text the hierarchy of Project-KISS (top-level project), Project-ACE (subproject responsible for building AceIS), and AceIS (integrated IS encompassing the components).
- Added to Section 1, "Terminology distinctions," that Project-ACE does not refer only to development of ACE itself. Removed duplicate descriptions in 3.1 and 5.1 and replaced them with references to Section 1.
- Consolidated the distinction between the responsibilities of the ACE component and AceIS Core in Section 1. Detailed APIs, execution placement, authority, and responsibility contracts remain open issues.
- Clarified how unlabeled statements should be treated, and added that statements explicitly updated in later editions take precedence over those in earlier editions.

#### Fourth-Edition Refinement (2026-10-12)

- Updated the document's edition information and status description to "Fourth-Edition Draft, Refined Version" to reflect the reorganization of the text.
- Reviewed the referent of "Ace" in the security section and revised wording to avoid confusing the roles of the ACE component, which handles intelligent functions, and the integrated system AceIS, which builds, verifies, and applies changes.
- Revised the update-method description, clarifying the concept of obtaining diffs and then building, verifying, and incorporating them on the AceIS side. Specific trust boundaries and acceptance conditions for updates remain matters for consideration in Section 9.4.
- Changed `-lc` and `-lgcc` to code formatting so that they read clearly as linker arguments in Markdown.
- Standardized the use of "KISS" and "Project-KISS" in the list of responsibility boundaries in the proposed development stages.
- Aligned the security and update items among ADR candidates with the wording in the body, while retaining their existing treatment as candidates and policies rather than finalized decisions.
- Maintained the policy of not promoting open design issues or proposals to finalized specifications without evidence.

### Fifth Edition (2026-11-07, Changes from the Fourth Edition)

-   Section 10.6: Added the AIR name and the responsibility boundaries of PAUL/GENE/PETER in the compiler PoC.
-   Section 10.7: Added concepts for SIMD-native defaults, an option to force scalar operation, and cross-target specification.
-   Section 10.8: Made postmortem analysis using Core Dump and AIR Mapping the initial debugging path, so that a dedicated debugger is not a blocker. Explicitly stated constraints and verification conditions.
-   Section 10.9: Added a PoC development experiment centered on local LLMs and made environment setup a non-blocker.
-   Updated Phase 1 and the open issues. Existing fourth-edition statements are generally retained.
