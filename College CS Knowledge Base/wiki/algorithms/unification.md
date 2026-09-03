---
title: "Unification"
type: algorithm
tags: [csce420, logic, substitution, mgu, occurs-check]
sources: [csce420-midterm-practice, csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

Unification finds a substitution that makes two logical expressions identical. It is the mechanism that lets [[Resolution]] work on [[First-Order Logic|first-order]] clauses rather than only propositional ones: two literals resolve when their atoms unify. The substitution produced is the **most general unifier (MGU)** — it commits to no more than necessary.

$$\text{Unify}(p, q) = \theta \quad \text{where} \quad p\theta = q\theta$$

## Procedure

Walk the two expressions in parallel, argument by argument:

1. **Both identical constants or the same variable** — succeed, no binding.
2. **Variable vs. term** — bind the variable to the term, apply the binding to everything remaining, and compose it into $\theta$.
3. **Two different constants** — **fail**.
4. **Two functions with different symbols or arities** — **fail** (clash).
5. **Same function symbol** — recurse on corresponding arguments.

**Occurs check:** binding $x$ to a term containing $x$ (e.g. $x / f(x)$) must fail, or the substitution produces an infinite term.

Bindings compose. After binding $x/f(y)$, every later step works on the already-substituted expressions — skipping this is the most common source of wrong answers.

## Worked Examples (Midterm Practice, Problem 9)

Here $x, y, z$ are variables; $A, B, C$ are constants; $f, g$ are functions; $P$ is a predicate.

### Set 1 — NOT unifiable

$$P(f(z),\ g(y),\ z) \qquad P(x,\ x,\ B)$$

| Step | Pair | Action | $\theta$ so far |
|---|---|---|---|
| 1 | $f(z)$ vs $x$ | $x$ is a variable, bind it | $\{x/f(z)\}$ |
| 2 | apply $\theta$ | second expression becomes $P(f(z),\, f(z),\, B)$ | |
| 3 | $g(y)$ vs $f(z)$ | **function clash** — $g \ne f$ | **fail** |

**Not unifiable.** The culprit is the repeated variable $x$ in the second expression: unifying position 1 forces $x = f(z)$, which then forces position 2 to be $f(\cdot)$, but position 2 of the first expression is headed by $g$. (Position 3 would have failed too — $z$ would need to be both $B$ and, via $f(z)$, a subterm of itself.)

### Set 2 — Unifiable

$$P(x,\ A,\ g(x)) \qquad P(f(y),\ y,\ g(z))$$

| Step | Pair | Action | $\theta$ so far |
|---|---|---|---|
| 1 | $x$ vs $f(y)$ | bind $x$ | $\{x/f(y)\}$ |
| 2 | $A$ vs $y$ | bind $y$ to the constant | $\{x/f(A),\ y/A\}$ |
| 3 | $g(f(A))$ vs $g(z)$ | same function symbol, recurse: $z$ vs $f(A)$ | $\{x/f(A),\ y/A,\ z/f(A)\}$ |

**MGU:** $\theta = \{x/f(A),\ y/A,\ z/f(A)\}$

**Unified expression:** $P(f(A),\ A,\ g(f(A)))$

Note step 2 propagating backward: binding $y/A$ updates the earlier binding $x/f(y)$ to $x/f(A)$. That is composition of substitutions, and it is what "show all your steps" is asking for.

> Worked here from the problem statement; the practice exam ships without an answer key.

## From the Lecture

### The Purpose

The resolution step is valid in predicate calculus when two clauses contain complementary **predicates** — but their arguments must first be made identical. Given

$$C_1: P(x) \lor Q(x) \qquad C_2: \neg P(f(y)) \lor R(y)$$

substituting $f(y)$ for $x$ in $C_1$ permits the resolution, yielding $C_3: Q(f(y)) \lor R(y)$.

Unification is the algorithm that finds such a substitution — the missing piece in the chain *natural language → first-order formulas → standard form → resolution*.

### Built on Substitution

Unification composes [[Substitution|substitutions]]: each disagreement resolved contributes one binding, composed onto what has been built so far. The result is the **most general unifier (MGU)** — the substitution that commits to as little as possible while making the terms identical.

### Worked Example

The deck works this stepwise, showing both expressions after each binding is applied:

```
1  {x/g(y)}   P(g(y), f(g(y)), z)   P(g(y), f(g(a)), y)
2  {y/a}      P(g(a), f(g(a)), z)   P(g(a), f(g(a)), a)
3  {z/a}      P(g(a), f(g(a)), a)
```

**Unifier: $\{x/g(a),\, y/a,\, z/a\}$.**

Each step scans left to right for the first disagreement, binds a variable to the opposing term, and applies that binding to *both* expressions before continuing — which is why the earlier $\{x/g(y)\}$ is later refined to $x/g(a)$ once $y/a$ is discovered.

### Where It Is Used

Unification is required for [[Resolvents and Factors|factors and binary resolvents]], both of which are defined in terms of a most general unifier, and it is the parameter-passing mechanism of [[Prolog]].

## See Also

- [[Resolution]]
- [[First-Order Logic]]
- [[Logical Inference]]
