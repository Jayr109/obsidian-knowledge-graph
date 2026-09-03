---
title: "CSCE 313 Lecture 14 — Thread Synchronization I: Mutexes and Locks"
type: source
tags: [csce313, threads, mutexes, locks, critical-sections, race-conditions, producer-consumer]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 14 (announced March 23) covers mutual exclusion with mutexes as the first synchronization primitive, the critical section concept, the producer-consumer problem, and motivates condition variables to resolve the deadlock that naive mutex-only solutions create.

## Atomic Operations

An **atomic operation** either runs to completion or not at all — no intermediate state is visible to other threads. In x86, each machine instruction is individually atomic (a single instruction fully executes before the thread can be preempted). However, high-level operations (e.g., `x = x + 1`) compile to multiple instructions and are not atomic as a whole.

## Critical Sections

A **critical section** is a segment of code that accesses shared resources (shared variables, files, devices) and must not be executed by more than one thread simultaneously to maintain consistency.

Properties required:
1. **Mutual exclusion** — only one thread in the critical section at a time.
2. **Progress** — if no thread is in the critical section, one waiting thread can enter.
3. **Bounded waiting** — no thread waits forever (no starvation).

## Mutex (Mutual Exclusion Lock)

A mutex is a binary lock that protects a critical section. The thread that locks it is the only one that can unlock it.

**pthreads API:**
```c
pthread_mutex_t m;
pthread_mutex_init(&m, NULL);    // initialize (constructor-like)
pthread_mutex_lock(&m);          // acquire lock; blocks if already held
pthread_mutex_unlock(&m);        // release lock
pthread_mutex_destroy(&m);       // cleanup
```

**C++ std::mutex:**
```cpp
#include <mutex>
std::mutex m;
m.lock();
// critical section
m.unlock();
```

**C++ std::unique_lock** (RAII wrapper — auto-unlock on scope exit):
```cpp
std::unique_lock<std::mutex> ul(m);  // locks on construction
// critical section
ul.unlock();  // can unlock early
// ... 
ul.lock();    // can re-lock
```

## Coarse vs. Fine-Grained Locking

**Coarse-grained:** lock covers the entire thread body → correct, but threads are effectively sequential (no true concurrency). Lock/unlock overhead is low (once per thread).

**Fine-grained:** lock covers only the specific critical section inside the loop → threads interleave in non-critical sections → better parallelism. Lock/unlock overhead is per-iteration.

```cpp
// Coarse: lock entire loop body
m->lock();
for (int i = 0; i < x; i++) { *p = *p + 1; }
m->unlock();

// Fine: lock only the increment
for (int i = 0; i < x; i++) {
    m->lock();
    *p = *p + 1;
    m->unlock();
}
```

Both produce a correct final value, but fine-grained allows more interleaving.

## Producer-Consumer Problem

A **producer** generates data items and puts them in a shared queue; a **consumer** removes and uses items. Multiple producers and consumers may operate concurrently.

**Challenge:** race conditions in queue access + deadlock when consumers hold the lock while waiting for the queue to be non-empty.

**Naive mutex-only attempt (broken):**
```cpp
void Consumer() {
    mutex.lock();
    while (list.size() == 0);  // spin-wait with lock held!
    // ...
    mutex.unlock();
}
```
This deadlocks: the consumer holds the lock while waiting; the producer cannot acquire it to add data.

## Why Condition Variables Are Needed

Mutual exclusion alone provides isolation but not **execution ordering**. The producer-consumer relationship requires:
- The consumer to wait if the queue is empty.
- The producer to signal the consumer when data is added.
- These operations must be atomic with respect to the lock.

The solution — condition variables — is introduced here and detailed in [[CSCE 313 Lecture 15 — Thread Synchronization II]].

```
A condition variable (CV) is:
- a queue of waiting threads, plus
- a lock for access to the critical section

wait(cv, lock):
  - assumes lock is held on entry
  - releases the lock and puts caller to sleep atomically
  - on wakeup, reacquires the lock before returning

signal(cv):
  - wakes one waiting thread (or does nothing if no waiters)
```

## Thread-Safe Functions

A function is **thread-safe** if concurrent calls from multiple threads produce correct results. Functions that use global/static state are generally not thread-safe. See `strtok_r()`, `ctime_r()`, etc., for thread-safe replacements.

## Visual Slides

Lock/unlock timeline diagram (slide p7–p8), coarse/fine grained timeline comparison (slide p12), and producer-consumer queue diagram (slides p13, p23) were visual-only.

## See Also

- [[Mutexes and Locks]]
- [[Thread Synchronization]]
- [[Threads]]
- [[Condition Variables]]
- [[CSCE 313]]
