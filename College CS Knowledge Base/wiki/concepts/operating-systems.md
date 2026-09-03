---
title: "Operating Systems"
type: concept
tags: [operating-systems, csce313, abstraction, virtualization, protection]
sources: [csce313-lecture-01-introduction-to-operating-systems, csce313-lecture-02-architectural-support-for-os]
course: CSCE 313
updated: 2026-04-10
---

An operating system (OS) is the layer of software that interfaces between diverse hardware resources and the many applications running on a machine. It implements a virtual machine for each application whose interface is more convenient, secure, reliable, and portable than the raw hardware interface.

## Three Core Roles ("Three Hats")

Every OS serves three fundamental roles simultaneously:

| Role | Description | Example |
|------|-------------|---------|
| **Illusionist** | Provides clean, easy-to-use abstractions of physical resources | Each process sees a private address space; each has a seemingly dedicated CPU |
| **Referee** | Manages protection, isolation, and fair sharing among competing processes | Memory isolation prevents one process from reading another's memory |
| **Glue** | Provides common services usable by all programs | File systems, network stacks, system call interfaces |

## What the OS Abstracts

| Physical Resource | OS Abstraction |
|------------------|----------------|
| CPU | Process / Thread |
| Physical memory | Virtual address space (per process) |
| Disk | File / File system |
| Network interface | Socket |
| Hardware clock | Timer / alarm |

## Hardware Requirements

An OS can only enforce its policies if the hardware cooperates. The four required hardware mechanisms are:

1. **Privilege levels** — instructions restricted to kernel mode (ring 0) cannot execute in user mode (ring 3).
2. **Memory isolation** — the MMU (Memory Management Unit) translates virtual addresses through page tables and generates faults on unauthorized accesses.
3. **Interrupts** — hardware can deliver an asynchronous notification to the kernel at any time, allowing the OS to regain control.
4. **Safe mode transfers** — the kernel defines entry points (interrupt vector table) so user code cannot jump to arbitrary kernel addresses.

## Kernel vs. User Mode

Processes run in **user mode** (CPL=3 on x86): restricted from executing privileged instructions and accessing kernel memory. The OS kernel runs in **kernel mode** (CPL=0): full access to all hardware. Mode switches occur via:
- Interrupts (hardware-triggered, asynchronous).
- Exceptions/faults (CPU-triggered, synchronous — e.g., page fault, divide-by-zero).
- System calls / traps (program-triggered, synchronous — e.g., `INT 0x80`, `syscall`).

## OS as Government Analogy

The OS does no useful computational work itself; it legislates on resource use by competing applications and enforces fairness policies — analogous to a government that facilitates rather than produces (Prof. Mortier, Cambridge).

## UNIX/Linux

Linux (created by Linus Torvalds in 1991, GPL-licensed in 1992) is the dominant OS for servers, HPC clusters, and mobile (Android). CSCE 313 uses Linux and the POSIX API as its concrete OS.

## Key Concepts in CSCE 313

- [[Processes]] — the fundamental unit of execution.
- [[Virtual Memory]] — per-process address space abstraction.
- [[System Calls]] — the interface between user programs and the OS.
- [[Interrupts and Exceptions]] — hardware/software event delivery.
- [[File Systems]] — persistent named storage.
- [[Threads]] — concurrent execution within a process.

## See Also

- [[Processes]]
- [[Virtual Memory]]
- [[System Calls]]
- [[Interrupts and Exceptions]]
- [[CSCE 313]]
