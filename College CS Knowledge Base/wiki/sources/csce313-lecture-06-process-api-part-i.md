---
title: "CSCE 313 Lecture 6 — Process API Part I"
type: source
tags: [csce313, processes, fork, exec, process-api]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 6 covers the UNIX process API, focusing on the `exec` family of functions and the combined use of `fork()` + `exec()` to create new processes that run different programs. References: APUE §8.3, §8.10; OSSTEP §5.1–5.3; SPiL Chapter 11.

## The Process API

Common process operations in operating systems:
- **Create** — launch a new process (e.g., typing a shell command).
- **Destroy** — forcibly terminate a runaway process.
- **Reap** — collect exit status of terminated children (e.g., shell waits for child).
- **Control** — suspend, resume, change priority.
- **Status** — query runtime, memory usage, state.

The UNIX process API provides four system calls: `fork()`, `exec()`, `wait()`, and `exit()`.

## The exec() System Call

`exec()` loads a different program into the current process. It replaces the process's code, data, stack, and heap with the new program's image. The process retains its PID, open file descriptors, environment, and current directory.

**Key behavior:** `exec` does not return on success. If the code after `execvp(...)` runs, the call failed.

```c
char *args[] = { "ls", "-l", "-a", NULL };
execvp(args[0], args);
// This line only runs if exec fails
printf("======AFTER========\n");
```

## exec Family of Functions

Six variants, differing in how the path and arguments are specified:

```c
int execl (const char *path, const char *arg, ...);       // list args, full path
int execlp(const char *file, const char *arg, ...);       // list args, uses PATH
int execle(const char *path, const char *arg, ..., char *const envp[]); // list args + env
int execv (const char *path, char *const argv[]);         // vector args, full path
int execvp(const char *file, char *const argv[]);         // vector args, uses PATH
int execve(const char *path, char *const argv[], char *const envp[]); // vector args + env
```

Naming convention:
- `l` (list) vs. `v` (vector) — how arguments are passed.
- `p` — search `PATH` environment variable for the executable.
- `e` — pass a custom environment array `envp[]`.

All variants internally call `execve(2)`, which is the actual syscall.

## fork() + exec() Pattern

Running a new program without destroying the current one requires `fork()` first:

1. `fork()` duplicates the current process, creating a child with the same address space.
2. The child calls `exec()` to replace itself with the new program.
3. The parent may call `wait()` or `waitpid()` to synchronize.

**Shell command interpreter pattern:**

```c
while (true) {
    command = read_command(stdin);
    if (command == "exit") break;
    if ((pid = fork()) > 0) {
        waitpid(pid, &status, 0);   // parent waits for child
    } else {
        execvp(command, ...);       // child runs the command
    }
}
```

Without `fork()`, `execvp()` would overwrite the shell's own image and the loop would be lost.

## Process States (Programmer's View)

From the programmer's perspective, a process is in one of three states:
- **Running** — executing on CPU or in the run queue.
- **Stopped** — suspended (received SIGSTOP, SIGTSTP, SIGTTIN, or SIGTTOU); resumes on SIGCONT.
- **Terminated** — stopped permanently; caused by (1) a terminating signal, (2) returning from `main()`, or (3) calling `exit()`.

## Visual Slides

Diagrams showing memory before/after `execvp()` (slides p7–p8) and the relationship between the six exec functions (slide p15) were visual-only. The `fork()` return value semantics (< 0 failure, = 0 child, > 0 parent receiving child PID) are shown in diagrams.

## See Also

- [[Process API]]
- [[Processes]]
- [[Pipes and FIFO]]
- [[CSCE 313]]
