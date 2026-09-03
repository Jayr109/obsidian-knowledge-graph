---
title: "Mutexes and Locks"
type: concept
tags: [csce313, mutexes, locks, mutual-exclusion, pthreads, critical-sections]
sources: [csce313-lecture-14-thread-synchronization-i-mutexes, csce313-lecture-15-thread-synchronization-ii, csce313-lecture-16-thread-synchronization-iii-semaphores]
course: CSCE 313
updated: 2026-04-10
---

A mutex (mutual exclusion lock) is a binary synchronization primitive that protects a critical section by allowing only one thread to hold the lock at a time. It is the most fundamental tool for preventing race conditions in multithreaded programs.

## Semantics

- **Lock/Acquire:** If the mutex is unlocked, the calling thread locks it and continues. If it is already locked, the calling thread blocks until it becomes available.
- **Unlock/Release:** The holding thread unlocks the mutex. If other threads are blocked on it, one is awakened.
- **Ownership:** A pthreads mutex can only be unlocked by the thread that locked it.

## POSIX pthreads API

```c
#include <pthread.h>

pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;  // static init
// or:
pthread_mutex_t m;
pthread_mutex_init(&m, NULL);   // dynamic init

pthread_mutex_lock(&m);         // acquire (blocks if held)
pthread_mutex_unlock(&m);       // release
pthread_mutex_destroy(&m);      // cleanup

// Non-blocking attempt:
int pthread_mutex_trylock(pthread_mutex_t *m);  // returns EBUSY if locked
```

## C++ std::mutex and std::unique_lock

```cpp
#include <mutex>

// Raw mutex
std::mutex m;
m.lock();
// critical section
m.unlock();

// RAII wrapper (preferred) — auto-unlocks on scope exit
std::unique_lock<std::mutex> ul(m);  // locks in constructor
// critical section
ul.unlock();    // early unlock if needed
// ...
ul.lock();      // re-lock
// destructor unlocks if still locked
```

`std::unique_lock` provides exception safety: even if an exception is thrown inside the critical section, the destructor releases the lock.

## Coarse vs. Fine-Grained Locking

**Coarse-grained:** Lock covers a large block of code (e.g., the entire thread body).
- Simple and easy to reason about.
- Threads are effectively sequential → poor parallelism.
- Low lock overhead (one lock/unlock per thread execution).

**Fine-grained:** Lock covers only the minimal shared state access (e.g., one increment inside a loop).
- Threads can interleave in non-critical sections → better parallelism.
- Higher lock overhead (one lock/unlock per iteration).
- Harder to reason about; easier to introduce bugs.

```cpp
// Coarse: serialize entire thread
m->lock();
for (int i = 0; i < x; i++) { *p = *p + 1; }
m->unlock();

// Fine: serialize only the write
for (int i = 0; i < x; i++) {
    m->lock();
    *p = *p + 1;
    m->unlock();
}
```

Both produce the same correct final value; the choice depends on performance requirements.

## What Mutexes Cannot Do

Mutual exclusion provides **isolation** (only one thread in CS at a time) but not **ordering** (no way to wait for a condition). For ordering constraints — e.g., "wait until the queue is non-empty" — use [[Condition Variables]] or [[Semaphores]].

**Deadlock with mutexes:** Holding a mutex while waiting for a condition that requires another thread to acquire the same mutex:
```cpp
void Consumer() {
    m.lock();
    while (list.empty());   // deadlock: producer can never lock m to add data
    // ...
    m.unlock();
}
```

## Mutex vs. Semaphore

A mutex is essentially a binary semaphore (initial value = 1) with the additional constraint that only the owning thread can unlock it. A binary [[Semaphores|semaphore]] may be posted by any thread, making it suitable for signaling patterns.

## See Also

- [[Thread Synchronization]]
- [[Condition Variables]]
- [[Semaphores]]
- [[Threads]]
- [[CSCE 313]]
