# STAT 212 Knowledge Base — Operation Log

Append-only. Newest entries first.

---

## [2026-08-01] derive | Sign test homework — median home-owner tax increase (n=22, c=$300)

Four-part homework worked from [[Sign Test]]. Data: 22 tax increases, 16 below $300, 6 above, no ties, sample median 250.5 (right-skewed). Statistic Y = #{Xi > 300} = 6, Y ~ Bin(22, 0.5) under H0, E[Y] = 11. (1) Two-sided: P = 2·P(Y≤6) = 0.05248, fail to reject at 0.05. (2) Lower-tailed (claim becomes Ha): P = P(Y≤6) = 0.02624, reject. (3) Concept illustrated: one-tailed p is exactly half the two-tailed p; more power in the chosen direction but the direction must be fixed before seeing data (else true Type I error doubles — HARKing); the 0.05 cutoff is a sharp line through continuous evidence. (4) Normal approximation: p-hat = 6/22, Z = -2.1320, P = 0.0165 — anti-conservative vs. the exact 0.0262 at n=22; continuity correction gives Z = -1.9188, P = 0.0275. Plain-text (no LaTeX) format per student request. Offered to add an exact-binomial p-value section to the [[Sign Test]] page and file a method page on exact vs. normal.

## [2026-07-05] derive | Theory Assignment 2 — slope decomposition, E/Var of slope, SSR, ρ̂²=R²

Produced four step-tagged derivations for handwritten homework: (1) β̂₁ = β₁ + Σ(xᵢ−x̄)εᵢ/Sx²; (2) E(β̂₁)=β₁ and Var(β̂₁)=σ²/Sx² under independent N(0,σ²) errors; (3) SSR = β̂₁²Sx² via β̂₀ = ȳ−β̂₁x̄; (4) ρ̂² = R̂² via SSE = SST−β̂₁²Sx². Cited prior-assignment results R1–R4 (now filed as wiki pages) and [[Unbiasedness of the Slope Estimator]], [[Rules of Expectation and Variance]], [[ANOVA Decomposition of SST]], [[Correlation Coefficient]]. Plain-text (no LaTeX) format per student request. Offered to file (1)–(4) as derivation pages.

## [2026-07-05] derive | Theory assignment results R1, R3, R4 filed

Filed three theory-homework results as linked derivation pages (using the two-column justification-tag format): `sum-of-deviations-equals-zero` (Problem 1, $\sum(x_i-\bar x)=0$), `slope-estimator-deviation-form` (Problem 3, the two $\hat\beta_1$ forms agree), and `slope-as-correlation-times-sd-ratio` (Problem 4, $\hat\beta_1=\hat\rho\,\hat\sigma_Y/\hat\sigma_X$). Problem 2 (solving the normal equations) is the existing `least-squares-estimators` page. Added back-links from least-squares-estimators, correlation-coefficient, and rules-of-expectation-and-variance. Updated `index.md`. Purpose: student is allowed to cite these results on the next theory assignment.

## [2026-07-04] lint | Full knowledge base

Ran LINT over all 44 wiki pages. Findings: (1) fixed 1 dangling link — `[[More General Regression]]` in `residual-diagnostic-plots.md` retargeted to `[[Variable Transformations]]`. (2) All 44 pages catalogued in `index.md`; no dangling links in wiki or index after fix. (3) All 6 derivation pages have a justification tag (MS/BD/Move sum/Zeros out/Rule of Expectations/etc.) on every step row — 40 steps total, all tagged. (4) The 7 `sources/` pages show as graph "orphans" (nothing wiki-links to them) — expected by design: they are catalogued in `index.md` and link outward to the concepts they cover. No action needed.

## [2026-07-04] ingest | Notes 7 — Distribution-Free Procedures

Ingested `raw/7 - Nonparametric Methods.pdf` (slides 219–239). Created source page `lecture-07-nonparametric-methods` plus 3 concept pages: sign test (median), signed-rank test (Wilcoxon, symmetric), Kruskal-Wallis test (nonparametric one-way ANOVA). Updated `index.md`. **All 7 source PDFs now ingested.**

## [2026-07-04] ingest | Notes 6 — Categorical Data Analysis

Ingested `raw/6 - Categorical Data.pdf` (slides 172–217). Created source page `lecture-06-categorical-data` plus 3 concept pages: multinomial distribution; chi-square goodness-of-fit test (specified & estimated-parameter cases, incl. Poisson/Normality checks); contingency tables & chi-square (homogeneity of proportions and independence). Updated `index.md`.

## [2026-07-04] ingest | Notes 5 — Multifactor ANOVA (Two-Way ANOVA)

Ingested `raw/5 - Two Way ANOVA.pdf` (slides 141–170). Created source page `lecture-05-two-way-anova` plus 2 concept pages: two-way ANOVA (interaction, main effects, SST=SSA+SSB+SSAB+SSE, testing strategy) and experimental design (CRD vs. randomized block design, RBD model & analysis). Updated `index.md`.

## [2026-07-04] ingest | Notes 4 — Analysis of Variance (One-Way ANOVA)

Ingested `raw/4 - One Way ANOVA.pdf` (slides 114–139). Created source page `lecture-04-one-way-anova` plus 3 wiki pages: concept (one-way ANOVA model, sums of squares, ANOVA table, F-test); derivation (expected mean squares — E(MSE)=σ² and E(MSTr)); method (multiple comparisons & Tukey's procedure, EWER). Updated `index.md`.

## [2026-07-04] ingest | Notes 3 — Multiple Regression

Ingested `raw/3 - Multiple Linear Regression.pdf` (slides 81–112). Created source page `lecture-03-multiple-linear-regression` plus 5 wiki pages: concepts (multiple linear regression, influential observations & Cook's D); theorems (F-test for model utility, reduction method / partial F-test). Reuses the matrix least-squares and inference machinery from Notes 2. Updated `index.md`.

## [2026-07-04] ingest | Notes 2 — More General Regression Analyses

Ingested `raw/2 - More General Regression.pdf` (slides 46–79). Created source page `lecture-02-more-general-regression` plus 6 wiki pages: concepts (polynomial regression, model selection criteria, variable transformations); derivation (polynomial normal equations in matrix form); theorem (inference for polynomial regression). Variable-transformations page ties directly to the windmill (reciprocal) and bacteria (log) homeworks. Updated `index.md`.

## [2026-07-04] ingest | Notes 1 — Simple Linear Regression and Correlation

Ingested `raw/1 - Simple Linear Regression.pdf` (44 slides). Created source page `lecture-01-simple-linear-regression` plus 16 wiki pages: overview, course, person (Galton); concepts (SLR model, least squares, R², residuals/diagnostics, correlation); derivations (least-squares estimators, ANOVA decomposition of SST, unbiasedness of slope, prediction error variance); theorems (sampling distribution of slope, inference for mean & prediction, rules of expectation/variance); methods (residual diagnostic plots, CIs/PIs in R). Updated `index.md`. Covers the machinery behind the earlier windmill/bacteria homework.

## [2026-07-04] init | Knowledge base created

Created `College STAT212 Knowledge Base` with schema in `CLAUDE.md`, empty `index.md`, `raw/` (drop sources here), and `wiki/` skeleton (concepts, derivations, theorems, methods, courses, people, sources). Ready for first ingest.
