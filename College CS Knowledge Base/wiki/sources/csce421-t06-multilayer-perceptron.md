---
title: "CSCE 421 T06 — Multi-Layer Perceptron/Networks"
type: source
tags: [lecture, csce421, mlp, neural-networks, xor, backpropagation, universal-approximation, forward-propagation]
sources: []
course: CSCE 421
updated: 2026-09-22
---

Topic deck 6 of [[CSCE 421]], by [[Shuiwang Ji]], based on *Learning From Data*. 24 slides. The deck where the course leaves linear models behind: it motivates layers from the **XOR** failure, builds the [[Multilayer Perceptron]], and derives [[Backpropagation]] in the book's sensitivity notation.

> **Extraction note:** several slides are diagram-only, and the text layer loses overline/accent characters. Where the raw text reads `f = h1h2 + h1h2`, the slide means $f = h_1\bar{h}_2 + \bar{h}_1 h_2$ (XOR); where slide 11 reads `tan(x)`, it means $\tanh(x)$, confirmed by slide 15's explicit *"Using $\theta = \tanh$."*

## XOR: A Limitation of the Linear Model

The deck opens on the classical failure — XOR is not [[Linear Separability|linearly separable]], so no single [[Perceptron]] can implement it. This is the same Minsky–Papert limitation catalogued from the survey side in [[CSCE 420]].

## Decomposing XOR

The fix is to build XOR out of linear pieces:

$$f = h_1\bar{h}_2 + \bar{h}_1 h_2, \qquad h_1(\mathbf{x}) = \mathrm{sign}\left(\mathbf{w}_1^T\mathbf{x}\right),\quad h_2(\mathbf{x}) = \mathrm{sign}\left(\mathbf{w}_2^T\mathbf{x}\right)$$

Each $h_i$ is a perceptron — a single hyperplane. XOR is a Boolean combination of two of them.

## Perceptrons for OR and AND

The combination operators are themselves perceptrons, with weights given explicitly:

$$\mathrm{OR}(x_1, x_2) = \mathrm{sign}(x_1 + x_2 + 1.5), \qquad \mathrm{AND}(x_1, x_2) = \mathrm{sign}(x_1 + x_2 - 1.5)$$

Note that only the **bias** differs between them — $+1.5$ versus $-1.5$. Three slides then build $f$ up visually from these pieces.

## The Multilayer Perceptron (MLP)

> More layers allow us to implement $f$. These additional layers are called **hidden layers**.

## Universal Approximation

> Any target function $f$ that can be decomposed into linear separators can be implemented by a **3-layer MLP**. A sufficiently smooth separator can "essentially" be decomposed into linear separators.

The hedge in *"essentially"* is the deck's own. See [[Multilayer Perceptron]] for what the theorem does and does not promise.

## The Neural Network: Why $\tanh$

> $E_{in}$ is **not smooth** (due to sign function), so cannot use gradient descent.
> $\mathrm{sign}(x) \approx \tanh(x) \longrightarrow$ gradient descent to minimize $E_{in}$.

Exactly the argument that produced the [[Sigmoid Function]] in T02, reapplied one level up: a hard threshold has zero gradient everywhere, so replace it with a smooth approximation. See [[Activation Functions]] for how this choice is revisited in T09, where ReLU replaces tanh.

## Zooming into a Hidden Node — Notation

The bookkeeping for layers $\ell = 0, 1, 2, \dots, L$, where layer $\ell$ has "dimension" $d^{(\ell)}$ and therefore $d^{(\ell)} + 1$ nodes:

| Symbol | Name | Shape |
|---|---|---|
| $s^{(\ell)}$ | signals in | $d^{(\ell)}$ dimensional vector |
| $x^{(\ell)}$ | outputs | $d^{(\ell)} + 1$ dimensional vector |
| $W^{(\ell)}$ | weights in | $\left(d^{(\ell-1)}+1\right) \times d^{(\ell)}$ matrix |
| $W^{(\ell+1)}$ | weights out | $\left(d^{(\ell)}+1\right) \times d^{(\ell+1)}$ matrix |

The $+1$ everywhere is the bias coordinate carried forward from [[Linear Models]]. The full network is specified by

$$\mathbf{W} = \left\{W^{(1)}, W^{(2)}, \dots, W^{(L)}\right\}$$

## The Linear Signal, Again

> Input $s^{(\ell)}$ is a linear combination (using weights) of the outputs of the previous layer $x^{(\ell-1)}$.

$$s^{(\ell)} = \left(W^{(\ell)}\right)^T x^{(\ell-1)}, \qquad s_j^{(\ell)} = \left(\mathbf{w}_j^{(\ell)}\right)^T x^{(\ell-1)}$$

with the slide explicitly noting *"(recall the linear signal $s = \mathbf{w}^T\mathbf{x}$)"* and the transition $s^{(\ell)} \xrightarrow{\theta} x^{(\ell)}$. **A neural network is the same signal-then-wrap recipe, stacked.**

## Forward Propagation

$$\mathbf{x} = x^{(0)} \xrightarrow{W^{(1)}} s^{(1)} \xrightarrow{\theta} x^{(1)} \xrightarrow{W^{(2)}} s^{(2)} \xrightarrow{\theta} x^{(2)} \cdots \xrightarrow{W^{(L)}} s^{(L)} \xrightarrow{\theta} x^{(L)} = h(\mathbf{x})$$

```
1: x(0) <- x                                [Initialization]
2: for l = 1 to L do                        [Forward Propagation]
3:     s(l) <- (W(l))^T x(l-1)
4:     x(l) <- [ 1 ; theta(s(l)) ]
5: end for
6: h(x) = x(L)                              [Output]
```

Line 4 re-attaches the constant $1$ at each layer so the next layer has its bias input.

## Minimizing $E_{in}$

$$E_{in}(h) = E_{in}(\mathbf{W}) = \frac{1}{N}\sum_{n=1}^{N}\left(h(\mathbf{x}_n) - y_n\right)^2$$

> Using $\theta = \tanh$ makes $E_{in}$ differentiable so we can use gradient descent $\longrightarrow$ **local minimum**.

The "local minimum" is stated flatly and matters: unlike [[Logistic Regression]], whose $E_{in}$ *"has only one valley,"* a network's error surface is **not convex**. Gradient descent proceeds identically:

$$\mathbf{W}(t+1) = \mathbf{W}(t) - \eta\,\nabla E_{in}(\mathbf{W}(t))$$

## Gradient of $E_{in}$ and the Sensitivity

Writing $E_{in}(\mathbf{w}) = \frac{1}{N}\sum_n e_n\left(h(\mathbf{x}_n), y_n\right)$, the per-layer gradient is an average of per-example gradients, so the problem reduces to finding $\frac{\partial e(\mathbf{x})}{\partial W^{(\ell)}}$. Since $e(\mathbf{x})$ depends on $W^{(\ell)}$ only through $s^{(\ell)} = \left(W^{(\ell)}\right)^T x^{(\ell-1)}$, the chain rule gives

$$\frac{\partial e}{\partial W^{(\ell)}} = \frac{\partial s^{(\ell)}}{\partial W^{(\ell)}} \cdot \left(\frac{\partial e}{\partial s^{(\ell)}}\right)^T = x^{(\ell-1)}\left(\delta^{(\ell)}\right)^T$$

where the **sensitivity** is defined as

$$\delta^{(\ell)} = \frac{\partial e}{\partial s^{(\ell)}}$$

**This is the central object of the deck.** The gradient for any layer is an outer product of that layer's input with that layer's sensitivity — so once you have every $\delta^{(\ell)}$, you have every gradient.

## The Backpropagation Algorithm

$$\delta^{(1)} \longleftarrow \delta^{(2)} \cdots \longleftarrow \delta^{(L-1)} \longleftarrow \delta^{(L)}$$

Obtained by *"multiple applications of the chain rule"* along the perturbation path

$$\Delta s^{(\ell)} \xrightarrow{\theta} \Delta x^{(\ell)} \xrightarrow{\mathbf{w}^{(\ell+1)}} \Delta s^{(\ell+1)} \cdots \longrightarrow \Delta e(\mathbf{x})$$

Arrows run **right to left**: sensitivities are computed at the output layer and propagated backward. Forward pass gets the $x^{(\ell)}$, backward pass gets the $\delta^{(\ell)}$, and the outer product of the two gives the gradient. Full derivation on [[Backpropagation]].

## Closing

> Algorithm for gradient descent on $E_{in}$: can do **batch version or sequential version (SGD)** — the same choice as T02.

The final slide returns to the **digits data** from T02, closing the loop: the same classification problem, now with learned rather than hand-designed features. That step is the subject of [[Deep Learning]].

## See Also

- [[Multilayer Perceptron]]
- [[Backpropagation]]
- [[Neural Networks]]
- [[Perceptron]]
- [[Linear Separability]]
- [[Gradient Descent]]
- [[Deep Learning]]
- [[CSCE 421]]
