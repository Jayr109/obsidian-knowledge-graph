---
title: "Skolemization"
type: concept
tags: [csce420, skolemization, skolem-function, quantifiers, standard-form]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

**Skolemization** eliminates existential quantifiers by replacing the bound variable with a constant or a function of the universally quantified variables to its left. It is step 3 of the conversion to standard form, and the step that makes [[Resolution]] possible — resolution needs clauses with only universal variables.

## The Rule

Assume the formula is in [[Prenex Normal Form]]: $F = Q_1x_1 Q_2x_2 \dots Q_nx_n (M)$.

For each existential $\exists x_r$:

- **If universal quantifiers appear to its left**, delete $\exists x_r$ and replace every $x_r$ by $f(x_{s_1}, \dots, x_{s_m})$, where $x_{s_1}, \dots, x_{s_m}$ are **all the universally quantified variables to the left of $x_r$**, and $f$ is a new function symbol — a **Skolem function** — not appearing in $F$.
- **If no $\forall$ appears to its left**, remove $\exists$ and replace the variable with a new constant $a$ — a **Skolem constant**.

> A constant is just a function with no arguments, so the two cases are one rule.

## Worked Example

$$\exists x \forall y \forall z \exists u \forall v \exists w\; P(x,y,z,u,v,w)$$

- $\exists x$ — nothing universal to its left → Skolem constant $a$
- $\exists u$ — $y, z$ to its left → $f(y,z)$
- $\exists w$ — $y, z, v$ to its left → $g(y,z,v)$

Result:

$$\forall y \forall z \forall v\; P(a,\, y,\, z,\, f(y,z),\, v,\, g(y,z,v))$$

## Why Quantifier Order Changes the Answer

The clearest demonstration, and a standard exam item:

| Formula | Skolemized | Meaning |
|---|---|---|
| $\exists x \forall y\; \text{Loves}(x,y)$ | $\forall y\; \text{Loves}(a, y)$ | **One** particular lover $a$ loves everyone |
| $\forall y \exists x\; \text{Loves}(x,y)$ | $\forall y\; \text{Loves}(f(y), y)$ | Everyone is loved by **someone, possibly different** |

The **constant** $a$ says the choice is fixed; the **function** $f(y)$ says the choice *depends on* $y$. This is exactly why $\forall x \exists y \neq \exists y \forall x$ — see [[First-Order Logic]].

## The Intuition

Why is replacing "there exists" with a name legitimate? The lecture motivates it with a proof done by hand first: given $\exists x (B(x) \land D(x))$, one argues *"there must be an $x$ in the domain, which we shall arbitrarily call $a$, such that $B(a) \land D(a)$ is true."* Skolemization mechanizes that move — naming the witness.

Skolemization does **not** preserve logical equivalence; it preserves **satisfiability**, which is all refutation-based proving requires.

## See Also

- [[Prenex Normal Form]]
- [[First-Order Logic]]
- [[Resolution]]
- [[Unification]]
- [[CSCE 420]]
