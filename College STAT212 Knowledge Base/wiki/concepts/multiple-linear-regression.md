---
title: "Multiple Linear Regression"
type: concept
tags: [multiple-regression, model, interaction, matrix]
sources: [lecture-03-multiple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Multiple linear regression models one response `Y` from **several** predictors $x_1,\dots,x_k$. All the machinery of [[Polynomial Regression]] carries over verbatim — only the columns of the design matrix change.

## The model

$$Y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_k x_k + \epsilon, \qquad \epsilon \sim N(0, \sigma^2),$$

with $E(Y) = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k$ and $\mathrm{Var}(Y) = \sigma^2$ (both conditional on the predictors). Each $\beta_i$ is the change in average `Y` per unit increase in $x_i$ **holding the others fixed**.

## Flexibility: derived predictors

A predictor can be a function of others, so `k` (terms) may exceed `p` (distinct variables):
- **Interaction:** $Y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1 x_2 + \epsilon$ (here $x_3 = x_1 x_2$).
- **Quadratic (curved surface):** $Y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1^2 + \beta_4 x_2^2 + \epsilon$.

A plane $\beta_0 + \beta_1 x_1 + \beta_2 x_2$ has no curvature; add interaction/quadratic terms if the surface of averages curves.

## Estimation

Least squares gives $\hat\beta = (X^TX)^{-1}X^Ty$ (design-matrix columns are $1, x_1, \dots, x_k$); see [[Polynomial Normal Equations in Matrix Form]]. Then $\hat\sigma^2 = SSE/(n-k-1) = MSE$, and $R^2 = SSR/SST$ as usual ([[Coefficient of Determination]]).

- R: `summary(lm(y ~ x1 + x2 + x3))`.
- Multiplicative models (e.g. mesquite $Z = \beta_0^* u_1^{\beta_1}\cdots u_4^{\beta_4}\epsilon'$) become linear by taking logs of response and predictors — see [[Variable Transformations]].

## Inference

- Each coefficient: $\hat\beta_i \pm t_{n-k-1;\alpha/2}\,\hat\sigma\sqrt{c_{i+1}}$ (same as [[Inference for Polynomial Regression]]).
- Whole model: [[F-Test for Model Utility]]. Subset of predictors: [[Reduction Method (Partial F-Test)]].
- Diagnostics: standardized residuals $e_i^* = (y_i - \hat y_i)/\hat\sigma$ and [[Influential Observations and Cook's D]].

## See Also
- [[F-Test for Model Utility]]
- [[Reduction Method (Partial F-Test)]]
- [[Influential Observations and Cook's D]]
- [[Model Selection Criteria]]
