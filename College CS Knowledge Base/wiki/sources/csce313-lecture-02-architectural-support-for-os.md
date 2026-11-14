---
title: "CSCE 313 Lecture 2 — Architectural Support for Operating Systems"
type: source
tags: [csce313, operating-systems, interrupts, exceptions, system-calls, privilege-levels]
sources: []
course: CSCE 313
updated: 2026-09-13
---

Lecture 2 covers the hardware mechanisms that allow an OS to enforce isolation between user processes and the kernel. Topics include privilege levels (rings), virtual memory isolation, interrupts and exceptions, and the system call interface. Reference: OSSTEP Chapter 6. Slides adapted from Crooks & Zaharia CS162 (UCB) and Prof. Mortier (Cambridge).

## Hardware Requirements for OS Operation

The OS relies on four hardware mechanisms:

1. **Privileged instructions** — unsafe instructions cannot execute in user mode (CPL ≠ 0).
2. **Memory isolation** — memory accesses outside a process's address space are prohibited (enforced via virtual memory and page tables).
3. **Interrupts** — the kernel can regain control from a running process at any time.
4. **Safe transfers** — control transitions from user mode to kernel mode (and back) follow a defined protocol.

## Privilege Levels

x86 processors define a Current Privilege Level (CPL) stored in bits of the code segment register. CPL=0 is the most privileged (OS/kernel) mode; CPL=3 is user mode. The general model is extended to four "rings" (0–3), where lower ring number means higher privilege.

## Interrupts and Exceptions

**Hardware Interrupts.** Asynchronous signals from I/O devices (e.g., timers, network cards). Guaranteed to be taken on an instruction boundary (Intel Vol 3A §6-6). The kernel initializes an interrupt vector table; upon receipt, the processor saves `%rflags`, `%cs`, `%rip` on the stack and transfers control to the handler. The handler saves all registers, services the device, restores registers, and returns with `iret` (restoring `%rflags + %cs + %rip`).

**Software Interrupts / System Calls.** Synchronous, explicit instruction (`INT 0x80` in 32-bit Linux, `syscall` in 64-bit). Used to request OS services. The OS associates a handler address with each exception number, preventing user code from jumping to arbitrary kernel addresses.

**Exceptions.** Synchronous events triggered by instruction execution:
- **Faults** — recoverable; %rip points to the faulting instruction (e.g., page fault, segfault). May restart.
- **Aborts** — severe, unrecoverable (e.g., hardware failure, ECC checksum error). Does not return.
- **Traps** — intentional synchronous interrupt from user code (e.g., `INT 3`, `SYSCALL`).

**Intel Exception Numbers (selected):**
| # | Type | Description |
|---|------|-------------|
| 0 | Fault | Divide error |
| 13 | Fault | Segmentation fault |
| 14 | Fault | Page fault |
| 18 | Abort | Machine check |
| 128 | Trap | Old-style system call (INT 0x80) |
| 32–127, 129–255 | Interrupt/Trap | OS-defined |

## Exception Examples

**Page Fault (recoverable):** On access to an unmapped page, the kernel's page fault handler allocates the page and updates the page table, then restarts the faulting instruction.

**Illegal Memory Reference (SIGSEGV):** On an out-of-bounds access, the page fault handler detects the invalid address and sends `SIGSEGV` to the process.

**Abort:** Machine check, memory parity errors — current program is killed and control handed to OS.

## System Calls

A trap is a synchronous interrupt intentionally triggered by a user process to request OS services (e.g., more memory, I/O). System calls provide a function-call-like interface between application and OS.

**32-bit Linux:** Load syscall number in `eax`; load args in `ebx`, `ecx`, `edx`, `esi`, `edi`, `ebp`; invoke `int 0x80`; return value in `eax`.

**64-bit Linux:** Load syscall number in `%rax`; load args in `%rdi`, `%rsi`, `%rdx`, `%r10`, `%r8`, `%r9`; invoke `syscall`; return value in `%rax`.

**System Call Flow (example: `open`):**
1. User stub sets `%rax = SYSOPEN (= 2)` and executes `trap`.
2. Kernel stub copies args from user memory, validates them, calls `open_handler(arg1, arg2)`.
3. Handler performs the actual file open.
4. Return value placed in `%rax`; control returns to user stub.

**Types of System Calls:** Process control (`fork`, `exec`, `exit`, `wait`), file management (`open`, `close`, `read`, `write`), device management, information maintenance, and communication.

**stdin/stdout/stderr.** Every process starts with three open file descriptors: 0 (stdin), 1 (stdout), 2 (stderr), corresponding to C's `cin`/`cout`/`cerr`.

## Exception Class Summary

| Class | Cause | Sync/Async | Return Behavior |
|-------|-------|-----------|-----------------|
| Interrupt | I/O device signal | Async | Return to next instruction |
| Fault | Unintentional, recoverable | Sync | Maybe return to current instruction |
| Abort | Unintentional, non-recoverable | Sync | Do not return |
| Trap / Syscall | Intentional from user | Sync | Return to next instruction |

## Visual Slides

Diagram slides captured minimally: privilege ring diagram, virtual memory layout, interrupt/exception control flow diagram, system call invocation diagram.

## See Also

- [[Interrupts and Exceptions]]
- [[System Calls]]
- [[Virtual Memory]]
- [[Processes]]
- [[CSCE 313]]
- [[Operating Systems]]
