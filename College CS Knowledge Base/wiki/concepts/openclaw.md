---
title: "OpenClaw"
type: concept
tags: [csce465, security, ai-agents, openclaw, attack-surface]
sources: [csce465-hw1-build-and-threat-model-an-ai-agent]
course: CSCE 465
updated: 2026-09-03
---

OpenClaw is the AI agent framework [[CSCE 465]] uses as the platform for all four homework assignments. The course's interest in it is that it *exposes the full stack from external input to host execution* — it is not a toy, so its trust boundaries are the real ones. Everything on this page is as presented in the HW1 briefing and the instructor's own paper; claims about the project's scale are the deck's, recorded as such.

**Per the assignment deck:** the first open-source autonomous AI agent runtime connecting LLMs to over 15 execution surfaces, and (as stated on the slide) the fastest-growing open-source project in GitHub history at 384k stars within months of launch.

## Architecture

Six core components:

- **Channel Adapter** — external input arrives here
- **Gateway Control Plane**
- **Agent Runtime & Memory System**
- **Plugins & Skills**
- **External/Local LLM Providers**
- **Privileged Local Execution Process**

## How a Request Becomes an Action

The [[AI Agent Security|agent loop]] as OpenClaw implements it: context assembly → model call → tool dispatch through the gateway, where the **exec policy** decides whether to run → execution.

The detail that matters for the homework: on the default `coding` profile the policy is **`ask=off`** — the call runs with **no human approval**. After onboarding the observed posture is `security=full, ask=off`, and the audit trail shows `tool.action.started:exec -> finished:exec` with no approval record. The default is not "ask the operator."

## Attack Surface — Ten Interfaces

From the instructor's paper, *A Security Analysis of the OpenClaw AI Agent Framework* (Suwansathit, Zhang & Gu, 2026), across **470 advisories**:

| # | Interface | # | Interface |
|---|---|---|---|
| 1 | Channel Input | 6 | Exec Policy Engine |
| 2 | Plugin & Skill Distribution | 7 | Container Boundary |
| 3 | Agent Context Window | 8 | Host OS Interface |
| 4 | Gateway WebSocket | 9 | LLM Provider Interface |
| 5 | Tool Dispatch | 10 | Inter-Agent Communication |

**By advisory volume:** Gateway 26%, Channel Input 25%, Exec Policy 16%, Tool Dispatch 15% — together 82% of the total, all clustered at the boundary where external input becomes an internal decision.

**The dominant pattern**, and the paper's central finding: *per-layer trust checks, no unified policy — cross-layer attacks resist local fixes.* Each layer validates against its own assumptions; no layer owns the end-to-end question. A fix applied at any single layer leaves the composition unchanged. This is [[Security Policy and Mechanism|policy composition]] failing exactly as Lecture 2 warned it does.

## The Kill Chain

Three phases:

**01 — Ingress & Reasoning (Initial Access & Context Manipulation).** Malicious inputs enter via channels or webhooks. Attackers use context manipulation to alter LLM reasoning — *the stage that distinguishes AI attacks from classic ones*.

**02 — Active Exploitation (Execution & Escalation).** The compromised agent executes unauthorized tool calls, steals active session keys, and escalates privileges to rewrite safety policy states.

**03 — Systemic Impact (Host & Data Compromise).** Host remote code execution, data exfiltration, system persistence, browser compromise.

Note the escalation in phase 02 targets *the policy state itself* — the agent rewrites the rules that were supposed to constrain it. Any control that lives inside the blast radius of the thing it constrains is not a control.

> **Deck inconsistency:** the slide is titled "The kill chain — 6 stages" but presents three numbered phases. Most likely six stages grouped into three, with the finer breakdown in the paper rather than the slide. Recorded rather than guessed at.

## Practical Notes from the Briefing

Configuration gotchas the assignment calls out, kept because they are the difference between a working lab and an apparently broken one:

- **Local backend** (Ollama + `qwen3.5:4b`): free and offline, ~3–5 min per turn on CPU, needs the full 8 GB. **Requires `OLLAMA_CONTEXT_LENGTH=16384` and `num_ctx: 16384`** — Ollama's 4096 default silently truncates the agent's ~13k-token prompt, and the model then makes **no tool calls at all**, which looks like a broken setup rather than a truncation. Named as the #1 cause of "my agent does nothing."
- **API backend** (TAMUS AI, `protected.gpt-4o`): seconds per turn, $5/day credit. **Requires the provided `tamu-shim.mjs` proxy** — without it OpenClaw sends `content:null` on tool-call turns and the TAMUS proxy rejects it with HTTP 422. The smoke test passes without the shim, so the failure only surfaces later, during the injection experiment.
- `web_fetch` **blocks localhost** — for the indirect-injection trial the page must be fetched manually and pasted in as clearly delimited external content.
- On a 6 GB VM use `qwen3.5:2b` with `num_ctx: 8192`.
- If `openclaw onboard` is interrupted, wait ~5 minutes before retrying — a migration lock clears itself.

## See Also

- [[AI Agent Security]]
- [[Prompt Injection]]
- [[CVE-2024-5565]]
- [[Security Policy and Mechanism]]
- [[Guofei Gu]]
- [[CSCE 465]]
