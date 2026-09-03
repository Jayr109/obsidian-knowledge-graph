---
title: "Best-First Search"
type: algorithm
tags: [csce420, best-first, evaluation-function, informed-search]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Best-first search is the generic **informed** search: order the node list by an evaluation function and always visit the most promising node. [[Greedy Best-First Search]] and [[A* Search]] are both instances, differing only in the evaluation function supplied.

## The Algorithm

```
Function: Best-First-Search (problem, Eval-Fn)
  Queuing-Fn <- sorted list by Eval-Fn(node)
  return General-Search(problem, Queuing-Fn)
```

It is the [[General Search Algorithm]] with a sorting queuing function: expanded nodes are added and the list is re-sorted by each node's `Eval-Fn` value.

## The Family

| Algorithm | Eval-Fn |
|---|---|
| [[Uniform-Cost Search]] | $g(n)$ |
| [[Greedy Best-First Search]] | $h(n)$ |
| [[A* Search]] | $g(n) + h(n)$ |
| [[Beam Search]] | any, but keeps only the best $n$ |

One of the simplest evaluation functions is the estimated cost to reach the goal — which gives greedy search.

## Where the Domain Knowledge Enters

Informed search means obtaining an evaluation function **from domain knowledge**. The search algorithm itself is unchanged from the uninformed case; all the leverage is in $h(n)$. This is why [[Admissible Heuristics]] gets its own treatment — heuristic design, not algorithm design, is where the work is.

## See Also

- [[Greedy Best-First Search]]
- [[A* Search]]
- [[Admissible Heuristics]]
- [[General Search Algorithm]]
- [[Heuristic Search]]
- [[CSCE 420]]
