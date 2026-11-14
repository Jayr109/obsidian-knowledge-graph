---
title: "Signed-Rank Test"
type: concept
tags: [nonparametric, signed-rank, wilcoxon, median, hypothesis-test]
sources: [lecture-07-nonparametric-methods]
course: STAT 212
updated: 2026-07-04
---

The signed-rank test (Wilcoxon) tests the population median/center $\tilde\mu$ while assuming the population is **symmetric** (but not necessarily Normal). By using the *ranks* of the deviations — not just their signs — it retains more information than the [[Sign Test]] and is often more powerful.

## Procedure

Random sample $X_1,\dots,X_n$; test $H_0: \tilde\mu = c$.

1. Rank $|X_1 - c|, \dots, |X_n - c|$ from smallest to largest, keeping track of the sign of each $X_i - c$.
2. Let $I(x) = 1$ if $x \ge 0$, else 0; let $R(|X_i - c|)$ be the rank of $|X_i - c|$.
3. Compute the signed-rank statistic (sum of ranks with **positive** signs):
$$S_+ = \sum_{i=1}^n I(X_i - c)\, R(|X_i - c|).$$
4. Standardize:
$$Z = \frac{S_+ - n(n+1)/4}{\sqrt{n(n+1)(2n+1)/24}} \approx N(0,1) \text{ for } n \ge 10.$$

## Rejection regions

| Alternative | Reject $H_0$ if |
|-------------|------------------|
| $H_a: \tilde\mu > c$ | $Z \ge z_\alpha$ |
| $H_a: \tilde\mu < c$ | $Z \le -z_\alpha$ |
| $H_a: \tilde\mu \ne c$ | $\lvert Z \rvert \ge z_{\alpha/2}$ |

- Example (arthritis pH, $c = 7.39$, $n = 14$): density looks roughly symmetric (so the test applies); $S_+ = 1 + 4 + 13 = 18$, $Z = \dfrac{18 - 14\cdot15/4}{\sqrt{14\cdot15\cdot29/24}} = -2.166$ ⇒ reject; median pH < 7.39 ($P = 0.03$). Agrees with, and is slightly stronger than, the sign test.

## When to use it

- Requires the extra **symmetry** assumption that the sign test does not.
- More powerful than the sign test because it uses the magnitude (via ranks), not just the sign of each deviation.

## See Also
- [[Sign Test]]
- [[Kruskal-Wallis Test]]
