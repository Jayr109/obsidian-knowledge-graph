---
title: "CSCE 313 Lecture 10 — UNIX I/O: File Descriptors, Redirection, and Standard I/O"
type: source
tags: [csce313, file-descriptors, io-redirection, stdio, dup2, fork]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 10 deepens coverage of file descriptors: why open/close sessions exist, FD inheritance across `fork()`, I/O redirection with `dup2()`, and the Standard I/O (stdio) layer built on top of Unix I/O. It also covers when to use each I/O layer.

## Why File Descriptors Require Sessions

Opening and closing a file is not just a formality. The kernel internally caches per-session information:
- Where the file is stored on disk and which device.
- The current sequential read/write position.
- Which blocks are cached and where.
- Other processes currently accessing the file.

Without open/close, these session-scoped resources could not be managed correctly.

## File Descriptor Behavior

**Lowest available FD.** `open()` always returns the smallest unused descriptor integer. Descriptors 0, 1, 2 are pre-allocated (stdin/stdout/stderr). After `close(fd); fd2 = open(...)`, `fd2` will equal the value that `fd` had.

**dup() / dup2().**
```c
int dup(int oldfd);           // returns lowest available fd pointing to same FT entry
int dup2(int oldfd, int newfd); // makes newfd point to same FT entry as oldfd
```

After `dup2(fd2, fd3)`, both `fd2` and `fd3` point to the same open file table entry, sharing offset. A `read(fd2)` and subsequent `read(fd3)` advance the same shared offset.

## File Descriptors and fork()

`fork()` duplicates the parent's descriptor table. Each child FD points to the **same** open file table entry as the corresponding parent FD → they share the file offset.

**Example: open before fork**
```c
int myfd = open("myf.txt", O_RDONLY);
fork();
read(myfd, &c, 1);  // both parent and child share offset
```
If file contains `"ab"`, child reads `'a'` (offset 0→1), parent reads `'b'` (offset 1→2).

**Example: open after fork**  
Each process opens the file independently → two separate FT entries → separate offsets. Both read `'a'`.

## I/O Redirection

Shell redirects (`ls > foo.txt`) are implemented with `dup2()`:
1. Shell opens `foo.txt` → gets fd 3.
2. Shell forks.
3. In child: `dup2(3, 1)` — fd 1 (stdout) now points to `foo.txt`'s FT entry.
4. Child closes fd 3.
5. Child execs `ls`.

Now `ls`'s writes to stdout go to `foo.txt`.

## Standard I/O (stdio)

The C standard library provides a higher-level I/O layer implemented using Unix I/O:

| stdio function | Unix equivalent |
|---|---|
| `fopen` / `fclose` | `open` / `close` |
| `fread` / `fwrite` | `read` / `write` |
| `fgets` / `fputs` | `read` / `write` (line-oriented) |
| `fscanf` / `fprintf` | (formatted wrappers) |
| `fseek` | `lseek` |

Standard I/O models files as **streams** — an abstraction pairing an fd with an in-memory buffer. `stdin` (fd 0), `stdout` (fd 1), `stderr` (fd 2) are pre-opened streams.

**Buffering behavior:**
- `fprintf(stdout, ...)` to a terminal: flushed on `'\n'`.
- `fprintf(fp, ...)` to a disk file: flushed when the internal buffer is full.
- `fflush(fp)` forces a flush.

## Unix I/O vs. Standard I/O

**Pros of Unix I/O over stdio:**
- Lowest overhead; most general.
- Provides `stat()` for file metadata.
- Async-signal-safe (usable inside signal handlers).
- Required for maximum performance (e.g., direct block I/O on RAID).

**Cons of Unix I/O:**
- Efficient access requires manual buffering (device-dependent, tricky).

**Pros of stdio over Unix I/O:**
- Portable (same code compiles for Linux and Windows).
- Automatic buffering reduces syscall overhead.
- Less burden on programmer.

**Cons of stdio:**
- No metadata access.
- Incompatible with network sockets (poorly documented restrictions).

**General rule:** use the highest-level I/O that meets requirements. Use raw Unix I/O only inside signal handlers, for absolute peak performance, or when you need metadata.

## Visual Slides

The DT/FT/vT diagram after `dup2(4,1)` (slides p13–p14) and the Unix I/O vs. stdio layering diagram (slide p20) were visual-only; the conceptual content is captured above.

## See Also

- [[File Descriptors]]
- [[UNIX File I/O]]
- [[Pipes and FIFO]]
- [[Process API]]
- [[CSCE 313]]
