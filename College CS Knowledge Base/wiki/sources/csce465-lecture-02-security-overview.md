---
title: "CSCE 465 Lecture 2 — Security Overview"
type: source
tags: [csce465, security, foundations, design-principles, attacks, assurance]
sources: []
course: CSCE 465
updated: 2026-09-01
---

Lecture 2 of [[CSCE 465]] (`raw/CSCE465_02_SecurityOverview.2026.pdf`, 25 PDF pages laid out two slides per page = 50 logical slides, instructor [[Guofei Gu]]). This is the course's real foundations lecture — where Lecture 1 was mostly logistics, this deck is almost entirely content. It follows a four-part roadmap: security definition and objectives, threats and attacks, achieving security (policy / mechanism / assurance), and security design principles.

## Structure

| Slides | Section | Content |
|---|---|---|
| 3–11 | **Definition and objectives** | Formal definition; CIA components; confidentiality interpretations; crypto ≠ confidentiality; integrity prevention vs detection; commercial and military examples; InfoSec = CompSec + ComSec |
| 12–15 | **Motivation** | Why security matters (critical infrastructure); why security is hard (three slides) |
| 16–24 | **Threats and attacks** | Threat vs attack; active vs passive; interception, tampering, fabrication, interruption; packet capture; MITM; impact |
| 25–32 | **Achieving security** | Policy / mechanism / assurance; prevention-detection-recovery; security services; trust and assumptions; the cost trade-off |
| 33–38 | **Assurance in practice** | Security by obscurity; security by legislation; specification-design-implementation; operational issues; human issues; the security life-cycle |
| 39–50 | **Design principles** | The ten Saltzer & Schroeder principles, one or two slides each |

## Content Worth Keeping

**A second, formal definition.** Security is a *state of well-being of information and infrastructures* in which successful yet **undetected** theft, tampering, and disruption is kept **low or tolerable**. The concession to tolerance and the emphasis on *undetected* are both new relative to Lecture 1. → [[Computer Security]]

**Confidentiality is context-dependent.** Data, existence, and configuration confidentiality are three different claims, and encryption only addresses the first. *Who is talking to whom is itself important information.* → [[CIA Triad]], [[Security Attack Taxonomy]]

**Integrity mechanisms prevent or detect, and both have costs.** Prevention keeps the system consistent but is hard to design and cannot handle malicious insiders; detection is easier (checksums, consistency checks) but leaves causes unknown. → [[CIA Triad]]

**Why security is hard.** Eight structural reasons, ending on the one that governs the rest: defense is inherently more expensive than offense, because **offense only needs the weakest link**. → [[Computer Security]]

**Four attack families, one per violated property.** Interception (confidentiality), tampering (integrity), fabrication (authenticity), interruption (availability), plus MITM as the position that enables all four. → [[Security Attack Taxonomy]]

**Three questions: what, how, how well.** Policy, mechanism, assurance. Prevention is more fundamental than detection because detection depends on an audit trail that prevention must protect — but for authorized-privilege misuse and in-network message modification, detection is the *only* option. → [[Security Policy and Mechanism]]

**Six security services.** Confidentiality, authentication, integrity, non-repudiation, access control, monitor & response. → [[Security Services]]

**Assurance is economic.** Security ↔ functionality ↔ ease of use ↔ cost is a four-way trade-off, not a solvable optimization. Security by obscurity and security by legislation are both named and rejected as *principal* strategies. → [[Security Assurance]]

**The ten design principles.** Economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability, work factor, compromise recording. The most durable material in the course. → [[Security Design Principles]]

## Internal Inconsistency Worth Noting

Slide 4 (the definition) says security rests on **confidentiality, authenticity, integrity, and availability** — four properties. Slide 5 (basic components) lists **three**, folding authenticity into integrity as *origin integrity*. Both framings are standard; the lecture uses the four-way split when classifying attacks (fabrication attacks authenticity specifically) and the three-way split when listing objectives. Recorded on [[CIA Triad]] rather than silently normalized to one.

## Open Questions the Lecture Poses and Does Not Answer

These are left as discussion prompts, and are the likeliest exam material:

- On a **switched network**, what can a promiscuous-mode `tcpdump` actually see? What do DNS lookups, header-only packets, and payloads each reveal?
- Where else should **caching be viewed skeptically** under complete mediation? (The slide gives DNS cache poisoning as the cue.)
- Does the **root/administrator user concept violate least privilege?**

## Extraction Note

Text extracted with PyMuPDF, same as Lecture 1. **Unlike Lecture 1, this deck has no image-only slides** — all 25 pages carry substantive text, and the extraction is essentially complete. Several slides are diagram-supported (the A→B attacker diagrams for each attack family, the two firewall configurations for fail-safe defaults, the CompSec/ComSec Venn diagram, the ten-principle wheel), but in every case the accompanying text carries the content, so nothing is lost. The one figure whose detail is not recoverable is the OC3Mon packet-capture appliance photo on slide 18; its specification (rack-mounted PC, optical splitter, DAG card, source endace.com) is in the text.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Computer Security]]
- [[CIA Triad]]
- [[Security Attack Taxonomy]]
- [[Security Policy and Mechanism]]
- [[Security Services]]
- [[Security Assurance]]
- [[Security Design Principles]]
- [[CSCE 465 Lecture 1 — Course Introduction]]
