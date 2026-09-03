---
title: "Slope as Correlation Times SD Ratio"
type: derivation
tags: [least-squares, slope, correlation, standard-deviation]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-05
---

Shows the least-squares slope equals the sample correlation times the ratio of sample standard deviations: $\hat\beta_1 = \hat\rho\,\dfrac{\hat\sigma_Y}{\hat\sigma_X}$. Uses the deviation form of $\hat\beta_1$ from [[Slope Estimator in Deviation Form]]. **Proved as Problem 4 of the theory assignment.** This is the identity noted on the [[Correlation Coefficient]] page.

## Definitions

$$\hat\sigma_X = \sqrt{\tfrac1n\sum_i (x_i-\bar x)^2},\quad \hat\sigma_Y = \sqrt{\tfrac1n\sum_i (y_i-\bar y)^2},$$
$$\hat\rho = \frac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum_i (y_i-\bar y)^2}\,\sqrt{\sum_i (x_i-\bar x)^2}}.$$

## Step 1 — simplify the SD ratio $\hat\sigma_Y/\hat\sigma_X$

| Step | Justification |
|------|---------------|
| $\dfrac{\hat\sigma_Y}{\hat\sigma_X} = \dfrac{\sqrt{\tfrac1n\sum_i (y_i-\bar y)^2}}{\sqrt{\tfrac1n\sum_i (x_i-\bar x)^2}}$ | BD (definitions of $\hat\sigma_Y,\hat\sigma_X$) |
| $= \sqrt{\dfrac{\tfrac1n\sum_i (y_i-\bar y)^2}{\tfrac1n\sum_i (x_i-\bar x)^2}} = \sqrt{\dfrac{\sum_i (y_i-\bar y)^2}{\sum_i (x_i-\bar x)^2}}$ | MS ($\sqrt a/\sqrt b=\sqrt{a/b}$; the $\tfrac1n$ cancels) |
| $= \dfrac{\sqrt{\sum_i (y_i-\bar y)^2}}{\sqrt{\sum_i (x_i-\bar x)^2}}$ | MS ($\sqrt{a/b}=\sqrt a/\sqrt b$) |

## Step 2 — form $\hat\rho\cdot(\hat\sigma_Y/\hat\sigma_X)$

| Step | Justification |
|------|---------------|
| $\hat\rho\,\dfrac{\hat\sigma_Y}{\hat\sigma_X} = \dfrac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum_i (y_i-\bar y)^2}\,\sqrt{\sum_i (x_i-\bar x)^2}}\cdot\dfrac{\sqrt{\sum_i (y_i-\bar y)^2}}{\sqrt{\sum_i (x_i-\bar x)^2}}$ | BD (insert $\hat\rho$ and Step 1) |
| $= \dfrac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum_i (x_i-\bar x)^2}\,\sqrt{\sum_i (x_i-\bar x)^2}}$ | MS ($\sqrt{\sum(y_i-\bar y)^2}$ cancels) |
| $= \dfrac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sum_i (x_i-\bar x)^2}$ | MS ($\sqrt a\cdot\sqrt a = a$) |
| $= \hat\beta_1$ | BD ([[Slope Estimator in Deviation Form]]) |

## Result

$$\hat\beta_1 = \hat\rho\,\frac{\hat\sigma_Y}{\hat\sigma_X}. \qquad \blacksquare$$

## See Also
- [[Slope Estimator in Deviation Form]]
- [[Correlation Coefficient]]
- [[Least Squares Estimation]]
