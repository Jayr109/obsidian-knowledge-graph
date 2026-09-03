---
title: "Bellman-Ford Algorithm"
type: algorithm
tags: [sssp, bellman-ford, negative-edges, negative-cycles, shortest-paths, graph]
sources: [lecture-10-sssp]
course: CSCE 411
updated: 2026-04-09
---

# Bellman-Ford Algorithm

Bellman-Ford solves SSSP for directed graphs that may contain **negative edge weights** (but no negative cycles reachable from s). It also detects negative cycles.

## Algorithm

```
BellmanFord(G, s):
  dist[s] = 0; dist[v] = ∞ for all v ≠ s
  for i from 1 to n-1:
    for each edge (u,v) in E:
      if dist[u] + w(u,v) < dist[v]:
        dist[v] = dist[u] + w(u,v)
  // Negative cycle detection:
  for each edge (u,v) in E:
    if dist[u] + w(u,v) < dist[v]:
      return "negative cycle reachable from s"
```

---

## Correctness

**Invariant**: after k rounds, `dist[v]` = the shortest path distance from s to v using **at most k edges**.

Since any simple shortest path in an n-vertex graph uses at most n−1 edges (assuming no negative cycles), n−1 rounds suffice to compute all correct distances.

**Negative cycle detection**: if any edge remains tense after n−1 rounds, there must be a negative cycle reachable from s (a shorter path would require looping, which implies a negative cycle).

---

## Runtime

**O(nm)** — (n−1) rounds × m edge relaxations per round.

---

## When to Use

- Graph has negative edges but no negative cycles
- Negative cycle detection is needed
- [[Dijkstra's Algorithm]] fails (negative edges present)
- [[Floyd-Warshall]] is too slow (O(n³)) or all-pairs is not needed

## DAG Alternative

For DAGs with negative edges, use DAG Shortest Paths (O(n + m)) — topological order guarantees no cycles. See [[SSSP]].

---

## See Also

- [[SSSP]]
- [[Dijkstra's Algorithm]]
- [[Floyd-Warshall]]
- [[CSCE 411]]
