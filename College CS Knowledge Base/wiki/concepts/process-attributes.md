---
title: "Process Attributes"
type: concept
tags: [csce313, process-attributes, pid, uid, gid, signals, sessions, context-switch]
sources: [csce313-lecture-08-process-attributes, csce313-lecture-12-threads-introduction]
course: CSCE 313
updated: 2026-04-10
---

Process attributes are the OS-maintained properties that characterize a process's identity, security context, resource accounting, and execution state. These are stored in the Process Control Block (PCB) and determine how the scheduler, access control system, and signal delivery mechanism treat the process.

## Identity

| Attribute | API | Description |
|-----------|-----|-------------|
| **PID** | `getpid()` | Unique process identifier. Assigned sequentially; recycled after termination. |
| **PPID** | `getppid()` | Parent process ID. |
| **PGRP** | `getpgrp()` | Process group ID. Signals can be sent to all processes in a group. |
| **Session** | `getsid()` | Session ID. A session is a collection of process groups (e.g., all processes in a terminal window). |

## Security Context

| Attribute | Description |
|-----------|-------------|
| **UID / EUID / SUID** | Real user ID, effective user ID (used for permission checks), saved UID. `setuid` executables can elevate EUID to file owner's UID. |
| **GID / EGID / SGID** | Analogous group IDs. |
| **Capabilities** | Fine-grained kernel privileges (beyond simple root/non-root). Stored in `cap_effective`, `cap_inheritable`, `cap_permitted` in the PCB. |

## CPU State (Saved on Context Switch)

| Field | Description |
|-------|-------------|
| Program counter (%rip) | Address of next instruction |
| Stack pointer (%rsp) | Top of the current stack frame |
| General-purpose registers | %rax, %rbx, %rcx, %rdx, %rsi, %rdi, %r8–%r15 |
| Condition codes (%rflags) | Result flags (zero, sign, carry, overflow) |
| Segment registers | %cs (code segment, encodes CPL), %ss, etc. |

## Scheduling Information

Stored in PCB: process priority, scheduling class (SCHED_NORMAL, SCHED_FIFO, SCHED_RR), pointers to run queue. The kernel's CPU scheduler selects from the run queue using this information.

## Memory Information

- Page table base pointer (CR3 on x86).
- Memory limits (stack size, heap size).
- Memory-mapped regions.

## Signals: The Full API

Signals are the primary mechanism for asynchronous event delivery to processes.

### Signal Disposition

```c
signal(signo, SIG_DFL);     // restore default action
signal(signo, SIG_IGN);     // ignore signal (not SIGKILL or SIGSTOP)
signal(signo, my_handler);  // install custom handler
```

Preferred API for more control:
```c
struct sigaction {
    void (*sa_handler)(int);
    sigset_t sa_mask;         // signals to block during handler
    int sa_flags;             // SA_RESTART, SA_SIGINFO, SA_NOCLDWAIT, etc.
    void (*sa_sigaction)(int, siginfo_t *, void *); // 3-arg variant
};
int sigaction(int signo, struct sigaction *act, struct sigaction *oact);
```

### Sending Signals

```c
int kill(pid_t pid, int sig);   // send to process (pid > 0) or group (pid < 0) or all (pid == -1)
int raise(int sig);              // send to self; equivalent to kill(getpid(), sig)
unsigned int alarm(unsigned int seconds); // schedule SIGALRM; cancels previous; alarm(0) cancels
int pause(void);                 // suspend until any signal arrives
```

### Signal Sets and Masking

```c
sigset_t set;
sigemptyset(&set);              // clear all
sigfillset(&set);               // set all
sigaddset(&set, SIGINT);        // add one
sigdelset(&set, SIGINT);        // remove one
int sigprocmask(int how, const sigset_t *set, sigset_t *old);
// how: SIG_BLOCK, SIG_UNBLOCK, SIG_SETMASK
```

The **signal mask** is the set of signals currently blocked for the process. A signal handler automatically blocks its own signal type while running (prevents re-entrancy).

### Common Signals

| Signal | Default | Common Cause |
|--------|---------|--------------|
| SIGINT (2) | Terminate | Ctrl+C |
| SIGKILL (9) | Terminate | `kill -9`; cannot be caught |
| SIGSEGV (11) | Core dump | Invalid memory access |
| SIGTERM (15) | Terminate | Graceful shutdown request |
| SIGCHLD (17) | Ignore | Child terminated |
| SIGSTOP (19) | Stop | Unconditional stop; cannot be caught |
| SIGTSTP (20) | Stop | Ctrl+Z terminal stop |
| SIGCONT (18) | Continue | Resume stopped process |
| SIGPIPE (13) | Terminate | Write to pipe with no reader |
| SIGALRM (14) | Terminate | Timer expired |

## Context Switch Mechanics

When the OS preempts a process, it:
1. Saves all CPU registers to the PCB.
2. Updates the process state (running → ready or blocked).
3. Selects the next process from the run queue.
4. Loads the next process's CPU registers from its PCB.
5. Updates CR3 (page table base) → TLB flush.
6. Resumes execution.

Cost: CPU state save/restore is fast; TLB flush on address space change is the dominant cost.

## See Also

- [[Processes]]
- [[Process API]]
- [[Interrupts and Exceptions]]
- [[Virtual Memory]]
- [[CSCE 313]]
