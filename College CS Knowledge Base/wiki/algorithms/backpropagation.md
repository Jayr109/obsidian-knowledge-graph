---
title: "Backpropagation"
type: algorithm
tags: [csce420, backpropagation, gradient-descent, chain-rule, multilayer]
sources: [csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
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

## See Also

- [[Neural Networks]]
- [[Perceptron]]
- [[Gradient Descent]]
- [[Deep Learning]]
- [[CSCE 420]]
