---
title: "Kruskal's Algorithm"
type: algorithm
tags: [mst, kruskal, union-find, sorting, greedy, graph]
sources: [lecture-11-msts]
course: CSCE 411
updated: 2026-04-09
---

# Kruskal's Algorithm

Kruskal's algorithm finds a Minimum Spanning Tree by processing edges in sorted order and adding each edge if it doesn't create a cycle.

## Algorithm

```
Kruskal(G):
  Sort edges by weight (ascending)
  For each vertex v: make_set(v)
  MST = {}
  for each edge (u,v) in sorted order:
    if find(u) ≠ find(v):   // u and v are in different components
      MST.add(u,v)
      union(u, v)
  return MST
```

## Correctness

Each added edge is the lightest edge crossing the cut between two existing components. By the Light Edge Property, it belongs to some MST.

## Runtime

- Sorting: O(m log m)
- Union-Find operations: O(m · α(n)) ≈ O(m) with union by rank + path compression
- **Total: O(m log m)** — dominated by sorting

## When to Use vs Prim-Jarník

- **Kruskal's** is simpler to implement and better for sparse graphs
- **[[Prim-Jarník Algorithm]]** with Fibonacci heap is better for dense graphs: O(m + n log n) vs O(m log m)
- For dense graphs (m ≈ n²): Prim-Jarník is asymptotically faster

## See Also

- [[Minimum Spanning Trees]]
- [[Prim-Jarník Algorithm]]
- [[Disjoint Sets]]
- [[CSCE 411]]
