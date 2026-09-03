---
title: "Iterative Deepening Search"
type: algorithm
tags: [csce420, ids, iterative-deepening, uninformed-search, optimal]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Iterative deepening search (IDS) runs [[Depth-Limited Search]] repeatedly with an increasing depth limit until a solution is found. It is the resolution of the BFS/DFS tradeoff: **DFS's linear space with BFS's completeness and optimality.**

## Behavior

Node visit order across successive limits:

```
l = 0 :  1
l = 1 :  1 2 3
l = 2 :  1 2 4 5 3 6 7
l = 3 :  1 2 4 8 9 5 10 11 3 6 12 13 7 14 15
```

Each pass is an ordinary DLS — enqueue at front, carrying `(<depth>, <node>)`. The algorithm **re-visits already-explored nodes at each successive depth limit**.

## Evaluation

With branching factor $b$ and solution depth $d$:

- **Complete** — unlike DLS, which is only conditionally complete
- **Time**: $O(b^d)$ nodes visited, worst case
- **Space**: $O(bd)$ — the DFS-style bound
- **Optimal** — unlike DFS or DLS

## Why the Repeated Work Is Acceptable

The obvious objection is that IDS re-explores the shallow levels once per iteration. The reason this is tolerable: in a tree with branching factor $b$, the **deepest level contains most of the nodes**, so the sum over all iterations stays $O(b^d)$ — the same order as a single BFS pass. Constant-factor waste buys an exponential space saving.

## When to Use It

The lecture's summary: **good when the search space is huge and the depth of the solution is not known.** That combination is common, which is why IDS is the standard uninformed default.

## The Informed Analogue

[[IDA*]] applies the identical idea to [[A* Search]], substituting the $f$-cost for depth as the thing being limited. The motivation is the same — A* is complete and optimal but space-hungry, exactly as BFS is.

## See Also

- [[Depth-Limited Search]]
- [[Depth-First Search]]
- [[Breadth-First Search]]
- [[IDA*]]
- [[Uninformed Search]]
- [[CSCE 420]]
