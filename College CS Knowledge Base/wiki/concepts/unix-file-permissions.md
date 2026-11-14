---
title: "Unix File Permissions"
type: concept
tags: [csce465, security, access-control, unix, setuid, chmod, posix-acl]
sources: [csce465-lecture-07-operating-system-security]
course: CSCE 465
updated: 2026-10-08
---

The Unix permission model as [[CSCE 465]] teaches it — **standard for all UNIXes**: every file is owned by a **user** and has an associated **group**, with permissions displayed in **compact 10-character notation** (`ls -l`). This page covers the security surface; [[File Systems]] from [[CSCE 313]] covers the on-disk mechanics, and [[Access Control Models]] covers how the ACL is evaluated.

```
jk@sphere:~/test$ ls -l
-rw-r-----  1 jk ugrad 0 2005-10-13 07:18 file1
-rwxrwxrwx  1 jk ugrad 0 2005-10-13 07:18 file2
```

The ten characters are: file type, then three triples — **owner**, **group**, **other** — each `rwx`.

## Regular Files

| Notation | Meaning |
|---|---|
| `-rwxrwxrwx` | read/write/execute to everyone |
| `-r--r--r--` | read-only to everyone, **including owner** |
| `-rwx------` | read/write/execute for owner, forbidden to everyone else |
| `-rw-r-----` | read/write for owner, read-only for group, forbidden to others |
| `-rw-r--r--` | read/write for owner, read-only for everyone else |

The second row is worth pausing on: the owner is denied write to their own file. Unix checks the *first matching* class rather than taking the union, so being the owner means you get the **owner** bits and nothing else — more permissive group or other bits do not help you.

## Directories: The Same Bits Mean Different Things

**Permission bits are interpreted differently for directories**, and this is where most Unix permission confusion lives:

| Bit | On a directory |
|---|---|
| **Read** | List the **names** of files in the directory — **but not their properties** like size and permissions |
| **Write** | **Create and delete** files within the directory |
| **Execute** | **Enter** the directory and get **properties** of files in it |

Directory lines in `ls -l` begin with `d`.

| Notation | Meaning |
|---|---|
| `drwxrwxrwx` | full access to everyone |
| `drwx--x---` | full access to owner; **group can access known filenames** but not list them; forbidden to others |
| `drwxrwx---` | full access to owner and group, forbidden to others |
| `drwxr-xr-x` | all can enter and list; only owner can add/delete files |

Three consequences the slides imply:

- **Read without execute is nearly useless** — you get names and nothing else.
- **Execute without read** (`--x`) is the useful oddity: a user who already knows a filename can reach it, but cannot enumerate the directory. That is the `drwx--x---` row, and it is how "secret" shared files are handed out by path.
- **Write on the directory lets you delete a file you cannot write.** Deletion is a directory operation, not a file operation — the file's own permissions are irrelevant.

## The File Sharing Challenge

The lecture poses a real problem and shows two natural solutions **both failing**:

> **Creating and modifying groups requires root.** Given a directory `drwx------x` and a file in it:
> - give write permission to user1, user2, user3, … **without creating a new group**
> - **selectively revoke** a user

**Solution 1** — give the file write permission for everyone, and create different random hard links: `user1-23421`, `user2-56784`, …
**Problem:** selectively removing access fails — **a hard link can be copied.** Once user1 knows the name, revoking that link does not help; they can make their own link to the same inode.

**Solution 2** — create random **symbolic** links instead.
**Problem:** **a symbolic link tells you where it points.** The secret path is no longer secret.

> **Why this is in the lecture.** Both attempts try to use *obscurity of the name* as an access control mechanism, and both fail for the reason [[Security Design Principles|open design]] predicts. The real lesson is that the Unix user/group/other model is too coarse for per-user sharing, and no clever use of links fixes a model problem — which is exactly the argument for POSIX ACLs below.

## Special Permission Bits

Three bits beyond `rwx`:

### Set-user-ID (`suid` / `setuid`)

> On **executable** files, causes the program to run as the **file owner** regardless of who runs it. Ignored for everything else. In the 10-character display, replaces the **4th** character (`x` or `-`) with `s` (or `S` if not also executable).

```
-rwsr-xr-x   setuid, executable by all
-rwxr-xr-x   executable by all, but not setuid
-rwSr--r--   setuid, but NOT executable  -  not useful
```

This is the single most security-sensitive bit in Unix: a setuid-root binary runs with full privilege no matter who invokes it, so **every setuid program is a privilege-escalation path if it has a bug**. It is [[Security Design Principles|least privilege]] deliberately suspended, which is why the principle's page notes that most systems lack the granularity to apply it precisely. See [[Process Attributes]] for the UID/EUID mechanics.

### Set-group-ID (`sgid` / `setgid`)

> On **executable** files: run with the **file's group**, regardless of whether the user is in that group.
> On **directories**: files created within inherit the **directory's group** — *useful for directories shared by multiple users with different default groups.*
> Replaces the **7th** character with `s` (or `S`).

```
-rwxr-sr-x   setgid file, executable by all
drwxrwsr-x   setgid directory; files within will have the group of the directory
-rw-r-Sr--   setgid file, but not executable  -  not useful
```

The directory behavior is the partial answer to the file-sharing challenge above — it is how group collaboration actually works in practice.

### Sticky Bit

> On directories, **prevents users from deleting or renaming files they do not own.**

This repairs the "write on the directory lets you delete anything" hole noted earlier, and it is why `/tmp` is world-writable without being a free-for-all.

## Root

> The **root** account is a super-user account, like Administrator on Windows. **Multiple roots possible.** **File permissions do not restrict root.** This is **dangerous, but necessary, and OK with good practices.**

That last clause is the lecture being honest about the same tension [[Security Design Principles|least privilege]] raised: *does the root/administrator concept violate the principle?* Yes — and it ships anyway.

**Becoming root:**

| Command | Effect |
|---|---|
| `su` | Changes home directory, PATH, and shell to root's, but **doesn't touch most of the environment** and **doesn't run login scripts** |
| `su -` | Logs in as root **just as if root had done so normally** |
| `sudo <command>` | Run **just one command** as root |
| `su [-] <user>` | Become another non-root user — **root does not need to enter a password** |

`sudo` is the least-privilege option of the four: one command, logged, with no persistent root shell. The `su` versus `su -` distinction matters for security because an inherited environment (PATH especially) is an injection vector into a root session.

## Changing Permissions

- Permissions are changed with **`chmod`**
- **Only the file owner or root can change permissions**
- A user who owns a file can use **`chgrp`** to set its group to **any group of which the user is a member**
- **root** can change ownership with **`chown`** (optionally changing group in the same command)
- `chown`, `chmod`, and `chgrp` take **`-R`** to recurse through subdirectories

| Command | Effect |
|---|---|
| `chmod u+s file1` | Sets the setuid bit on file1 (**doesn't change the execute bit**) |
| `chgrp testgrp file1` | Sets file1's group to testgrp, **if the user is a member** |
| `chmod -R g=rwX dir1` | Adds group read/write to dir1 and everything within, and group execute **only where someone already has execute** |
| `chmod g+w,o-rwx file1 file2` | Adds group write, denies all access to others |
| `chown -R root dir1` | Changes ownership of dir1 and everything within to root |

The capital `X` in `g=rwX` is the subtle one — it sets execute only on directories and on files that are already executable by someone, which is what you want when recursing and almost never what `g=rwx` gives you.

## Octal Notation

> The symbolic syntax is nice for simple cases but bad for complex changes. The alternative is **three or four octal digits**, 0–7.

```
[special bits][user bits][group bits][other bits]

special digit = (4 if setuid) + (2 if setgid) + (1 if sticky)
all others    = (4 if readable) + (2 if writable) + (1 if executable)
```

| Octal | Meaning |
|---|---|
| `777` / `0777` | read/write/execute to everyone (**dangerous!**) |
| `1777` | same as 777, **plus sticky bit** |
| `2775` | same as 775, **plus setgid** (useful for directories) |
| `775` / `0775` | rwx for owner and group, r-x for others |
| `644` / `0644` | read/write for owner, read-only for everyone else |
| `640` / `0640` | read/write for owner, read-only for group, forbidden to others |

`1777` is `/tmp`. `2775` is the shared-group-directory pattern from the sgid section.

## Limitations, and POSIX ACLs

> **Unix permissions are not perfect** — **groups are restrictive**, and there are **limitations on file creation.**
>
> Linux optionally uses **POSIX ACLs**:
> - Builds **on top of** traditional Unix permissions
> - **Several users and groups can be named**, each with different permissions
> - Allows **finer-grained** access control
> - Each ACL entry is of the form **`type:[name]:rwx`**
> - **Setuid, setgid, and sticky bits are outside the ACL system**

POSIX ACLs are the direct answer to the file-sharing challenge — naming individual users is exactly what the user/group/other model cannot do. That the special bits sit *outside* the ACL system is worth remembering: the most security-critical bits are the ones the newer, finer mechanism does not cover.

## See Also

- [[Operating System Security]]
- [[Access Control Models]]
- [[NTFS Permissions]]
- [[File Systems]]
- [[Process Attributes]]
- [[Security Design Principles]]
- [[CSCE 465]]
