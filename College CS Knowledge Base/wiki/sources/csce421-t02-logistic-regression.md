---
title: "CSCE 421 T02 — Logistic Regression for Binary Classification"
type: source
tags: [lecture, csce421, logistic-regression, cross-entropy, gradient-descent, sgd, maximum-likelihood]
sources: []
course: CSCE 421
updated: 2026-09-13
---

Topic deck 2 of [[CSCE 421]], by [[Shuiwang Ji]]. 30 slides. Derives [[Logistic Regression]] from maximum likelihood, introduces the [[Cross-Entropy Loss]], and develops [[Gradient Descent]] and SGD as the optimizer — since no closed form exists.

## Setup: Digits Data

Each digit is a $16 \times 16$ image, giving a raw input $\mathbf{x} = (1, x_1, \dots, x_{256})$ and a 257-dimensional weight vector. Hand-designed **intensity and symmetry features** collapse this to $\mathbf{x} = (1, x_1, x_2)$ with $\dim = 3$.

> A *feature* is defined here as an important property of the input that you think is useful for classification. Several slides on image representations, transformations, and learning invariant representations are visual-only and not captured in text extraction.

## From Signal to Probability

The linear signal $s = \mathbf{w}^T\mathbf{x}$ is unchanged from [[Linear Regression]]. What changes is what happens to it:

$$h(\mathbf{x}) = \theta(\mathbf{w}^T\mathbf{x}), \qquad \theta(s) = \frac{1}{1+e^{-s}}$$

Motivating example: predicting probability of heart attack from age, blood sugar, HDL, LDL, mass, and height — the target is $y \in [0,1]$.

**The key tension**: the data is still binary, $y_n = \pm 1$. We cannot measure a probability — we only see whether an event occurred, and must infer a probability from it. The target function being learned is $f(\mathbf{x}) = P[y = +1 \mid \mathbf{x}]$, with $P(y=1\mid\mathbf{x}) = f(\mathbf{x})$ and $P(y=-1\mid\mathbf{x}) = 1 - f(\mathbf{x})$.

## Choosing the Error Measure

A naive squared-error measure against $\tfrac{1}{2}(1+y_n)$ captures "want $h \approx 1$ when $y=+1$" but is *hard to minimize*. The deck instead motivates cross-entropy:

$$E_{in}(\mathbf{w}) = \frac{1}{N}\sum_{n=1}^{N}\ln\left(1 + e^{-y_n \mathbf{w}^T\mathbf{x}_n}\right)$$

Admittedly "complicated and ugly," but it rests on a probabilistic interpretation of $h$ and is mathematically convenient. Sanity check: $y_n = +1$ encourages $\mathbf{w}^T\mathbf{x}_n \gg 0$ so $\theta(\mathbf{w}^T\mathbf{x}_n) \approx 1$; $y_n = -1$ encourages $\mathbf{w}^T\mathbf{x}_n \ll 0$ so $\theta \approx 0$.

## Derivation from Maximum Likelihood

Because $\theta(-s) = 1 - \theta(s)$, the two cases collapse to the compact form $P(y \mid \mathbf{x}) = \theta(y \cdot \mathbf{w}^T\mathbf{x})$. With independently generated samples the likelihood is $\prod_n P(y_n \mid \mathbf{x}_n)$, and maximizing it is equivalent to minimizing $\frac{1}{N}\sum_n \ln\frac{1}{P(y_n\mid \mathbf{x}_n)}$, which specializes exactly to the cross-entropy above. Full chain on [[Maximum Likelihood Estimation]].

## Optimization

Linear regression has a closed form via the pseudoinverse; **logistic regression does not** — the gradient must be driven to zero numerically.

The hill-descent analogy (a ball on hilly terrain rolls to a local valley) sets up the question: which direction, given we have no gravity? A Taylor expansion of $E_{in}(\mathbf{w}(t) + \eta\hat{\mathbf{v}})$ shows the first-order change $\eta\nabla E_{in}(\mathbf{w}(t))^T\hat{\mathbf{v}}$ is minimized at

$$\hat{\mathbf{v}} = -\frac{\nabla E_{in}(\mathbf{w}(t))}{\lVert\nabla E_{in}(\mathbf{w}(t))\rVert}$$

— the negative gradient is the steepest direction. The deck notes that this $E_{in}$ **has only one valley**.

Absorbing the normalization gives fixed-rate gradient descent $\mathbf{w}(t+1) = \mathbf{w}(t) - \eta\nabla E_{in}(\mathbf{w}(t))$; the effective step shrinks near a minimum since $\lVert\nabla E_{in}\rVert \to 0$.

**Learning-rate behavior** ("Goldilocks" slide): $\eta = 0.1$ took 75 steps; $\eta = 2$ took 10 steps; a variable $\eta_t$ took 10 steps.

## SGD and the Batch Comparison

SGD picks one random point $(\mathbf{x}_*, y_*)$ and runs a GD iteration on its error alone. For logistic regression the update is

$$\mathbf{w}(t+1) \leftarrow \mathbf{w}(t) + y_*\mathbf{x}_*\left(\frac{\eta}{1+e^{y_*\mathbf{w}^T\mathbf{x}_*}}\right)$$

Advantages listed: the *average* move matches GD; computation is a factor $1/N$ cheaper per step; stochasticity helps escape local minima; and it is simple.

| Method | Updates per iteration | Convergence | Stability | Cost |
|---|---|---|---|---|
| Batch GD | After full dataset | Slow | Stable | High |
| Stochastic GD | After each sample | Fast | Noisy (unstable) | Low |
| Mini-Batch GD | After each mini-batch | Moderate | Balanced | Moderate |

## Neural Network View

A slide draws logistic regression as a single neuron: inputs $x_0 \dots x_d$, weights $w_0 \dots w_d$, a summation, and $\theta$ producing "probability that the input belongs to the $+1$ class." See [[Neural Networks]].

## See Also

- [[Logistic Regression]]
- [[Cross-Entropy Loss]]
- [[Gradient Descent]]
- [[Maximum Likelihood Estimation]]
- [[Sigmoid Function]]
- [[CSCE 421]]
- [[Linear Models]]
