---
title: "Guofei Gu"
type: person
tags: [instructor, security, network-security, CSCE 465]
sources: [csce465-lecture-01-course-introduction, csce465-lecture-02-security-overview, csce465-hw1-build-and-threat-model-an-ai-agent, csce465-lecture-03-introduction-to-cryptography, csce465-lecture-03a-secret-key-cryptography-i, csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation, csce465-lecture-05-public-key-cryptography, csce465-lecture-04-hash-functions, csce465-lecture-06a-user-authentication, csce465-lecture-07-operating-system-security, csce465-lecture-11-malware]
course: CSCE 465
updated: 2026-11-04
---

Guofei Gu is a professor in the Department of Computer Science & Engineering at Texas A&M University, director of the SUCCESS Lab, and the instructor for [[CSCE 465]] (Computer & Network Security).

## Courses Taught

- [[CSCE 465]] — Computer & Network Security (465/765)

## SUCCESS Lab

The **Secure Communication and Computer Systems (SUCCESS) Lab** (`https://success.cse.tamu.edu/`) works across three stated areas:

- **Intelligent Security** — AI for cybersecurity, and security *for* AI
- **Programmable Security** — next-generation networks and systems: SDN, cloud, edge, 5G
- **Ubiquitous Security** — pervasive and emerging technology: mobile, IoT, web, Web3

Those three areas map onto the course's own trajectory, which ends on AI agent security rather than treating it as an aside.

## Background as Presented

The introductory lecture lists 21,000+ citations, several best-paper and Test-of-Time awards, and papers among the most-cited security work of the past four decades. Named systems include **BotHunter** (botnet detection), **FRESCO** (an SDN security framework), and the commercially transferred **SMASH**. Recognition includes IEEE Fellow and ACM Distinguished Member. The lab was advertised as having openings.

The BotHunter lineage explains why the course's own [[Security Threat Landscape|threat survey]] gives botnets their own slide, and why intrusion detection is one of the four homework units.

**BotHunter arrived as course content in Lecture 11.** The malware lecture's botnet section closes on *BotHunter: Detecting Malware Infection Through IDS-Driven Dialog Correlation* (Gu, Porras, Yegneswaran, Fong & Lee), alongside *A Multi-perspective Analysis of the Storm (Peacomm) Worm* (Porras, Saïdi & Yegneswaran). The lecture's stated open research questions — botnet detection under varying vantage points, whether a botnet's operation can be disabled, click-fraud and phishing detection — are the lab's agenda presented as coursework. See [[Botnets]].

## Publications Used in the Course

*A Security Analysis of the OpenClaw AI Agent Framework* (Suwansathit, Zhang & Gu, 2026) is assigned reading for HW1. It supplies the 10-interface attack-surface taxonomy and the list of 470 advisories that students draw their Task 4 advisory from. Its central finding — *per-layer trust checks, no unified policy, so cross-layer attacks resist local fixes* — is recorded on [[OpenClaw]].

This is the clearest instance of the lab's stated "Security for AI" direction feeding directly into the course: the homework platform, the reading, and the bonus task all sit on the group's own research.

## See Also

- [[CSCE 465]]
- [[Security Threat Landscape]]
- [[Botnets]]
- [[Malware]]
- [[OpenClaw]]
- [[AI Agent Security]]
- [[Computer Security]]
