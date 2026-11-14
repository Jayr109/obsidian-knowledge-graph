---
title: "Role-Based Access Control"
type: concept
tags: [csce465, security, rbac, roles, access-control, hybrid-policy]
sources: [csce465-lecture-08-security-theory-policies-and-models]
course: CSCE 465
updated: 2026-10-20
---

**Role-Based Access Control (RBAC)** inserts a layer between users and permissions: rights attach to **job functions**, and users are granted roles rather than rights. [[CSCE 465]] files it as a hybrid policy alongside the [[Chinese Wall Model|Chinese Wall]], and it is by a wide margin the model in this lecture that the student is most likely to meet in working software.

## The Argument

> In an enterprise, we don't really do anything **as ourselves** — we do things as some **job function**. E.g. student, professor, doctor.
>
> **Access depends on function, not identity.**

The lecture's example:

- Allison, bookkeeper for the Math Dept, has access to financial records
- She leaves
- Betty is hired as the new bookkeeper, so she now has access to those records

> The **role** of "bookkeeper" dictates access, not the identity of the individual.

## Roles

> A **role** is a collection of privileges/permissions associated with some function or affiliation.
>
> **Important: the permissions are static, the user-role membership is transient.**
>
> Not directly [[Access Control Models|MAC]] or [[Access Control Models|DAC]], but may be one or either of these.

That middle line is the whole engineering case. Two things change at very different rates — *what a bookkeeper may do* changes rarely and after deliberation; *who is the bookkeeper* changes whenever someone is hired, promoted or fired. RBAC puts the join between them in one place.

> **What RBAC actually buys you, derived.** Not expressiveness — anything RBAC states can be written directly into an [[Access Control Matrix|access control matrix]] by expanding each role to its members. It buys **administration**. The matrix formulation makes Allison's departure an *n*-cell edit across every system she touched, and the cells you miss are exactly the standing access nobody notices until an audit. Routed through a role it is one revocation. The win is that the error-prone operation happens once instead of *n* times — which is why RBAC is a hybrid policy rather than an information-flow model: it constrains **how policy is edited**, not how information moves.

## Why It Sits Apart From the Others

| | Decided by | Changes when |
|---|---|---|
| [[Bell-LaPadula Model\|BLP]] / [[Biba Integrity Model\|Biba]] | Comparing two labels | Labels are reassigned |
| [[Chinese Wall Model\|Chinese Wall]] | The subject's read history | The subject reads something |
| **RBAC** | The subject's **current role set** | The subject's **job** changes |

BLP and Biba answer *may this information move?*; RBAC answers *who should hold this right in the first place?* They are orthogonal, and real systems stack them — an SELinux box enforces MLS over a filesystem whose accounts are organized by role.

RBAC also connects back to [[Security Design Principles|least privilege]] more directly than any other model here: a role is least privilege made administratively tractable, because the privilege set is scoped to a job rather than to a person who has accumulated access across several jobs.

## See Also

- [[Security Models]]
- [[Chinese Wall Model]]
- [[Bell-LaPadula Model]]
- [[Biba Integrity Model]]
- [[Access Control Matrix]]
- [[Access Control Models]]
- [[Security Design Principles]]
- [[CSCE 465]]
