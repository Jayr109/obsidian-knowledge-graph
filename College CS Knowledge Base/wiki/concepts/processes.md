---
title: "Processes"
type: concept
tags: [csce313, processes, pcb, process-states, context-switch, virtual-memory]
sources: [csce313-lecture-01-introduction-to-operating-systems, csce313-lecture-02-architectural-support-for-os, csce313-lecture-08-process-attributes]
course: CSCE 313
updated: 2026-04-10
---

A process is an instance of a running program — the fundamental unit of execution in an operating system. A process is an executing program with restricted rights: it runs in user mode with a private address space, limited access to hardware, and interacts with the OS only through the [[System Calls]] interface.

## What a Process Consists Of

| Component | Contents |
|-----------|----------|
| **Address space** | Code (text), data (globals/statics), heap (dynamic allocation), stack (local vars, return addresses) |
| **CPU state** | Program counter (%rip), stack pointer (%rsp), general-purpose registers |
| **I/O state** | Open file descriptor table, terminal association |
| **OS metadata** | Process Control Block (PCB) |

## Virtual Address Space Layout (64-bit Linux)

```
0xFFFFFFFFFFFF  ← top
  KERNEL        (kernel code and data — inaccessible to user)
0x800000000000
  STACK         (grows downward; local variables, return addresses)
  UNUSED        (unallocated virtual address space)
  HEAP          (grows upward; malloc/new)
  DATA          (global and static variables)
  TEXT (CODE)   (program instructions; read-only)
0x000000000000  ← bottom
```

Each process has its own page table, providing a separate virtual address space even though all processes share the same physical memory.

## Process Lifecycle States

```
          create
            ↓
          ready ←─────────── preempt ──────────┐
            ↓ schedule                          │
          running ──── I/O request ──→ blocked ─┘
            ↓ exit          I/O complete ↑
          terminated
```

| State | Meaning |
|-------|---------|
| **Ready** | Waiting for CPU; can run but not currently scheduled |
| **Running** | Actively executing on a CPU core |
| **Blocked/Waiting** | Waiting for an I/O event or resource |
| **Terminated** | Execution complete; PCB entry remains until parent reaps |

## Process Control Block (PCB)

The OS represents each process with a PCB (Linux: `struct task_struct`). Key fields:

| Field | Purpose |
|-------|---------|
| State | ready / running / blocked / terminated |
| PID | Unique process ID |
| PC / registers | CPU state (saved/restored on context switch) |
| Memory info | Page table pointer, memory limits |
| Open files | File descriptor table |
| UID / GID | User/group identity |
| Parent pointer | Parent process link |
| Priority / scheduling info | CPU scheduler data |
| Signal handling | Pending signals, signal mask, handlers |

## Context Switch

When the OS switches the CPU from one process to another, it:
1. Saves the running process's CPU state (PC, SP, registers) into its PCB.
2. Selects the next process.
3. Loads the next process's CPU state from its PCB.
4. Resumes execution.

Context switches happen 100–1000+ times per second. Cost: saving/restoring CPU state (low) + TLB/cache flush on address space change (potentially high).

## Multitasking

Multiple processes execute concurrently via time-slicing: the OS gives each process brief CPU bursts in rapid succession, creating the illusion of simultaneous execution. True parallelism requires multiple CPU cores.

## Process Creation: fork()

`fork()` creates a new process by duplicating the calling process. The child is an exact copy: same code, data, heap, stack, and open file descriptors — but has a new PID.

Return values: `< 0` (failure), `= 0` (child), `> 0` (parent; value = child's PID).

After fork, parent and child execute independently. Their separate virtual address spaces are backed by copy-on-write pages initially shared with the parent.

## Process Termination

A process terminates when it:
1. Returns from `main()`.
2. Calls `exit()`.
3. Receives a terminating signal.

On termination, the OS closes all file descriptors and frees most resources, but the PCB entry (exit status) persists as a **zombie** until the parent calls `wait()` to reap it.

## Relationship to Threads

A process traditionally contains a single thread of control. [[Threads]] are lighter-weight execution units within a process that share the process's address space but each have their own stack and register state.

## See Also

- [[Virtual Memory]]
- [[System Calls]]
- [[Process API]]
- [[Process Attributes]]
- [[Threads]]
- [[Operating Systems]]
- [[CSCE 313]]
