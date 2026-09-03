---
title: "Edmonds-Karp Algorithm"
type: algorithm
tags: [max-flow, edmonds-karp, bfs, ford-fulkerson, polynomial]
sources: [lecture-15-maximum-flow]
course: CSCE 411
updated: 2026-04-09
---

# Edmonds-Karp Algorithm

Edmonds-Karp is Ford-Fulkerson with **BFS** used to find augmenting paths (shortest path by hop count). This guarantees polynomial runtime regardless of edge capacities.

## Key Property

Using BFS, augmenting paths always have the minimum number of edges. Two structural lemmas ensure fast convergence:

1. **Increasing Distances Lemma**: distances from s to all vertices in the residual graph are non-decreasing across iterations
2. **Disappearing Edges Lemma**: each edge can "disappear and reappear" at most n/2 times before the algorithm terminates

## Runtime

**Theorem**: Edmonds-Karp runs in O(nm²).

- At most O(nm) augmentations (from the two lemmas)
- Each BFS is O(m)
- Total: O(nm²)

This is polynomial in n and m, **independent of edge capacities or flow values**.

## Comparison with Ford-Fulkerson

| Algorithm | Runtime | Terminates for irrationals? |
|---|---|---|
| Ford-Fulkerson (arbitrary path) | O(\|f*\| · m) | No |
| Edmonds-Karp (BFS) | O(nm²) | Yes |

The fastest known max-flow algorithm runs in O(m^(1+o(1))).

## See Also

- [[Ford-Fulkerson Algorithm]]
- [[Maximum Flow]]
- [[CSCE 411]]
