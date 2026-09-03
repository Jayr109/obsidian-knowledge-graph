---
title: "Prompt Injection"
type: concept
tags: [csce465, security, ai-agents, prompt-injection, llm]
sources: [csce465-hw1-build-and-threat-model-an-ai-agent]
course: CSCE 465
updated: 2026-09-03
---

Prompt injection is the attack that arises when text an attacker controls reaches a language model's context and is acted on as an instruction. It is the central subject of [[CSCE 465]]'s first homework, and structurally it is a **provenance** failure, not a parsing failure: the model receives instructions and data concatenated into one undifferentiated string, and nothing in that string records where each part came from.

The one-sentence version from the assignment: *"the context window is the program"* — and it has **no type distinction between content and commands**.

## Direct vs. Indirect

The distinction is about the **channel the instruction rides**, not the words it contains. The homework's Task 3 runs both trials with the same agent, the same tool, and the same sentence — "run the safe marker" — and the only variable is origin.

| | Direct | Indirect |
|---|---|---|
| Where the instruction sits | A `role:user` turn the operator typed | Inside a retrieved page, file, or API response |
| Operator's own message | "Use the safe-marker skill…" | "Summarize this page." |
| Channel | **Control** channel | **Data** channel |
| Trust status | Authenticated origin, one hop | Untrusted |
| Who intended the action | The operator | The attacker |

**Direct injection** places attacker-controlled text straight into the prompt. It is "direct" because the instruction arrives as a turn a principal actually typed — the origin is authenticated even if the intent is hostile.

**Indirect injection** plants the instruction in data the agent will *later* retrieve — a web page, a file, an API response, an email. The operator asks only for a summary; the page contains the command. The operator never said it and may never see it.

## The Structural Point

> Untrusted data becomes a possible instruction the moment retrieved bytes are concatenated into the prompt with no trust label.

That sentence is the whole concept. The attack does not require a bug, a bypass, or a malformed input — it requires only that the system flatten two different trust levels into one buffer. Every downstream trust decision then inherits from that step.

The assignment is explicit that the Task 3 deliverable is **the annotated transcript that identifies the one turn and names its channel — not whether the model obeyed.** Whether a particular model takes the bait is a property of that model on that day; whether the architecture can distinguish the channels is the security property.

## Why Encryption Does Not Fix It

This is the cleanest illustration in the course of the [[CIA Triad|confidentiality vs. authorization]] distinction, and it directly extends [[Security Attack Taxonomy|Lecture 2's argument]] that cryptography does not guarantee confidentiality:

- Encryption protects data **in transit** — against eavesdropping, tampering, and replay by an **on-path** attacker.
- Indirect injection is **not on-path**. The payload is authored into content the agent is *legitimately asked to read*.
- A perfectly confidential, authenticated pipe still delivers the poisoned page **intact** — arguably it delivers it more reliably.

> *"Did this arrive unmodified?"* is the wrong question. *"Should the agent act on it?"* is an **authorization** problem.

Integrity and authentication of the *channel* say nothing about the authority of the *content*. This is the same category error as trusting a signed binary to be benign because the signature verified.

## Observed Behavior in the Homework's Own Trials

Worth recording because it shows what the guardrails actually did:

- **Direct trial:** the model called the skill, the exec policy ran the command with `ask=off`, `marker.txt` was created, and the audit log shows `tool.action.started:exec -> finished:exec` with **no approval record**. Nothing prompted the operator.
- **Indirect trial:** the planted block steered the 4B model toward hunting for the skill (which it would not do for a plain report), but it **stalled before exec**. The assignment is careful about why: it was stopped by *the skill's own guardrail plus a weak model* — **no OpenClaw policy fired.** The architecture did not catch it; the model was simply not capable enough to finish.

That distinction — stopped by luck versus stopped by design — is the point of running both trials.

## Is Prompt Injection Required, Helpful, or Irrelevant?

Task 4 asks this of a real advisory, and the three categories are worth keeping as an analytic tool:

| Category | Meaning | Example from the assignment |
|---|---|---|
| **Required** | The sink is reachable *only* by steering the model | [[CVE-2024-5565]] — no other attacker-controlled route to `exec()` |
| **Helpful, not required** | Injection is a realistic delivery vector, but an operator could trigger it too | An exec-allowlist parser bypass |
| **Irrelevant** | No model or context window in the loop at all | An unauthenticated admin endpoint; a channel display-name spoof |

The nuance the assignment insists on: a vulnerability can have a classic root weakness whose fix belongs on the sink side, while still not existing *from an external attacker's view* without prompt injection.

## Defenses, as the Assignment Frames Them

The durable fix is never "filter the bad words." It is to **constrain the tool so that a permitted call cannot be repurposed** — have the model emit a restricted, validated structure that a trusted component interprets, rather than executable text. That is [[Security Design Principles|economy of mechanism and least privilege]] applied at the model boundary, and it is the same move as parameterized queries against SQL injection.

## See Also

- [[AI Agent Security]]
- [[OpenClaw]]
- [[CVE-2024-5565]]
- [[Security Attack Taxonomy]]
- [[Security Design Principles]]
- [[CIA Triad]]
- [[CSCE 465]]
