---
title: "Inference for the Mean Response and Prediction"
type: theorem
tags: [confidence-interval, prediction-interval, inference]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

Two distinct interval problems at a chosen predictor value $x = x_0$: (1) a **confidence interval** for the *mean* response $E(Y) = \beta_0 + \beta_1 x_0$, and (2) a **prediction interval** for a *single new* response `Y`. Prediction is subject to more uncertainty, so its interval is always wider. These are the formulas used for Q15–Q18 of the windmill homework.

## Point estimate (both problems)

$$\widehat{E(Y)} = \hat\beta_0 + \hat\beta_1 x_0.$$

This is unbiased and normally distributed, with

$$\mathrm{Var}(\hat\beta_0 + \hat\beta_1 x_0) = \sigma^2\left[\frac1n + \frac{(x_0 - \bar x)^2}{\sum_{i=1}^n (x_i - \bar x)^2}\right].$$

## (1) Confidence interval for the mean $E(Y)$ at $x_0$

$$(\hat\beta_0 + \hat\beta_1 x_0) \pm t_{n-2;\,\alpha/2}\, SE(x_0), \qquad SE(x_0) = \hat\sigma\left[\frac1n + \frac{(x_0-\bar x)^2}{\sum_i (x_i-\bar x)^2}\right]^{1/2}.$$

## (2) Prediction interval for a new $Y$ at $x_0$

$$(\hat\beta_0 + \hat\beta_1 x_0) \pm t_{n-2;\,\alpha/2}\, SE_{\text{pred}}(x_0), \qquad SE_{\text{pred}}(x_0) = \hat\sigma\left[1 + \frac1n + \frac{(x_0-\bar x)^2}{\sum_i (x_i-\bar x)^2}\right]^{1/2}.$$

The extra **"$1 +$"** comes from the new observation's own noise $\epsilon$ — see [[Prediction Error Variance]].

## Key contrasts

- The prediction interval is **wider** than the mean CI at the same $x_0$ (extra $+1$ inside the root). Makes sense: predicting one random outcome is harder than estimating an average.
- Both intervals are **narrowest at $x_0 = \bar x$** and widen as $x_0$ moves away from $\bar x$ (the $(x_0 - \bar x)^2$ term).
- Interpretation (95%, $\alpha = 0.05$): we are 95% confident the future `Y` lies in the prediction interval.

## R commands
```r
predict(lm(y~x), newdata=data.frame(x=68), interval="confidence", level=0.95)
predict(lm(y~x), newdata=data.frame(x=72), interval="prediction", level=0.98)
```
Galton examples: 95% mean CI at $x_0=68$ is $(68.70, 68.99)$; 98% prediction interval at $x_0=72$ is $(65.22, 76.59)$.

## See Also
- [[Prediction Error Variance]]
- [[Sampling Distribution of the Slope Estimator]]
- [[Confidence and Prediction Intervals in R]]
