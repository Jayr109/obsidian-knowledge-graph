---
title: "ANOVA Decomposition of SST"
type: derivation
tags: [ANOVA, sums-of-squares, R-squared]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Proves the fundamental identity $SST = SSE + SSR$ behind the [[Coefficient of Determination]]. The trick is [[Rules of Expectation and Variance|Add 0]] ($y_i - \bar y = (y_i - \hat y_i) + (\hat y_i - \bar y)$), expand the square, and show the cross term vanishes.

## Setup

Recall $SST = \sum_i (y_i - \bar y)^2$, $SSE = \sum_i (y_i - \hat y_i)^2$, $SSR = \sum_i (\hat y_i - \bar y)^2$, and from [[Least Squares Estimators Derivation]] that $\hat y_i = \hat\beta_0 + \hat\beta_1 x_i = \bar y - \hat\beta_1\bar x + \hat\beta_1 x_i$.

## Expanding SST

| Step | Justification |
|------|---------------|
| $SST = \sum_i (y_i - \hat y_i + \hat y_i - \bar y)^2$ | Add 0 (insert $-\hat y_i + \hat y_i$) |
| $= \sum_i (y_i - \hat y_i)^2 + \sum_i (\hat y_i - \bar y)^2 + 2\sum_i (y_i - \hat y_i)(\hat y_i - \bar y)$ | MS (expand square, Move sum onto each term) |
| $= SSE + SSR + 2\sum_i (y_i - \hat y_i)(\hat y_i - \bar y)$ | BD (definitions of SSE, SSR) |

## The cross term is 0

Two facts from the fitted line: $\hat y_i - \bar y = \hat\beta_1 (x_i - \bar x)$ and $y_i - \hat y_i = (y_i - \bar y) - \hat\beta_1(x_i - \bar x)$.

| Step | Justification |
|------|---------------|
| $\sum_i (y_i - \hat y_i)(\hat y_i - \bar y) = \sum_i \big[(y_i-\bar y) - \hat\beta_1(x_i-\bar x)\big]\,\hat\beta_1(x_i-\bar x)$ | BD (substitute both facts) |
| $= \hat\beta_1 \sum_i (x_i-\bar x)(y_i-\bar y) - \hat\beta_1^2 \sum_i (x_i-\bar x)^2$ | Move sum (distribute) |
| $= \hat\beta_1^2 \sum_i (x_i-\bar x)^2 - \hat\beta_1^2 \sum_i (x_i-\bar x)^2$ | BD (since $\hat\beta_1 = \tfrac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2}$) |
| $= 0$ | Zeros out |

## Result

$$SST = SSE + SSR = SSE + \sum_{i=1}^n (\hat y_i - \bar y)^2.$$

## See Also
- [[Coefficient of Determination]]
- [[Least Squares Estimators Derivation]]
