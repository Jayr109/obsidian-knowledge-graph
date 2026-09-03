---
title: "Unsupervised Learning"
type: concept
tags: [csce420, unsupervised, clustering, pca, dimensionality-reduction, redundancy]
sources: [csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
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

## See Also

- [[Self-Organizing Map]]
- [[Machine Learning Paradigms]]
- [[Curse of Dimensionality]]
- [[Inductive Bias]]
- [[CSCE 420]]
