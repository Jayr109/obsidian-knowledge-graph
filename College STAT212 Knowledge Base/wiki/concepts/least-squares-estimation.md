---
title: "Least Squares Estimation"
type: concept
tags: [regression, least-squares, estimation]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Least squares is the method for estimating the intercept $\beta_0$ and slope $\beta_1$ of the [[Simple Linear Regression Model]]. Given data $(x_1, y_1), \dots, (x_n, y_n)$, we choose the values $b_0, b_1$ that minimize the sum of squared vertical deviations of the data from the line:

$$f(b_0, b_1) = \sum_{i=1}^n \left[ y_i - (b_0 + b_1 x_i) \right]^2.$$

Carl Friedrich Gauss (1777–1855) is credited with discovering least squares. The method minimizes `f` by taking partial derivatives with respect to $b_0$ and $b_1$, setting them to 0, and solving (the **normal equations**). Full steps: [[Least Squares Estimators Derivation]].

## The least squares estimators

$$\hat\beta_1 = \frac{\sum_{i=1}^n (x_i - \bar x)(y_i - \bar y)}{\sum_{i=1}^n (x_i - \bar x)^2}, \qquad \hat\beta_0 = \bar y - \hat\beta_1 \bar x.$$

These are the **least squares estimates** of $\beta_0$ and $\beta_1$. The fitted (least squares) line is $\hat y = \hat\beta_0 + \hat\beta_1 x$.

Note the slope passes through $(\bar x, \bar y)$ (from $\hat\beta_0 = \bar y - \hat\beta_1 \bar x$), and can be written using correlation as $\hat\beta_1 = R\,\hat\sigma_Y / \hat\sigma_X$ (see [[Correlation Coefficient]]).

## Predicted values and residuals

- **Predicted (fitted) values:** $\hat y_i = \hat\beta_0 + \hat\beta_1 x_i$.
- **Residuals:** $e_i = y_i - \hat y_i$ — proxies for the unobservable errors $\epsilon_i$. See [[Residuals and Model Diagnostics]].

## Example (Galton father–son data)

`summary(lm(y~x))` in R gives $\hat\beta_0 = 33.887$, $\hat\beta_1 = 0.514$, so $\hat y = 33.887 + 0.514x$: each extra inch of father's height corresponds to +0.514 in. average son's height.

## See Also
- [[Least Squares Estimators Derivation]]
- [[Simple Linear Regression Model]]
- [[Residuals and Model Diagnostics]]
- [[Correlation Coefficient]]
