---
title: "Semaphores"
type: concept
tags: [csce313, semaphores, synchronization, producer-consumer, bounded-buffer]
sources: [csce313-lecture-16-thread-synchronization-iii-semaphores]
course: CSCE 313
updated: 2026-04-10
---

A semaphore is a non-negative integer shared among threads or processes, supporting exactly two atomic operations: `wait()` (decrement, blocking if zero) and `post()` (increment, possibly waking a waiter). Introduced by Dijkstra, semaphores are a general-purpose synchronization primitive supporting both mutual exclusion and scheduling constraints.

## Operations

```
wait() [P, sem_wait]:
  Atomically:
    while (value == 0) { sleep; }
    value--;

post() [V, sem_post]:
  Atomically:
    value++;
    if (any thread waiting) { wake one; }
```

Both operations must be **fully atomic** — two concurrent `wait()` calls cannot both decrement below 0, and a `post()` cannot be missed even if it coincides exactly with a `wait()` entering sleep.

## POSIX API

```c
#include <semaphore.h>

sem_t sem;
sem_init(&sem, 0, initial_value);  // 0 = thread-scope (not process-scope)
sem_wait(&sem);                    // P operation; blocks if value == 0
sem_post(&sem);                    // V operation; increments and wakes a waiter
sem_destroy(&sem);
```

For process-scope semaphores (second arg = 1) or named semaphores: `sem_open()`, `sem_close()`, `sem_unlink()`.

## Two Uses

### 1. Mutual Exclusion (Binary Semaphore, initial = 1)

```c
Semaphore mutex(1);   // initial value 1

mutex.wait();
// critical section
mutex.post();
```

Exactly one thread can be in the critical section. Equivalent to a mutex, but any thread (not just the owner) can post.

### 2. Scheduling Constraint (Signaling, initial = 0)

```c
Semaphore s(0);   // initial value 0

// Thread A (waiter):
s.wait();          // blocks until Thread B signals
use(data);

// Thread B (signaler):
data = compute();
s.post();          // unblocks Thread A
```

With initial value 0, Thread A blocks until Thread B posts. Also models `ThreadJoin`:
```c
Semaphore done(0);
ThreadFinish { done.post(); }
ThreadJoin   { done.wait(); }
```

## Implementation (using mutex + CV)

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
        cv.notify_one();
    }
};
```

`notify_one()` rather than `notify_all()` — only one thread can decrement, so waking only one is sufficient. `notify_all()` is correct but causes unnecessary spurious wakeups.

## Bounded Buffer (Full Producer-Consumer)

The classic bounded-buffer problem: producer fills a fixed-size buffer; consumer empties it. Both must wait when the buffer is full (producer) or empty (consumer).

**Three-semaphore solution:**
```c
Semaphore fullSlots(0);        // number of filled slots; initially 0
Semaphore emptySlots(bufSize); // number of empty slots; initially bufSize
Semaphore sync(1);             // mutex for buffer access

void Producer(item) {
    emptySlots.wait();  // wait for an empty slot
    sync.wait();
    enqueue(item);
    sync.post();
    fullSlots.post();   // announce a filled slot
}

void Consumer() {
    fullSlots.wait();   // wait for a filled slot
    sync.wait();
    item = dequeue();
    sync.post();
    emptySlots.post();  // announce an empty slot
    return item;
}
```

**Critical ordering rule:** Always acquire the scheduling semaphore (`emptySlots`/`fullSlots`) **before** the mutual exclusion semaphore (`sync`). Reversing the order causes deadlock.

## Semaphore vs. Mutex vs. CV

| Primitive | Initial value | Who can unlock | Scheduling? | Count > 1? |
|-----------|-------------|----------------|-------------|-----------|
| Mutex | 1 | Owner only | No | No |
| Binary semaphore | 1 | Any thread | No | No |
| Counting semaphore | n | Any thread | Yes | Yes |
| Condition variable | — | N/A (uses mutex) | Yes | N/A |

Semaphores combine mutual exclusion and signaling in a single primitive; condition variables separate the two concerns (require a separate mutex).

## See Also

- [[Thread Synchronization]]
- [[Mutexes and Locks]]
- [[Condition Variables]]
- [[Threads]]
- [[CSCE 313]]
