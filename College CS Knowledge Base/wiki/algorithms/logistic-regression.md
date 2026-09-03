---
title: "Logistic Regression"
type: algorithm
tags: [csce421, logistic-regression, sigmoid, cross-entropy, maximum-likelihood, binary-classification]
sources: [csce421-t02-logistic-regression, csce421-t03-softmax-regression]
course: CSCE 421
updated: 2026-08-25
---

Logistic regression passes the [[Linear Models|linear signal]] through the [[Sigmoid Function]] to produce a probability, and is trained by minimizing [[Cross-Entropy Loss]] with [[Gradient Descent]]. Despite the name it is a **classification** method — the lecture calls the name outright *wrong*: training data have discrete $y$, but the model makes probabilistic predictions.

## Hypothesis

$$h(\mathbf{x}) = \theta\!\left(\mathbf{w}^T\mathbf{x}\right), \qquad \theta(s) = \frac{1}{1+e^{-s}}$$

Motivating example: predict the probability of a heart attack in the next year from age, blood sugar, HDL, LDL, mass, and height. The output is $y \in [0,1]$.

## The Central Difficulty

The data is still binary, $y_n = \pm 1$. **We cannot measure a probability** — we only observe whether an event occurred and must infer a probability from it.

The target function being learned is

$$f(\mathbf{x}) = P[y = +1 \mid \mathbf{x}]$$

and the data gives only samples generated from it: $P(y=1\mid\mathbf{x}) = f(\mathbf{x})$, $P(y=-1\mid\mathbf{x}) = 1-f(\mathbf{x})$. This is why a proper error measure has to be argued for rather than assumed.

## Why Not Squared Error?

A hypothesis is good if $h(\mathbf{x}_n) \approx 1$ when $y_n = +1$ and $h(\mathbf{x}_n) \approx 0$ when $y_n = -1$. The direct encoding of that wish,

$$E_{in}(h) = \frac{1}{N}\sum_{n=1}^{N}\left(h(\mathbf{x}_n) - \tfrac{1}{2}(1+y_n)\right)^2$$

is correct but **hard to minimize** — squared error composed with a sigmoid is non-convex in $\mathbf{w}$. Cross-entropy is chosen instead for convexity and a probabilistic justification.

## Cross-Entropy Error

$$E_{in}(\mathbf{w}) = \frac{1}{N}\sum_{n=1}^{N}\ln\left(1 + e^{-y_n\mathbf{w}^T\mathbf{x}_n}\right)$$

Sanity check on the signs: $y_n = +1$ pushes toward $\mathbf{w}^T\mathbf{x}_n \gg 0$ so $\theta \approx 1$; $y_n = -1$ pushes toward $\mathbf{w}^T\mathbf{x}_n \ll 0$ so $\theta \approx 0$.

## Derivation from Maximum Likelihood

The compact form is what makes the derivation work. Since $\theta(-s) = 1-\theta(s)$,

$$P(y\mid\mathbf{x}) = \begin{cases}\theta(\mathbf{w}^T\mathbf{x}) & y = +1\\ \theta(-\mathbf{w}^T\mathbf{x}) & y = -1\end{cases} \;=\; \theta\!\left(y\cdot\mathbf{w}^T\mathbf{x}\right)$$

With independent samples, maximize the likelihood $\prod_{n=1}^{N}P(y_n\mid\mathbf{x}_n)$:

$$\max \prod_n P(y_n\mid\mathbf{x}_n) \;\Leftrightarrow\; \max \sum_n \ln P(y_n\mid\mathbf{x}_n) \;\Leftrightarrow\; \min \frac{1}{N}\sum_n \ln\frac{1}{P(y_n\mid\mathbf{x}_n)}$$

Substituting the model gives $\min \frac{1}{N}\sum_n \ln\frac{1}{\theta(y_n\mathbf{w}^T\mathbf{x}_n)} = \min \frac{1}{N}\sum_n\ln(1+e^{-y_n\mathbf{w}^T\mathbf{x}_n})$ — the cross-entropy error, derived rather than assumed. See [[Maximum Likelihood Estimation]].

## Optimization

No closed form exists — unlike [[Linear Regression]], $\nabla_\mathbf{w}E_{in}(\mathbf{w}) = 0$ cannot be solved analytically. The gradient is driven to zero numerically by [[Gradient Descent]]:

$$\mathbf{w}(t+1) = \mathbf{w}(t) - \eta\,\nabla E_{in}(\mathbf{w}(t))$$

Favorable structure: this $E_{in}$ **has only one valley** — it is convex, so the local minimum gradient descent finds is global.

The SGD update for a single point $(\mathbf{x}_*, y_*)$:

$$\mathbf{w}(t+1) \leftarrow \mathbf{w}(t) + y_*\mathbf{x}_*\left(\frac{\eta}{1+e^{y_*\mathbf{w}^T\mathbf{x}_*}}\right)$$

## As a Neural Network

Logistic regression is exactly one neuron: inputs $x_0,\dots,x_d$, weights $w_0,\dots,w_d$, a summation, and the sigmoid activation, outputting the probability of the $+1$ class. Stacking such units is the step to [[Neural Networks]].

## Relation to Multi-Class

Binary logistic regression is the $K=2$ special case of [[Softmax Regression]] — proved two ways in T03: sigmoid is the two-class softmax after a shift, and the logistic loss equals binary cross-entropy.

## See Also

- [[Softmax Regression]]
- [[Sigmoid Function]]
- [[Cross-Entropy Loss]]
- [[Gradient Descent]]
- [[Maximum Likelihood Estimation]]
- [[Linear Models]]
- [[CSCE 421]]
