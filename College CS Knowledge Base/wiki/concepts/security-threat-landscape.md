---
title: "Security Threat Landscape"
type: concept
tags: [csce465, security, malware, botnet, phishing, ransomware]
sources: [csce465-lecture-01-course-introduction, csce465-hw1-build-and-threat-model-an-ai-agent]
course: CSCE 465
updated: 2026-09-03
---

[[CSCE 465]] motivates itself with a survey of what is actually being attacked and how, rather than with a definition. The stated justification for the course is simply the **increased volume of security incidents**, followed by a named list of threat categories. This page holds that list with each item defined; the lecture itself gave the names plus news screenshots, so the definitions here are the standard ones rather than the instructor's own wording.

## The Named Threats

- **Malware** — software written to run against the interests of the system's owner: viruses, worms, trojans, spyware, rootkits. Malware analysis is one of the course's network security topics.
- **Spam** — unsolicited bulk messaging, mostly email. Its significance to security is as a *delivery channel*: spam is how phishing and malware reach the target at scale.
- **Botnet** — a population of compromised machines under a common command-and-control channel. Botnets are the mechanism that turns individual compromises into aggregate capability; the other threats on this list are frequently *powered* by one. Given its own slide in the lecture, which matches [[Guofei Gu]]'s BotHunter work.
- **DDoS attack** — distributed denial of service: exhausting a target's bandwidth, connection state, or compute from many sources at once so legitimate requests cannot be served. A pure [[CIA Triad|availability]] attack, and the canonical use of a botnet. Lecture 12 works two mechanisms through: [[SYN Flooding]], and the [[Smurf Attack]] with its DNS amplification variant.
- **Phishing** — inducing a person to hand over credentials or run attacker code by impersonating a trusted party. The attack surface is the user, not the software, which is why it survives technical hardening.
- **Ransomware** — malware that encrypts the victim's data and sells back the key. Notable for violating all three [[CIA Triad]] components at once.
- **AI/agentic attacks** — attacks carried out or amplified by AI systems and autonomous agents. The newest entry on the list, and the one the course treats as an active direction rather than settled material: the outline ends on "AI agent and security," and every homework is built on [[OpenClaw]]. This is now the best-documented category in the KB — see [[AI Agent Security]] and [[Prompt Injection]] — because the first assignment teaches it in depth.

## Relation to the Attack Taxonomy

This list names *what is out there*. [[Security Attack Taxonomy]] gives the orthogonal cut — *which property each attack violates* (interception, tampering, fabrication, interruption). Every item below can be placed in that taxonomy, and most span several: ransomware is interruption plus interception, a botnet is fabrication at the host level enabling interruption at the network level.

## Why the List Is Organized This Way

The list is not a taxonomy of mechanisms — it mixes a delivery channel (spam), an infrastructure (botnet), an effect (DDoS), a target class (phishing), and a business model (ransomware). That is the point: real incidents are compositions. A phishing email delivered as spam installs malware that enrolls the machine in a botnet, which is rented to launch a DDoS or to deploy ransomware. Studying any one category in isolation misses the chain, which is the argument for a survey course.

## Visual Gap

Slides 7–18 of the introductory deck are image-only — news headlines and incident screenshots illustrating the scale of recent breaches, plus a botnet architecture diagram on slide 15. None of that content is in the PDF text layer, so the specific incidents cited in lecture are **not** captured here. See the [[CSCE 465 Lecture 1 — Course Introduction|source page]] for the full extraction note.

## See Also

- [[Computer Security]]
- [[CIA Triad]]
- [[Security Attack Taxonomy]]
- [[AI Agent Security]]
- [[Prompt Injection]]
- [[CSCE 465]]
- [[Guofei Gu]]
- [[Malware]]
- [[Worms]]
- [[Notable Worms]]
- [[Botnets]]
- [[Stuxnet]]
- [[Computer Viruses]]
- [[SYN Flooding]]
- [[Smurf Attack]]
