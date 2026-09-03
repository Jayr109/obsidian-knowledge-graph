---
title: "Process API"
type: concept
tags: [csce313, process-api, fork, exec, wait, exit, zombie]
sources: [csce313-lecture-06-process-api-part-i, csce313-lecture-07-process-api-part-ii, csce313-lecture-05-ipc-pipes-and-fifo]
course: CSCE 313
updated: 2026-04-10
---

The UNIX process API is the set of system calls for creating, running, and managing processes. The four core syscalls are `fork()`, `exec()`, `wait()`/`waitpid()`, and `exit()`.

## fork() — Create a New Process

```c
#include <unistd.h>
pid_t fork(void);
```

Creates an exact copy of the calling process. The child inherits the parent's address space (copy-on-write), open file descriptors, signal handlers, and environment.

**Return values:**
- `< 0` — fork failed; no child created.
- `= 0` — executing in the child process.
- `> 0` — executing in the parent; value is the child's PID.

After fork, parent and child run independently. Scheduling order is non-deterministic.

**Exponential fork:** n calls to `fork()` with no conditional branching create 2ⁿ processes.

## exec() — Replace Process Image

The exec family loads a new program into the current process, replacing code, data, stack, and heap. The process retains its PID, open FDs, working directory, and environment.

```c
int execvp(const char *file, char *const argv[]); // most common
int execv (const char *path, char *const argv[]);
int execl (const char *path, const char *arg, ...);
int execlp(const char *file, const char *arg, ...);
int execle(const char *path, const char *arg, ..., char *const envp[]);
int execve(const char *path, char *const argv[], char *const envp[]); // actual syscall
```

**`exec` does not return on success.** Code after `execvp(...)` runs only if exec failed.

## wait() / waitpid() — Synchronize with Child

```c
pid_t wait(int *status);
// Equivalent to: waitpid(-1, status, 0)
// Blocks until ANY child terminates; returns child's PID.

pid_t waitpid(pid_t pid, int *status, int options);
// pid: specific child PID, or -1 for any child
// status: pointer to exit info (or NULL)
// options: 0 = block; WNOHANG = non-blocking
```

**Extracting exit code:** `WEXITSTATUS(status)` (valid when `WIFEXITED(status)` is true).

## exit() — Terminate a Process

```c
void exit(int status);  // C library (flushes stdio buffers)
void _exit(int status); // raw syscall (no cleanup)
```

A process also terminates on `return` from `main()` or receipt of a terminating signal.

## fork() + exec() Pattern

The canonical way to run a new program from an existing process:

```c
pid_t pid = fork();
if (pid == 0) {
    // child: replace image with new program
    execvp("ls", args);
    perror("exec failed");
    exit(1);
} else {
    // parent: wait for child to finish
    waitpid(pid, &status, 0);
}
```

The shell uses exactly this pattern to run every command.

## Zombie Processes

A **zombie** is a process that has terminated but whose PCB has not been reaped. It holds no resources except a process table slot. Multiple zombies fill the (finite) process table.

**Prevention methods:**
1. Call `wait()` / `waitpid()` after each `fork()`.
2. `signal(SIGCHLD, SIG_IGN)` — kernel auto-reaps children.
3. Install a SIGCHLD handler that calls `waitpid(-1, 0, WNOHANG)` in a loop.

**Reparenting:** When a parent exits with zombie children, those zombies are adopted by `init` (PID 1), which periodically reaps them.

## Process States

```
Running → Stopped: SIGSTOP, SIGTSTP, SIGTTIN, SIGTTOU
Stopped → Running: SIGCONT
Running → Terminated: exit(), return from main, terminating signal
```

## Signal Basics

Signals are software interrupts. A process can:
- **Accept the default** action (`signal(SIGINT, SIG_DFL)`).
- **Ignore** (`signal(SIGINT, SIG_IGN)`) — not for SIGKILL/SIGSTOP.
- **Catch** with a handler (`signal(SIGINT, my_handler)`).

See [[Process Attributes]] for the full signal API.

## See Also

- [[Processes]]
- [[Process Attributes]]
- [[Pipes and FIFO]]
- [[Inter-Process Communication]]
- [[CSCE 313]]
