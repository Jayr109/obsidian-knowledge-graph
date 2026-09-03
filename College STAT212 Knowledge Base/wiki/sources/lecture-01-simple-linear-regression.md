---
title: "Source: Simple Linear Regression and Correlation (Notes 1)"
type: source
tags: [regression, correlation, least-squares, diagnostics, inference]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Summary of the first set of course notes, *Simple Linear Regression and Correlation* (44 slides). This source introduces the simple linear regression (SLR) model, least-squares estimation, estimation of the error variance, residual diagnostics, the coefficient of determination, inference for the slope, confidence/prediction intervals, and the correlation coefficient. It is the foundation for the windmill / bacteria homework worked earlier in the course.

## Contents by slide

- **Slides 1–7 — Motivation.** Regression studies relationships between `x` and `y`. Example 1 (Galileo gravity, deterministic, noise = measurement error only). Example 2 ([[Sir Francis Galton]] father–son heights, noise is intrinsic, "regression toward the mean").
- **Slides 8–11 — The model.** The [[Simple Linear Regression Model]], its four assumptions, and interpretation of `E(Y_i)`, `Var(Y_i)`, and the slope.
- **Slides 11–15 — Least squares.** [[Least Squares Estimation]]; the [[Least Squares Estimators Derivation]] via partial derivatives; Gauss; Galton R fit.
- **Slides 16–18 — Error variance.** Predicted values, [[Residuals and Model Diagnostics|residuals]], `SSE`, and the unbiased estimator `σ̂² = SSE/(n−2)`.
- **Slides 18–21 — Diagnostics.** [[Residual Diagnostic Plots]] for checking linearity, equal variance, and normality.
- **Slides 22–27 — R².** [[ANOVA Decomposition of SST|SST = SSE + SSR]] and the [[Coefficient of Determination]].
- **Slides 28–31 — Inference for slope.** [[Sampling Distribution of the Slope Estimator]], the [[Unbiasedness of the Slope Estimator|unbiasedness proof]], `t` confidence intervals and tests.
- **Slides 32–39 — Mean & prediction.** [[Inference for the Mean Response and Prediction]] — CI for `E(Y)` at `x₀` and prediction interval for a new `Y`.
- **Slides 40–44 — Correlation.** The [[Correlation Coefficient]] `ρ`, its estimator `R`, the identity `R² = r²`, and testing `ρ = 0`.

## Key numbers referenced
- Galton least-squares line: `ŷ = 33.887 + 0.514x`; `R² = 0.251`; `σ̂_β̂₁ = 0.027`.
- 95% CI for slope: `(0.461, 0.567)`; `T = 19.01` for `H₀: β₁ = 0`.

## See Also
- [[Simple Linear Regression Model]]
- [[Least Squares Estimation]]
- [[Coefficient of Determination]]
- [[STAT 212 Overview]]
