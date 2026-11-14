---
title: "CIA Triad"
type: concept
tags: [csce465, security, foundations, confidentiality, integrity, availability]
sources: [csce465-lecture-01-course-introduction, csce465-lecture-02-security-overview, csce465-lecture-08-security-theory-policies-and-models]
course: CSCE 465
updated: 2026-10-20
---

The **CIA triad** — Confidentiality, Integrity, Availability — is the standard decomposition of what "secure" means, and the framing [[CSCE 465]] uses to organize the rest of the course. Any security goal, mechanism, or attack in the course can be located against one or more of the three; naming which component an attack violates is usually the first analytical step.

## Confidentiality

Keeping data and resources **hidden** from parties not entitled to them. The primary mechanism family is cryptography — secret-key and public-key encryption, both of which get their own unit — supplemented by access control at the OS level.

**Confidentiality means different things in different contexts**, and Lecture 2 insists the precise notion depends on the environment the system will be used in. Three distinct interpretations:

| Kind | Example claim |
|---|---|
| **Data** | "No one should know my bank account balance" |
| **Existence** | "No one should know that I shop at XYZ.com" |
| **Configuration** | "No one should know what software I run" |

Only the first is protected by encrypting content. Existence confidentiality is violated by traffic analysis; configuration confidentiality is violated by fingerprinting. This is why the lecture asks directly whether cryptography guarantees confidentiality — and answers no: **who is talking to whom is itself important information**. See [[Security Attack Taxonomy]].

## Integrity

Preventing **unauthorized changes** to data or resources. The lecture splits this in two, and the split is load-bearing:

- **Data integrity** — the content has not been altered. Enforced by hashes and message digests.
- **Origin integrity** — the content came from who it claims to have come from. This is **authentication**.

The two are independent. A message can be unmodified but forged (data integrity without origin integrity), or genuinely from the right sender but tampered with in transit (origin integrity without data integrity). Most real protocols need both, which is why the cryptography unit covers hashes and authentication as one continuous topic rather than separately.

Lecture 2 gives each half a question that makes the distinction concrete:

- **Data integrity** — *"Is my bank account balance correct?"*
- **Origin integrity** — *"Was this application really written by Microsoft?"*

**Integrity mechanisms can either prevent or detect violations**, and the lecture states the trade-off rather than picking a winner:

| Approach | Pro | Con |
|---|---|---|
| **Prevention** | Keeps the system consistent | Difficult to design. "Easy" to keep bad guys out — but how do you identify malicious *insiders*? |
| **Detection** | Easier to design in some cases (file checksums, transaction consistency checks) | Causes of violations often remain unknown |

The insider question is the one that recurs all course: prevention assumes you can tell authorized from unauthorized, and against an insider that assumption fails by definition. See [[Security Policy and Mechanism]].

## Availability

Enabling **access** to data and resources for parties entitled to them. This is the component that non-security engineering already cares about under other names (uptime, reliability), but the security version assumes the loss is deliberate: a [[Security Threat Landscape|DDoS attack]] or ransomware makes a system unavailable on purpose.

## Formal Statement

Lecture 8 gives each component a set-theoretic definition before building [[Security Models|security models]] on them. In all three, **X** is a set of entities and **I** is information (or, for availability, a resource):

| Component | *I* has the property with respect to *X* if… |
|---|---|
| **Confidentiality** | **no** *x* ∈ *X* can obtain information from *I* |
| **Integrity** | **all** *x* ∈ *X* **trust** information in *I* |
| **Availability** | **all** *x* ∈ *X* can **access** *I* |

Confidentiality's definition carries a clause worth noticing: ***I* can be disclosed to others.** The property is relative to *X*, not absolute — the final exam answer key is confidential with respect to the students while being freely available to the instructors. Every confidentiality claim is implicitly a claim about *whom* data is hidden from, which is why [[Security Models|a policy must name its subjects]] before it can be evaluated.

The formal integrity definition also sharpens the data/origin split above into three kinds:

- **Data integrity** — trust in *I*, its conveyance and its protection
- **Origin integrity** — *I* is information about the origin of something, or an identity. This is **authentication**
- **Assurance** — *I* is a resource, and integrity means the resource **functions as it should**. See [[Security Assurance]]

Availability likewise splits in two:

- **Traditional** — *x* gets access or does not
- **Quality of service** — *x* was promised a *level* of access (a specific bandwidth, say) and does not get it, **even though some access is achieved**

The QoS case is the one that catches people out: a system can be degraded to uselessness while every availability check reports success.

## Two Worked Examples

The lecture instantiates all three components twice, which is a useful exam pattern — the same triad, different stakes:

| | Commercial | Military |
|---|---|---|
| **Confidentiality** | An employee should not learn their manager's salary | Missile target coordinates should not be improperly disclosed |
| **Integrity** | An employee should not be able to modify their own salary | Target coordinates should not be improperly modified |
| **Availability** | Paychecks should be printed on time as stipulated by law | When the proper command is issued, the missile should fire |

Note that the commercial availability example is a *legal* obligation, not a technical one. Availability requirements usually come from outside the system.

## Three Components or Four?

Worth flagging, because the lecture is internally inconsistent on exactly one point. The **definition** slide says security rests on *confidentiality, authenticity, integrity, and availability* — four properties. The **components** slide immediately after lists three, folding authenticity into integrity as origin integrity.

Both framings are standard and neither is wrong; they differ in whether authentication is promoted to a top-level property. The course's own [[Security Attack Taxonomy|attack taxonomy]] uses the four-way split (it names a distinct *fabrication* attack against authenticity), while the components slide and [[Security Services]] use the three-way one. Expect either on an exam, and say which you are using.

## Why All Three

The three pull against each other, and a mechanism that maximizes one often costs another. An encrypted, offline, air-gapped archive is excellent for confidentiality and terrible for availability. Ransomware is the clean example of a single attack that violates confidentiality (data exfiltrated), integrity (data encrypted in place), and availability (the owner locked out) at once.

## See Also

- [[Computer Security]]
- [[Security Models]]
- [[Multi-Level Security]]
- [[Cryptography]]
- [[Cryptography Taxonomy]]
- [[Security Attack Taxonomy]]
- [[Security Services]]
- [[Security Policy and Mechanism]]
- [[Security Threat Landscape]]
- [[CSCE 465]]
