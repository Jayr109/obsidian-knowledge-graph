---
title: "Linear Separability"
type: concept
tags: [csce420, linear-separability, xor, perceptron, minsky-papert]
sources: [csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

A function is **linearly separable** if a straight line (or hyperplane in higher dimensions) can divide its classes. This property exactly characterizes what a [[Perceptron]] can represent.

## The Two Data Sets

The deck contrasts two sets of $(x_1, x_2)$ points labelled 0 or 1:

- **Data set 1** — linearly separable: a straight line can be drawn between the classes
- **Data set 2** — not linearly separable: **perceptrons cannot represent such a function**

## The Boolean Cases

Plotting the two inputs $I_0, I_1$ on a square:

| Function | Separable? |
|---|---|
| **AND** | Yes — one corner against three |
| **OR** | Yes — three corners against one |
| **XOR** | **No** |

XOR's true cases are the two *diagonal* corners, and its false cases the other diagonal. No single line separates one diagonal pair from the other.

## Minsky and Papert (1969)

The result is historically loaded. Demonstrating that perceptrons cannot compute XOR — a trivially simple function — contributed to the collapse of funding and interest in neural network research, one of the AI winters described in [[History of AI]].

The resolution was already implicit: [[Perceptron|a *network* of perceptron units can compute any Boolean function]], since AND/OR/NOT are functionally complete. The missing piece was not representational power but a **training procedure for multiple layers** — supplied by [[Backpropagation]], which the deck notes arrived in 1969 and became popular in the 1980s.

## The Modern Reading

Linear separability is a statement about the *representation*, not the problem. Data not separable in its original coordinates may become separable after a feature transformation — which is what hidden layers learn to perform, and the point [[Neural Networks]] makes about the neuron staying linear while the feature map bends the boundary.

## See Also

- [[Perceptron]]
- [[Backpropagation]]
- [[Neural Networks]]
- [[History of AI]]
- [[CSCE 420]]
