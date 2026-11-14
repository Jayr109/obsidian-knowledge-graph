---
title: "CSCE 465"
type: course
tags: [csce465, security, network-security, cryptography, course]
sources: [csce465-lecture-01-course-introduction, csce465-lecture-02-security-overview, csce465-hw1-build-and-threat-model-an-ai-agent, csce465-lecture-03-introduction-to-cryptography, csce465-lecture-03a-secret-key-cryptography-i, csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation, csce465-lecture-05-public-key-cryptography, csce465-lecture-04-hash-functions, csce465-lecture-06a-user-authentication, csce465-lecture-07-operating-system-security, csce465-lecture-08-security-theory-policies-and-models, csce465-lecture-09-software-security-buffer-overflow, csce465-recitation-gdb-basics, csce465-lecture-10-network-basics, csce465-lecture-11-malware]
course: CSCE 465
updated: 2026-11-04
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
| Applied Cryptography | [[Cryptography\|Definitions and cryptanalysis]]; [[Classical Ciphers\|early ciphers]]; [[One-Time Pad]]; [[Secret Key Cryptography]] — [[Feistel Cipher]], [[DES]], [[Triple DES]], [[AES]]; [[Block Cipher Modes of Operation\|modes of operation]]; [[Stream Ciphers]]; [[Message Authentication Code\|MACs]]; [[Hash Functions\|hashes and message digests]] — [[MD5]], [[SHA-1]], [[HMAC]]; [[Public Key Cryptography]] — [[RSA]], [[Diffie-Hellman Key Exchange\|Diffie-Hellman]], [[Digital Signatures]], [[Public Key Infrastructure\|PKI]]; authentication and security handshake pitfalls |
| Authentication | [[User Authentication]] — [[Password Authentication\|passwords]], [[S/Key Protocol\|S/Key]], [[Biometrics]], [[Authentication Tokens\|tokens]]; security handshake pitfalls |
| OS and System Security | [[Operating System Security\|OS security]]; fundamental security theories — the [[Safety Problem\|safety problem]], [[Security Models\|security models]], [[Multi-Level Security\|MLS]], [[Bell-LaPadula Model\|BLP]], [[Biba Integrity Model\|Biba]], [[Chinese Wall Model\|Chinese Wall]], [[Role-Based Access Control\|RBAC]]; [[Access Control Models\|access control]] — [[Unix File Permissions\|Unix]] and [[NTFS Permissions\|NTFS]]; software security — [[Buffer Overflow\|buffer overflow]], [[Stack Smashing\|stack smashing]], [[Shellcode\|shellcode]], [[Format String Vulnerabilities\|format strings]], [[Buffer Overflow Defenses\|defenses]] and [[Stack Canaries\|canaries]] |
| Network Security | [[Internet Protocol\|TCP/IP basics]] — [[TCP]], [[ICMP]], [[HTTP]], [[SMTP]]; [[Malware\|malware]] — [[Computer Viruses\|viruses]], [[Worms\|worms]], [[Notable Worms\|case studies]], [[Botnets\|botnets]], [[Stuxnet]]; vulnerability analysis; firewalls; intrusion detection; web security |
| AI | AI agent and security — [[AI Agent Security]], [[Prompt Injection]], [[OpenClaw]] |

## Teaching Style

Four stated modes: **descriptive** (what is out there), **critical** (what is wrong with it), **skill-oriented** (homework and labs), and **interactive** (discussion counts toward the grade; students are encouraged to present findings).

## Ethics

The course studies threats and attacks directly, so ethics are stated as a course-level rule rather than a footnote: students are told to be fully aware of the ethics of the techniques being taught, and to ask the instructor first whenever the line is unclear. The Aggie Honor Code applies, and assignments must be written in the student's own words and code.

## Ingested Sources

- [[CSCE 465 Lecture 1 — Course Introduction]] — 39 slides; logistics plus the security definition, goals, and CIA triad
- [[CSCE 465 Lecture 2 — Security Overview]] — 50 slides; the foundations lecture — definition, attack taxonomy, policy/mechanism/assurance, and the ten design principles
- [[CSCE 465 HW1 — Build and Threat-Model an AI Agent]] — 31 slides; assignment brief, but two thirds real content on AI agent security and prompt injection
- [[CSCE 465 Lecture 3 — Introduction to Cryptography]] — 29 slides; opens the applied cryptography unit — definitions, cryptanalysis, early ciphers, the one-time pad, and the primitive taxonomy
- [[CSCE 465 Lecture 3a — Secret Key Cryptography (I)]] — ~63 slides; the first full algorithms — Feistel structure, DES component by component, Triple DES and meet-in-the-middle, AES, side channels
- [[CSCE 465 Lecture 3b — Secret Key Cryptography (II): Modes of Operation]] — ~37 slides; ECB/CBC/OFB/CFB/CTR, IVs, MACs, stream ciphers, and the CSS/DeCSS post-mortem
- [[CSCE 465 Lecture 4 — Hash Functions]] — ~47 slides; properties and the birthday attack, six applications, MD5, SHA-1, HMAC and the extension attack
- [[CSCE 465 Lecture 5 — Public Key Cryptography]] — ~59 slides; RSA end to end, Diffie-Hellman with its MITM attack, digital signatures, and PKI/CAs including the Comodo breach
- [[CSCE 465 Lecture 6a — User Authentication]] — ~46 slides; identification vs authentication, the four bases, passwords and salt, S/Key, biometrics, tokens
- [[CSCE 465 Lecture 7 — Operating System Security]] — ~42 slides; the boot chain as attack surface, cold boot, DAC/MAC and policy, Unix permissions, NTFS
- [[CSCE 465 Lecture 8 — Security Theory: Security Policies and Models]] — 47 slides; the undecidability of safety, then the four classical models — BLP, Biba, Chinese Wall, RBAC
- [[CSCE 465 Lecture 9 — Software Security: Buffer Overflow]] — ~47 slides; opens the software security unit — stack smashing end to end, heap/off-by-one/function-pointer/format-string variants, and the five defense families
- [[CSCE 465 Recitation — gdb Basics]] — 11 slides (one-up, TA-delivered); the debugger the buffer-overflow labs need, including `bt` and `info frame`
- [[CSCE 465 Lecture 10 — Network Basics]] — 26 slides; deliberate background for the network security unit — IP, TCP, ICMP, HTTP and SMTP, with telnet used to speak the last two by hand
- [[CSCE 465 Lecture 11 — Malware]] — 57 slides, the largest deck of the semester; the malware taxonomy, viruses, worms from Morris to Slammer, botnets and BotHunter, and Stuxnet

Decks are two-up (two logical slides per PDF page).

**Applied cryptography is complete** — secret key (ciphers, modes, MACs, stream ciphers), hashes (MD5, SHA-1, HMAC), and public key (RSA, Diffie-Hellman, signatures, PKI). **OS and system security** runs across Lectures 7 and 8 (mechanisms, then theory), **software security** opened with Lecture 9 (memory corruption), and **network security** opened with Lectures 10 and 11 (TCP/IP background, then malware). **Still outstanding: vulnerability analysis, firewalls, intrusion detection and web security**; the AI agent unit arrived early via HW1.

Decks run 1, 2, 3, 3a, 3b, 4, 5, **6a**, 7, 8, 9, 10, 11, plus a one-up gdb recitation. The **6a** label implies a **6b** — per the course outline, likely *authentication and security handshake pitfalls* — and there is no Lecture 6. Both are open gaps.

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
- [[Cryptography]]
- [[Cryptanalysis]]
- [[Cipher Security Models]]
- [[Classical Ciphers]]
- [[One-Time Pad]]
- [[Cryptography Taxonomy]]
- [[Secret Key Cryptography]]
- [[Block Ciphers]]
- [[Confusion and Diffusion]]
- [[Feistel Cipher]]
- [[DES]]
- [[Triple DES]]
- [[AES]]
- [[Block Cipher Modes of Operation]]
- [[Initialization Vector]]
- [[Message Authentication Code]]
- [[Stream Ciphers]]
- [[Content Scrambling System]]
- [[Public Key Cryptography]]
- [[RSA]]
- [[Diffie-Hellman Key Exchange]]
- [[Digital Signatures]]
- [[Public Key Infrastructure]]
- [[Hash Functions]]
- [[Birthday Attack]]
- [[Hash Function Applications]]
- [[MD5]]
- [[SHA-1]]
- [[HMAC]]
- [[User Authentication]]
- [[Password Authentication]]
- [[S/Key Protocol]]
- [[Biometrics]]
- [[Authentication Tokens]]
- [[Operating System Security]]
- [[Access Control Models]]
- [[Access Control Matrix]]
- [[Safety Problem]]
- [[Security Models]]
- [[Multi-Level Security]]
- [[Bell-LaPadula Model]]
- [[Biba Integrity Model]]
- [[Chinese Wall Model]]
- [[Role-Based Access Control]]
- [[Unix File Permissions]]
- [[NTFS Permissions]]
- [[Buffer Overflow]]
- [[Stack Smashing]]
- [[Shellcode]]
- [[Heap and Pointer Overflows]]
- [[Format String Vulnerabilities]]
- [[Unsafe C Functions]]
- [[Buffer Overflow Defenses]]
- [[Stack Canaries]]
- [[GDB]]
- [[Internet Protocol]]
- [[TCP]]
- [[ICMP]]
- [[HTTP]]
- [[SMTP]]
- [[Malware]]
- [[Computer Viruses]]
- [[Worms]]
- [[Notable Worms]]
- [[Search Worms]]
- [[Botnets]]
- [[Stuxnet]]
- [[Side-Channel Attacks]]
- [[CSCE 313]]
- [[Computer Networking]]
