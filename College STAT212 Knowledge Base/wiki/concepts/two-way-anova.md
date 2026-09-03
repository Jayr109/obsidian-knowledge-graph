---
title: "Two-Way ANOVA"
type: concept
tags: [ANOVA, two-way, interaction, main-effects, F-test]
sources: [lecture-05-two-way-anova]
course: STAT 212
updated: 2026-07-04
---

Two-way (two-factor) ANOVA assesses the effects of **two** factors A and B on a response, and — crucially — whether they **interact**. It extends [[One-Way ANOVA]] with an interaction term and a four-way sums-of-squares decomposition.

## The model

With `a` levels of A, `b` levels of B, and `n` replicates per cell:

$$X_{ijk} = \mu_{ij} + \epsilon_{ijk} = \mu + \alpha_i + \beta_j + \gamma_{ij} + \epsilon_{ijk},$$

$i=1,\dots,a$; $j=1,\dots,b$; $k=1,\dots,n$; $\epsilon_{ijk}\sim N(0,\sigma^2)$ iid. Here $\mu$ = grand mean, $\alpha_i$ = main effect of A, $\beta_j$ = main effect of B, and $\gamma_{ij} = \mu_{ij} - (\mu + \alpha_i + \beta_j)$ = **interaction**.

## Interaction

- **Additive (no-interaction) model:** $\mu_{ij} = \mu + \alpha_i + \beta_j$ (only $a+b-1$ mean parameters vs. $ab$ in general). No interaction $\iff$ all $\gamma_{ij} = 0$.
- **Meaning:** with interaction, "the effect of Factor A on the response depends on the level of Factor B." In the additive case $\mu_{ij} - \mu_{\ell j} = \alpha_i - \alpha_\ell$ doesn't depend on `j`.
- **Interaction plot:** plot cell means vs. levels of B, one line per level of A. **Parallel lines ⇒ no interaction**; non-parallel (crossing) lines ⇒ interaction.

## Sums of squares and ANOVA table

Using cell/row/column/grand means $\bar X_{ij\cdot}, \bar X_{i\cdot\cdot}, \bar X_{\cdot j\cdot}, \bar X_{\cdots}$:

$$SST = SSA + SSB + SSAB + SSE,$$
with $SSA = bn\sum_i(\bar X_{i\cdot\cdot}-\bar X_{\cdots})^2$, $SSB = an\sum_j(\bar X_{\cdot j\cdot}-\bar X_{\cdots})^2$, $SSAB = n\sum_{i,j}(\bar X_{ij\cdot}-\bar X_{i\cdot\cdot}-\bar X_{\cdot j\cdot}+\bar X_{\cdots})^2$, $SSE = \sum_{i,j,k}(X_{ijk}-\bar X_{ij\cdot})^2$.

| Source | df | MS | F |
|--------|----|----|---|
| Factor A | $a-1$ | $MSA = SSA/(a-1)$ | $F_A = MSA/MSE$ |
| Factor B | $b-1$ | $MSB$ | $F_B = MSB/MSE$ |
| Interaction AB | $(a-1)(b-1)$ | $MSAB$ | $F_{AB} = MSAB/MSE$ |
| Error | $ab(n-1)$ | $MSE$ | |
| Total | $abn-1$ | | |

## Testing strategy (order matters)

1. **Test interaction first**: $H_{0,AB}: \gamma_{ij}=0$ for all $i,j$ via $F_{AB} \sim F_{(a-1)(b-1),\,ab(n-1)}$. A large $SSAB$ signals interaction.
2. **If interaction is significant:** do **not** test the main-effect hypotheses ($H_{0A}, H_{0B}$) — they're misleading. Instead explain the interaction from the means plot and compare the $ab$ **treatment means** with Tukey: $Q_{\alpha,ab,ab(n-1)}\sqrt{MSE/n}$.
3. **If interaction is not significant:** test $H_{0A}: \alpha_i=0$ ($F_A \ge F_{a-1,\,ab(n-1)}$) and $H_{0B}: \beta_j=0$ ($F_B \ge F_{b-1,\,ab(n-1)}$). If a main effect is significant, use Tukey on that factor's levels, e.g. $|\bar X_{i\cdot\cdot}-\bar X_{\ell\cdot\cdot}| \ge Q_{\alpha,a,ab(n-1)}\sqrt{MSE/(bn)}$.

## In R
```r
fit = aov(Response ~ FactorA * FactorB, data = Data)
anova(fit)
TukeyHSD(fit, "FactorA")   # or the interaction; also plot(TukeyHSD(...))
```

## See Also
- [[One-Way ANOVA]]
- [[Multiple Comparisons and Tukey's Procedure]]
- [[Experimental Design: CRD and Randomized Block]]
