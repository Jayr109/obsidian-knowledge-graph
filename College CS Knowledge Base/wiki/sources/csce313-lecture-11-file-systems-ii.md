---
title: "CSCE 313 Lecture 11 — File Systems II"
type: source
tags: [csce313, file-systems, inodes, hard-links, symbolic-links, disk-layout]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 11 covers the on-disk layout of a UNIX file system: data regions, inode tables, bitmaps, superblock, indexed allocation (direct and indirect block pointers), hard links vs. symbolic links, and the UNIX directory API. Reference: OSSTEP Chapter 40. Slide content attributed to Prof. Youjip Won (KAIST).

## File System Abstraction Goals

- **Named hierarchical data** — human-readable filenames.
- **Reliability** — operations like file creation must be atomic (allocate inode + data blocks + update directory atomically to survive power loss).
- **Controlled sharing** — access control (permissions, ownership).

## Disk Layout

A disk is a linear sequence of fixed-size blocks (e.g., 4 KB each). A simple file system layout (low to high block address):

```
[ Superblock | inode bitmap | data bitmap | inode table | data region ]
```

| Component | Purpose |
|-----------|---------|
| **Superblock** | Metadata about the file system: type, size, inode count, inode table start address. Read first when mounting. |
| **Bitmaps** | One bit per inode or data block: 0 = free, 1 = in-use. Two bitmaps: inode bitmap and data bitmap. |
| **Inode table** | Array of on-disk inodes. Each inode is 256 bytes; 16 inodes per 4KB block. |
| **Data region** | Stores actual file and directory content. |

**Example:** With inode tables in blocks 3–7 and 256-byte inodes, the file system supports up to 80 inodes (max 80 files/directories).

## The Inode

Each file or directory has one inode, identified by an **inode number** (index into the inode table). Given inode #32: offset = 32 × 256 = 8192 bytes; add inode table start (12 KB) → 20 KB on disk.

Key inode fields (`struct inode` in Linux):
```c
unsigned long i_ino;    // inode number
umode_t i_mode;         // file type + permissions
unsigned int i_nlink;   // hard link count
uid_t i_uid;            // owner UID
gid_t i_gid;            // owner GID
loff_t i_size;          // file size in bytes
time_t i_atime/mtime/ctime; // access/modify/change timestamps
__u32 i_data[15];       // block pointers (ext3: 12 direct + 1 single + 1 double + 1 triple)
```

## Indexed Allocation: Block Pointers

An inode uses a tiered pointer scheme to locate file data blocks:

| Pointer type | Level | Capacity (4KB blocks, 4-byte ptrs = 1024 ptrs/block) |
|---|---|---|
| **Direct** (12) | 0 | 12 × 4KB = 48 KB |
| **Single indirect** (1) | 1 | 1024 × 4KB = 4 MB |
| **Double indirect** (1) | 2 | 1024² × 4KB = 4 GB |
| **Triple indirect** (1) | 3 | 1024³ × 4KB = 4 TB |

Small files (< 48 KB) use only direct pointers. Large files chain through indirect blocks.

**Direct pointer:** block number points to a data block.  
**Single indirect:** block number points to a block of direct pointers.  
**Double indirect:** block number → block of single-indirect pointers.  
**Triple indirect:** block number → block of double-indirect pointers.

## File Hierarchy: Directories

Directories are special files whose data blocks contain an array of `(name, inode number)` pairs. The file system tree is built by nesting directories.

A leaf directory always has link count 2 (one from its parent's entry + one from its own `.` entry).

## Hard Links

A hard link is a directory entry that maps a name to an existing inode number. Multiple hard links to the same inode are all "first class" — no distinction between original and link.

```c
link("/dirA/name1", "/dirB/name2");  // creates second name for inode 12345
unlink("/dirA/name1");               // decrements link count; frees inode when count = 0
```

Shell: `ln <existing> <link>`. Cannot hard-link directories (prevents cycles).

## Symbolic (Soft) Links

A symbolic link is a separate inode whose data is a **pathname string**. The OS dereferences the path on each access.

```c
symlink("/dirA/name1", "/dirB/name2");
```

Shell: `ln -s <target> <link>`. Symlinks:
- Can point to directories.
- Can cross file system boundaries.
- Can point to non-existent targets (dangling symlink).
- Only hard links count toward the inode's link count; symlinks do not.

## Creating and Reading Files (Steps)

**Create a 12 KB file "newfile":**
1. Find a free inode (e.g., #47) in the inode bitmap.
2. Find 3 free data blocks (e.g., 2, 20, 100) in the data bitmap.
3. Write data into blocks 2, 20, 100.
4. Update inode #47 with metadata and block pointers.
5. Create a directory entry `(47, "newfile")` in the parent directory.

**Read a file:**
1. Search directory for the filename → extract inode number.
2. Read the inode from the inode table.
3. Follow block pointers to read each data block in sequence.

## Partition Layout

```
[ Superblock | Bitmaps | inode table | Data Area ]
```

A disk drive can contain multiple partitions; each partition can have its own independent file system.

## UNIX Directory API

```c
DIR *opendir(const char *dirname);
struct dirent *readdir(DIR *dirp);    // stateful cursor; returns next entry
void rewinddir(DIR *dirp);
int closedir(DIR *dirp);
char *getcwd(char *buf, size_t size); // get current working directory
```

`struct dirent` contains: `d_ino` (inode number), `d_type` (file type), `d_name` (filename).

## Magnetic Disk Characteristics

A disk block read involves: (1) seek — arm moves to the correct track (~10 ms, very slow); (2) rotational latency — wait for sector to rotate under head; (3) transfer — read sector at SATA rate (~500 MB/s). Seeks dominate latency.

## Visual Slides

Multiple diagram-heavy slides: disk layout progression (slides p5–p9), inode table layout (slide p10), indexed allocation diagram (slide p31), link diagrams (slides p16, p19, p23, p24), and magnetic disk anatomy (slides p12–p13) were visual or minimally captured.

## See Also

- [[File Systems]]
- [[File Descriptors]]
- [[UNIX File I/O]]
- [[CSCE 313]]
