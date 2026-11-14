---
title: "Convexity"
type: concept
tags: [csce421, convexity, optimization, loss-functions, global-minimum, gradient-descent]
sources: [csce421-t05-loss-functions, csce421-t05-loss-functions-notes]
course: CSCE 421
updated: 2026-09-22
---

Convexity is the property that decides whether [[Gradient Descent]] can be trusted. [[CSCE 421]] introduces it formally in T05 as the criterion separating usable loss functions from unusable ones, after leaning on it informally since T01.

## Definition

A function $f(\cdot)$ is **convex** if

$$f\left(tx_1 + (1-t)x_2\right) \le t f(x_1) + (1-t) f(x_2), \qquad t \in [0,1]$$

and **strictly convex** if

$$f\left(tx_1 + (1-t)x_2\right) < t f(x_1) + (1-t) f(x_2), \qquad t \in (0,1),\; x_1 \ne x_2$$

## The Intuition

> A function is convex if the **line segment between any two points on the function is not below the function**. A function is strictly convex if the line segment between any two distinct points is strictly above the function, except for the two points themselves.

Read the definition against that picture: the left side is the function evaluated at a point *between* $x_1$ and $x_2$; the right side is the straight line connecting $f(x_1)$ to $f(x_2)$, evaluated at the same place. Convexity says the function never rises above its own chords — it holds water.

The difference between convex and **strictly** convex is whether flat segments are allowed. A straight line is convex but not strictly convex, since the chord lies exactly *on* it.

## Why It Matters for Learning

A convex function has **no local minima that are not global minima**. That single fact is what licenses gradient descent:

| Surface | What gradient descent finds |
|---|---|
| Convex | **The** minimum — wherever you start |
| Non-convex | *A* local minimum — depends on initialization |

This is why the deck's remark about [[Logistic Regression]] mattered — *"our $E_{in}$ has only one valley"* — and why squared error composed with a sigmoid was rejected in T02 for being non-convex despite being a correct expression of the goal.

## Convexity of the Losses

From the T05 comparison:

| Loss | Convex | Strictly convex |
|---|---|---|
| Zero-one | **No** | — |
| Perceptron | Yes | **No** |
| Hinge | Yes | **No** |
| Square | Yes | Yes |
| Log | Yes | Yes |
| Exponential | Yes | Yes |

Two observations the deck draws out:

**Zero-one loss is the only non-convex one**, and it is precisely the quantity you want to minimize. It is a step function — flat regions with zero gradient, and a discontinuity with no derivative. Nothing to descend. Every other loss in [[Loss Functions]] exists as a **convex surrogate** for it.

**Hinge and perceptron loss are convex but not strictly convex** because of their flat region: both are exactly zero over a range of margins. A non-strictly-convex function can have a whole *set* of minimizers rather than a unique one — every $\mathbf{w}$ in that set is equally optimal.

## The Limit of Convexity

Convexity runs out at [[Multilayer Perceptron|neural networks]]. Composing layers destroys it even when the loss itself is convex, which is why T06 states that gradient descent on a network reaches a **local minimum**, with no promise it is global. Convexity is a property of the first half of the course, and its absence defines the second.

## See Also

- [[Loss Functions]]
- [[Gradient Descent]]
- [[Logistic Regression]]
- [[Multilayer Perceptron]]
- [[CSCE 421]]
