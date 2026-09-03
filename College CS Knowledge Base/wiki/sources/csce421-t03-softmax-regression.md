---
title: "CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class"
type: source
tags: [lecture, csce421, softmax, multi-class, cross-entropy, shift-invariance]
sources: []
course: CSCE 421
updated: 2026-08-25
---

Topic deck 3 of [[CSCE 421]], by [[Shuiwang Ji]]. 20 slides. Generalizes binary [[Logistic Regression]] to $K$ classes via the [[Softmax Function]], trains with [[Cross-Entropy Loss]], and proves two structural results: softmax is shift-invariant in its parameters, and the binary case is exactly the $K=2$ case of the multi-class one.

Companion typed notes with the full gradient derivations: [[CSCE 421 T03 Notes — Softmax Regression Derivations]].

## Recap and the Sigmoid's Three Properties

Binary LR predicts $y_i \in \{-1,+1\}$ by estimating $P(y\mid \mathbf{x}_i)$ and thresholding, with $P(y\mid\mathbf{x}) = \theta(y\mathbf{w}^T\mathbf{x})$.

The deck poses the [[Sigmoid Function]]'s three properties as a question — *why are they important?*

| Property | Why it matters |
|---|---|
| $0 < \theta(s) < 1$ for all $s$ | Probabilistic interpretation |
| $\theta(-s) = 1 - \theta(s)$ | Compact representation $P(y\mid\mathbf{x}) = \theta(y\mathbf{w}^T\mathbf{x})$ |
| $\theta$ is monotonic | Order preserved — it is still a linear model |

The slide closes by asking directly: *is logistic regression a linear model? Why?*

## Multi-Class Setup

Given $\mathcal{D} = (\mathbf{x}_1,y_1),\dots,(\mathbf{x}_N,y_N)$ with $\mathbf{x}_i \in \mathbb{R}^{d+1}$ and $y_i \in \{1,\dots,K\}$, estimate the probability of each class:

$$h_\mathbf{w}(\mathbf{x}) = \left[P(y=1\mid\mathbf{x};\mathbf{w}),\ \dots,\ P(y=K\mid\mathbf{x};\mathbf{w})\right]^T$$

**Critical assumption**: there is no ordinal relationship between the classes. So the model needs $K$ weight vectors $\mathbf{w}_k$ and computes $K$ linear signals $\mathbf{w}_k^T\mathbf{x}$ — then must map $\mathbb{R}^K$ to a probability distribution.

## Softmax

$$\mathrm{softmax}(\mathbf{v}) = \frac{1}{\sum_{k=1}^{K}e^{v_k}}\left[e^{v_1},\ e^{v_2},\ \dots,\ e^{v_K}\right]^T$$

It maps $\mathbb{R}^K$ into $(0,1)^K$ with elements summing to 1. Applying it to the $K$ signals gives the multi-class hypothesis.

Two consequences the deck draws out:

- Although there are $K$ vectors, **only $K-1$ are independent**, because of the sum-to-one constraint.
- That is *why binary problems need only one weight vector*.

## Cross-Entropy Training

A loss function measures error between predictions and true labels; here it must measure the distance between two probability distributions. For one sample,

$$H(P,Q) = -\sum_{i=1}^{K} p_i \log(q_i)$$

with $P$ the one-hot vector of the true class and $Q$ the softmax output. Because $P$ is one-hot, this collapses to $-\log \hat{y}_c$ for true class $c$ — summarized on a slide as: **the cross entropy loss maximizes the log probability of the correct class.**

Over all samples:

$$\mathrm{loss}(X,Y;\mathbf{w}) = -\sum_{i=1}^{N}\sum_{c=1}^{K}\mathbb{I}[y_i = c]\log\frac{e^{\mathbf{w}_c^T\mathbf{x}_i}}{\sum_{k=1}^{K}e^{\mathbf{w}_k^T\mathbf{x}_i}}$$

## Two Proofs

**Shift-invariance.** Subtracting the same $\mathbf{u}$ from every $\mathbf{w}_k$ leaves the softmax output unchanged — the factor $e^{-\mathbf{u}^T\mathbf{x}}$ appears in numerator and denominator and cancels. This is what makes the $K-1$ independence claim precise.

**Equivalence to sigmoid at $K=2$.** Using shift-invariance to subtract $\mathbf{w}_1$, the two-class softmax reduces to $\left[h_{\hat{\mathbf{w}}}(\mathbf{x}),\ 1-h_{\hat{\mathbf{w}}}(\mathbf{x})\right]$ with $\hat{\mathbf{w}} = \mathbf{w}_1 - \mathbf{w}_2$ — the sigmoid hypothesis.

A third chain shows minimizing the logistic loss equals minimizing binary cross-entropy, so the two objectives yield identical weights. Together: **binary LR is a special case of multi-class LR at $K=2$.**

## Derivatives and the Road to Deep Learning

The deck defers the gradient derivation to the notes, listing the only tools needed: univariate calculus, the chain rule, and $\partial(\mathbf{w}^T\mathbf{b})/\partial\mathbf{w} = \mathbf{b}$.

The closing slide replaces the hand-designed input $\mathbf{x}$ with a CNN or Transformer over images, text, or speech, keeping softmax and cross-entropy as the head — posing the question *how to learn $X$ automatically?* See [[Deep Learning]].

## See Also

- [[Softmax Regression]]
- [[Softmax Function]]
- [[Sigmoid Function]]
- [[Cross-Entropy Loss]]
- [[Logistic Regression]]
- [[CSCE 421 T03 Notes — Softmax Regression Derivations]]
- [[CSCE 421]]
