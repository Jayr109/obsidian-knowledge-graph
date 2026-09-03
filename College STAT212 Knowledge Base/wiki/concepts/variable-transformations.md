---
title: "Variable Transformations"
type: concept
tags: [transformations, log, reciprocal, linearization, variance-stabilizing]
sources: [lecture-02-more-general-regression]
course: STAT 212
updated: 2026-07-04
---

Transforming `x` and/or `y` can turn a curved (nonlinear) relationship into a straight-line model, letting us reuse all of [[Simple Linear Regression Model|simple linear regression]]. This is exactly the technique behind the windmill homework (reciprocal of wind speed) and the bacteria homework (log of count).

## Non-polynomial (nonlinear) models

More generally $Y_i = f(x_i; \theta_1,\dots,\theta_k) + \epsilon_i$ with `f` known up to parameters (e.g. $\exp(\theta_1+\theta_2 x+\theta_3 x^2)$ or $\theta_1\cos(2\pi\theta_2 x)$). Least squares still estimates the $\theta$'s, but the normal equations are usually **nonlinear** and harder to solve. Choice of `f` comes from subject-matter knowledge.

## Linearizing transforms

**Multiplicative exponential error** $Y = \alpha e^{\beta x}\epsilon$ ($\epsilon > 0$):
$$\log Y = \log\alpha + \beta x + \log\epsilon,$$
so with $Y' = \log Y$, $\beta_0 = \log\alpha$, $\beta_1 = \beta$, $\epsilon' = \log\epsilon$ we recover the straight-line model $Y' = \beta_0 + \beta_1 x + \epsilon'$.

**Power law** $Y = \alpha x^\beta\epsilon$ ($x > 0$):
$$\log Y = \log\alpha + \beta\log x + \log\epsilon,$$
so taking $x' = \log x$ gives the straight-line model in $(\log x, \log y)$.

**Reciprocal (windmill):** the DC-output vs. wind-speed data linearizes under $x' = 1/x$, giving $Y = \beta_0 + \beta_1(1/x)$ — see [[STAT 212 Overview]] and the earlier windmill worked example.

## Variance-stabilizing role

For $Y = \alpha x^\beta\epsilon$: $\mathrm{Var}(Y) = \alpha^2 x^{2\beta}\mathrm{Var}(\epsilon)$ grows with `x` even if $\epsilon$ has constant variance, but $\mathrm{Var}(\log Y) = \mathrm{Var}(\log\epsilon)$ is constant. **When the response's spread appears to increase (or decrease) with `x`, that is a tipoff to take logs** — restoring the homoskedasticity assumption.

- Example 7 (Beveridge European wheat-price index, 1500–1869): raw residuals fan out (variance grows over time); log-transformed residuals have constant spread and no pattern.

## See Also
- [[Residual Diagnostic Plots]]
- [[Simple Linear Regression Model]]
- [[Polynomial Regression]]
