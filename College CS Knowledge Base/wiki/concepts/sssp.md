---
title: "SSSP"
type: concept
tags: [sssp, shortest-paths, dijkstra, bellman-ford, dag, graph]
sources: [lecture-10-sssp]
course: CSCE 411
updated: 2026-04-09
---

# SSSP

**Single Source Shortest Paths (SSSP)**: given a weighted directed graph and source vertex s, find the shortest path from s to every reachable vertex. The result is a **shortest path tree** rooted at s.

---

## Algorithm Selection

| Graph Type | Algorithm | Runtime |
|---|---|---|
| Unweighted | BFS | O(n + m) |
| Non-negative weights | Dijkstra (binary heap) | O((n + m) log n) |
| Non-negative weights, dense | Dijkstra (Fibonacci heap) | O(m + n log n) |
| Negative weights, no neg cycles | Bellman-Ford | O(nm) |
| DAG (any weights) | DAG Shortest Paths | O(n + m) |

**Negative cycles**: SSSP is undefined if a negative cycle lies on any path from s to t — path length can be made arbitrarily small by looping through the cycle.

---

## The Universal Algorithm (Ford/Dantzig/Minty, 1950s)

All SSSP algorithms are special cases of one framework:

> Repeatedly relax **tense edges** until none remain.

A **tense edge** (u, v) satisfies: `dist[v] > dist[u] + w(u,v)`

The algorithms differ in which tense edge they choose to relax next.

---

## Dijkstra's Algorithm

See [[Dijkstra's Algorithm]].

Greedily extracts the minimum-distance unvisited vertex; requires non-negative edge weights.

---

## Bellman-Ford Algorithm

See [[Bellman-Ford Algorithm]].

Runs n−1 rounds relaxing all edges. Handles negative weights; detects negative cycles.

---

## DAG Shortest Paths

Process vertices in topological order; relax all outgoing edges. Handles negative edges because a DAG has no cycles.

**Runtime**: O(n + m)

---

## See Also

- [[Dijkstra's Algorithm]]
- [[Bellman-Ford Algorithm]]
- [[BFS and DFS]]
- [[Floyd-Warshall]]
- [[Graph Theory]]
- [[CSCE 411]]
