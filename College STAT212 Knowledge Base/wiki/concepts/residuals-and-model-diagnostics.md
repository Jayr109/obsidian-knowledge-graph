---
title: "Residuals and Model Diagnostics"
type: concept
tags: [regression, residuals, diagnostics, variance, normality]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Residuals are the observed minus fitted values, $e_i = y_i - \hat y_i$, and serve as proxies for the unobservable errors $\epsilon_i$ of the [[Simple Linear Regression Model]]. They are the main tool for checking whether the model assumptions hold: if the model is correct, $e_1, \dots, e_n$ should behave like a random sample from a normal distribution. This concept underlies the residual/QQ/density-plot questions on the windmill homework.

## Estimating the error variance $\sigma^2$

Since $\sigma^2 = \mathrm{Var}(\epsilon_i) = E\{[Y_i - (\beta_0 + \beta_1 x_i)]^2\}$, we estimate it from the residuals. Define the **error sum of squares** $SSE = \sum_{i=1}^n e_i^2$. The estimator is

$$\hat\sigma^2 = \frac{SSE}{n-2}.$$

We divide by $n-2$ (not $n$) to make $\hat\sigma^2$ **unbiased** — we lose 2 degrees of freedom for the two estimated parameters $\beta_0, \beta_1$ (compare the sample variance dividing by $n-1$ for one estimated mean). Here $\hat\sigma = \sqrt{\hat\sigma^2}$ is the residual standard error.

## Diagnostic plots

| Plot | What it checks | What "good" looks like |
|------|----------------|------------------------|
| $e_i$ vs. $x_i$ | Is the true curve more complex than a line? | Random cloud, no pattern/curvature |
| $e_i$ vs. $\hat y_i$ | Equal-variance (homoskedasticity) assumption | Random cloud, constant spread (no fanning) |
| Histogram / KDE / normal QQ plot of $e_i$ | Normality assumption | Bell-shaped density; QQ points on the $y = x$ line |

- A **pattern** (e.g. a curve) in $e_i$ vs. $x_i$ ⇒ the straight line is inadequate; a transformation may be needed.
- **Fanning** (spread increasing with $\hat y_i$) in $e_i$ vs. $\hat y_i$ ⇒ non-constant variance.
- A **QQ plot** should closely resemble the $y = x$ line if residuals are normal.

Procedure recipe: [[Residual Diagnostic Plots]].

## See Also
- [[Residual Diagnostic Plots]]
- [[Coefficient of Determination]]
- [[Simple Linear Regression Model]]
