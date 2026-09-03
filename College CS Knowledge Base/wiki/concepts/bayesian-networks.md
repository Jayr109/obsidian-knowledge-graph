---
title: "Bayesian Networks"
type: concept
tags: [csce420, probability, belief-networks, inference, causality]
sources: [csce420-final-practice, csce420-lecture-05-probabilistic-reasoning]
course: CSCE 420
updated: 2026-09-01
---

A Bayesian network (belief network) is a directed acyclic graph in which nodes are random variables and edges express direct dependence. Each node carries a conditional probability table (CPT) giving $P(X_i \mid Parents(X_i))$. The graph is a compact encoding of a full joint distribution: instead of $2^n - 1$ numbers, you store one CPT per node.

## The Chain Rule

The joint probability of any complete assignment factors as the product of each node's CPT entry:

$$P(x_1, \dots, x_n) = \prod_{i=1}^{n} P\big(x_i \mid parents(X_i)\big)$$

A node with no parents contributes its prior. This is the only formula needed for the "compute the joint probability" exam question.

## Worked Example (Final Practice, Problem 3)

Network: $A \rightarrow B \leftarrow C$. Both $A$ and $C$ are root nodes; $B$ has both as parents.

| Priors | | CPT for $B$ | | |
|---|---|---|---|---|
| $P(A) = 0.2$ | | $A$ | $C$ | $P(B \mid A,C)$ |
| $P(C) = 0.1$ | | T | T | 0.4 |
| | | T | F | 0.1 |
| | | F | T | 0.2 |
| | | F | F | 0.3 |

Compute $P(A, \neg B, C)$:

$$P(A, \neg B, C) = P(A)\, P(C)\, P(\neg B \mid A, C)$$
$$= 0.2 \times 0.1 \times \big(1 - P(B \mid A, C)\big) = 0.2 \times 0.1 \times (1 - 0.4) = 0.2 \times 0.1 \times 0.6$$

which is $0.012$, though the problem says no calculator is needed and the formula suffices.

Two things to get right: $A$ and $C$ are root nodes so they contribute *priors*, not conditionals; and $\neg B$ means taking the complement of the CPT entry for the row $A = T$, $C = T$ — the row is chosen by the values of the *parents*, which are both true here regardless of $B$ being negated.

## Node Ordering (Final Practice, Problem 4)

Adding nodes in **causal order** (causes before effects) produces sparser networks with smaller CPTs and edges that match real dependencies. Adding them in diagnostic order (effects first) forces spurious edges between effects that are actually conditionally independent given their common cause.

For Cavity, Catch (the dentist's steel probe catches on the cavity), and Toothache:

- **Order (2): Cavity, Catch, Toothache** — correct. Cavity is the common cause; both Catch and Toothache are its effects, and they are conditionally independent given Cavity. Result: $Catch \leftarrow Cavity \rightarrow Toothache$, two edges.
- **Order (1): Toothache, Catch, Cavity** — worse. Introducing Toothache first, then Catch, requires an edge between them (they are marginally dependent, since both signal a cavity), and then Cavity needs edges from both. Result: three edges and larger CPTs, for the same distribution.

> Worked here from the problem statements; the practice exam ships without an answer key.

## From the Lecture

### Definition

A belief network represents dependence between random variables and gives a **concise specification of the joint probability distribution**, as a directed acyclic graph:

1. a set of random variables — the **nodes**
2. a set of **directed edges** from node to node
3. each node carries a **conditional probability table** quantifying the effect of its parents
4. the graph has **no cycles**

### The Burglary Example

A new burglar alarm can be triggered by an actual burglary *or* an earthquake. Neighbours John and Mary each agreed to call when they hear it.

```
Burglary   Earthquake
      \       /
       \     /
        Alarm
        /    \
  JohnCalls  MaryCalls
```

Sample CPT for $P(Alarm \mid Burglary, Earthquake)$:

| Burglary | Earthquake | P | ¬P |
|---|---|---|---|
| True | True | 0.950 | 0.050 |
| True | False | 0.950 | 0.050 |
| False | True | 0.290 | 0.710 |
| False | False | 0.001 | 0.999 |

Full network parameters: $P(B) = .002$, $P(E) = .001$; $P(J|A) = .90$, $P(J|\neg A) = .05$; $P(M|A) = .70$, $P(M|\neg A) = .01$.

### Two Ways to Read a Network

- As a **representation of the joint distribution** — helpful when *constructing* the network
- As an **encoding of conditional independence statements** — helpful when *designing inference procedures*

Both views are needed, and they are used at different times.

### The Chain Rule Factorization

$$P(x_1, \dots, x_n) = \prod_{i=1}^{n} P(x_i \mid Parents(X_i))$$

Derived from two facts: the general chain rule

$$P(x_1,\dots,x_n) = \prod_{i=1}^{N} P(x_i \mid x_{i-1},\dots,x_1)$$

together with the network's structural claim

$$P(X_i \mid X_{i-1},\dots,X_1) = P(X_i \mid Parents(X_i))$$

The second equation is where the conditional independence assumption enters — it says the parents **screen off** all other predecessors. **The belief network fully defines a joint probability distribution.**

### Worked Calculation

Probability that the alarm sounded, neither burglary nor earthquake occurred, and both John and Mary call:

$$P(J \land M \land A \land \neg B \land \neg E) = P(J|A)P(M|A)P(A|\neg B \land \neg E)P(\neg B)P(\neg E)$$
$$= 0.9 \times 0.7 \times 0.001 \times 0.999 \times 0.998 = 0.00062$$

Each factor is read straight off one CPT row — no joint table is ever materialized.

### Structure Encodes Independence

$$P(MaryCalls \mid JohnCalls, Alarm, Earthquake, Burglary) = P(MaryCalls \mid Alarm)$$

Even though `Earthquake` and `Burglary` sit upstream, they are **conditionally independent of MaryCalls given Alarm**. Finding that dependency structure is the construction problem — see [[Belief Network Construction]].

For query types including **explaining away**, see [[Probabilistic Inference]].

## See Also

- [[Decision Tree Learning]]
- [[Machine Learning Paradigms]]
- [[History of AI]]
- [[CSCE 420]]
