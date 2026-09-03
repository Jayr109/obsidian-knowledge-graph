---
title: "Max-Weight Matching in Trees"
type: algorithm
tags: [tree-DP, matching, dynamic-programming, graphs]
sources: [exam-3-solutions-sp26]
course: CSCE 411
updated: 2026-05-03
---

Max-Weight Matching in Trees finds the maximum total edge weight of a matching in a weighted tree in O(n) time via tree DP. A matching is a set of edges with no shared vertex; "max weight" may mean fewer edges than the maximum-size matching. This extends [[Maximum Weight Independent Set]] (which assigns weights to vertices) to edge-weighted matching.

## Problem Definition

**Input**: A weighted tree T = (V, E, w) with n vertices, w: E → ℝ.

**Output**: The weight of a maximum-weight matching M ⊆ E (no two edges in M share a vertex).

## Algorithm

Root T at an arbitrary vertex r. For every u ∈ V(T), define:

MWM(u) = maximum matching weight achievable within the subtree of T rooted at u.

**Recurrence**:

```
MWM(u) = max(
  Σ_{v ∈ Children(u)} MWM(v),
  max_{v ∈ Children(u)} [w(u,v) + Σ_{w ∈ Children(v) ∪ Children(u) − {v}} MWM(w)]
)
```

**Case 1** (no edge of u is in the matching): recurse independently on each child's subtree. Result = sum of children's MWM values.

**Case 2** (include edge {u,v} for some child v): add w(u,v) then recurse on:
- All children of u *other than v* (each can still be matched freely in their subtrees), and
- All children of v (v is now matched to u, so v cannot be matched to any of its children — those children become "free" subproblems).

**Base case**: if u is a leaf, both sums/max are over empty sets → MWM(u) = 0. ✓

## Implementation

Fill by postorder traversal. Augment each vertex u with u.mwm. Since MWM(u) depends only on descendants, postorder guarantees all required values are ready.

Answer = MWM(r).

## Runtime Analysis

Work per vertex u:
- 1 constant step for the base/dispatch
- O(|Children(u)|) for the sum in Case 1
- O(|Children(u)| + |Grandchildren(u)|) for the max in Case 2

Total:

```
Σ_{u ∈ V} (1 + 2|Children(u)| + |Grandchildren(u)|)
= n + 2·Σ|Children| + Σ|Grandchildren|
≤ n + 2n + n = O(n)
```

(Each vertex is the child of at most one vertex and the grandchild of at most one vertex.)

**Time**: O(n) — **Space**: Θ(n)

## Contrast with Related Problems

| Problem | Weights on | General graph | Trees |
|---------|-----------|--------------|-------|
| [[Maximum Weight Independent Set]] | Vertices | NP-hard | O(n) DP |
| Max-Weight Matching in Trees | Edges | NP-hard (in general) | O(n) DP |
| Max-Size Matching | — | O(n·m) via flow | O(n) DP or flow |

## See Also

- [[Maximum Weight Independent Set]]
- [[Graph DP]]
- [[Dynamic Programming]]
- [[Bipartite Matching]]
- [[Exam 3 Solutions — Spring 2026]]
- [[CSCE 411]]
