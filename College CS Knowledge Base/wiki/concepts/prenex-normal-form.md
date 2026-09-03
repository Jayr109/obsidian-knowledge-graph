---
title: "Prenex Normal Form"
type: concept
tags: [csce420, prenex, quantifiers, standard-form, first-order-logic]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

A first-order formula is in **Prenex Normal Form** when all quantifiers are pulled to the front:

$$\underbrace{Q_1x_1\, Q_2x_2 \dots Q_nx_n}_{\text{prefix}}\; \underbrace{(M)}_{\text{matrix}}$$

where each $Q_i$ is $\forall$ or $\exists$, and the **matrix** $M$ contains no quantifiers. It is step 1 of the three-step conversion to standard form required by [[Resolution]].

## The Three-Step Standard Form

1. **Prenex Normal Form** — move all quantifiers to the front
2. **Convert the matrix to [[Normal Forms|CNF]]** — exactly as in propositional logic
3. **[[Skolemization]]** — eliminate existential quantifiers

Result: $\forall x_1 \forall x_2 \dots \forall x_n (\text{CNF})$ — a set of clauses in which **every variable is universally quantified**, so the quantifiers can be dropped from the notation entirely.

## Quantifier Equivalences

The rules used to migrate quantifiers outward (with $Q$ either $\forall$ or $\exists$):

| Equivalence | Note |
|---|---|
| $(Qx\,F(x)) \lor G = Qx\,(F(x) \lor G)$ | valid when $G$ has no free $x$ |
| $(Qx\,F(x)) \land G = Qx\,(F(x) \land G)$ | same condition |
| $\neg(\forall x\,F(x)) = \exists x\,(\neg F(x))$ | **negation flips the quantifier** |
| $\neg(\exists x\,F(x)) = \forall x\,(\neg F(x))$ | |
| $(\forall x\,F(x)) \land (\forall x\,G(x)) = \forall x\,(F(x) \land G(x))$ | $\forall$ distributes over $\land$ |
| $(\exists x\,F(x)) \lor (\exists x\,G(x)) = \exists x\,(F(x) \lor G(x))$ | $\exists$ distributes over $\lor$ |
| $(Q_1x\,F(x)) \lor (Q_2x\,H(x)) = Q_1x\,Q_2z\,(F(x) \lor H(z))$ | **rename to avoid capture** |

Two traps. First, $\forall$ distributes over $\land$ but **not** over $\lor$; $\exists$ over $\lor$ but **not** over $\land$. Second, when both sides bind the same variable name, one must be **renamed** ($x \to z$) before merging — otherwise the variables are wrongly identified.

## Worked Example

Convert $(\forall x\,P(x)) \rightarrow (\exists y\,Q(y))$:

$$= \neg(\forall x\,P(x)) \lor (\exists y\,Q(y)) = (\exists x\,\neg P(x)) \lor (\exists y\,Q(y)) = \exists x\,\exists y\,(\neg P(x) \lor Q(y))$$

Note the first step: eliminating $\rightarrow$ places the antecedent under a negation, which **flips $\forall$ into $\exists$**.

## See Also

- [[Skolemization]]
- [[First-Order Logic]]
- [[Normal Forms]]
- [[Resolution]]
- [[CSCE 420]]
