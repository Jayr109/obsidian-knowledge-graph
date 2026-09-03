---
title: "CSCE 313 Lecture 16 — Thread Synchronization III: Condition Variables and Semaphores"
type: source
tags: [csce313, threads, semaphores, condition-variables, bounded-buffer, producer-consumer]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 16 presents the full bounded-buffer producer-consumer problem, introduces counting semaphores as a second synchronization primitive, and shows both CV-based and semaphore-based solutions.

## std::mutex vs. std::unique_lock

`std::unique_lock` wraps `std::mutex` with RAII semantics:
- Locks in constructor, unlocks in destructor (exception-safe).
- Supports `lock()`, `unlock()`, and deferred locking.
- Required by `std::condition_variable::wait()`.

## Counting Semaphores

A **semaphore** is a non-negative integer shared among threads/processes, supporting exactly two atomic operations:

```
wait() (P, sem_wait):
  Block until value > 0; then atomically decrement value by 1.

post() (V, sem_post):
  Atomically increment value by 1; may wake a waiting thread.
```

Both `wait` and `post` must be atomic — two concurrent `wait()` calls cannot both decrement below 0; a thread sleeping in `wait()` cannot miss a `post()` even if they coincide.

**POSIX API (`<semaphore.h>`):**
```c
sem_t sem;
sem_init(&sem, 0, initial_value);  // 2nd arg 0 = thread-scope (not process)
sem_wait(&sem);                    // P operation
sem_post(&sem);                    // V operation
sem_destroy(&sem);
```

## Two Uses of Semaphores

### 1. Mutual Exclusion (Binary Semaphore, initial value = 1)
```c
semaphore.wait();  // lock
// critical section
semaphore.post();  // unlock
```
With initial value 1, exactly one thread can be in the critical section.

### 2. Scheduling Constraint (Signal Pattern, initial value = 0)
```c
// Thread 1 (producer):
data = longfunction();
semaphore.post();  // signal Thread 2

// Thread 2 (consumer):
semaphore.wait();  // wait for signal
temp = readanduse(data);
```
With initial value 0, Thread 2 blocks until Thread 1 posts. Equivalent to `ThreadJoin`:
```c
Semaphore s(0);
ThreadJoin  { s.wait(); }   // joiner blocks
ThreadFinish{ s.post(); }   // joinee unblocks joiner
```

## Semaphore Implementation

A semaphore can be implemented using a mutex and a condition variable:
```cpp
class Semaphore {
    int value;
    mutex m;
    condition_variable cv;
public:
    Semaphore(int v) : value(v) {}
    void wait() {
        unique_lock<mutex> l(m);
        cv.wait(l, [this]{ return value > 0; });
        value--;
    }
    void post() {
        unique_lock<mutex> l(m);
        value++;
        cv.notify_one();  // notify_all is correct but causes spurious wakeups
    }
};
```

## Bounded Buffer (Full Producer-Consumer)

**Problem:** Producer puts items into a fixed-size buffer; consumer removes them. Both must wait when the buffer is full (producer) or empty (consumer).

**Three correctness constraints:**
1. Consumer waits if buffer is empty (scheduling constraint).
2. Producer waits if buffer is full (scheduling constraint).
3. Only one thread manipulates the buffer at a time (mutual exclusion).

**Semaphore solution:**
```c
Semaphore fullSlots(0);        // initially no items
Semaphore emptySlots(bufSize); // initially all slots empty
mutex sync(1);                 // mutual exclusion

void Producer(item) {
    emptySlots.wait();  // decrement empty count (wait if full)
    sync.wait();
    enqueue(item);
    sync.post();
    fullSlots.post();   // increment full count (wake consumer)
}

void Consumer() {
    fullSlots.wait();   // decrement full count (wait if empty)
    sync.wait();
    item = dequeue();
    sync.post();
    emptySlots.post();  // increment empty count (wake producer)
    return item;
}
```

**Order of waits matters:** Acquiring `sync` before `emptySlots`/`fullSlots` causes deadlock (a consumer holds `sync` while waiting for `fullSlots`; a producer cannot acquire `sync` to add data). Always acquire the scheduling semaphore before the mutual exclusion semaphore.

**Order of posts does not matter** for correctness, but may affect scheduling efficiency.

**Scales to multiple producers/consumers** without modification — semaphore semantics handle it.

## Rendezvous Pattern

Two threads must synchronize: `a1` happens before `b2`, and `b1` happens before `a2`:
```
Thread A:                Thread B:
statement a1;            statement b1;
// sync point            // sync point
statement a2;            statement b2;
```
Use two semaphores initialized to 0:
```c
Semaphore aArrived(0), bArrived(0);
// Thread A: a1; aArrived.post(); bArrived.wait(); a2;
// Thread B: b1; bArrived.post(); aArrived.wait(); b2;
```

## Visual Slides

The counting semaphore entry/exit diagram (slide p8) and the bounded buffer timeline were visual-only.

## See Also

- [[Semaphores]]
- [[Condition Variables]]
- [[Mutexes and Locks]]
- [[Thread Synchronization]]
- [[CSCE 313]]
