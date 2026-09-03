---
title: "Floyd-Warshall"
type: algorithm
tags: [dynamic-programming, graphs, shortest-paths, algorithms]
sources: [lecture-22-graph-dp]
course: CSCE 411
updated: 2026-04-09
---

Floyd-Warshall is a [[Dynamic Programming]] algorithm for solving the All-Pairs Shortest Paths (APSP) problem: find the shortest path between every pair of vertices in a weighted directed graph. It runs in O(V³) time and handles negative edge weights (but not negative cycles).

## Problem Definition

**Input**: Weighted directed graph G = (V, E) with edge weights w(u,v). May contain negative edges but no negative cycles.
**Output**: For all pairs (i, j), the shortest path distance d(i, j).

## Algorithm

**Key Idea**: DP over intermediate vertices. Let `D[i][j][k]` = shortest path from i to j using only vertices {1, ..., k} as intermediates.

**Recurrence**:
```
D[i][j][k] = min(
    D[i][j][k-1],          // path doesn't use vertex k
    D[i][k][k-1] + D[k][j][k-1]  // path goes through vertex k
)
```

**Base case**: `D[i][j][0]` = w(i,j) if edge exists, 0 if i=j, ∞ otherwise.

**Answer**: `D[i][j][V]` for all pairs.

**Time**: O(V³) — three nested loops over V vertices.
**Space**: O(V²) — with in-place update, the k dimension can be dropped.

## Implementation

```
for k from 1 to V:
    for i from 1 to V:
        for j from 1 to V:
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])
```

## Comparison with SSSP Reduction

Running SSSP (e.g., Dijkstra) from every vertex also solves APSP in O(V · (E log V)) for non-negative weights. Floyd-Warshall is preferred when:
- Graphs are dense (E ≈ V²), making Floyd-Warshall's O(V³) competitive.
- Negative edge weights are present (Dijkstra doesn't handle them; Bellman-Ford would give O(V² · E)).
- Simplicity of implementation matters.

## Historical Note

Named after Robert Floyd and Stephen Warshall. Robert Floyd is the academic great-great-great-grandfather of [[Calvin Beideman]] — a lineage noted in Lecture 22 as a "fun fact."

## See Also

- [[Graph DP]]
- [[Dynamic Programming]]
- [[Maximum Weight Independent Set]]
- [[Calvin Beideman]]
- [[CSCE 411]]
