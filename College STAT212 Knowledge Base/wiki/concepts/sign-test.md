---
title: "Sign Test"
type: concept
tags: [nonparametric, sign-test, median, hypothesis-test]
sources: [lecture-07-nonparametric-methods]
course: STAT 212
updated: 2026-07-04
---

The sign test is a distribution-free test for the population **median** $\tilde\mu$ (where $P(X \ge \tilde\mu) = P(X \le \tilde\mu) = \tfrac12$). It is the nonparametric counterpart of the one-sample `t`-test, which targets the **mean**. For symmetric populations the mean and median coincide; for skewed ones the two tests address different hypotheses.

## Setup and statistic

Random sample $X_1,\dots,X_n$; test $H_0: \tilde\mu = c$. The test statistic counts how many observations exceed `c`:

$$Y = \#\{X_i > c\}.$$

Under $H_0$, about half the $X_i$ exceed `c`, so $Y \sim \text{Binomial}(n, \tfrac12)$. Under $H_a: \tilde\mu > c$, `Y` tends to be larger.

## Normal approximation (n ≥ 10)

$$\frac{Y - n/2}{\sqrt n / 2} \approx N(0,1) \text{ under } H_0.$$

Rejection regions:

| Alternative | Reject $H_0$ if |
|-------------|------------------|
| $H_a: \tilde\mu > c$ | $\dfrac{Y-n/2}{\sqrt n/2} \ge z_\alpha$ |
| $H_a: \tilde\mu < c$ | $\dfrac{Y-n/2}{\sqrt n/2} \le -z_\alpha$ |
| $H_a: \tilde\mu \ne c$ | $\dfrac{\lvert Y-n/2 \rvert}{\sqrt n/2} \ge z_{\alpha/2}$ |

- Example (arthritis pH, $c = 7.39$, $n = 14$, $Y = 3$): statistic $= \dfrac{3-7}{\sqrt{14}/2} = -2.138$, two-sided $P = 0.0325$ ⇒ reject; median pH of sufferers (sample median 7.25) is lower.

## Pros and cons

- **Pros:** only assumes a random sample — nothing about the distribution's shape; often more powerful than the `t`-test for **heavy-tailed** populations.
- **Cons:** if the population really is Normal, the `t`-test is more powerful; the sign test discards magnitude information (only uses signs) — the [[Signed-Rank Test]] recovers some of that.

## See Also
- [[Signed-Rank Test]]
- [[Kruskal-Wallis Test]]
