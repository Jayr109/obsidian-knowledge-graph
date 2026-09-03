---
title: "F-Test for Model Utility"
type: theorem
tags: [F-test, multiple-regression, hypothesis-test]
sources: [lecture-03-multiple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

The overall F-test (the textbook's "model utility" test) asks whether a [[Multiple Linear Regression]] model has *any* predictive value — i.e. whether at least one predictor has a nonzero coefficient.

## Hypotheses

$$H_0: \beta_1 = \beta_2 = \cdots = \beta_k = 0 \quad\text{vs.}\quad H_a: \text{at least one } \beta_j \ne 0.$$

Under $H_0$ (and if the model is correct), `Y` is unrelated to $x_1,\dots,x_k$.

## Test statistic

$$F = \frac{SSR/k}{MSE} = \frac{R^2/k}{(1 - R^2)/(n - k - 1)}.$$

If $\epsilon_1,\dots,\epsilon_n$ are normal, then under $H_0$, $F \sim F_{k,\,n-k-1}$ (the F-distribution with `k` and `n-k-1` degrees of freedom).

## Decision

- **Rejection region:** reject $H_0$ if $F \ge F_{k,\,n-k-1;\,\alpha}$, the $(1-\alpha)$ quantile of $F_{k,\,n-k-1}$.
- **p-value:** $P(F > F_{\text{obs}})$ with $F \sim F_{k,\,n-k-1}$; find via the F-table or R.
- Reported on the last line of `summary(lm(...))`.

Example (mesquite): $F = 28.6$, $P = 7.3\times10^{-7}$ ⇒ the model is useful; at least one log-dimension predicts log leaf weight.

## See Also
- [[Reduction Method (Partial F-Test)]]
- [[Multiple Linear Regression]]
- [[Coefficient of Determination]]
