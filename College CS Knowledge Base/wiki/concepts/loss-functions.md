---
title: "Loss Functions"
type: concept
tags: [csce421, loss-functions, margin, zero-one-loss, perceptron-loss, hinge-loss, log-loss, exponential-loss, square-loss, convexity]
sources: [csce421-t05-loss-functions, csce421-t05-loss-functions-notes]
course: CSCE 421
updated: 2026-09-22
---

[[CSCE 421]] devotes a whole topic to putting six loss functions on one axis. The payoff is structural: **every binary classifier in the course computes the same [[Linear Models|linear signal]] and differs only in how it penalizes the result.** Choosing a loss is choosing an algorithm.

## The Margin: $y_i s_i$

Given labels $y_i \in \{+1,-1\}$ and the linear score $s_i = \mathbf{w}^T\mathbf{x}_i$, every loss below is a function of the single quantity $y_i s_i$, the **margin**:

| Condition | Meaning |
|---|---|
| $y_i s_i > 0$ | prediction is **correct** |
| $\lvert s_i \rvert$ large | prediction is **confident** |
| $y_i s_i \gg 0$ | very correct |
| $y_i s_i \ll 0$ | very wrong |

Because $y_i = \pm 1$, multiplying by the label flips the sign of $s_i$ exactly when the label is negative — the same trick that collapsed two cases into one in [[Logistic Regression]]. The margin folds *correctness* and *confidence* into one number, which is what makes a single comparison plot possible.

**Read every loss below as a curve over $y_i s_i$, decreasing left to right.** The right side is correct predictions; the left side is mistakes.

## The Six Losses

Each is applied as $\frac{1}{n}\sum_{i=1}^{n} L(y_i, s_i)$.

### Zero-one loss

$$L_{0/1}(y_i, s_i) = \begin{cases} 1 & \text{if } y_i s_i < 0 \ 0 & \text{otherwise}\end{cases}$$

Counts mistakes. **This is what you actually care about** — it is the error rate. Every wrong prediction costs 1 regardless of how wrong, and it is a step function: flat, with a jump at zero.

### Perceptron loss

$$L_{p}(y_i, s_i) = \max(0,\, -y_i s_i)$$

Fixes zero-one's indifference by *"penalizing each wrong prediction by the extent of violation."* Zero for correct predictions; grows linearly with how far past the boundary a mistake lies. Gradient descent on it gives the classic [[Perceptron]] update $\mathbf{w} \leftarrow \mathbf{w} + y_n\mathbf{x}_n$.

### Square loss

$$L_{s}(y_i, s_i) = (1 - y_i s_i)^2$$

Standard for regression ([[Linear Regression]]), usable for classification but badly behaved there. Two problems, both stated in the deck: it *"tends to penalize wrong predictions excessively,"* and — the strange one — **when $y_i s_i$ is large and the prediction is correct, the loss is large.** Being confidently right is punished, because the parabola opens upward on both sides of $y_i s_i = 1$.

### Log loss (cross entropy)

$$L_{\log}(y_i, s_i) = \log\left(1 + e^{-y_i s_i}\right)$$

What [[Logistic Regression]] minimizes — identical to the $E_{in}$ derived from maximum likelihood in T02. Smooth everywhere, decreasing everywhere, asymptotically linear on the left and asymptotically zero on the right. Never exactly zero, so it keeps pushing for margin even on correct points.

### Hinge loss

$$L_{h}(y_i, s_i) = \max(0,\, 1 - y_i s_i)$$

Used by **support vector machines** to obtain a *"maximum-margin"* classifier. Identical in form to perceptron loss but with the kink moved from $0$ to $1$: a point must be correct **by a margin of at least 1** to escape penalty. Hence *"a data may be penalized even if it is predicted correctly."*

### Exponential loss

$$L_{\exp}(y_i, s_i) = e^{-y_i s_i}$$

*"More aggressive"* — grows exponentially for negative margins, *"very sensitive to wrong predictions."* Used by **AdaBoost**. The price of that sensitivity is fragility: a single badly mislabeled outlier can dominate the total loss.

## Comparison

The deck's six conclusions, condensed:

| Loss | Penalizes correct points? | Convex? | Smooth? | Aggressiveness on errors |
|---|---|---|---|---|
| Zero-one | No | **No** | No | flat (always 1) |
| Perceptron | No | Yes, not strictly | No (kink at 0) | linear |
| Hinge | **Yes**, within margin 1 | Yes, not strictly | No (kink at 1) | linear |
| Log | **Yes**, slightly | Yes | **Yes** | asymptotically linear |
| Square | **Yes**, severely | Yes | Yes | quadratic |
| Exponential | **Yes** | Yes | Yes | exponential |

Three readings worth carrying:

1. **Zero-one is the only non-convex one, and it is the one you actually want.** Its flat regions have zero gradient and its jump has no derivative, so it cannot be optimized directly. Every other loss here is a **convex surrogate** — something minimizable that tracks it. This is the deck's real thesis.
2. **Log loss is the smooth hinge.** *"The log loss is similar to the hinge loss but it is a smooth function which can be optimized with the gradient descent method."* Hinge's kink versus log's smoothness is the practical difference between SVM solvers and [[Gradient Descent]].
3. **Square loss is the odd one out**, the only loss that punishes confident correct predictions. That is why it belongs to regression and is a poor choice for classification.

## Why This Deck Exists

T01 through T03 each introduced a model with its loss attached, as if they came as a package. T05 separates them: the [[Linear Models|linear signal]] is shared infrastructure, and **the loss is the swappable part that determines what algorithm you have**. Swap log loss for hinge loss and logistic regression becomes an SVM, with no change to $s = \mathbf{w}^T\mathbf{x}$.

The notes add that this is not tied to linear models at all — *"they can also be used for nonlinear classifiers"* — which is why the same losses reappear unchanged on top of a [[Multilayer Perceptron]].

## See Also

- [[Convexity]]
- [[Cross-Entropy Loss]]
- [[Logistic Regression]]
- [[Perceptron]]
- [[Linear Models]]
- [[Gradient Descent]]
- [[CSCE 421]]
