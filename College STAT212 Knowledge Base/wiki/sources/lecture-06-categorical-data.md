---
title: "Source: Categorical Data Analysis (Notes 6)"
type: source
tags: [categorical-data, multinomial, chi-square, goodness-of-fit, contingency-tables]
sources: [lecture-06-categorical-data]
course: STAT 212
updated: 2026-07-04
---

Summary of the sixth set of course notes, *Categorical Data Analysis* (slides 172–217). Categorical (count) data record how many cases fall into each category. Covers the multinomial model, chi-square goodness-of-fit tests (with fully specified or estimated category probabilities), and contingency-table tests for homogeneity of proportions and independence.

## Contents by slide

- **Slides 172–177 — Setup & multinomial.** Categorical/count data; cross-classified tables; the [[Multinomial Distribution]] (generalizes the binomial); $E(N_i)=np_i$, $Var(N_i)=np_i(1-p_i)$.
- **Slides 178–184 — GOF, specified probs.** [[Chi-Square Goodness-of-Fit Test]]: $H_0$ fully specifies $p_{i0}$; $\chi^2 = \sum(N_i - np_{i0})^2/(np_{i0}) \sim \chi^2_{r-1}$. Grand-jury example ($\chi^2=61.3$, reject).
- **Slides 185–200 — GOF, estimated params.** When $H_0$ leaves parameters free, estimate them and lose df: $\chi^2 \sim \chi^2_{r-1-\ell}$. Poisson traffic example ($\ell=1$); Normality-check example ($\ell=2$).
- **Slides 201–209 — Homogeneity.** [[Contingency Tables and Chi-Square]] (homogeneity of proportions across `k` populations): $\hat e_{ij}=n_i n_{\cdot j}/n$, df $=(k-1)(r-1)$. Market-study example.
- **Slides 210–217 — Independence.** Independence of two traits in one sample: $H_0: p_{ij}=p_{i\cdot}p_{\cdot j}$; same $\chi^2$, df $=(I-1)(J-1)$. Gun-control example ($\chi^2=43.25$, reject).

## Key facts referenced
- GOF validity: $r\ge3$ and each expected count (roughly) $\ge 5$.
- Estimating $\ell$ parameters reduces GOF df to $r-1-\ell$ (need $r-1>\ell$).
- Homogeneity and independence tests are computationally identical; sampling scheme and hypothesis differ.

## See Also
- [[Multinomial Distribution]]
- [[Chi-Square Goodness-of-Fit Test]]
- [[Contingency Tables and Chi-Square]]
- [[STAT 212 Overview]]
