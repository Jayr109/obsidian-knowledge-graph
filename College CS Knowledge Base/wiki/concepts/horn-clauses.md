---
title: "Horn Clauses"
type: concept
tags: [csce420, horn-clauses, backward-chaining, prolog, inference]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

A **Horn clause** is a clause containing **at most one positive literal**. Horn Normal Form is a conjunction of Horn clauses. The restriction buys computational tractability — inference over Horn clauses is markedly cheaper than over general [[Normal Forms|CNF]].

## Definition and Examples

Horn clauses: $F \lor \neg G \lor \neg H$ and $\neg F \lor G$ — each has exactly one unnegated literal.

A conjunction such as $(F \lor \neg G \lor \neg H) \land (\neg F \lor G)$ is in Horn Normal Form.

## The Implication Reading

This is the point of the form. Using $F \rightarrow G = \neg F \lor G$ in reverse:

$$F \lor \neg G \lor \neg H \quad\equiv\quad (G \land H) \rightarrow F$$

So the example above reads as $((G \land H) \rightarrow F) \land (F \rightarrow G)$.

**Horn clauses are exactly the implications whose conclusion is a single literal.** The at-most-one-positive-literal condition is the syntactic shadow of "one thing on the right-hand side of the arrow."

## Why It Matters

- **Easier inference** — computationally less intensive than other normal forms
- **Suited to backward chaining** — see [[Forward and Backward Chaining]]. Working backward from a goal means finding a rule that concludes it; with a single conclusion per rule, that search is unambiguous.
- **Restrictive** — *not all formulas can be represented in Horn Normal Form*. A clause with two positive literals, such as $P \lor Q$ ("either P or Q"), has no Horn equivalent, so genuine disjunctive conclusions are outside the fragment.

That tradeoff — tractability bought with expressiveness — is why [[Prolog]] is built on Horn clauses rather than full first-order logic.

## See Also

- [[Normal Forms]]
- [[Forward and Backward Chaining]]
- [[Prolog]]
- [[Resolution]]
- [[CSCE 420]]
