---
title: "One-Way ANOVA"
type: concept
tags: [ANOVA, one-way, F-test, sums-of-squares]
sources: [lecture-04-one-way-anova]
course: STAT 212
updated: 2026-07-04
---

One-way (single-factor) analysis of variance tests whether the means of `k` groups (levels of one factor) are equal. Despite its name, ANOVA compares **means** — it does so by comparing the variance *between* groups to the variance *within* groups. It shares the sums-of-squares structure of [[Coefficient of Determination|regression]].

## The model

For groups $i = 1,\dots,k$ with $n_i$ observations each:

$$X_{ij} = \mu_i + \epsilon_{ij}, \qquad \epsilon_{ij} \sim N(0, \sigma^2)\ \text{iid}.$$

Equivalently, group `i`'s data $X_{i1},\dots,X_{in_i}$ is an independent random sample from $N(\mu_i, \sigma^2)$ — all groups share the **same variance** $\sigma^2$. Total sample size $N = n_1 + \cdots + n_k$.

## Hypotheses

$$H_0: \mu_1 = \mu_2 = \cdots = \mu_k \quad\text{vs.}\quad H_a: \text{at least two } \mu_i \text{ differ}.$$

Estimates: group means $\bar X_i = \tfrac1{n_i}\sum_j X_{ij}$; grand mean $\bar X = \tfrac1N\sum_i\sum_j X_{ij} = \tfrac1N\sum_i n_i\bar X_i$.

## Sums of squares

| Quantity | Formula | Measures |
|----------|---------|----------|
| $SSTr$ (treatment/between) | $\sum_{i=1}^k n_i(\bar X_i - \bar X)^2$ | variation **between** groups (explained) |
| $SSE$ (error/within) | $\sum_{i=1}^k\sum_{j=1}^{n_i}(X_{ij}-\bar X_i)^2$ | variation **within** groups (unexplained) |
| $SST$ (total) | $\sum_{i=1}^k\sum_{j=1}^{n_i}(X_{ij}-\bar X)^2$ | all variation |

with the decomposition $SST = SSTr + SSE$ (same idea as the [[ANOVA Decomposition of SST]] in regression).

## ANOVA table and F-test

| Source | df | SS | MS | F |
|--------|----|----|----|---|
| Treatments | $k-1$ | $SSTr$ | $MSTr = SSTr/(k-1)$ | $MSTr/MSE$ |
| Error | $N-k$ | $SSE$ | $MSE = SSE/(N-k)$ | |
| Total | $N-1$ | $SST$ | | |

$$F = \frac{MSTr}{MSE} \sim F_{k-1,\,N-k}\ \text{under } H_0.$$

Reject $H_0$ at level $\alpha$ if $F \ge F_{k-1,\,N-k;\,\alpha}$ (or via the p-value). `F` is expected to be ≈ 1 under $H_0$ and larger when means differ — see [[Expected Mean Squares in ANOVA]]. A value $F \le 1$ never signals a difference.

## In R
```r
fit = aov(Response ~ as.factor(Factors), data = Data)
anova(fit)
```
Example (iron in 4 formations, $k=4$, $n_i=10$): $F = 10.85$, $P = 3.2\times10^{-5}$ ⇒ mean iron differs across formations. To find *which* differ, use [[Multiple Comparisons and Tukey's Procedure]].

## See Also
- [[Expected Mean Squares in ANOVA]]
- [[Multiple Comparisons and Tukey's Procedure]]
- [[Two-Way ANOVA]]
- [[F-Test for Model Utility]]
