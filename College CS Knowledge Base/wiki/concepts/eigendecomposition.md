---
title: "Eigendecomposition"
type: concept
tags: [csce421, eigendecomposition, orthogonal-matrix, spectral-theorem, symmetric-matrix, linear-algebra]
sources: [csce421-t11-pca-autoencoders, csce421-t11-pca-notes]
course: CSCE 421
updated: 2026-11-08
---

Eigendecomposition factorizes a square matrix into its eigenvectors and eigenvalues. [[CSCE 421]] covers it in [[CSCE 421 T11 — Principal Component Analysis and Autoencoders|T11]] as the linear-algebra groundwork for [[Singular Value Decomposition|SVD]] and [[Principal Component Analysis|PCA]] — the covariance matrix PCA maximizes against is symmetric, which is the case where everything is well behaved.

## Orthogonal Matrices First

A matrix $Q$ is **orthogonal** when its columns and rows are orthonormal vectors:

$$Q^TQ = QQ^T = I \qquad\Longrightarrow\qquad Q^{-1} = Q^T$$

> a very useful property as it provides an easy way to compute the inverse

For $Q = [q_1,\dots,q_n]$ this means $q_i^Tq_j = 0$ when $i \ne j$, and $q_i^Tq_i = 1$.

### The asymmetry for partial column sets

A point the lecture makes deliberately, because the PCA reconstruction proof depends on it. Split the columns into $Q_1 = [q_1,\dots,q_i]$ and $Q_2 = [q_{i+1},\dots,q_n]$. Then:

$$Q_1^TQ_1 = I, \quad Q_2^TQ_2 = I, \qquad\text{but}\qquad Q_1Q_1^T \ne I, \quad Q_2Q_2^T \ne I$$

The reason is what each product means. $Q_1^TQ_1$ collects pairwise inner products of the kept columns — still orthonormal, so still the identity (of smaller size). $Q_1Q_1^T$ is the **projection onto the subspace those columns span**, which cannot be the identity unless they span everything.

That projection is exactly the $GG^T$ appearing in PCA's reconstruction step: $GG^T\tilde{X}$ projects the data onto the principal subspace and no further.

## Eigendecomposition

A square $n\times n$ matrix $S$ with $n$ linearly independent eigenvectors factorizes as

$$S = Q\Lambda Q^{-1}$$

with $Q$'s columns the eigenvectors and $\Lambda$ diagonal holding the eigenvalues.

> Note that **only diagonalizable matrices** can be factorized in this way.

## The Symmetric Case

Everything PCA needs lives here:

> If $S$ is a symmetric matrix, its eigenvectors are **orthogonal**. Thus $Q$ is an orthogonal matrix and we have
>
> $$S = Q\Lambda Q^T$$

The inverse becomes a transpose, which is both cheaper and numerically safer. All eigenvalues of a real symmetric matrix are **real**, and the eigenvectors can always be chosen **orthonormal**.

This matters for PCA because the covariance matrix

$$C = \frac{1}{n}\sum_i (x_i-\bar{x})(x_i-\bar{x})^T$$

is symmetric by construction — it is a sum of outer products of a vector with itself. That is precisely why the Ky Fan theorem, which requires a symmetric matrix, applies to it.

## The Spectral Form

Writing the factorization as a sum of rank-1 pieces:

$$S = Q\Lambda Q^T = \lambda_1 q_1q_1^T + \lambda_2 q_2q_2^T + \lambda_3 q_3q_3^T = \lambda_1P_1 + \lambda_2P_2 + \lambda_3P_3$$

Each $P_i = q_iq_i^T$ is a **rank-1 projection matrix** onto the direction $q_i$, and they satisfy

$$P_1 + P_2 + P_3 = I, \qquad P_iP_j = O \ \ (i \ne j)$$

The first says the projections partition the space completely; the second says they are mutually non-overlapping. So a symmetric matrix decomposes space into orthogonal directions and scales each independently by its eigenvalue — the **spectral theorem**.

This is the same rank-1-sum pattern SVD uses, and the lecture presents them on consecutive slides to make the parallel visible:

| | Decomposition | Applies to | Diagonal entries |
|---|---|---|---|
| Eigendecomposition | $S = Q\Lambda Q^T$ | symmetric square matrices | **may be negative** |
| [[Singular Value Decomposition]] | $R = U\tilde\Sigma V^T$ | **any** matrix, rectangular included | **non-negative, sorted** |

Eigendecomposition uses one basis on both sides; SVD uses two independent ones, which is what buys it generality. See [[Singular Value Decomposition]] for why that difference lets $\Sigma$ stay non-negative without losing anything.

## See Also

- [[Singular Value Decomposition]]
- [[Principal Component Analysis]]
- [[CSCE 421]]
