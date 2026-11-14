---
title: "Backpropagation"
type: algorithm
tags: [csce420, csce421, backpropagation, gradient-descent, chain-rule, multilayer, sensitivity, computational-graph]
sources: [csce420-lecture-06-machine-learning, csce421-t06-multilayer-perceptron, csce421-t07-backpropagation-examples]
course: CSCE 420, CSCE 421
updated: 2026-09-22
---

Backpropagation trains multilayer feed-forward networks by **gradient descent**, distributing error blame from the output layer back through the hidden layers. Proposed alongside multilayer networks in the 1950s–60s, the training procedure arrived in **1969** and became popular in the **1980s**.

## The Problem It Solves

> The output layer has an explicit error measure, so finding the error surface is trivial. However, for the hidden layers, how much error each connection eventually causes at the output nodes is hard to determine.

**Backpropagation determines how to distribute the blame to each connection.** That is the whole idea; the rest is the chain rule.

## Gradient Descent

Minimize total error $E$ by tweaking weights. Adjusting all $W_i$ simultaneously is impractical, so proceed iteratively, changing each weight proportional to the local gradient:

$$\Delta W_i = \alpha \times \left(-\frac{\partial E}{\partial W_i}\right)$$

Negative slope → increase $W$; positive slope → decrease it. Partial derivatives are used because $E$ depends on many weights at once. See [[Gradient Descent]] for the fuller treatment in [[CSCE 421]].

## Hidden-to-Output Weights

Error function, with $g$ the sigmoid and $T_i$ the target:

$$E = \sum_i (E_i)^2, \qquad E_i = T_i - O_i = T_i - g\Big(\sum_j W_{ij}a_j\Big)$$

Differentiating by the chain rule:

$$\frac{\partial E}{\partial W_{ij}} = -(T_i - O_i) \times g'\Big(\sum_j W_{ij}a_j\Big) \times a_j = -a_j \times \Delta_i$$

giving the update rule

$$W_{ij} \leftarrow W_{ij} + \alpha \times a_j \times \Delta_i, \qquad \Delta_i = (T_i - O_i)\,g'\Big(\sum_j W_{ij}a_j\Big)$$

## The Sigmoid Derivative Trick

From $g(x) = \frac{1}{1+e^{-x}}$ it is easy to verify

$$g'(x) = g(x)\,(1 - g(x))$$

so since $g(\sum_j W_{ij}a_j) = O_i$, we get $g'(\sum_j W_{ij}a_j) = O_i(1 - O_i)$.

**The forward pass output can be reused directly in the backward pass** — no re-evaluation of the activation function. This is a genuine efficiency, and it is one reason the sigmoid was the default activation for so long.

## Reading the Update Rule

$\Delta_i$ carries $(T_i - O_i)$ — *target minus output*, the same **predicted-minus-true** shape as the [[Perceptron]] rule and as the softmax cross-entropy gradient in [[Softmax Regression]]. The weight change is that error term times the incoming activation $a_j$: **blame is assigned in proportion to how much each input contributed.**

---

# The CSCE 421 Treatment

[[CSCE 421]] derives the same algorithm twice — once in matrix form over layers ([[CSCE 421 T06 — Multi-Layer Perceptron/Networks|T06]]), once numerically on a computational graph ([[CSCE 421 T07 — Backpropagation by Examples|T07]]). The section above is the [[CSCE 420]] survey version; this is the derivation.

## Setup

For a [[Multilayer Perceptron]] with layers $\ell = 1, \dots, L$, weights $W^{(\ell)}$, signals $s^{(\ell)} = \left(W^{(\ell)}\right)^T x^{(\ell-1)}$ and outputs $x^{(\ell)} = \theta\left(s^{(\ell)}\right)$, the objective decomposes over examples:

$$E_{in}(\mathbf{w}) = \frac{1}{N}\sum_{n=1}^{N} e_n\left(h(\mathbf{x}_n), y_n\right), \qquad \frac{\partial E_{in}}{\partial W^{(\ell)}} = \frac{1}{N}\sum_{n=1}^{N}\frac{\partial e_n}{\partial W^{(\ell)}}$$

so the problem reduces to one example's $\dfrac{\partial e(\mathbf{x})}{\partial W^{(\ell)}}$.

## The Sensitivity

$e(\mathbf{x})$ depends on $W^{(\ell)}$ **only through** $s^{(\ell)}$. The chain rule therefore factors cleanly:

$$\frac{\partial e}{\partial W^{(\ell)}} = \frac{\partial s^{(\ell)}}{\partial W^{(\ell)}} \cdot \left(\frac{\partial e}{\partial s^{(\ell)}}\right)^T = x^{(\ell-1)}\left(\delta^{(\ell)}\right)^T$$

where the **sensitivity** of layer $\ell$ is

$$\delta^{(\ell)} = \frac{\partial e}{\partial s^{(\ell)}}$$

**This is the organizing idea.** Every layer's gradient is an outer product of two things: $x^{(\ell-1)}$, already computed on the forward pass, and $\delta^{(\ell)}$, which is all that remains to find. Note the shape — *incoming activation* times *error term* — is exactly the $a_j \times \Delta_i$ of the [[CSCE 420]] update rule above. Same fact, book notation.

## Propagating Backward

Sensitivities are obtained by *"multiple applications of the chain rule"* along the perturbation path

$$\Delta s^{(\ell)} \xrightarrow{\;\theta\;} \Delta x^{(\ell)} \xrightarrow{\;\mathbf{w}^{(\ell+1)}\;} \Delta s^{(\ell+1)} \longrightarrow \cdots \longrightarrow \Delta e(\mathbf{x})$$

giving the recursion that names the algorithm:

$$\delta^{(1)} \longleftarrow \delta^{(2)} \longleftarrow \cdots \longleftarrow \delta^{(L-1)} \longleftarrow \delta^{(L)}$$

$\delta^{(L)}$ is computable directly, since the output layer's effect on the error is explicit. Every earlier layer's sensitivity is then built from the one after it — **blame flows from the output backward**, which is precisely the problem stated at the top of this page.

## The Two Passes

| Pass | Direction | Produces |
|---|---|---|
| Forward | $x^{(0)} \to x^{(L)}$ | the activations $x^{(\ell)}$ and the prediction $h(\mathbf{x})$ |
| Backward | $\delta^{(L)} \to \delta^{(1)}$ | the sensitivities $\delta^{(\ell)}$ |
| Combine | per layer | $\partial e / \partial W^{(\ell)} = x^{(\ell-1)}\left(\delta^{(\ell)}\right)^T$ |

Both passes cost about the same as one forward evaluation, which is why training a deep network is feasible at all.

## The Computational-Graph View (T07)

T07 drops the matrices and runs the chain rule on a scalar graph. With $f(x,y,z) = (x+y)z$ and $q = x+y$, at $x=-2,\; y=5,\; z=-4$:

| Quantity | Computation | Value |
|---|---|---|
| $q$ | $x + y$ | $3$ |
| $f$ | $qz$ | $-12$ |
| $\partial f/\partial z$ | $= q$ | $3$ |
| $\partial f/\partial q$ | $= z$ | $-4$ |
| $\partial f/\partial y$ | $\frac{\partial f}{\partial q}\frac{\partial q}{\partial y} = (-4)(1)$ | $-4$ |
| $\partial f/\partial x$ | $\frac{\partial f}{\partial q}\frac{\partial q}{\partial x} = (-4)(1)$ | $-4$ |

The pattern each node follows:

$$\underbrace{\frac{\partial f}{\partial y}}_{\text{gradient}} = \underbrace{\frac{\partial f}{\partial q}}_{\text{upstream}} \times \underbrace{\frac{\partial q}{\partial y}}_{\text{local}}$$

A node needs only the gradient handed to it from ahead and its own derivative. **No node knows the global structure** — which is why this generalizes to arbitrary architectures and why automatic differentiation in every modern framework is built this way. It is the scalar version of $\delta^{(\ell)} \leftarrow \delta^{(\ell+1)}$.

### Gate patterns

| Gate | Role | Effect on the upstream gradient |
|---|---|---|
| **add** | gradient **distributor** | copies it unchanged to every input |
| **max** | gradient **router** | all of it to the max input, zero to the rest |
| **mul** | gradient **switcher** | scales it by the *other* input's value |

Confirmed by the example: the add gate sent $-4$ to both $x$ and $y$; the mul gate sent $q=3$ to $z$ and $z=-4$ to $q$.

## What Backpropagation Does Not Give You

It computes the gradient efficiently and correctly. It does **not** make the problem convex — a network's $E_{in}$ has many valleys, so gradient descent reaches *a* local minimum, not *the* minimum. See [[Convexity]].

## See Also

- [[Multilayer Perceptron]]
- [[Neural Networks]]
- [[Perceptron]]
- [[Gradient Descent]]
- [[Convexity]]
- [[Deep Learning]]
- [[CSCE 420]]
- [[CSCE 421]]
