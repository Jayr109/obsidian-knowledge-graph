---
title: "Overfitting"
type: concept
tags: [csce421, overfitting, generalization, polynomial-regression, model-complexity, rms-error]
sources: [csce421-t04-overfitting]
course: CSCE 421
updated: 2026-09-22
---

Overfitting is fitting the training data so well that the fit stops describing the underlying pattern and starts describing the noise. It is the failure mode that makes [[In-Sample and Out-of-Sample Error|$E_{in}$ and $E_{out}$]] diverge, and the reason minimizing training error is not the same thing as learning.

## The Polynomial Case Study

[[CSCE 421]] demonstrates it with polynomial curve fitting: observe $x$, predict a real target $t$, fit a polynomial of order $M$ by minimizing sum-of-squares error. The order $M$ controls flexibility — how many wiggles the curve is allowed.

| $M$ | Fit quality on the deck's data |
|---|---|
| $0$ (constant) | Rather poor — **underfitting** |
| $1$ (linear) | Rather poor |
| $3$ (cubic) | **Best fit** |
| $9$ | Excellent on training data, oscillates wildly, very poor representation |

The $M = 9$ case is the whole point. With 10 data points, a 9th-order polynomial has exactly enough freedom to pass through every one of them — **training error reaches zero** — and the curve between the points is garbage.

## Why a Perfect Fit Is a Bad Sign

A flexible enough model does not have to choose between the signal and the noise; it can reproduce both. The noise is specific to the sample you happened to draw, so reproducing it is worse than useless on new data.

This is the second failure mode named on [[In-Sample and Out-of-Sample Error]] — $E_{in}$ small, $E_{out}$ large — and it is the one that motivates everything in [[CSCE 421 T04 — Overfitting and Regularization|T04]].

## Diagnosing It: The RMS Curve

Plot **root-mean-square error** against $M$ for training and test sets:

- **Training RMS** falls monotonically — more flexibility always fits the sample better.
- **Test RMS** falls, bottoms out, then rises sharply.

The gap between the two curves *is* the overfitting, and the bottom of the test curve is the model complexity you want. That training error decreases monotonically is exactly why you cannot select $M$ by training error: it would always name the most complex option.

## The Symptom in the Coefficients

The deck shows the fitted coefficients at each $M$. Those for $M = 9$ are **enormous in magnitude with alternating signs** — the wild oscillation is produced by large terms nearly cancelling each other.

This observation is the bridge to the fix. If pathological fits have large coefficients, then penalizing large coefficients should suppress them without reducing $M$ at all. That is [[Regularization]].

## The General Statement

Overfitting is not about polynomials. It is the interaction between three things:

| Factor | Effect |
|---|---|
| Model flexibility | More flexibility, more overfitting risk |
| Amount of data | More data, less risk at the same flexibility |
| Noise in the data | More noise, more there is to spuriously fit |

A [[Multilayer Perceptron|neural network]] with millions of parameters faces the same tension the $M=9$ polynomial does, which is why [[Regularization]] and [[Model Selection]] remain central in [[Deep Learning]].

Contrast with the opposite failure: a [[Linear Models|hypothesis set]] too limited to express the target, where $E_{in}$ never gets small at all. Both are surveyed from the [[CSCE 420]] side in [[Supervised Learning Issues]].

## See Also

- [[Regularization]]
- [[Model Selection]]
- [[In-Sample and Out-of-Sample Error]]
- [[Linear Regression]]
- [[Supervised Learning Issues]]
- [[CSCE 421]]
