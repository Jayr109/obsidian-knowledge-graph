---
title: "IDA*"
type: algorithm
tags: [csce420, search, heuristics, iterative-deepening, memory]
sources: [csce420-midterm-practice, csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

IDA* (Iterative Deepening A*) keeps A*'s completeness and optimality while reducing space from exponential to **linear in the current search depth**. It does this by replacing the priority queue with repeated depth-first searches bounded by an increasing f-limit, implemented recursively as DFS-CONTOUR.

## Algorithm

1. Set the initial f-limit to $f(\text{root}) = h(\text{root})$.
2. Run **DFS-CONTOUR**: a depth-first search that expands any node with $f(n) \le \text{f-limit}$ and prunes (returns) at any node with $f(n) > \text{f-limit}$, recording the smallest such $f$ it saw.
3. If a goal was found, return it.
4. Otherwise set the new f-limit to that smallest pruned $f$ value and go to step 2.

Each iteration explores exactly one more [[Heuristic Search|contour]] than the last.

## Why Space Is Linear

DFS-CONTOUR is recursive, so **memory = the call stack**. At any instant the only nodes retained are those on the path from the root to the current node, plus their immediate unexplored siblings. When a recursive call returns, its entire subtree is discarded. So space is $O(bd)$ where $d$ is the current depth and $b$ the branching factor — not $O(b^d)$.

A* cannot do this because best-first order jumps around the tree: to pick the globally smallest $f$ next, it must remember every candidate. IDA* gives up that global ordering, recovering it approximately through the f-limit, and pays for it by **re-expanding** nodes on every iteration.

## Trade-off

| | [[A* Search]] | IDA* |
|---|---|---|
| Space | Exponential (all generated nodes) | **Linear in depth** (call stack) |
| Node re-expansion | None | Re-expands all previous contours each iteration |
| Complete | Yes | Yes |
| Optimal | Yes (admissible $h$) | Yes (admissible $h$) |

The re-expansion cost is usually acceptable: in an exponentially growing tree the last contour dominates the total work, so repeating the earlier ones adds a constant factor rather than an asymptotic penalty.

Midterm Practice Problem 2 asks exactly this contrast; the node-by-node answer is worked on [[A* Search]].

## From the Lecture

IDA* is [[Iterative Deepening Search]] with the **$f$-cost** playing the role that depth plays there: search within an $f$ bound, then raise the bound and restart until a solution is found.

```
function IDA*(problem)
  root <- Make-Node(Initial-State(problem))
  f-limit <- f-Cost(root)
  loop
    solution, f-limit <- DFS-Contour(root, f-limit)
    if solution != NULL then return solution
    if f-limit == infinity then return failure
  end loop
```

### DFS-Contour

```
function DFS-Contour (root, f-limit): returns solution, f-limit
  if f-cost(root) > f-limit, return null solution and f-cost(root)
  if root is a goal node, return solution and its f-cost(root)
  for successors of root do
    (solution, new-f-limit) <- DFS-Contour(successors, f-limit)
    if new-f-limit is minimum so far then best-so-far <- (solution, new-f-limit)
  end for
  return (solution, f-limit) of the best-so-far
```

The returned $f$-limit is the **minimum $f$-cost among nodes that exceeded the current bound** — that becomes the next contour. Implementation mirrors recursive DFS.

### Time Complexity Depends on the Heuristic

This is the detail the practice exam does not cover:

- **Few distinct $h$ values** → few $f$-contours → behaviour approaches [[A* Search]].
- **Complex problems** → each contour may contain only *one* new node. If A* visits $N$ nodes, IDA* then visits $1 + 2 + \dots + N = \frac{N(N+1)}{2} = O(N^2)$.

That quadratic blow-up is the real cost of the memory saving.

### The Epsilon Fix

Use a **fixed increment $\epsilon$** for the $f$-limit instead of the exact next contour. The solution is then suboptimal by at most $\epsilon$ — called **$\epsilon$-admissible**. This trades a bounded amount of optimality for far fewer iterations.

### Evaluation

- **Complete and optimal**
- **Space**: proportional to the longest path explored — because it is depth-first
- **Time**: depends on the number of distinct values $h(n)$ can assume

## See Also

- [[A* Search]]
- [[Heuristic Search]]
- [[CSCE 420]]
