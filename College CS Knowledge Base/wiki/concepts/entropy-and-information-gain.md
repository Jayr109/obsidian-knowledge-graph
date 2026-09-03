---
title: "Entropy and Information Gain"
type: concept
tags: [csce420, entropy, information-gain, shannon, decision-trees]
sources: [csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

The criterion [[Decision Tree Learning]] uses to choose which attribute to test first: pick the attribute that **maximizes information gain**, i.e. reduces entropy the most.

## Entropy

$$\text{Entropy}(E) = \sum_{i \in C} -P_i \log_2(P_i)$$

where $E$ is a set of examples ($\langle x, f(x)\rangle$ pairs) and $C$ the set of output classes.

> **Entropy measures the average surprisal of events. Less probable events are more surprising.**

- **More random (50/50)** → **high** entropy
- **More uniform (0/100)** → **low** entropy

In the restaurant example, the initial set and the "Full" subset are high entropy; the "None" and "Some" subsets are low — those splits nearly determine the answer by themselves.

## Information Gain

$$\text{Gain}(E, A) = \text{Entropy}(E) - \sum_{v \in \text{Values}(A)} \frac{|E_v|}{|E|}\,\text{Entropy}(E_v)$$

where $A$ is an attribute and $E_v$ the examples with $A = v$.

The second term is the **weighted average entropy after splitting** on $A$, each subset weighted by its share of the examples. Gain is therefore *entropy removed by the split*.

The weighting matters: an attribute that produces one tiny pure subset and one large messy one gains little, because the messy subset dominates the average.

## Why This Implements Ockham's Razor

Choosing the highest-gain attribute at each step is a greedy strategy for reaching certainty in **as few tests as possible**, which is exactly the short-tree preference described in [[Inductive Bias]]. The information-theoretic criterion is how an abstract preference for simplicity becomes an executable rule.

Note it is *greedy* — locally maximal gain at each node, with no backtracking, so the tree is not guaranteed globally minimal. This is the same greedy-versus-optimal tension as in [[Greedy Best-First Search]].

## See Also

- [[Decision Tree Learning]]
- [[Inductive Bias]]
- [[Machine Learning]]
- [[CSCE 420]]
