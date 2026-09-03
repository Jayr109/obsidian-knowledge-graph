---
title: "Resolvents and Factors"
type: concept
tags: [csce420, resolvent, factor, binary-resolvent, resolution, mgu]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

Applying [[Resolution]] in first-order logic requires two definitions the propositional case does not need: the **factor** of a clause, and the **binary resolvent** of two clauses.

## Factor of a Clause

If two or more literals of a clause $C$ **with the same sign** have a most general unifier $\sigma$, then $C\sigma$ is a **factor** of $C$. If $C\sigma$ is a unit clause, it is a **unit factor**.

**Example.** $C = P(x) \lor P(f(y)) \lor \neg Q(x)$. The first two literals unify with $\sigma = \{x/f(y)\}$, so

$$C\sigma = P(f(y)) \lor \neg Q(f(y))$$

Factoring collapses redundant literals, making clauses more succinct. Its real purpose: **when two clauses cannot be resolved directly, their factors may be resolvable.**

## Binary Resolvent

Let $C_1$ and $C_2$ be **parent clauses with no variables in common**, containing literals $L_1$ and $L_2$ such that $L_1$ and $\neg L_2$ have a most general unifier $\sigma$. Then

$$(C_1\sigma - L_1\sigma) \cup (C_2\sigma - L_2\sigma)$$

is a **binary resolvent**. $L_1$ and $L_2$ are the *literals resolved upon*.

A clause is treated as a **set of literals**: $\{P(x)\} \cup \{Q(x)\} = P(x) \lor Q(x)$.

### The Three-Step Recipe

1. Find the most general unifier $\sigma$
2. Apply $\sigma$ to both $C_1$ and $C_2$
3. Remove the complementary literals and take the union

**Example.** $C_1 = P(x) \lor Q(x)$ and $C_2 = \neg P(a) \lor R(y)$, with $\sigma = \{x/a\}$:

$$C_1\sigma = P(a) \lor Q(a), \quad C_2\sigma = \neg P(a) \lor R(y) \;\Longrightarrow\; Q(a) \lor R(y)$$

## Resolvent (Full Definition)

A **resolvent** of parents $C_1$ and $C_2$ is any one of:

1. a binary resolvent of $C_1$ and $C_2$
2. a binary resolvent of $C_1$ and a **factor** of $C_2$
3. a binary resolvent of a factor of $C_1$ and $C_2$
4. a binary resolvent of a factor of $C_1$ and a factor of $C_2$

Cases 2–4 exist precisely because factoring can unlock resolutions unavailable to the raw clauses.

**Exercise from the slides**: resolve $C_1 = P(x) \lor P(f(y)) \lor R(g(y))$ with $C_2 = \neg P(f(g(a))) \lor Q(b)$ — requiring the factor of $C_1$ against $C_2$, i.e. case 3.

## See Also

- [[Resolution]]
- [[Unification]]
- [[Substitution]]
- [[Resolution Strategies]]
- [[CSCE 420]]
