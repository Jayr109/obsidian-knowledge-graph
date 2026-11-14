---
title: "Unsupervised Learning"
type: concept
tags: [csce420, unsupervised, clustering, pca, dimensionality-reduction, redundancy]
sources: [csce420-lecture-06-machine-learning, csce421-t11-pca-autoencoders]
course: CSCE 420, CSCE 421
updated: 2026-11-08
---

Unsupervised learning receives **no teacher signal** — just a set of unlabeled inputs $\{\vec{x}_i\}$. The network must discover patterns, features, regularities, correlations, or categories in the data and encode them in its output, displaying some degree of **self-organization**.

## The Redundancy Condition

> Unsupervised learning can be useful when there is **redundancy** in the input data. A data channel where the input content is less than the channel capacity has redundancy.

This is the precise statement of when unsupervised learning is possible at all. If the data filled its space uniformly there would be no structure to find. Redundancy *is* the structure — and connects directly to the [[Curse of Dimensionality]]: high-dimensional data is learnable only because it does not actually fill its space.

## Six Things It Can Do

| Capability | Description |
|---|---|
| **Familiarity** | How similar is the current input to past inputs? |
| **Principal Component Analysis** | Find orthogonal basis vectors to project high-dimensional data onto |
| **Clustering** | $n$ output classes, each a distinct category; nearby patterns share a class |
| **Prototyping** | For a given input, determine the most similar output class or exemplar |
| **Encoding** | An application of clustering/prototyping |
| **Feature mapping** | Topographic mapping of input space onto the output network configuration |

The last is what [[Self-Organizing Map|SOM]] does, and what distinguishes it from plain clustering: the *arrangement* of the output units carries information.

## Methods Listed

Principal Component Analysis (PCA), [[Self-Organizing Map|Self-Organizing Maps]], Independent Component Analysis (ICA), Multi-Dimensional Scaling (MDS), ISOMAP, Locally Linear Embedding (LLE), and t-distributed Stochastic Neighbor Embedding (t-SNE).

## The Open Issues

- Discovering structure; discovering features; removing redundancy
- **How many clusters?**
- **What distance measure to use?**

Both questions are unanswerable from the data alone — they are choices, and therefore a form of [[Inductive Bias]]. This is the characteristic difficulty of unsupervised learning: with no target, there is no unambiguous notion of a correct answer.


## In CSCE 421

[[CSCE 421]] is a supervised-learning course through its first ten decks — every model from [[Linear Regression]] to [[Transformers]] is trained against labels. **[[CSCE 421 T11 — Principal Component Analysis and Autoencoders|T11]] is the first unsupervised topic**, and it states the property plainly: PCA *"is an unsupervised learning technique, and therefore does not need labels."*

Two methods are covered, and the deck proves they are the same method:

- **[[Principal Component Analysis]]** — project onto the subspace of maximal variance, which is also the subspace of minimal reconstruction error
- **[[Autoencoders]]** — learn an encoder and decoder that reconstruct the input through a bottleneck

PCA turns out to be a linear autoencoder with tied weights and no bias. Both are **dimensionality reduction** by the definition this page gives, and both exploit exactly the redundancy condition above — if the data had no redundant structure, no lower-dimensional projection could reconstruct it.

## See Also

- [[Self-Organizing Map]]
- [[Machine Learning Paradigms]]
- [[Principal Component Analysis]]
- [[Autoencoders]]
- [[Curse of Dimensionality]]
- [[Inductive Bias]]
- [[CSCE 420]]
