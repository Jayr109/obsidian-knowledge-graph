---
title: "CSCE 421"
type: course
tags: [csce421, machine-learning, course, linear-models]
sources: [csce421-t01-linear-regression, csce421-t02-logistic-regression, csce421-t03-softmax-regression, csce421-t03-softmax-regression-notes]
course: CSCE 421
updated: 2026-08-27
---

CSCE 421 (Machine Learning) is Texas A&M's undergraduate machine learning course, taught by [[Shuiwang Ji]]. The lecture material is built on Abu-Mostafa, Magdon-Ismail & Lin's *Learning From Data*, and the opening arc is deliberately linear: every model in the first three topics is a linear model, differing only in what the linear signal $s = \mathbf{w}^T\mathbf{x}$ is passed through and what error measure is minimized.

## Logistics

- **Instructor:** [[Shuiwang Ji]] (Department of Computer Science & Engineering)
- **Primary text:** *Learning From Data* (Abu-Mostafa, Magdon-Ismail & Lin)
- Supplementary typed notes are distributed alongside the slides; the softmax notes were compiled by Yaochen Xie from Ji's lecture notes

## Topic Arc (T01–T03)

The first three topic decks form one continuous argument:

| Deck | Model | Output | Error measure | Optimizer |
|---|---|---|---|---|
| **T01** | [[Linear Regression]] | $y \in \mathbb{R}$ | Squared error | Closed form (pseudoinverse) |
| **T02** | [[Logistic Regression]] | $y \in [0,1]$, data $\pm 1$ | [[Cross-Entropy Loss]] | [[Gradient Descent]] / SGD |
| **T03** | [[Softmax Regression]] | Distribution over $K$ classes | Cross-entropy | Gradient descent |

The through-line: all three share the [[Linear Models|linear signal]] $\mathbf{w}^T\mathbf{x}$. T01 uses it raw, T02 squashes it with the [[Sigmoid Function]], T03 generalizes that to the [[Softmax Function]] over $K$ signals. T03 closes by proving the binary case is exactly the $K=2$ case of the multi-class one.

## Framing

The course opens by separating tasks that need arithmetic from tasks that need learning: a large multiplication is not intelligence, but answering *"is there a tree in this photo?"* cannot be written down as a rule. Learning from data means writing a program with free parameters and tuning them from labeled examples.

See [[Machine Learning Paradigms]] for the supervised/unsupervised/reinforcement split as this course frames it.

## Ingested Sources

- [[CSCE 421 T01 — Introduction and Linear Regression]] — 20 slides
- [[CSCE 421 T02 — Logistic Regression for Binary Classification]] — 30 slides
- [[CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class]] — 20 slides
- [[CSCE 421 T03 Notes — Softmax Regression Derivations]] — 6-page typed notes carrying the derivations the slides omit

Decks are numbered by topic (T01, T02, ...), not by lecture date. Some ship a companion notes PDF; ingest both when present.

## See Also

- [[Linear Models]]
- [[Linear Regression]]
- [[Logistic Regression]]
- [[Softmax Regression]]
- [[Gradient Descent]]
- [[Machine Learning Paradigms]]
- [[Shuiwang Ji]]
