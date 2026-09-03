---
title: "Softmax Function"
type: concept
tags: [csce421, softmax, multi-class, probability-distribution, shift-invariance, kronecker-delta]
sources: [csce421-t03-softmax-regression, csce421-t03-softmax-regression-notes]
course: CSCE 421
updated: 2026-08-25
---

Softmax maps a vector of $K$ real-valued scores to a probability distribution over $K$ classes. It generalizes the [[Sigmoid Function]] from two classes to many, and is the output layer of [[Softmax Regression]] and of essentially every modern classifier.

## Definition

Given $\mathbf{v} = [v_1,\dots,v_K]^T \in \mathbb{R}^K$:

$$\mathrm{softmax}(\mathbf{v}) = \frac{1}{\sum_{k=1}^{K}e^{v_k}}\begin{bmatrix}e^{v_1}\\ e^{v_2}\\ \vdots\\ e^{v_K}\end{bmatrix}$$

## Properties

| Property | Consequence |
|---|---|
| Maps $\mathbb{R}^K \to (0,1)^K$ | Every output is a valid probability |
| Outputs sum to 1 | The result is a genuine distribution, not just $K$ independent scores |
| Order-preserving | The largest score stays the largest probability |
| Shift-invariant | Adding a constant vector to all inputs changes nothing |

The sum-to-one property is what makes softmax more than an elementwise squashing: the classes *compete*. Raising one score necessarily lowers the others' probabilities, which is the right behavior for mutually exclusive classes.

## Shift-Invariance

Subtracting the same $\mathbf{u}$ from every weight vector leaves the output unchanged, because $e^{-\mathbf{u}^T\mathbf{x}}$ factors out of numerator and denominator and cancels:

$$\frac{e^{(\mathbf{w}_k-\mathbf{u})^T\mathbf{x}}}{\sum_i e^{(\mathbf{w}_i-\mathbf{u})^T\mathbf{x}}} = \frac{e^{\mathbf{w}_k^T\mathbf{x}}\,e^{-\mathbf{u}^T\mathbf{x}}}{\left(\sum_i e^{\mathbf{w}_i^T\mathbf{x}}\right)e^{-\mathbf{u}^T\mathbf{x}}} = \frac{e^{\mathbf{w}_k^T\mathbf{x}}}{\sum_i e^{\mathbf{w}_i^T\mathbf{x}}}$$

Two consequences:

1. **The parameterization is over-complete.** Only $K-1$ of the $K$ weight vectors are independent — which is why binary classification needs just one.
2. **It enables the sigmoid equivalence proof.** Shifting by $\mathbf{w}_1$ is the first step in showing the $K=2$ softmax equals the sigmoid. See [[Softmax Regression]].

## Derivative

With $p_i$ the $i$-th softmax output, the Jacobian splits on index equality and unifies via the **Kronecker delta**:

$$\frac{\partial p_i}{\partial a_j} = p_i\left(\delta_{ij}-p_j\right), \qquad \delta_{ij} = \begin{cases}1 & i=j\\ 0 & i \neq j\end{cases}$$

Diagonal terms are $p_i(1-p_i)$; off-diagonal terms are $-p_ip_j$. Note the diagonal case is exactly the sigmoid derivative.

Composed with [[Cross-Entropy Loss]], all of this structure cancels to leave $\partial L/\partial a_k = p_k - y_k$. Full derivation in [[CSCE 421 T03 Notes — Softmax Regression Derivations]].

## See Also

- [[Sigmoid Function]]
- [[Softmax Regression]]
- [[Cross-Entropy Loss]]
- [[Deep Learning]]
- [[CSCE 421]]
