---
title: "Inference for Polynomial Regression"
type: theorem
tags: [polynomial-regression, confidence-interval, prediction-interval, hypothesis-test, matrix]
sources: [lecture-02-more-general-regression]
course: STAT 212
updated: 2026-07-04
---

Inference for the coefficients, mean response, and a new response in the [[Polynomial Regression]] model, using the matrix quantities from [[Polynomial Normal Equations in Matrix Form]]. All formulas parallel the simple-linear case with $n-k-1$ degrees of freedom.

## Standard error of a coefficient

$$SE(\hat\beta_i) = \sigma\sqrt{c_{i+1}}, \qquad c_j = j\text{th diagonal element of } (X^TX)^{-1}.$$

Under the normal-error assumptions, $\dfrac{\hat\beta_i - \beta_i}{\hat\sigma\sqrt{c_{i+1}}} \sim t_{n-k-1}$.

## Confidence interval / test for $\beta_i$

$$\hat\beta_i \pm t_{n-k-1;\,\alpha/2}\, \hat\sigma\sqrt{c_{i+1}}.$$

Useful degree test: in a cubic model $H_0: \beta_3 = 0$ (quadratic suffices) vs. $H_a: \beta_3 \ne 0$ (genuinely cubic).

## Point estimate at $x_0$

$$\hat\mu(x_0) = \hat\beta_0 + \hat\beta_1 x_0 + \cdots + \hat\beta_k x_0^k, \qquad x^T = (1\ x_0\ x_0^2\ \cdots\ x_0^k).$$

## CI for the mean response at $x_0$

$$\hat\mu(x_0) \pm t_{n-k-1;\,\alpha/2}\, \hat\sigma\sqrt{x^T (X^TX)^{-1} x}.$$

## Prediction interval for a new $Y$ at $x_0$

$$\hat\mu(x_0) \pm t_{n-k-1;\,\alpha/2}\, \hat\sigma\sqrt{1 + x^T (X^TX)^{-1} x}.$$

Again the extra **"$1 +$"** widens the prediction interval versus the mean CI (same logic as [[Prediction Error Variance]]).

## In R
All simple-linear commands apply after `fit = lm(y ~ poly(x, 3, raw=T))`: `summary`, `confint`, `predict(..., interval="confidence")`, `predict(..., interval="prediction")`.

## See Also
- [[Polynomial Normal Equations in Matrix Form]]
- [[Inference for the Mean Response and Prediction]]
- [[Multiple Linear Regression]]
