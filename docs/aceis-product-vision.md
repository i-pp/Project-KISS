<!--
SPDX-FileCopyrightText: 2026 I-plusplus Inc.
SPDX-License-Identifier: LicenseRef-KOL-v1
-->

# AceIS Product Vision and Engineering Targets

**Status: Vision and design targets.** This is the proposed shared direction for AceIS, not an implementation specification or a release commitment.

## What AceIS Is

AceIS is a new generation of operating system that we call an IS: Integrated / Intelligence / Individual System. SIMD-native AI is part of the system's foundation. We are redesigning how people work, play, and use computers around native intelligence, rather than adding an AI application to an existing OS. The system should handle the complexity of coordination while keeping meaningful decisions and control with the person using it.

An individual AI should grow with its user. It can benefit from updates synchronized with other AI individuals while retaining its own identity.

Separately, explore a hub-based neural network with bypass paths as a communications design goal. Any shorter path must retain the same required protections.

## Engineering Targets

- **Native execution.** Develop the dedicated `acc` compiler and AIR (its intermediate representation) for SIMD-native execution. Use native module objects (`.mo` is working notation) to compose system functions. The object format, execution rules, and ABI remain to be specified.

- **Initial POSIX and Linux compatibility.** Provide an optional compatibility path and guarantee operation only for an explicitly tested subset of Linux applications on named configurations. Define the application list, supported ABIs, and tests before making any compatibility claim. Native components must not depend on the compatibility layer.

- **Real-time scheduling by default.** Make real-time scheduling the default. On suitable devices, aim to run games alongside other work while maintaining defined timing and responsiveness targets. Specify the device profiles, competing workloads, resource budgets, and acceptance tests before promising timing or performance.

- **Growth without loss of individuality.** Define what an AI individual retains, what it may share, what the user controls, and how synchronized updates are checked. The synchronization protocol, exchanged data, and learning method are open design work.

- **Fast and secure communication.** Explore how a neural hub can provide bypass paths that reduce communication overhead without bypassing authorization or protection. Specify what the hub can access, how routes are validated, what happens on failure, and how latency, throughput, and security are tested.

## How To Report Progress

Keep the **product vision**, **initial acceptance targets**, and **verified results** separate. A compiler milestone or working boot component is real progress, but it does not demonstrate a complete IS. Record the tested hardware or emulator, conditions, and reproducible evidence for each result. Keep the existing observation, verification, and improvement cycle; the AI's ability to propose an improvement does not grant it authority to apply changes.

## Related Design Records

- [Project-KISS integrated design and system vision, v5 draft](Project-KISS_design_v5_draft.en.md)

- [Design update for acc, native sysroot, Ace-Core, and verification](design-update-2026-11-07.md)
