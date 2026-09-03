---
title: "Dijkstra's Algorithm"
type: algorithm
tags: [sssp, dijkstra, shortest-paths, priority-queue, greedy, graph]
sources: [lecture-10-sssp]
course: CSCE 411
updated: 2026-04-09
---

# Dijkstra's Algorithm

Dijkstra's algorithm solves SSSP for graphs with **non-negative edge weights**. It greedily visits vertices in order of increasing distance from the source.

## Algorithm

```
Dijkstra(G, s):
  dist[s] = 0; dist[v] = ∞ for all v ≠ s
  Q = priority queue of all vertices (keyed by dist)
  while Q is not empty:
    u = extract_min(Q)
    for each neighbor v of u:
      if dist[u] + w(u,v) < dist[v]:
        dist[v] = dist[u] + w(u,v)   // relax edge
        pred[v] = u
        decrease_key(Q, v, dist[v])
```

The predecessor array `pred` implicitly encodes the shortest path tree.

---

## Correctness

**Key invariant**: when a vertex u is extracted from Q, `dist[u]` is its final shortest-path distance.

**Proof sketch** (by induction on vertices extracted):
- When u is extracted, all previously extracted vertices have their final distances.
- Any shortest path to u must pass through only previously extracted vertices (since dist[u] is the minimum in Q).
- Because all edge weights are non-negative, no future relaxation can decrease dist[u].

**Fails for negative edges**: a negative edge (x, v) could reduce dist[v] after v has already been finalized. Dijkstra never revisits finalized vertices, so it would return an incorrect distance.

---

## Runtime

| Priority Queue | Extract-Min | Decrease-Key | Total |
|---|---|---|---|
| Binary heap | O(log n) | O(log n) | O((n + m) log n) |
| Fibonacci heap | O(log n) amortized | O(1) amortized | O(m + n log n) |

The Fibonacci heap version is **asymptotically optimal** for general graphs with non-negative weights.

---

## Comparison with Prim-Jarník

Dijkstra and [[Prim-Jarník Algorithm]] have nearly identical structure:
- Dijkstra updates `key[v]` with `dist[u] + w(u,v)`
- Prim-Jarník updates `key[v]` with just `w(u,v)`

Same priority queue operations; different semantics.

---

## See Also

- [[SSSP]]
- [[Bellman-Ford Algorithm]]
- [[Prim-Jarník Algorithm]]
- [[Graph Theory]]
- [[CSCE 411]]
