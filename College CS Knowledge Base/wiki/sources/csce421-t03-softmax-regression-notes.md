---
title: "CSCE 421 T03 Notes — Softmax Regression Derivations"
type: source
tags: [notes, csce421, softmax, cross-entropy, derivatives, kronecker-delta, homework]
sources: []
course: CSCE 421
updated: 2026-08-25
---

Typed companion notes to [[CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class]], authored by [[Shuiwang Ji]] and compiled by Yaochen Xie. 6 pages. The notes restate the slide material in prose and then supply what the slides omit: **the full derivatives of softmax and of the cross-entropy loss**, which the deck flags as necessary for the homework.

The stated aim is a complete, self-contained introduction to multi-class LR, usable at undergraduate or graduate level.

## Relationship to the Slides

Sections 2–4 track [[CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class]] closely — binary recap, softmax, cross-entropy, shift-invariance, and the $K=2$ sigmoid equivalence, with the same proofs. Two additions worth noting:

- The sigmoid is described as mapping $\mathbb{R}$ to $(0,1)$ **while preserving order**, since it is monotonically increasing — the order-preservation point the slides raise only as a question.
- Softmax likewise preserves the order of its inputs.
- The binary/multi-class loss-equivalence proof is noted as *already proved in the assignment*, and is reproduced in the notes.

## Section 5.1 — Derivative of Softmax

With $p_i$ the $i$-th element of $\mathrm{softmax}(\mathbf{a})$, the derivation splits on whether the indices match.

For $j = i$, quotient rule on $e^{a_i}/\sum_k e^{a_k}$:

$$\frac{\partial p_i}{\partial a_i} = \frac{e^{a_i}\sum_k e^{a_k} - e^{2a_i}}{\left(\sum_k e^{a_k}\right)^2} = p_i(1-p_i)$$

For $j \neq i$, the numerator does not depend on $a_j$:

$$\frac{\partial p_i}{\partial a_j} = \frac{0 - e^{a_i}e^{a_j}}{\left(\sum_k e^{a_k}\right)^2} = -p_i p_j$$

Unified with the **Kronecker delta**:

$$\frac{\partial p_i}{\partial a_j} = p_i(\delta_{ij} - p_j), \qquad \delta_{ij} = \begin{cases}1 & i = j\\ 0 & i \neq j\end{cases}$$

## Section 5.2 — Derivative of Cross-Entropy with Softmax

The payoff of the whole document. Starting from $L = -\sum_i y_i\log(p_i)$ and applying the chain rule through $\log$ and then the softmax derivative above:

$$\frac{\partial L}{\partial a_k} = -\sum_i y_i\frac{1}{p_i}\cdot p_i(\delta_{ki}-p_k) = -y_k(1-p_k) + \sum_{i\neq k}y_i p_k = p_k\sum_{i=1}^{K}y_i - y_k$$

Using $\sum_{i=1}^{K} y_i = 1$ (the one-hot vector sums to one):

$$\boxed{\ \frac{\partial L}{\partial a_k} = p_k - y_k\ }$$

**The result is the headline**: the gradient of cross-entropy with respect to the pre-softmax logits is simply *predicted minus true*. All the $\delta_{ij}$ bookkeeping cancels. This is why softmax and cross-entropy are paired — the composition has a trivial gradient, and it is the same $\hat{y}-y$ form that appears in [[Linear Regression]] and [[Logistic Regression]].

## Exam and Homework Relevance

The slides state explicitly that these derivations are needed for the homework, and that the only prerequisites are univariate calculus, the chain rule, and $\partial(\mathbf{w}^T\mathbf{b})/\partial\mathbf{w} = \mathbf{b}$.

## See Also

- [[Softmax Regression]]
- [[Softmax Function]]
- [[Cross-Entropy Loss]]
- [[CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class]]
- [[Gradient Descent]]
- [[CSCE 421]]
