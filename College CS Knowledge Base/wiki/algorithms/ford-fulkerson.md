---
title: "Ford-Fulkerson Algorithm"
type: algorithm
tags: [max-flow, ford-fulkerson, residual-graph, augmenting-path, min-cut]
sources: [lecture-15-maximum-flow]
course: CSCE 411
updated: 2026-04-09
---

# Ford-Fulkerson Algorithm

Ford-Fulkerson finds a maximum flow by repeatedly finding augmenting paths in the residual graph.

## Residual Graph

Given flow f on network G, the residual graph G_f has:
- **Forward edge** (u, v): residual capacity c(u,v) − f(u,v) — can push more flow
- **Backward edge** (v, u): residual capacity f(u,v) — can cancel existing flow

## Augmenting Path

Any path from s to t in G_f. Augmenting along it increases total flow by the **bottleneck** capacity (minimum residual capacity on the path).

## Algorithm

```
FordFulkerson(G, s, t):
  f = 0 (no flow on any edge)
  while there exists an augmenting path P in G_f:
    bottleneck = min residual capacity on P
    augment flow along P by bottleneck
  return f
```

## Correctness

A flow f is maximum ↔ no augmenting path exists in G_f ↔ value of f equals the capacity of some s-t cut.

This equivalence is the **Max-Flow Min-Cut Theorem**.

## Runtime

- **Integer capacities**: O(|f*| · m) — each augmentation increases flow by ≥ 1
- **Irrational capacities**: may not terminate (can cycle or converge to a non-optimal value)
- **Bad case**: two crossing edges each with capacity 1000; alternating augmenting path choices → 2000 iterations (exponential in the bit-length of capacities)

## See Also

- [[Edmonds-Karp Algorithm]]
- [[Maximum Flow]]
- [[CSCE 411]]
