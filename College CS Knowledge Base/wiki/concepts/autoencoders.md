---
title: "Autoencoders"
type: concept
tags: [csce420, csce421, autoencoders, self-supervised, compression, embeddings, neural-networks, pca, reconstruction-error, vae]
sources: [csce420-sp26-0331-backprop-ii-recorded-lecture, csce420-sp26-0406-demos-autoencoders-srn-genetic-algorithms, csce421-t11-pca-autoencoders, csce421-t11-pca-notes]
course: CSCE 420, CSCE 421
updated: 2026-11-08
---

An **autoencoder** is a feed-forward network trained to reproduce its own input: copy the input column of the dataset into the target column and run ordinary [[Backpropagation]]. Nothing else changes — same architecture, same learning rule.

## Why It Counts as Self-Supervised

The original data has no labels, so the raw task looks **unsupervised**. But once the input is copied to the target, *"the task itself becomes a supervised learning task, although the target is just the same as the input."* The standard name is **self-supervised** — the supervision signal is manufactured from the data.

## The Bottleneck Is the Point

A 10×10 image flattened to 100 inputs → **a few hidden units** (3 in the lecture example, 10 in the slide) → 100 outputs. If the network can reproduce thousands of training images through that bottleneck, then every image has been reduced to a handful of real numbers.

| Stage | Weights used | Result |
|---|---|---|
| **Encode** | input → hidden | the compact code (e.g. 10 numbers for a 100-pixel image — 10× compression) |
| transmit / store | — | only the code travels |
| **Decode** | hidden → output | reconstruction of the original image |

## Embeddings

The compression view is the historical motivation; the modern reason autoencoders matter is that the hidden code *"distills the features in the input"* — it is an **embedding**. The same idea underlies the hidden vectors of [[Convolutional Neural Networks]] and the pretraining of [[Large Language Models]], where masked-token prediction is another way of manufacturing a self-supervised target.

---

# The CSCE 421 Treatment

The section above is the [[CSCE 420]] survey. [[CSCE 421 T11 — Principal Component Analysis and Autoencoders|T11]] arrives at autoencoders from the opposite direction — it spends 27 slides deriving [[Principal Component Analysis|PCA]], then shows PCA **is** a linear autoencoder.

## The Framework

$$\min\; L\big(X,\, D(E(X))\big), \qquad E(X)\in\mathbb{R}^{k\times n},\; k < p$$

> Without any constraint, the reconstruction task can be easily solved by **directly copying**. However, autoencoders come with a crucial restriction that **the dimension of intermediate outputs should be smaller than inputs.**

The bottleneck is not a design preference — without it the objective is trivially satisfiable and nothing is learned. This is the same point the 420 survey makes as "the bottleneck is the point", stated as a constraint on the optimization.

## PCA Is a Linear Autoencoder

Take an encoder and decoder that are single linear maps sharing one weight matrix, with no bias:

$$E(X) = W^TX \in\mathbb{R}^{k\times n}, \qquad D(E(X)) = WW^TX \in\mathbb{R}^{p\times n}, \qquad W\in\mathbb{R}^{p\times k}$$

Since $\mathrm{rank}(WW^TX) \le k$, minimizing mean squared error gives

$$\min_{W:\,\mathrm{rank}(WW^TX)\le k}\lVert X - WW^TX\rVert_F$$

which is **character for character** the problem PCA was just shown to solve, with optimum at $W = G = U_k$. The notes' one-sentence summary:

> PCA is a special case of autoencoders, where the encoder and decoder are both **one-layer linear transformations, which share the weights and do not have bias terms.**

Each clause is load-bearing — one layer, linear, tied weights, no bias. Relax any of them and the equivalence fails.

## Does Gradient Descent Recover PCA?

The notes ask this directly and answer it in two parts:

> **Yes in terms of the minimal reconstruction error, and not necessarily in terms of optimal $W$.**

Gradient descent reaches the same global minimum error. But PCA's solution is only defined up to an orthogonal matrix (the $Q$ in the Ky Fan theorem), so the $W$ it lands on need not be the eigenvector basis:

> If the hidden units have **linear activation functions**, the error function has a **unique global minimum**, and at this minimum the network performs a projection onto the subspace spanned by the principal components… Note, however, that these vectors **need not be orthogonal or normalized.**

So the network finds the **right subspace** but not necessarily a tidy basis for it. The sets of possible solutions are identical; one is reachable from another by an orthogonal transformation.

## Why This Framing Matters

It locates autoencoders on a spectrum rather than presenting them as a separate idea:

| Encoder/decoder | What you get |
|---|---|
| one linear layer, tied weights, no bias | exactly PCA |
| deeper, still linear | still the principal subspace — depth alone buys nothing |
| **nonlinear activations** | genuinely beyond PCA — curved manifolds, not just subspaces |

The nonlinearity is what makes a deep autoencoder more than a slow way to compute eigenvectors — the same lesson as [[Multilayer Perceptron]], where stacking linear layers collapses to one.

The companion notes also place the wider family: word2vec as an autoencoder variant, and **variational autoencoders (VAE)** and **generative adversarial networks (GAN)** as the generative descendants.

## See Also

- [[Principal Component Analysis]]
- [[Singular Value Decomposition]]
- [[Unsupervised Learning]]

- [[Neural Networks]]
- [[Backpropagation]]
- [[Large Language Models]]
- [[CSCE 420 Spring 2026 — 03-31 Backprop II, Recorded Lecture]]
- [[CSCE 420 Spring 2026 — 04-06 Demos, Autoencoders, SRN, Genetic Algorithms]]
