---
title: "Substitution"
type: concept
tags: [csce420, substitution, unification, composition, instance]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

A **substitution** is a finite set $\{v_1/t_1, \dots, v_n/t_n\}$ where each $v_i$ is a variable, each $t_i$ is a term (constant, variable, or function of terms), and **no two $v_i$ are identical**. The notation $v_i/t_i$ means *$v_i$ is replaced with $t_i$*.

The empty substitution is $\epsilon = \{\}$.

**Why it matters**: substitution is what makes two clauses with different variable names compatible so they can be resolved. It is the machinery underneath [[Unification]].

## Applying a Substitution

Given $\theta = \{v_1/t_1, \dots, v_n/t_n\}$ and an expression $E$, then $E\theta$ is obtained by replacing **simultaneously** each occurrence of $v_i$ in $E$ by $t_i$. $E\theta$ is called an **instance** of $E$. Russell & Norvig write this $\text{SUBST}(\theta, E)$.

Simultaneity matters: $\{x/y,\, y/a\}$ applied to $P(x,y)$ gives $P(y,a)$, not $P(a,a)$.

### Examples

| $\theta$ | $E$ | $E\theta$ |
|---|---|---|
| $\{x/a,\, y/f(b),\, z/c\}$ | $P(x,y,z)$ | $P(a, f(b), c)$ |
| $\{x/f(z),\, y/z\}$ | $P(x,y)$ | $P(f(z), z)$ |
| $\{x/\text{Socrates}\}$ | $\neg MAN(x) \lor MORTAL(x)$ | $\neg MAN(\text{Socrates}) \lor MORTAL(\text{Socrates})$ |

The third is the Socrates syllogism, and shows substitution doing the work propositional logic could not — see [[Propositional Logic]].

## Composition

Given $\theta = \{x_1/t_1, \dots, x_n/t_n\}$ and $\lambda = \{y_1/u_1, \dots, y_m/u_m\}$, the composition $\theta \circ \lambda$ is obtained from

$$\{x_1/t_1\lambda,\; \dots,\; x_n/t_n\lambda,\; y_1/u_1,\; \dots,\; y_m/u_m\}$$

by **deleting**:

- any $x_j/t_j\lambda$ where $t_j\lambda = x_j$ — a variable mapping to itself is meaningless
- any $y_i/u_i$ where $y_i \in \{x_1, \dots, x_n\}$ — already covered by $\theta$

Composition is how the [[Unification]] algorithm accumulates its answer: each disagreement resolved contributes one binding, composed onto the substitution built so far.

## See Also

- [[Unification]]
- [[Resolvents and Factors]]
- [[Resolution]]
- [[First-Order Logic]]
- [[CSCE 420]]
