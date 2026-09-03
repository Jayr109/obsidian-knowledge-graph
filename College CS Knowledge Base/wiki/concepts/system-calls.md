---
title: "System Calls"
type: concept
tags: [csce313, system-calls, traps, kernel-mode, posix, abi]
sources: [csce313-lecture-02-architectural-support-for-os]
course: CSCE 313
updated: 2026-04-10
---

A system call (syscall) is the mechanism by which a user-space process requests a service from the OS kernel. System calls provide a controlled gateway from user mode (CPL=3) to kernel mode (CPL=0), allowing programs to perform privileged operations — file I/O, process creation, memory allocation, network communication — safely.

## Mechanism

A system call is implemented as a **trap**: a synchronous software interrupt intentionally triggered by the user program. The processor atomically:
1. Saves the current instruction pointer, stack pointer, and flags.
2. Switches from user mode (CPL=3) to kernel mode (CPL=0).
3. Transfers control to the kernel's trap handler (via the interrupt vector table).

The OS associates a handler address with each syscall number, preventing user code from jumping to arbitrary kernel locations.

## Calling Convention

### 64-bit Linux (x86-64)
1. Load syscall number into `%rax`.
2. Load up to 6 arguments into `%rdi`, `%rsi`, `%rdx`, `%r10`, `%r8`, `%r9`.
3. Execute `syscall` instruction.
4. Return value is in `%rax` (negative values encode errno).

### 32-bit Linux (legacy)
1. Load syscall number into `eax`.
2. Load arguments into `ebx`, `ecx`, `edx`, `esi`, `edi`, `ebp`.
3. Execute `int 0x80`.
4. Return value in `eax`.

## System Call Flow (example: `open`)

```
User program calls open("test", "rw")
  ↓
User stub (libc wrapper):
  - Set %rax = SYSOPEN (= 2)
  - Set argument registers
  - Execute syscall instruction   ← privilege switch here
  ↓
Kernel trap handler:
  - Copy args from user memory
  - Validate args (security check)
  - Call open_handler(arg1, arg2)
  - Place return value in %rax
  - iret (return to user mode)
  ↓
User stub: read %rax as return value
```

## Standard System Calls by Category

| Category | Examples |
|----------|----------|
| **Process control** | `fork`, `exec`, `exit`, `wait`, `kill`, `getpid` |
| **File management** | `open`, `close`, `read`, `write`, `lseek`, `stat`, `unlink` |
| **Device management** | `ioctl`, request/release device |
| **Information maintenance** | `getpid`, `alarm`, `sleep`, `time` |
| **Communication** | `pipe`, `socket`, `bind`, `connect`, `accept`, `send`, `recv` |
| **Memory** | `mmap`, `brk` (heap management) |

## stdin, stdout, stderr

Every UNIX process is created with three open file descriptors:
- **0** — stdin (standard input)
- **1** — stdout (standard output)
- **2** — stderr (standard error)

These correspond to C's `stdin`/`stdout`/`stderr` streams and C++'s `cin`/`cout`/`cerr`.

## System Call vs. Library Function

Library functions (e.g., `printf`, `fopen`) run in user space and may internally invoke system calls. `printf` eventually calls `write(1, ...)`. Developers typically use library wrappers rather than invoking syscalls directly, but low-level systems programming often calls syscalls directly via their libc wrappers (`open`, `read`, `write`).

## Performance

Each syscall incurs a mode switch (user → kernel → user), which costs on the order of hundreds of nanoseconds. Minimizing unnecessary syscalls (e.g., via buffering in stdio) is important for performance.

## See Also

- [[Operating Systems]]
- [[Interrupts and Exceptions]]
- [[Processes]]
- [[UNIX File I/O]]
- [[CSCE 313]]
