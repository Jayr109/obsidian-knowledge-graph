---
title: "Security Services"
type: concept
tags: [csce465, security, services, authentication, non-repudiation, access-control]
sources: [csce465-lecture-02-security-overview]
course: CSCE 465
updated: 2026-09-01
---

Security functions are made available to users as a set of **security services**, exposed through APIs or integrated interfaces. [[CSCE 465]] lists six. The list is worth memorizing as a list, because it is the layer where the abstract [[CIA Triad]] becomes something a system actually offers a caller.

## The Six Services

**Confidentiality** — protection of any information from exposure to unintended entities. The lecture is explicit that this covers more than payload:
- Information content
- The parties involved
- Where they are, how they communicate, how often

That second and third bullet are the reason encryption alone is not confidentiality — see [[Security Attack Taxonomy|does cryptography guarantee confidentiality?]].

**Authentication** — assurance that an entity of concern, or the origin of a communication, is authentic: it is what it claims to be, or from whom it claims to be. This is [[CIA Triad|origin integrity]] offered as a service.

**Integrity** — assurance that information has not been tampered with.

**Non-repudiation** — evidence that a party *was indeed* the sender or receiver of certain information. Note what makes this distinct: authentication convinces the receiver, non-repudiation convinces a **third party** later, and does so over the sender's objection. It is the only service on the list whose adversary is the legitimate participant rather than an outsider, which is why it needs asymmetric cryptography (a shared secret proves nothing to an outsider, since either holder could have produced the evidence).

**Access control** — facilities to determine and enforce who may access what: resources, hosts, software, network connections. This is where a [[Security Policy and Mechanism|policy]] becomes an enforceable mechanism.

**Monitor and response** — facilities for monitoring security attacks, generating indications, surviving (tolerating) attacks, and recovering from them. The service form of the detection and recovery goals.

## How the Services Map to the Goals

| Service | Primary [[CIA Triad]] component | Mechanism family |
|---|---|---|
| Confidentiality | Confidentiality | Prevention |
| Authentication | Integrity (origin) | Prevention |
| Integrity | Integrity (data) | Prevention or detection |
| Non-repudiation | Integrity (origin), after the fact | Detection / evidence |
| Access control | All three | Prevention |
| Monitor & response | Availability, and recovery generally | Detection and recovery |

**Cryptography underlies many security mechanisms** — the lecture states this directly, and it is why the applied cryptography unit comes before the OS, network, and web units rather than after. Four of the six services above are implemented primarily with cryptographic primitives.

## See Also

- [[CIA Triad]]
- [[Security Policy and Mechanism]]
- [[Security Attack Taxonomy]]
- [[Computer Security]]
- [[CSCE 465]]
