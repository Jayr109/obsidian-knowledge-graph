---
title: "Contingency Tables and Chi-Square"
type: concept
tags: [contingency-table, chi-square, homogeneity, independence, categorical-data]
sources: [lecture-06-categorical-data]
course: STAT 212
updated: 2026-07-04
---

A contingency table cross-classifies counts by two traits (rows and columns). Two classic questions — **homogeneity of proportions** and **independence** — are tested with the *same* chi-square statistic, differing only in sampling scheme and hypothesis. This is the categorical analogue of comparing several populations, like [[One-Way ANOVA]] is for continuous data.

## The common test statistic

With observed cell counts $n_{ij}$ and estimated expected counts

$$\hat e_{ij} = \frac{(\text{row } i\text{ total})(\text{col } j\text{ total})}{n},$$

$$\chi^2 = \sum_i \sum_j \frac{(n_{ij} - \hat e_{ij})^2}{\hat e_{ij}}.$$

Reject $H_0$ if $\chi^2 \ge \chi^2_{\text{df},\,\alpha}$. Validity requires all expected counts $\ge 5$ (roughly).

## Homogeneity of proportions

Setup: `k` **separate** populations, each sampled independently (row totals $n_i$ fixed by design), each split into the same `r` categories. Test whether the category proportions are equal across populations:

$$H_0: p_{1j} = p_{2j} = \cdots = p_{kj}\ \text{for all } j, \qquad \text{df} = (k-1)(r-1).$$

- Example (market study, 3 cities × 3 awareness levels): $\chi^2 = 24.61$, df $= 4$ ⇒ reject; cities 1 and 3 similar, city 2 differs.

## Independence of two traits

Setup: a **single** sample of `n` items, each classified by two traits; **neither** row nor column totals fixed in advance. Test whether the two traits are independent:

$$H_0: p_{ij} = p_{i\cdot}\,p_{\cdot j}\ \text{for all } i,j, \qquad \text{df} = (I-1)(J-1).$$

This says row-membership is independent of column-membership (equivalently, the conditional distribution across rows is the same for every column).

- Example (500 voters: political affiliation × gun-control attitude): $\chi^2 = 43.25 > \chi^2_{4,0.05}=9.488$ ⇒ reject; attitude depends on affiliation (Democrats favor stricter control more than Republicans).

## Homogeneity vs. independence

The arithmetic is identical. They differ in the **sampling method** (several fixed-size samples vs. one sample) and in the **hypothesis** (equal proportions across populations vs. independence of two traits). The distinction matters more for tables with >2 traits.

## See Also
- [[Chi-Square Goodness-of-Fit Test]]
- [[Multinomial Distribution]]
- [[One-Way ANOVA]]
