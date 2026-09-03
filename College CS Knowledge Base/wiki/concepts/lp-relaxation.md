---
title: "LP Relaxation"
type: concept
tags: [linear-programming, integer-programming, optimization, CSCE-411]
sources: [homework-7-solutions-sp26]
course: CSCE 411
updated: 2026-05-03
---

An LP relaxation is the [[Linear Programming|linear program]] obtained from an integer program (IP) by removing the integrality constraints. Solving the LP relaxation is always at least as easy as the IP, and sometimes the LP relaxation achieves the same optimal value — meaning the LP has an integral optimal solution even without requiring integrality. Whether this "tightness" holds depends on the structure of the constraint matrix.

## Integer Programs

An integer program (IP) is an LP with the additional constraint that all variables must take integer values:

```
maximize   cᵀx
subject to  Ax ≤ b
            x ≥ 0
            x ∈ ℤⁿ   ← this constraint makes it an IP
```

IPs can model many problems that LPs cannot (e.g., exact matching, set cover). However, solving IPs is NP-hard in general (IP is NP-complete). The best known algorithms for general IPs are exponential.

## LP Relaxation

The LP relaxation of the above IP simply removes `x ∈ ℤⁿ`:

```
maximize   cᵀx
subject to  Ax ≤ b
            x ≥ 0
```

Since the LP feasible region contains the IP feasible region (integers are a subset of reals), the LP optimum is always ≥ the IP optimum (for maximization). The LP relaxation is an **upper bound** on the IP.

## When the Relaxation Is Tight (Integral Optima)

The LP relaxation has an integral optimal solution whenever the constraint matrix A is **totally unimodular (TU)**: every square submatrix of A has determinant 0, +1, or −1. If A is TU and b is integral, then every LP vertex is integral, so the optimal LP solution is integral and equals the IP optimum.

**Key TU matrices**:
- Incidence matrix of a bipartite graph (rows = vertices, columns = edges)
- Network flow constraint matrices
- Interval matrices (consecutive-ones property)

## Example: Bipartite Matching

**IP formulation** (see [[Bipartite Matching]]):

```
maximize   Σ xₑ           (maximize matching size)
subject to  Σ_{e ∈ δ(v)} xₑ ≤ 1   for all v ∈ V   (at most one matched edge per vertex)
            xₑ ≥ 0, xₑ ∈ ℤ
```

**LP relaxation**: remove `xₑ ∈ ℤ`. The constraint matrix is the vertex-edge incidence matrix of a bipartite graph, which is TU. Therefore the LP relaxation always has an integral optimal solution — which corresponds to a valid maximum matching.

**Alternative proof via flow**: the LP is equivalent to maximum flow in a unit-capacity network. Since capacities are integral, [[Edmonds-Karp Algorithm]] finds an integral max flow → integral LP solution. This establishes integrality without invoking total unimodularity directly.

**Consequence** ([[König's Theorem]]): the LP dual of the matching LP is the fractional vertex cover LP. Both have integral optima on bipartite graphs, so by strong LP duality, max matching = min vertex cover.

## LP Relaxation as Approximation

When the LP relaxation does NOT have an integral optimum, it can still be useful:

- **LP-rounding**: solve the LP; round fractional values to integers; analyze the approximation ratio introduced by rounding.
- Example: rounding the LP relaxation of Vertex Cover gives a 2-approximation (round each yᵥ > 0 up to 1).

This approach is a major technique in [[Approximation Algorithms]].

## See Also

- [[Linear Programming]]
- [[König's Theorem]]
- [[Bipartite Matching]]
- [[Vertex Cover]]
- [[Approximation Algorithms]]
- [[Homework 7 Solutions — Spring 2026]]
- [[CSCE 411]]
