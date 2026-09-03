---
title: "Perceptron"
type: algorithm
tags: [csce420, perceptron, linear-separability, xor, minsky-papert]
sources: [csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

A perceptron is a single threshold-gated unit: weight the inputs, sum, and apply a step function. It can represent **exactly the linearly separable functions** — a limitation that famously stalled neural network research.

## The Unit

$$a_i = \text{step}_t\Big(\sum_{j=1}^{n} W_{ij}a_j\Big) = \text{step}_0\Big(\sum_{j=0}^{n} W_{ij}a_j\Big), \quad W_{i0} = t,\; a_0 = -1$$

The threshold is absorbed as a **bias weight** with a constant $-1$ input — the same trick as the augmented vector in [[Linear Models]].

### Activation Functions

| Function | Definition |
|---|---|
| $\text{Step}_t(x)$ | 1 if $x > t$, else 0 |
| $\text{Sign}(x)$ | $+1$ if $x > 0$, else $-1$ |
| $\text{Sigmoid}(x)$ | $1/(1+e^{-x})$ |
| $\tanh(x/2)$ | $(1-e^{-x})/(1+e^{-x})$ |

Note $\text{Step}_t(x) = \text{Step}_0(x - t)$ — which is what licenses folding the threshold into the weights.

## Boolean Gates

Perceptrons can represent basic boolean functions, with $x_0 = -1$:

| Gate | Weights |
|---|---|
| **AND** | $w_0 = 1.5,\; w_1 = 1,\; w_2 = 1$ |
| **OR** | $w_0 = 0.5,\; w_1 = 1,\; w_2 = 1$ |
| **NOT** | $w_0 = -0.5,\; w_1 = -1$ |

Since AND, OR and NOT are functionally complete, **a network of perceptron units can compute any Boolean function.** The deck then asks: *what about XOR or EQUIV?*

## The Geometric Picture

Output is 1 when $w_1x_1 + w_2x_2 - w_0 > 0$. Rearranging (for $w_2 > 0$):

$$x_2 > -\frac{w_1}{w_2}x_1 + \frac{w_0}{w_2}$$

So the unit draws a **line** of slope $-w_1/w_2$ and intercept $w_0/w_2$: **above the line output 1, on or below output 0.** This generalizes to a hyperplane for $n$ inputs.

**The role of the bias**: with $w_0 = 0$ the line must pass through the origin, so learning can only adjust its *slope*. The bias is what lets the boundary translate.

## The Limitation

Only functions whose classes are separable by a linear boundary can be represented. AND and OR are linearly separable; **XOR is not** — no single line divides its two classes.

**Perceptrons cannot represent XOR (Minsky and Papert, 1969).** See [[Linear Separability]].

## Learning Rule

Weights need not be set by hand. Train on (input, output) pairs with

$$W_j \leftarrow W_j + \alpha \times I_j \times \text{Err}, \qquad \text{Err} = \text{DesiredOutput} - \text{NetworkOutput}$$

where $\alpha$ is the learning rate. Note the *predicted minus true* shape — the same form that recurs in [[Backpropagation]] and, in [[CSCE 421]], in [[Logistic Regression]] and [[Softmax Regression]].

## See Also

- [[Linear Separability]]
- [[Backpropagation]]
- [[Neural Networks]]
- [[Linear Models]]
- [[CSCE 420]]
