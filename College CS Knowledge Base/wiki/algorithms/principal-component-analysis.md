---
title: "Principal Component Analysis"
type: algorithm
tags: [csce421, pca, dimensionality-reduction, unsupervised, covariance, ky-fan, svd, reconstruction-error]
sources: [csce421-t11-pca-autoencoders, csce421-t11-pca-notes]
course: CSCE 421
updated: 2026-11-08
---

PCA projects high-dimensional data onto a lower-dimensional subspace that **simultaneously maximizes retained variance and minimizes reconstruction error**. It is the first [[Unsupervised Learning|unsupervised]] method in [[CSCE 421]] — it uses no labels at all — and the course derives it from the variance objective, then proves the same solution is optimal for reconstruction.

## Reduction, Not Selection

A distinction the lecture states explicitly and is easy to test:

| | What it does |
|---|---|
| **Feature selection** | keeps a **subset** of the original features, discards the rest |
| **Feature reduction** (PCA) | **still uses all the features**, combined into fewer new ones |

Each principal component is a linear combination of *every* original feature. Nothing is thrown away; the information is repackaged.

## The Objective: Maximum Variance

Given $x_1,\dots,x_n \in \mathbb{R}^p$ and a unit vector $a$ defining the projection $z_i = a^Tx_i$:

$$a^* = \arg\max_{\lVert a\rVert = 1}\; \frac{1}{n}\sum_{i=1}^{n}(z_i - \bar{z})^2$$

The constraint $\lVert a\rVert = 1$ is essential — without it you could inflate the variance arbitrarily by scaling $a$, which says nothing about direction.

### The derivation

Short enough to reproduce from memory, and worth being able to. Start by noting $\bar{z} = \frac{1}{n}\sum_i a^Tx_i = a^T\bar{x}$:

$$\begin{aligned}
a^* &= \arg\max_{\lVert a\rVert=1} \frac{1}{n}\sum_i (a^Tx_i - a^T\bar{x})^2 \\
&= \arg\max_{\lVert a\rVert=1} \frac{1}{n}\sum_i a^T(x_i-\bar{x})(x_i-\bar{x})^Ta \\
&= \arg\max_{\lVert a\rVert=1} a^T\underbrace{\left(\frac{1}{n}\sum_i (x_i-\bar{x})(x_i-\bar{x})^T\right)}_{C,\ p\times p\ \text{covariance matrix}}a \\
&= \arg\max_{\lVert a\rVert=1} a^TCa
\end{aligned}$$

The move that makes it work is the middle line: a squared scalar $(a^Tv)^2$ is rewritten as $a^Tvv^Ta$, which lets $a$ come outside the sum and exposes the covariance matrix.

## Generalizing to k Dimensions

$$A^* = \arg\max_{A\in\mathbb{R}^{p\times k}:\;A^TA=I_k}\; \mathrm{trace}\left(A^TCA\right)$$

Two things to read off. The constraint $A^TA = I_k$ forces the $k$ projection directions to be **orthonormal** — otherwise they would all collapse onto the single highest-variance direction. And the trace is exactly the **sum of the variances** along each direction:

$$\mathrm{trace}(A^TCA) = \sum_{i=1}^{k}\left(a_i^TCa_i\right)$$

## The Solution: Ky Fan Theorem

> **Theorem (Ky Fan).** Let $H\in\mathbb{R}^{n\times n}$ be symmetric with eigenvalues $\lambda_1 \ge \cdots \ge \lambda_n$ and corresponding eigenvectors $U = [u_1,\dots,u_n]$. Then
>
> $$\lambda_1 + \cdots + \lambda_k = \max_{A:\,A^TA=I_k} \mathrm{trace}(A^THA)$$
>
> and the optimal $A^*$ is $A^* = [u_1,\dots,u_k]Q$ with $Q$ an **arbitrary orthogonal matrix**.

The covariance matrix $C$ is symmetric, so the theorem applies directly: **take the eigenvectors of $C$ for its $k$ largest eigenvalues.** The maximum achievable variance is $\lambda_1 + \cdots + \lambda_k$.

**PCA solutions are not unique.** The trailing $Q$ means any orthogonal rotation of the chosen basis spans the same subspace and achieves the same objective. The course uses $Q = I$. This non-uniqueness returns when PCA is compared to [[Autoencoders]].

## Computing It: Use SVD, Not the Covariance Matrix

The naive route — form $C$, eigendecompose it — is a bad idea:

> If $p$ is large, it is very costly to compute eigenvectors of $C$ directly. Moreover, if $p \gg n$, there are known computational problems.

$C$ is $p \times p$, so for 10,000-dimensional data it is a 100-million-entry matrix regardless of how few samples you have. The fix uses the [[Singular Value Decomposition|SVD]] relation that the left-singular vectors of a matrix are the eigenvectors of $MM^T$:

```
X  (p x n)  ->  centre  ->  X~  ->  SVD: X~ = U Σ~ V^T  ->  G = U_k  (p x k)

projected features:   Z = G^T X~   (k x n)
```

with $\tilde{X} = X - \bar{X}\mathbf{1}_n^T$. Because $C = \frac{1}{n}\tilde X\tilde X^T$, the columns of $U$ are already the eigenvectors of $C$, sorted — **no covariance matrix is ever formed.**

The $k$-th **row** of $Z$ is the $k$-th **principal component**.

## Minimum Reconstruction Error

Reconstruct by projecting back up: $\check{X} = GZ = GG^T\tilde{X}$. The claim is that this is the best possible rank-$k$ approximation:

$$GG^T\tilde{X} = \arg\min_{B:\;\mathrm{rank}(B)\le k}\lVert \tilde{X} - B\rVert_F$$

The proof is four lines, and it works by showing $GG^T\tilde X$ *is* the truncated SVD — which [[Singular Value Decomposition|is already known]] to be the optimal low-rank approximation:

$$GG^T\tilde X = U_kU_k^TU\tilde\Sigma V^T = U_kU_k^T[U_k\;\;U_{-k}]\tilde\Sigma V^T = U_k[I\;\;0]\tilde\Sigma V^T = U_k\Sigma_kV_k^T = \sum_{i=1}^{k}\sigma_iu_iv_i^T$$

So the error is

$$\lVert \tilde X - GG^T\tilde X\rVert_F = \sqrt{\sum_{i=k+1}^{n}\sigma_i^2}, \qquad \lVert \tilde X - GG^T\tilde X\rVert_2 = \sigma_{k+1}$$

optimal in **both** the Frobenius and spectral norms. **Both goals announced at the start are now met by the same projection** — that equivalence is the elegant part of PCA, not a coincidence.

## Why You Must Centre First

Maximum variance holds either way, since $C$ is unchanged by shifting the data. Minimum reconstruction error does **not**. Reconstructing the uncentered $X$ gives

$$\lVert X - GG^TX\rVert_F = \lVert \underbrace{(\tilde X - GG^T\tilde X)}_{\text{the real error}} + \underbrace{(\bar X - GG^T\bar X)}_{\text{reconstructing the mean}}\rVert_F$$

The second term measures how well the subspace reproduces the **mean**, which is an offset, not structure — it should not count as error at all. Centre the data and it vanishes. The companion notes carry this derivation; the slides assert the conclusion only.

## Relation to Autoencoders

A linear [[Autoencoders|autoencoder]] with tied weights and no bias —

$$E(X) = W^TX, \qquad D(E(X)) = WW^TX$$

— minimizing mean squared error solves exactly the problem PCA solves, with optimum at $W = G$. The notes' summary:

> PCA is a special case of autoencoders, where the encoder and decoder are both **one-layer linear transformations, which share the weights and do not have bias terms.**

Gradient descent on such an autoencoder reaches the **same minimal reconstruction error**, but not necessarily the same $W$ — the two differ by an orthogonal matrix, which is the non-uniqueness from the Ky Fan solution reappearing. Replace the linear encoder with a nonlinear network and you leave PCA behind entirely; that is what makes a deep autoencoder more than PCA.

## See Also

- [[Singular Value Decomposition]]
- [[Eigendecomposition]]
- [[Autoencoders]]
- [[Unsupervised Learning]]
- [[Curse of Dimensionality]]
- [[Deep Learning]]
- [[CSCE 421]]
