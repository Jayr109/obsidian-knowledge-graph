---
title: "Prediction Error Variance"
type: derivation
tags: [prediction-interval, variance, inference]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Derives the variance of the prediction error when predicting a *new* response `Y` at $x = x_0$, which produces the extra "$1 +$" term that makes a prediction interval wider than a confidence interval for the mean (see [[Inference for the Mean Response and Prediction]]). This is exactly why the windmill homework's prediction interval was wider than its mean CI.

## Setup

Model for the new observation: $Y = \beta_0 + \beta_1 x_0 + \epsilon$. We guess $\hat\beta_0 + \hat\beta_1 x_0$. The total prediction error decomposes as:

$$\underbrace{[(\beta_0 + \beta_1 x_0) - (\hat\beta_0 + \hat\beta_1 x_0)]}_{\text{error from estimating }\beta_0,\beta_1} + \underbrace{\epsilon}_{\text{deviation of }Y\text{ from its mean}}.$$

## Variance of the prediction error

Assume the new $\epsilon$ is **independent** of the data used to compute $\hat\beta_0, \hat\beta_1$.

| Step | Justification |
|------|---------------|
| $\mathrm{Var}(\text{pred error}) = \mathrm{Var}(\hat\beta_0 + \hat\beta_1 x_0) + \mathrm{Var}(\epsilon)$ | Independence (variance of a sum of independent terms) |
| $= \sigma^2\left[\dfrac1n + \dfrac{(x_0-\bar x)^2}{\sum_i (x_i-\bar x)^2}\right] + \sigma^2$ | BD (variance of mean estimator; $\mathrm{Var}(\epsilon)=\sigma^2$) |
| $= \sigma^2\left[1 + \dfrac1n + \dfrac{(x_0-\bar x)^2}{\sum_i (x_i-\bar x)^2}\right]$ | MS (factor out $\sigma^2$) |

## Result

$$\mathrm{Var}(\text{prediction error}) = \sigma^2\left(1 + \frac1n + \frac{(x_0-\bar x)^2}{\sum_{i=1}^n (x_i-\bar x)^2}\right).$$

Replacing $\sigma$ with $\hat\sigma$ gives $SE_{\text{pred}}(x_0)$; the "$1 +$" is the source of the extra width versus the mean CI.

## See Also
- [[Inference for the Mean Response and Prediction]]
- [[Rules of Expectation and Variance]]
