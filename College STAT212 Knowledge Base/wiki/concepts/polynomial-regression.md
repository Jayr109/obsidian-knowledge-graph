---
title: "Polynomial Regression"
type: concept
tags: [polynomial-regression, least-squares, model]
sources: [lecture-02-more-general-regression]
course: STAT 212
updated: 2026-07-04
---

Polynomial regression extends the [[Simple Linear Regression Model]] to curved relationships while staying *linear in the parameters*, so ordinary least squares still applies. It provides a flexible class of models with a controlled number of parameters (justified by Occam's razor / parsimony and Taylor's theorem: a smooth function is approximated arbitrarily well by a high-enough-degree polynomial).

## The model

$$Y = \beta_0 + \beta_1 x + \beta_2 x^2 + \cdots + \beta_k x^k + \epsilon, \qquad \epsilon \sim N(0, \sigma^2).$$

Given data, minimize $f(b_0,\dots,b_k) = \sum_{i=1}^n \big(y_i - \sum_{j=0}^k b_j x_i^j\big)^2$. Setting $\partial f/\partial b_j = 0$ for $j = 0,\dots,k$ gives the **normal equations** — a *linear* system, which is why polynomial regression is easy to solve. See [[Polynomial Normal Equations in Matrix Form]].

## Estimating $\sigma^2$

With predicted values $\hat y_i = \hat\beta_0 + \hat\beta_1 x_i + \cdots + \hat\beta_k x_i^k$ and residuals $e_i = y_i - \hat y_i$:

$$\hat\sigma^2 = MSE = \frac{SSE}{n - k - 1}.$$

We subtract $k+1$ (one per estimated coefficient) — generalizing the $n-2$ of the straight-line case.

## Sums of squares and $R^2$

The decomposition $SST = SSR + SSE$ and $R^2 = SSR/SST = 1 - SSE/SST$ carry over unchanged (see [[Coefficient of Determination]]); $R^2$ is the fraction of variation explained by the polynomial model. But raw $R^2$ always rises with degree — use [[Model Selection Criteria]] to pick the degree.

## In R
```r
fit = lm(y ~ poly(x, 3, raw = T))   # equivalently lm(y ~ x + I(x^2) + I(x^3))
summary(fit)                         # or lm(y ~ poly(x, 3)) for orthogonal polynomials
```
Both raw and orthogonal forms give identical fitted values and residuals. All prior `summary`/`confint`/`predict` commands apply.

## See Also
- [[Polynomial Normal Equations in Matrix Form]]
- [[Model Selection Criteria]]
- [[Inference for Polynomial Regression]]
- [[Multiple Linear Regression]]
