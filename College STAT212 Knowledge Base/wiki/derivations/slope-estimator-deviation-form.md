---
title: "Slope Estimator in Deviation Form"
type: derivation
tags: [least-squares, slope, deviations, identity]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-05
---

Shows the slope estimator from the normal equations, $\hat\beta_1 = \dfrac{\sum_i x_i(y_i - \bar y)}{\sum_i x_i(x_i - \bar x)}$, equals the standard **deviation form** $\hat\beta_1 = \dfrac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sum_i (x_i-\bar x)^2}$. The trick is that the extra terms vanish by [[Sum of Deviations Equals Zero]]. **Proved as Problem 3 of the theory assignment** (Problem 2 = [[Least Squares Estimators Derivation]]).

## Numerator: $\sum_i (x_i-\bar x)(y_i-\bar y) = \sum_i x_i(y_i-\bar y)$

| Step | Justification |
|------|---------------|
| $\sum_i (x_i-\bar x)(y_i-\bar y) = \sum_i\big[x_i(y_i-\bar y) - \bar x(y_i-\bar y)\big]$ | MS (expand over $(x_i-\bar x)$) |
| $= \sum_i x_i(y_i-\bar y) - \sum_i \bar x(y_i-\bar y)$ | Move sum |
| $= \sum_i x_i(y_i-\bar y) - \bar x\sum_i (y_i-\bar y)$ | X is constant (pull $\bar x$ out) |
| $= \sum_i x_i(y_i-\bar y) - \bar x\cdot 0$ | Zeros out ($\sum_i(y_i-\bar y)=0$, [[Sum of Deviations Equals Zero]]) |
| $= \sum_i x_i(y_i-\bar y)$ | MS |

## Denominator: $\sum_i (x_i-\bar x)^2 = \sum_i x_i(x_i-\bar x)$

| Step | Justification |
|------|---------------|
| $\sum_i (x_i-\bar x)^2 = \sum_i (x_i-\bar x)(x_i-\bar x)$ | MS ($a^2 = a\cdot a$) |
| $= \sum_i\big[x_i(x_i-\bar x) - \bar x(x_i-\bar x)\big]$ | MS (expand the first factor) |
| $= \sum_i x_i(x_i-\bar x) - \bar x\sum_i (x_i-\bar x)$ | Move sum; X is constant |
| $= \sum_i x_i(x_i-\bar x) - \bar x\cdot 0$ | Zeros out ($\sum_i(x_i-\bar x)=0$) |
| $= \sum_i x_i(x_i-\bar x)$ | MS |

## Combine

$$\hat\beta_1 = \frac{\sum_i x_i(y_i-\bar y)}{\sum_i x_i(x_i-\bar x)} = \frac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sum_i (x_i-\bar x)^2}. \qquad \blacksquare$$

Both numerator and denominator also equal the "raw" forms $\sum_i x_i y_i - n\bar x\bar y$ and $\sum_i x_i^2 - n\bar x^2$.

## See Also
- [[Sum of Deviations Equals Zero]]
- [[Least Squares Estimators Derivation]]
- [[Slope as Correlation Times SD Ratio]]
- [[Correlation Coefficient]]
