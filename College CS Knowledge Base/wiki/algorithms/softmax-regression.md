---
title: "Softmax Regression"
type: algorithm
tags: [csce421, softmax, multi-class, cross-entropy, shift-invariance, multinomial-logistic-regression]
sources: [csce421-t03-softmax-regression, csce421-t03-softmax-regression-notes]
course: CSCE 421
updated: 2026-08-25
---

Softmax regression (multi-class logistic regression) generalizes [[Logistic Regression]] from two classes to $K$, replacing the [[Sigmoid Function]] with the [[Softmax Function]] over $K$ linear signals and training with [[Cross-Entropy Loss]]. Binary logistic regression turns out to be exactly its $K=2$ case.

## Setup

Given $\mathcal{D} = (\mathbf{x}_1,y_1),\dots,(\mathbf{x}_N,y_N)$ with $\mathbf{x}_i \in \mathbb{R}^{d+1}$ and $y_i \in \{1,2,\dots,K\}$, estimate the full distribution over classes:

$$h_\mathbf{w}(\mathbf{x}) = \begin{bmatrix}P(y=1\mid\mathbf{x};\mathbf{w})\\ \vdots\\ P(y=K\mid\mathbf{x};\mathbf{w})\end{bmatrix}$$

**Critical assumption**: no ordinal relationship between classes. Classes are unordered labels, not magnitudes — which is why each needs its own weight vector rather than a shared scale.

## Hypothesis

Compute $K$ linear signals $\mathbf{w}_k^T\mathbf{x}$, then map $\mathbb{R}^K$ to a probability distribution:

$$h_\mathbf{w}(\mathbf{x}) = \mathrm{softmax}\begin{bmatrix}\mathbf{w}_1^T\mathbf{x}\\ \vdots\\ \mathbf{w}_K^T\mathbf{x}\end{bmatrix} = \frac{1}{\sum_{k=1}^{K}e^{\mathbf{w}_k^T\mathbf{x}}}\begin{bmatrix}e^{\mathbf{w}_1^T\mathbf{x}}\\ \vdots\\ e^{\mathbf{w}_K^T\mathbf{x}}\end{bmatrix}$$

**Only $K-1$ of the $K$ weight vectors are independent**, because the outputs must sum to one. This is precisely why binary problems need only a single weight vector.

## Loss

Cross-entropy between the one-hot true distribution $P$ and the predicted $Q$. For a sample in true class $c$:

$$\mathrm{loss}(\mathbf{x},y;\mathbf{w}) = H(\mathbf{y},\hat{\mathbf{y}}) = -\sum_k y_k\log\hat{y}_k = -\log\hat{y}_c = -\log\frac{e^{\mathbf{w}_c^T\mathbf{x}}}{\sum_{k=1}^{K}e^{\mathbf{w}_k^T\mathbf{x}}}$$

Because the true distribution is one-hot, every term but the correct class vanishes — **cross-entropy loss maximizes the log probability of the correct class**. Over the dataset:

$$\mathrm{loss}(X,Y;\mathbf{w}) = -\sum_{i=1}^{N}\sum_{k=1}^{K}\mathbb{I}[y_i = k]\log\frac{e^{\mathbf{w}_k^T\mathbf{x}_i}}{\sum_{j=1}^{K}e^{\mathbf{w}_j^T\mathbf{x}_i}}$$

## Property 1 — Shift-Invariance in Parameters

Subtracting the same vector $\mathbf{u}$ from every weight vector leaves the output unchanged.

**Proof.** With $\mathbf{w}_i' = \mathbf{w}_i - \mathbf{u}$:

$$P(y=k\mid\mathbf{x};\mathbf{w}') = \frac{e^{(\mathbf{w}_k-\mathbf{u})^T\mathbf{x}}}{\sum_i e^{(\mathbf{w}_i-\mathbf{u})^T\mathbf{x}}} = \frac{e^{\mathbf{w}_k^T\mathbf{x}}e^{-\mathbf{u}^T\mathbf{x}}}{\left(\sum_i e^{\mathbf{w}_i^T\mathbf{x}}\right)e^{-\mathbf{u}^T\mathbf{x}}} = P(y=k\mid\mathbf{x};\mathbf{w}) \qquad \blacksquare$$

The common factor cancels. This makes the "$K-1$ independent vectors" claim precise: the parameterization is over-complete by exactly one vector's worth of freedom.

## Property 2 — Equivalence to Sigmoid at $K=2$

Using shift-invariance to subtract $\mathbf{w}_1$ from both weight vectors:

$$h_\mathbf{w}(\mathbf{x}) = \frac{1}{e^{\mathbf{w}_1^T\mathbf{x}}+e^{\mathbf{w}_2^T\mathbf{x}}}\begin{bmatrix}e^{\mathbf{w}_1^T\mathbf{x}}\\ e^{\mathbf{w}_2^T\mathbf{x}}\end{bmatrix} = \begin{bmatrix}\frac{1}{1+e^{-\hat{\mathbf{w}}^T\mathbf{x}}}\\ 1-\frac{1}{1+e^{-\hat{\mathbf{w}}^T\mathbf{x}}}\end{bmatrix} = \begin{bmatrix}h_{\hat{\mathbf{w}}}(\mathbf{x})\\ 1-h_{\hat{\mathbf{w}}}(\mathbf{x})\end{bmatrix}$$

where $\hat{\mathbf{w}} = \mathbf{w}_1 - \mathbf{w}_2$. The two-class softmax *is* the sigmoid.

A companion chain shows $\arg\min_\mathbf{w}E_{in}(\mathbf{w})$ for the logistic loss equals $\arg\min_\mathbf{w}H(\{p,1-p\},\{q,1-q\})$ with $p = \mathbb{I}[y_n = +1]$ and $q = h(\mathbf{x}_n)$ — so the two losses yield identical weights.

Together: **binary logistic regression is a particular case of multi-class logistic regression when $K=2$.**

## Gradient

Derived in [[CSCE 421 T03 Notes — Softmax Regression Derivations]]. Softmax derivative, unified by the Kronecker delta:

$$\frac{\partial p_i}{\partial a_j} = p_i\left(\delta_{ij} - p_j\right)$$

Composed with cross-entropy, everything collapses:

$$\frac{\partial L}{\partial a_k} = p_k - y_k$$

**Predicted minus true.** This clean gradient is the reason softmax and cross-entropy are always paired, and it feeds directly into [[Gradient Descent]].

## Road to Deep Learning

Replacing hand-designed $\mathbf{x}$ with a CNN or Transformer over images, text, or speech — while keeping softmax and cross-entropy as the output head — is the step to [[Deep Learning]]. The classifier head does not change; only where the features come from.

## See Also

- [[Logistic Regression]]
- [[Softmax Function]]
- [[Cross-Entropy Loss]]
- [[Gradient Descent]]
- [[Deep Learning]]
- [[CSCE 421 T03 Notes — Softmax Regression Derivations]]
- [[CSCE 421]]
