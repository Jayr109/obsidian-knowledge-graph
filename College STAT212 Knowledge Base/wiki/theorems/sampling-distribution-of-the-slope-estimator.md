---
title: "Sampling Distribution of the Slope Estimator"
type: theorem
tags: [slope, sampling-distribution, t-distribution, inference]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

The three properties of the least-squares slope $\hat\beta_1$ that make inference (confidence intervals, hypothesis tests) about $\beta_1$ possible.

## Properties of $\hat\beta_1$

Recall $\hat\beta_1 = \dfrac{\sum_i (x_i - \bar x)(Y_i - \bar Y)}{\sum_i (x_i - \bar x)^2}$.

1. **Unbiased:** $E(\hat\beta_1) = \beta_1$. Proof: [[Unbiasedness of the Slope Estimator]].
2. **Variance:** $\mathrm{Var}(\hat\beta_1) = \dfrac{\sigma^2}{\sum_{i=1}^n (x_i - \bar x)^2}$.
3. **Normal:** $\hat\beta_1$ is normally distributed.

## Standardized statistic and the t-distribution

The estimated standard error is $\hat\sigma_{\hat\beta_1} = \dfrac{\hat\sigma}{\sqrt{\sum_i (x_i - \bar x)^2}}$ (using $\hat\sigma$ from [[Residuals and Model Diagnostics]]). Then

$$T = \frac{\hat\beta_1 - \beta_1}{\hat\sigma_{\hat\beta_1}} \sim t_{n-2}.$$

## Confidence interval for $\beta_1$

A $(1-\alpha)100\%$ CI for the slope:

$$\hat\beta_1 \pm t_{n-2;\,\alpha/2}\; \hat\sigma_{\hat\beta_1},$$

where $t_{n-2;\,\alpha/2}$ is the $(1-\alpha/2)$ quantile of $t_{n-2}$.

## Hypothesis test for $\beta_1$

To test $H_0: \beta_1 = \beta_{10}$ use $T = \dfrac{\hat\beta_1 - \beta_{10}}{\hat\sigma_{\hat\beta_1}}$ (like a one-sample `t`-test but with $n-2$ df).

- Two-sided $H_a: \beta_1 \ne \beta_{10}$: reject if $|T| > t_{n-2;\,\alpha/2}$.
- One-sided: reject if $T > t_{n-2;\,\alpha}$ (for $>$) or $T < -t_{n-2;\,\alpha}$ (for $<$).

Testing $H_0: \beta_1 = 0$ is of special interest — it asks whether `x` has any linear effect on `Y`. (Galton: $T = 19.01$, `P` $< 2\times10^{-16}$, strong positive relationship.)

## See Also
- [[Unbiasedness of the Slope Estimator]]
- [[Inference for the Mean Response and Prediction]]
- [[Correlation Coefficient]]
