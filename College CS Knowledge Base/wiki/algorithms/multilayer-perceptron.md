---
title: "Multilayer Perceptron"
type: algorithm
tags: [csce421, mlp, neural-networks, xor, hidden-layers, universal-approximation, forward-propagation, tanh]
sources: [csce421-t06-multilayer-perceptron]
course: CSCE 421
updated: 2026-09-22
---

A multilayer perceptron stacks layers of [[Perceptron|perceptron]]-like units so that the composition can express functions no single linear separator can. It is where [[CSCE 421]] leaves linear models behind — and it does so by **reusing the linear signal at every layer** rather than abandoning it.

## The Motivation: XOR

No single perceptron can implement XOR, because XOR is not [[Linear Separability|linearly separable]]. But XOR *is* a Boolean combination of two linear separators:

$$f = h_1\bar{h}_2 + \bar{h}_1 h_2, \qquad h_1(\mathbf{x}) = \mathrm{sign}\left(\mathbf{w}_1^T\mathbf{x}\right), \quad h_2(\mathbf{x}) = \mathrm{sign}\left(\mathbf{w}_2^T\mathbf{x}\right)$$

And the combining operations are themselves perceptrons:

$$\mathrm{OR}(x_1,x_2) = \mathrm{sign}(x_1 + x_2 + 1.5), \qquad \mathrm{AND}(x_1,x_2) = \mathrm{sign}(x_1 + x_2 - 1.5)$$

Note these differ **only in the bias** — $+1.5$ versus $-1.5$. So XOR is buildable from perceptrons wired in two stages. The extra stages are called **hidden layers**, and that construction is the entire argument for depth.

## Universal Approximation

> Any target function $f$ that can be decomposed into linear separators can be implemented by a **3-layer MLP**. A sufficiently smooth separator can "essentially" be decomposed into linear separators.

Read the hedges carefully. The theorem says a sufficiently wide network *can represent* almost anything — it says nothing about whether [[Gradient Descent]] will **find** those weights, or how many units are needed, or whether the result generalizes. Representability and learnability are different claims. Compare the expressiveness ladder in [[Neural Networks]], which catalogues the same result from the [[CSCE 420]] survey side.

## Why $\tanh$ Replaces $\mathrm{sign}$

> $E_{in}$ is not smooth (due to sign function), so cannot use gradient descent. $\mathrm{sign}(x) \approx \tanh(x) \longrightarrow$ gradient descent to minimize $E_{in}$.

Identical to the argument that introduced the [[Sigmoid Function]] in T02, applied one level up. A hard threshold has zero derivative everywhere it is defined, so the chain rule dies at the first layer. $\tanh$ is the smooth stand-in — same S-shape, differentiable everywhere, and the activation is written $\theta$ throughout the deck.

## Notation

Layers $\ell = 0, 1, \dots, L$. Layer $\ell$ has dimension $d^{(\ell)}$, hence $d^{(\ell)} + 1$ nodes (the $+1$ is the bias coordinate carried from [[Linear Models]]).

| Symbol | Meaning | Shape |
|---|---|---|
| $s^{(\ell)}$ | signals into layer $\ell$ | $d^{(\ell)}$ |
| $x^{(\ell)}$ | outputs of layer $\ell$ | $d^{(\ell)} + 1$ |
| $W^{(\ell)}$ | weights into layer $\ell$ | $\left(d^{(\ell-1)}+1\right) \times d^{(\ell)}$ |

The whole network is specified by $\mathbf{W} = \left\{W^{(1)}, W^{(2)}, \dots, W^{(L)}\right\}$.

## The Linear Signal, Per Layer

$$s^{(\ell)} = \left(W^{(\ell)}\right)^T x^{(\ell-1)}, \qquad s_j^{(\ell)} = \left(\mathbf{w}_j^{(\ell)}\right)^T x^{(\ell-1)}$$

The deck flags this explicitly — *"recall the linear signal $s = \mathbf{w}^T\mathbf{x}$."* **Every unit in every layer does exactly what the perceptron did**; the only new thing is that its inputs are the previous layer's outputs rather than the raw features. A network is the signal-then-wrap recipe applied $L$ times:

$$s^{(\ell)} \xrightarrow{\;\theta\;} x^{(\ell)}$$

## Forward Propagation

$$\mathbf{x} = x^{(0)} \xrightarrow{W^{(1)}} s^{(1)} \xrightarrow{\theta} x^{(1)} \xrightarrow{W^{(2)}} \cdots \xrightarrow{W^{(L)}} s^{(L)} \xrightarrow{\theta} x^{(L)} = h(\mathbf{x})$$

```
1: x(0) <- x                            [Initialization]
2: for l = 1 to L do
3:     s(l) <- (W(l))^T x(l-1)          [linear signal]
4:     x(l) <- [ 1 ; theta(s(l)) ]      [activate, re-attach bias]
5: end for
6: h(x) = x(L)                          [Output]
```

Line 4 prepends the constant $1$ at every layer so the next layer has a bias input available.

## Training

$$E_{in}(\mathbf{W}) = \frac{1}{N}\sum_{n=1}^{N}\left(h(\mathbf{x}_n) - y_n\right)^2, \qquad \mathbf{W}(t+1) = \mathbf{W}(t) - \eta\,\nabla E_{in}(\mathbf{W}(t))$$

Same [[Gradient Descent]] as T02, and the batch/SGD choice carries over unchanged. **One critical difference:** the deck says gradient descent here reaches a **local minimum**. Composing layers destroys [[Convexity]], so unlike [[Logistic Regression]] — whose $E_{in}$ *"has only one valley"* — a network's error surface has many, and where you land depends on initialization.

Computing $\nabla E_{in}$ efficiently is the problem [[Backpropagation]] solves, via the per-layer sensitivity

$$\delta^{(\ell)} = \frac{\partial e}{\partial s^{(\ell)}}, \qquad \frac{\partial e}{\partial W^{(\ell)}} = x^{(\ell-1)}\left(\delta^{(\ell)}\right)^T$$

## Where It Leads

The deck closes on the **digits data** from T02 — the same problem, but with features learned by the hidden layers rather than hand-designed as intensity and symmetry. That substitution is the step to [[Deep Learning]], and it is why [[Linear Models]] flags feature choice as the thing deep learning automates.

## See Also

- [[Backpropagation]]
- [[Neural Networks]]
- [[Perceptron]]
- [[Linear Separability]]
- [[Convexity]]
- [[Gradient Descent]]
- [[Deep Learning]]
- [[CSCE 421]]
