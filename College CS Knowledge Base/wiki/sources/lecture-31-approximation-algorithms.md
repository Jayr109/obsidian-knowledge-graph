---
title: "Lecture 31 — Approximation Algorithms"
type: source
tags: [CSCE-411, approximation, vertex-cover, max-cut, FPTAS, lecture]
sources: []
course: CSCE 411
updated: 2026-04-27
---

CSCE 411 lecture by Calvin Beideman (26 slides). The "what next" after NP-completeness: how to build polynomial-time algorithms that produce *near-optimal* solutions when exact polynomial-time algorithms are impossible. Defines the approximation ratio, approximation schemes, and FPTAS, then walks through two canonical examples: a 1/2-approximation for Max-Cut and a 2-approximation for Vertex Cover (with a striking demonstration that the natural greedy *fails* badly).

## Slides Index

| # | Title | Notes |
|---|-------|-------|
| 1 | Title — Approximation Algorithms | Beideman |
| 2 | Final Exam | Same logistics as Lecture 29; review sheet posted today |
| 3 | Learning Objectives | Define approximation ratio, scheme, FPTAS; design and analyze approximations |
| 4 | How to deal with NP-Hardness | 3 axes of relaxation: time, inputs, optimality |
| 5 | Example: Vertex Cover | (visual) |
| 6 | Faster exponential-time Algorithms | (visual) |
| 7 | Restricted Classes of Graphs | VC poly-time on trees (DP) and bipartite (LP) |
| 8 | Approximate Vertex Cover | Setup: 2-approximation exists |
| 9 | Optimization Problems | NP is decision; optimization is the natural setting for approximation |
| 10 | Approximation Algorithms | Definition of approximation ratio (visual) |
| 11 | Approximation Schemes | PTAS, FPTAS (visual) |
| 12 | Max-Cut | (visual — definition) |
| 13 | Approximation Algorithm for Max-Cut | (visual — pseudocode) |
| 14 | Greedy Max-Cut Example | (visual) |
| 15 | Runtime for Greedy Max-Cut | (visual) |
| 16 | Approximation Ratio for Greedy Max-Cut | 1/2-approximation |
| 17 | Vertex Cover | (visual — definition) |
| 18 | Greedy Algorithm for Vertex Cover | Repeatedly pick highest-degree vertex |
| 19 | Greedy Vertex-Cover Example | (visual) |
| 20 | Bad Examples for Greedy? | GreedyVertexCover is not a 1.33-approximation |
| 21 | Worse Examples for Greedy? | Not a 1.74-approximation (graph from Ryan O'Donnell) |
| 22 | Even Worse Examples | Not 2.08, not 3, not 10, not 999,999 — no constant ratio |
| 23 | An approximation algorithm for Vertex-Cover | The matching-based 2-approximation |
| 24 | VertexCoverApprox Example | (visual) |
| 25 | Runtime for VertexCoverApprox | (visual) |
| 26 | Approximation Ratio for VertexCoverApprox | 2-approximation (visual proof) |

Many slides are visual-only (graph constructions, gadget diagrams, pseudocode). Text extraction captured prose explanations and slide titles.

## Key Takeaways

### Three Ways to Deal with NP-Hardness

If P ≠ NP, no polynomial-time algorithm finds the *best* solution for *every* input of an NP-hard problem. We can relax any one of these three:

1. **Time** — accept exponential time; design *faster* exponential algorithms (e.g., 2^(n/2) instead of 2ⁿ). Practical for small inputs.
2. **Inputs** — solve only special cases. Vertex Cover is poly-time on trees ([[Maximum Weight Independent Set]]-style DP) and on bipartite graphs (via [[Linear Programming]]).
3. **Optimality** — output a "good enough" solution. This is the **approximation algorithm** strategy.

### Decision vs. Optimization

NP is technically a class of *decision* problems (yes/no). Approximating yes/no doesn't make sense. But every NP problem has a natural *optimization* counterpart:

- Vertex Cover (decision): is there a VC of size ≤ k?
- Min-Vertex-Cover (optimization): find the smallest VC.
- Max-Cut (optimization): find a cut with the maximum number of crossing edges.

Approximation algorithms target these optimization variants.

### Approximation Ratio

For a minimization problem, an algorithm A is an **α-approximation** (α ≥ 1) if for every input I:

$$\frac{A(I)}{\text{OPT}(I)} \le \alpha$$

For maximization, the ratio is flipped (or stated as 1/α): A(I) / OPT(I) ≥ 1/α.

Smaller α (closer to 1) is better. A 2-approximation guarantees output is at most twice optimal; a 1.5-approximation is tighter.

### Approximation Schemes

A **PTAS** (polynomial-time approximation scheme) is a family of algorithms parameterized by ε > 0, where each is a (1+ε)-approximation running in poly(n) time (with constants possibly depending on ε).

An **FPTAS** (fully polynomial-time approximation scheme) requires the runtime to also be polynomial in 1/ε. FPTAS is the strongest standard guarantee: arbitrarily good approximation in time polynomial in input size and the approximation parameter.

### Greedy Max-Cut: 1/2-Approximation

**Algorithm**: place each vertex on whichever side of the cut maximizes the number of crossing edges (ties broken arbitrarily). One vertex at a time.

**Guarantee**: at least m/2 edges cross — a **1/2-approximation** of optimal (since OPT ≤ m trivially). Equivalently, a 2-approximation in the minimization sense, but Max-Cut is a maximization problem so we say "1/2-approximation."

**Why it works**: at each step, the chosen side has at least as many incident crossing edges as the other side, so at least half of each vertex's edges to *already-placed* vertices end up crossing. Summed, ≥ m/2 edges cross.

### Greedy Vertex Cover: Arbitrarily Bad

**Natural greedy**: repeatedly pick the highest-degree vertex, remove it and its incident edges, repeat.

**Striking result**: this greedy is **not a constant-factor approximation**. Beideman walked through graphs showing greedy is not a 1.33, 1.74, 2.08, 3, 10, or even 999,999-approximation. For any constant α, there exists a graph where greedy outputs a cover α times the optimum.

The construction (due to Ryan O'Donnell): a bipartite graph where one side has high-degree "trap" vertices that look attractive to greedy but force it to also cover the low-degree side. By scaling, the ratio grows without bound.

**Lesson**: intuitive greedy choices on hard problems may have *no constant-factor guarantee at all*. A naïve approximation can be unboundedly worse than optimal.

### VertexCoverApprox: Matching-Based 2-Approximation

**Algorithm**:
```
C ← ∅
while edges remain:
    pick any remaining edge (u, v)
    add both u and v to C
    remove all edges incident to u or v
return C
```

**Equivalently**: build a *maximal matching* M (greedily pick disjoint edges); return the set of all matched endpoints.

**Why it's a 2-approximation**:
- Every edge in M must be covered by OPT → OPT ≥ |M|.
- C contains 2|M| vertices.
- ⇒ |C| = 2|M| ≤ 2·OPT.

**Runtime**: O(n + m) — each edge is examined once.

**Note the contrast with Greedy**: VertexCoverApprox picks *both* endpoints of an arbitrary edge — the "wasteful"-looking move — and gets a tight 2-approximation. Greedy picks the seemingly-best vertex and gets nothing.

This is a classic teaching example: **the right algorithm for approximation often does not look like the natural greedy.**

## Cross-References

- Builds on: [[Lecture 28 — NP-Completeness]], [[Lecture 29 — NP-Hardness Proofs]] (motivation: VC is NP-complete)
- Connects to: [[Maximum Weight Independent Set]] (tree DP for VC), [[Linear Programming]] (LP for bipartite VC)
- Continues into: open research (PTAS, hardness of approximation)

## See Also

- [[Approximation Algorithms]]
- [[Vertex Cover]]
- [[NP Completeness]]
- [[Lecture 29 — NP-Hardness Proofs]]
- [[Maximum Weight Independent Set]]
- [[Linear Programming]]
- [[CSCE 411]]
