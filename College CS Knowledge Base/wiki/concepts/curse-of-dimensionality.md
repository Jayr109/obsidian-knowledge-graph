---
title: "Curse of Dimensionality"
type: concept
tags: [csce420, dimensionality, sample-complexity, generalization]
sources: [csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

Sample requirements grow **exponentially** with the number of feature dimensions. This is the structural reason high-dimensional learning is hard, and why it cannot be fixed by collecting somewhat more data.

## The Arithmetic

To cover 10 different values per feature dimension:

| Dimensions | Samples needed |
|---|---|
| 1-D | $10^1 = 10$ |
| 2-D | $10^2 = 100$ |
| 3-D | $10^3 = 1{,}000$ |

The pattern continues: $10^d$ for $d$ dimensions.

## Why It Matters Here

Recall from [[Machine Learning]] that a $50 \times 50$ image is a **2,500-dimensional** vector, and real data reaches a million dimensions. At $10^{2500}$ samples for even coarse coverage, the requirement is not merely large but **physically meaningless** — vastly more than the number of atoms in the universe.

So dense coverage of the input space is permanently off the table. Any method that works in high dimensions must exploit **structure** — that real data occupies a thin, low-dimensional region of the space rather than filling it. That assumption is what dimensionality-reduction methods in [[Unsupervised Learning]] (PCA, [[Self-Organizing Map|SOM]], t-SNE) are built to find, and what makes [[Deep Learning]]'s learned representations valuable.

## See Also

- [[Supervised Learning Issues]]
- [[Machine Learning]]
- [[Unsupervised Learning]]
- [[Inductive Bias]]
- [[CSCE 420]]
