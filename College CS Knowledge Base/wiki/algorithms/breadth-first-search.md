---
title: "Breadth-First Search"
type: algorithm
tags: [csce420, bfs, uninformed-search, fifo]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Breadth-first search (BFS) explores the search tree level by level, visiting all nodes at depth $d$ before any at depth $d+1$. As an instance of the [[General Search Algorithm]], it is defined by one choice: **enqueue expanded nodes at the end of the node list** (FIFO).

## Behavior

On a complete binary tree numbered breadth-first, the visit order is simply `1 2 3 4 5 6 7 8 9 10 11 12 13 14 15`.

Queue evolution (bold = just expanded and added):

```
[1]                                  initial node list
[[2][3]]                             visit 1, enqueue 2 and 3
[[3][4][5]]                          visit 2, enqueue 4 and 5
[[4][5][6][7]]                       visit 3, enqueue 6 and 7 - all depth-2 nodes now queued
...
[[8][9][10][11][12][13][14][15]]     all depth-3 nodes queued
```

The characteristic signature: at any moment the node list holds an entire depth layer.

## Evaluation

With branching factor $b$ and solution depth $d$:

- **Complete** — it will find a solution if one exists
- **Time**: $1 + b + b^2 + \dots + b^d$
- **Space**: $O(b^{d+1})$, where $d$ is the depth of the *shallowest* solution
- **Optimal** for unit step costs (the shallowest goal is the cheapest)

## Space Is the Real Problem

The lecture is explicit that **space is more of a problem than time in most cases**, even though time is exponential too. The reason is practical: an algorithm that is merely slow can be left running, but one that exhausts memory simply stops. This is the motivation for [[Iterative Deepening Search]], which achieves BFS's guarantees at DFS's space cost.

## Relationship to Uniform-Cost

[[Uniform-Cost Search]] is BFS generalized to non-unit step costs: instead of visiting the shallowest node, visit the lowest-cost node, where BFS is the special case $g(n) = \text{Depth}(n)$.

## See Also

- [[Uninformed Search]]
- [[Depth-First Search]]
- [[Uniform-Cost Search]]
- [[Iterative Deepening Search]]
- [[General Search Algorithm]]
- [[CSCE 420]]
