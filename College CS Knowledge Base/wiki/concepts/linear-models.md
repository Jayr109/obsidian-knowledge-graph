---
title: "Linear Models"
type: concept
tags: [csce421, linear-models, perceptron, linear-signal, hypothesis-set, machine-learning]
sources: [csce421-t01-linear-regression, csce421-t02-logistic-regression]
course: CSCE 421
updated: 2026-08-25
---

A linear model scores an input by a weighted sum of its features, the **linear signal** $s = \mathbf{w}^T\mathbf{x}$. [[CSCE 421]] treats this as *the* fundamental model and the first one to try: [[Linear Regression]], [[Logistic Regression]], and [[Softmax Regression]] are all the same signal, differing only in what is applied to $s$ and what error measure is minimized.

## The Linear Signal

$$s = \mathbf{w}^T\mathbf{x} = \sum_{i=0}^{d} w_i x_i$$

The signal is linear in two senses, and both matter for different reasons:

| Linear in | Consequence |
|---|---|
| $\mathbf{x}$ | Gives the line / hyperplane separator — the geometric picture |
| $\mathbf{w}$ | **Makes the algorithms work** — the optimization picture |

The second is the one that is easy to overlook. Logistic regression passes $s$ through a nonlinearity, so its *output* is not linear in $\mathbf{x}$; it is still called a linear model because the signal is linear in the parameters and the decision boundary is a hyperplane.

## Weights and the Bias

Running example from the deck: credit approval from age, salary, debt, years in job, years at home. The weights encode importance and direction:

- Input $x_i$ is important $\Rightarrow$ large $|w_i|$
- Input $x_i$ beneficial $\Rightarrow w_i > 0$
- Input $x_i$ detrimental $\Rightarrow w_i < 0$

A raw threshold rule — approve if $\sum_{i=1}^{d} w_i x_i > \text{threshold}$ — is folded into the weight vector by introducing a **bias weight** $w_0 = -\text{threshold}$ and a constant coordinate $x_0 = 1$. This is why $\mathbf{x}$ is the *augmented* vector $\mathbf{x} \in \{1\} \times \mathbb{R}^d$ and $\mathbf{w} \in \mathbb{R}^{d+1}$: the threshold comparison becomes a comparison against zero.

## The Perceptron Hypothesis Set

$$\mathcal{H} = \left\{\, h(\mathbf{x}) = \mathrm{sign}\!\left(\mathbf{w}^T\mathbf{x}\right) \,\right\}$$

A **hypothesis set** is the space of candidate functions learning is allowed to search. This one is called the *perceptron* or *linear separator*. Learning means picking $\mathbf{w}$; the hypothesis set fixes what shapes of decision boundary are reachable at all.

## What Distinguishes the Three Models

| Model | Applied to $s$ | Target | Error measure |
|---|---|---|---|
| Perceptron | $\mathrm{sign}(s)$ | $y = \pm 1$ | Classification error |
| [[Linear Regression]] | nothing — use $s$ directly | $y \in \mathbb{R}$ | Squared error |
| [[Logistic Regression]] | [[Sigmoid Function]] $\theta(s)$ | $y \in [0,1]$ | [[Cross-Entropy Loss]] |
| [[Softmax Regression]] | [[Softmax Function]] over $K$ signals | distribution over $K$ classes | Cross-entropy |

## Features

A **feature** is an important property of the input believed useful for classification. Feature choice changes the input dimension dramatically: raw $16\times16$ digit images give $\dim = 257$, while hand-designed intensity and symmetry features give $\dim = 3$. Replacing hand-designed features with learned ones is exactly the step from linear models to [[Deep Learning]].

## See Also

- [[Linear Regression]]
- [[Logistic Regression]]
- [[Softmax Regression]]
- [[Neural Networks]]
- [[CSCE 421]]
