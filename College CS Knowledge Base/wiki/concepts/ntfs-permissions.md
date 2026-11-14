---
title: "NTFS Permissions"
type: concept
tags: [csce465, security, access-control, ntfs, windows, inheritance]
sources: [csce465-lecture-07-operating-system-security]
course: CSCE 465
updated: 2026-10-08
---

The Windows side of [[Access Control Models|access control]] in [[CSCE 465]]. NTFS attaches an **ACL** to each file and folder, built from **ACEs** naming users and groups — and unlike [[Unix File Permissions|Unix]], those entries can **deny** as well as allow, and they are **inherited**.

```
NTFS partition
  └── ACL
        ├── ACE:  User 1 / Group 1       Read
        └── ACE:  Group 1 / User 2       Full Control
```

## The Three Combination Rules

> - **NTFS permissions are cumulative**
> - **File permissions override folder permissions**
> - **Deny overrides Allow**

The lecture's example: User 1 is in Group A (Read on Folder A) and Group B (Write on Folder A); File1 and File2 sit inside, and Group B is **denied Write** on File2.

> **Worked through.** *Cumulative* means User 1's effective permission on Folder A is Read ∪ Write = Read/Write — group memberships add up rather than the first match winning, which is the opposite of Unix's owner/group/other selection. *File overrides folder* means a permission set directly on File2 beats whatever Folder A granted. *Deny overrides Allow* then settles the conflict: User 1 can write File1 but not File2, even though a group they belong to was granted Write on the parent.
>
> Read the three rules as an evaluation order: **accumulate all applicable permissions, let the more specific object win, and let any deny win over any allow.** That is the [[Access Control Models|closed policy with negative authorizations and deny priority]] the lecture names, implemented.

## Inheritance

> Permissions set on a folder are propagated to descendants, and the system **keeps track of inherited ACEs** — so a **block of inheritance** can be placed on a subtree.

```
Folder A  [Read/Write]
   └── File1      inherits Read/Write    ->  access allowed
Folder A  [Read/Write]
   └── File1      block of inheritance   ->  access denied
```

NTFS therefore distinguishes three kinds of permission on any object:

| Kind | Definition |
|---|---|
| **Explicit** | Set by the owner for each user/group on this object |
| **Inherited** | Dynamically inherited from the **explicit** permissions of ancestor folders |
| **Effective** | Obtained by **combining** the explicit and inherited permissions |

**Determining effective permissions:**

1. **By default, a user/group has no privileges** — the closed/default-secure baseline
2. **Explicit permissions override conflicting inherited permissions**
3. **Denied permissions override conflicting allowed permissions**

Note rule 2 and the "deny overrides allow" rule can pull in opposite directions, and rule 2 is listed first: **an explicit Allow beats an inherited Deny.** That ordering is the thing to get right — "deny always wins" is the common oversimplification, and it is wrong when the allow is explicit and the deny is inherited.

> The system must **track which ACEs were inherited** precisely so it can apply rule 2. That bookkeeping is the cost of Windows's design choice to resolve inheritance at *set* time rather than walking ancestors at *check* time — see the [[Access Control Models|Linux vs Windows comparison]].

## Move vs Copy

A behavior with real security consequences and no Unix analogue:

| Operation | Same volume | Across volumes |
|---|---|---|
| **Move** | Permissions stay **the same as the source** | Permissions become **those of the destination** |
| **Copy** | Permissions become **those of the destination** | Permissions become **those of the destination** |

> **Why the odd case is odd.** A move *within* a volume is a rename — the file's data and its ACL never move, so the ACL survives. Everything else is a create-plus-write at the destination, and a newly created object inherits from its new parent.
>
> The security consequence: **dragging a file out of a restricted folder into a public one, on the same volume, carries the restrictive permissions with it** — which surprises users who expect the destination's rules. And the reverse is worse: moving a file *into* a protected folder on the same volume leaves it with its old, permissive ACL, so it sits in a secure directory without being secure. Copy is the predictable operation; move is not.

> **Visual gap:** the NTFS sections lean on diagrams — the basic-permissions table (slide 37), the multiple-permissions example (38), the inheritance figure (39), and the move/copy volume diagrams (42–43) are images. Their labels survive in the text layer and the rules are stated in prose, but the per-permission detail of the "Basic NTFS Permissions" table is **not recoverable** from the PDF.

## Compared with Unix

| | [[Unix File Permissions\|Unix]] | NTFS |
|---|---|---|
| Entries | Owner / group / other, three bits each | Arbitrarily many ACEs naming users and groups |
| Multiple group memberships | **First matching class wins** | **Cumulative** — all applicable permissions union |
| Deny | Not expressible (POSIX ACLs aside) | **First-class**, and overrides allow |
| Ancestors | Checked on **every** access (execute bit on each path component) | **Ignored** at check time; resolved at set time via inheritance |
| Finer grain | Requires **POSIX ACLs** bolted on top | Native |

NTFS is the more expressive model and the more complicated one to reason about. Unix's coarseness is a usability problem (the [[Unix File Permissions|file-sharing challenge]]); NTFS's expressiveness is an auditability problem — *effective* permission on a deeply nested object is a computation over explicit entries, inherited entries, group memberships, and two override rules, which is hard for an administrator to hold in their head and therefore easy to get wrong.

## See Also

- [[Access Control Models]]
- [[Unix File Permissions]]
- [[Operating System Security]]
- [[Security Design Principles]]
- [[CSCE 465]]
