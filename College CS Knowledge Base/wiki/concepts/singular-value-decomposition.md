---
title: "Singular Value Decomposition"
type: concept
tags: [csce421, svd, low-rank-approximation, frobenius-norm, spectral-norm, linear-algebra, truncated-svd]
sources: [csce421-t11-pca-autoencoders, csce421-t11-pca-notes]
course: CSCE 421
updated: 2026-11-08
---

SVD factorizes **any** real matrix — rectangular included — into a rotation, a scaling, and another rotation. [[CSCE 421]] introduces it in [[CSCE 421 T11 — Principal Component Analysis and Autoencoders|T11]] as the computational engine behind [[Principal Component Analysis|PCA]] and as the source of the best-low-rank-approximation theorem that makes PCA optimal.

## Definition

For a real $m\times n$ matrix with $m \ge n$:

$$R = U\tilde{\Sigma}V^T$$

where $U$ is orthogonal $m\times m$, $V$ is orthogonal $n\times n$, and $\tilde\Sigma$ is diagonal $m\times n$ with non-negative entries:

$$U^TU = UU^T = I_{m\times m}, \qquad V^TV = VV^T = I_{n\times n}, \qquad \tilde\Sigma = \begin{bmatrix}\Sigma_{n\times n}\\0\end{bmatrix}_{m\times n}$$

$$\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_n \ge 0 \qquad\text{(the singular values)}$$

If $\mathrm{rank}(R) = r$ then $\sigma_1 \ge \cdots \ge \sigma_r > 0$ and $\sigma_{r+1} = \cdots = \sigma_n = 0$. **The number of nonzero singular values is the rank.**

## The Rank-1 Sum

The reading the lecture emphasizes — "Pattern P4" in its linear-algebra refresher:

$$R = \sum_{i=1}^{r}\sigma_i u_i v_i^T$$

Each $u_iv_i^T$ is an outer product and therefore **rank 1**. So any matrix is a weighted sum of rank-1 pieces, ordered by weight. That ordering is what makes truncation meaningful.

## Relation to Eigendecomposition

The bridge PCA is built on:

> The columns of $U$ (**left**-singular vectors) are orthonormal eigenvectors of $RR^T$, and the columns of $V$ (**right**-singular vectors) are orthonormal eigenvectors of $R^TR$.

Verified directly:

$$R^TR = V\Sigma^2V^T, \qquad RR^T = U\begin{bmatrix}\Sigma^2 & 0\\0 & 0\end{bmatrix}U^T$$

So the singular values are the **square roots of the eigenvalues** of $R^TR$. This is the fact that lets PCA skip forming its covariance matrix — see [[Principal Component Analysis]].

### When are SVD and eigendecomposition the same?

The deck poses this as a question and answers it in two conditions:

1. $R$ is **symmetric**, $R = R^T$
2. $R$ is **positive semi-definite**, $x^TRx \ge 0$ for all $x$

Both are needed. Symmetry gives orthogonal eigenvectors (so $Q$ is orthogonal, matching $U$ and $V$); positive semi-definiteness makes every eigenvalue non-negative, matching the sign constraint on singular values.

### Why Λ can be negative but Σ cannot

A question the slides pose without answering. Eigendecomposition keeps the sign because an eigenvector's direction is fixed — $Sv = \lambda v$ with $\lambda < 0$ means $S$ **reverses** $v$, and that reversal is a real property of $S$.

SVD has two independent bases, $U$ and $V$, so a sign can always be pushed into one of them: $\sigma u v^T = (-\sigma)(-u)v^T$. Flip the singular vector and the singular value turns positive. **Generality is not lost**, because nothing constrains $u$ and $v$ to be related — which is exactly why SVD works on rectangular matrices where "eigenvector" has no meaning. The same reasoning answers exercise 6.1 of the companion notes, where an eigenvalue of $-2$ becomes a singular value of $2$ and forces a reordering.

## Compact SVD

Drop the zero rows and columns:

$$R = U_r\Sigma_rV_r^T = \sum_{i=1}^{r}\sigma_iu_iv_i^T$$

Same matrix, no wasted storage on components that contribute nothing.

## Truncated SVD and Best Low-Rank Approximation

Keep only the $k$ largest:

$$R_k = U_k\Sigma_kV_k^T = \sum_{i=1}^{k}\sigma_iu_iv_i^T$$

This is not merely *a* rank-$k$ approximation — it is provably **the best one**, in two different norms at once:

$$\min_{B:\,\mathrm{rank}(B)\le k}\lVert R - B\rVert_F = \lVert R - R_k\rVert_F = \sqrt{\sum_{i=k+1}^{n}\sigma_i^2}$$

$$\min_{B:\,\mathrm{rank}(B)\le k}\lVert R - B\rVert_2 = \lVert R - R_k\rVert_2 = \sigma_{k+1}$$

where $\lVert\cdot\rVert_F$ is the **Frobenius norm** and $\lVert\cdot\rVert_2$ the **spectral norm** (the largest singular value).

The lecture flags the asymmetry: *"note the difference in terms of approximation errors when different matrix norms are used."* The Frobenius error aggregates **all** discarded singular values; the spectral error is just the **largest** one discarded. Same optimal $R_k$, different accounting of what truncation cost.

**This theorem is what makes PCA optimal.** PCA's reconstruction proof works entirely by showing its projection equals the truncated SVD, and then invoking this result.

## See Also

- [[Eigendecomposition]]
- [[Principal Component Analysis]]
- [[Autoencoders]]
- [[CSCE 421]]
