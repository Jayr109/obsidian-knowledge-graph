---
title: "CSCE 465 Lecture 7 — Operating System Security"
type: source
tags: [csce465, os-security, access-control, unix-permissions, ntfs, cold-boot]
sources: []
course: CSCE 465
updated: 2026-10-08
---

Lecture 7 of [[CSCE 465]] (`raw/CSCE465_07_OS_Security.pdf`, 21 PDF pages laid out two slides per page ≈ 42 logical slides, instructor [[Guofei Gu]]). Opens the **OS and system security** unit from the course outline. Roadmap: *basic OS and OS security concepts, filesystem security*.

This is the first CSCE 465 lecture to overlap heavily with [[CSCE 313]], which already covers [[Operating Systems|what an OS is]], [[Processes|processes]], [[Virtual Memory|virtual memory]], and [[File Systems|file systems]] from the systems side. The derived pages deliberately **do not restate those mechanics** — they cover the security surface and link across.

## Structure

| Slides | Section | Content |
|---|---|---|
| 4–11 | **OS and boot** | Computer model; OS concepts; the boot sequence; BIOS passwords; hibernation; cold boot attack; measured/trusted boot and the TCB; event logging |
| 12–17 | **Access control** | General filesystem principles, ACEs and ACLs; DAC vs MAC; closed vs open policy; deny priority; Linux vs Windows ACL evaluation |
| 18–24 | **Linux filesystem** | File access control scope; hard vs symbolic links; Unix permissions and the 10-character notation; file and directory examples; the file-sharing challenge |
| 25–34 | **Unix permissions in depth** | Special bits (setuid, setgid, sticky); root and `su`/`sudo`; `chmod`/`chgrp`/`chown`; octal notation |
| 35–43 | **ACLs and NTFS** | Limitations of Unix permissions and POSIX ACLs; NTFS ACLs; cumulative rules; inheritance and effective permissions; move vs copy |

## Pages Derived

| Page | What it holds |
|---|---|
| [[Operating System Security]] | The boot chain as attack surface — BIOS passwords, hibernation, cold boot, trusted boot/TCB, event logging |
| [[Access Control Models]] | ACE/ACL, DAC vs MAC, closed vs open policy, deny priority, the Linux-vs-Windows evaluation comparison |
| [[Unix File Permissions]] | 10-character notation, directory semantics, the file-sharing challenge, special bits, root, chmod, octal, POSIX ACLs |
| [[NTFS Permissions]] | Cumulative/override rules, inheritance, explicit/inherited/effective, move vs copy |

## Content Worth Keeping

**The boot chain is the attack surface.** *A malicious user could potentially seize execution at several points in the boot process* — and every OS protection mechanism is code that only runs once the OS is running. BIOS passwords, trusted boot, and the TCB each defend one link. → [[Operating System Security]]

**Hibernation strips two guarantees at once.** RAM contents are implicitly protected by process isolation and by volatility; writing them to `hiberfil.sys` removes both, and no permission check was ever consulted. → [[Operating System Security]]

**The cold boot attack defeats five full-disk encryption systems without breaking a cipher.** Cooling DRAM to −50 °C gives **< 0.2% decay after one minute**, long enough to read the key out of RAM. Demonstrated against dm-crypt, LoopAES, BitLocker, FileVault, and TrueCrypt (Halderman et al., USENIX Security 2008). → [[Operating System Security]]

**A file handle is opaque, and the permission check happens once at open.** That is efficient and a deliberate departure from complete mediation. → [[Access Control Models]]

**DAC cannot enforce confidentiality against a cooperating insider; MAC can.** Under discretionary control the owner may legitimately give a secret away. That is why MAC exists and why DAC nonetheless ships in every general-purpose OS. → [[Access Control Models]]

**Closed policy is fail-safe defaults; Windows uses closed-with-deny-priority.** Same whitelist-vs-blacklist argument as Lecture 2's firewall example. → [[Access Control Models]]

**Linux pays at check time, Windows pays at set time.** Linux walks every path component and needs execute on each, so *different paths to the same file are not equivalent*; Windows materializes inheritance so a check reads one ACL. Neither is more secure — they fail differently. → [[Access Control Models]]

**Directory permission bits mean different things.** Read lists names only; write creates and **deletes**; execute enters and reads properties. So **write on a directory lets you delete a file you cannot write** — which is what the sticky bit repairs. → [[Unix File Permissions]]

**The file-sharing challenge fails twice for the same reason.** Random hard links fail because a hard link can be copied; random symlinks fail because a symlink tells you where it points. Both tried to use name obscurity as access control. → [[Unix File Permissions]]

**setuid is least privilege deliberately suspended.** Every setuid-root binary is a privilege-escalation path if it has a bug. → [[Unix File Permissions]]

**NTFS permissions are cumulative, and explicit beats inherited before deny beats allow.** "Deny always wins" is the common oversimplification and it is wrong when the allow is explicit and the deny inherited. → [[NTFS Permissions]]

**Move within a volume keeps the source's permissions; everything else takes the destination's.** A move is a rename, so the ACL never moves — which means dragging a file into a protected folder on the same volume leaves it unprotected. → [[NTFS Permissions]]

## Connection to the Rest of the KB

This lecture is where the course's own earlier material and [[CSCE 313]] meet:

- [[Security Services]] named **access control** as one of the six services; this is its implementation.
- [[Security Design Principles]] gets three concrete instances: **fail-safe defaults** (closed policy), **least privilege** (setuid suspending it, `sudo` restoring it), **economy of mechanism** (why a TCB must be small), and **compromise recording** (event logging, with Lecture 2's caveat that the audit trail must itself be protected).
- The [[Side-Channel Attacks|cold boot attack]] is a physical side channel — the abstract model says RAM clears at power-off and the device disagrees for a few seconds.
- [[File Systems]] and [[Process Attributes]] from CSCE 313 supply the hard-link/inode and UID/EUID mechanics the derived pages link to rather than restate.

## Extraction Note

Text extracted with PyMuPDF. The prose-heavy first half extracted cleanly; permission tables and notation survived intact, including the `ls -l` samples and the full octal table.

**Visual gaps, all in the second half:**
- The **measured/trusted boot** figure (slide 10) carries only the TCB definition in its text layer; the stages and measurement flow it depicts are **not recoverable**.
- The **"Basic NTFS Permissions"** table (slide 37) is image-only — **28 images, 272 characters** on that page. The per-permission detail is **not recoverable**.
- The multiple-permissions example (38), inheritance figure (39), and move/copy volume diagrams (42–43) are images whose **labels** survive; the rules they illustrate are stated in prose and were reconstructed from those, not read off the figures.
- Slide 35 carries **39 images** — the POSIX ACL / Unix-limitations slide — with its bullets intact.

**Slide numbering oddity:** the deck's internal page numbers jump from 40 to 42, skipping 41. Whether a slide was removed or the numbering simply skips is not determinable from the file.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Operating System Security]]
- [[Access Control Models]]
- [[Unix File Permissions]]
- [[NTFS Permissions]]
- [[Operating Systems]]
- [[File Systems]]
- [[CSCE 465 Lecture 6a — User Authentication]]
