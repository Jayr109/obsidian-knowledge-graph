---
title: "Propositional Logic"
type: concept
tags: [csce420, propositional-logic, wff, semantics, validity, satisfiability]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

Propositional logic is the simplest formal language in the [[Knowledge Base Systems|logic hierarchy]]: it commits ontologically only to **facts**, with no objects or relations. Its limits are what motivate [[First-Order Logic]].

## Syntax: Well-Formed Formulas

Components of a wff:

- **Propositional symbols (atoms)**: $P, Q, R$
- **Parentheses**: ( )
- **Connectives**: $\neg, \land, \lor, \rightarrow, \leftrightarrow$
- **Constants**: True, False

The grammar:

```
wff => atom | constant
wff => (¬ wff)
wff => (wff ∨ wff) | (wff ∧ wff) | (wff → wff) | (wff ↔ wff)
```

**Operator precedence**, decreasing: $\neg$ ; then $\land, \lor$ ; then $\rightarrow, \leftrightarrow$. So

$$\neg P \rightarrow Q \lor \neg R \land S \quad\text{parses as}\quad (\neg P) \rightarrow ((Q \lor (\neg R)) \land S)$$

## Semantics

- Atoms take True or False values.
- An **interpretation** assigns specific truth values to the atoms.
- A formula with $n$ atoms has $2^n$ possible truth assignments.
- A formula is **true under an interpretation** iff it evaluates to True under that assignment.

The three key classifications:

| Term | Definition |
|---|---|
| **Valid** | True under **all** interpretations |
| **Inconsistent (unsatisfiable)** | False under **all** interpretations |
| **Satisfiable** | True under at least one interpretation |

**The duality that drives theorem proving**: a formula $G$ is valid **iff** $\neg G$ is inconsistent. This is why [[Resolution]] proves things by refutation — it is easier to derive a contradiction than to check all interpretations.

## Models and Equivalence

- If $F$ is True under interpretation $I$, we say **$I$ satisfies $F$**, and **$I$ is a model for $F$**.
- If $F$ is False under $I$, we say **$I$ falsifies $F$**.
- $F$ and $G$ are **equivalent** iff they have the same truth values under every interpretation.
- A satisfiable $F$ can have many models — at least one.

> **Caution from the slides**: do not confuse a formula named $F$ with the constant **False**.

## The Basic Laws

| Law | Form |
|---|---|
| Commutative | $F \lor G = G \lor F$; $F \land G = G \land F$ |
| Associative | $(F \lor G) \lor H = F \lor (G \lor H)$ |
| Distributive | $F \lor (G \land H) = (F \lor G) \land (F \lor H)$ |
| Identity | $F \lor \text{False} = F$; $F \land \text{True} = F$ |
| Universal bound | $F \lor \text{True} = \text{True}$; $F \land \text{False} = \text{False}$ |
| Negation | $F \lor \neg F = \text{True}$; $F \land \neg F = \text{False}$ |
| Double negation | $\neg(\neg F) = F$ |
| **De Morgan** | $\neg(F \lor G) = \neg F \land \neg G$; $\neg(F \land G) = \neg F \lor \neg G$ |
| Equivalence | $F \leftrightarrow G = (F \rightarrow G) \land (G \rightarrow F)$ |
| **Implication** | $F \rightarrow G = \neg F \lor G$ |
| Idempotent | $F \land F = F$; $F \lor F = F$ |
| Absorption | $P \land (P \lor Q) = P$; $P \lor (P \land Q) = P$ |

The implication and De Morgan laws do the heavy lifting in [[Normal Forms|CNF conversion]].

## The Limitation

The lecture's motivating failure:

- $P$: All men are mortal
- $Q$: Socrates is a man
- $R$: Socrates is mortal

**Can you prove $(P \land Q) \rightarrow R$ in propositional logic?** No. The three propositions are atomic and unrelated — nothing inside $P$ connects "men" to "Socrates". Propositional logic cannot reason with **general rules**, which is exactly what [[First-Order Logic]] adds.

## See Also

- [[Normal Forms]]
- [[Inference Rules]]
- [[Logical Consequence]]
- [[First-Order Logic]]
- [[Knowledge Base Systems]]
- [[CSCE 420]]
