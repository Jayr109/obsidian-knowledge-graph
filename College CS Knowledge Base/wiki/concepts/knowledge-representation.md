---
title: "Knowledge Representation"
type: concept
tags: [csce420, knowledge-representation, logic, frames, representation-hypothesis]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

Traditional AI recognizes **two classes of representation**: *logic*, based on first-order predicate calculus, and *frames*, based on networks of nodes representing objects or concepts with labeled arcs representing relations. The lecture's framing is that these are **competitive but complementary** — neither subsumes the other.

## The Representation Hypothesis

A central tenet of AI: intelligent behavior is based on

- **representation** of input and output data as symbols, and
- **reasoning** by processing symbol structures, producing new symbol structures.

The problem then reduces to a design question: *what should the representations and the reasoning process be?* This is the hypothesis that [[Symbolic AI]] rests on.

## Logic vs. Frames

| | Strengths | Weaknesses |
|---|---|---|
| **Logic** (first-order) | Logical power; rigorous mathematical foundation | Slow (search); rigidity (strictly T/F) |
| **Frames** | Supports **defaults** — data is seldom complete; procedural attachment | Weak logical power |

*Procedural attachment* means attaching code to slots that fires on events — pullers (if needed), pushers (if added), and hooks for if-referenced, if-deleted, if-changed.

The trade is clean: logic buys rigor at the cost of speed and brittleness; frames buy defaults and flexibility at the cost of inferential power. Rigidity matters because real knowledge is full of exceptions that a strict T/F system cannot express gracefully.

## Alternatives to the Representation Hypothesis

The lecture explicitly lists positions that reject the symbolic premise:

- **Analog information** — continuous rather than discrete values
- **Special-purpose hardware** — domain-specific functions such as vision
- **Neural networks** — *subsymbolic*, distributed (vector) representations

That third item is the direct ancestor of [[Deep Learning]], and naming it here frames the symbolic/subsymbolic split that [[Neurosymbolic AI]] later tries to heal.

## See Also

- [[Knowledge Base Systems]]
- [[Propositional Logic]]
- [[First-Order Logic]]
- [[Symbolic AI]]
- [[Neurosymbolic AI]]
- [[CSCE 420]]
