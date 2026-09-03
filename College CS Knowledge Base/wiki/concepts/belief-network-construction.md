---
title: "Belief Network Construction"
type: concept
tags: [csce420, belief-networks, node-ordering, causal-models, knowledge-engineering]
sources: [csce420-lecture-05-probabilistic-reasoning]
course: CSCE 420
updated: 2026-09-01
---

How to *build* a [[Bayesian Networks|belief network]] — and why the order in which nodes are added determines whether the result is compact or useless.

## The Construction Algorithm

1. Choose the set of relevant variables $X_i$ describing the domain.
2. Choose an **ordering** of the variables.
3. While variables remain:
   1. Pick a variable $X_i$ and add a node for it.
   2. Set $Parents(X_i)$ to some **minimal set of nodes already in the net** such that the conditional independence property is satisfied.
   3. Define the conditional probability table for $X_i$.

## Why It Works

- Because **newly added nodes cannot point to existing nodes**, the resulting graph is always **acyclic** by construction.
- Violation of the probability axioms is avoided.
- The result is **compact** compared with the full joint table — locally structured, or sparse.

### The Compactness Result

| Representation | Entries |
|---|---|
| Belief network, $n$ nodes, $k$ parents each | $n2^k$ |
| Full joint probability table | $2^n$ |

For $n = 30$ and $k = 3$, that is 240 versus over a billion. **The saving is the entire reason belief networks exist.**

## Node Ordering Matters Enormously

Two orderings of the burglary example produce very different networks:

- `MaryCalls, JohnCalls, Alarm, Burglary, Earthquake`
- `MaryCalls, JohnCalls, Earthquake, Burglary, Alarm`

Both **represent the same joint distribution** — but some represent the conditional independence relations far better. The bad ordering yields a graph requiring **the same number of entries as a full joint probability table**, discarding the entire benefit.

### Why the Bad Ordering Fails

Adding `MaryCalls` then `JohnCalls`, conditional independence does not hold:

$$P(JohnCalls|MaryCalls) \neq P(JohnCalls)$$

so **MaryCalls must become a parent of JohnCalls** — an edge that is not causal. The reason: *if Mary calls, the alarm probably went off, which makes it more likely John calls.* Without `Alarm` in the network yet, that correlation has to be wired directly.

## The Rule: Add Root Causes First

For $A$ to be a parent of $B$, $A$ must be added **before** $B$. So **add nodes with direct influence on others first** — the root causes.

**Stick to a causal model** rather than a diagnostic one. Three benefits:

- Conditional probability tables can be made **smaller**
- The conditional probabilities are **easier to come up with** — see the causal-vs-diagnostic argument in [[Bayes Rule]]
- It is **easier to reason** about the domain using the network

## Knowledge Engineering for Uncertain Reasoning

The deck's closing checklist:

1. **Decide what to talk about** — gradually add factors influencing the current collection of events
2. **Determine the variables** and the range of their values
3. **Encode general knowledge** about dependence: *qualitative* (which variable depends on which) then *quantitative* (the probability values, from experience or sampled data)
4. **Encode the specific problem instance** — assign values to variables
5. **Pose queries** — what is the probability of $X$? how sensitive are the CPT values to perturbation?

## See Also

- [[Bayesian Networks]]
- [[Conditional Independence]]
- [[Probabilistic Inference]]
- [[Bayes Rule]]
- [[CSCE 420]]
