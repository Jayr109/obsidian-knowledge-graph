---
title: "Inter-Process Communication"
type: concept
tags: [csce313, ipc, pipes, fifo, shared-memory, message-passing]
sources: [csce313-lecture-05-ipc-pipes-and-fifo]
course: CSCE 313
updated: 2026-04-10
---

Inter-Process Communication (IPC) refers to the mechanisms by which separate processes exchange data and coordinate their actions. Because processes have isolated virtual address spaces (enforced by the OS), communication requires explicit OS support — it cannot happen via simple pointer sharing.

## Two Paradigms

### Message Passing

Processes exchange discrete messages through a channel maintained by the OS. The OS handles buffering, synchronization, and delivery. Neither process needs to know the other's address space.

**UNIX message-passing IPC mechanisms:**
- **Anonymous pipes** (`pipe()`) — byte-stream channel between related processes (parent/child).
- **Named pipes / FIFOs** (`mkfifo()`) — byte-stream channel identified by a filesystem name; any two processes can use it.
- **Sockets** — full-duplex channels for local or networked processes.
- **Message queues** (`mq_open()`) — typed messages with priorities.

### Shared Memory

Processes map the same region of physical memory into their respective address spaces. Communication is via direct reads and writes to shared variables — very fast, but requires explicit synchronization (mutexes, semaphores) to prevent races.

**POSIX shared memory:** `shm_open()`, `mmap()`.

## Trade-offs

| Property | Message Passing | Shared Memory |
|----------|----------------|---------------|
| Synchronization | Implicit (reads block until data available) | Explicit (locks/semaphores required) |
| Throughput | Lower (kernel copies data) | Higher (zero-copy) |
| Complexity | Lower for simple patterns | Higher (race conditions) |
| Scope | Local and networked | Local only |

## Pipes and FIFOs in CSCE 313

[[Pipes and FIFO]] are the primary IPC mechanism covered in CSCE 313 (Lecture 5):

- **Anonymous pipe** — `int pipe(int pipefd[2])`. Unidirectional byte stream; `pipefd[1]` is write end, `pipefd[0]` is read end. Inherited by child after `fork()`. Both ends must be properly closed to signal EOF.
- **Named pipe (FIFO)** — `mkfifo(path, mode)`. Associated with a filesystem name; any process with permissions can open it. Used for client/server IPC on the same machine.

Both are unidirectional and do not persist data after reading.

## Sockets

Sockets (covered in [[CSCE 313 Lecture 18 — Introduction to Networking/Internet]]) generalize pipes to full-duplex, networked communication. A Unix domain socket has a filesystem pathname and works entirely on the local machine. A TCP/IP socket communicates over the network.

## See Also

- [[Pipes and FIFO]]
- [[Computer Networking]]
- [[Processes]]
- [[Thread Synchronization]]
- [[CSCE 313]]
