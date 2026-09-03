---
title: "Model Selection Criteria"
type: concept
tags: [model-selection, adjusted-R-squared, AIC, BIC, parsimony]
sources: [lecture-02-more-general-regression]
course: STAT 212
updated: 2026-07-04
---

Criteria for choosing model complexity (e.g. polynomial degree `k`) that balance fit against parsimony. The core problem: raw [[Coefficient of Determination|$R^2$]] is **guaranteed to increase** with degree ($R^2_1 < R^2_2 < \cdots < R^2_{n-1} = 1$), so maximizing $R^2$ always picks the most complex model — violating Occam's razor.

## Adjusted $R^2$

Penalizes $R^2_k$ by the number of parameters:

$$R^2_{\text{adj},k} = \frac{(n-1)R^2_k - k}{n-1-k} = R^2_k - \frac{k}{n-1-k}(1 - R^2_k).$$

The penalty grows with `k`; choose the `k` that **maximizes** $R^2_{\text{adj},k}$. In R: `summary(fit)$adj`.

## AIC and BIC

Let $SSE_k$ be the SSE for the degree-`k` model:

$$AIC_k = n\log(SSE_k) + 2k, \qquad BIC_k = n\log(SSE_k) + k\log(n).$$

Choose `k` to **minimize** AIC (or BIC). Because $\log(n) > 2$ for $n \ge 8$, **BIC penalizes complexity more than AIC**, so BIC tends to pick smaller/simpler models. In R: `AIC(fit)` and `AIC(fit, k = log(length(y)))`.

## How well they work (simulation, true degree 3)

| Criterion | % choosing correct degree 3 | Tendency |
|-----------|------------------------------|----------|
| BIC | 84.0% | best; favors simpler models |
| AIC | 52.5% | second best |
| Adjusted $R^2$ | 23.1% | worst; over-estimates degree |

Larger `n` improves all three. AIC/BIC are preferred over adjusted $R^2$ for degree selection.

## See Also
- [[Polynomial Regression]]
- [[Coefficient of Determination]]
