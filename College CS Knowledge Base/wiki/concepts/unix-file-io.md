---
title: "UNIX File I/O"
type: concept
tags: [csce313, file-io, unix-io, system-calls, posix]
sources: [csce313-lecture-09-unix-file-io, csce313-lecture-10-file-descriptors-redirection-stdio]
course: CSCE 313
updated: 2026-04-10
---

UNIX I/O is the low-level file access interface provided directly by the kernel through system calls. It treats all I/O resources — disk files, terminals, devices, pipes, and sockets — uniformly as sequences of bytes accessed via file descriptors.

## The UNIX File Model

A Unix file is a sequence of bytes `B_0, B_1, …, B_{m-1}`. Almost everything in UNIX is a file:

| Path | What it represents |
|------|--------------------|
| `/home/user/foo.txt` | Regular file on disk |
| `/dev/tty2` | Terminal (character device) |
| `/dev/sda2` | Block device (disk partition) |
| `/dev/null` | Null device |
| `/proc/self/maps` | Kernel data structure |
| A FIFO path | Named pipe |
| A socket path | Unix domain socket |

## Core System Calls

### open()
```c
#include <fcntl.h>
int open(const char *pathname, int oflag, mode_t mode);
// Returns lowest available fd >= 0; -1 on error
```

`oflag` must include one of: `O_RDONLY`, `O_WRONLY`, `O_RDWR`. Optional ORed flags: `O_CREAT`, `O_TRUNC`, `O_APPEND`, `O_EXCL`, `O_NONBLOCK`, `O_SYNC`.

When creating a file (`O_CREAT`), `mode` is an **octal** permission bitmask (e.g., `0700`). The final permissions are `mode & ~umask`.

### close()
```c
int close(int fd);  // 0 on success, -1 on error
```

Frees the file descriptor. Always close FDs within the same scope to avoid leaks. All open FDs are closed automatically on process exit.

### read()
```c
ssize_t read(int fd, void *buf, size_t num);
// Returns: bytes read (>0), EOF (0), or error (-1)
```

Reads at the current file offset; advances offset by bytes read. **Short counts** (< `num` bytes returned) are possible and not errors — always check the return value and loop if needed.

### write()
```c
ssize_t write(int fd, const void *buf, size_t num);
// Returns: bytes written (>0), or error (-1)
```

Writes at current offset (or end-of-file if `O_APPEND`). Short counts also possible.

### lseek()
```c
off_t lseek(int fd, off_t offset, int whence);
// whence: SEEK_SET (from start), SEEK_CUR (from current), SEEK_END (from end)
// Returns new file offset, or -1 on error
```

Repositions the file offset without transferring data.

## File Types (from stat)

```c
#include <sys/stat.h>
struct stat {
    ino_t st_ino;      // inode number
    mode_t st_mode;    // type + permissions
    uid_t st_uid;      // owner UID
    gid_t st_gid;      // owner GID
    off_t st_size;     // size in bytes
    time_t st_atime, st_mtime, st_ctime;
    ...
};
int stat(const char *path, struct stat *buf);  // follow symlinks
int lstat(const char *path, struct stat *buf); // don't follow symlinks
int fstat(int fd, struct stat *buf);           // stat via fd
```

## File Permission Model

Permissions are a 9-bit (plus 3 special bits) octal value: `[user][group][others]`, each `rwx`.

```
S_IRWXU = 0700  (owner rwx)
S_IRWXG = 0070  (group rwx)
S_IRWXO = 0007  (others rwx)
```

Permission check order: if caller's UID == file's UID, apply user bits; else if any of caller's GIDs == file's GID, apply group bits; else apply other bits.

**Bit semantics on directories:**
- `r` — list directory contents (but need `x` too for metadata).
- `w` — create/delete files in directory.
- `x` — traverse (look up filenames); needed to access any file in the directory.

## Standard I/O vs. Unix I/O

| Property | Unix I/O (syscalls) | Standard I/O (libc) |
|----------|--------------------|--------------------|
| Level | Kernel (lowest) | Library (higher) |
| Buffering | Manual | Automatic |
| Portability | POSIX only | ANSI C (Windows too) |
| Metadata (stat) | Yes | No |
| Signal-safe | Yes | No |
| Network sockets | Yes | Restricted |

**General rule:** use stdio for disk/terminal files; use Unix I/O inside signal handlers or for maximum performance.

## See Also

- [[File Descriptors]]
- [[File Systems]]
- [[Pipes and FIFO]]
- [[System Calls]]
- [[CSCE 313]]
