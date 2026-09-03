---
title: "CSCE 313 Lecture 5 — Inter-Process Communication: Pipes and FIFO"
type: source
tags: [csce313, ipc, pipes, fifo, fork, dup2, unix-philosophy]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 5 covers the two fundamental message-passing IPC mechanisms in UNIX: anonymous pipes (created with `pipe()`) and named pipes/FIFOs (created with `mkfifo()`). It also introduces `fork()` briefly and the `dup2()` system call for I/O redirection. References: OSSTEP Chapter 5, SPiL Chapter 13, APUE §7.1–7.6.

## Inter-Process Communication Overview

IPC allows processes to communicate and synchronize actions. Two main paradigms:
1. **Message passing** — data moves through a channel (pipes, sockets, message queues).
2. **Shared memory** — processes map the same memory region.

This lecture focuses on message passing via pipes and FIFOs.

## Anonymous Pipes

A pipe is a unidirectional data channel created with the `pipe()` system call:

```c
int pipe(int pipefd[2]);
// pipefd[0] = read end; pipefd[1] = write end
// Returns 0 on success, -1 on failure
```

Data written to `pipefd[1]` is buffered by the kernel until read from `pipefd[0]`. Data is received in FIFO order.

**Usage pattern with `fork()`.** A process creates a pipe, then forks. The pipe's file descriptors are inherited by both parent and child. Typically one end closes in each process to establish directional flow:
- Parent writes to `pipefd[1]`; child reads from `pipefd[0]`.
- The unused end must be closed: if `pipefd[1]` stays open in the child, `read()` on `pipefd[0]` will block forever (no EOF is delivered while a write end is open).

**Bidirectional communication.** Two pipes are needed—one `parent→child` pipe and one `child→parent` pipe. A single pipe must not be used for bidirectional communication.

**Shell pipe operator.** The shell `cmd1 | cmd2` creates a pipe, forks two children, and uses `dup2()` to redirect cmd1's stdout to the write end and cmd2's stdin to the read end.

## dup2() — File Descriptor Duplication

```c
int dup2(int oldfd, int newfd);
```

Creates a copy of `oldfd` as `newfd` (closing `newfd` first if open). Both descriptors then refer to the same open file description and share file offset and status flags.

**How `ls | sort` works:**
1. Create pipe: `pipe()` → fds 3 (read) and 4 (write).
2. Fork.
3. In child (ls): `dup2(4, 1)` — redirect stdout to write end; close fd 3 and 4; exec `ls`.
4. In child (sort): `dup2(3, 0)` — redirect stdin to read end; close fd 3 and 4; exec `sort`.
5. Both children close the pipe ends not needed. ls writes to stdout; sort reads from stdin.

## FIFO (Named Pipes)

A FIFO is a named pipe associated with a filesystem path. Unlike anonymous pipes, any process with appropriate permissions can open it by name—no shared ancestor required.

```c
#include <sys/stat.h>
int mkfifo(const char *pathname, mode_t mode);
```

Shell equivalent: `mkfifo` or `mknod p`.

Once created, processes use `open()`, `read()`, `write()`, and `close()` on the FIFO path just like a regular file. A common use case is client/server communication on the same machine (e.g., an anti-virus server that any client can contact by name).

## Unix Philosophy

The Unix philosophy (Ken Thompson) underpins pipe usage:
1. Make each program do one thing well.
2. Expect every program's output to become another program's input.

This design enables powerful command chaining: `ls -l | sort -k5 | tail -1 | awk '{print $NF}'`.

## Limitations

**Anonymous pipes:**
- Unidirectional.
- Can only be shared between related processes (parent/child or siblings).
- Cannot connect to long-running services or reference a pipe created elsewhere.

**FIFOs:**
- Not regular files — data is discarded after reading; cannot be re-read.
- Only one reader gets data (no broadcast).
- Not suitable for true bidirectional communication on a single FIFO.

## Aside: exec and fork Considerations

The `execl()` family of calls replaces the process image entirely with a new program; the process keeps its PID, open FDs, environment, but code and data are overwritten. The lecture references Baumann et al. (HotOS '19) on modern criticisms of fork: it is no longer simple (violates thread safety, is insecure with modern mitigations, and can be slow).

## Visual Slides

Several command pipeline diagrams (slides p9–p15) and the dup2 step-by-step diagram (p31) were visual-only; key logic is captured in the text above.

## See Also

- [[Inter-Process Communication]]
- [[Pipes and FIFO]]
- [[File Descriptors]]
- [[Process API]]
- [[CSCE 313]]
