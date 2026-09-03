---
title: "Source: Multiple Regression (Notes 3)"
type: source
tags: [multiple-regression, F-test, reduction-method, model-selection, diagnostics]
sources: [lecture-03-multiple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Summary of the third set of course notes, *Multiple Regression* (slides 81–112). Extends regression to several predictors: the model and its interaction/quadratic terms, matrix least squares (identical machinery to polynomial regression), estimation of $\sigma^2$ with $n-k-1$ df, $R^2$, inference for individual coefficients, the **F-test for model utility**, the **reduction method** (partial F-test) for testing a subset of predictors, model selection (R²/AIC/BIC and all-subsets `leaps`), residual diagnostics with standardized residuals, and influential observations via **Cook's D**.

## Contents by slide

- **Slides 81–84 — The model.** [[Multiple Linear Regression]]: $Y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + \epsilon$; interaction ($x_1 x_2$) and quadratic ($x_1^2$) terms; plane vs. curved surface.
- **Slides 85–87 — Least squares.** Same normal equations / matrix solution $\hat\beta = (X^TX)^{-1}X^Ty$ as [[Polynomial Normal Equations in Matrix Form]]. R: `lm(y ~ x1 + x2 + x3)`.
- **Slides 88–92 — Example 8.** Mesquite tree data (predict leaf weight); multiplicative model → linear via logs; scatterplot matrix.
- **Slides 93–95 — Estimation & inference.** $\hat\sigma^2 = SSE/(n-k-1)$; $R^2$; coefficient CIs/tests and matrix CI/PI (same as [[Inference for Polynomial Regression]]).
- **Slides 95–96 — F-test.** [[F-Test for Model Utility]]: $H_0: \beta_1 = \cdots = \beta_k = 0$.
- **Slides 97–104 — Reduction method.** [[Reduction Method (Partial F-Test)]]: test a subset of coefficients = 0 via full vs. reduced SSE.
- **Slides 105–107 — Model selection.** $R^2$ for equal-size models; AIC/BIC otherwise; all-subsets via `leaps` ($2^k$ models).
- **Slides 108–112 — Diagnostics.** Standardized residuals; [[Influential Observations and Cook's D]].

## Key facts referenced
- F-statistic (utility): $F = \dfrac{SSR/k}{MSE} = \dfrac{R^2/k}{(1-R^2)/(n-k-1)} \sim F_{k,\,n-k-1}$.
- Reduction F: $F = \dfrac{(SSE_r - SSE_f)/\ell}{SSE_f/(n-k-1)} \sim F_{\ell,\,n-k-1}$.
- Mesquite: full model $R^2 = 0.884$, utility $F = 28.6$ ($P = 7.3\times10^{-7}$).
- Cook's D > 1.5 flags a possible influential outlier.

## See Also
- [[Multiple Linear Regression]]
- [[F-Test for Model Utility]]
- [[Reduction Method (Partial F-Test)]]
- [[STAT 212 Overview]]
