---
title: "Graph DP"
type: concept
tags: [dynamic-programming, graphs, algorithms]
sources: [lecture-22-graph-dp]
course: CSCE 411
updated: 2026-04-09
---

Graph DP is the application of [[Dynamic Programming]] to problems where the input is a graph rather than an array or sequence. The central challenge is choosing subproblems that exploit the graph's structure, since naive approaches (treating edges as an array) often miss structure that makes the problem tractable.

## Key Insight: Subproblem Design for Graphs

- **General graphs**: subproblems often index over sets of vertices or edges (e.g., [[Floyd-Warshall]] uses intermediate vertex sets).
- **Trees**: subproblems correspond to subtrees. This is a powerful idea because many hard problems on general graphs become tractable on trees.
  - Maximum Weight Independent Set is NP-hard on general graphs but polynomial on trees via tree DP (see [[Maximum Weight Independent Set]]).

## All-Pairs Shortest Paths (APSP)

The goal is to find shortest paths between every pair of vertices in a weighted graph.

**Reduction to SSSP**: Run single-source shortest paths (e.g., Dijkstra or Bellman-Ford) from every vertex. Cost: O(V · SSSP).

**DP approach**: [[Floyd-Warshall]] uses a DP over intermediate vertices, achieving O(V³) with a cleaner implementation that also handles negative edge weights (but not negative cycles).

## Algorithms

- [[Floyd-Warshall]] — APSP via DP over intermediate vertices
- [[Maximum Weight Independent Set]] — tree DP via include/exclude recurrence on subtrees

## See Also

- [[Dynamic Programming]]
- [[Floyd-Warshall]]
- [[Maximum Weight Independent Set]]
- [[CSCE 411]]
