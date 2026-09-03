---
title: "Answer Extraction"
type: concept
tags: [csce420, question-answering, answer-predicate, resolution, applications]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

[[Resolution]] natively answers only **yes/no** questions — it derives False or it does not. **Answer extraction** recovers *which object* satisfied the query, turning a theorem prover into a question-answering system.

## The Problem

Given a database of facts and axioms, ask *"Who is a grandparent of Harmonia?"*:

$$\exists x\, \text{Grandparent}(x, \text{Harmonia})$$

Negated for refutation:

$$\neg\exists x\,\text{Grandparent}(x,\text{Harmonia}) = \forall x\,\neg \text{Grandparent}(x, \text{Harmonia})$$

Resolution derives False, which establishes *"there **is** a grandparent of Harmonia."* True, but it does not say **who** — and who is the actual question.

## The Insight

> The binding which $x$ ultimately receives **is** the desired answer.

Running the proof, one substitution applied along the way to $\neg\text{Grandparent}(x, \text{Harmonia})$ is $\{x/\text{Hera}\}$ — so Hera is an answer. The information was always present in the [[Substitution|substitutions]]; it was simply discarded when the proof terminated.

## The Answer Predicate

To capture it mechanically, append a special literal to the negated goal:

$$\neg \text{Grandparent}(x, \text{Harmonia}) \lor \text{Answer}(x)$$

The **Answer predicate** has two engineered properties:

- It **does not resolve with anything** — it is inert, and merely rides along accumulating variable bindings.
- The prover **treats a clause consisting only of Answer as False** — so the proof still terminates normally.

Resolution then ends not at False but at $\text{Answer}(\text{Hera})$, which carries the answer in its argument.

## The Worked Domain

```
∀x∀y∀z ((Parent(x,z) ∧ Parent(z,y)) → Grandparent(x,y))
∀x∀y (Mother(x,y) → Parent(x,y))
∀x∀y (Father(x,y) → Parent(x,y))
Father(Zeus, Ares)
Mother(Hera, Ares)
Father(Ares, Harmonia)
```

## Why It Matters

This is the bridge from theorem proving to a **practical application**. It is also the mechanism behind [[Prolog]]: a Prolog query returns variable bindings, not merely success.

## See Also

- [[Resolution]]
- [[Substitution]]
- [[Prolog]]
- [[Resolution Strategies]]
- [[CSCE 420]]
