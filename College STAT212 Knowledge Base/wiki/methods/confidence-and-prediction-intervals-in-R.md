---
title: "Confidence and Prediction Intervals in R"
type: method
tags: [R, confidence-interval, prediction-interval, procedure]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

R recipes for the inference tasks in [[Sampling Distribution of the Slope Estimator]] and [[Inference for the Mean Response and Prediction]].

## Fit and read coefficients
```r
fit = lm(y ~ x)
summary(fit)   # estimates, std errors, t values, p-values, R^2, residual SE
```
The `summary` table gives $\hat\beta_0, \hat\beta_1$, their standard errors, `t` values ($=$ estimate/SE), and two-sided `p`-values. `Multiple R-squared` is the [[Coefficient of Determination]].

## Confidence interval for the slope $\beta_1$
```r
confint(fit, level = 0.95)
```
Equivalent by hand: $\hat\beta_1 \pm t_{n-2;\,\alpha/2}\,\hat\sigma_{\hat\beta_1}$.

## CI for the mean response at $x_0$
```r
predict(fit, newdata = data.frame(x = 68),
        interval = "confidence", level = 0.95)
```

## Prediction interval for a new $Y$ at $x_0$
```r
predict(fit, newdata = data.frame(x = 72),
        interval = "prediction", level = 0.98)
```

## Correlation test
```r
cor.test(x, y)   # R, 95% CI for rho, two-sided test of H0: rho = 0
```

## By-hand checklist (matches the windmill homework)
1. Fit; read $\hat\beta_0, \hat\beta_1, \hat\sigma$ (residual SE), and $\sum(x_i-\bar x)^2$.
2. Slope CI: $\hat\beta_1 \pm t_{n-2;\alpha/2}\cdot \hat\sigma/\sqrt{\sum(x_i-\bar x)^2}$.
3. Mean CI at $x_0$: use $SE(x_0)=\hat\sigma\sqrt{1/n + (x_0-\bar x)^2/\sum(x_i-\bar x)^2}$.
4. Prediction interval at $x_0$: use $SE_{\text{pred}}=\hat\sigma\sqrt{1 + 1/n + (x_0-\bar x)^2/\sum(x_i-\bar x)^2}$.

## See Also
- [[Inference for the Mean Response and Prediction]]
- [[Sampling Distribution of the Slope Estimator]]
- [[Residual Diagnostic Plots]]
