---
title: "Expected Mean Squares in ANOVA"
type: derivation
tags: [ANOVA, expectation, mean-squares, F-test]
sources: [lecture-04-one-way-anova]
course: STAT 212
updated: 2026-07-04
---

Derives $E(MSE) = \sigma^2$ and $E(MSTr) = \sigma^2 + \tfrac1{k-1}\sum_i n_i(\mu_i-\bar\mu)^2$ for [[One-Way ANOVA]]. These expectations justify the F-test: $MSE$ estimates $\sigma^2$ regardless of $H_0$, while $MSTr$ estimates $\sigma^2$ **only when the means are equal**, so $F = MSTr/MSE \approx 1$ under $H_0$ and $>1$ otherwise.

## Part 1: $E(MSE) = \sigma^2$

| Step | Justification |
|------|---------------|
| $SSE = \sum_{i=1}^k \sum_{j=1}^{n_i}(X_{ij}-\bar X_i)^2 = \sum_i (n_i-1)S_i^2$ | BD (group sample variance $S_i^2 = \tfrac1{n_i-1}\sum_j(X_{ij}-\bar X_i)^2$) |
| $MSE = \dfrac{SSE}{N-k} = \dfrac1{N-k}\sum_i (n_i-1)S_i^2$ | BD (weighted average of the $S_i^2$) |
| $E(S_i^2) = \sigma^2$ for each `i` | BD (sample variance is unbiased; equal variances) |
| $E(MSE) = \dfrac1{N-k}\sum_i (n_i-1)\sigma^2 = \sigma^2$ | Rule of Expectations; MS ($\sum(n_i-1) = N-k$) |

So $E(MSE) = \sigma^2$ **whether or not** $H_0$ holds.

## Part 2: What $MSTr$ estimates

Write $\bar X_i = \mu_i + \bar\epsilon_i$ (where $\bar\epsilon_i = \tfrac1{n_i}\sum_j\epsilon_{ij}$), and $\bar X = \bar\mu + \bar\epsilon$ with $\bar\mu = \tfrac1N\sum_i n_i\mu_i$.

| Step | Justification |
|------|---------------|
| $\bar X_i - \bar X = (\mu_i - \bar\mu) + (\bar\epsilon_i - \bar\epsilon)$ | MS (subtract the two lines above) |
| $(\bar X_i - \bar X)^2 = (\mu_i-\bar\mu)^2 + (\bar\epsilon_i-\bar\epsilon)^2 + 2(\mu_i-\bar\mu)(\bar\epsilon_i-\bar\epsilon)$ | MS (expand the square) |
| $E(SSTr) = \sum_i n_i(\mu_i-\bar\mu)^2 + E\!\left[\sum_i n_i(\bar\epsilon_i-\bar\epsilon)^2\right]$ | Rule of Expectations (cross term has mean 0; X is constant) |
| $\quad = \sum_i n_i(\mu_i-\bar\mu)^2 + (k-1)\sigma^2$ | BD (the error term contributes $(k-1)\sigma^2$) |
| $E(MSTr) = \dfrac{E(SSTr)}{k-1} = \sigma^2 + \dfrac1{k-1}\sum_i n_i(\mu_i-\bar\mu)^2$ | MS (divide by $k-1$) |

## Consequence

$$E(MSTr) = \sigma^2 + \frac1{k-1}\sum_{i=1}^k n_i(\mu_i-\bar\mu)^2.$$

- If all $\mu_i = \bar\mu$ (i.e. $H_0$ true): the sum is 0, so $E(MSTr) = \sigma^2$ ⇒ $F \approx 1$.
- Otherwise $E(MSTr) > \sigma^2$ ⇒ `F` tends to be $> 1$. This is why we reject only for large `F`.

## See Also
- [[One-Way ANOVA]]
- [[Rules of Expectation and Variance]]
