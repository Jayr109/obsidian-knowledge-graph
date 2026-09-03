---
title: "First-Order Logic"
type: concept
tags: [csce420, logic, quantifiers, skolemization, knowledge-representation]
sources: [csce420-midterm-practice, csce420-final-practice, csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

First-order logic (FOL) extends propositional logic with objects, relations, functions, and quantifiers, so it can express general statements about unbounded domains. Its vocabulary: **constants** ($A, B, C$), **variables** ($x, y, z, w$), **functions** ($f(\cdot), g(\cdot)$), **predicates** ($P(\cdot), Q(\cdot), R(\cdot)$), and the quantifiers $\forall$ and $\exists$.

## Conversion to Clause Form

[[Resolution]] operates only on clauses (disjunctions of literals), so every FOL sentence must first be converted to conjunctive normal form:

1. Eliminate implications: $\alpha \to \beta$ becomes $\neg\alpha \lor \beta$.
2. Move $\neg$ inward (De Morgan); note $\neg\forall x\, P \equiv \exists x\, \neg P$ and $\neg\exists x\, P \equiv \forall x\, \neg P$.
3. Standardize variables apart so no two quantifiers bind the same name.
4. **Skolemize** — remove existential quantifiers (below).
5. Drop universal quantifiers (all remaining variables are implicitly universal).
6. Distribute $\lor$ over $\land$ to get a conjunction of clauses.
7. Split on $\land$: each conjunct becomes a separate clause.

Step 7 is the one exams punish. Both practice exams warn about it — the midterm's Problem 10 says outright: *"Make sure that each clause does not include ∧. If it does, your setup is incorrect."*

## Skolemization

An existentially quantified variable is replaced by a new symbol standing for "the thing that exists." What it may depend on is the whole point:

- $\exists y$ **not** inside any universal quantifier → replace $y$ with a new **Skolem constant** $A$.
- $\exists y$ inside $\forall x$ → replace $y$ with a new **Skolem function** $f(x)$ of the enclosing universally quantified variables.

A Skolem constant is just a Skolem function of arity zero, which is exactly why the dependency structure is what distinguishes the two quantifier orders.

## Why Quantifier Order Matters (Midterm Practice, Problem 8)

The problem asks why $\forall x\, \exists y\ Loves(x,y)$ is not equivalent to $\exists y\, \forall x\ Loves(x,y)$, and requires skolemization to make the point.

| Sentence | English | Skolemized |
|---|---|---|
| $\forall x\, \exists y\ Loves(x,y)$ | Everybody loves somebody | $Loves(x, f(x))$ |
| $\exists y\, \forall x\ Loves(x,y)$ | There is somebody whom everybody loves | $Loves(x, A)$ |

In the first, $y$ falls inside the scope of $\forall x$, so skolemization yields a **function** $f(x)$: the beloved may be a different person for each lover. In the second, $y$ is outermost and depends on nothing, so it becomes a **constant** $A$: one fixed individual loved by all.

$Loves(x, A)$ entails $Loves(x, f(x))$ — set $f(x) = A$ — but not conversely, since $f$ may be non-constant. The implication runs one way only, so the two sentences are not equivalent. The Skolem term's *arity* is the formal record of the dependency, which is why skolemization is the clean way to answer.

## From the Lecture

The deck's treatment follows Chang & Lee, *Symbolic Logic and Mechanical Theorem Proving* (1973), with substitution notation from Russell & Norvig.

### Why Predicate Calculus

[[Propositional Logic]] cannot reason with **general rules**. The motivating failure: $P$ = "all men are mortal", $Q$ = "Socrates is a man", $R$ = "Socrates is mortal" — $(P \land Q) \rightarrow R$ is not provable, because the atoms are unrelated. First-order logic fixes this by adding **objects, relations, properties, and functions**:

$$\forall x\; MAN(x) \rightarrow MORTAL(x), \qquad MAN(\text{Socrates}) \;\vdash\; MORTAL(\text{Socrates})$$

### The Three New Concepts

- **Terms** — objects in the domain, and how things get transformed (functions)
- **Predicates** — properties of objects, or relations; True or False valued
- **Quantifiers** — express properties of large sets without enumerating

A **term** is a constant ($a, b, c$), a variable ($x, y, z$), or $f(t_1, \dots, t_n)$ for a function symbol $f$ and terms $t_i$.

### Functions vs. Predicates

The distinction most often blurred:

| | Returns | Example |
|---|---|---|
| **Function** | a single object (a term) | $FatherOf(GeorgeJr) = GeorgeSr$ |
| **Predicate** | a truth value | $IsFather(GeorgeSr, GeorgeJr) = \text{True}$ |

$Brother(x,y)$ must be disambiguated: $AreBrothers(x,y)$ is a predicate; $BrotherOf(x,y)$ is a function returning a common brother.

### Quantifier Mistakes

The single most common error class, stated directly:

| English | Correct | Wrong — and why |
|---|---|---|
| All skunks are stinky | $\forall x\; Skunk(x) \rightarrow Stinky(x)$ | $\forall x\; Skunk(x) \land Stinky(x)$ — says *everything* is a stinky skunk |
| Some cats are white | $\exists x\; Cat(x) \land White(x)$ | $\exists x\; Cat(x) \rightarrow White(x)$ — true if there is anything that *is not a cat* |

**The rule: $\forall$ pairs with $\rightarrow$; $\exists$ pairs with $\land$.**

### Properties of Quantifiers

- $\forall x \forall y = \forall y \forall x$ and $\exists x \exists y = \exists y \exists x$ — like quantifiers commute
- $\forall x \exists y \neq \exists y \forall x$ — **unlike quantifiers do not**
- Each is definable from the other: $\forall x\, Likes(x, Coffee) = \neg\exists x\, \neg Likes(x, Coffee)$

Compare $\exists x \forall y\, Loves(x,y)$ ("someone loves everyone") with $\forall y \exists x\, Loves(x,y)$ ("everyone is loved by someone"). [[Skolemization]] makes the difference mechanical: a Skolem **constant** versus a Skolem **function**.

### Semantics: Domain and Interpretation

A **domain** $D$ is the section of the world being described — the set of all objects. An **interpretation** of a formula consists of a nonempty $D$ plus assignments:

1. each **constant** → an element of $D$
2. each $n$-ary **function** → a mapping $D^n \to D$
3. each $n$-ary **predicate** → a mapping $D^n \to \{\text{True}, \text{False}\}$

Evaluation: $\forall x\, G$ is True iff $G$ is True for **every** $x$ in $D$; $\exists x\, G$ is True iff $G$ is True for **any** $x$ in $D$.

### Bound vs. Free Variables

The **scope** of a quantifier is the range over which its variable takes effect. An occurrence is **bound** iff it lies within the scope of a quantifier employing that variable, and **free** otherwise.

- Bound: $\forall x \forall y\, P(x,y)$
- Free: $\forall x\, P(x,y)$ — the $y$ is free
- Both: $(\forall x\, P(x,y)) \land (\forall y\, Q(y))$

### The Decidability Problem

Consistency, satisfiability, and validity are defined as in propositional logic — but **many domains are infinite** (algebra, for instance), so there are infinitely many interpretations. Consequently **none of these properties is decidable in general for predicate calculus.** Truth tables do not generalize, which is why [[Resolution]] exists.

### Standard Form

Three steps, each with its own page: [[Prenex Normal Form]] → CNF matrix → [[Skolemization]]. The result is a set of clauses in CNF with **all variables universally quantified**.

## See Also

- [[Resolution]]
- [[Unification]]
- [[Logical Inference]]
- [[Situation Calculus]]
- [[Symbolic AI]]
