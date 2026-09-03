---
title: "Supervised Learning Issues"
type: concept
tags: [csce420, generalization, sample-complexity, overfitting, catastrophic-forgetting]
sources: [csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

The open problems that make supervised learning hard, as the deck enumerates them. Supervised learning takes input-target pairs $\{\langle \vec{x}_i, \vec{t}_i \rangle\}$ and splits into **regression** (approximating $y = f(x)$) and **classification** (face recognition, handwriting, credit risk).

## The Questions

| Question | Concept |
|---|---|
| How well will it do on **training** inputs? | Fitting |
| How well will it do on **novel** inputs? | **Generalization** |
| How many samples are needed? | **Sample complexity** |
| Why does that number explode? | **[[Curse of Dimensionality]]** |
| What model should we choose? | **[[Inductive Bias]]** |

Plus **catastrophic forgetting**, which makes online learning hard — a network trained on new data tends to lose what it learned before.

**Generalization is the real goal**; performance on the training set is only a means. This is the same distinction [[In-Sample and Out-of-Sample Error]] formalizes in [[CSCE 421]] as $E_{in}$ versus $E_{out}$.

## Techniques Listed

Neural networks, decision tree learning, support vector machines, radial basis functions, naive Bayes learning, $k$-nearest neighbor.

Of these the course develops [[Neural Networks]] and [[Decision Tree Learning]] in depth.

## Computational Learning Theory

Named as the field addressing sample complexity — how many examples suffice for a given level of performance and generalization. The deck flags it rather than developing it.

## See Also

- [[Machine Learning]]
- [[Curse of Dimensionality]]
- [[Inductive Bias]]
- [[Decision Tree Learning]]
- [[In-Sample and Out-of-Sample Error]]
- [[CSCE 420]]
