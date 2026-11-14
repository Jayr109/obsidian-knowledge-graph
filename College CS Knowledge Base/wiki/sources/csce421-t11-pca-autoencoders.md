---
title: "CSCE 421 T11 — Principal Component Analysis and Autoencoders"
type: source
tags: [lecture, csce421, pca, svd, eigendecomposition, autoencoders, dimensionality-reduction, unsupervised, linear-algebra]
sources: []
course: CSCE 421
updated: 2026-11-08
---

Topic deck 11 of [[CSCE 421]], by [[Shuiwang Ji]]. 32 slides, with a companion typed note — [[CSCE 421 T11 Notes — Principal Component Analysis and Autoencoders]] — carrying the same derivations plus two exercises. **The first unsupervised-learning topic in the course.** Builds the linear algebra from scratch, derives [[Principal Component Analysis|PCA]] twice (maximum variance, then minimum reconstruction error), and closes by proving PCA is a linear [[Autoencoders|autoencoder]].

Slide numbers match PDF pages exactly (footer reads "1 / 32" on page 1).

## Part 1 — Linear Algebra Refresher (slides 2–6)

Four slides adapted from Kenji Hiranabe's *The Art of Linear Algebra*, teaching the same products several ways. The point is not the arithmetic but the **column-combination reading**, which everything later depends on.

**Matrix times vector, two ways** (slide 2):

$$A\mathbf{x} = \begin{bmatrix}1&2\\3&4\\5&6\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix} = \begin{bmatrix}x_1+2x_2\\3x_1+4x_2\\5x_1+6x_2\end{bmatrix} = x_1\begin{bmatrix}1\\3\\5\end{bmatrix} + x_2\begin{bmatrix}2\\4\\6\end{bmatrix}$$

> At first, you learn (Mv1). But when you get used to viewing it as (Mv2), you can understand $A\mathbf{x}$ as **a linear combination of the columns of A**. Those products fill the **column space** of A denoted $\mathbf{C}(A)$. The solution space of $A\mathbf{x}=\mathbf{0}$ is the **nullspace** $\mathbf{N}(A)$.

Slide 3 does the mirror image for $\mathbf{y}A$ (a combination of A's **rows**). Slide 4 gives four readings of matrix × matrix, the fourth being the one that matters: *"Multiplication AB is broken down to a sum of rank 1 matrices."*

**Diagonal matrices** (slide 5): *"Applying a diagonal matrix from the right **scales each column**. Applying a diagonal matrix from the left **scales each row**. Burn this into your memories."*

**Pattern P4** (slide 6), the one the whole deck runs on:

$$U\Sigma V^T = \sigma_1\mathbf{u}_1\mathbf{v}_1^T + \sigma_2\mathbf{u}_2\mathbf{v}_2^T + \sigma_3\mathbf{u}_3\mathbf{v}_3^T$$

> A matrix is broken down to a **sum of rank 1 matrices**, as in singular value/eigenvalue decomposition.

## Part 2 — Orthogonal Matrices and Eigen-Decomposition (slides 7–9)

**Orthogonal matrices** (slide 7): $Q^TQ = QQ^T = I$, hence $Q^{-1} = Q^T$ — *"a very useful property as it provides an easy way to compute the inverse."*

The subtlety worth noting, stated as point 4: for a **partial** set of columns $Q_1 = [q_1,\dots,q_i]$ and $Q_2 = [q_{i+1},\dots,q_n]$,

$$Q_1^TQ_1 = I, \quad Q_2^TQ_2 = I, \quad\text{but}\quad Q_1Q_1^T \ne I, \quad Q_2Q_2^T \ne I$$

This asymmetry is used directly in the reconstruction proof on slide 26.

**Eigen-decomposition** (slide 8):

$$S = Q\Lambda Q^{-1}, \qquad\text{and if } S \text{ is symmetric}, \quad S = Q\Lambda Q^T$$

> Note that **only diagonalizable matrices** can be factorized in this way. If $S$ is a symmetric matrix, its eigenvectors are orthogonal.

Slide 9 shows the spectral form: $S = \lambda_1 P_1 + \lambda_2 P_2 + \lambda_3 P_3$ with $P_i = q_iq_i^T$, noting $P_1+P_2+P_3 = I$ and $P_iP_j = O$ for $i \ne j$. See [[Eigendecomposition]].

## Part 3 — Singular Value Decomposition (slides 10–15)

$$R = U\tilde{\Sigma}V^T, \qquad \sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_n \ge 0$$

with $U$ orthogonal $m\times m$, $V$ orthogonal $n\times n$, and $\tilde\Sigma$ diagonal $m \times n$. If $\mathrm{rank}(R) = r$ then $\sigma_1 \ge \cdots \ge \sigma_r > 0$ and the rest are zero.

**Relation to eigen-decomposition** (slide 12) — the link PCA is built on:

> The columns of $U$ (left-singular vectors) are orthonormal eigenvectors of $RR^T$, and the columns of $V$ (right-singular vectors) are orthonormal eigenvectors of $R^TR$.

$$R^TR = V\Sigma^2V^T, \qquad RR^T = U\begin{bmatrix}\Sigma^2 & 0\\0&0\end{bmatrix}U^T$$

**Slide 13 poses three questions** rather than answering them, which marks them as likely exam material:

> 1. Under what conditions are SVD and eigen-decomposition the same? **First, $R$ is symmetric. Second, $R$ is positive semi-definite.**
> 2. The diagonal entries of $\Lambda$ **can be negative**, while those of $\Sigma$ are **non-negative**. What are the fundamental reasons underlying this difference?
> 3. Why do the requirements on the singular values (non-negative and sorted) not prevent the generality of SVD?

**Compact SVD** (slide 14) drops the zero components: $R = U_r\Sigma_rV_r^T = \sum_{i=1}^{r}\sigma_i u_i v_i^T$.

**Truncated SVD and best low-rank approximation** (slide 15) — the result PCA's optimality rests on:

$$R_k = \sum_{i=1}^{k}\sigma_iu_iv_i^T$$

$$\min_{B:\mathrm{rank}(B)\le k}\lVert R-B\rVert_F = \lVert R - R_k\rVert_F = \sqrt{\sum_{i=k+1}^{n}\sigma_i^2}, \qquad \min_{B:\mathrm{rank}(B)\le k}\lVert R-B\rVert_2 = \sigma_{k+1}$$

> $R_k$ is the **best rank-k approximation** to $R$ in terms of **both** the Frobenius norm and spectral norm. Note the difference in terms of approximation errors when different matrix norms are used.

See [[Singular Value Decomposition]].

## Part 4 — PCA (slides 16–27)

### What it is (slide 16)

> PCA is a statistical procedure that can be used to achieve **feature (dimensionality) reduction**.
>
> Note, **feature reduction is different from feature selection**. After feature reduction, we still use all the features, while feature selection selects a subset of features to use.
>
> The goal is to project the high-dimensional features to a lower-dimensional space with **maximal variance** and **minimum reconstruction error simultaneously**. We derive PCA based on maximizing variance, and then we show the solution also minimizes reconstruction error.
>
> In machine learning, PCA is an **unsupervised learning technique**, and therefore **does not need labels**.

The feature-reduction / feature-selection distinction is a clean one-line exam question.

### PCA to 1D (slides 17–18)

Given $x_1,\dots,x_n \in \mathbb{R}^p$ and a unit projection $a$ with $a^Tx_i = z_i$:

$$a^* = \arg\max_{\lVert a\rVert = 1} \frac{1}{n}\sum_{i=1}^{n}(z_i - \bar{z})^2$$

Slide 18 is the derivation, and it is short enough to reproduce on an exam. Using $\bar{z} = a^T\bar{x}$:

$$a^* = \arg\max_{\lVert a\rVert=1}\frac{1}{n}\sum_i (a^Tx_i - a^T\bar{x})^2 = \arg\max_{\lVert a\rVert=1} a^T\underbrace{\left(\frac{1}{n}\sum_i (x_i-\bar{x})(x_i-\bar{x})^T\right)}_{p\times p \text{ covariance matrix}}a = \arg\max_{\lVert a\rVert=1} a^TCa$$

### PCA to k dimensions (slide 19)

$$A^* = \arg\max_{A\in\mathbb{R}^{p\times k}:\,A^TA = I_k} \mathrm{trace}\left(A^TCA\right) \tag{2}$$

> PCA requires different projection vectors to be **orthogonal**. The trace is the **sum of the variances** after projecting onto each of the $k$ directions: $\mathrm{trace}(A^TCA) = \sum_{i=1}^{k}(a_i^TCa_i)$.

### Ky Fan Theorem (slide 20)

> **Theorem (Ky Fan).** Let $H\in\mathbb{R}^{n\times n}$ be symmetric with eigenvalues $\lambda_1 \ge \cdots \ge \lambda_n$ and eigenvectors $U = [u_1,\dots,u_n]$. Then
>
> $$\lambda_1 + \cdots + \lambda_k = \max_{A\in\mathbb{R}^{n\times k}:A^TA=I_k}\mathrm{trace}(A^THA)$$
>
> And the optimal $A^*$ is given by $A^* = [u_1,\dots,u_k]Q$ with $Q$ an **arbitrary orthogonal matrix**.

### Solution (slide 21)

$C$ is symmetric, so the theorem applies directly: $A^* = [u_1,\dots,u_k]Q$ where the $u_i$ are eigenvectors of $C$ for its $k$ largest eigenvalues.

> It also follows that **solutions to PCA are not unique**, and they differ by an orthogonal matrix. We used the special case where $Q = I$.

### Computing it efficiently (slides 22–23)

With $\tilde{X} = X - \bar{X}\mathbf{1}_n^T$ the centered data,

$$C = \frac{1}{n}\tilde{X}\tilde{X}^T \in \mathbb{R}^{p\times p}$$

> If $p$ is large, it is **very costly to compute eigenvectors of $C$ directly**. Moreover, if $p \gg n$, there are known computational problems.

The fix is SVD, since the columns of $U$ in $\tilde X = U\tilde\Sigma V^T$ are already the eigenvectors of $\tilde X \tilde X^T$:

$$X \to \tilde{X} \to \tilde{X} = U\tilde\Sigma V^T \to G = U_k \in\mathbb{R}^{p\times k}, \qquad G^T\tilde{X} = Z \in\mathbb{R}^{k\times n} \tag{3}$$

> The $k$-th **row** in $Z$ is called the $k$-th **principal component (PC)**.

### Centered or not? (slide 24)

> Maximal variance can be achieved in **both** cases, as the covariance matrix $C$ will not change. But the **minimal reconstruction error can only be achieved when $\tilde X$ is used**.
>
> A common practice to avoid any confusion is to **center the data before applying PCA**.

### Minimum reconstruction error (slides 25–27)

Reconstruct via $\check{X} = GZ = GG^T\tilde{X}$. The claim to prove:

$$GG^T\tilde{X} = B^* = \arg\min_{B:\mathrm{rank}(B)\le k}\lVert \tilde{X}-B\rVert_F \tag{4}$$

Slide 26's chain shows $GG^T\tilde X$ *is* the truncated SVD:

$$GG^T\tilde X = U_kU_k^TU\tilde\Sigma V^T = U_kU_k^T[U_k\;\; U_{-k}]\tilde\Sigma V^T = U_k[I\;\;0]\tilde\Sigma V^T = U_k\Sigma_kV_k^T = \sum_{i=1}^{k}\sigma_iu_iv_i^T$$

so by the slide-15 result the error is $\sqrt{\sum_{i=k+1}^n \sigma_i^2}$, and likewise $\sigma_{k+1}$ in spectral norm.

> Therefore, PCA projects the high-dimensional features to a lower-dimensional space with **minimum reconstruction error in terms of both Frobenius and spectral norms.**

**Both goals from slide 16 are now proved**, which is the architecture of the whole deck.

## Part 5 — Autoencoders (slides 28–31)

An encoder $E(\cdot)$ and decoder $D(\cdot)$ with the output reconstructing the input:

> Without any constraint, the reconstruction task can be easily solved by **directly copying**. However, autoencoders come with a crucial restriction that **the dimension of intermediate outputs should be smaller than inputs.**

$$\min\; L\big(X,\, D(E(X))\big)$$

### PCA as an autoencoder (slides 30–31)

Take a **linear** autoencoder with tied weights and no bias:

$$E(X) = W^TX \in\mathbb{R}^{k\times n}, \qquad D(E(X)) = WW^TX \in\mathbb{R}^{p\times n}, \qquad W\in\mathbb{R}^{p\times k}$$

With mean-squared-error loss the objective is

$$\min_{W:\mathrm{rank}(WW^TX)\le k}\lVert X - WW^TX\rVert_F \tag{5}$$

> Comparing Eqn. (4) and Eqn. (5), it is easy to see that **the optima can be achieved when $W = G$**, where $G$ is given by PCA.
>
> If the hidden units in autoencoders have **linear activation functions**, then the error function has a **unique global minimum**, and at this minimum the network performs a projection onto the subspace spanned by the principal components.
>
> Thus the vectors of weights leading into the hidden units form a **basis set that spans the principal subspace**. Note, however, that these vectors **need not be orthogonal or normalized** (Bishop DL book: Section 19.1.1).

That last caveat is the same non-uniqueness from slide 21 — PCA solutions differ by an orthogonal matrix, and gradient descent has no reason to land on the orthonormal one.

## See Also

- [[Principal Component Analysis]]
- [[Singular Value Decomposition]]
- [[Eigendecomposition]]
- [[Autoencoders]]
- [[Unsupervised Learning]]
- [[CSCE 421 T11 Notes — Principal Component Analysis and Autoencoders]]
- [[CSCE 421]]
- [[Shuiwang Ji]]
