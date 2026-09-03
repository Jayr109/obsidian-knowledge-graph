---
title: "Pipes and FIFO"
type: concept
tags: [csce313, pipes, fifo, ipc, unix, dup2]
sources: [csce313-lecture-05-ipc-pipes-and-fifo, csce313-lecture-09-unix-file-io]
course: CSCE 313
updated: 2026-04-10
---

Pipes and FIFOs are the two UNIX byte-stream IPC mechanisms. An anonymous pipe is a kernel-buffered, unidirectional channel between related processes. A FIFO (named pipe) is a pipe identified by a filesystem path, usable by any two processes that can open the path.

## Anonymous Pipes

Created with `pipe()`:
```c
int pipe(int pipefd[2]);
// pipefd[0] = read end; pipefd[1] = write end
// Returns 0 on success, -1 on error
```

Data written to `pipefd[1]` is buffered by the kernel until read from `pipefd[0]`. The pipe is a FIFO byte stream — no message boundaries.

### Key Properties

- **Unidirectional.** Data flows one way only.
- **Inherited across fork.** A process creates a pipe before forking; child inherits both ends.
- **EOF semantics.** `read()` returns 0 (EOF) only when **all** write ends are closed. If any process still holds `pipefd[1]` open, `read()` blocks indefinitely even if no writes are pending. Each process must close the end it does not use.
- **Bidirectional communication** requires two pipes.
- **Related processes only.** No way to reference a pipe not created by an ancestor.

### Shell Pipe Operator

`cmd1 | cmd2` is implemented by creating a pipe, forking two children, and using `dup2()` to redirect:
- Child 1 (cmd1): `dup2(pipefd[1], 1)` — stdout → write end; close both pipefd FDs; `exec cmd1`.
- Child 2 (cmd2): `dup2(pipefd[0], 0)` — stdin → read end; close both pipefd FDs; `exec cmd2`.

### dup2() for Redirection

```c
int dup2(int oldfd, int newfd);
```
Makes `newfd` point to the same open file table entry as `oldfd`. After `dup2(pipefd[1], 1)`, writing to fd 1 (stdout) goes to the pipe's write end.

## FIFO (Named Pipe)

Created with `mkfifo()`:
```c
#include <sys/stat.h>
int mkfifo(const char *pathname, mode_t mode);
```

Or shell: `mkfifo myfifo` or `mknod p myfifo`.

A FIFO appears as a special file in the filesystem. Processes open it with `open()` and use `read()`/`write()` as usual. The kernel routes data between processes.

### Key Properties

- **Unrelated processes can communicate** — no shared ancestor required; any process with permission can open the FIFO path.
- **Blocking open.** By default, `open(fifo, O_RDONLY)` blocks until another process opens the write end (and vice versa). Use `O_NONBLOCK` to avoid blocking.
- **Not a regular file.** Data is discarded after reading — no re-reads, no persistence.
- **Unidirectional.** A FIFO should not be used for bidirectional communication (a writer may read its own data).
- **Single reader.** Only one process reads a given piece of data.

### Use Case: Client/Server on Same Machine

```
Server: mkfifo("/tmp/myserver.fifo", 0666);
        fd = open("/tmp/myserver.fifo", O_RDONLY);
        loop: read request, process, respond via another FIFO

Client: fd = open("/tmp/myserver.fifo", O_WRONLY);
        write(fd, request, ...);
```

## Limitations of Both

- No broadcasting (only one reader gets each piece of data).
- Not suitable for bidirectional single-channel communication.
- Pipes: cannot connect to pre-existing unrelated processes.
- FIFOs: data lost after reading; cannot serve multiple clients reliably with a single FIFO.

## See Also

- [[Inter-Process Communication]]
- [[UNIX File I/O]]
- [[File Descriptors]]
- [[Process API]]
- [[CSCE 313]]
