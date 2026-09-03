---
title: "Simple Linear Regression Model"
type: concept
tags: [regression, model, assumptions]
sources: [lecture-01-simple-linear-regression]
course: STAT 212
updated: 2026-07-04
---

The simple linear regression (SLR) model describes the relationship between a single predictor `x` and a response `Y` as a straight line plus random error. The response is modeled as $Y_i = \beta_0 + \beta_1 x_i + \epsilon_i$ for $i = 1, \dots, n$, where the $\epsilon_i$ are random "noise." The goal (the *statistical problem*) is to infer the unknown parameters $\beta_0$, $\beta_1$, and $\sigma^2$ from data $(x_1, y_1), \dots, (x_n, y_n)$.

## Variables

- $x_1, \dots, x_n$ — the **predictor** (also: control, independent, explanatory, covariate, regressor, feature). Values are **fixed by the experimenter** (or treated as conditioned/fixed even if random).
- $Y_1, \dots, Y_n$ — the **response** (also: outcome, dependent variable). These are **random variables** (capital `Y`), even though each $x_i$ is fixed.

## The four assumptions

1. $\epsilon_1, \dots, \epsilon_n$ are **unobserved** random variables (errors / noise).
2. The $\epsilon_i$ are **independent** of each other. → tag [[Rules of Expectation and Variance|Independence]]
3. Each $\epsilon_i \sim N(0, \sigma^2)$ — normal, mean 0, and **constant variance** for all `i` (the *homoskedasticity* assumption).
4. $\beta_0$ (intercept), $\beta_1$ (slope), and $\sigma^2$ (error variance) are **unknown but fixed** parameters.

## Consequences of the model

$$E(Y_i) = \beta_0 + \beta_1 x_i, \qquad \mathrm{Var}(Y_i) = \sigma^2.$$

Because $E(\epsilon_i) = 0$, the mean response is a linear function of `x`; because $\mathrm{Var}(\epsilon_i) = \sigma^2$, every response has the same spread. See the derivation-style steps in [[Rules of Expectation and Variance]].

- **Interpretation of the mean:** the average value of `Y` in the sub-population where the predictor equals `x` lies on the line $y = \beta_0 + \beta_1 x$.
- **Interpretation of $\sigma^2$:** it controls how tightly points cluster about the line. If $\sigma^2 = 0$ the relationship is deterministic.
- **Interpretation of the slope $\beta_1$:** the change in the *average* response for a 1-unit increase in `x`. (E.g. $\beta_1 = -5$ means the average response drops by 5 per unit increase in `x`.)

## Two sources of "noise" (Examples 1 & 2)

- **Example 1 (Galileo gravity):** the true relationship $y = \sqrt{2x/g}$ is exact; differences at the same height are *only* measurement error.
- **Example 2 ([[Sir Francis Galton]] heights):** differences among sons of equal-height fathers are *intrinsic*, not just measurement error — illustrating "regression toward the mean" (slope of the line of averages is < 1).

## See Also
- [[Least Squares Estimation]]
- [[Residuals and Model Diagnostics]]
- [[Coefficient of Determination]]
- [[Sampling Distribution of the Slope Estimator]]
- [[Rules of Expectation and Variance]]
