---
title: "Experimental Design: CRD and Randomized Block"
type: concept
tags: [experimental-design, CRD, randomized-block, blocking, ANOVA]
sources: [lecture-05-two-way-anova]
course: STAT 212
updated: 2026-07-04
---

Design of experiment refers to how treatments are assigned to experimental units. The two designs covered are the completely randomized design (CRD) and the randomized block design (RBD). Blocking reduces noise from unit-to-unit differences, making treatment differences easier to detect.

## Completely randomized design (CRD)

With `N` units and `t` treatments (administer treatment `i` to $n_i$ units, $\sum n_i = N$), randomly assign units to treatments. This is the design implicitly assumed in [[One-Way ANOVA]] ($t = k$) and [[Two-Way ANOVA]] ($t = ab$, $N = abn$).

## Randomized block design (RBD)

Differences between experimental units add variance ("noise") that masks treatment differences. In an RBD, **similar units are grouped into blocks**, and all treatments are randomly assigned to units *within* each block.

- *Twins example:* 10 pairs of identical twins; within each pair, coin-flip which twin gets the treatment vs. placebo. Each pair is a **block**. This beats the CRD (20 people split at random) because it controls for between-unit variation.
- **Motivation:** applying treatments to similar units removes block-to-block variation from the error, making treatment effects easier to detect.

## RBD model and analysis

For treatment `i` in block `j` ($k$ treatments, $n$ blocks):

$$X_{ij} = \mu + \alpha_i + b_j + \epsilon_{ij},$$

where $\alpha_i$ is the treatment effect and $b_j$ the block effect. Sums of squares:

$$SSTr = n\sum_i(\bar X_{i\cdot}-\bar X_{\cdots})^2,\quad SSB = k\sum_j(\bar X_{\cdot j}-\bar X_{\cdots})^2,\quad SSE = SST - SSTr - SSB.$$

| Source | df | F |
|--------|----|---|
| Treatments | $k-1$ | $F_{Tr} = MSTr/MSE$ |
| Blocks | $n-1$ | $F_B = MSB/MSE$ |
| Error | $(k-1)(n-1)$ | |
| Total | $kn-1$ | |

Test $H_0: \alpha_1 = \cdots = \alpha_k$ with $F_{Tr} \ge F_{k-1,\,(k-1)(n-1)}$. The block effect $F_B$ can be examined but is not of primary interest. If treatments differ, use Tukey: $|\bar X_{i\cdot}-\bar X_{\ell\cdot}| \ge Q_{\alpha,k,(k-1)(n-1)}\sqrt{MSE/n}$.

- Example (caffeine on cyclist endurance): treatments = 4 caffeine doses, blocks = 9 cyclists; $F_{Tr}=5.92 > F_{3,24;0.01}=4.72$ ⇒ doses differ. Tukey: no caffeine gives lower mean endurance than any of doses 5/9/13, which don't differ among themselves.

## In R
```r
fit = aov(Response ~ Treatment + Block)
anova(fit)
TukeyHSD(fit, "Treatment")
```

## See Also
- [[Two-Way ANOVA]]
- [[One-Way ANOVA]]
- [[Multiple Comparisons and Tukey's Procedure]]
