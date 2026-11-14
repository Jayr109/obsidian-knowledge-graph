---
title: "Access Control Matrix"
type: concept
tags: [csce465, security, access-control, policy, subjects-objects-rights]
sources: [csce465-lecture-08-security-theory-policies-and-models]
course: CSCE 465
updated: 2026-10-20
---

The **access control matrix** is the general representation of an access control policy: a table whose rows are subjects, whose columns are objects, and whose cells hold the rights that subject has over that object. [[CSCE 465]] introduces it as the thing every concrete mechanism in [[Access Control Models|Lecture 7]] — Unix mode bits, ACLs, NTFS ACEs — is an *encoding* of, and as the object the [[Safety Problem|safety theorem]] is proved about.

## Access Control as a Function

> An access control system determines what **rights** a particular entity (**subjects**) has for a set of **objects**.

The lecture's example questions make the shape concrete:

- Do you have the right to read `/etc/passwd`?
- Does Alice have the right to view the CSE website?
- Do students have the right to share project data?
- Does a student have the right to change another student's grades?

Formally, an access control policy is a function:

```
P(S, O, R) -> { accept, deny }

S = set of subjects
O = set of objects
R = set of rights
```

> **The policy is a lot of these tuples, whether explicitly represented that way or not.**

That clause is the one to remember. A Unix file's `rwxr-xr--` does not look like a tuple set, but it *denotes* one; so does an NTFS ACL and so does a firewall ruleset. The matrix is the canonical form, and every real mechanism is a compression of it chosen to be storable and checkable.

> **Why nobody stores the matrix, derived.** With *n* subjects and *m* objects the matrix is *n × m* and overwhelmingly empty. The two standard compressions are the two the course has already shown without naming them as such: storing it **by column** gives an [[Access Control Models|access control list]] — each object carries the subjects that may touch it, which is what Unix and NTFS do — and storing it **by row** gives a **capability list**, where each subject carries tokens for the objects it may touch. The [[Access Control Models|opaque file handle]] from Lecture 7 is a capability. Which axis you compress along decides what is cheap: ACLs make "who can read this file?" easy and "what can this user reach?" hard, and capabilities reverse it.

## Subjects, Objects, Rights

- **Objects** are the protected resources — files, folders, devices, records.
- **Subjects** are the active entities that request access. Note that a subject is usually a *process acting for a user*, not the user: this is why [[Process Attributes|UID and EUID]] exist, and why [[Unix File Permissions|setuid]] is dangerous.
- **Rights** are the operations — read, write, execute, and in the full HRU model also *own* and *grant*, which is what lets rights propagate and therefore what makes safety non-trivial.

## Why This Representation Is the Theory's Starting Point

The matrix is expressive enough to describe any policy, which is its virtue and its defect. Because commands can create subjects and objects and copy rights between cells, the system that manipulates the matrix is powerful enough to simulate a [[Turing Machines|Turing machine]] — which is exactly how the [[Safety Problem|undecidability of safety]] is proved.

The response is to stop writing arbitrary policies over the matrix and instead adopt a [[Security Models|security model]]: a restricted language whose policies have a fixed shape. [[Bell-LaPadula Model|BLP]] and [[Biba Integrity Model|Biba]] both do this by making the matrix a function of labels rather than a free table — cell contents are *computed* from the subject's and object's levels, not listed. A policy you cannot write down arbitrarily is a policy you can reason about.

## Administration: Who Fills the Matrix In

Who gets to write in the cells is the **DAC vs. MAC** question, and the full treatment — including the Lecture 8 examples (process labeling, AppArmor) — is on [[Access Control Models]] rather than repeated here.

What belongs on *this* page is what each style does to the matrix itself:

- Under **DAC** the matrix is **stored**. Owners edit their own column, and the cells are data — which is why the representation question (ACL by column, capability by row) is a real engineering decision.
- Under **MAC** the matrix is **not stored at all**. Each cell is *computed* on demand by comparing the subject's label with the object's, via what the lecture calls a **dominance calculus**. See [[Multi-Level Security]].

That is the deeper reason the formal models exist. A computed matrix cannot be edited into an unsafe state one cell at a time, so the [[Safety Problem|safety question]] that is undecidable over a stored matrix becomes answerable over a derived one.

## See Also

- [[Security Models]]
- [[Safety Problem]]
- [[Access Control Models]]
- [[Multi-Level Security]]
- [[Bell-LaPadula Model]]
- [[Unix File Permissions]]
- [[Process Attributes]]
- [[Security Policy and Mechanism]]
- [[CSCE 465]]
