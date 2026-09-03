---
title: "CSCE 313 Lecture 9 — UNIX File I/O"
type: source
tags: [csce313, file-io, file-descriptors, unix-io, inodes, permissions]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 9 introduces UNIX file I/O at the system call level: the file abstraction, `open()`/`close()`/`read()`/`write()`/`lseek()`, file permissions, the three-table kernel representation (descriptor table, file table, v-node table), and file sharing semantics.

## The UNIX File Abstraction

A Unix file is a sequence of bytes `B_0, B_1, …, B_{m-1}`. Almost all I/O devices are represented as files:
- `/dev/sda2` — a disk partition.
- `/dev/tty2` — a terminal.
- `/dev/mem` — kernel memory image.
- `/proc` — kernel data structures.

**Common file types:**
- Regular files (user/app data).
- Directories (contain names and inode numbers of other files; use `readdir` not raw byte I/O).
- Character special / block special (terminals, disks).
- FIFO (named pipe for IPC).
- Socket (network communication; has a pathname for Unix domain sockets).

## Core System Calls

### open()
```c
#include <fcntl.h>
int open(const char *pathname, int oflag, ... /* mode_t mode */);
// Returns fd >= 0 on success, -1 on error (errno set)
```

`oflag` must include exactly one of: `O_RDONLY`, `O_WRONLY`, `O_RDWR`. Optional flags OR'd in: `O_CREAT` (create if not exists; requires `mode`), `O_TRUNC`, `O_APPEND`, `O_EXCL`, `O_NONBLOCK`, `O_SYNC`.

`open()` always returns the **lowest available** file descriptor. Descriptors 0 (stdin), 1 (stdout), 2 (stderr) are pre-allocated for each new process.

### close()
```c
int close(int fd);  // Returns 0 OK, -1 error
```
Frees the descriptor for reuse. The kernel closes all open FDs on process termination.

### read()
```c
ssize_t read(int fd, void *buf, size_t num);
// Returns bytes read; 0 on EOF; -1 on error
```
Begins at the current file offset and advances it. **Short counts** (fewer bytes than requested) are possible and not errors (EOF, network buffering, record devices, signal interruption).

### write()
```c
ssize_t write(int fd, void *buf, size_t num);
// Returns bytes written; -1 on error
```
Begins at current offset (or end-of-file if `O_APPEND`). Short counts are also possible.

### lseek()
Repositions the file offset without reading or writing.

## File Permissions

Created with `open(pathname, O_CREAT, mode)`. Mode is an **octal** bitmask:

| Symbol | Octal | Meaning |
|--------|-------|---------|
| `S_IRWXU` | `0700` | owner rwx |
| `S_IRUSR` | `0400` | owner read |
| `S_IWUSR` | `0200` | owner write |
| `S_IXUSR` | `0100` | owner execute |
| `S_IRWXG` | `0070` | group rwx |
| `S_IRWXO` | `0007` | others rwx |

**Important:** pass `0700` (octal), not `700` (decimal = different bits).

Bit semantics:
- `r` on files: read the file (also need `x` on containing dir).
- `r` on directories: list files in dir (but need `x` for metadata).
- `w` on files: write the file (also need `w` on dir to delete).
- `x` on files: execute. On directories: look up a file by name.
- `setuid` (`u+s`): effective UID changes to file owner on execution.
- `setgid` (`g+s`): effective GID changes.
- sticky bit: for directories, restricts deletion.

## The stat Structure

```c
struct stat {
    __ino_t  st_ino;    // inode number
    __mode_t st_mode;   // file type + permissions
    __uid_t  st_uid;    // owner UID
    __gid_t  st_gid;    // owner GID
    __off_t  st_size;   // file size in bytes
    struct timespec st_atim, st_mtim, st_ctim; // access/modify/change times
    ...
};
```

## Three-Table Kernel Representation

The kernel uses three data structures to represent open files:

1. **Descriptor Table (DT)** — one per process. Indexed by file descriptor integer. Each entry points to an open file table entry.
2. **File (Open File) Table (FT)** — shared by all processes. Each entry holds: current file offset, reference count (number of DT entries pointing to it), status flags, pointer to v-node table entry.
3. **v-node Table (vT)** — shared by all processes. One entry per file. Contains file metadata (size, type, permissions, access/mod times).

**Two distinct opens of the same file** create two separate FT entries (each with its own offset) pointing to one vT entry. The vT refcount = 2.

**File sharing via fork():** The child inherits the parent's DT (copies of all entries). Both parent and child FT entries point to the same FT entry → same offset. A `read()` in the child advances the offset seen by the parent.

**File sharing via dup2():** Two DT entries in the same process point to the same FT entry → same offset. Used for I/O redirection.

## Visual Slides

Three-table diagrams (slides p32–p35) are visual; the text above captures their structure. The `st_mode` bit layout diagram (slide p15) was partially captured.

## See Also

- [[UNIX File I/O]]
- [[File Descriptors]]
- [[File Systems]]
- [[Pipes and FIFO]]
- [[CSCE 313]]
