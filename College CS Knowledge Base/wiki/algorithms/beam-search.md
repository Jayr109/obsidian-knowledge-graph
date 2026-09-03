---
title: "Beam Search"
type: algorithm
tags: [csce420, beam-search, informed-search, branching-factor]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Beam search is [[Best-First Search]] with a fixed limited branching factor: expand only the best $n$ nodes by evaluation-function value and discard the rest. The number $n$ is the **width of the beam**.

## The Tradeoff

Capping the frontier bounds memory to $O(n)$ regardless of depth — but discarding nodes makes the search **incomplete**, since the solution path may run through a node that fell outside the beam.

Beam search is essentially a middle point between [[Greedy Best-First Search]] ($n = 1$, keep only the best) and full best-first ($n = \infty$, keep everything).

## Where It Is Used

- Domains with **continuous time functions**, such as speech recognition
- Domains with a **huge branching factor**, where retaining the full frontier is impossible

## Relation to Hill Climbing

The lecture lists "keep $n$ best nodes (beam search)" as one of the standard remedies for [[Hill Climbing]]'s local-maximum problem. Running several candidates in parallel makes it less likely that all of them are stuck simultaneously — a weaker but cheaper version of random restart.

## See Also

- [[Best-First Search]]
- [[Hill Climbing]]
- [[Greedy Best-First Search]]
- [[Local Search]]
- [[CSCE 420]]
