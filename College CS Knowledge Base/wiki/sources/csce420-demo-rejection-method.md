---
title: "CSCE 420 Demo — Rejection Method Animation"
type: source
tags: [csce420, demo, video, rejection-sampling, approximate-inference, monte-carlo, probability]
sources: []
course: CSCE 420
exam: final
updated: 2026-09-17
---

A 37-second silent screen recording of a matplotlib animation (`raw/CSCE420_demo_rejection-method.mp4`; the export gave no semester, so it is filed undated). It illustrates the **rejection method** — sample uniformly, keep only samples that satisfy a condition — the basic Monte-Carlo idea behind **rejection sampling** for approximate inference in [[Bayesian Networks]] (Deck 05). Final-exam scope only insofar as the belief-network material is; the demo itself is background.

## What the Animation Shows

- **Left panel**: random points drawn uniformly in the unit square, added frame by frame. Points with **x < 0.3** are drawn as blue dots (**accept**); points with x ≥ 0.3 as orange crosses (**reject**). The boundary is the vertical line x = 0.3.
- **Right panel**: a two-bar histogram of the running **Accept** and **Reject** fractions. As samples accumulate the bars settle at **≈ 0.3 / 0.7** — the acceptance rate converges to the probability of the region.
- Standard matplotlib animation controls beneath (once / loop / reflect).

## The Point

The fraction of accepted samples estimates the probability of the accept condition, with no formula needed — only the ability to generate samples and test them. For a belief network the same loop samples every variable from its CPT in topological order, **rejects** samples that contradict the evidence, and estimates P(query | evidence) from the survivors. The demo's 70% rejection rate is also the method's weakness: when the evidence is unlikely, almost every sample is thrown away — the motivation for the textbook's smarter samplers (likelihood weighting, MCMC). The deck itself stays with exact inference — see [[CSCE 420 Lecture 5 — Uncertainty and Probabilistic Reasoning]].

## See Also

- [[Bayesian Networks]]
- [[CSCE 420 Lecture 5 — Uncertainty and Probabilistic Reasoning]]
- [[CSCE 420 Spring 2026 — 03-16 Belief Network Inference]]
- [[CSCE 420]]
