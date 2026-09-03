---
title: "Rules of Expectation and Variance"
type: theorem
tags: [expectation, variance, covariance, reference]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Reference sheet of the $E[\cdot]$ and $\mathrm{Var}[\cdot]$ identities used throughout the derivations, mapped to the course's handwriting justification tags (**Rule of Expectations**, **Rule of Variance**, **X is constant**, **Independence**). Cite this page from any derivation that manipulates expectations or variances.

## Expectation rules (tag: Rule of Expectations)

- **Linearity:** $E[aX + bY] = aE[X] + bE[Y]$ for constants $a, b$ (always, no independence needed).
- **Constant:** $E[c] = c$; and $E[cX] = cE[X]$ — pull constants out (tag: **X is constant**).
- **Sum over index:** $E\left[\sum_i X_i\right] = \sum_i E[X_i]$ (tag: **Move sum** + Rule of Expectations).
- **Model error:** in the [[Simple Linear Regression Model]], $E[\epsilon_i] = 0$, so $E[Y_i] = \beta_0 + \beta_1 x_i$.

## Variance rules (tag: Rule of Variance)

- **Constant scaling:** $\mathrm{Var}[aX + b] = a^2\,\mathrm{Var}[X]$ (additive constants drop; tag: **X is constant**).
- **Sum of independent terms:** $\mathrm{Var}\left[\sum_i X_i\right] = \sum_i \mathrm{Var}[X_i]$ **only if independent** (tag: **Independence**).
- **General sum:** $\mathrm{Var}[X + Y] = \mathrm{Var}[X] + \mathrm{Var}[Y] + 2\,\mathrm{Cov}[X, Y]$.
- **Definition:** $\mathrm{Var}[X] = E\big[(X - E[X])^2\big] = E[X^2] - (E[X])^2$.

## Covariance (tag: BD / Rule of Variance)

- $\mathrm{Cov}[X, Y] = E[(X - \mu_X)(Y - \mu_Y)]$.
- If `X`, `Y` independent then $\mathrm{Cov}[X, Y] = 0$ (converse is **not** true — see [[Correlation Coefficient]]).

## Handy summation identities (tag: MS / Zeros out)

- $\sum_i (x_i - \bar x) = 0$ (tag: **Zeros out**; proof: [[Sum of Deviations Equals Zero]]).
- $\sum_i (x_i - \bar x)^2 = \sum_i x_i(x_i - \bar x) = \sum_i x_i^2 - n\bar x^2$.
- $\sum_i (x_i - \bar x)(y_i - \bar y) = \sum_i x_i y_i - n\bar x\bar y$.

## See Also
- [[Unbiasedness of the Slope Estimator]]
- [[Prediction Error Variance]]
- [[ANOVA Decomposition of SST]]
- [[Simple Linear Regression Model]]
