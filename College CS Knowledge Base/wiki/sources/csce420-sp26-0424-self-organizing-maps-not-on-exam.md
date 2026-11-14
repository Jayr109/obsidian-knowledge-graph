---
title: "CSCE 420 Spring 2026 — 04-24 Self-Organizing Maps (Not on Exam)"
type: source
tags: [csce420, lecture-recording, spring-2026, self-organizing-maps, som, kohonen, unsupervised-learning, redundancy, pca, t-sne, dimensionality-reduction, best-matching-unit, neighborhood-function, topology-preservation, density-mapping, traveling-salesman, space-filling-curve]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-04-24
deck: slide06
exam: excluded
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. With technical content finished early, he returned to the **Self-Organizing Maps** section of the ML deck that had been skipped on 04-06. Unsupervised learning framing, PCA and t-SNE, Kohonen's algorithm with the update rule worked geometrically, and an extended run of the classic Java SOM applet (1-D, 2-D, 3-D, space-filling). Slides 06 SOM section.

> **NOT ON THE FINAL.** He stated this twice (04-15 and 04-22): *"I won't put that on the exam, because I wasn't expecting to cover it."* Filed for completeness; do not pull from this page when studying for the final. See [[CSCE 420 Final Review]].

## Unsupervised Learning

No target, no teacher signal. The network must discover **patterns, features, regularities, correlations, categories** in the input and encode them in its output; the connections *"must display some degree of self-organization."*

Works only when there is **redundancy**. Random (x, y, z) → a structureless box of points. Channel view: two channels always carrying the same bit → **capacity 2, information content 1**. Uses: **familiarity** (how similar is this input to past inputs), **PCA** (rotate coordinates to maximize projected variance — even 100-d data can be read off its top two directions), **dimensionality reduction**, **clustering** (how many clusters, what prototype), **encoding**, **feature mapping**.

**t-SNE on MNIST** (he had ChatGPT generate it): 32×32 = 1024-d images projected to 2-D; without labels you could still see the clusters. Confusable neighbours share pixels: **2↔0, 6↔0, 8↔2, 9↔7**.

## Kohonen's SOM (1982)

A **grid** of units — 1-D chain, 2-D lattice (4 or 8 neighbours), 3-D — where the lattice defines **neighbourhood**. Each unit j holds a **weight / reference vector w_j** with the **same dimension as the input**, so it *"lives in the input space."*

**Algorithm**: sample input x (no target) → compare with every w_j → **best-matching unit** i = argmin ‖x − w_j‖ (Euclidean) → update **all** units:

**w_j ← w_j + α · Λ(j, i) · (x − w_j)**

Worked geometrically with a 3×3 grid and 2-D input: plot each w_j as a point in input space and connect grid neighbours → a "strange-looking graph." Then:
- α = 1, Λ = 1 → **every** weight jumps exactly onto x — *"totally useless."*
- α = 0.5, Λ = 1 → every weight moves **halfway** toward x; α = 0.1 → a tenth.
- **Neighbourhood function** Λ: **1.0 at the BMU**, high for grid-neighbours (they move most of the way), near **0** far away (barely move). This is what makes grid-neighbours grow similar. Defined as a **Gaussian** of the grid-coordinate difference r = (r₁, r₂) between unit j and the BMU; its σ is the **neighbourhood radius**.

**Schedule**: start with a **large radius** and **high α**, shrink both gradually.

**Three properties**: **approximation of the input space**; **topology preservation** (nearby units ↔ nearby inputs); **density mapping** (more units where inputs are dense).

## Applet Demos (Java SOM applet, resurrected)

Plotting each unit at its weight vector with grid edges drawn; randomly initialized weights make edges criss-cross the whole space.

| Setup | What happened |
|---|---|
| 9×9 grid, 50 inputs, radius 5 | everything collapses toward the centre, then units are "jogged" toward whichever input was just sampled; ends with units sitting on inputs (more units than samples) |
| 9×9, 300 inputs | grid spreads to **cover the input distribution**; dense regions attract more units — density mapping visible |
| **1-D chain of 100, 10 inputs** | the chain threads through the points — *"a pretty good solution to the traveling salesman problem, even though I don't think it's optimal"*; late in training only ~5 units near the BMU move |
| 1-D chain of 600, 1000 inputs (C-shape) | fewer units than inputs → chain becomes a **space-filling curve**, bulging into under-represented regions like a fractal |
| 2-D grid, 10 points in 3-D | grid reaches the points; intermediate units represent intermediate space |
| 2-D sheet, 500 points in 3-D | *"like crumpling a piece of paper to fill 3-D space"* — surfaces fold in fractally |
| flat "pizza box" | the sheet learns the thin height dimension too — appears "pillowy" from the side |

**Resurrection story**: the applet needed Java ≤ 8; podium machines had Java 21. He had **Codex** write a Java harness and then **patch the compiled `.class` bytecode**, replacing every deprecated `Thread.stop` with `Thread.interrupt` — repo linked in the lecture resources. Continues 04-27 with SOM error measures.

## See Also

- [[CSCE 420 Spring 2026 — 04-22 LLMs, Diffusion, Deep Learning Wrap-Up]]
- [[CSCE 420 Spring 2026 — 04-27 SOM Evaluation, AI Ethics (Not on Exam)]]
- [[CSCE 420 Spring 2026 — 04-06 Demos, Autoencoders, SRN, Genetic Algorithms]]
- [[CSCE 420 Lecture 6 — Machine Learning]]
- [[CSCE 420]]
