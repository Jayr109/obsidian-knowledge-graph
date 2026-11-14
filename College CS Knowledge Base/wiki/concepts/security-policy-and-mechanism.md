---
title: "Security Policy and Mechanism"
type: concept
tags: [csce465, security, policy, mechanism, foundations]
sources: [csce465-lecture-02-security-overview, csce465-lecture-08-security-theory-policies-and-models]
course: CSCE 465
updated: 2026-10-20
---

[[CSCE 465]] frames the whole engineering problem as three questions asked in order:

| Question | Answer |
|---|---|
| **What?** | Security **policy** |
| **How?** | Security **mechanism** |
| **How well?** | [[Security Assurance\|Security assurance]] |

Keeping these separate is the single most useful discipline in the course. Most confused security arguments are a mechanism being offered as an answer to a policy question, or a policy being assumed to hold because a mechanism exists.

## Policy

**A policy says what is, and what is not, allowed.** It *defines* security for a given site or system — which means the word "secure" is meaningless until a policy is stated. There is no property a system has in isolation; there is only conformance to a stated partition of allowed and disallowed states.

**Composition of policies** is where this gets dangerous. When two policies are combined and they conflict, the discrepancies themselves create vulnerabilities. Nothing about two individually-sound policies guarantees their composition is sound — a recurring theme wherever two systems with different assumptions are integrated.

### Formally: A Policy Partitions States

Lecture 8 restates the same idea as a state machine, which is the form the theory unit needs:

> A policy partitions system states into:
>
> - **Authorized (secure)** — states the system can enter
> - **Unauthorized (nonsecure)** — if the system enters any of these, it is a security violation
>
> A **secure system** starts in an authorized state and **never** enters an unauthorized state. A **breach of security** occurs when a system enters an unauthorized state.

Security is therefore a property of **every reachable state**, not of a snapshot — which is exactly why the general question of whether a system is secure turns out to be [[Safety Problem|undecidable]].

### The Cheating Example

The lecture's test of whether the definition has teeth:

> Policy disallows cheating, including copying homework with or without permission. A class has students do homework on a computer. **Anne forgets to read-protect her homework file. Bill copies it.** Who cheated?

| | Verdict | Why |
|---|---|---|
| **Bill** | **Cheated** | The policy forbids copying; he did it; the system entered an unauthorized state (Bill holding a copy of Anne's assignment) |
| **Anne** | **Did not breach security** | Read-protecting her homework was **not required by the policy**. Had the policy said students must read-protect homework files, she *would* have breached it — she did not do this |

The lecture adds that even if copying is not explicit in the computer security policy it is certainly implicit: *it is not credible that a unit of the university allows something the university as a whole forbids, unless the unit explicitly says so.*

> **Why this example is doing real work, derived.** It separates *carelessness* from *violation*. Anne's omission is what made the breach possible and is still not a breach, because a policy is a written partition of states and nothing else — blame tracks the document, not the causal chain. The same slide quietly makes the opposite point too: the policy could easily have been written to make Anne's omission a violation, and whether it was is a drafting decision made before anyone ran any code. That is the practical content of "the word *secure* is meaningless until a policy is stated."

## Mechanism

**Mechanisms enforce policies.** They fall into three general types, which are also the [[Computer Security|goals of security]]:

- **Prevention** — stop attackers from violating the policy
- **Detection** — detect attackers' violations of the policy
- **Response/Recovery** — stop the attack, assess and repair damage, and continue functioning correctly even if the attack succeeds

### Prevention Is More Fundamental

The lecture argues prevention has priority, with a specific reason: **detection requires that the audit trail be protected from alteration.** Detection is not an independent alternative — it presupposes a preventive mechanism guarding the log. An attacker who can rewrite the audit trail has defeated detection without ever being prevented.

### But Sometimes Detection Is the Only Option

Two cases where prevention is unavailable in principle:

- **Accountability in the proper use of authorized privileges.** If a subject is genuinely authorized, there is nothing to prevent — misuse is indistinguishable from use at the moment of access. Only after-the-fact review separates them. This is the insider problem in its purest form.
- **Modification of messages in a network.** You cannot stop an attacker who controls a link from altering bits; you can only make the alteration detectable.

This asymmetry is why the course treats intrusion detection as a full topic rather than a fallback, and why [[Security Design Principles|compromise recording]] is one of the ten design principles.

## Trust and Assumptions

Trust underlies every aspect of security, and the lecture makes the assumptions explicit because they are where real systems fail:

**For policies:**
- They unambiguously partition system states into allowed and disallowed
- They correctly capture the security requirements

**For mechanisms:**
- They are assumed to enforce the policy
- The supporting mechanisms they depend on work correctly

Every one of these is an assumption, not a guarantee. A policy that partitions ambiguously, or that partitions cleanly but captures the wrong requirement, produces a system that is provably conformant and still insecure.

## See Also

- [[Computer Security]]
- [[Safety Problem]]
- [[Security Models]]
- [[Access Control Matrix]]
- [[Security Assurance]]
- [[Security Services]]
- [[Security Design Principles]]
- [[CSCE 465]]
