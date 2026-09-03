---
title: "Sum of Deviations Equals Zero"
type: derivation
tags: [identity, deviations, summation, zeros-out]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-05
---

Proves the identity $\sum_{i=1}^n (x_i - \bar x) = 0$ (and identically $\sum_i (y_i - \bar y) = 0$). This is the workhorse "Zeros out" fact that recurs in [[Unbiasedness of the Slope Estimator]], [[ANOVA Decomposition of SST]], and [[Slope Estimator in Deviation Form]]. **Proved as Problem 1 of the theory assignment.**

## Step-by-step

Recall $\bar x = \tfrac1n\sum_{i=1}^n x_i$.

| Step | Justification |
|------|---------------|
| $\sum_i (x_i - \bar x) = \sum_i x_i - \sum_i \bar x$ | Move sum (put $\Sigma$ on each term) |
| $= \sum_i x_i - n\bar x$ | X is constant ($\bar x$ doesn't depend on $i$, so $\sum_i \bar x = n\bar x$) |
| $= \sum_i x_i - n\left(\tfrac1n\sum_i x_i\right)$ | BD (definition of $\bar x$) |
| $= \sum_i x_i - \sum_i x_i$ | MS ($n\cdot\tfrac1n = 1$) |
| $= 0$ | Zeros out |

## Result

$$\sum_{i=1}^n (x_i - \bar x) = 0, \qquad \sum_{i=1}^n (y_i - \bar y) = 0. \qquad \blacksquare$$

The same argument with $y$ in place of $x$ gives the companion identity.

## See Also
- [[Slope Estimator in Deviation Form]]
- [[Unbiasedness of the Slope Estimator]]
- [[Rules of Expectation and Variance]]
