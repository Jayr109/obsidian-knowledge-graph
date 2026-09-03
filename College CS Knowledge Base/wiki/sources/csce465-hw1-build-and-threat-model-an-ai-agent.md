---
title: "CSCE 465 HW1 — Build and Threat-Model an AI Agent"
type: source
tags: [csce465, homework, ai-agents, prompt-injection, openclaw, assignment]
sources: []
course: CSCE 465
updated: 2026-09-03
---

The Homework 1 briefing deck for [[CSCE 465]] (`raw/CSCE465_hw1-intro.pdf`, 16 PDF pages, two-up = 31 logical slides, dated 9/1/26, instructor [[Guofei Gu]]). **This is an assignment specification, not a lecture** — but roughly two thirds of it is genuine technical content, because the assignment teaches [[Prompt Injection]] before asking the student to demonstrate it. Those concepts are filed on their own pages; this page records the assignment's requirements, structure, and constraints.

> **Nothing in this knowledge base contains work product for this assignment.** The pages derived from this deck cover the concepts the deck teaches. The report, transcripts, diagram, and analysis are the student's to produce.

## Structure

| Slides | Part | Content |
|---|---|---|
| 2–5 | **Part 1** — AI agents and OpenClaw | What an agent is; the loop; OpenClaw architecture; how a request becomes an action |
| 6–9 | **Part 2** — Threat model & attack surface | 10 interfaces, 470 advisories; the kill chain; four trust boundaries that fail |
| 10–16 | **Part 3** — Prompt injection | Direct and indirect, with a worked trial of each; the structural difference; why encryption does not fix it |
| 17–22 | **Part 4** — Worked example | [[CVE-2024-5565]] (Vanna.AI) end to end, as the Task 4 template |
| 23–31 | **Part 4** *(sic)* — What HW1 asks | Grading, backends, gotchas, bonus, report requirements, rules, AI policy, resources |

## The Assignment

**120 points, individual**, plus an optional bonus worth up to 200.

| Task | Points | Deliverable |
|---|---|---|
| **1 — Build and verify the lab** | 40 | Install the agent stack, connect a model, run 3–5 benign agent tasks, submit reproducible evidence |
| **2 — Harmless local tool + web lab** | 20 | A fixed-command marker script, a `safe-marker` skill, a benign page and an adversarial page |
| **3 — Direct vs. indirect injection experiment** | 20 | Two trials, annotated transcripts, exec-policy evidence, a ≤600-word analysis |
| **4 — Threat model + one real advisory** | 35 | Data-flow diagram with assets / principals / boundaries / threats / controls, plus a 500–700-word advisory analysis |
| **Clarity, Git history, AI-use record** | 5 | — |

**Grading does not depend on which backend is chosen, or on the model obeying an injection.** The Task 3 deliverable is the annotated transcript that identifies the one turn and names its channel — not whether the model complied.

## Bonus Task

Optional. **100 points per accepted vulnerability, up to 200** (two). Deadline is **the last day of Fall classes — not the HW1 due date**, graded separately, and it does not affect the 120-point total.

Must be genuinely new: not in the project's published security advisories, any CVE, issue, or changelog, and not already reported by a classmate. **First substantive report wins.** Submit `hw1/bonus/<name>/` containing `advisory.md` (Task 4 structure), a working PoC in the VM, and `disclosure.md`. **Report to the instructor first — no public posting, no third-party testing.**

## Submission

Centers on `report.pdf` (or `report.md`), **written by the student in their own words**, containing setup notes, benign-task results, Task 3 (both trials, annotated transcripts, exec-policy, the four answers), Task 4 (diagram + labels + advisory analysis), and screenshots showing each task ran on the student's VM.

Also in the repo: `README.md`, `AI_USAGE.md`, the code (`bin/`, `skills/`, `web/`), `versions.txt`, `evidence/`. **No `requirements.txt`** — HW1 installs no Python packages.

**Late policy:** 20% off the earned score per day, no credit after 5 days. The bonus task is exempt.

## Rules — Everything Stays Inside the VM

Stated as hard constraints:

- Everything runs in the course VM and its local containers. **NAT networking only, never bridged.**
- Do not scan or touch campus networks, public IPs, another student's machine, or any system not built for this course.
- Only fake secrets, local mock services, harmless marker files. **No reverse shells, persistence, credential theft, cryptomining, public malware, or real command-and-control.**
- Do not connect personal messaging accounts, browser profiles, SSH keys, cloud credentials, or password stores to OpenClaw.
- Do not mount the host home directory or the Docker socket into an agent container.
- A task is never expected to affect anything outside the VM.

## AI Use Policy

AI tools are permitted for learning, brainstorming, debugging, and coding. But:

- **All answers and the final report must be written by the student** and reflect their own understanding. AI-assisted content must be carefully reviewed and independently verified.
- **Prompts and AI responses must be submitted** as a separate file (an exported conversation or log). Passwords, API keys, and personal information may be redacted.
- **`AI_USAGE.md` is required**, briefly explaining what and how AI was used and which parts were informed by it.
- The student remains responsible for understanding, verifying, and explaining everything submitted. Per the slide: the use of AI does not excuse incorrect results, unsupported claims, or code the student cannot explain.
- **A largely AI-generated report loses credit** under "Clarity, Git history, and AI-use record" and **may be treated as an integrity issue.**

## Concepts Taught by This Deck

- [[AI Agent Security]] — the agent loop; why LLM output driving execution is a new class of problem; the four trust boundaries that fail
- [[OpenClaw]] — architecture, the 10-interface attack surface, the kill chain, the `ask=off` default, and the backend configuration gotchas
- [[Prompt Injection]] — direct vs. indirect as a *channel* distinction; why encryption does not help; the required/helpful/irrelevant taxonomy
- [[CVE-2024-5565]] — the Vanna.AI advisory worked end to end as the Task 4 template

## Resources Named

- **Textbook:** van Oorschot, *Computer Security and the Internet*, 2nd ed. — **Ch. 1 and Ch. 9**
- OpenClaw docs: install, Ollama provider, skills, gateway sandboxing
- The instructor's paper: *A Security Analysis of the OpenClaw AI Agent Framework* (Suwansathit, Zhang & Gu, 2026) — the attack-surface taxonomy and the advisory list for Task 4
- Ubuntu 24.04, Docker, Node, Ollama, Suricata, AppArmor
- **TA office hours: Thursdays 2–4 PM**, and Piazza

## Deck Inconsistencies Noted

Two, both minor, both recorded rather than silently corrected:

1. **Two "Part 4" sections.** Slide 17 opens "PART 4 — Worked example" and slide 23 opens "PART 4 — What Homework 1 asks of you." There is no Part 5; the second is presumably meant to be one.
2. **"The kill chain — 6 stages"** is the slide title, but three numbered phases are shown. Likely six stages grouped into three phases, with the finer breakdown in the paper. Recorded on [[OpenClaw]].

Separately, Lecture 1 gave the TA office hour as **TBD**; this deck fixes it at **Thursdays 2–4 PM**. The [[CSCE 465]] course page now carries the specific time.

## Extraction Note

Text extracted with PyMuPDF. **No image-only slides** — all 16 pages carry substantive text. Slide 4 (OpenClaw architecture) and slide 7 (attack-surface advisory distribution) have accompanying figures whose numeric content is in the text; the precise per-interface breakdown beyond the four largest categories exists only in the pie chart and is **not** recoverable.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Prompt Injection]]
- [[AI Agent Security]]
- [[OpenClaw]]
- [[CVE-2024-5565]]
- [[CSCE 465 Lecture 2 — Security Overview]]
