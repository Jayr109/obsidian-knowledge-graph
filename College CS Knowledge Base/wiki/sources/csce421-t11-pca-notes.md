---
title: "CSCE 421 T11 Notes — Principal Component Analysis and Autoencoders"
type: source
tags: [notes, csce421, pca, svd, autoencoders, exercises, ky-fan, reconstruction-error]
sources: []
course: CSCE 421
updated: 2026-11-08
---

Companion typed note to [[CSCE 421 T11 — Principal Component Analysis and Autoencoders]]. 8 pages, by **Shuiwang Ji**, **Zhengyang Wang** and **Ying Wei** (all Texas A&M). Stated aim:

> This introduction of PCA aims at providing a **complete, self-contained, and easy-to-understand** introduction of PCA. The only required background would be **college-level linear algebra**.

Unlike the [[CSCE 421 T05 Notes — A Unified View of Loss Functions|T05 note]], which merely restated its slides, **this one carries material the deck does not** — and it ends with exercises.

## What the Note Adds

Three things are in the note and not on the slides.

### 1. Reconstructing the *uncentered* data (§4.3, second half)

The slides prove minimum reconstruction error for the centered $\tilde X$ and stop. The note then repeats the verification for the original $X$ and confronts the apparent failure:

$$\hat{X} = GG^TX, \qquad\text{but}\qquad GG^TX \ne B^* = \arg\min_{B:\mathrm{rank}(B)\le k}\lVert X - B\rVert_F$$

> This is because $GG^TX$ is **not the truncated SVD of $X$** (note the difference here: $G$ is computed from the SVD of $\tilde X$).

Does that mean PCA fails here? No — the note decomposes the error:

$$\lVert X - \hat{X}\rVert_F = \lVert (\tilde{X} + \bar{X}) - GG^T(\tilde{X}+\bar{X})\rVert_F = \lVert (\tilde{X} - GG^T\tilde{X}) + (\bar{X} - GG^T\bar{X})\rVert_F$$

> The term $(\bar X - GG^T\bar X)$ represents the difference between the original **mean matrix** and the reconstructed mean matrix. However, the mean matrix is **an offset term in the projection and should not be considered** when computing the reconstruction error.
>
> To conclude, to show that PCA projects data with minimum reconstruction error, **we should center the data first.**

This is the full justification for slide 24's "center the data" advice, which the deck asserts without proof.

### 2. Will gradient descent give the same result as PCA? (§5.2)

The slides note the optimum is reached at $W = G$ and leave it there. The note asks the obvious follow-up and answers it precisely:

> The answer is **two-fold: yes in terms of the minimal reconstruction error and not necessary in terms of optimal $W$.**
>
> Gradient descent converges to the global optima, resulting in the **same minimal reconstruction error** as PCA. However, the solutions to PCA are **not unique and can differ by an orthogonal matrix**. Thus the optimal $W$ can be different from a PCA solution $G$. But **one can be computed from another through an orthogonal matrix and the sets of possible solutions are the same.**

And the summary sentence worth memorizing:

> **PCA is a special case of autoencoders, where the encoder and decoder are both one-layer linear transformations, which share the weights and do not have bias terms.**

Every clause in that sentence is doing work — *one-layer*, *linear*, *shared weights*, *no bias*. Drop any one and the equivalence breaks.

### 3. Wider autoencoder context (§5.1)

> Variants of autoencoders have been used to learn embeddings of data. For example, in natural language processing, word embedding models like **word2vec** can be seen as a variant of autoencoders. In addition, other variants have achieved great successes in data generation, like **variational autoencoders (VAE)** and **generative adversarial networks (GAN)**. Here, we discuss the original autoencoders.

## Exercises (§6)

**Two exercises, neither with a solution given.** Worth attempting — the first is a direct test of the slide-13 questions.

**6.1 — Eigen-decomposition and SVD.** Given a symmetric $A\in\mathbb{R}^{3\times3}$ with eigen-decomposition

$$A = U\begin{pmatrix}3&0&0\\0&1&0\\0&0&-2\end{pmatrix}U^T$$

> What is the singular value decomposition of this matrix?

The point is the **negative eigenvalue**. Singular values must be non-negative and sorted, so $\sigma = (3, 2, 1)$ — the eigenvalue $-2$ contributes $|-2| = 2$, the sign is absorbed by flipping the corresponding singular vector, and the columns must be reordered since $2 > 1$. This is exactly slide 13's second question made concrete.

**6.2 — Ky Fan Theorem.** *"Provide a complete proof of the Ky Fan Theorem."* The deck states the theorem (slide 20) and uses it without proof, so this fills the gap deliberately left.

## Content Index

| Section | Content |
|---|---|
| 2.1 | Orthogonal matrix |
| 2.2 | Eigen-decomposition |
| 3.1–3.4 | SVD: definition, relation to eigen-decomposition, compact, truncated / best low-rank |
| 4.1 | What is PCA; 1D derivation; k-dimensional; Ky Fan; solution |
| 4.2 | How to compute PCA (the SVD route) |
| 4.3 | Minimum reconstruction error — **centered and uncentered** |
| 5.1–5.2 | Autoencoders; PCA as autoencoders |
| 6 | Exercises |

Everything in §2–§5 that overlaps the slides is reproduced on [[Principal Component Analysis]], [[Singular Value Decomposition]] and [[Eigendecomposition]].

## References Cited

- Hinton GE, Salakhutdinov RR (2006) *Reducing the dimensionality of data with neural networks.* Science 313: 504–507.
- Aggarwal CC (2018) *Neural Networks and Deep Learning: A Textbook.* Springer.

The acknowledgements credit **Jieping Ye** (University of Michigan) as the source of the SVD/PCA framing, and Lei Cai for proof-reading.

## See Also

- [[CSCE 421 T11 — Principal Component Analysis and Autoencoders]]
- [[Principal Component Analysis]]
- [[Singular Value Decomposition]]
- [[Autoencoders]]
- [[CSCE 421]]
