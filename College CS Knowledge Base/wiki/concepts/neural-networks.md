---
title: "Neural Networks"
type: concept
tags: [csce420, neural-networks, perceptron, linear-separability, feature-engineering]
sources: [csce420-final-practice, csce420-lecture-01-introduction, csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

A neural network is a layered composition of units, each computing a nonlinearity applied to a weighted sum of its inputs plus a bias. A single threshold unit implements a **linear** decision boundary — a hyperplane in its input space. Everything a network can express beyond that comes from composing units in layers, or from changing what the inputs are.

## The Expressiveness Ladder

| Architecture | Regions it can carve |
|---|---|
| Single unit (perceptron) | One half-plane — only linearly separable classes |
| One hidden layer, $k$ units, linear output threshold | Boolean combinations of $k$ half-planes (intersections, unions, slabs) |
| Two hidden layers | Arbitrary regions, to any accuracy |

[[CSCE 421]] derives this ladder from the bottom up in [[Multilayer Perceptron]], where XOR motivates hidden layers and [[Backpropagation]] trains them.

Minsky and Papert's 1969 result on the limitations of the perceptron — the single-unit row of this table — is in the [[History of AI]] timeline as the trigger for the first neural-network winter.

## Counting Hidden Units (Final Practice, Problem 6)

The dataset is 16 points on a $4 \times 4$ grid, $x_1, x_2 \in \{0,1,2,3\}$, with class **o** at $(1,1), (2,1), (2,2), (3,3)$ and class **x** at the other twelve. The network offered has **two hidden units and one output unit** (each with a bias). Can it reach 100% accuracy?

**Answer: No.**

Two hidden units give two half-planes, $H_1$ and $H_2$. The output unit is itself a linear threshold, so the region it labels **o** must be some linearly separable Boolean combination of them: $H_1 \cap H_2$, $H_1 \cup H_2$, a single half-plane, or a constant. Each option fails.

**Union, single half-plane, or constant.** If the **o** region is a union of half-planes or a single half-plane, the **x** region is an intersection of half-planes, hence convex. But $(2,1)$ is the midpoint of the two **x** points $(1,0)$ and $(3,2)$, and $(2,1)$ is an **o** point. So the **x** region is not convex, and all three options are ruled out.

**Intersection (the wedge case).** Suppose **o** $\subseteq H_1 \cap H_2$. Every **x** point must then fall outside $H_1$ or outside $H_2$. Sort them into $G_1$ (outside $H_1$) and $G_2$ (outside $H_2$); each complement is an open half-plane, hence convex. Now consider these three **x** points:

$$(1,0), \qquad (1,2), \qquad (3,2)$$

Each pair has an **o** point exactly at its midpoint:

| Pair of **x** points | Midpoint | Class |
|---|---|---|
| $(1,0)$ and $(1,2)$ | $(1,1)$ | **o** |
| $(1,2)$ and $(3,2)$ | $(2,2)$ | **o** |
| $(1,0)$ and $(3,2)$ | $(2,1)$ | **o** |

If any two of these shared a group, the convexity of that group's half-plane would put the **o** midpoint outside $H_1$ (or $H_2$) — but every **o** point must lie inside *both*. So all three must occupy pairwise different groups. Three points, pairwise distinct, only two groups: contradiction.

Every case fails, so no setting of the weights achieves 100%. The fix is a third hidden unit — three lines can carve out the triangle containing the **o** points, which two cannot.

> Worked here from the dataset; the practice exam ships without an answer key.

## Feature Engineering vs. Depth (Final Practice, Problem 7)

The spiral dataset is not linearly separable and needs a highly nonlinear boundary. The problem compares a network given raw input $(x_1, x_2)$ against one given the expanded input $(x_1, x_2, x_1^2, x_2^2)$.

**(1) Which needs a much smaller network? The second.** With raw inputs the network must *construct* every nonlinearity out of many layers and units. Handing it squared terms supplies curvature for free: a single unit over $(x_1, x_2, x_1^2, x_2^2)$ computes $w_1 x_1 + w_2 x_2 + w_3 x_1^2 + w_4 x_2^2 + b$, whose zero set is a **conic** — circle, ellipse, hyperbola — in the original plane. Radial structure like a spiral is far cheaper to approximate with conics than with line segments. This is the classic trade: good features buy you depth.

**(2) Would the first hidden layer's decision boundaries be linear in both cases?** In the original $(x_1, x_2)$ plane the answer is **No** — case one gives straight lines, case two gives conics, and that difference is exactly why case two needs fewer units. Read instead as a question about each neuron's own input space, the answer flips to Yes, since a threshold unit is always a hyperplane in whatever coordinates it receives. The wording is ambiguous, but the "No" reading is the one that connects to part (1), and the substantive point holds either way: **the neuron stays linear; the feature map is what bends the boundary.**

> The intended answer for (2) is not determinable from the paper alone.

## The Single-Neuron View (CSCE 421)

[[CSCE 421]] arrives at the same object from the opposite direction. [[Logistic Regression]] drawn as a diagram *is* one neuron: inputs $x_0,\dots,x_d$, weights $w_0,\dots,w_d$, a summation, and a [[Sigmoid Function|sigmoid]] activation emitting the probability of the $+1$ class. [[Softmax Regression]] widens this to $K$ output units under a [[Softmax Function|softmax]].

This makes the relationship concrete: a neural network is these units stacked and composed, and the classifier at the top of a deep network is still softmax with [[Cross-Entropy Loss]]. What deep learning adds is not a new output layer but *learned features* in place of hand-designed ones.

## From the Lecture (Deck 6)

### Definition

> A neural network is one particular form of **learning from data**: simple processing elements ("units" or "neurons"), a connective structure with associated weights, and **learning as the adaptation of connection weights.**

Neural networks are presented as having **many faces**, all valid: an abstract mathematical/statistical model, an optimization algorithm, a pattern recognition algorithm, a tool for understanding brain function, and a robust engineering application.

### The Biological Numbers

| Quantity | Value |
|---|---|
| Neocortex thickness | 1.6 mm |
| Neocortex area | 2,500 cm² (~2.5 ft²) |
| Neurons | 86 billion; ~10 billion in neocortex |
| Connections | 150 trillion; 60 trillion in neocortex |
| Connections per neuron | ~1,800 |
| **Energy per operation** | **$10^{-16}$ J** vs. $10^{-6}$ J in modern computers |

The energy figure is ten orders of magnitude apart — the single most striking number in the deck.

**How the brain differs from computers**: densely connected, massively parallel, highly nonlinear, **asynchronous (no central clock)**, fault tolerant, highly adaptable, creative.

### The Abstraction

A neuron becomes $f(\sum wx)$ — input, connection weight, and a **transfer (activation) function**. Typical choices: step, sign, sigmoid, $\tanh(x/2)$.

### Two Classification Axes

| Axis | Options |
|---|---|
| **Teacher exists?** | *Supervised*: perceptrons, backprop networks. *Unsupervised*: [[Self-Organizing Map\|SOM]], PCA, k-means |
| **Recurrent connections?** | *Feed-forward*: perceptrons, backprop networks. *[[Recurrent Neural Networks\|Recurrent]]*: Hopfield, Boltzmann machines, SRN, LSTM, GRU |

> **When counting layers, only count those that compute** — the input layer does not compute, it is just values.

### The Two Architectures

- **[[Perceptron|Perceptrons]]** — single layer, threshold-gated
- **Backpropagation networks** — multiple layers, sigmoid or tanh activation

The progression from one to the other is the historical arc: perceptrons are limited to [[Linear Separability|linearly separable]] functions, and [[Backpropagation]] is what made the multilayer fix trainable.

## From the Lecture (Deck 7)

Deck 7 restates the essentials compactly: a weighted sum followed by a nonlinear activation, with weights changed by gradient descent $w_{ij} \leftarrow w_{ij} - \eta \frac{\partial E}{\partial w_{ij}}$, and gives backprop in its two-case form:

$$\delta_k = (T_k - a_k)\,\sigma'(net_k) \quad\text{(hidden to output)}$$
$$\delta_j = \Big[\sum_k w_{kj}\delta_k\Big]\sigma'(net_j) \quad\text{(deeper weights)}$$

The second equation *is* backpropagation: a hidden unit's blame is the weighted sum of the blames of the units it feeds.

### What Neurons Do: Two Valid Views

- **Function approximation**
- **Decision boundary**

plus a third the deck flags for later — **representing input features**.

The $y = \sin(x)$ worked example makes the first concrete. With model `[2,tanh:1,linear]` — one hidden layer of 2 units, one linear output — **the hidden neurons represent sigmoids and the output is a linear combination of them.** Adding units and layers ($[20,\tanh:3,\tanh:1,\text{linear}]$) composes sigmoids into arbitrarily complex shapes.

The deck also uses it to show a limitation: **out-of-range inputs** expose that the network has fitted the training interval, not learned $\sin$.

## See Also

- [[Logistic Regression]]
- [[Softmax Regression]]
- [[Deep Learning]]
- [[Machine Learning Paradigms]]
- [[Decision Tree Learning]]
- [[Self-Organizing Map]]
- [[History of AI]]
- [[CSCE 421]]
