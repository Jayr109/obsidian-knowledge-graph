---
title: "Source: Multifactor ANOVA — Two-Way ANOVA (Notes 5)"
type: source
tags: [ANOVA, two-way, interaction, experimental-design, randomized-block]
sources: [lecture-05-two-way-anova]
course: STAT 212
updated: 2026-07-04
---

Summary of the fifth set of course notes, *Multifactor ANOVA* (slides 141–170), covering **two-factor (two-way) ANOVA** and **experimental design**. Two factors A and B act on a response; the central question is whether they interact, and whether each has a main effect. Also introduces completely randomized vs. randomized block designs.

## Contents by slide

- **Slides 141–147 — Model & interaction.** [[Two-Way ANOVA]]: $X_{ijk} = \mu + \alpha_i + \beta_j + \gamma_{ij} + \epsilon_{ijk}$; additive (no-interaction) model $\mu_{ij} = \mu + \alpha_i + \beta_j$; interaction $\gamma_{ij}$; parallel-lines interaction plot.
- **Slides 148–151 — Sums of squares & test.** Cell/row/column/grand means; $SST = SSA + SSB + SSAB + SSE$; ANOVA table; F-tests $F_A, F_B, F_{AB}$; interpretation of $SSAB$.
- **Slides 152–153 — Testing strategy.** Test interaction **first**; if significant, don't test main effects — interpret via the means plot; else test main effects. R: `aov(Response ~ FactorA * FactorB)`.
- **Slides 154–159 — Example & Tukey.** Soybean example ($F_{AB}=4.17$, interaction present); Tukey for treatment means and for factor levels.
- **Slides 160–163 — Experimental design.** [[Experimental Design: CRD and Randomized Block]]: completely randomized design (CRD) vs. randomized block design (RBD); blocking reduces noise.
- **Slides 164–170 — RBD analysis.** RBD model $X_{ij} = \mu + \alpha_i + b_j + \epsilon_{ij}$; $SST = SSTr + SSB + SSE$; $F_{Tr} = MSTr/MSE$; caffeine/cyclists example.

## Key facts referenced
- Two-way (with interaction) df: A $= a-1$, B $= b-1$, AB $= (a-1)(b-1)$, Error $= ab(n-1)$.
- Interaction $\Leftrightarrow$ non-parallel lines in the means plot; no interaction $\Leftrightarrow$ all $\gamma_{ij}=0$.
- RBD df: treatments $= k-1$, blocks $= n-1$, error $= (k-1)(n-1)$.

## See Also
- [[Two-Way ANOVA]]
- [[Experimental Design: CRD and Randomized Block]]
- [[One-Way ANOVA]]
- [[STAT 212 Overview]]
