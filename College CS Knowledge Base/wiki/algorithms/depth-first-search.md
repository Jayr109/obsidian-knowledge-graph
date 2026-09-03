---
title: "Depth-First Search"
type: algorithm
tags: [csce420, dfs, uninformed-search, stack, lifo]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Depth-first search (DFS) explores as deeply as possible before backtracking. In the [[General Search Algorithm]] it is defined by one choice: **enqueue expanded nodes at the front** of the node list (stack push, LIFO).

## Behavior

On a complete binary tree numbered breadth-first, the DFS visit order is `1 2 4 8 9 5 10 11 3 6 12 13 7 14 15`.

Queue evolution (bold = just expanded and pushed):

```
[[1]]              initial node list
[[2][3]]           pop 1, push its children at the front
[[4][5][3]]        pop 2, push at the front
[[8][9][5][3]]     pop 4, push at the front
...
```

Compare with [[Breadth-First Search]]: identical algorithm, opposite insertion end, completely different traversal.

## Evaluation

With branching factor $b$, solution depth $d$, and maximum depth $m$:

- **Incomplete** — may wander down the wrong path indefinitely
- **Time**: $O(b^m)$ nodes visited, worst case
- **Space**: $O(bm)$ — only the dangling nodes along the current search path
- **Non-optimal**

The space result is the reason DFS matters. It is linear in depth, not exponential, because the algorithm never holds more than one root-to-frontier path plus siblings.

## When to Use It

- **Good** when there are many shallow goals
- **Bad** for deep or infinite-depth state spaces — precisely where incompleteness bites

Reversible operators make infinite depth easy to produce accidentally; see [[Repeated States]].

## Implementation

Two options with the same behavior:

- **Explicit stack** — store expanded nodes in a stack
- **Recursion** — the recursive call stack stores them implicitly

Keep the state/node distinction: a **state** is the world configuration; a **node** additionally carries current depth, evaluation info, and the path to the current position.

## Fixing the Incompleteness

[[Depth-Limited Search]] caps the depth, restoring conditional completeness. [[Iterative Deepening Search]] then sweeps the cap upward, recovering completeness *and* optimality while keeping DFS's linear space.

## See Also

- [[Uninformed Search]]
- [[Breadth-First Search]]
- [[Depth-Limited Search]]
- [[Iterative Deepening Search]]
- [[Repeated States]]
- [[CSCE 420]]
