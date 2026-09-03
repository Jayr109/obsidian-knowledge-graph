---
title: "CSCE 313 Lecture 7 — Process API Part II"
type: source
tags: [csce313, processes, wait, zombie-processes, signals, process-api]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 7 completes the process API coverage with `wait()`/`waitpid()` for parent-child synchronization, the zombie process problem, and three methods for zombie prevention: `wait()`, ignoring SIGCHLD, and a SIGCHLD signal handler.

## Process Synchronization with wait()

After `fork()`, the parent and child execute independently. Without synchronization, their execution order is non-deterministic.

```c
pid_t waitpid(pid_t pid, int *status, int options);
```

- `pid`: target process ID. `-1` means any child.
- `status`: pointer to an int where the child's exit information is written (`NULL` if not needed). Use `WEXITSTATUS(status)` to extract the exit code.
- `options`: bit flags. `0` blocks until the target terminates. `WNOHANG` returns immediately if no child has exited.

A simpler form:
```c
pid_t wait(int *status);  // equivalent to waitpid(-1, &status, 0)
```

`wait()` blocks the parent until any child terminates, then returns the child's PID.

## Zombie Processes

When a child process terminates, its PCB (Process Control Block) entry remains in the process table until the parent calls `wait()` to "reap" it. If the parent never calls `wait()`, the dead child becomes a **zombie process**: it holds no resources except a PCB slot, but that slot is never reclaimed.

**Consequences:** Multiple zombies fill the process table (finite size), preventing new processes from being created — a resource leak.

**Fork bomb example** (creates infinite zombies):
```c
while(1) fork();
```

## Zombie Prevention

Three methods:

### 1. Explicit wait() call
```c
wait(NULL);  // parent blocks until any child exits
```
The child's PCB is immediately reaped.

### 2. Ignoring SIGCHLD with SIG_IGN
```c
signal(SIGCHLD, SIG_IGN);
```
Tells the kernel to automatically discard child exit status; no zombie is created.

### 3. SIGCHLD signal handler
```c
void func(int signum) {
    wait(NULL);  // reap inside handler
}
signal(SIGCHLD, func);
```
When a child terminates, the kernel delivers SIGCHLD to the parent, which invokes `func`, which calls `wait()` asynchronously. To handle multiple simultaneous child exits, use a loop:
```c
void my_handler(int sig) {
    pid_t pid;
    while ((pid = waitpid(-1, 0, WNOHANG)) > 0)
        printf("Child %d exited.\n", pid);
}
```

## Reparenting

When a parent process is killed while a zombie child exists, the zombie is **reparented** to `init` (PID 1), which periodically calls `wait()` to reap orphans. This is why killing the parent clears the zombie.

## Key Behavior Details

- A zombie cannot be killed directly with `kill -9` — it holds no resources to kill.
- Killing the parent causes all its zombie children to be adopted by init and reaped.
- `waitpid` on a specific PID blocks only for that child; `wait` reaps any child in order of completion.
- Process IDs are assigned sequentially and recycled after termination.

## Visual Slides

The parent-child synchronization timeline diagram (slide p6), zombie comic (slide p10), and context switch diagrams were visual-only.

## See Also

- [[Process API]]
- [[Processes]]
- [[Process Attributes]]
- [[CSCE 313]]
