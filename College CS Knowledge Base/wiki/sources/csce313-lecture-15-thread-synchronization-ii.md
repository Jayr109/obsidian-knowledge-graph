---
title: "CSCE 313 Lecture 15 — Thread Synchronization II"
type: source
tags: [csce313, threads, condition-variables, mutexes, producer-consumer, cpp-threads]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 15 covers the full condition variable API (pthreads and C++), correct producer-consumer solutions, a detour through the C++ thread API (lambdas, function objects), and the event-driven programming alternative to threads.

## Condition Variables: Full API

A condition variable (CV) is a synchronization primitive that allows threads to wait for a specific condition to become true, atomically releasing a mutex while waiting.

**pthreads API:**
```c
pthread_cond_t cv = PTHREAD_COND_INITIALIZER;
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;

pthread_cond_wait(&cv, &m);    // atomically release m and sleep; reacquire m on wakeup
pthread_cond_signal(&cv);      // wake one waiting thread (or noop if none)
pthread_cond_broadcast(&cv);   // wake all waiting threads
```

**Rule:** Always hold the associated mutex when calling `wait`, `signal`, or `broadcast`. Always re-check the condition in a `while` loop after `wait` returns (spurious wakeups).

**C++ API:**
```cpp
#include <condition_variable>
#include <mutex>
std::condition_variable cv;
std::mutex m;

std::unique_lock<std::mutex> ul(m);
cv.wait(ul, []{return list.size() > 0;});  // predicate-form: loops internally
cv.notify_one();   // wake one
cv.notify_all();   // wake all
```

## Correct Producer-Consumer

```cpp
queue<int> list;
condition_variable cv;
mutex m;

void Producer() {
    int data = getdatafrmsrc();
    m.lock();
    list.push_back(data);
    m.unlock();
    cv.notify_all();  // wake consumers
}

void Consumer() {
    unique_lock<mutex> ul(m);
    cv.wait(ul, []{return list.size() > 0;});  // wait until non-empty
    int data = list.front();
    list.pop();
    ul.unlock();
}
```

**Key steps:**
1. Declare CV and mutex globally.
2. Producer: push data under lock, then `notify_one/all()`.
3. Consumer: hold lock, call `wait()` with predicate (re-checks condition on spurious wakeup), consume data, release lock.

## Condition Variable Correctness Pattern (pthreads)

Progressively correct patterns (Cond Var I–IV from the lecture):

**Broken (spin-wait without CV):**
```c
while (done == 0);  // busy wait
```

**Correct (CV IV — canonical form):**
```c
// in child thread:
pthread_mutex_lock(&m);
done = 1;
pthread_cond_signal(&c);
pthread_mutex_unlock(&m);

// in parent (waiter):
pthread_mutex_lock(&m);
while (done == 0)
    pthread_cond_wait(&c, &m);
pthread_mutex_unlock(&m);
```

The `while` loop is essential: if `signal` runs before `wait`, the `done` flag catches it. If `wait` is entered while done=0, it sleeps and wakes on signal.

## Broadcasting

`notify_all()` / `pthread_cond_broadcast()` wakes all waiting threads. Each woken thread re-checks the predicate; only those for which it is true proceed. Used when multiple consumers might be waiting for the same queue to become non-empty.

## The "Lost Wakeup" Problem

If `mutex.unlock()` and `cv.wait()` are not atomic, a signal between them is lost:
```
Thread A:           Thread B:
release(mutex);     // lock available
                    signal(cv);  // no one waiting yet!
add_to_waitqueue(); // now waiting, but missed signal
```

`pthread_cond_wait` solves this by atomically releasing the mutex and entering the wait queue.

## C++ Thread API (Detour)

Four ways to create a thread in C++11:
```cpp
// 1. Function
thread t1(hello_world, s);

// 2. Callable object (operator())
HelloWorld hw;
thread t2(hw, s);

// 3. Member function
thread t3(&HelloWorld::hello_world, &hw, s);

// 4. Lambda
thread t4([s] { cout << s; });
```

Lambda syntax: `[capture-list] (parameters) -> return_type { body }`.

## Event-Driven Programming Alternative

John Ousterhout (~1995) argued that threads are bad for most purposes because they are too hard to program correctly (synchronization, deadlocks). **Event-driven programming** (single-threaded):
- One execution stream; no CPU concurrency.
- Register callbacks for events (e.g., I/O ready, timer).
- Event loop dispatches to handlers.
- No preemption of handlers.

Events are recommended for I/O-bound programs where CPU parallelism is not needed; threads are justified only when true CPU concurrency matters.

## Visual Slides

CV wait/signal timeline diagram (slide p16), producer-consumer scenario timeline (slide p22), coarse/fine locking timeline (slides p12), and C++ thread comparison table (slide p27) were visual-only.

## See Also

- [[Condition Variables]]
- [[Mutexes and Locks]]
- [[Thread Synchronization]]
- [[Semaphores]]
- [[CSCE 313]]
