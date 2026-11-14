---
title: "CSCE 421 T07 — Backpropagation by Examples"
type: source
tags: [lecture, csce421, backpropagation, chain-rule, computational-graph, gradient-flow]
sources: []
course: CSCE 421
updated: 2026-09-22
---

Topic deck 7 of [[CSCE 421]]. 9 slides, credited *"Courtesy: Fei-Fei Li & Justin Johnson & Serena Yeung"* — the Stanford CS231n treatment. Where [[CSCE 421 T06 — Multi-Layer Perceptron/Networks|T06]] derives [[Backpropagation]] in matrix/sensitivity notation, this deck does the same thing **numerically on a computational graph**, one node at a time.

> **Extraction note:** the deck is an animation — slides 3–8 are the same figure revealed progressively, with the numeric gradient values written on the graph edges as images. The formulas below are extractable; the annotated values are reconstructed from the worked example.

## The Example

$$f(x, y, z) = (x + y)\,z, \qquad x = -2,\; y = 5,\; z = -4$$

Broken into two nodes by introducing an intermediate variable:

$$q = x + y, \qquad f = qz$$

**Local gradients** — each node knows only its own derivatives, computed without reference to the rest of the graph:

$$\frac{\partial q}{\partial x} = 1, \quad \frac{\partial q}{\partial y} = 1, \qquad \frac{\partial f}{\partial q} = z, \quad \frac{\partial f}{\partial z} = q$$

**Goal:** $\dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial y}, \dfrac{\partial f}{\partial z}$

## Forward Pass

$$q = x + y = -2 + 5 = 3, \qquad f = qz = 3 \times (-4) = -12$$

## Backward Pass

Walk right to left, seeding the output with $\frac{\partial f}{\partial f} = 1$:

| Step | Quantity | Computation | Value |
|---|---|---|---|
| 1 | $\partial f/\partial f$ | seed | $1$ |
| 2 | $\partial f/\partial z$ | $= q$ | $3$ |
| 3 | $\partial f/\partial q$ | $= z$ | $-4$ |
| 4 | $\partial f/\partial y$ | $\frac{\partial f}{\partial q}\frac{\partial q}{\partial y} = (-4)(1)$ | $-4$ |
| 5 | $\partial f/\partial x$ | $\frac{\partial f}{\partial q}\frac{\partial q}{\partial x} = (-4)(1)$ | $-4$ |

## Upstream × Local

The framing the deck labels explicitly on slides 7–8, and the one worth memorizing:

$$\underbrace{\frac{\partial f}{\partial y}}_{\text{gradient}} = \underbrace{\frac{\partial f}{\partial q}}_{\text{upstream gradient}} \cdot \underbrace{\frac{\partial q}{\partial y}}_{\text{local gradient}}$$

Every node in any network does exactly this: receive the **upstream gradient** from the node ahead of it, multiply by its own **local gradient**, pass the product back. No node needs to know the global structure. That locality is what makes backpropagation implementable for arbitrary architectures — and it is the same fact T06 expresses as $\delta^{(\ell)} \leftarrow \delta^{(\ell+1)}$.

## Patterns in Backward Flow

The closing slide names three gate behaviors:

| Gate | Behavior | What it does to the upstream gradient |
|---|---|---|
| **add** | gradient **distributor** | passes it unchanged to every input |
| **max** | gradient **router** | sends it entirely to the max input, $0$ to the others |
| **mul** | gradient **switcher** | scales it by the *other* input's value |

Verify against the example: the add gate $q = x+y$ sent $-4$ to **both** $x$ and $y$ — distributor. The mul gate $f = qz$ sent $q = 3$ to $z$ and $z = -4$ to $q$ — each got the other's value, hence "switcher."

These patterns let you read gradients off a graph by inspection, which is the practical payoff of the deck.

## Relation to T06

| | T06 | T07 |
|---|---|---|
| Notation | matrices, $\delta^{(\ell)}$, layers | scalars, named nodes |
| Object | $\frac{\partial e}{\partial W^{(\ell)}} = x^{(\ell-1)}(\delta^{(\ell)})^T$ | $\frac{\partial f}{\partial x}$ on a graph |
| Purpose | why it works for a network | how to actually execute it |

Same chain rule, two levels of abstraction. T07 is the mechanical drill for T06's derivation.

## See Also

- [[Backpropagation]]
- [[Multilayer Perceptron]]
- [[CSCE 421 T06 — Multi-Layer Perceptron/Networks]]
- [[Neural Networks]]
- [[Gradient Descent]]
- [[CSCE 421]]
