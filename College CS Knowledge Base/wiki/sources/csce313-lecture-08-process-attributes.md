---
title: "CSCE 313 Lecture 8 — Process Attributes"
type: source
tags: [csce313, processes, pcb, context-switch, scheduling, threads]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 8 covers process attributes (PCB fields), the process lifecycle state machine, context switching mechanics, and closes with an introduction to user-level thread switching via `swapcontext`/`makecontext`. Instructor attribution: Houngninou (guest lecturer sections).

## Memory Regions of a Process

| Region | Contents |
|--------|----------|
| **Stack** | Function parameters, return addresses, local variables |
| **Heap** | Dynamically allocated memory (`malloc`/`new`) |
| **Text** | Program code; program counter and register values |
| **Data** | Global and static variables |

## Process Lifecycle States

| State | Description |
|-------|-------------|
| **Start** | Initial state on process creation |
| **Ready** | Waiting for CPU; OS scheduler selects from this queue |
| **Running** | Actively executing on CPU |
| **Waiting/Blocked** | Waiting for an I/O event or resource |
| **Terminated** | Finished; waiting to be removed from memory |

State transitions: create → ready → running (scheduled) → blocked (I/O request) → ready (I/O complete) → running → terminated (preempt sends running → ready).

## Process Control Block (PCB)

The OS represents each process in the kernel with a PCB (also called `task_struct` in Linux). Fields include:

| Field | Purpose |
|-------|---------|
| Process state | ready / running / blocked / terminated |
| Process privileges | access control |
| Process ID (PID) | unique identifier |
| Pointer | pointer to parent process |
| Program counter | address of next instruction |
| CPU registers | general-purpose registers for context save/restore |
| CPU scheduling info | priority, scheduling queue pointers |
| Memory management info | page table pointer, memory limits |
| Accounting info | CPU time used, time limits |
| I/O status info | list of open I/O devices |

Linux's `struct task_struct` includes fields: `state`, `flags`, `run_list`, `next_task`/`prev_task`, `mm_struct`, `exit_code`/`exit_signal`, `pid`/`pgrp`/`session`, parent/child/sibling pointers, `thread_group`, `uid`/`euid`/`suid`/`fsuid`, `gid`/`egid`, signal handling structures, and `thread_struct` (CPU-specific state).

## Context Switch

A **context switch** is the mechanism by which the OS saves the CPU state of the current process into its PCB and loads the state of a different process from that process's PCB. Steps:

1. Running process is preempted (via timer interrupt or voluntary yield).
2. OS saves `%rip`, `%rsp`, all callee-saved registers into PCB.
3. OS loads the register values from the new process's PCB.
4. Execution resumes in the new process.

Context switches happen 100–1000+ times per second.

**Low-level mechanism (`ctxsw`):**
```asm
ctxsw:
    push %rdi; push %rsi; push %rbp; push %rbx; push %r12; push %r13; push %r14
    mov %rsp, (%rdi)    # save current stack pointer in from_sp
    mov (%rsi), %rsp    # restore new stack pointer from to_sp
    pop %r14; pop %r13; pop %r12; pop %rbx; pop %rbp; pop %rsi; pop %rdi
    ret                 # return to caller of ctxsw in the new thread
```

`%rdi = from_sp` (where to save old SP), `%rsi = to_sp` (where to load new SP).

## User-Level Thread Switching (Lab 3 Preview)

The lecture introduces POSIX `ucontext` primitives for user-space cooperative threading:
- `getcontext(&uctx)` — copies the caller's current CPU context.
- `makecontext(&uctx, func, 0)` — crafts a new stack frame for `func`.
- `swapcontext(&from, &to)` — saves current context into `from`, restores `to`.

A `t_yield()` cooperative yield function uses `swapcontext` to switch between threads stored in a proc table array. No preemption; no true parallelism; user-space switching only. The "other" thread returns from the `swapcontext` call it previously made.

## Thread Preview

A thread has: its own stack, its own register state. Threads share: address space, data, code, open files, signal disposition. Full thread coverage is in [[CSCE 313 Lecture 12 — Threads Introduction]].

## Visual Slides

State machine diagram (slide p8), context switch timeline diagram (slides p15–p18), and ctxsw register layout (slide p19) were visual-only or had garbled text extraction from diagram labels.

## See Also

- [[Processes]]
- [[Process Attributes]]
- [[Process API]]
- [[Threads]]
- [[CSCE 313]]
