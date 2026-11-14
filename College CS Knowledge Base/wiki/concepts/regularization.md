---
title: "Regularization"
type: concept
tags: [csce421, regularization, overfitting, penalty-term, lambda, weight-decay, dropout, data-augmentation, early-stopping]
sources: [csce421-t04-overfitting, csce421-t09-cnn]
course: CSCE 421
updated: 2026-10-20
---

Regularization controls [[Overfitting]] by **adding a penalty term to the error function to discourage the coefficients from reaching large values**. It attacks the symptom identified in the polynomial case study — pathological fits have huge, nearly-cancelling coefficients — without reducing the model's nominal flexibility.

## The Idea

Instead of minimizing error alone, minimize error plus a penalty on the size of the weights:

$$\tilde{E}(\mathbf{w}) = \underbrace{E(\mathbf{w})}_{\text{fit the data}} + \underbrace{\lambda \cdot \Omega(\mathbf{w})}_{\text{keep weights small}}$$

For the sum-of-squares case in [[CSCE 421 T04 — Overfitting and Regularization|T04]], with $\Omega(\mathbf{w}) = \lVert\mathbf{w}\rVert^2$:

$$\tilde{E}(\mathbf{w}) = \frac{1}{2}\sum_{n=1}^{N}\left(y(x_n, \mathbf{w}) - t_n\right)^2 + \frac{\lambda}{2}\lVert\mathbf{w}\rVert^2$$

The minimizer must now trade off two competing demands, and large coefficients have to *earn* their size by buying enough error reduction to pay the penalty.

## The Role of Lambda

> The coefficient $\lambda$ governs the **relative importance of the regularization term** compared with the sum-of-squares error term.

| $\lambda$ | Behavior |
|---|---|
| $\lambda = 0$ | No penalty — the original unregularized fit, free to overfit |
| $\lambda$ small | Mild shrinkage; wild oscillation suppressed, real structure kept |
| $\lambda$ large | Weights crushed toward zero — the fit **underfits**, approaching a constant |

So $\lambda$ is a continuous dial between the two failure modes. The effect-of-the-regularization-parameter slides show the fitted curve sweeping from the oscillating $M=9$ fit to a nearly flat one as $\lambda$ grows.

## Why It Works

The $M=9$ polynomial achieves its oscillation through large positive and negative coefficients that nearly cancel. Those cancellations are fragile — tiny changes in the data swing the curve enormously. The penalty makes that configuration expensive, so the optimizer finds a smoother function within the *same* hypothesis set.

**The key point:** the model keeps all $M+1$ parameters. Regularization does not remove flexibility, it makes flexibility costly. This is why it scales to models where reducing parameter count is not an option — a [[Multilayer Perceptron|neural network]] cannot easily be shrunk, but its weights can be penalized. In that context the same penalty is usually called **weight decay**.

## The Problem It Creates

$\lambda$ cannot be chosen by minimizing training error, since training error is always lowest at $\lambda = 0$. It is a **hyperparameter**, and selecting it is exactly the problem [[Model Selection]] addresses:

> Model selection: estimation of the optimal value of the regularization parameter. In practice, cross validation is commonly applied for model selection.

Choosing $M$ and choosing $\lambda$ are therefore the same kind of decision, made the same way.

## Beyond Weight Penalties

The $\lambda\lVert\mathbf{w}\rVert^2$ penalty above is the T04 form — a **deterministic term added to the loss**. [[CSCE 421 T09 — Convolutional Neural Networks|T09]] introduces a second family that attacks [[Overfitting]] by **injecting randomness** instead, and states the unifying pattern twice:

> **Training: add some kind of randomness. Testing: average out randomness (sometimes approximate).**
>
> Examples: Dropout, Batch Normalization, Data Augmentation, DropConnect

| Method | Randomness added during training | How it is removed at test |
|---|---|---|
| [[Dropout]] | units randomly zeroed, $p = 0.5$ common | use the full network, rescaled |
| [[Batch Normalization]] | statistics from a random minibatch | fixed running averages |
| Data augmentation | random flips, crops, scales | evaluate on the untransformed image |
| Early stopping | — | stop where validation accuracy turns |

Seeing [[Batch Normalization]] on this list is the non-obvious part, and it explains its hedged claim to *"act as a form of regularization in a funny way"* — which minibatch an example lands in is random, so its normalized value is too.

Weight penalties and noise injection are complementary and routinely combined. Both reduce effective capacity without removing parameters, which is what makes them usable on networks where reducing the parameter count is not an option.

## See Also

- [[Dropout]]
- [[Batch Normalization]]
- [[Overfitting]]
- [[Model Selection]]
- [[In-Sample and Out-of-Sample Error]]
- [[Linear Regression]]
- [[Deep Learning]]
- [[CSCE 421]]
