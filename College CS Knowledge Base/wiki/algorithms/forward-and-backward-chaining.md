---
title: "Forward and Backward Chaining"
type: algorithm
tags: [csce420, forward-chaining, backward-chaining, theorem-proving, horn-clauses]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

Given a set of facts (ground literals) and rules, a theorem can be proved in three ways: **forward chaining**, **backward chaining**, or [[Resolution]]. The first two are the intuitive directions; resolution is the mechanizable one.

## The Three Approaches

| Method | Direction | Description |
|---|---|---|
| **Forward chaining** | Facts → goal | Use known facts and rules to deduce new facts; stop when the desired theorem appears |
| **Backward chaining** | Goal → facts | Work backward from the theorem, finding rules that could deduce it, then try to deduce those rules' premises |
| **[[Resolution]]** | Refutation | Add the negated theorem and derive False |

## The Worked Example

Given as true:

$$A \quad (1) \qquad B \quad (2) \qquad D \quad (3) \qquad A \land B \rightarrow C \quad (4) \qquad C \land D \rightarrow E \quad (5)$$

Prove $E$.

**Forward chaining.** $A$ and $B$ are true (1, 2), so by (4) $C$ is true — call this (6). From $D$ (3), $C$ (6), and (5), conclude $E$ is true.

**Backward chaining.** Find a rule concluding $E$: rule (5). For it to give $E$, both $C$ and $D$ must hold. $D$ is given (3), so only $C$ remains. Find a rule concluding $C$: rule (4). Repeat until all premises are established.

## Which to Use

**Backward chaining is ideal for [[Horn Clauses|Horn Normal Form]]** — and the reason is structural. A Horn clause is an implication with exactly *one* literal as its conclusion, so "find a rule that concludes $X$" has an unambiguous answer. With general clauses that step is a search in itself.

The broader tradeoff:

- **Forward** is *data-driven* — it derives everything derivable, which may be far more than the goal requires.
- **Backward** is *goal-driven* — it only explores what could bear on the question, but may re-derive the same subgoal repeatedly.

Backward chaining is the strategy [[Prolog]] implements.

## See Also

- [[Horn Clauses]]
- [[Resolution]]
- [[Prolog]]
- [[Logical Consequence]]
- [[Inference Rules]]
- [[CSCE 420]]
