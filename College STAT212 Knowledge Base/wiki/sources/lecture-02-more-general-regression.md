---
title: "Source: More General Regression Analyses (Notes 2)"
type: source
tags: [polynomial-regression, transformations, model-selection, matrix-form]
sources: [lecture-02-more-general-regression]
course: STAT 212
updated: 2026-07-04
---

Summary of the second set of course notes, *More General Regression Analyses* (slides 46–79). Handles the one-predictor case when a straight line is inadequate: polynomial regression, the matrix form of least squares, estimating $\sigma^2$ with $n-k-1$ df, model-selection criteria (adjusted $R^2$, AIC, BIC), inference for polynomial coefficients, non-polynomial (nonlinear) models, and **variable transformations** — the log and reciprocal transforms that linearize curved data (as in the windmill homework).

## Contents by slide

- **Slides 46–49 — Motivation.** Example 5: curved pattern in residuals reveals nonlinearity. General model $Y = f(x) + \epsilon$; limit candidate models (Occam's razor / parsimony). Polynomials as a flexible-but-parsimonious class (Taylor's theorem).
- **Slides 50–53 — Polynomial regression.** [[Polynomial Regression]]: the degree-$k$ model, least squares, normal equations, $\hat\sigma^2 = SSE/(n-k-1)$, and $SST = SSR + SSE$, $R^2$ as before.
- **Slides 51–52 — Matrix form.** [[Polynomial Normal Equations in Matrix Form]]: $X^TXb = X^Ty$, solution $\hat\beta = (X^TX)^{-1}X^Ty$.
- **Slides 54, 72 — R.** `lm(y~poly(x,3,raw=T))`; all prior `summary`/`confint`/`predict` commands still apply.
- **Slides 55–62 — Example 6.** Fitting degrees 1–16 to cubic data; over-fitting at high degree; bootstrap.
- **Slides 63–68 — Model selection.** [[Model Selection Criteria]]: why raw $R^2$ always increases; adjusted $R^2$, AIC, BIC.
- **Slides 69–71 — Inference.** [[Inference for Polynomial Regression]]: CI/test for each $\beta_i$, matrix CI for the mean, matrix prediction interval.
- **Slides 73–79 — Transformations.** [[Variable Transformations]]: nonlinear models via least squares; log/reciprocal transforms; Example 7 (Beveridge wheat prices) — logging stabilizes variance.

## Key facts referenced
- $\hat\sigma^2 = MSE = SSE/(n-k-1)$ for a degree-$k$ polynomial.
- $R^2_1 < R^2_2 < \cdots$ always increases with degree ⇒ use adjusted $R^2$/AIC/BIC.
- $AIC_k = n\log(SSE_k) + 2k$; $BIC_k = n\log(SSE_k) + k\log(n)$ (BIC penalizes more).
- Increasing variance with `x` is a tipoff to take logs.

## See Also
- [[Polynomial Regression]]
- [[Variable Transformations]]
- [[Model Selection Criteria]]
- [[STAT 212 Overview]]
