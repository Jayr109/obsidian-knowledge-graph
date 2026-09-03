---
title: "File Descriptors"
type: concept
tags: [csce313, file-descriptors, open-file-table, inode, dup2, io-redirection]
sources: [csce313-lecture-09-unix-file-io, csce313-lecture-10-file-descriptors-redirection-stdio]
course: CSCE 313
updated: 2026-04-10
---

A file descriptor (FD) is a small non-negative integer that a process uses as a handle to an open file, pipe, socket, or other I/O resource. It is the key abstraction enabling UNIX's "everything is a file" model.

## The Three-Table Model

The kernel uses three data structures to represent open files:

```
Process A                         Kernel (shared)
Descriptor Table (DT)    Open File Table (FT)    v-node Table (vT)
[one per process]        [shared by all]         [one entry per file]

 fd 0 ──────────────→  FT entry ──────────────→  vnode
 fd 1 ──────────────→  FT entry                  (size, type,
 fd 2 ──────────────→  FT entry                   permissions,
 fd 3 ──────────────→  FT entry ──────────────→  vnode  timestamps)
```

### Descriptor Table (DT)
- One per process; private.
- Indexed by fd integer.
- Each entry points to an open file table entry.

### Open File Table (FT)
- Shared by all processes.
- Each entry contains:
  - **File offset** (current read/write position).
  - **Reference count** (number of DT entries pointing to this FT entry).
  - **Status flags** (`O_RDONLY`, `O_APPEND`, etc.).
  - **Pointer to v-node entry**.

### v-node Table (vT)
- Shared by all processes.
- One entry per unique open file.
- Contains file metadata: type, size, permissions, ownership, timestamps.

## Pre-Allocated Descriptors

Every new process starts with three open file descriptors:

| fd | Name | Default connection |
|----|------|--------------------|
| 0 | stdin | terminal input |
| 1 | stdout | terminal output |
| 2 | stderr | terminal output |

`open()` always returns the **lowest available** fd. After `close(3); fd = open(...)`, the new fd will be 3.

## File Sharing Scenarios

### Two Opens of the Same File
```c
int fd1 = open("foo.txt", O_RDONLY);  // FT entry A, offset 0
int fd2 = open("foo.txt", O_RDONLY);  // FT entry B, offset 0
```
Two separate FT entries → separate offsets. `read(fd1)` and `read(fd2)` both start from byte 0.

### fork() — Shared Offset
```c
int fd = open("foo.txt", O_RDONLY);  // FT entry, offset 0
fork();
// Both parent and child fd point to same FT entry → shared offset.
read(fd, &c, 1);  // child reads byte 0 → offset becomes 1
// parent reads byte 1 (shared offset)
```

### dup() / dup2() — Aliased FDs
```c
int fd2 = dup(fd1);            // new fd, same FT entry → shared offset
int r = dup2(oldfd, newfd);    // newfd now aliases oldfd's FT entry
```

After `dup2(fd2, fd1)`, fd1 and fd2 share the same offset. A read on either advances both.

## I/O Redirection with dup2()

Shell `ls > foo.txt`:
1. Open `foo.txt` → fd 3.
2. `dup2(3, 1)` → stdout (fd 1) now points to `foo.txt`'s FT entry.
3. Close fd 3.
4. `exec ls` — ls writes to fd 1 → data goes to `foo.txt`.

Shell `ls | sort`:
1. `pipe()` → fd 3 (read), fd 4 (write).
2. Fork.
3. Child ls: `dup2(4, 1)` → stdout → pipe write; close 3 and 4; `exec ls`.
4. Child sort: `dup2(3, 0)` → stdin → pipe read; close 3 and 4; `exec sort`.

## FD Lifecycle

- **Created:** `open()`, `pipe()`, `socket()`, `accept()`, `dup()`, inherited from parent.
- **In use:** `read()`, `write()`, `lseek()`, `ioctl()`, etc.
- **Destroyed:** `close()`, or automatically on process exit.

**FD leak:** forgetting to call `close()` when done. Each process has a per-process limit on open FDs (typically 1024 by default; configurable via `ulimit -n`).

## See Also

- [[UNIX File I/O]]
- [[Pipes and FIFO]]
- [[File Systems]]
- [[Process API]]
- [[CSCE 313]]
