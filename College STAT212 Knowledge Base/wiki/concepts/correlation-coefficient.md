---
title: "Correlation Coefficient"
type: concept
tags: [correlation, covariance, inference]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

The correlation coefficient measures how strongly two variables `X` and `Y` are linearly related, *without* designating one as response and the other as predictor. The population correlation is $\rho$; its sample estimate is `R` (Pearson's product-moment correlation).

## Population correlation

Given random variables `X`, `Y` with means $\mu_X, \mu_Y$:

$$\rho \equiv \mathrm{Corr}(X, Y) = \frac{\mathrm{Cov}(X, Y)}{\sigma_X \sigma_Y}, \quad \mathrm{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)],$$

with $\sigma_X^2 = \mathrm{Var}(X)$, $\sigma_Y^2 = \mathrm{Var}(Y)$. Always $-1 \le \rho \le 1$.

## Sample correlation

For i.i.d. pairs $(X_1, Y_1), \dots, (X_n, Y_n)$, substitute the moment estimates $\hat\sigma_X^2 = \frac1n\sum(X_i - \bar X)^2$, etc., to get:

$$\hat\rho = R = \frac{\sum_{i=1}^n (X_i - \bar X)(Y_i - \bar Y)}{\left[\sum (X_i - \bar X)^2 \sum (Y_i - \bar Y)^2\right]^{1/2}}.$$

## Key facts

- $R^2$ equals the [[Coefficient of Determination]] — hence the shared symbol.
- The slope estimator satisfies $\hat\beta_1 = R\, \hat\sigma_Y / \hat\sigma_X$ (see [[Least Squares Estimation]]).
- The closer `R` is to $\pm 1$, the stronger the linear relationship; $R \approx 0$ suggests $\rho \approx 0$.
- **Caution:** $\rho = 0$ does *not* imply `X` and `Y` are independent.

## Testing $H_0: \rho = 0$

$$T = \frac{R\sqrt{n-2}}{\sqrt{1 - R^2}}.$$

When $H_0$ is true and `n` is large, $T \approx N(0,1)$. In R, `cor.test(x, y)` returns `R`, a 95% CI for $\rho$, and a two-sided test of $H_0: \rho = 0$.

## See Also
- [[Slope as Correlation Times SD Ratio]]
- [[Coefficient of Determination]]
- [[Least Squares Estimation]]
- [[Sampling Distribution of the Slope Estimator]]
