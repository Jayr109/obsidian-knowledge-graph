---
title: "Security Design Principles"
type: concept
tags: [csce465, security, design-principles, saltzer-schroeder]
sources: [csce465-lecture-02-security-overview, csce465-hw1-build-and-threat-model-an-ai-agent]
course: CSCE 465
updated: 2026-09-03
---

Ten principles for designing systems that resist attack, presented in [[CSCE 465]] as the closing third of the security overview. They are the Saltzer & Schroeder principles (from the 1975 paper *The Protection of Information in Computer Systems*), and they are the most durable content in the course: unlike a specific protocol or vulnerability class, these have not changed in fifty years. Each one is a design-time constraint, not a mechanism — they tell you how to arrange mechanisms, not which to use.

## The Ten Principles

### 1. Economy of Mechanism
**Keep the design as simple and as small as possible.**

The justification is about *verification*, not elegance. Errors that grant unwanted access will not surface during normal operation — nobody notices a door that fails to lock when nobody tries it. Finding them requires line-by-line verification, and that check fails on overly complicated systems. Simplicity is what makes the audit tractable.

### 2. Fail-Safe Defaults
**Base decisions on permissions rather than exclusions.**

The default configuration should be conservative: deny unless explicitly allowed. The lecture's firewall example makes the difference concrete:

| Configuration | Rule order | Attack on port 1433 |
|---|---|---|
| Blacklist | Deny port 23, **allow port \*** | Gets through |
| Whitelist | Allow port 80, **deny port \*** | Blocked |

Both administrators believed they had configured a firewall. The blacklist fails because it requires enumerating every bad thing, and the attacker only needs the one you forgot. The whitelist fails *closed*, so an oversight costs availability rather than security.

### 3. Complete Mediation
**Every access to every object must be checked for authority.**

Informally: no back doors. Every access, every time — not just the first one. Two implications the lecture draws:

- You need a foolproof method for **origin authentication**, since the check is only as good as the identity it checks against.
- **Caching should be viewed skeptically.** A cache is precisely a record of a check you are declining to repeat, so it trades mediation for speed. DNS cache poisoning is the canonical failure.

### 4. Open Design
**The design of a system should not be secret.**

Security must not depend on attackers' ignorance. Three arguments: attackers are well motivated, open design permits review and reassures skeptics, and keeping widely-distributed software secret is impossible anyway. The lecture's example is the **Content Scramble System (CSS)** for DVDs, broken in 1999 by a Norwegian group.

The correct pattern is **public algorithms with secret parameters** — the community verifies the design while each organization keeps its own secret instance (its keys). This is the same principle as Kerckhoffs's, and it is why [[Computer Security|security by obscurity]] is treated as a failure mode rather than a strategy.

### 5. Separation of Privilege
**A protection mechanism requiring two keys is more robust than one that admits the holder of a single key.**

Multiple independent conditions to reach a restricted resource. Physical-world examples: two keys to launch a missile, witnesses on marriage licenses, notarized documents, bank safety deposit boxes. In computer security the usual form is **separation of duty** — the employee who creates payment authorizations cannot also issue the checks.

### 6. Least Privilege
**Every program and user operates with the bare minimum privileges needed to function.**

A subject gets only the privileges required to complete its task. Privileges may be temporarily augmented for a specific action, but must be relinquished immediately on completion.

The lecture raises two honest caveats. Most systems lack the *granularity* of permissions to apply this precisely. And it poses the question directly: **does the root/administrator concept violate this principle?** The all-or-nothing superuser is the standard counterexample — it is the reason capability systems, `sudo`, and role separation exist.

### 7. Least Common Mechanism
**Minimize the amount of mechanism common to more than one user and depended on by all users.**

Read most commonly as *minimize shared channels*. Anything two users share is a potential path between them. Examples of mechanisms that exist to un-share: base/bounds memory protection, virtual memory, virtual machines, VPNs. The motivation is confidentiality and integrity protection against information flow and **side channels** — the shared resource leaks even when it is never explicitly read.

### 8. Psychological Acceptability
**Security settings should match what an ordinary user expects, and interfaces should be intuitive.**

Two implications, and the second is the sharper one:
1. If security isn't easy to use, people won't use it.
2. If *mandatory* security features aren't easy to use, people will use them **incorrectly** — which is often worse than not at all, because it produces the appearance of protection.

### 9. Work Factor
**Compare the cost of circumventing a mechanism against the resources of the expected attacker.**

Security is proportionate, not absolute. A university database protecting student grades faces snoopers and grade-changing students; a system protecting military secrets faces government intelligence organizations. The first needs less sophisticated measures than the second. Designing for the wrong adversary wastes budget in one direction and loses everything in the other.

### 10. Compromise Recording
**Sometimes recording the details of an intrusion beats preventing it.**

The explicit concession that prevention is not always the best buy. Internet-connected surveillance cameras protect a building *in lieu of* reinforcing doors and windows; office servers log all file accesses, mail, and browsing. This is the design-principle form of the [[Computer Security|detection]] goal, and it is why the course devotes a full unit to intrusion detection.

## The Through-Line

Principles 1–4 concern the *structure* of the mechanism (simple, closed by default, always checked, publicly reviewable). Principles 5–7 concern the *distribution* of authority (split it, minimize it, don't share it). Principles 8–10 concede that engineering meets reality — users are human, attackers have budgets, and prevention has a price.

Two of the ten (work factor, compromise recording) are explicitly economic. That is the lecture's larger argument restated: **defense is inherently more expensive than offense**, because the attacker needs only the weakest link. Principles that ration defensive effort are not compromises — they are the only way the economics work.

## Applied: the AI Agent Case

The first homework is a working demonstration that these principles are what actually fix modern systems. [[OpenClaw]]'s default `coding` profile runs tool calls with `ask=off` — no approval step — which is **fail-safe defaults inverted**. Its attack surface shows *per-layer trust checks with no unified policy*, so cross-layer attacks survive local fixes — a **complete mediation** failure at the level of composition rather than of any one check. And the durable fix for [[CVE-2024-5565]] is not to sanitize model output but to have the model emit a constrained spec a trusted renderer interprets: **economy of mechanism** and **least privilege** applied at the model boundary, so a permitted call cannot be repurposed.

The surface is new. The discipline is fifty years old.

## See Also

- [[Computer Security]]
- [[Security Policy and Mechanism]]
- [[Security Assurance]]
- [[Security Attack Taxonomy]]
- [[AI Agent Security]]
- [[Prompt Injection]]
- [[CVE-2024-5565]]
- [[CSCE 465]]
