# STAT 212 Knowledge Base — Master Index

Master catalog of all wiki pages. Updated on every ingest.

---

## Overview
- [[STAT 212 Overview]] — high-level synthesis and course arc

## Concepts
- [[Simple Linear Regression Model]] — the SLR model, its four assumptions, and interpretation
- [[Least Squares Estimation]] — minimizing squared deviations to estimate the line
- [[Coefficient of Determination]] — $R^2$ and the sums-of-squares it comes from
- [[Residuals and Model Diagnostics]] — residuals, $\hat\sigma^2$, and assumption checks
- [[Correlation Coefficient]] — $\rho$, its estimator $R$, and testing $\rho=0$
- [[Polynomial Regression]] — degree-$k$ model, still linear in the parameters
- [[Model Selection Criteria]] — adjusted $R^2$, AIC, BIC for choosing complexity
- [[Variable Transformations]] — log/reciprocal transforms that linearize curved data
- [[Multiple Linear Regression]] — several predictors; interaction & quadratic terms
- [[Influential Observations and Cook's D]] — outliers, leverage, Cook's distance
- [[One-Way ANOVA]] — comparing $k$ group means via between/within variance
- [[Two-Way ANOVA]] — two factors, interaction, and main effects
- [[Experimental Design: CRD and Randomized Block]] — CRD vs. blocking to reduce noise
- [[Multinomial Distribution]] — the model for categorical/count data
- [[Chi-Square Goodness-of-Fit Test]] — observed vs. expected counts
- [[Contingency Tables and Chi-Square]] — homogeneity and independence tests
- [[Sign Test]] — distribution-free test for the median
- [[Signed-Rank Test]] — Wilcoxon test for symmetric populations
- [[Kruskal-Wallis Test]] — nonparametric one-way ANOVA

## Derivations
- [[Least Squares Estimators Derivation]] — $\hat\beta_0, \hat\beta_1$ via the normal equations
- [[Sum of Deviations Equals Zero]] — $\sum(x_i-\bar x)=0$ (theory HW Problem 1)
- [[Slope Estimator in Deviation Form]] — the two forms of $\hat\beta_1$ agree (theory HW Problem 3)
- [[Slope as Correlation Times SD Ratio]] — $\hat\beta_1 = \hat\rho\,\hat\sigma_Y/\hat\sigma_X$ (theory HW Problem 4)
- [[ANOVA Decomposition of SST]] — proof that $SST = SSE + SSR$
- [[Unbiasedness of the Slope Estimator]] — proof that $E(\hat\beta_1) = \beta_1$
- [[Prediction Error Variance]] — the "$1+$" term behind wider prediction intervals
- [[Polynomial Normal Equations in Matrix Form]] — $\hat\beta = (X^TX)^{-1}X^Ty$
- [[Expected Mean Squares in ANOVA]] — why $E(MSTr)\ge E(MSE)$ justifies the F-test

## Theorems & Rules
- [[Sampling Distribution of the Slope Estimator]] — properties of $\hat\beta_1$, slope CI & test
- [[Inference for the Mean Response and Prediction]] — CI for $E(Y)$ and prediction interval
- [[Inference for Polynomial Regression]] — coefficient/mean/prediction inference (matrix form)
- [[F-Test for Model Utility]] — overall test that any predictor matters
- [[Reduction Method (Partial F-Test)]] — test a subset of predictors via full vs. reduced SSE
- [[Rules of Expectation and Variance]] — $E[\cdot]$/$\mathrm{Var}[\cdot]$ reference with justification tags

## Methods
- [[Residual Diagnostic Plots]] — residual/QQ/density plots to check assumptions (R)
- [[Confidence and Prediction Intervals in R]] — `lm`, `confint`, `predict`, `cor.test`
- [[Multiple Comparisons and Tukey's Procedure]] — which means differ; EWER control

## Courses
- [[STAT 212 Course]] — topics, tools, and conventions

## People
- [[Sir Francis Galton]] — pioneer of regression and correlation; father–son height data

## Sources
- [[Source: Simple Linear Regression and Correlation (Notes 1)]] — Notes 1 (44 slides)
- [[Source: More General Regression Analyses (Notes 2)]] — Notes 2 (slides 46–79)
- [[Source: Multiple Regression (Notes 3)]] — Notes 3 (slides 81–112)
- [[Source: Analysis of Variance — One-Way ANOVA (Notes 4)]] — Notes 4 (slides 114–139)
- [[Source: Multifactor ANOVA — Two-Way ANOVA (Notes 5)]] — Notes 5 (slides 141–170)
- [[Source: Categorical Data Analysis (Notes 6)]] — Notes 6 (slides 172–217)
- [[Source: Distribution-Free Procedures (Notes 7)]] — Notes 7 (slides 219–239)
