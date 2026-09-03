---
title: "Reduction Method (Partial F-Test)"
type: theorem
tags: [F-test, reduction-method, nested-models, hypothesis-test]
sources: [lecture-03-multiple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

The reduction method (partial F-test) tests whether a **subset** of predictors can be dropped from a [[Multiple Linear Regression]] model. It compares a full model against a nested reduced model. **Do not** test a subset by running separate single-coefficient `t`-tests — that can give incorrect conclusions; use this joint test.

## Hypotheses

For a `k`-predictor model, test that the last $\ell$ coefficients are 0 (relabel so the tested ones are last):

$$H_0: \beta_{k-\ell+1} = \beta_{k-\ell+2} = \cdots = \beta_k = 0.$$

$H_0$ says those $\ell$ predictors are not needed alongside the others.

## Test statistic

Fit the **full** model (all `k` predictors) → $SSE_f$. Fit the **reduced** model (drop the $\ell$ predictors) → $SSE_r$. Then

$$F = \frac{(SSE_r - SSE_f)/\ell}{SSE_f/(n - k - 1)} \sim F_{\ell,\,n-k-1} \text{ under } H_0.$$

$F$ is always $\ge 0$ because $SSE_r \ge SSE_f$: adding predictors can never increase the least-squares SSE.

## Decision

Reject $H_0$ iff $F \ge F_{\ell,\,n-k-1;\,\alpha}$ (or via the p-value). In R, `anova(fit)` supplies the SSEs.

Example (mesquite, $H_0: \beta_1 = \beta_3 = 0$): $SSE_f = 2.0368$, $SSE_r = 2.8261$, $F = \dfrac{(2.8261 - 2.0368)/2}{2.0368/15} = 2.906 < F_{2,15;0.05} = 3.68$ ⇒ do **not** reject; the reduced 2-predictor model ($R^2 = 0.84$ vs. 0.88) is nearly as good and simpler.

## See Also
- [[F-Test for Model Utility]]
- [[Multiple Linear Regression]]
- [[Model Selection Criteria]]
