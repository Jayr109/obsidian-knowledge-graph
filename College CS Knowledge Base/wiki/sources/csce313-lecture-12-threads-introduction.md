---
title: "CSCE 313 Lecture 12 — Threads Introduction"
type: source
tags: [csce313, threads, pthreads, concurrency, race-conditions, signals]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 12 (announced Mar 4) covers two topics: UNIX signals (the first two-thirds of the lecture) and an introduction to POSIX threads via `pthread_create`/`pthread_join`. The lecture also demonstrates race conditions arising from shared state between threads.

## Part 1: UNIX Signals

### What is a Signal?

A signal is a software interrupt — a notification delivered to a process by the kernel or another process to indicate that an asynchronous event has occurred (e.g., the user pressed Ctrl+C, or a timer expired). Every signal has a name beginning with `SIG`.

Selected signals:
- `SIGABRT` — abort signal (process called `abort()`).
- `SIGALRM` — timer expired (`alarm()`).
- `SIGINT` — terminal interrupt (Ctrl+C).
- `SIGTSTP` — terminal stop (Ctrl+Z) — suspends process.
- `SIGKILL` — unconditional termination (cannot be caught or ignored).
- `SIGSTOP` — unconditional stop (cannot be caught or ignored).
- `SIGCHLD` — child process terminated (ignored by default).
- `SIGSEGV` — invalid memory reference.
- `SIGFPE` — arithmetic exception (divide-by-zero for integers).
- `SIGPIPE` — write to broken pipe.
- `SIGUSR1`, `SIGUSR2` — user-defined.

### Signal Disposition

A process can do one of three things with a signal:
1. **Accept default action** — `signal(SIGINT, SIG_DFL)`. Most signals terminate; `SIGCONT` resumes; `SIGSTOP`/`SIGTSTP` stop.
2. **Ignore** — `signal(SIGINT, SIG_IGN)`. Cannot ignore `SIGKILL` or `SIGSTOP`.
3. **Catch (handle)** — `signal(SIGINT, my_handler)`. Install a custom function.

### Registering a Signal Handler

```c
void sighandler(int signum) {
    printf("Signal caught!\n");
}
signal(SIGINT, sighandler);
```

Preferred (more portable) API: `sigaction()`.
```c
int sigaction(int signo, struct sigaction *act, struct sigaction *oact);
struct sigaction {
    void (*sa_handler)(int);          // handler function
    sigset_t sa_mask;                 // signals to block during handler
    int sa_flags;                     // options
    void (*sa_sigaction)(int, siginfo_t *, void *); // 3-arg handler variant
};
```

### Generating Signals

```c
int kill(pid_t pid, int sig);    // send sig to process/group; pid=-1 → all processes
int raise(int sig);              // send sig to self; equivalent to kill(getpid(), sig)
```

### Signal Sets and Blocking

```c
sigset_t set;
sigemptyset(&set);          // initialize empty set
sigfillset(&set);           // all signals
sigaddset(&set, SIGINT);    // add one signal
sigdelset(&set, SIGINT);    // remove one signal
sigismember(&set, SIGINT);  // test membership
```

`sigprocmask(SIG_BLOCK, &set, &old_set)` — add `set` to the process's blocked signals.  
`sigprocmask(SIG_UNBLOCK, &set, &old_set)` — remove `set` from blocked signals.  
`sigprocmask(SIG_SETMASK, &set, &old_set)` — replace blocked set.

When a signal's handler is invoked, that signal is automatically blocked until the handler returns.

### SIGCHLD: Asynchronous Child Reaping

```c
void my_handler(int sig) {
    pid_t pid;
    while ((pid = waitpid(-1, 0, WNOHANG)) > 0)
        printf("Child %d exited.\n", pid);
}
signal(SIGCHLD, my_handler);
```

### Timer: alarm()

```c
unsigned int alarm(unsigned int seconds);
// Generates SIGALRM after 'seconds'; only one alarm per process.
// Returns 0 or remaining seconds of previous alarm.
// alarm(0) cancels any previous alarm.
```

`pause()` suspends the process until any signal is caught.

## Part 2: Threads Introduction

### What is Concurrency?

Concurrency is the execution of multiple instruction streams at the "same" time (via interleaving on one core or true parallelism on multiple cores).

### What is a Thread?

A thread is a single sequential flow of control within a process. Multiple threads in a process share the same address space but each has its own:
- Stack
- Registers (including `%rip`, `%rsp`)
- Signal mask

They share: heap, global data, code, open file descriptors, signal disposition.

### Motivation for Threads

- **Parallelism** — true parallel execution on multi-core machines.
- **Overlap I/O and computation** — while one thread blocks on I/O, another continues executing. Example: 10 web requests × 100 ms = 1 s with 1 thread; 100 ms with 10 threads.
- **Lower overhead than processes** — thread creation is cheaper; context switch saves only CPU state (not memory/I/O state); sharing is zero-copy.

### POSIX Thread API (pthreads)

```c
#include <pthread.h>

// Create a thread
int pthread_create(pthread_t *tid, const pthread_attr_t *attr,
                   void *(*func)(void *), void *arg);
// Returns 0 on success, positive error code on failure.
// tid: set to the new thread's ID
// attr: NULL for defaults
// func: thread entry function
// arg: argument passed to func

// Wait for a thread
int pthread_join(pthread_t tid, void **status);
// Blocks until thread 'tid' terminates; *status gets the thread's return value

// Exit explicitly
void pthread_exit(void *status);

// Detach (daemon thread — not joinable)
int pthread_detach(pthread_t tid);

// Get own thread ID
pthread_t pthread_self(void);
```

### Race Conditions

A race condition occurs when the output of a concurrent program depends on the relative scheduling order of threads. Example: two threads both executing `x = x + 1` on a shared variable:

```
Case 1 (x=2): T1: load; T1: add; T1: store; T2: load; T2: add; T2: store
Case 2 (x=1): T1: load; T2: load; T1: add; T2: add; T1: store; T2: store (lost update)
```

Instruction reordering by the compiler or CPU can also cause races when threads share data, because a compiler may swap "unrelated" lines without realizing another thread depends on the ordering.

### Thread Safety

A function is **thread-safe** if it can be called concurrently by multiple threads without corruption. Functions using global/static state (e.g., `strtok`, `ctime`, `rand`) are not thread-safe. POSIX provides `_r` (reentrant) variants: `strtok_r`, `ctime_r`, etc.

### Visual Slides

The UNIX signals table (slide p9), thread vs. process comparison table (slide p27), and various diagrams were visual-only.

## See Also

- [[Threads]]
- [[Thread Synchronization]]
- [[Process Attributes]]
- [[Process API]]
- [[CSCE 313]]
