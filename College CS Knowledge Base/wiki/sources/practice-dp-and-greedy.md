---
title: "Practice — DP and Greedy"
type: source
tags: [csce411, practice, dynamic-programming, greedy, vertex-cover, graph-coloring]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Practice — DP and Greedy

**Source file:** `raw/CSCE_411_DP_and_Greedy_Practice_Solutions.pdf`
**Course:** CSCE 411, Spring 2026
**Topics:** Dynamic Programming on trees, Greedy graph coloring

## Problem 1: Minimum Vertex Cover in Trees

**Problem:** Given a weighted tree T, find a minimum weight vertex cover (a subset S of vertices such that every edge has at least one endpoint in S).

**DP approach (O(n)):**

Define two subproblems per vertex u:
- VC_in(u) = min weight vertex cover of the subtree rooted at u, **where u is included** in the cover
- VC_out(u) = min weight vertex cover of the subtree rooted at u, **where u is excluded** from the cover

**Recurrences:**

For a leaf u:
- VC_in(u) = w(u)
- VC_out(u) = 0

For an internal vertex u with children c₁, c₂, ..., cₖ:
- **Include u:** Each child can be included or excluded (since the edge (u, cᵢ) is covered by u)
  - VC_in(u) = w(u) + Σᵢ min(VC_in(cᵢ), VC_out(cᵢ))
- **Exclude u:** Each child **must** be included (to cover the edge (u, cᵢ))
  - VC_out(u) = Σᵢ VC_in(cᵢ)

**Answer:** min(VC_in(root), VC_out(root))

**Runtime:** Each vertex processed once → O(n).

## Problem 2: Graph (d+1)-Coloring via Greedy

**Problem:** Given a graph G where every vertex has degree at most d, show a greedy algorithm produces a valid (d+1)-coloring.

**Algorithm:**
1. Order vertices arbitrarily: v₁, v₂, ..., vₙ
2. For each vertex vᵢ in order: assign the smallest color in {1, 2, ..., d+1} not already used by any of vᵢ's neighbors

**Correctness:**
When processing vᵢ, at most d neighbors have already been colored (those processed before vᵢ). The palette {1, ..., d+1} has d+1 colors. By pigeonhole, at least one color is not used by any neighbor — so the greedy assignment always succeeds.

**Note:** This is not necessarily optimal (the chromatic number may be less than d+1), but it guarantees a valid coloring exists using d+1 colors for any graph with max degree d.

## See Also

- [[Dynamic Programming]]
- [[Greedy Algorithms]]
- [[Maximum Weight Independent Set]]
- [[CSCE 411]]
