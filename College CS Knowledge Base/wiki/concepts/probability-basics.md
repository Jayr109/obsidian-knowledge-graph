---
title: "Probability Basics"
type: concept
tags: [csce420, probability, axioms, joint-distribution, random-variables]
sources: [csce420-lecture-05-probabilistic-reasoning]
course: CSCE 420
updated: 2026-09-01
---

The notation, axioms, and joint-distribution machinery the rest of the probabilistic reasoning unit assumes.

## Notation

- **Random variable**: a variable that can take different values
  - $A, B, \dots$ — boolean (True/False)
  - $X, Y, \dots$ — numerical or multi-valued enumerations (1, 2, 0.5, Cloudy, Rainy, Sunny)
- $P(X = v)$ — probability that $X$ has value $v$; can be viewed as an **event**
- For booleans, $P(A)$ means $P(A = \text{True})$ and $P(\neg A)$ means $P(A = \text{False})$
- $\mathbf{P}(X)$ — **probability distribution**, the full list of probabilities for all values of $X$ (note the bold)

Logical connectives apply: $P(A \lor B)$, $P(A \land \neg B)$, $P(Cavity \land \neg Insured)$.

## Conditional Probability

$$P(A|B) = \frac{P(A \land B)}{P(B)}$$

The area intuition the deck uses: the bounding rectangle $U$ has area 1, so $P(A)$ is just the area of $A$. Writing $P(A|B)$ means **$B$ now takes the role of $U$** — within that restricted event space, how much is $A$? That is why the definition divides by $P(B)$: it renormalizes to the new universe.

As evidence accumulates, conditioning grows: $P(Cavity | Toothache \land BadBreath)$.

## The Three Axioms

1. $0 \le P(A) \le 1$
2. $P(A) = 1$ for a **valid** proposition (true under all interpretations); $P(A) = 0$ for an **inconsistent** one
3. $P(A \lor B) = P(A) + P(B) - P(A \land B)$

Axiom 2 is the bridge to logic: validity and inconsistency, defined in [[Propositional Logic]], become probability 1 and 0.

### Derived Properties

From the axioms, taking $B = \neg A$:

$$P(A \lor \neg A) = P(A) + P(\neg A) - P(A \land \neg A) \;\Rightarrow\; P(\text{True}) = P(A) + P(\neg A) - P(\text{False})$$

hence $P(\neg A) = 1 - P(A)$. More generally $\sum_{v \in V} P(X = v) = 1$.

## Joint Probability Distribution

An **atomic event** assigns a particular value to *every* random variable. The joint distribution $\mathbf{P}(X_1, \dots, X_n)$ completely specifies the probabilities of all atomic events, and they sum to 1.

### Worked Table

| | Toothache | ¬Toothache | Sum |
|---|---|---|---|
| **Cavity** | 0.04 | 0.06 | $P(C) = 0.1$ |
| **¬Cavity** | 0.01 | 0.89 | $P(\neg C) = 0.9$ |
| **Sum** | $P(T) = 0.05$ | $P(\neg T) = 0.95$ | 1.0 |

- $P(C \lor T) = 0.1 + 0.05 - 0.04 = 0.11$
- $P(C|T) = 0.04 / 0.05 = 0.8$
- $P(T|C) = 0.04 / 0.1 = 0.5$

Note $P(C|T) \neq P(T|C)$ — the asymmetry that [[Bayes Rule]] exists to navigate.

## The Scaling Problem

> In practice, writing a full joint probability table is impossible or too much effort: for $n$ boolean random variables you need $2^n$ entries.

This single fact motivates everything that follows — [[Conditional Independence]] and [[Bayesian Networks]] are both machinery for avoiding the full joint table.

## See Also

- [[Bayes Rule]]
- [[Conditional Independence]]
- [[Bayesian Networks]]
- [[Uncertainty]]
- [[CSCE 420]]
