---
title: "Chi-Square Goodness-of-Fit Test"
type: concept
tags: [chi-square, goodness-of-fit, categorical-data, hypothesis-test]
sources: [lecture-06-categorical-data]
course: STAT 212
updated: 2026-07-04
---

The chi-square goodness-of-fit (GOF) test checks how well a model for the category probabilities of a [[Multinomial Distribution]] fits observed counts. The core idea: compare **observed** counts $N_i$ with the **expected** counts under $H_0$.

## The statistic

If $H_0$ is true, the expected count in category `i` is $E(N_i) = np_{i0}$. The overall discrepancy is

$$\chi^2 = \sum_{i=1}^r \frac{(N_i - np_{i0})^2}{np_{i0}} \approx \chi^2_{r-1}\ \text{under } H_0.$$

Reject $H_0$ at level $\alpha$ if $\chi^2 \ge \chi^2_{r-1,\,\alpha}$.

**Validity conditions:** $r \ge 3$, and the expected counts should not be too small (rule of thumb: all $np_{i0} \ge 5$).

## Case 1 — fully specified probabilities

$H_0: p_1 = p_{10}, \dots, p_r = p_{r0}$ with the $p_{i0}$ known and summing to 1. Degrees of freedom $= r-1$.

- Example (grand jury): test whether 66 jurors match county age percentages (0.42, 0.23, 0.16, 0.19). $\chi^2 = 61.27 > \chi^2_{3,0.05}=7.815$ ⇒ reject; older jurors over-represented ($P < 0.005$).

## Case 2 — probabilities depend on estimated parameters

If $H_0$ leaves $\ell$ parameters $\theta$ free, estimate them (ideally by minimum-$\chi^2$; often a simple estimate suffices), compute estimated expected counts $n\pi_i(\hat\theta)$, then

$$\chi^2 = \sum_{i=1}^r \frac{(N_i - n\pi_i(\hat\theta))^2}{n\pi_i(\hat\theta)} \approx \chi^2_{r-1-\ell}.$$

Each estimated parameter costs one degree of freedom (need $r-1 > \ell$).

- **Poisson fit** (traffic accidents, $\ell=1$, $\hat\theta$ = sample mean = 2.12): $\chi^2 = 2.74 < \chi^2_{4,0.05}=9.488$ ⇒ do not reject; counts consistent with Poisson.
- **Normality check** ($\ell=2$, estimate $\bar X$ and $s^2$): bin the data, expected count = $n\cdot P(\text{class})$ from $N(\bar X, s^2)$. Buffalo snowfall: $\chi^2=1.41 < \chi^2_{3,0.05}=7.815$ ⇒ consistent with Normal. (A rigorous alternative to the eyeball [[Residual Diagnostic Plots|QQ plot]].)

## See Also
- [[Multinomial Distribution]]
- [[Contingency Tables and Chi-Square]]
- [[Residual Diagnostic Plots]]
