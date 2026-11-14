---
title: "Activation Functions"
type: concept
tags: [csce421, activation-functions, relu, tanh, sigmoid, saturation, vanishing-gradient]
sources: [csce421-t09-cnn, csce421-t06-multilayer-perceptron]
course: CSCE 421
updated: 2026-10-20
---

The activation is the nonlinearity applied to a layer's [[Linear Models|linear signal]] — the "wrap" in signal-then-wrap. [[CSCE 421]] meets three of them in sequence, each introduced because the previous one failed at something.

## Why One Is Needed At All

Without a nonlinearity, stacking layers is pointless: a composition of linear maps is a linear map, so an $L$-layer network would collapse to a single matrix. The activation is what makes depth buy expressiveness.

But it cannot be *any* nonlinearity. [[CSCE 421 T06 — Multi-Layer Perceptron/Networks|T06]] states the constraint:

> $E_{in}$ is not smooth (due to sign function), so cannot use gradient descent.

$\mathrm{sign}(s)$ has zero derivative everywhere it is defined and none at the jump, so the chain rule dies at the first layer. **The activation must be differentiable** for [[Backpropagation]] to exist.

## The Three

### sign

$$\mathrm{sign}(s) = \begin{cases} +1 & s > 0 \\ -1 & s < 0\end{cases}$$

The [[Perceptron]]'s activation. Correct output type for classification, useless for learning — zero gradient everywhere.

### tanh

$$\theta(s) = \tanh(s), \qquad \theta'(s) = 1 - \tanh^2(s) = 1 - x^2$$

T06's replacement for $\mathrm{sign}$, *"$\mathrm{sign}(x) \approx \tanh(x)$"* — same S-shape, differentiable everywhere. T09's assessment:

> - Squashes numbers to range $[-1,1]$
> - **zero centered (nice)**
> - **still kills gradients when saturated**

Note $\theta'(s) = 1 - x^2$ uses the *forward-pass output* directly — no re-evaluation needed, the same efficiency the [[Sigmoid Function]] gives in [[Backpropagation]], and the step used throughout the HW2 worked example.

### ReLU

$$f(s) = \max(0, s)$$

T09's list, verbatim:

> - **Does not saturate** (in + region)
> - Very **computationally efficient**
> - **Converges much faster** than sigmoid/tanh in practice (e.g. **6x**)
> - Actually more biologically plausible than sigmoid
> - **Not zero-centered** output
> - An annoyance: *hint, what is the gradient when $x < 0$?*

## Saturation, and Why It Matters

This is the thread connecting all three.

A **saturated** unit is one pushed far into a flat region of its activation. For tanh at $s = 5$, $\tanh(5) \approx 0.9999$ and $\theta'(5) \approx 0.0002$. [[Backpropagation]] multiplies by that derivative when passing $\delta$ backward:

$$\delta^{(\ell)} = \theta'(s^{(\ell)}) \cdot W^{(\ell+1)}\delta^{(\ell+1)}$$

So a saturated unit **multiplies the gradient by nearly zero**, and every layer below it receives almost no signal. Stack several and the gradient vanishes entirely — the classic **vanishing gradient** problem, and the reason deep networks were hard to train before ReLU.

ReLU's derivative is exactly $1$ for $s > 0$, so gradient passes through **undiminished**. That single fact is most of the "6x faster" claim.

## The Dead ReLU

T09's closing question answers itself: for $s < 0$ the gradient is **zero**. A unit whose input is negative for every training example receives no gradient ever and can never recover — it is **dead**.

So ReLU trades tanh's *gradual* saturation on both sides for *total* death on one side. In practice the trade is strongly worth it, and variants (leaky ReLU, ELU, GELU) exist to patch the negative region.

## Summary

| | Range | Differentiable | Saturates | Gradient issue |
|---|---|---|---|---|
| $\mathrm{sign}$ | $\{-1,+1\}$ | **no** | — | no gradient at all |
| $\tanh$ | $[-1,1]$ | yes | **both sides** | vanishing when saturated |
| ReLU | $[0,\infty)$ | yes (except 0) | $+$ side no | **dead units** at $s<0$ |

## Relation to Normalization

[[Batch Normalization]] attacks saturation from the other direction — instead of changing the activation, it rescales what reaches it so units sit in their responsive region. T09 places BN *"after Fully Connected or Convolutional layers, and before nonlinearity"* for exactly this reason, and lists *"improves gradient flow through the network"* first among its benefits.

The learnable $\gamma, \beta$ matter here too: pinning every input to unit variance would trap tanh in its near-linear middle, so the network is given the means to undo that where it wants saturation.

## See Also

- [[Sigmoid Function]]
- [[Batch Normalization]]
- [[Backpropagation]]
- [[Multilayer Perceptron]]
- [[Perceptron]]
- [[CSCE 421]]
