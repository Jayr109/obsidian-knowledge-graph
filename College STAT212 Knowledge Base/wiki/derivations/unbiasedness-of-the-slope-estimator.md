---
title: "Unbiasedness of the Slope Estimator"
type: derivation
tags: [slope, unbiased, expectation, inference]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Proves that $E(\hat\beta_1) = \beta_1$, i.e. the least-squares slope is an unbiased estimator (Property 1 of the [[Sampling Distribution of the Slope Estimator]]). Uses the model $Y_i = \beta_0 + \beta_1 x_i + \epsilon_i$ with $E(\epsilon_i) = 0$.

## Simplify the numerator of $\hat\beta_1$

$\hat\beta_1 = \dfrac{\sum_i (x_i - \bar x)(Y_i - \bar Y)}{\sum_i (x_i - \bar x)^2}$.

| Step | Justification |
|------|---------------|
| Numerator $= \sum_i (x_i - \bar x)Y_i - \bar Y \sum_i (x_i - \bar x)$ | Move sum (split the product) |
| $\sum_i (x_i - \bar x) = 0$, so numerator $= \sum_i (x_i - \bar x)Y_i$ | Zeros out ($\sum(x_i-\bar x)=0$) |

## Substitute the model for $Y_i$

| Step | Justification |
|------|---------------|
| $\sum_i (x_i-\bar x)Y_i = \sum_i (x_i-\bar x)(\beta_0 + \beta_1 x_i + \epsilon_i)$ | BD (model equation) |
| $= \beta_0\sum_i (x_i-\bar x) + \beta_1\sum_i x_i(x_i-\bar x) + \sum_i \epsilon_i(x_i-\bar x)$ | Move sum (distribute over 3 terms) |
| $= \beta_1 \sum_i (x_i-\bar x)^2 + \sum_i \epsilon_i(x_i-\bar x)$ | Zeros out ($\beta_0$ term $=0$; $\sum x_i(x_i-\bar x)=\sum(x_i-\bar x)^2$) |

## Divide by $\sum_i (x_i - \bar x)^2$

| Step | Justification |
|------|---------------|
| $\hat\beta_1 = \beta_1 + \dfrac{\sum_i \epsilon_i(x_i-\bar x)}{\sum_i (x_i-\bar x)^2}$ | MS (divide through) |
| $E(\hat\beta_1) = \beta_1 + \dfrac{\sum_i (x_i-\bar x)E(\epsilon_i)}{\sum_i (x_i-\bar x)^2}$ | Rule of Expectations ($x_i$ constant, linearity); X is constant |
| $E(\hat\beta_1) = \beta_1$ | Zeros out ($E(\epsilon_i)=0$) |

## Result

$$E(\hat\beta_1) = \beta_1. \qquad \blacksquare$$

## See Also
- [[Sampling Distribution of the Slope Estimator]]
- [[Rules of Expectation and Variance]]
- [[Least Squares Estimators Derivation]]
