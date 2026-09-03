---
title: "Cross-Entropy Loss"
type: concept
tags: [csce421, cross-entropy, loss-function, one-hot, maximum-likelihood, information-theory]
sources: [csce421-t02-logistic-regression, csce421-t03-softmax-regression, csce421-t03-softmax-regression-notes]
course: CSCE 421
updated: 2026-08-25
---

Cross-entropy measures the distance between two probability distributions, and is the standard loss for probabilistic classifiers. In [[CSCE 421]] it is the error measure for both [[Logistic Regression]] and [[Softmax Regression]] — derived from [[Maximum Likelihood Estimation]] rather than assumed.

## Definition

For a true distribution $P = (p_1,\dots,p_K)$ and a predicted distribution $Q = (q_1,\dots,q_K)$:

$$H(P,Q) = -\sum_{i=1}^{K}p_i\log(q_i)$$

In classification, $P$ is the **one-hot encoding** of the true label — a vector with 1 at the correct class index and 0 everywhere else — and $Q$ is the model's predicted vector.

## The One-Hot Collapse

Because $P$ is one-hot, every term but the true class $c$ multiplies by zero:

$$H(\mathbf{y},\hat{\mathbf{y}}) = -\sum_k y_k\log\hat{y}_k = -\log\hat{y}_c$$

Summarized in one sentence: **cross-entropy loss maximizes the log probability of the correct class.** The loss only ever looks at what probability the model assigned to the right answer.

## Binary Form

For binary [[Logistic Regression]] with $y_n = \pm 1$, cross-entropy takes the compact form

$$E_{in}(\mathbf{w}) = \frac{1}{N}\sum_{n=1}^{N}\ln\left(1+e^{-y_n\mathbf{w}^T\mathbf{x}_n}\right)$$

which looks unlike the definition above, but is exactly it — the T03 equivalence proof shows $\arg\min$ of this equals $\arg\min$ of $H(\{p,1-p\},\{q,1-q\})$ with $p = \mathbb{I}[y_n=+1]$ and $q = h(\mathbf{x}_n)$.

## Multi-Class Form

$$\mathrm{loss}(X,Y;\mathbf{w}) = -\sum_{i=1}^{N}\sum_{k=1}^{K}\mathbb{I}[y_i=k]\log\frac{e^{\mathbf{w}_k^T\mathbf{x}_i}}{\sum_{j=1}^{K}e^{\mathbf{w}_j^T\mathbf{x}_i}}$$

## Why Cross-Entropy and Not Squared Error

Two independent reasons, both given in lecture:

1. **It is derived, not chosen.** Maximizing likelihood is *equivalent* to minimizing cross-entropy — the loss falls out of the probabilistic model rather than being imposed. See [[Maximum Likelihood Estimation]].
2. **It is convex and easy to minimize.** Squared error composed with a sigmoid is non-convex; the lecture's blunt assessment of the squared-error version is "not very convenient (hard to minimize)." Cross-entropy looks uglier — $\ln$, $e^{(\cdot)}$ — but is mathematically friendly.

## The Gradient Is Why It Is Paired With Softmax

Composed with [[Softmax Function|softmax]], the gradient with respect to the pre-softmax logits collapses to

$$\frac{\partial L}{\partial a_k} = p_k - y_k$$

**Predicted minus true** — all the $\delta_{ij}$ terms from the softmax Jacobian cancel. Derivation in [[CSCE 421 T03 Notes — Softmax Regression Derivations]]. The same $\hat{y}-y$ shape appears in [[Linear Regression]]'s normal-equation gradient, which is why one optimizer serves all of them.

## See Also

- [[Softmax Function]]
- [[Sigmoid Function]]
- [[Logistic Regression]]
- [[Softmax Regression]]
- [[Maximum Likelihood Estimation]]
- [[Gradient Descent]]
- [[CSCE 421]]
