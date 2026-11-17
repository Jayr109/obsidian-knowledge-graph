---
title: "Computer Security"
type: concept
tags: [csce465, security, foundations]
sources: [csce465-lecture-01-course-introduction, csce465-lecture-02-security-overview]
course: CSCE 465
updated: 2026-09-10
---

Security, informally, is **the prevention of certain types of intentional actions from occurring**. The definition is deliberately built around *intent*: an accidental disk failure and a deliberate wipe can destroy the same data, but only the second is a security problem. This is the entry point for [[CSCE 465]], and everything else in the course — the [[CIA Triad|three components]], the four goals below, and the [[Security Threat Landscape|catalogue of real attacks]] — is an elaboration of it.

## Two Definitions

Lecture 1 gives the informal one above. Lecture 2 gives a formal one, and the difference between them is instructive:

> Security is a **state of well-being of information and infrastructures** in which the possibility of successful yet **undetected** theft, tampering, and disruption of information and services is kept **low or tolerable**.

Three things this adds. It is a property of a *state*, not of an action. It concedes that the goal is "low or tolerable" rather than zero — security is a risk position, not an absolute. And the word **undetected** does real work: an attack you detect and recover from is a different, lesser failure than one you never learn about. That single word is why [[Security Policy and Mechanism|detection]] ranks alongside prevention.

The formal definition names four properties — confidentiality, authenticity, integrity, availability — while the components slide names three. See [[CIA Triad]] for why both are standard.

## Core Vocabulary

The four terms are defined as a chain, and the course uses them precisely:

| Term | Definition |
|---|---|
| **Threat** | A potential intentional action that security aims to prevent |
| **Attack** | A threat that is actually carried out |
| **Attacker** | The party carrying out an attack |
| **Asset** | The object an attack is directed at |

The chain matters because the three quantities you can actually manipulate are different: you cannot remove attackers, you can rarely remove threats, but you can harden assets and raise the cost of attacks. A **vulnerability** is the property of an asset that lets a threat become an attack — the course's third homework unit is vulnerability analysis.

## Goals of Security

The lecture separates four goals, in increasing order of pessimism about whether defense works:

- **Prevention** — stop attackers from violating the security policy at all
- **Detection** — notice when the policy *has* been violated
- **Recovery** — stop the attack in progress, then assess and repair the damage
- **Survivability** — keep functioning correctly *even if* the attack succeeds

Prevention is the only goal that assumes defense wins. The other three assume it does not, which is why [[Intrusion Detection Systems|intrusion detection]] is a full unit of the course rather than a fallback. Survivability is the strongest: it demands correct function under active compromise, not merely a return to correctness afterward.

Lecture 2 collapses these into three mechanism families — prevention, detection, response/recovery — with survivability folded into recovery, and argues that **prevention is more fundamental** because detection depends on an audit trail that prevention must protect. See [[Security Policy and Mechanism]].

## Why Security Is Hard

Lecture 2 spends three slides on this, and the reasons are structural rather than technical:

- **Lack of awareness of threats and risks.** Security measures are often not considered until after an enterprise has been penetrated. (Improving, but slowly.)
- **Historical reluctance to invest.** The Windows lineage from 95 through 2000, XP, XP SP2, Vista, 7, and 10 is offered as the trajectory of a vendor gradually taking security seriously — but **legacy software persists**, so the old assumptions never fully retire.
- **Lack of security in the TCP/IP protocol suite.** Most TCP/IP protocols were not built with security in mind; the IETF is still retrofitting. This is the direct cause of the network attacks in [[ARP]] and the network security unit.
- **Complexity of security management and administration.** Security is not just encryption and authentication.
- **Software vulnerabilities** — buffer overflows named specifically; better tools and techniques are needed.
- **Complexity of computers and networks**, and **wide-open network policies** at many Internet sites.
- **Attacker skills keep improving** — and attacking is a *business*, with the incentives that implies.
- **User ignorance**, exploited through social engineering.

The last item is the general principle: **defense is inherently more expensive than offense, because offense only needs the weakest link.** A defender must secure every path; an attacker must find one. This asymmetry is the economic fact underneath the entire field, and it is why two of the ten [[Security Design Principles]] are explicitly about rationing defensive effort.

## Information Security = Computer Security + Communications Security

The lecture positions the field as the union of two older ones: **CompSec** (security for computers) and **ComSec** (security for communications and networking) together make **InfoSec**. This is the structural reason [[CSCE 465]] is titled *Computer & Network Security* and why its units alternate between host-side and wire-side concerns.

Why it matters at all: computers and networks are the nerves of basic services and critical infrastructure — financial services and commerce, transportation, power grids — and they are targets of attack by adversaries.

## Policy, Mechanism, Assurance

The course's three organizing questions — *what?*, *how?*, *how well?* — are developed on their own pages:

- **Policy and mechanism** — what is allowed, and what enforces it: [[Security Policy and Mechanism]]
- **Assurance** — how well the mechanisms guarantee the policy, and what it costs: [[Security Assurance]]
- **Services** — the six functions exposed to users: [[Security Services]]
- **Design principles** — the ten constraints on how mechanisms are arranged: [[Security Design Principles]]
- **Cryptography** — the mechanism family underlying most of the others: [[Cryptography]], [[Cryptography Taxonomy]]

The distinction students most often collapse: a violation is always a violation *of a policy*, so with no policy stated, "secure" has no meaning. Mechanisms without assurance are the normal failure mode in practice — the system has a [[Firewalls|firewall]], and no one has checked what it enforces.

## Ethics

Because studying defense requires studying attack, [[CSCE 465]] states ethics as a standing rule: be fully aware of the ethics of any technique being learned, and ask the instructor before acting whenever the line is unclear.

## See Also

- [[CIA Triad]]
- [[Security Policy and Mechanism]]
- [[Security Assurance]]
- [[Security Services]]
- [[Security Design Principles]]
- [[Security Attack Taxonomy]]
- [[Cryptography]]
- [[Security Threat Landscape]]
- [[Vulnerability Analysis]]
- [[Firewalls]]
- [[Intrusion Detection Systems]]
- [[CSCE 465]]
- [[Guofei Gu]]
