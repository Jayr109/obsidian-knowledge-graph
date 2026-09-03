---
title: "Linear Regression"
type: algorithm
tags: [csce421, linear-regression, least-squares, normal-equations, pseudoinverse, supervised-learning]
sources: [csce421-t01-linear-regression]
course: CSCE 421
updated: 2026-08-25
---

Linear regression fits $h(\mathbf{x}) = \mathbf{w}^T\mathbf{x}$ to a real-valued target by minimizing squared error. It is the one model in the [[CSCE 421]] opening arc with a **closed-form solution** — no iteration needed — which is what makes it the natural first model.

## Problem

Same features as the credit-approval example behind [[Linear Models]], but the target changes from a decision to a quantity: instead of Approve/Deny, predict the **credit line** in dollars. So $y \in \mathbb{R}$, and the $\mathrm{sign}(\cdot)$ of the perceptron is dropped:

$$h(\mathbf{x}) = \sum_{i=0}^{d} w_i x_i = \mathbf{w}^T\mathbf{x}$$

## Error Measure

$$E_{in}(h) = \frac{1}{N}\sum_{n=1}^{N}\left(h(\mathbf{x}_n) - y_n\right)^2 \qquad\text{(in-sample)}$$

$$E_{out}(h) = \mathbb{E}_x\left[(h(\mathbf{x}) - y)^2\right] \qquad\text{(out-of-sample)}$$

See [[In-Sample and Out-of-Sample Error]] — only $E_{in}$ is computable from data; $E_{out}$ is the quantity actually cared about.

## Matrix Form

| Object | Shape | Meaning |
|---|---|---|
| $X$ | $N \times (d+1)$ | Data matrix, one augmented $\mathbf{x}_n^T$ per row |
| $\mathbf{y}$ | $N$ | Target vector |
| $\hat{\mathbf{y}} = X\mathbf{w}$ | $N$ | In-sample predictions |

$$E_{in}(\mathbf{w}) = \frac{1}{N}\lVert \hat{\mathbf{y}} - \mathbf{y}\rVert_2^2 = \frac{1}{N}\lVert X\mathbf{w} - \mathbf{y}\rVert_2^2 = \frac{1}{N}\left(\mathbf{w}^TX^TX\mathbf{w} - 2\mathbf{w}^TX^T\mathbf{y} + \mathbf{y}^T\mathbf{y}\right)$$

## Derivation of the Solution

Two vector-calculus identities are all that is needed:

$$\nabla_\mathbf{w}\left(\mathbf{w}^T\mathbf{b}\right) = \mathbf{b}, \qquad \nabla_\mathbf{w}\left(\mathbf{w}^TA\mathbf{w}\right) = \left(A + A^T\right)\mathbf{w}$$

With $A = X^TX$ (symmetric) and $\mathbf{b} = X^T\mathbf{y}$:

$$\nabla_\mathbf{w}E_{in}(\mathbf{w}) = \frac{2}{N}\left(X^TX\mathbf{w} - X^T\mathbf{y}\right)$$

Setting $\nabla E_{in}(\mathbf{w}) = \mathbf{0}$ gives the **normal equations**:

$$X^TX\mathbf{w} = X^T\mathbf{y}$$

and, when $X^TX$ is invertible,

$$\mathbf{w}_{lin} = \left(X^TX\right)^{-1}X^T\mathbf{y}$$

The minimum is a true minimum, not merely a stationary point, because $E_{in}$ is convex in $\mathbf{w}$ ($X^TX$ is positive semidefinite).

## Algorithm

1. Construct $X$ and $\mathbf{y}$ from the dataset $(\mathbf{x}_1,y_1),\dots,(\mathbf{x}_N,y_N)$, where each $\mathbf{x}$ includes the $x_0 = 1$ coordinate.
2. Compute the **pseudoinverse** $X^\dagger$. If $X^TX$ is invertible, $X^\dagger = (X^TX)^{-1}X^T$.
3. Return $\mathbf{w}_{lin} = X^\dagger\mathbf{y}$.

## Contrast with the Other Models

This closed form is the exception. [[Logistic Regression]] has no analytic solution — its gradient cannot be set to zero symbolically — so it falls back on [[Gradient Descent]]. Note the shared shape of the gradient though: here $\nabla E_{in} \propto X^T(\hat{\mathbf{y}} - \mathbf{y})$, the same *predicted minus true* structure that appears in the softmax cross-entropy gradient.

## See Also

- [[Linear Models]]
- [[Logistic Regression]]
- [[In-Sample and Out-of-Sample Error]]
- [[Gradient Descent]]
- [[CSCE 421]]
