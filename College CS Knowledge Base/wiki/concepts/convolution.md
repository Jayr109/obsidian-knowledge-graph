---
title: "Convolution"
type: concept
tags: [csce421, convolution, image-filtering, sobel, edge-detection, kernel, stride, padding]
sources: [csce421-t08-convolution, csce421-t09-cnn]
course: CSCE 421
updated: 2026-10-20
---

Convolution slides a small array of weights — a **kernel** or **filter** — over an input, computing a dot product at every position. [[CSCE 421]] introduces it twice: first as classical image filtering with hand-designed kernels ([[CSCE 421 T08 — Convolution|T08]]), then as a learned layer ([[CSCE 421 T09 — Convolutional Neural Networks|T09]]). The pedagogical point is that **only the source of the numbers changes.**

## The Operation

Place the kernel over a window of the input, multiply elementwise, sum to one output value, move, repeat. For a $3\times3$ kernel $w$ over an image $x$:

$$y(i,j) = \sum_{u=-1}^{1}\sum_{v=-1}^{1} w(u,v)\, x(i+u,\, j+v)$$

Each output pixel is a weighted sum of its neighborhood — the [[Linear Models|linear signal]] $\mathbf{w}^T\mathbf{x}$ again, applied to a local patch instead of the whole input.

## What the Kernel Decides

T08 makes the point with four worked kernels:

| Kernel | Effect |
|---|---|
| all ones | **Box filter** — *"replaces each pixel with an average of its neighborhood"*, smoothing |
| 1 in the center, else 0 | identity, *"no change"* |
| 1 offset from center | translation, *"shifted left by 1 pixel"* |
| Sobel (below) | edge detection |

**The numbers in the kernel are the whole operation.** That is exactly why learning them is a sensible thing to do.

## Sobel Filters

$$\text{vertical edges: } \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1\end{bmatrix} \qquad \text{horizontal edges: } \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1\end{bmatrix}$$

Each is the transpose of the other. The structure is a **signed difference across the center**: a region of constant brightness sums to zero, so only a *change* in intensity produces a response. The centre weight of $2$ smooths along the edge while differencing across it. T08 shows both with *"(absolute value)"* — the raw response is signed, and the magnitude is what gets displayed.

## Spatial Arithmetic

T09 turns the operation into arithmetic you can be examined on. For input size $N$, filter size $F$:

$$\text{output size} = \frac{N - F}{\text{stride}} + 1$$

$$\text{with padding } P: \qquad \frac{N + 2P - F}{\text{stride}} + 1$$

A **non-integer result means the configuration is invalid** — the filter does not fit. T09 shows $N=7, F=3$ at stride 3 giving $2.33$ and notes it *"doesn't fit."*

To preserve spatial size, pad with

$$P = \frac{F-1}{2} \qquad (F=3 \to P=1,\; F=5 \to P=2,\; F=7 \to P=3)$$

which matters because *"32x32 input convolved repeatedly with 5x5 filters shrinks volumes spatially (32 → 28 → 24 …). Shrinking too fast is not good."*

## The Three Properties That Earn It a Layer

**Translation equivariance.** *"Process each window in the same way, apply the same weights regardless of the window location."* Shift the input, and the output shifts identically — the response *"does not depend on x."* An edge is an edge wherever it appears, so the detector should not need relearning per position.

**Parameter sharing.** T09 draws one figure three ways: convolution needs 3 parameters where locally-connected needs 12 and fully-connected needs 24, both *"no weight-sharing."* A filter is reused at every position instead of each position learning its own weights.

**Locality.** Written as a matrix, convolution is $y = Wx$ with $W$ **sparse** and its nonzero entries **tied** to each other across rows. It is a fully connected layer with most weights forced to zero and the rest forced to be equal.

## Receptive Field

The region of input that can influence one output. A single kernel of size 3 gives a receptive field of 3; stacking another gives 5; adding stride 2 gives 7. *"Composing many conv layers can create a large receptive field"* — depth buys global context without any single layer being global.

## The Step That Makes It Learning

T08's closing slide:

> Convolutional neural networks are based on the idea of image convolutions. Convolutional neural networks **use data to train filter parameters**.

A Sobel kernel is nine numbers a human chose. A CNN runs identical machinery with nine numbers found by [[Gradient Descent]]. This is the concrete answer to *"how to learn x automatically?"* posed at the end of [[CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class|T03]], and the substitution [[Linear Models]] identifies as the move from hand-designed features to [[Deep Learning]].

## See Also

- [[Convolutional Neural Networks]]
- [[CNN Architectures]]
- [[Linear Models]]
- [[Deep Learning]]
- [[CSCE 421]]
