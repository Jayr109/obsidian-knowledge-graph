---
title: "Coefficient of Determination"
type: concept
tags: [regression, R-squared, ANOVA, goodness-of-fit]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

The coefficient of determination, $R^2$, measures the fraction of the total variation in the response `y` that is explained by the straight-line relationship with `x`. It is built from the three sums of squares of the [[ANOVA Decomposition of SST]].

## The three sums of squares

- **Total sum of squares:** $SST = \sum_{i=1}^n (y_i - \bar y)^2$ — all variation in the $y_i$, from any source.
- **Error sum of squares:** $SSE = \sum_{i=1}^n e_i^2 = \sum (y_i - \hat y_i)^2$ — *unsystematic* variation, pure noise unrelated to `x`.
- **Regression sum of squares:** $SSR = \sum_{i=1}^n (\hat y_i - \bar y)^2$ — *systematic* variation explained by the linear model.

The key identity (proved in [[ANOVA Decomposition of SST]]) is:

$$SST = SSE + SSR.$$

## Definition

$$R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}, \qquad 0 \le R^2 \le 1.$$

$R^2$ is the fraction of total variation in `y` explained by the linear relationship with `x`. Higher $R^2$ ⇒ tighter clustering about the line.

- Example (windmill homework): $R^2 = 0.9800$ — the reciprocal model explains ~98% of the variation.
- Example (Galton father–son): $R^2 = 0.251$ — only ~25% of variation in sons' heights is explained.

## Relationship to correlation

$R^2$ equals the square of the sample [[Correlation Coefficient]]: $R^2 = r^2 = \hat\rho^{\,2}$.

## See Also
- [[ANOVA Decomposition of SST]]
- [[Correlation Coefficient]]
- [[Residuals and Model Diagnostics]]
