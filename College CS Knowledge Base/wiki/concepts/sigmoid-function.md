---
title: "Sigmoid Function"
type: concept
tags: [csce421, sigmoid, logistic-function, activation, probability, monotonic]
sources: [csce421-t02-logistic-regression, csce421-t03-softmax-regression, csce421-t03-softmax-regression-notes]
course: CSCE 421
updated: 2026-08-25
---

The sigmoid (logistic) function squashes a real-valued [[Linear Models|linear signal]] into $(0,1)$ so it can be read as a probability. It is what turns a linear signal into [[Logistic Regression]], and is the $K=2$ special case of the [[Softmax Function]].

## Definition

$$\theta(s) = \frac{e^s}{1+e^s} = \frac{1}{1+e^{-s}}, \qquad s \in \mathbb{R}$$

## The Three Properties

[[CSCE 421]] poses these as a question — *why are they important?* — and answers it:

| Property | Why it matters |
|---|---|
| $0 < \theta(s) < 1$ for all $s$ | **Probabilistic interpretation** — output is always a valid probability |
| $\theta(-s) = 1 - \theta(s)$ | **Compact representation** — lets $P(y\mid\mathbf{x})$ collapse to $\theta(y\,\mathbf{w}^T\mathbf{x})$ |
| $\theta$ is monotonic (increasing) | **Order preserved** — thresholding $\theta$ is the same as thresholding $s$, so the model stays linear |

Each property does real work later, which is the point of asking:

- Property 1 is what licenses reading $h(\mathbf{x})$ as $P[y=+1\mid\mathbf{x}]$ at all.
- Property 2 is the step that makes the [[Maximum Likelihood Estimation|maximum-likelihood]] derivation of [[Cross-Entropy Loss]] go through — without it, the $y=+1$ and $y=-1$ cases could not be merged into one expression.
- Property 3 is the answer to *"is logistic regression a linear model?"* — since $\theta$ preserves order, the decision boundary $\theta(\mathbf{w}^T\mathbf{x}) = 0.5$ is exactly the hyperplane $\mathbf{w}^T\mathbf{x} = 0$.

## Why the Model Is Still Linear

This is the subtlety the lecture flags as "may not be obvious." The *output* $\theta(\mathbf{w}^T\mathbf{x})$ is a nonlinear function of $\mathbf{x}$. But:

- the signal $\mathbf{w}^T\mathbf{x}$ is linear in both $\mathbf{x}$ and $\mathbf{w}$, and
- $\theta$ is a fixed, monotonic, parameter-free squashing applied afterward.

So the decision boundary remains a hyperplane. The nonlinearity rescales confidence, not geometry.

## Relation to Softmax

Softmax generalizes sigmoid to $K$ classes. At $K=2$, after using shift-invariance to subtract $\mathbf{w}_1$, the two-class softmax reduces exactly to $[\,\theta(\hat{\mathbf{w}}^T\mathbf{x}),\ 1-\theta(\hat{\mathbf{w}}^T\mathbf{x})\,]$ with $\hat{\mathbf{w}} = \mathbf{w}_1 - \mathbf{w}_2$. Proof on [[Softmax Regression]].

Note the consequence of Property 2: in the binary case **only one probability need be estimated**, since the two sum to one. That is the $K-1$ independent weight vectors rule at $K=2$.

## As an Activation Function

In the single-neuron view of [[Logistic Regression]], $\theta$ is the activation. Its derivative $\theta'(s) = \theta(s)(1-\theta(s))$ is the $K=2$ case of the softmax Jacobian $p_i(\delta_{ij}-p_j)$ derived in [[CSCE 421 T03 Notes — Softmax Regression Derivations]].

## See Also

- [[Softmax Function]]
- [[Logistic Regression]]
- [[Cross-Entropy Loss]]
- [[Linear Models]]
- [[Neural Networks]]
- [[CSCE 421]]
