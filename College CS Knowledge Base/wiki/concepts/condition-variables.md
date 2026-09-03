---
title: "Condition Variables"
type: concept
tags: [csce313, condition-variables, pthreads, producer-consumer, wait-signal]
sources: [csce313-lecture-15-thread-synchronization-ii, csce313-lecture-16-thread-synchronization-iii-semaphores]
course: CSCE 313
updated: 2026-04-10
---

A condition variable (CV) is a synchronization primitive that allows threads to efficiently wait for an arbitrary condition to become true, atomically releasing a mutex while sleeping. It solves the ordering problem that mutexes alone cannot address.

## Semantics

A CV is associated with a mutex and a predicate (condition). Operations:

- **wait(cv, mutex):** Atomically releases `mutex` and puts the calling thread to sleep on `cv`. When awakened, reacquires `mutex` before returning. Caller must hold `mutex` on entry.
- **signal(cv):** Wakes one thread waiting on `cv` (or does nothing if no waiters). Calling thread should hold the associated mutex.
- **broadcast(cv):** Wakes all threads waiting on `cv`.

The atomicity of "release lock + sleep" is critical: it eliminates the lost-wakeup bug (a signal between `unlock` and `wait` would be missed if they were separate operations).

## The while-loop Rule

**Always check the condition in a `while` loop**, not an `if`:

```c
// Correct
pthread_mutex_lock(&m);
while (queue.empty())
    pthread_cond_wait(&cv, &m);
// consume from queue
pthread_mutex_unlock(&m);

// Wrong (if-based)
pthread_mutex_lock(&m);
if (queue.empty())
    pthread_cond_wait(&cv, &m);
// may proceed on spurious wakeup with empty queue!
```

Reasons: **spurious wakeups** (OS may wake a thread with no signal), and multiple consumers may be woken by `broadcast` but only one gets the item.

## POSIX pthreads API

```c
#include <pthread.h>

pthread_cond_t cv = PTHREAD_COND_INITIALIZER;
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;

pthread_cond_wait(&cv, &m);       // wait (releases m, reacquires on wake)
pthread_cond_signal(&cv);         // wake one waiter
pthread_cond_broadcast(&cv);      // wake all waiters

pthread_cond_init(&cv, NULL);     // dynamic init
pthread_cond_destroy(&cv);        // cleanup
```

## C++ API

```cpp
#include <condition_variable>
std::condition_variable cv;
std::mutex m;

// Wait with predicate (loops internally on spurious wakeups)
std::unique_lock<std::mutex> ul(m);
cv.wait(ul, []{ return !queue.empty(); });

cv.notify_one();   // signal
cv.notify_all();   // broadcast
```

`std::condition_variable::wait` with a predicate is equivalent to:
```cpp
while (!predicate()) cv.wait(ul);
```

## Producer-Consumer Pattern

### pthreads version

```c
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t not_empty = PTHREAD_COND_INITIALIZER;

void *producer(void *arg) {
    pthread_mutex_lock(&m);
    enqueue(item);
    pthread_cond_signal(&not_empty);
    pthread_mutex_unlock(&m);
    return NULL;
}

void *consumer(void *arg) {
    pthread_mutex_lock(&m);
    while (queue_empty())
        pthread_cond_wait(&not_empty, &m);
    item = dequeue();
    pthread_mutex_unlock(&m);
    return NULL;
}
```

### C++ version

```cpp
queue<int> q;
condition_variable cv;
mutex m;

void producer() {
    lock_guard<mutex> lk(m);
    q.push(item);
    cv.notify_all();
}

void consumer() {
    unique_lock<mutex> ul(m);
    cv.wait(ul, []{ return !q.empty(); });
    int item = q.front(); q.pop();
}
```

## Signal vs. Broadcast

Use `signal` when exactly one waiter should proceed (e.g., exactly one consumer should dequeue).  
Use `broadcast` when all waiters should re-check the condition (e.g., a resource becomes available; which thread gets it depends on predicate re-evaluation).

## Canonical Usage Pattern

1. Declare one mutex and one (or more) CVs.
2. All accesses to shared state are under the mutex.
3. Waiter: `lock → while(!condition) wait(cv, m) → consume → unlock`.
4. Producer: `lock → produce → signal/broadcast → unlock`.

## See Also

- [[Thread Synchronization]]
- [[Mutexes and Locks]]
- [[Semaphores]]
- [[Threads]]
- [[CSCE 313]]
