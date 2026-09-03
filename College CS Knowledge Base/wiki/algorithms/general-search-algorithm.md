---
title: "General Search Algorithm"
type: algorithm
tags: [csce420, search, queuing-function, completeness, optimality]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Every search strategy in [[CSCE 420]] is the same algorithm with a different **queuing function**. The general skeleton maintains a node list, repeatedly fetches the front node, tests it for the goal, and enqueues its children according to a strategy-specific rule.

## The Skeleton

```
Function: General-Search (problem, Que-Fn)
  node-list <- [ Make-Node(initial-state) ]
  loop
    If Empty(node-list) then return FAIL
    node <- Get-First-Node(node-list)          // fetch node: this is a VISIT
    If (node == goal) then return node          // success
    node-list <- Que-Fn(node-list, Expand(node))  // expand and queue
  end loop
```

- **node** = state plus bookkeeping: current depth, path to the current state, evaluation info
- **Expand(node)** returns the set of child nodes

Because only `Que-Fn` changes between strategies, the whole family reduces to one design decision: *where do newly expanded nodes go in the list?*

| Strategy | Queuing function |
|---|---|
| [[Breadth-First Search]] | Enqueue at end |
| [[Depth-First Search]] | Enqueue at front (stack push) |
| [[Uniform-Cost Search]] | Keep sorted by path cost $g(n)$ |
| [[Best-First Search]] | Keep sorted by evaluation function |

## Visit vs. Expand

The lecture flags this distinction emphatically, and it is a standard exam trap.

> **A visit is the act of fetching a node out of the node list and goal-testing it.** Expanding — generating a node's children — is a different event.

Time complexity is counted in **visits**, not expansions. A node can sit in the node list, having been generated, without ever being visited.

## Four Evaluation Criteria

| Criterion | Question |
|---|---|
| **Time complexity** | How many nodes are visited? |
| **Space complexity** | How many nodes are stored in the node list at any one time? |
| **Completeness** | If a solution exists, is it guaranteed to be found? |
| **Optimality** | Is the *best* solution guaranteed? |

Completeness and optimality are independent. [[Depth-Limited Search]] is conditionally complete but never optimal; [[Iterative Deepening Search]] is both.

## Depth Convention

Depth is 0 at the root, and each move adds 1 to the parent's depth. This matters when reading complexity expressions — BFS space is $O(b^{d+1})$ under this convention.

## See Also

- [[Search Problem Formulation]]
- [[Uninformed Search]]
- [[Best-First Search]]
- [[CSCE 420]]
