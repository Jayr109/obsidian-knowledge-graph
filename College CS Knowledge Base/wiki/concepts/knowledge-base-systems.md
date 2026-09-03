---
title: "Knowledge Base Systems"
type: concept
tags: [csce420, knowledge-base, inference-engine, soundness, completeness, declarative]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

A knowledge-based system splits into **domain-independent algorithms** — the *inference engine* — and **domain-specific content** — the *knowledge base*. That separation is the architectural point: one reasoning engine serves many domains.

## The Two Halves

| Component | Role | Question it answers |
|---|---|---|
| **Knowledge base (KB)** | A set of sentences in a formal language: facts and rules | How do we *represent* knowledge? |
| **Inference engine** | Generates new sentences from old ones in the KB | How do we *derive* new knowledge? |

**The KB is declarative**: it says *what* we want, not *how* we want it done. It is not procedural. This is what allows the same KB to be queried in ways its author never anticipated.

## Logic as the Representational Language

Logic consists of:

- **Syntax** — sentence structure
- **Semantics** — how sentences relate to the real world (truth values)
- **Interpretation** — the fact to which a sentence refers, i.e. a T/F assignment
- **Inference** — deriving new sentences from old ones

## Soundness and Completeness

The two properties every inference procedure is judged on:

| Property | Definition | Slogan |
|---|---|---|
| **Sound** | No false sentences can be derived from the KB | Everything proved is true |
| **Complete** | Can derive all true conclusions from a set of premises | Everything true can be proved |

Both are needed and they are independent. An unsound engine invents falsehoods; an incomplete one silently misses valid conclusions. [[Resolution]] is proved to be both for first-order logic.

## Types of Logic

Two axes: **ontological** — what exists in the world — and **epistemological** — what we can know about it.

| Language | Ontological commitment | Epistemological commitment |
|---|---|---|
| [[Propositional Logic]] | facts | T / F / unknown |
| [[First-Order Logic]] | facts, objects, relations | T / F / unknown |
| Temporal logic | facts, objects, relations, times | T / F / unknown |
| Probability theory | facts | degree of belief 0..1 |
| Fuzzy logic | degree of truth | degree of belief 0..1 |

Note the difference between the last two rows, which is easy to blur: **probability theory keeps facts crisp and makes *belief* graded; fuzzy logic makes *truth itself* graded.** First-order logic is also called predicate calculus.

Adding to the ontological column buys expressiveness — that is the whole argument for moving from propositional to first-order logic. Adding to the epistemological column buys the ability to handle uncertainty, which is what [[Bayesian Networks]] does.

## See Also

- [[Knowledge Representation]]
- [[Propositional Logic]]
- [[First-Order Logic]]
- [[Logical Inference]]
- [[Bayesian Networks]]
- [[CSCE 420]]
