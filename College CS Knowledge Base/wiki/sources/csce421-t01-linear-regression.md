---
title: "CSCE 421 T01 — Introduction and Linear Regression"
type: source
tags: [lecture, csce421, linear-regression, perceptron, least-squares, supervised-learning]
sources: []
course: CSCE 421
updated: 2026-08-25
---

Topic deck 1 of [[CSCE 421]], by [[Shuiwang Ji]], based on *Learning From Data*. 20 slides. Motivates machine learning by contrast with arithmetic, introduces the [[Linear Models|linear model]] and perceptron hypothesis set, then derives least-squares [[Linear Regression]] in closed form.

## Framing: What Needs Learning?

Two opening questions set up the course:

1. A large multiplication, $213621.36521 \times 142513.54 / 1254.3215$ — **does this require intelligence?** No; it is arithmetic.
2. *Is there a tree in the photo?* (Y/N, or $\pm 1$) — this cannot be reduced to a written rule.

**Learning from data** is the answer to the second: write a program with free parameters, show it examples with desired outputs, and tweak the parameter values when the output is wrong.

## Paradigms

| Paradigm | Mapping | Sub-types |
|---|---|---|
| **Supervised** | $x \to y$ | *Classification* ($y$ discrete, binary or multi-class); *Regression* ($y$ continuous) |
| **Unsupervised** | $x$ only | Clustering, density estimation |
| **Reinforcement** | Sequential decision making | Noted as useful in training LLMs |

See [[Machine Learning Paradigms]].

## Three Learning Problems

The deck's framing claims, stated plainly:

- Linear models are *perhaps the fundamental model* — and the first model to try.
- **Logistic regression is a wrong name**: its training data have discrete $y$, but it makes probabilistic predictions.
- Logistic regression is a linear model, *though it may not be obvious*.

## The Linear Model and Perceptron

Running example: credit approval from features (age, salary, debt, years in job, years at home). Weight each input and sum to a "Credit Score" $\sum_{i=1}^{d} w_i x_i$; approve above a threshold, deny below.

Weight interpretation: important input $\Rightarrow$ large $|w_i|$; beneficial $\Rightarrow w_i > 0$; detrimental $\Rightarrow w_i < 0$.

Folding the threshold into a bias weight $w_0$ gives the **perceptron hypothesis set**

$$\mathcal{H} = \{\, h(\mathbf{x}) = \mathrm{sign}(\mathbf{w}^T\mathbf{x}) \,\}, \quad \mathbf{w} \in \mathbb{R}^{d+1},\ \mathbf{x} \in \{1\} \times \mathbb{R}^d$$

The deck stresses the dual reading of the **linear signal**: linear in $\mathbf{x}$ gives the line/hyperplane separator; linear in $\mathbf{w}$ is *what makes the algorithms work*. See [[Linear Models]].

## Linear Regression

Same credit features, different target: instead of Approve/Deny, predict the **credit line** in dollars — so $y \in \mathbb{R}$ and $h(\mathbf{x}) = \mathbf{w}^T\mathbf{x}$, with no sign function.

Error measures:

$$E_{in}(h) = \frac{1}{N}\sum_{n=1}^{N}(h(\mathbf{x}_n) - y_n)^2, \qquad E_{out}(h) = \mathbb{E}_x\left[(h(\mathbf{x}) - y)^2\right]$$

See [[In-Sample and Out-of-Sample Error]].

## Closed-Form Solution

In matrix form $E_{in}(\mathbf{w}) = \frac{1}{N}\lVert X\mathbf{w} - \mathbf{y}\rVert_2^2$. Using $\nabla_w(\mathbf{w}^T\mathbf{b}) = \mathbf{b}$ and $\nabla_w(\mathbf{w}^TA\mathbf{w}) = (A + A^T)\mathbf{w}$, setting the gradient to zero gives the **normal equations** $X^TX\mathbf{w} = X^T\mathbf{y}$, hence $\mathbf{w}_{lin} = (X^TX)^{-1}X^T\mathbf{y}$ when $X^TX$ is invertible.

Full derivation and the three-step algorithm on [[Linear Regression]].

## See Also

- [[Linear Regression]]
- [[Linear Models]]
- [[In-Sample and Out-of-Sample Error]]
- [[Machine Learning Paradigms]]
- [[CSCE 421]]
- [[Shuiwang Ji]]
