---
title: "AI Agent Security"
type: concept
tags: [csce465, security, ai-agents, llm, trust-boundaries]
sources: [csce465-hw1-build-and-threat-model-an-ai-agent]
course: CSCE 465
updated: 2026-09-03
---

An **AI agent** is a loop that lets a language model drive real actions. [[CSCE 465]] treats it as a distinct class of security problem, and the reason is compact: **LLM reasoning + real execution surfaces**. The model's output no longer produces text for a human to evaluate — it directly drives actions on the host.

> A wrong or manipulated token is no longer a bad sentence — it can be a command that runs.

## The Loop

1. **Context assembly** — the system prompt, the user's message, and any fetched page, file, or tool output are concatenated into one prompt.
2. **Model call** — the LLM returns text that may contain a tool call.
3. **Tool dispatch** — the runtime routes the call; an exec policy decides whether to run it.
4. **Execution** — the tool runs, and its result is fed back into step 1.

Tools are real: shell commands, file read/write, HTTP fetch, browser control, Docker.

**Every trust decision inherits from step 1**, where data and instructions are mixed. That is the sentence the whole unit turns on — the vulnerability is introduced by concatenation, before the model is ever consulted, and every later check is operating on already-flattened input.

## Four Trust Boundaries That Do Not Hold

The assignment names these explicitly, and each is an assumption a conventional system would never make:

- **LLM output is trusted.** The runtime executes tool calls the model emits without questioning intent. There is no notion of *why* a call was proposed.
- **Skill content equals operator trust.** A skill downloaded from a registry enters the context as if the operator had written it themselves. Third-party content inherits first-party authority.
- **Data paths are treated as information, not instructions.** Web pages, log headers, filenames, and channel metadata all land in the prompt **unlabeled**.
- **The context window is the program** — and it has **no type distinction between content and commands.**

The last one subsumes the others. In every other part of this course, the fix for confusing data with code is a type boundary: parameterized queries, `execve` argument arrays, structured serialization. The context window has none, which is why [[Prompt Injection]] is not a bug to be patched but a property of the architecture.

## Why This Is Not a Classic Attack

The stage that distinguishes AI attacks from classic ones is **context manipulation** — altering the *reasoning* rather than corrupting memory or bypassing a check. There is no malformed input, no parser confusion, no privilege escalation primitive. The input is well-formed and the system behaves exactly as designed; the attacker has simply supplied a premise.

This maps onto [[Security Attack Taxonomy|the four attack families]] awkwardly, which is itself informative. An indirect injection is closest to **fabrication** — the attacker causes an action to be attributed to the operator — but the mechanism is neither identity spoofing nor message tampering. The instruction is delivered honestly, through a channel working correctly, and is misinterpreted as authoritative because the architecture has no way to record that it was not.

## Where It Sits in the Course

This is the material behind the [[Security Threat Landscape|AI/agentic attacks]] entry from Lecture 1, and it is why [[CSCE 465]] ends on AI agent security rather than treating it as an aside. It is also the platform for all four homework assignments — see [[OpenClaw]].

The connection back to first principles: the durable defenses are the old ones. Constrain the tool ([[Security Design Principles|least privilege]]), check every access rather than trusting a prior decision (complete mediation), and default to refusing (fail-safe defaults). What is new is the surface, not the discipline.

## See Also

- [[Prompt Injection]]
- [[OpenClaw]]
- [[CVE-2024-5565]]
- [[Security Design Principles]]
- [[Security Attack Taxonomy]]
- [[Security Threat Landscape]]
- [[CSCE 465]]
