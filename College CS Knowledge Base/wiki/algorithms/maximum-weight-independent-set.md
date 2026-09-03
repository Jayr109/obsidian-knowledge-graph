---
title: "Maximum Weight Independent Set"
type: algorithm
tags: [dynamic-programming, graphs, trees, algorithms]
sources: [lecture-22-graph-dp]
course: CSCE 411
updated: 2026-04-09
---

The Maximum Weight Independent Set (MWIS) problem asks for a subset of vertices in a graph such that no two selected vertices are adjacent, and the total weight is maximized. On general graphs this is NP-hard, but on trees it is solvable in polynomial time via [[Dynamic Programming]] over subtrees.

## Problem Definition

**Input**: Graph G = (V, E) with vertex weights w(v).
**Output**: An independent set S ⊆ V (no two vertices in S share an edge) maximizing Σ w(v) for v ∈ S.

**General graphs**: NP-hard (related to NP-completeness, covered later in CSCE 411).
**Trees**: Polynomial — O(n) via tree DP.

## Tree DP Approach

**Key Insight**: For trees, natural subproblems correspond to **subtrees rooted at each node**. This exploits tree structure rather than treating the tree as a generic graph.

**Subproblems**: For each vertex v, define:
- `OPT(v, 1)` = max weight IS in subtree rooted at v, *including* v
- `OPT(v, 0)` = max weight IS in subtree rooted at v, *excluding* v

**Recurrence** (let children(v) = set of children of v):

```
OPT(v, 1) = w(v) + Σ OPT(c, 0)   for c in children(v)
             (include v → must exclude all children)

OPT(v, 0) = Σ max(OPT(c, 0), OPT(c, 1))  for c in children(v)
             (exclude v → each child can be included or not)
```

**Base case** (leaf node v): `OPT(v, 1) = w(v)`, `OPT(v, 0) = 0`

**Answer**: `max(OPT(root, 0), OPT(root, 1))`

**Time**: O(n) — each vertex processed once.
**Space**: O(n) — memoization table over all vertices.

## Example (from Lecture 22)

Tree with weights including 80, 62, 99, 20, 35 among others; optimal IS total weight was 296.

*Note: Full recurrence diagram was visual in lecture slides; text extraction captured the key formulation.*

## See Also

- [[Graph DP]]
- [[Dynamic Programming]]
- [[Floyd-Warshall]]
- [[CSCE 411]]
