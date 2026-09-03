---
title: "Source: Analysis of Variance — One-Way ANOVA (Notes 4)"
type: source
tags: [ANOVA, one-way, F-test, multiple-comparisons, tukey]
sources: [lecture-04-one-way-anova]
course: STAT 212
updated: 2026-07-04
---

Summary of the fourth set of course notes, *Analysis of Variance* (slides 114–139), covering **single-factor (one-way) ANOVA**. ANOVA compares the means of `k` groups by comparing between-group to within-group variance. Covers the model, the sums-of-squares decomposition, the ANOVA table and F-test, the expected mean squares that justify the test, and multiple-comparison procedures (experimentwise error rate and Tukey's HSD).

## Contents by slide

- **Slides 114–118 — Setup.** ANOVA compares means via variance. Single factor with `k` levels; connection to regression (factor levels as a numeric predictor).
- **Slides 116–117 — The model.** [[One-Way ANOVA]]: $X_{ij} = \mu_i + \epsilon_{ij}$, $\epsilon_{ij}\sim N(0,\sigma^2)$ iid; each group is an independent sample from $N(\mu_i,\sigma^2)$.
- **Slides 119–121 — Sums of squares.** $H_0: \mu_1=\cdots=\mu_k$; group/grand means; $SSTr$ (between), $SSE$ (within), and $SST = SSTr + SSE$.
- **Slides 122–125 — F-test.** ANOVA table; $MSTr = SSTr/(k-1)$, $MSE = SSE/(N-k)$; $F = MSTr/MSE \sim F_{k-1,\,N-k}$.
- **Slides 126–130 — Expected mean squares.** [[Expected Mean Squares in ANOVA]]: $E(MSE)=\sigma^2$ always; $E(MSTr)=\sigma^2 + \tfrac1{k-1}\sum n_i(\mu_i-\bar\mu)^2$; so `F` ≈ 1 under $H_0$.
- **Slides 131–133 — R & example.** `aov(Response ~ as.factor(Factors))`; iron-formations example ($F=10.85$, $P=3.2\times10^{-5}$).
- **Slides 134–139 — Multiple comparisons.** [[Multiple Comparisons and Tukey's Procedure]]: experimentwise error rate (EWER); Tukey's HSD.

## Key facts referenced
- $F = MSTr/MSE$; reject $H_0$ if $F \ge F_{k-1,\,N-k;\,\alpha}$. `F ≤ 1` never signals a difference.
- EWER with `m` independent size-α tests: $\alpha_E = 1 - (1-\alpha)^m$ (e.g. 5 tests → 0.226).
- Tukey CI: $\bar X_i - \bar X_j \pm Q_{\alpha,k,N-k}\sqrt{\tfrac{MSE}{2}(\tfrac1{n_i}+\tfrac1{n_j})}$.

## See Also
- [[One-Way ANOVA]]
- [[Expected Mean Squares in ANOVA]]
- [[Multiple Comparisons and Tukey's Procedure]]
- [[STAT 212 Overview]]
