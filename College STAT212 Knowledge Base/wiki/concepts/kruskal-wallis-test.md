---
title: "Kruskal-Wallis Test"
type: concept
tags: [nonparametric, kruskal-wallis, ANOVA, ranks, hypothesis-test]
sources: [lecture-07-nonparametric-methods]
course: STAT 212
updated: 2026-07-04
---

The Kruskal-Wallis (KW) test is the distribution-free analogue of [[One-Way ANOVA]]: it tests whether `k` populations have the same center (median), without assuming Normality. It is essentially an F-test performed on the **ranks** of the data, referred to a chi-square distribution.

## Assumptions and hypotheses

- A random sample from each of `k` populations (sizes $n_1,\dots,n_k$, $N = \sum n_i$).
- All populations have the **same distribution shape**, possibly shifted (the shape can be anything — this replaces the Normality of the [[One-Way ANOVA]] model).

$$H_0: \tilde\mu_1 = \tilde\mu_2 = \cdots = \tilde\mu_k \quad (\tilde\mu_i = \text{median of population } i).$$

## Procedure

1. Rank **all** `N` observations from smallest to largest; let $R_{ij}$ be the rank of $X_{ij}$.
2. Group mean rank $\bar R_i = \tfrac1{n_i}\sum_j R_{ij}$, and
$$s^2_{KW} = \frac1{N-1}\sum_{i=1}^k\sum_{j=1}^{n_i}\left(R_{ij} - \frac{N+1}{2}\right)^2.$$
3. Test statistic:
$$KW = \frac{1}{s^2_{KW}}\sum_{i=1}^k n_i\left(\bar R_i - \frac{N+1}{2}\right)^2.$$
4. Under $H_0$, $KW \approx \chi^2_{k-1}$. Reject $H_0$ at level $\alpha$ if $KW \ge \chi^2_{k-1,\,\alpha}$.

**Validity:** each $n_i \ge 6$ when $k=3$, or each $n_i \ge 5$ when $k > 3$.

## Relation to ANOVA

KW is (essentially) the [[One-Way ANOVA]] F-test with the raw data replaced by their ranks — but compared to a $\chi^2_{k-1}$ rather than an F-distribution.

- Example (strontium-90 in milk, $k=4$ regions, $n_i=5$): $\bar R = (6.2, 13.6, 5.2, 17)$, $s^2_{KW}=35$, $KW = 14.06 > \chi^2_{3,0.005}=12.838$ ⇒ reject; regions 2 and 4 have higher levels than 1 and 3 (pairwise KW can confirm).

## See Also
- [[One-Way ANOVA]]
- [[Sign Test]]
- [[Signed-Rank Test]]
