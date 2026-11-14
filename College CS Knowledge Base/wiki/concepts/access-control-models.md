---
title: "Access Control Models"
type: concept
tags: [csce465, security, access-control, dac, mac, acl, policy]
sources: [csce465-lecture-07-operating-system-security, csce465-lecture-08-security-theory-policies-and-models]
course: CSCE 465
updated: 2026-10-20
---

[[CSCE 465]] develops the access control machinery that [[Security Services|access control]] named as a service back in Lecture 2. This is the layer where a [[Security Policy and Mechanism|security policy]] stops being a document and becomes a decision the kernel makes on every file open.

## The Objects Involved

> - Files and folders are managed by the operating system
> - Applications, including shells, access files through an **API**
> - A **file handle** provides an *opaque* identifier for a file or folder
> - File operations: **open** (returns a handle), **read/write/execute**, **close** (invalidates the handle)

The handle being *opaque* is the security point: the application holds a token the kernel issued, not a path or a disk address, so the permission check happens **once at open** and the handle carries the result. That is efficient and it is a deliberate departure from [[Security Design Principles|complete mediation]] — the check is not repeated on every read.

**Hierarchical file organization:** a **tree** in Windows, a **DAG (directed acyclic graph)** in Linux. The difference is not cosmetic — a DAG means a file can be reached by more than one path, which is why Linux has [[File Systems|hard links]] and why, as below, *different paths to the same file are not equivalent*.

## Access Control Entries and Lists

> An **Access Control List (ACL)** for a resource is a **sorted list** of zero or more **Access Control Entries (ACEs)**.
>
> An ACE specifies that a certain set of accesses (read, execute, write) to the resource is **allowed or denied** for a user or group.

The lecture's example, for folder *"Bob's CS167 Grades"*:

```
Bob;  Read;         Allow
TAs;  Read;         Allow
TWD;  Read, Write;  Allow
Bob;  Write;        Deny
TAs;  Write;        Allow
```

**That the list is *sorted* is load-bearest.** Bob appears twice with conflicting entries, so the answer depends on evaluation order — which is exactly what the policy models below specify.

## DAC vs MAC

| | Discretionary Access Control (DAC) | Mandatory Access Control (MAC) |
|---|---|---|
| Who decides | **Users can protect what they own.** The owner may grant access to others and define the type (read/write/execute) | The system, via **multiple levels of security** for users and documents |
| Rule | Owner's discretion | **Read down and write up** |
| Status | **The standard model used in operating systems** | The alternative model |

> **"Read down and write up," derived.** In a multi-level system a subject may *read* data at or below its clearance and *write* at or above it. Reading down prevents a low-clearance user from seeing secrets; writing up prevents a high-clearance user from leaking secrets downward into a file that low-clearance users can read. The counterintuitive half is write-up — it means a cleared user can *add to* a file they cannot read back, which is the price of stopping declassification by copy-paste.
>
> The deep difference from DAC: under DAC the owner of a secret may legitimately hand it to anyone, so DAC **cannot** enforce a confidentiality policy against a cooperating insider. MAC can, which is why it appears in military systems and why DAC is nonetheless what every general-purpose OS ships.

### What Lecture 8 Adds

The theory lecture restates DAC and MAC with implementation examples and one piece of vocabulary this page needs:

- **DAC** — the individual user sets the mechanism to allow or deny access. Example: the **UNIX file system**, `rwx` assigned by file owners. See [[Unix File Permissions]].
- **MAC** — the **environment enforces a static policy**; the individual cannot alter it. Two examples: **process labeling**, where the system assigns labels to processes and objects and a **dominance calculus** evaluates rights, and **AppArmor**, path- and file-capability-based containment of a (possibly compromised) application.

"Dominance calculus" is the bridge to the formal models. Under MAC the matrix cell is not stored at all — it is **computed** by comparing the subject's label against the object's, which is precisely the [[Multi-Level Security|dominance relation]] that [[Bell-LaPadula Model|BLP]] and [[Biba Integrity Model|Biba]] are built from. Everything on this page is the *mechanism* layer; the policies those mechanisms enforce are in [[Security Models]], and the representation underneath both is the [[Access Control Matrix|access control matrix]].

## Closed vs Open Policy

**Closed policy** — also called **"default secure"**: permissions are grants, and anything not granted is denied.

```
Give Tom read access to "foo"
Give Bob r/w access to "bar"

Tom: read "foo"  ->  allowed
Tom: read "bar"  ->  DENIED
```

**Open policy**: permissions are denials, and anything not denied is allowed.

```
Deny Tom read access to "foo"
Deny Bob r/w access to "bar"

Tom: read "foo"  ->  denied
Tom: read "bar"  ->  ALLOWED
```

The closed policy is [[Security Design Principles|fail-safe defaults]] — *base decisions on permissions rather than exclusions* — and it is the same argument as the whitelist-versus-blacklist firewall example from Lecture 2. An open policy requires enumerating every bad thing, and the attacker only needs the one you forgot.

## Closed Policy with Negative Authorizations and Deny Priority

The hybrid, and the one that actually ships:

```
Give Tom r/w access to "bar"
Deny Tom write access to "bar"

Tom: read  "bar"  ->  allowed
Tom: write "bar"  ->  denied
```

> **This policy is used by Windows to manage access control to the file system.**

Closed by default (so unlisted access is denied), but with **negative** entries permitted and **deny taking priority** over allow. That resolves the sorted-list ambiguity in the CS167 example above: Bob's `Write; Deny` beats any allow. See [[NTFS Permissions]].

## Linux vs Windows: How the ACL Is Evaluated

The lecture's comparison, and the most exam-shaped table in the deck:

| | **Linux** | **Windows** |
|---|---|---|
| Entry types | **Allow-only** ACEs | **Allow and deny** ACEs |
| Conflict rule | — | By default, **deny ACEs precede allow** ones |
| What is consulted | ACL of the file **and of all its ancestor folders** | **Only** the file's ACL |
| Traversal | Start at the filesystem root, traverse the path of folders; **each folder must have execute (`cd`) permission** | Ancestors' ACLs are **ignored** when access is requested |
| Multiple paths | **Different paths to the same file are not equivalent** | — |
| Final check | The file's ACL must allow the requested access | — |
| Inheritance | — | Permissions set on a folder are usually **propagated to descendants**; the system **tracks inherited ACEs** |

The two designs make opposite trades, and the trade is **check-time versus set-time**:

> **Derived — the lecture gives the comparison table but does not draw this conclusion.**
>
> **Linux pays at check time.** Every access walks the whole path and tests execute permission on each directory, so the effective permission is a property of the *route taken*. That is why two hard links to one file can behave differently — the file's ACL is the same, the paths are not. It also means revoking access to a directory immediately revokes access to everything beneath it, with no bookkeeping.
>
> **Windows pays at set time.** Inheritance is computed when permissions are assigned and *materialized* onto descendants, so a check consults one ACL and stops. Fast, and location-independent — but changing a parent folder requires propagating to every descendant, and the system must track which ACEs were inherited so it can tell them from explicit ones. That tracking is exactly the explicit/inherited/effective machinery on [[NTFS Permissions]].

Neither is more secure in the abstract; they fail differently. Linux's model makes a permissive directory on the path a silent hole; Windows's makes a stale inherited ACE a silent hole.

## See Also

- [[Operating System Security]]
- [[Access Control Matrix]]
- [[Security Models]]
- [[Multi-Level Security]]
- [[Bell-LaPadula Model]]
- [[Unix File Permissions]]
- [[NTFS Permissions]]
- [[Security Design Principles]]
- [[Security Policy and Mechanism]]
- [[Security Services]]
- [[File Systems]]
- [[CSCE 465]]
