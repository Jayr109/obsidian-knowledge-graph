---
title: "Threads"
type: concept
tags: [csce313, threads, pthreads, concurrency, parallelism, context-switch]
sources: [csce313-lecture-12-threads-introduction, csce313-lecture-14-thread-synchronization-i-mutexes]
course: CSCE 313
updated: 2026-04-10
---

A thread is a single sequential flow of control within a process. Multiple threads within a process share the same address space but execute independently, each with its own stack and register state. Threads are the primary mechanism for exploiting parallelism and overlapping I/O with computation within a single program.

## Thread vs. Process

| Property | Thread | Process |
|----------|--------|---------|
| Address space | Shared with all threads in process | Private |
| Stack | Private | Private |
| Register state | Private | Private |
| Open files | Shared | Inherited on fork; otherwise separate |
| Global data / heap | Shared | Private (copy-on-write) |
| Creation cost | Low | High |
| Context switch cost | Low (only CPU state) | High (TLB flush + memory state) |
| Communication | Direct shared memory | IPC (pipes, sockets, etc.) |
| Fault isolation | None (one thread crash kills all) | Full (OS isolation) |

## Thread Private vs. Shared State

**Each thread has its own:**
- Stack (local variables, function call frames).
- Registers (`%rip`, `%rsp`, general-purpose registers).
- Signal mask.

**All threads in a process share:**
- Virtual address space (code + heap + globals).
- Open file descriptor table.
- Signal disposition.

## Motivation

1. **Parallelism** — on multi-core hardware, threads run simultaneously on separate cores.
2. **I/O overlap** — while one thread blocks on I/O, other threads continue executing. Example: 10 concurrent 100 ms HTTP requests take ~100 ms with 10 threads vs. 1000 ms with 1 thread.
3. **Lower overhead than processes** — thread creation is ~10× cheaper than `fork()`; context switches only save/restore CPU state.

## Thread Context Switch

Switching between threads in the same process:
- Save current thread's registers (PC, SP, GP regs).
- Restore next thread's registers.
- **No** page table switch (same address space).
- **No** TLB flush.

Much cheaper than a process context switch, which requires changing the page table and flushing TLBs.

## POSIX Thread API (pthreads)

```c
#include <pthread.h>

// Create
int pthread_create(pthread_t *tid, const pthread_attr_t *attr,
                   void *(*func)(void *), void *arg);

// Join (wait for termination)
int pthread_join(pthread_t tid, void **status);

// Exit (from within thread)
void pthread_exit(void *status);

// Detach (make non-joinable — daemon thread)
int pthread_detach(pthread_t tid);

// Get self ID
pthread_t pthread_self(void);

// Cancel another thread (at cancellation points)
int pthread_cancel(pthread_t tid);
```

**pthread_create:** `func` is called in a new thread with `arg` as its argument. `tid` is set to the new thread's identifier. Returns 0 on success.

**pthread_join:** blocks until the specified thread terminates. Thread's return value is placed in `*status`.

**Thread termination:** by returning from `func`, calling `pthread_exit()`, the main thread calling `exit()`, or `pthread_cancel()`.

## C++ Thread API (C++11)

```cpp
#include <thread>
std::thread t(func, arg);   // launch thread
t.join();                   // wait for it
t.detach();                 // detach (daemon)
```

Supports function pointers, callable objects, member functions, and lambdas:
```cpp
thread t([arg] { /* lambda body */ });
```

## Race Conditions

When two threads access the same memory location and at least one access is a write, the result depends on the interleaving order — a **race condition**. Example: two threads both execute `x = x + 1` (three instructions: load, add, store):

```
Thread A: load(x=0) → add(1) → [preempted]
Thread B: load(x=0) → add(1) → store(x=1)
Thread A:                     → store(x=1)   ← lost update; expected 2
```

Instruction reordering by the CPU and compiler can create additional races.

## Thread Safety

A function is **thread-safe** if it can be called concurrently by multiple threads without corruption. Functions using global or static state are generally not thread-safe. POSIX provides `_r` (reentrant) variants: `strtok_r`, `ctime_r`, `rand_r`, etc.

## Thread Application Patterns

- **Manager/worker** — one manager assigns tasks to worker threads; e.g., web server dispatching requests.
- **Pipeline** — task split into stages handled by different threads in sequence; e.g., video encode pipeline.

## See Also

- [[Thread Synchronization]]
- [[Mutexes and Locks]]
- [[Condition Variables]]
- [[Semaphores]]
- [[Processes]]
- [[CSCE 313]]
