---
title: "Greedy Best-First Search"
type: algorithm
tags: [csce420, greedy-search, heuristic, informed-search]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Greedy best-first search is [[Best-First Search]] using the heuristic $h(n)$ alone as the evaluation function — always move toward whatever *looks* closest to the goal. It is fast and it is wrong: incomplete and non-optimal, for the same reasons [[Depth-First Search]] is.

## The Algorithm

```
Function: Greedy-Best-First-Search (problem)
  h(n): estimated cost from n to goal
  return Best-First-Search(problem, h)
```

## Worked Example: Romania

Travelling from Arad to Bucharest with $h$ = straight-line distance:

```
VISIT (A): h=366, path=(A)
VISIT (S): h=253, path=(A S)
VISIT (F): h=178, path=(A S F)
VISIT (B): h=0,   path=(A S F B)
```

**Total path cost: 450.**

The greedy choice at each step is locally sensible — Sibiu looks closer than Timisoara or Zerind, Fagaras looks closer than Rimnicu Vilcea. But [[A* Search]] on the same map finds a route costing **418**, going through Rimnicu Vilcea and Pitesti. Greedy took the bait: Fagaras *looks* closer to Bucharest, but the road through it is longer.

That eight-unit gap is the entire argument for including $g(n)$.

## Evaluation

With branching factor $b$ and maximum depth $m$:

- **Time**: $O(b^m)$
- **Space**: same as time in the worst case (a bad heuristic) — **unlike DFS**, because the node list is retained
- **Incomplete**, just like DFS
- **Non-optimal**, just like DFS

The lecture repeatedly compares greedy to DFS: it commits to a direction and does not reconsider. The one place it is worse than DFS is space — DFS discards, greedy keeps a sorted frontier.

## The Fix

Add the cost already incurred: $f(n) = g(n) + h(n)$. See [[A* Search]].

## See Also

- [[A* Search]]
- [[Best-First Search]]
- [[Admissible Heuristics]]
- [[Uniform-Cost Search]]
- [[CSCE 420]]
