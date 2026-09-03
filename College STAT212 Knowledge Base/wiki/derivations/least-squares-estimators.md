---
title: "Least Squares Estimators Derivation"
type: derivation
tags: [least-squares, calculus, normal-equations]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Derives the [[Least Squares Estimation|least squares estimators]] $\hat\beta_0$ and $\hat\beta_1$ by minimizing $f(b_0, b_1) = \sum_{i=1}^n [y_i - (b_0 + b_1 x_i)]^2$. Set the two partial derivatives to zero (the *normal equations*) and solve.

## Step-by-step

| Step | Justification |
|------|---------------|
| $f(b_0,b_1) = \sum_i [y_i - (b_0 + b_1 x_i)]^2$ | BD (least squares objective) |
| $\dfrac{\partial f}{\partial b_0} = 2\sum_i [y_i - (b_0 + b_1 x_i)](-1)$ | MS (chain rule, $\partial/\partial b_0$) |
| $\dfrac{\partial f}{\partial b_1} = 2\sum_i [y_i - (b_0 + b_1 x_i)](-x_i)$ | MS (chain rule, $\partial/\partial b_1$) |
| Set $\partial f/\partial b_0 = 0 \Rightarrow \sum_i [y_i - (b_0 + b_1 x_i)] = 0$ | MS (divide by $-2$) |
| $\Rightarrow \sum_i y_i - n b_0 - b_1 \sum_i x_i = 0$ | Move sum (distribute $\Sigma$ over each term) |
| $\Rightarrow b_0 = \bar y - b_1 \bar x$ | MS (divide by $n$; $\bar y = \tfrac1n\sum y_i$) |
| Set $\partial f/\partial b_1 = 0 \Rightarrow \sum_i x_i[y_i - (b_0 + b_1 x_i)] = 0$ | MS (divide by $-2$) |
| Substitute $b_0 = \bar y - b_1\bar x$ and solve | BD (insert result above) |
| $b_1 = \dfrac{\sum_i (x_i - \bar x)(y_i - \bar y)}{\sum_i (x_i - \bar x)^2} = \hat\beta_1$ | MS (algebra on normal equations) |
| $\hat\beta_0 = \bar y - \hat\beta_1 \bar x$ | BD (best $b_0$ given $\hat\beta_1$) |

## Result

$$\hat\beta_1 = \frac{\sum_i (x_i - \bar x)(y_i - \bar y)}{\sum_i (x_i - \bar x)^2}, \qquad \hat\beta_0 = \bar y - \hat\beta_1 \bar x.$$

The fitted line always passes through $(\bar x, \bar y)$.

## See Also
- [[Least Squares Estimation]]
- [[Slope Estimator in Deviation Form]]
- [[Sum of Deviations Equals Zero]]
- [[ANOVA Decomposition of SST]]
- [[Unbiasedness of the Slope Estimator]]
