---
title: "Uninformed Search"
type: concept
tags: [csce420, uninformed-search, bfs, dfs, ids, complexity]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

**Uninformed** (blind) search strategies use systematic exploration with no domain knowledge beyond the problem definition — in contrast to [[Heuristic Search|informed search]], which uses an evaluation function to narrow the scope. All are instances of the [[General Search Algorithm]] differing only in queuing function.

## The Comparison Table

With branching factor $b$, solution depth $d$, maximum depth $m$, and depth limit $l$:

| Strategy | Complete? | Optimal? | Time | Space |
|---|---|---|---|---|
| [[Breadth-First Search]] | Yes | Yes (unit costs) | $1+b+b^2+\dots+b^d$ | $O(b^{d+1})$ |
| [[Uniform-Cost Search]] | Yes | Yes | — | — |
| [[Depth-First Search]] | **No** | No | $O(b^m)$ | $O(bm)$ |
| [[Depth-Limited Search]] | If $l \ge d$ | No | $O(b^l)$ | $O(bl)$ |
| [[Iterative Deepening Search]] | Yes | **Yes** | $O(b^d)$ | $O(bd)$ |
| [[Bidirectional Search]] | Yes | Yes | $O(b^{d/2})$ | $O(b^{d/2})$ |

## The Central Tradeoff

BFS and DFS fail in opposite ways, and the resolution is the point of the whole section:

- **BFS** is complete and optimal but its *space* is exponential — and the lecture stresses that **space is the bigger problem than time in most cases**.
- **DFS** has linear space $O(bm)$ but is incomplete: it may wander down an infinite or very deep branch.
- **[[Iterative Deepening Search]]** takes DFS's space and BFS's completeness and optimality, paying only a constant factor in repeated work. It is the default answer when the search space is huge and the solution depth is unknown.

That IDS re-visits already-explored nodes at each successive depth limit looks wasteful, but the bottom level dominates the node count, so the overhead is bounded.

## When Each Is Appropriate

- **DFS** — many shallow goals; bad for deep or infinite-depth state spaces
- **DLS** — the solution is known to lie within a depth bound
- **IDS** — huge space, unknown solution depth
- **BDS** — the goal is explicit and operators are reversible

## Implementation Note

The node list can be an explicit stack or queue, or implicit in a recursive call stack (as in DFS by recursion). Either way, distinguish **state** (the world configuration) from **node** (state + depth + evaluation info + path).

## See Also

- [[General Search Algorithm]]
- [[Search Problem Formulation]]
- [[Heuristic Search]]
- [[Repeated States]]
- [[CSCE 420]]
