---
title: "Thread Synchronization"
type: concept
tags: [csce313, thread-synchronization, race-conditions, critical-sections, atomicity]
sources: [csce313-lecture-14-thread-synchronization-i-mutexes, csce313-lecture-15-thread-synchronization-ii, csce313-lecture-16-thread-synchronization-iii-semaphores]
course: CSCE 313
updated: 2026-04-10
---

Thread synchronization is the discipline of coordinating concurrent threads that share mutable state to ensure correctness. Without synchronization, threads that read and write shared data can produce incorrect, non-deterministic results — race conditions. The key synchronization primitives in UNIX/POSIX are mutexes, condition variables, and semaphores.

## The Problem: Race Conditions

A **race condition** occurs when the correctness of a program depends on the relative timing of operations between threads. Because the scheduler can interleave threads at any point, high-level operations that compile to multiple machine instructions are not atomic.

**Classic example:** `x = x + 1` compiles to `load; add; store`. Two threads executing concurrently can produce `x = 1` instead of `x = 2`:

```
T1: load(x=0)  [preempt]
T2: load(x=0) → add → store(x=1)  [preempt]
T1:            → add → store(x=1)  ← lost update
```

Additional source: **instruction reordering** by the CPU or compiler for performance optimization. The compiler may reorder "independent" statements, breaking inter-thread dependencies.

## Critical Section

A **critical section** is a code segment that accesses shared resources and must not execute concurrently in multiple threads. Properties required:

1. **Mutual exclusion** — only one thread in the critical section at a time.
2. **Progress** — if no thread is in the CS and some want to enter, one will eventually proceed.
3. **Bounded waiting** — no thread waits forever.

## Atomic Operations

An **atomic operation** is one that executes completely without any other thread observing intermediate state. In x86, individual machine instructions are atomic (each completes before preemption). For larger critical sections, atomic behavior must be enforced with synchronization primitives.

## Synchronization Primitives

### Mutex (Mutual Exclusion Lock)
Provides exclusive access to a critical section. A mutex is either locked (held by one thread) or unlocked. See [[Mutexes and Locks]].

### Condition Variable
Allows threads to efficiently wait for a condition to become true, atomically releasing a mutex while sleeping. Avoids busy-waiting. See [[Condition Variables]].

### Semaphore
A non-negative counter supporting atomic `wait()` (decrement, block if 0) and `post()` (increment, wake a waiter). More general than a mutex — supports both mutual exclusion (initial value = 1) and scheduling constraints (initial value = 0). See [[Semaphores]].

## Producer-Consumer Problem

The canonical synchronization problem: a producer puts items in a shared buffer; consumers remove them. Requires:

1. **Mutual exclusion** — only one thread manipulates the buffer at a time.
2. **Consumer waits** when buffer is empty.
3. **Producer waits** when buffer is full (bounded buffer).

Cannot be solved with mutexes alone (deadlock: consumer holds lock while waiting for data; producer cannot acquire lock to produce). Solution requires condition variables or semaphores for scheduling constraints.

## Synchronization Pitfalls

**Deadlock:** Two or more threads each hold a resource the other needs. Classic fix: always acquire locks in a consistent global order.

**Priority inversion:** A high-priority thread waits for a resource held by a low-priority thread that is itself preempted.

**Spurious wakeups:** A condition variable `wait()` may return even if no `signal` was called. Always re-check the predicate in a `while` loop.

**Lost wakeup:** If `signal()` fires between a lock release and `wait()`, the signal is lost and the waiting thread sleeps forever. The `wait()` call must atomically release the lock and enter the wait queue.

## Granularity Trade-offs

- **Coarse-grained locking:** simple, correct, but serializes threads → limited parallelism.
- **Fine-grained locking:** better parallelism, but more lock/unlock overhead and risk of subtle bugs (partial updates visible between locks).

## See Also

- [[Mutexes and Locks]]
- [[Condition Variables]]
- [[Semaphores]]
- [[Threads]]
- [[CSCE 313]]
