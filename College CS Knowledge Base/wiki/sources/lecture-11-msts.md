---
title: "Lecture 11 — Minimum Spanning Trees"
type: source
tags: [mst, prim, kruskal, union-find, graph-layering, trees]
sources: [lecture-11-msts]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 11 — Minimum Spanning Trees

CSCE 411, Calvin Beideman, 38 slides.

## Graph Layering

Create k+1 copies of the graph to handle constrained path problems (e.g., "at most k toll/red edges"). Each layer represents using one more constrained edge. Edges that cross layers correspond to using one toll edge; edges within a layer are free.

Converts a constrained shortest-path problem into standard BFS/Dijkstra on the layered graph.

**Runtime**: O(k(m + n))

---

## Trees (Review)

A **tree** is a connected acyclic graph with exactly n−1 edges. Any two of the following three properties imply the third:

1. Connected
2. Acyclic
3. Exactly n−1 edges

Every connected graph has a spanning tree (repeatedly remove edges that are part of a cycle).

---

## Minimum Spanning Trees

An **MST** is a spanning tree of a weighted undirected connected graph with minimum total edge weight.

**Applications**:
- Borůvka (1926): designing an electrical grid
- Circuit design: minimize wire length
- TSP approximation: MST-based tour is ≤ 2× optimal for metric TSP

**Uniqueness**: the MST is unique if all edge weights are distinct.

---

## Cuts and the Light Edge Property

A **cut** (S, T) is a partition of V. An edge **crosses** the cut if one endpoint is in S and the other is in T.

**Theorem (Light Edge Property)**: For every cut (S, T) of G, the lightest edge crossing the cut is part of some MST.

This theorem is the foundation for all MST algorithms — both Prim-Jarník and Kruskal's greedily add the lightest safe edge, justified by this property.

---

## Prim-Jarník Algorithm

Start with one vertex; repeatedly add the lightest edge connecting the current tree to a new vertex.

- Named "Prim's" but discovered first by Vojtěch Jarník (1930); Prim published in 1957.
- **Runtime**: O((n + m) log n) with binary heap; O(m + n log n) with Fibonacci heap

---

## Kruskal's Algorithm

Sort all edges by weight; add the lightest edge that doesn't create a cycle. Uses the **Disjoint Sets** (Union-Find) ADT.

- **Runtime**: O(m log m + m·α(n)) ≈ O(m log m)

---

## Disjoint Sets ADT

Supports three operations: `make_set`, `find`, `union`.

| Implementation | find | union | Notes |
|---|---|---|---|
| Basic linked list | O(1) | O(n) worst | Worst case O(n²) total |
| Union by rank + path compression (disjoint forests) | O(α(n)) amortized | O(α(n)) amortized | α(n) ≤ 4 for all practical n |

---

## See Also

- [[Minimum Spanning Trees]]
- [[Prim-Jarník Algorithm]]
- [[Kruskal's Algorithm]]
- [[Disjoint Sets]]
- [[Graph Theory]]
- [[CSCE 411]]
