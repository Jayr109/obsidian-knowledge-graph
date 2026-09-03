---
title: "Prim-Jarník Algorithm"
type: algorithm
tags: [mst, prim, jarnik, priority-queue, greedy, graph]
sources: [lecture-11-msts]
course: CSCE 411
updated: 2026-04-09
---

# Prim-Jarník Algorithm

Prim-Jarník (commonly called "Prim's") finds a Minimum Spanning Tree by growing one tree from a single starting vertex, repeatedly adding the lightest edge that connects the current tree to a new vertex. The algorithm was discovered by Vojtěch Jarník in 1930, before Prim (1957).

## Algorithm

```
PrimJarnik(G, start):
  key[start] = 0; key[v] = ∞ for v ≠ start
  parent[v] = null for all v
  Q = priority queue of all vertices (keyed by key[])
  while Q is not empty:
    u = extract_min(Q)
    for each neighbor v of u with edge weight w(u,v):
      if v ∈ Q and w(u,v) < key[v]:
        key[v] = w(u,v)
        parent[v] = u
        decrease_key(Q, v, key[v])
MST = { (parent[v], v) : v ≠ start }
```

## Correctness

By the Light Edge Property: at each step, the lightest edge leaving the current tree crosses the cut (tree, non-tree) and is therefore part of some MST.

## Runtime

| Priority Queue | Total Runtime |
|---|---|
| Binary heap | O((n + m) log n) |
| Fibonacci heap | O(m + n log n) |

For dense graphs (m ≈ n²), the Fibonacci heap version gives O(n²), matching the naive O(n²) implementation.

## Comparison with Dijkstra's

Very similar structure:
- [[Dijkstra's Algorithm]] updates `key[v]` with `dist[u] + w(u,v)` (path distance)
- Prim-Jarník updates `key[v]` with just `w(u,v)` (edge weight only)

Same priority queue mechanics; different update semantics.

## See Also

- [[Minimum Spanning Trees]]
- [[Kruskal's Algorithm]]
- [[Dijkstra's Algorithm]]
- [[CSCE 411]]
