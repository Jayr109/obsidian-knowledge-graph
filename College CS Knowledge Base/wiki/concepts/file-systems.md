---
title: "File Systems"
type: concept
tags: [csce313, file-systems, inodes, directories, hard-links, symbolic-links, disk-layout]
sources: [csce313-lecture-11-file-systems-ii, csce313-lecture-09-unix-file-io]
course: CSCE 313
updated: 2026-04-10
---

A file system is the OS subsystem that organizes persistent data on a storage device into named, hierarchical structures. It provides three core guarantees: named hierarchical data, reliability (operations are atomic with respect to power failure), and controlled sharing (access permissions).

## On-Disk Layout

A UNIX file system partitions the disk into fixed-size blocks (typically 4 KB) and organizes them as:

```
[ Superblock | inode bitmap | data bitmap | inode table | data region ]
```

| Component | Purpose |
|-----------|---------|
| **Superblock** | File system metadata: type, total size, inode count, inode table location. Read at mount time. |
| **inode bitmap** | One bit per inode: 0 = free, 1 = in-use. |
| **data bitmap** | One bit per data block: 0 = free, 1 = in-use. |
| **inode table** | Array of on-disk inodes (each 256 bytes; 16 per 4KB block). |
| **data region** | File and directory content. |

## The Inode

Every file and directory has exactly one **inode** (index node), identified by its **inode number** (index into the inode table). The inode does **not** store the filename — that lives in the directory.

**Key inode fields (`struct inode`):**
```c
unsigned long i_ino;    // inode number
umode_t i_mode;         // file type + rwx permissions
unsigned int i_nlink;   // hard link count
uid_t i_uid;            // owner UID
gid_t i_gid;            // owner GID
loff_t i_size;          // file size in bytes
time_t i_atime/mtime/ctime;  // access/modify/change times
__u32 i_data[15];       // block pointers
```

## Indexed Allocation (Block Pointers)

The 15 block-pointer slots in an ext-style inode use a **tiered indirection** scheme:

| Slots | Pointer type | Depth | Capacity (4KB blocks, 1024 ptrs/indirect block) |
|-------|-------------|-------|------|
| 12 | Direct | 0 | 12 × 4KB = **48 KB** |
| 1 | Single indirect | 1 | 1024 × 4KB = **4 MB** |
| 1 | Double indirect | 2 | 1024² × 4KB = **4 GB** |
| 1 | Triple indirect | 3 | 1024³ × 4KB = **4 TB** |

Small files (< 48 KB) use only direct pointers. Large files chain through indirect blocks.

## Directories

A directory is a special file whose data blocks contain an array of `(inode_number, filename)` pairs. The VFS traverses directories to resolve pathnames like `/home/user/file.txt`.

A new (leaf) directory has link count 2: one from its parent entry, one from its own `.` entry.

## Hard Links

A hard link is a directory entry that maps a name to an existing inode number. Multiple hard links to the same inode are all first-class:

```c
link("/dirA/name1", "/dirB/name2");  // create second name
unlink("/dirA/name1");               // decrement link count; free inode when count=0
```

Rules:
- All hard links to a file are equal — no "original."
- Cannot hard-link directories (would create cycles).
- Cannot cross file system boundaries.

## Symbolic (Soft) Links

A symbolic link is a separate inode whose data content is a **pathname string**. The OS dereferences it on each access.

```c
symlink("/dirA/name1", "/dirB/name2");  // symlink at name2 pointing to name1
```

Rules:
- Can link to directories.
- Can cross file system boundaries.
- Can be dangling (target does not exist).
- Do not count toward the target inode's link count.

## File System Operations (Steps)

**Creating a 12 KB file:**
1. Find a free inode → update inode bitmap.
2. Find 3 free data blocks → update data bitmap.
3. Write file data into blocks.
4. Update the inode (size, block pointers, timestamps).
5. Add `(inode_number, filename)` entry to the parent directory.

**Reading a file:**
1. Locate inode via directory traversal.
2. Read the inode from the inode table.
3. Follow block pointers, reading each data block in sequence.

## Partition Structure

A disk may contain multiple partitions; each partition may have its own independent file system. Mounting attaches a file system to a directory in the VFS tree.

## Relationship to File Descriptors

Opening a file (`open()`) creates a chain:
```
fd (per-process DT) → open file table entry (per-open) → v-node (per-file)
```

The v-node is the in-memory representation of the on-disk inode. See [[File Descriptors]].

## The Security View

[[CSCE 465]] covers the permission layer on top of this structure: [[Unix File Permissions]] for the `rwx` model, the special bits, and POSIX ACLs; [[NTFS Permissions]] for the Windows side; and [[Access Control Models]] for why Linux checks every path component while Windows consults only the file's own ACL — which is what makes *different paths to the same file not equivalent* given the hard links described above.

## See Also

- [[File Descriptors]]
- [[UNIX File I/O]]
- [[Pipes and FIFO]]
- [[Operating Systems]]
- [[CSCE 313]]
