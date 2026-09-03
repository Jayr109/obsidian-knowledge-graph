---
title: "Multiple Comparisons and Tukey's Procedure"
type: method
tags: [ANOVA, multiple-comparisons, tukey, familywise-error, procedure]
sources: [lecture-04-one-way-anova]
course: STAT 212
updated: 2026-07-04
---

After a significant [[One-Way ANOVA]] F-test rejects $H_0: \mu_1 = \cdots = \mu_k$, we want to know *which* pairs of means differ. Testing all pairwise $H_0: \mu_i = \mu_j$ separately inflates the error rate; Tukey's procedure controls it.

## The experimentwise error rate (EWER)

Also called the familywise error rate (FWER): the probability of rejecting **at least one** true null when performing several tests. For `m` **independent** size-$\alpha$ tests, all nulls true:

$$\alpha_E = 1 - (1-\alpha)^m.$$

(By the complement rule and independence.) This grows fast with `m`:

| m | $\alpha_E$ (α=0.05) |
|---|---------------------|
| 1 | 0.050 |
| 3 | 0.143 |
| 5 | 0.226 |
| 10 | 0.401 |
| 20 | 0.642 |
| 50 | 0.923 |

So naive per-comparison testing almost guarantees a false positive with many comparisons.

## Tukey's procedure (HSD)

Controls the EWER at a chosen level $\alpha$ for all pairwise comparisons:

1. Choose the EWER $\alpha$.
2. Find the studentized-range critical value $Q_{\alpha,k,N-k}$ (Table A.7).
3. For each pair $(i,j)$ form the CI for $\mu_i - \mu_j$:
$$\bar X_i - \bar X_j \pm Q_{\alpha,k,N-k}\sqrt{\frac{MSE}{2}\left(\frac1{n_i} + \frac1{n_j}\right)}.$$
4. Declare $\mu_i \ne \mu_j$ (reject $H_0: \mu_i = \mu_j$) for every pair whose interval **excludes 0**.

This holds the overall (experimentwise) error rate at $\alpha$.

## In R
```r
TukeyHSD(aov(pounds ~ varieties))          # all pairwise 95% CIs
plot(TukeyHSD(aov(pounds ~ varieties)))    # visual
```
Example (orange-tree yields, $k=5$, $n=7$): only variety C's mean yield is significantly higher than variety A's; no other pair differs significantly.

## See Also
- [[One-Way ANOVA]]
- [[Two-Way ANOVA]]
