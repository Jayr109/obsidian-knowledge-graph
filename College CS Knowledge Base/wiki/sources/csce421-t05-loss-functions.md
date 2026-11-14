---
title: "CSCE 421 T05 — A Unified View of Loss Functions in Supervised Learning"
type: source
tags: [lecture, csce421, loss-functions, hinge-loss, zero-one-loss, perceptron-loss, exponential-loss, convexity, margin]
sources: []
course: CSCE 421
updated: 2026-09-22
---

Topic deck 5 of [[CSCE 421]], by [[Shuiwang Ji]]. 12 slides, with a companion typed note — [[CSCE 421 T05 Notes — A Unified View of Loss Functions]] — carrying the same content in prose. Steps back from individual models and compares **six loss functions on one axis**, revealing that everything in the course so far differs only in its choice of loss. Full treatment on [[Loss Functions]].

## The Unifying Device: $y_i s_i$

Given $X = [x_1, \dots, x_n]$ with labels $y_i \in \{+1, -1\}$ and $x_i \in \mathbb{R}^{d+1}$, a linear classifier computes the [[Linear Models|linear score]]

$$s_i = \mathbf{w}^T\mathbf{x}_i \tag{1}$$

The deck then studies *"the relations between loss values and $y_i s_i$"* — every loss is written as a function of this single quantity, called the **margin**:

| Reading | Meaning |
|---|---|
| Predict $-1$ if $s_i$ negative, $+1$ if positive | the decision rule |
| $y_i s_i > 0$ | **prediction is correct** |
| $\lvert s_i \rvert$ large | prediction confidence is large |
| $y_i s_i \gg 0$ | **very correct** |
| $y_i s_i \ll 0$ | **very wrong** |

Collapsing prediction and truth into one number is the whole trick of the deck: it puts six otherwise-unrelated formulas on a single pair of axes.

## The Six Losses

Each is presented as $\frac{1}{n}\sum_{i=1}^{n} L(y_i, s_i)$ over the dataset, differing only in $L$:

$$L_{0/1}(y_i, s_i) = \begin{cases} 1 & \text{if } y_i s_i < 0 \ 0 & \text{otherwise} \end{cases} \tag{2}$$

$$L_{p}(y_i, s_i) = \max(0,\, -y_i s_i) \tag{3}$$

$$L_{s}(y_i, s_i) = (1 - y_i s_i)^2 \tag{5}$$

$$L_{\log}(y_i, s_i) = \log\left(1 + e^{-y_i s_i}\right) \tag{7}$$

$$L_{h}(y_i, s_i) = \max(0,\, 1 - y_i s_i) \tag{9}$$

$$L_{\exp}(y_i, s_i) = e^{-y_i s_i} \tag{10}$$

Each slide's framing, in the deck's own terms:

- **Zero-one** — *"aims at measuring the number of prediction errors."*
- **Perceptron** — zero-one *"incurs the same loss value of 1 for all wrong predictions, no matter how far a wrong prediction is from the hyperplane."* Perceptron loss fixes this by *"penalizing each wrong prediction by the extent of violation."* Loss is 0 when correctly classified.
- **Square** — *"commonly used for regression problems,"* usable for classification but *"tends to penalize wrong predictions excessively,"* and notably *"when the value of $y_i s_i$ is large and the classifier is making correct predictions, the square loss incurs a large loss value."*
- **Log (cross entropy)** — *"Logistic regression employs the log loss."* Identical to the $E_{in}$ derived in T02; see [[Cross-Entropy Loss]].
- **Hinge** — *"support vector machines employ hinge loss to obtain a classifier with maximum-margin."* Unlike zero-one and perceptron, *"a data may be penalized even if it is predicted correctly."*
- **Exponential** — *"more aggressive,"* grows exponentially for negative values, *"very sensitive to wrong predictions."* Used by **AdaBoost**.

## Convexity

A formal definition, given because it is the property that decides whether a loss is usable:

$$f(tx_1 + (1-t)x_2) \le t f(x_1) + (1-t) f(x_2), \quad t \in [0,1]$$

with strict convexity replacing $\le$ by $<$ for $t \in (0,1)$, $x_1 \ne x_2$. The intuition given: *"a function is convex if the line segment between any two points on the function is not below the function."* See [[Convexity]].

## Comparison Slide

The six numbered conclusions, which are the deck's payoff and the most likely exam material:

1. Zero-one: correct $\Rightarrow$ zero penalty, otherwise penalty of one — **all wrong predictions receive the same loss**.
2. Perceptron: penalty proportional to extent of violation. For other losses, *"a data sample can still incur penalty even if it is classified correctly."*
3. Log loss is similar to hinge loss *"but it is a **smooth** function which can be optimized with the gradient descent method."*
4. Log loss grows slowly for negative values; **exponential and square are more aggressive**.
5. **Square loss will penalize correct predictions severely** when $y_i s_i$ is large.
6. **Zero-one loss is not convex while the other loss functions are convex.** Hinge and perceptron loss are **not strictly convex**.

Point 6 is the punchline of the whole deck: zero-one loss is what you actually want to minimize, and it is precisely the one you cannot optimize. Every other loss on the list is a convex surrogate for it.

## See Also

- [[Loss Functions]]
- [[Convexity]]
- [[Cross-Entropy Loss]]
- [[Logistic Regression]]
- [[Perceptron]]
- [[Gradient Descent]]
- [[CSCE 421]]
