---
title: "Source: Distribution-Free Procedures (Notes 7)"
type: source
tags: [nonparametric, distribution-free, sign-test, signed-rank, kruskal-wallis]
sources: [lecture-07-nonparametric-methods]
course: STAT 212
updated: 2026-07-04
---

Summary of the seventh set of course notes, *Distribution-Free Procedures* (slides 219–239). Nonparametric (distribution-free) methods stay valid under very general conditions — no Normality assumption — which matters most for small samples. Covers the sign test, the signed-rank test, and the Kruskal-Wallis test (nonparametric ANOVA).

## Contents by slide

- **Slides 219–220 — Motivation.** Parametric tests (`t`-test, ANOVA) rely on Normality, especially for small `n`. Nonparametric tests relax this.
- **Slides 220–227 — Sign test.** [[Sign Test]]: tests the population **median** $\tilde\mu$; statistic $Y$ = # of $X_i > c$; Normal approximation for $n \ge 10$. Arthritis pH example. Pros/cons vs. `t`-test.
- **Slides 228–233 — Signed-rank test.** [[Signed-Rank Test]]: assumes **symmetry**; uses ranks of $|X_i - c|$; statistic $S_+$; more powerful than the sign test. Same pH example.
- **Slides 234–239 — Kruskal-Wallis.** [[Kruskal-Wallis Test]]: distribution-free [[One-Way ANOVA]]; ranks all data, compares mean ranks; $KW \sim \chi^2_{k-1}$. Strontium-90 milk example.

## Key facts referenced
- Sign test statistic: $\dfrac{Y - n/2}{\sqrt n/2} \approx N(0,1)$ under $H_0$ (median = c).
- Signed-rank: $Z = \dfrac{S_+ - n(n+1)/4}{\sqrt{n(n+1)(2n+1)/24}}$.
- Kruskal-Wallis is essentially an F-test on the **ranks**, referred to $\chi^2_{k-1}$.
- Heavy-tailed populations: sign/rank tests can beat the `t`-test; Normal populations: `t`-test wins.

## See Also
- [[Sign Test]]
- [[Signed-Rank Test]]
- [[Kruskal-Wallis Test]]
- [[STAT 212 Overview]]
