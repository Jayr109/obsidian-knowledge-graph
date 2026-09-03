---
title: "Polynomial Normal Equations in Matrix Form"
type: derivation
tags: [polynomial-regression, matrix, normal-equations, least-squares]
sources: [lecture-02-more-general-regression]
course: STAT 212
updated: 2026-07-04
---

Writes the [[Polynomial Regression]] normal equations compactly in matrix form and states the least-squares solution $\hat\beta = (X^TX)^{-1}X^Ty$. This matrix machinery is the bridge to [[Multiple Linear Regression]].

## The scalar normal equations

Minimizing $f(b_0,\dots,b_k) = \sum_i (y_i - \sum_{j=0}^k b_j x_i^j)^2$ and setting $\partial f/\partial b_\ell = 0$ yields, for $\ell = 0,\dots,k$:

$$\sum_{j=0}^k b_j \sum_{i=1}^n x_i^{\,j+\ell} = \sum_{i=1}^n x_i^{\,\ell} y_i.$$

Each is linear in the $b_j$: $a_{\ell 0}b_0 + a_{\ell 1}b_1 + \cdots + a_{\ell k}b_k = c_\ell$.

## Matrix objects

$$b = [b_0\ b_1\ \cdots\ b_k]^T, \quad y = [y_1\ \cdots\ y_n]^T, \quad X = \begin{bmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^k \\ 1 & x_2 & x_2^2 & \cdots & x_2^k \\ & & \vdots & & \\ 1 & x_n & x_n^2 & \cdots & x_n^k \end{bmatrix}.$$

`X` is the $n \times (k+1)$ **design matrix**; $A^T$ denotes transpose.

## Normal equations and solution

| Step | Justification |
|------|---------------|
| The $k+1$ scalar normal equations stack as $X^TX\,b = X^Ty$ | MS (matrix bookkeeping of the sums above) |
| Assume $X^TX$ is invertible | BD (full-rank design condition) |
| $b = (X^TX)^{-1}X^Ty = \hat\beta$ | MS (left-multiply by $(X^TX)^{-1}$) |

## Result

$$\boxed{\;\hat\beta = (X^TX)^{-1}X^Ty\;}$$

The components of $\hat\beta$ are the least-squares estimates of $\beta_0,\dots,\beta_k$. The same formula gives the estimates for [[Multiple Linear Regression]] once `X`'s columns hold the predictors.

## See Also
- [[Polynomial Regression]]
- [[Inference for Polynomial Regression]]
- [[Multiple Linear Regression]]
