---
title: "Influential Observations and Cook's D"
type: concept
tags: [diagnostics, outliers, cooks-distance, leverage]
sources: [lecture-03-multiple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

A single observation can strongly influence the estimated coefficients or error variance in [[Multiple Linear Regression]]. Cook's distance quantifies that influence per observation. Spotting outliers is harder here than in simple regression because with >2 predictors you cannot simply plot `y` against the predictor vector.

## Standardized residuals

$$e_i^* = \frac{y_i - \hat y_i}{\hat\sigma}.$$

If the model is correct these behave like a random sample from the **standard** normal. Diagnostic plots:

| Plot | Purpose |
|------|---------|
| $e_i^*$ vs. `i` | check independence of errors |
| $e_i^*$ vs. $\hat y_i$ | check constant variance |
| $e_i^*$ vs. a predictor | check for a nonlinear relationship |
| normal probability plot / KDE | check normality |

## Two kinds of outliers

1. $x_i$ in the **middle** of the predictor range but $y_i$ unusually large/small — little effect on the $\hat\beta_i$, but can **inflate $\hat\sigma^2$**.
2. $x_i$ **far** from the other predictor vectors (high leverage) — can have a **big effect on the $\hat\beta_i$**.

## Cook's D

Cook's $D_i$ measures the distance between $\hat\beta$ and the estimate computed with observation `i` deleted — one value per case. Large $D_i$ ⇒ influential.

- $D < 1$: usually not an outlier.
- $D > 1.5$: possible outlier — refit without that case and see how much the $\hat\beta_i$ move.

In R:
```r
output = cooks.distance(fit)
plot(output, ylab = "Cook's D")
```

## See Also
- [[Residual Diagnostic Plots]]
- [[Multiple Linear Regression]]
