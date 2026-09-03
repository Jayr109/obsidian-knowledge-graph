---
title: "Gradient Descent"
type: algorithm
tags: [csce421, gradient-descent, sgd, optimization, learning-rate, taylor-expansion]
sources: [csce421-t02-logistic-regression]
course: CSCE 421
updated: 2026-08-25
---

Gradient descent minimizes a smooth function by repeatedly stepping in the direction of steepest decrease. It is the optimizer for every model in [[CSCE 421]] that lacks a closed form — [[Logistic Regression]] and [[Softmax Regression]] both rely on it, while [[Linear Regression]] does not need it.

## Why It Is Needed

| Model | Solving $\nabla_\mathbf{w}E_{in}(\mathbf{w}) = 0$ |
|---|---|
| [[Linear Regression]] | Analytic — the pseudoinverse |
| [[Logistic Regression]] | **No analytic solution**; set $\nabla E_{in} \to 0$ numerically |

## The Hill-Descent Picture

A ball on complicated hilly terrain rolls down into a local valley. Two questions follow: how do we reach the bottom of the *deepest* valley, and how do we do this without gravity?

The answer to the second is the gradient. For the specific case of logistic regression the first question is moot — that $E_{in}$ **has only one valley**.

## Choosing the Direction

From weights $\mathbf{w}(t)$, take a step of size $\eta$ in unit direction $\hat{\mathbf{v}}$:

$$\mathbf{w}(t+1) = \mathbf{w}(t) + \eta\hat{\mathbf{v}}$$

We get to pick $\hat{\mathbf{v}}$. The second-order Taylor expansion of a multivariate $f$ around $\mathbf{a}$ is

$$f(\mathbf{x}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a})^T(\mathbf{x}-\mathbf{a}) + \tfrac{1}{2}(\mathbf{x}-\mathbf{a})^TH_f(\mathbf{a})(\mathbf{x}-\mathbf{a})$$

Applying it to the change in error:

$$\Delta E_{in} = E_{in}(\mathbf{w}(t)+\eta\hat{\mathbf{v}}) - E_{in}(\mathbf{w}(t)) = \eta\,\nabla E_{in}(\mathbf{w}(t))^T\hat{\mathbf{v}} + O(\eta^2)$$

The first-order term is an inner product between a fixed vector and a unit vector, so it is minimized when $\hat{\mathbf{v}}$ points *opposite* the gradient:

$$\hat{\mathbf{v}} = -\frac{\nabla E_{in}(\mathbf{w}(t))}{\lVert\nabla E_{in}(\mathbf{w}(t))\rVert}$$

**The negative gradient is the steepest descent direction** — this is a derived fact, not a definition.

## Fixed Learning Rate

Normalizing by the gradient norm at every step is wasteful. Letting the step size scale with the gradient, $\eta_t = \eta\lVert\nabla E_{in}(\mathbf{w}(t))\rVert$, the norms cancel:

$$\mathbf{w}(t+1) = \mathbf{w}(t) - \eta\,\nabla E_{in}(\mathbf{w}(t))$$

This is self-correcting: $\lVert\nabla E_{in}\rVert \to 0$ near a minimum, so the effective step shrinks automatically as the algorithm converges.

Gradient descent can minimize **any smooth function** — logistic regression's $E_{in}$ is just one instance.

## The Goldilocks Step Size

| Setting | Behavior | Steps observed |
|---|---|---|
| $\eta = 0.1$ | Too small — creeps | 75 |
| $\eta = 2$ | Too large — overshoots | 10 |
| Variable $\eta_t$ | Just right | 10 |

## Stochastic Gradient Descent

Since $E_{in}(\mathbf{w}) = \frac{1}{N}\sum_n e(\mathbf{w},\mathbf{x}_n,y_n)$ is an average of per-point errors, one point suffices for an unbiased step. Pick a random $(\mathbf{x}_*,y_*)$ and run one GD iteration on its error alone:

$$\mathbf{w}(t+1) \leftarrow \mathbf{w}(t) - \eta\,\nabla_\mathbf{w}e(\mathbf{w},\mathbf{x}_*,y_*)$$

For logistic regression this is $\mathbf{w}(t+1) \leftarrow \mathbf{w}(t) + y_*\mathbf{x}_*\left(\frac{\eta}{1+e^{y_*\mathbf{w}^T\mathbf{x}_*}}\right)$.

**Advantages**: the average move matches full GD; each step costs a fraction $1/N$; stochasticity helps escape local minima; and it is simple.

## Batch / Stochastic / Mini-Batch

| Method | Updates per iteration | Convergence speed | Stability | Computation cost |
|---|---|---|---|---|
| **Batch GD** | After full dataset | Slow | Stable | High |
| **Stochastic GD** | After each sample | Fast | Noisy (unstable) | Low |
| **Mini-Batch GD** | After each mini-batch | Moderate | Balanced | Moderate |

Mini-batch is the compromise: divide the dataset into small batches and update after each.

## See Also

- [[Logistic Regression]]
- [[Softmax Regression]]
- [[Linear Regression]]
- [[Cross-Entropy Loss]]
- [[Deep Learning]]
- [[CSCE 421]]
