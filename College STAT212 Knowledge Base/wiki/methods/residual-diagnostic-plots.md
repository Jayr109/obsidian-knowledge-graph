---
title: "Residual Diagnostic Plots"
type: method
tags: [diagnostics, residuals, R, procedure]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Procedure for checking the [[Simple Linear Regression Model]] assumptions using [[Residuals and Model Diagnostics|residuals]]. This is the exact recipe behind the windmill homework's residual-vs-x, residual-vs-fitted, QQ, and density-plot questions.

## Compute residuals and fitted values in R
```r
fit    = lm(y ~ x)
resid  = fit$residuals
predict = fit$fitted.values
```

## The four plots and how to read them

| Command | Plot | Checks | "Good" pattern | "Bad" pattern |
|---------|------|--------|----------------|---------------|
| `plot(x, resid)` | residual vs. `x` | linearity | random cloud around 0 | curvature/trend ⇒ need a transform |
| `plot(predict, resid)` | residual vs. $\hat y$ | equal variance | constant-width band | fanning ⇒ variance grows with $\hat y$ |
| `hist(resid)` / `plot(density(resid))` | histogram / KDE | normality | single symmetric bell | skew / bimodal ⇒ non-normal |
| `qqnorm(resid)` | normal QQ plot | normality | points on the $y=x$ line (straight, increasing) | strong curvature ⇒ heavy tails/skew |

## Interpretation notes

- A **QQ plot** is always monotonically increasing (it plots *sorted* residuals vs. normal quantiles); the diagnostic is whether it's *straight*.
- A **density plot** of residuals peaks high when residuals are tightly spread — peak height $\approx 1/(\hat\sigma\sqrt{2\pi})$, not a fixed number.
- Residual vs. `x` and residual vs. $\hat y$ look nearly identical when the fitted values are a monotonic function of `x`.
- If diagnostics fail, try transforming `x` or `y` (e.g. the reciprocal $1/x$ that linearized the windmill data — see [[Variable Transformations]]).

## See Also
- [[Residuals and Model Diagnostics]]
- [[Simple Linear Regression Model]]
- [[Confidence and Prediction Intervals in R]]
