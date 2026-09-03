---
title: "CSCE 465"
type: course
tags: [csce465, security, network-security, cryptography, course]
sources: [csce465-lecture-01-course-introduction, csce465-lecture-02-security-overview, csce465-hw1-build-and-threat-model-an-ai-agent]
course: CSCE 465
updated: 2026-09-03
---

CSCE 465/765 (Computer & Network Security) is Texas A&M's security course, taught by [[Guofei Gu]] of the SUCCESS Lab. It is a survey of the whole field rather than a deep dive into one part: the arc runs background and security principles → applied cryptography → OS and software security → network security → AI agent security. The 465 (undergraduate) and 765 (graduate) sections share lectures; 765 additionally requires a mini-research project.

## Logistics

- **Instructor:** [[Guofei Gu]], Office 239 Peterson; office hour 3–4pm Tuesday or by appointment
- **TA:** Yuxuan Zhang (`yuz516@tamu.edu`), 242 Peterson (SUCCESS Lab); office hours **Thursdays 2–4 PM** (given as TBD in Lecture 1, fixed in the HW1 briefing)
- **Platforms:** Canvas for schedule and slides, Piazza for discussion/Q&A, email
- **Prerequisites:** [[CSCE 313]]; C/C++ programming experience and networking knowledge required; OS and discrete math assumed

## Grading

| Component | Weight |
|---|---|
| Assignments (4 homeworks/labs) | 50% |
| Exam 1 | 20% |
| Final Exam | 25% |
| Course participation | 5% |

Scale is standard 90/80/70/60. Late homework loses 20% per day. Regrade window is one week after grades are returned. Bonus points appear on some homework/labs. Academic misconduct results in an F*.

## Homework and Labs

Four assignments, each mixing paper-and-pencil questions with programming/lab work, run on real systems inside a virtual machine and virtual network:

1. **[[OpenClaw]] AI agent system** — serves as the shared base for all four assignments
2. **Applied cryptography**
3. **OS and software security**
4. **Network security and intrusion detection**

Some work is individual, some allows teams of two. The stated expectation is *learning by doing and by trial-and-error* — reports are graded on the learning experience (how the trial-and-error went) rather than only the final outcome. Students are expected to explore beyond lecture content.

### HW1 — Build and Threat-Model an AI Agent

120 points, **individual**, plus an optional bonus worth up to 200. Full requirements on [[CSCE 465 HW1 — Build and Threat-Model an AI Agent]].

| Task | Pts |
|---|---|
| 1 — Build and verify the lab | 40 |
| 2 — Harmless local tool + web lab | 20 |
| 3 — Direct vs. indirect injection experiment | 20 |
| 4 — Threat model + one real advisory | 35 |
| Clarity, Git history, AI-use record | 5 |

The bonus (100 points per accepted new OpenClaw vulnerability, up to two) is due **the last day of Fall classes**, not the HW1 deadline, and is graded separately.

### AI Use Policy

AI tools are permitted for learning, brainstorming, debugging, and coding, but the report must be written by the student in their own words. **Prompts and AI responses must be submitted** alongside it, plus an `AI_USAGE.md` describing what was used and where. A largely AI-generated report loses credit and may be treated as an integrity issue. The student remains responsible for explaining everything submitted.

### Lab Safety Rules

All work stays inside the course VM: NAT networking only, never bridged; no touching campus networks, public IPs, or other students' machines; fake secrets and harmless marker files only; no reverse shells, persistence, credential theft, cryptomining, or real command-and-control; no personal accounts, SSH keys, or cloud credentials connected to the agent; no host home directory or Docker socket mounted into an agent container.

## Mini-Research Project

Required for 765, optional but encouraged for 465. Teams of up to two design, implement, and evaluate a new attack, defense, system, tool, or service. Choosing it **replaces one homework and the final exam**. Process: topic selection and team formation (must talk to the instructor), monthly updates to instructor and TA, then an in-class presentation and written report. Graded on novelty, depth, correctness, clarity, and effort; bonus points for excellent projects and a people's-choice best project award. Project categories: analysis, measurement, development/implementation, algorithm design with a clear application, a new attack, or replicating and improving an important tool.

## Course Outline

| Unit | Topics |
|---|---|
| Background | [[CIA Triad]]; [[Security Policy and Mechanism\|security policies and mechanisms]]; [[Security Assurance\|assurance]]; [[Security Design Principles\|design principles]] |
| Applied Cryptography | Secret key cryptography; hashes and message digests; public key cryptography; authentication and security handshake pitfalls |
| OS and System Security | OS security; fundamental security theories; access control; software security |
| Network Security | Malware; vulnerability analysis; firewalls; intrusion detection; web security |
| AI | AI agent and security — [[AI Agent Security]], [[Prompt Injection]], [[OpenClaw]] |

## Teaching Style

Four stated modes: **descriptive** (what is out there), **critical** (what is wrong with it), **skill-oriented** (homework and labs), and **interactive** (discussion counts toward the grade; students are encouraged to present findings).

## Ethics

The course studies threats and attacks directly, so ethics are stated as a course-level rule rather than a footnote: students are told to be fully aware of the ethics of the techniques being taught, and to ask the instructor first whenever the line is unclear. The Aggie Honor Code applies, and assignments must be written in the student's own words and code.

## Ingested Sources

- [[CSCE 465 Lecture 1 — Course Introduction]] — 39 slides; logistics plus the security definition, goals, and CIA triad
- [[CSCE 465 Lecture 2 — Security Overview]] — 50 slides; the foundations lecture — definition, attack taxonomy, policy/mechanism/assurance, and the ten design principles
- [[CSCE 465 HW1 — Build and Threat-Model an AI Agent]] — 31 slides; assignment brief, but two thirds real content on AI agent security and prompt injection

Decks are two-up (two logical slides per PDF page). The background unit is now covered; cryptography, OS/software security, network security, and AI agent security are outstanding.

## See Also

- [[Guofei Gu]]
- [[Computer Security]]
- [[CIA Triad]]
- [[Security Attack Taxonomy]]
- [[Security Policy and Mechanism]]
- [[Security Services]]
- [[Security Assurance]]
- [[Security Design Principles]]
- [[Security Threat Landscape]]
- [[AI Agent Security]]
- [[Prompt Injection]]
- [[OpenClaw]]
- [[CVE-2024-5565]]
- [[CSCE 313]]
- [[Computer Networking]]
