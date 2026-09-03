---
title: "König's Theorem"
type: concept
tags: [bipartite-matching, vertex-cover, LP-duality, graphs, CSCE-411]
sources: [homework-7-solutions-sp26]
course: CSCE 411
updated: 2026-05-03
---

König's Theorem states that in any bipartite graph, the size of a maximum matching equals the size of a minimum vertex cover. This is a deep structural result connecting two apparently different optimization problems, and it follows cleanly from LP duality applied to the bipartite matching LP.

## Statement

> **Theorem (König, 1931)**: In every bipartite graph G = (V, E), the maximum matching size equals the minimum vertex cover size.

Symbolically: max |M| = min |C|.

This is **false** for general (non-bipartite) graphs — in a triangle K₃, the maximum matching has size 1 but the minimum vertex cover has size 2.

## Proof via LP Duality

**(1) Formulate bipartite matching as an IP**:

```
maximize   Σ_{e ∈ E} xₑ
subject to  Σ_{e ∈ δ({v})} xₑ ≤ 1   for all v ∈ V
            xₑ ≥ 0, xₑ ∈ ℤ          for all e ∈ E
```

**(2) LP relaxation has an integral optimum**: remove the integrality constraint. The resulting LP is equivalent to maximum flow in a unit-capacity network G′ (direct edges X→Y, add source s → X and Y → sink t with capacity 1). Since capacities are integral, [[Edmonds-Karp Algorithm]] finds an integral maximum flow. This flow is an integral optimal LP solution. See [[LP Relaxation]].

**(3) Compute the dual LP**: one dual variable yᵥ per primal constraint (per vertex), one dual constraint per primal variable (per edge):

```
minimize   Σ_{v ∈ V} yᵥ
subject to  yᵤ + yᵥ ≥ 1   for all {u,v} ∈ E
            yᵥ ≥ 0          for all v ∈ V
```

This is exactly the LP relaxation of **Minimum Vertex Cover** (yᵥ = 1 means v is in the cover).

**(4) The vertex cover LP relaxation is also integral on bipartite graphs**: the constraint matrix of the bipartite matching LP (equivalently, the incidence matrix of a bipartite graph) is **totally unimodular** — every square submatrix has determinant 0, +1, or −1. Therefore every LP vertex is integral, and the LP optimum equals the IP optimum.

**(5) Conclude via strong LP duality**: primal LP optimum (= max matching by step 2) = dual LP optimum (= min vertex cover by step 4). ✓

## Corollaries

- **Hall's Theorem**: a bipartite graph G = (X ∪ Y, E) has a perfect matching from X to Y iff for every S ⊆ X, |N(S)| ≥ |S|. (Follows from König's via the max-flow min-cut theorem.)
- Minimum vertex cover in bipartite graphs is solvable in polynomial time (reduce to max matching).
- Maximum independent set in bipartite graphs is solvable in polynomial time: |IS| = |V| − |VC| = |V| − max matching.

## Contrast with General Graphs

On general graphs:
- Max matching ≠ min vertex cover in general.
- The LP relaxation of vertex cover may have fractional optimal solutions (e.g., the triangle K₃ has LP optimum 3/2 but IP optimum 2).
- The LP-based 2-approximation for Vertex Cover applies to general graphs via a different argument — see [[Vertex Cover]].

## See Also

- [[Bipartite Matching]]
- [[Vertex Cover]]
- [[Linear Programming]]
- [[LP Relaxation]]
- [[Maximum Flow]]
- [[Edmonds-Karp Algorithm]]
- [[Homework 7 Solutions — Spring 2026]]
- [[CSCE 411]]
