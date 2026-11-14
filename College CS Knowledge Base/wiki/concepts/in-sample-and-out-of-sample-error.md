---
title: "In-Sample and Out-of-Sample Error"
type: concept
tags: [csce421, generalization, in-sample-error, out-of-sample-error, learning-from-data]
sources: [csce421-t01-linear-regression]
course: CSCE 421
updated: 2026-08-25
---

$E_{in}$ is the error a hypothesis makes on the training data; $E_{out}$ is its expected error on unseen data drawn from the same distribution. The central fact of learning is that **we can only compute $E_{in}$, but we only care about $E_{out}$**.

## Definitions

For squared error in [[Linear Regression]]:

$$E_{in}(h) = \frac{1}{N}\sum_{n=1}^{N}\left(h(\mathbf{x}_n)-y_n\right)^2 \qquad\text{in-sample error}$$

$$E_{out}(h) = \mathbb{E}_x\left[\left(h(\mathbf{x})-y\right)^2\right] \qquad\text{out-of-sample error}$$

The structural difference: $E_{in}$ is a **finite average over the $N$ points we have**; $E_{out}$ is an **expectation over the input distribution**, including every point we will never see.

## Why the Distinction Is the Whole Problem

Every training algorithm in the course minimizes $E_{in}$, because it is the only thing computable from a dataset. [[Linear Regression]] minimizes it in closed form; [[Logistic Regression]] and [[Softmax Regression]] minimize it by [[Gradient Descent]]. None of them can touch $E_{out}$ directly.

Learning is therefore only justified if small $E_{in}$ implies small $E_{out}$ — the generalization question. Fitting the training data is the *means*; performing on novel input is the *goal*, as [[Machine Learning Paradigms]] puts it.

Two ways this can fail:

- $E_{in}$ is small but $E_{out}$ is large — the hypothesis memorized the sample rather than the pattern. This is [[Overfitting]], and [[CSCE 421 T04 — Overfitting and Regularization|T04]] is devoted to it.
- $E_{in}$ itself never gets small — the hypothesis set was too limited to express the target.

## Relation to the Hypothesis Set

The gap between $E_{in}$ and $E_{out}$ depends on how rich the [[Linear Models|hypothesis set]] is. A set flexible enough to fit any labeling can drive $E_{in}$ to zero while saying nothing about unseen data. This is the tradeoff that motivates the generalization theory later in *Learning From Data*.

## Note on Error Measures

$E_{in}$ names a *role*, not a formula — the in-sample average of whatever error measure the model uses. It is squared error for [[Linear Regression]] and [[Cross-Entropy Loss]] for logistic and softmax regression. In the logistic case the same symbol $E_{in}(\mathbf{w})$ denotes $\frac{1}{N}\sum_n\ln(1+e^{-y_n\mathbf{w}^T\mathbf{x}_n})$.

## See Also

- [[Linear Regression]]
- [[Linear Models]]
- [[Cross-Entropy Loss]]
- [[Machine Learning Paradigms]]
- [[CSCE 421]]
