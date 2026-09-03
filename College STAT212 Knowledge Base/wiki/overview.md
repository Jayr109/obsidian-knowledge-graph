---
title: "STAT 212 Overview"
type: overview
tags: [overview, synthesis]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

High-level synthesis of the STAT 212 knowledge base. STAT 212 is a mathematical-statistics course centered on **regression and the analysis of variance**, taught largely through step-by-step derivations (using $E[\cdot]$/$\mathrm{Var}[\cdot]$ algebra) plus applied model-fitting and diagnostics in R.

## Course arc (by source) — all 7 note sets ingested

1. **[[Simple Linear Regression Model|Simple Linear Regression]]** — one predictor, one response; least squares, $R^2$, residual diagnostics, inference for the slope, CIs/PIs, and correlation.
2. **[[Variable Transformations|More General Regression]]** — [[Polynomial Regression|polynomials]], [[Model Selection Criteria|model selection]] (adj. $R^2$/AIC/BIC), and transformations that linearize curved data (the reciprocal fit behind the windmill data; the log fit behind the bacteria data).
3. **[[Multiple Linear Regression]]** — several predictors; matrix least squares, [[F-Test for Model Utility|model-utility F-test]], the [[Reduction Method (Partial F-Test)|partial F-test]], and [[Influential Observations and Cook's D|influence diagnostics]].
4. **[[One-Way ANOVA]]** — comparing $k$ group means via between/within variance; [[Multiple Comparisons and Tukey's Procedure|Tukey]] follow-up.
5. **[[Two-Way ANOVA]]** — two factors, interaction, main effects; [[Experimental Design: CRD and Randomized Block|CRD vs. randomized block]].
6. **[[Multinomial Distribution|Categorical Data]]** — [[Chi-Square Goodness-of-Fit Test|goodness-of-fit]] and [[Contingency Tables and Chi-Square|contingency-table]] chi-square tests.
7. **Nonparametric Methods** — distribution-free [[Sign Test|sign]], [[Signed-Rank Test|signed-rank]], and [[Kruskal-Wallis Test|Kruskal-Wallis]] tests.

## Central through-lines

- **The linear model** $Y_i = \beta_0 + \beta_1 x_i + \epsilon_i$ and its four assumptions ([[Simple Linear Regression Model]]) generalize to every later topic.
- **Sums of squares** decompositions ([[ANOVA Decomposition of SST]]) recur in $R^2$, ANOVA, and $F$-tests.
- **Derivation discipline:** expectation/variance manipulations use the [[Rules of Expectation and Variance]] with the course's justification tags.
- **Diagnostics:** residual plots, QQ plots, and density plots ([[Residual Diagnostic Plots]]) check assumptions across models.

## See Also
- [[Simple Linear Regression Model]]
- [[STAT 212 Course]]
