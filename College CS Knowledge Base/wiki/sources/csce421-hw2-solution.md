---
title: "CSCE 421 HW2 Solutions — Loss Functions, Backpropagation, MLP"
type: source
tags: [homework, solutions, csce421, backpropagation, loss-functions, hinge-loss, mlp, parameter-counting]
sources: []
course: CSCE 421
updated: 2026-10-20
---

Instructor-released solution key for Homework 2 of [[CSCE 421]], Fall 2026. 3 pages, 100 points across four questions. Covers [[Loss Functions]] (T05), a fully worked [[Backpropagation]] example from *Learning From Data* (T06), parameter counting, and a PyTorch MLP implementation.

**Q2 is the most valuable item in the key** — it is the only place in the course where the sensitivity notation of [[CSCE 421 T06 — Multi-Layer Perceptron/Networks|T06]] is carried through on actual numbers.

## Q1 — Loss Functions (10 pts)

**(1) State hinge, logistic and 0-1 loss, and compare them** using *"the unified picture we developed in class"*, with `s = w^T x + b`:

```
(a) hinge loss:    loss = max(0, 1 - ys)
(b) logistic loss: loss = ln(1 + exp(-ys))
(c) 0-1 loss:      loss = 1  if ys < 0,  else 0
```

> **Similarity:** hinge loss and logistic regression loss are **convex**.
>
> **Difference:** 0/1 loss is **not convex**. Logistic loss is **differentiable on every point**. 0/1 loss is **not differentiable at point 0**. Hinge loss is **not differentiable at point 1**. **0/1 loss and hinge loss will be exactly zero when ys >= 1**, while logistic loss will not.

Note the answer is organized on the margin `ys`, exactly as [[CSCE 421 T05 — A Unified View of Loss Functions in Supervised Learning|T05]] sets it up. Note also that the question uses `s = w^T x + b` with an explicit bias — the **notes** convention rather than the slides' augmented-vector convention.

**(2) Why is an SVM's boundary unaffected by a correctly classified point far from the boundary, while logistic regression's is affected?**

> Since a point is correctly classified and distant from the decision boundary, then `ys >> 1`. In **hinge loss, it will be zero**, so it's unaffected. While in **logistic loss, it's bigger than zero**, so it's affected.

This is the practical consequence of the flat-versus-asymptotic distinction in [[Loss Functions]], and it is the reason support vector machines are named after the few points that *do* matter.

## Q2 — Backpropagation by Hand (20 pts)

*Exercise 7.8 (e-Chap:7-15) in LFD.* Given

```
W(1) = [[0.1, 0.2],        W(2) = [[ 0.2],       W(3) = [[1],
        [0.3, 0.4]]                [ 1.0],               [2]]
                                   [-3.0]]
x(0) = [1, 2]^T,   y = 1,   theta = tanh on hidden layers, identity on output
```

> **Typo in the key:** the third weight matrix is printed as `W(1) = (1 2)` on page 1. It is `W(3)`, as the forward pass immediately uses it that way. (Page 1 also reads *"Forward propagation fives"* for *"gives"*.)

### Forward propagation

```
s(1) = W(1)^T x(0) = [[0.1, 0.3], [0.2, 0.4]] [1, 2]^T = [0.7, 1]^T
x(1) = [1, tanh(s(1))] = [1, 0.60, 0.76]^T

s(2) = W(2)^T x(1) = [0.2, 1, -3] [1, 0.60, 0.76]^T = [-1.48]
x(2) = [1, tanh(s(2))] = [1, -0.90]^T

s(3) = W(3)^T x(2) = [1, 2] [1, -0.90]^T = [-0.80]
x(3) = s(3) = [-0.80]                                    (identity output)
```

### Backpropagation

With `e = (x(3) - y)^2`:

```
delta(3) = 2(x(3) - y) theta'(s(3)) = 2 * (-0.8 - 1) * 1 = -3.6     because theta(s(3)) = s(3)

delta(2) = theta'(s(2)) W(3) delta(3)
         = (1 - (x(2))^2) * 2 * (-3.6) = (1 - (-0.9)^2) * 2 * (-3.6) = -1.368

delta(1) = theta'(s(1)) W(2) delta(2)
         = [ (1 - 0.6^2)  * 1    * (-1.368),
             (1 - 0.76^2) * (-3) * (-1.368) ]  =  [-0.876, 1.734]
```

Two mechanics worth extracting. First, `theta'(s) = 1 - tanh^2(s) = 1 - x^2`, so **the forward-pass activation is reused directly** — the same efficiency the sigmoid gives in [[Backpropagation]]. Second, the weight matrix used to pull `delta` backward **excludes the bias row**: `W(3)` contributes only its `2`, and `W(2)` only its `[1, -3]`, because the constant 1 has no incoming signal to be sensitive to.

### Gradients

```
de/dW(1) = x(0) delta(1)^T = [1,2]^T [-0.876, 1.734]  = [[-0.876, 1.734], [-1.752, 3.468]]

de/dW(2) = x(1) delta(2)^T = [1, 0.6, 0.76]^T [-1.368] = [-1.368, -0.821, -1.04]^T

de/dW(3) = x(2) delta(3)^T = [1, -0.9]^T [-3.6]        = [-3.6, 3.24]^T
```

Every one is the **outer product** `x^(l-1) (delta^(l))^T` from T06 slide 18.

> **Verified independently.** Recomputing this in full floating-point precision gives `delta(3) = -3.6062`, `delta(2) = -1.3503`, `delta(1) = [-0.8571, 1.7012]`. The method and every structural step in the key are correct; the small differences arise because **the key rounds intermediates to two decimals and propagates the rounded values** — its `delta(2)` uses `1 - 0.90^2 = 0.19` where the exact value is `1 - 0.9015^2 = 0.1873`. Reproducing this by hand, round the same way to match; in code, expect the exact figures.

## Q3 — Parameter Counting (10 pts)

> Fully-connected network with **5 hidden layers, each with 10 hidden units** (`d(l) = 10`). Input is **20-dimensional**, output is a **scalar**. Total trainable parameters, **including bias**?

```
(21 x 10) + (11 x 10) + (11 x 10) + (11 x 10) + (11 x 10) + (11 x 1) = 661
```

The rule: each layer contributes `(fan_in + 1) x fan_out`, the `+1` being the bias. So `20 -> 10` costs `21 x 10 = 210`, each `10 -> 10` costs `11 x 10 = 110` (four of them), and `10 -> 1` costs `11`. **Confirmed: 210 + 440 + 11 = 661.**

This is the `(d^(l-1) + 1) x d^(l)` shape of `W^(l)` from [[Multilayer Perceptron]], used as an arithmetic exercise.

## Q4 — PyTorch MLP (60 pts)

> 1. Need to follow the instructions to implement MLP correctly using **pytorch**.
> 2. Write your own evaluation code and **load the best training checkpoint** to evaluate on the test set.
> 3. Need to try **different hidden sizes** and report corresponding accuracies on the **validation set**, as well as the best model's accuracy on the test set. The best test accuracy you can achieve is **at least 86%**.

Point 3 is [[Model Selection]] as an assignment requirement — hidden size is the hyperparameter, the validation set chooses it, the test set is touched once at the end.

## See Also

- [[Backpropagation]]
- [[Multilayer Perceptron]]
- [[Loss Functions]]
- [[Convexity]]
- [[Model Selection]]
- [[CSCE 421]]
