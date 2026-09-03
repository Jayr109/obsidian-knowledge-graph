---
title: "Security Policy and Mechanism"
type: concept
tags: [csce465, security, policy, mechanism, foundations]
sources: [csce465-lecture-02-security-overview]
course: CSCE 465
updated: 2026-09-01
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
- [[Security Assurance]]
- [[Security Services]]
- [[Security Design Principles]]
- [[CSCE 465]]
