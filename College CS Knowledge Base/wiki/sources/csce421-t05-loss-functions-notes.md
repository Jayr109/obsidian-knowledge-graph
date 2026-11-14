---
title: "CSCE 421 T05 Notes — A Unified View of Loss Functions"
type: source
tags: [notes, csce421, loss-functions, convexity, margin, linear-classifier]
sources: []
course: CSCE 421
updated: 2026-09-22
---

Companion typed note to [[CSCE 421 T05 — A Unified View of Loss Functions in Supervised Learning]]. 4 pages, by **Shuiwang Ji** (Texas A&M), **Lei Cai** (Washington State University), and **Hao Yuan** (Texas A&M). Stated purpose: *"providing an introduction of different loss functions for supervised learning and shedding light on their differences and similarities... based on lecture notes by Shuiwang Ji... can be used for undergraduate and graduate level classes."*

## Relation to the Slides

The note and the deck cover **the same six losses with the same equations and the same comparison paragraph** — this is not a derivations supplement in the way the [[CSCE 421 T03 Notes — Softmax Regression Derivations|T03 notes]] were. Read either. Two differences are worth knowing:

**1. The bias is explicit.** The note writes the linear score as

$$s_i = \mathbf{w}^T\mathbf{x}_i + b \tag{1}$$

with $x_i \in \mathbb{R}^d$ and $b$ named separately as the bias, where the slides fold it in via the augmented vector ($x_i \in \mathbb{R}^{d+1}$, no separate $b$). Same model, two conventions — see [[Linear Models]] on the bias-folding trick.

**2. Scope is stated.** *"We describe these loss functions in the context of linear classifiers, but they can also be used for nonlinear classifiers."* The losses are independent of what computes $s_i$ — which is exactly why they carry over unchanged to [[Multilayer Perceptron|neural networks]] in T06.

## The Figures

The note's two figures are the ones the deck shows without text:

- **Figure 1** — graphical illustrations of each loss function individually.
- **Figure 2** — all losses overlaid on one plot of loss against $y_i s_i$, the "unified view" the title refers to.

These are the most useful artifact in either document: they make the six conclusions of the comparison section visible at a glance. See `raw/CSCE421_T05-loss-notes.pdf`.

## Content Index

| Section | Content |
|---|---|
| 2 | Linear classifier, equation (1) |
| 3 | Zero-one loss, equations (2)–(3) |
| 4 | Perceptron loss, equations (4)–(5) |
| 5 | Square loss, equations (6)–(7) |
| 6 | Log loss, equations (8)–(9) |
| 7 | Hinge loss, equations (10)–(11) |
| 8 | Exponential loss, equations (12)–(13) |
| 9 | Convexity |
| 10 | Comparison of loss functions |

All equations are reproduced on [[Loss Functions]].

## See Also

- [[CSCE 421 T05 — A Unified View of Loss Functions in Supervised Learning]]
- [[Loss Functions]]
- [[Convexity]]
- [[Linear Models]]
- [[CSCE 421]]
