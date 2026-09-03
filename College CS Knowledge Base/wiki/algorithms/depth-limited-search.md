---
title: "Depth-Limited Search"
type: algorithm
tags: [csce420, dls, depth-limit, uninformed-search]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Depth-limited search (DLS) is [[Depth-First Search]] with a hard cap: nodes at depth $l$ cannot be expanded further. The cap removes DFS's failure mode of descending forever, at the price of missing solutions deeper than $l$.

## Behavior

Visit order for successive depth limits:

```
l = 0 :  1
l = 1 :  1 2 3
l = 2 :  1 2 4 5 3 6 7
```

Queuing function: enqueue at front (stack push), **pushing the depth along with the node** as `(<depth>, <node>)` so the limit can be checked on pop.

Queue evolution at depth limit 2:

```
[[(d0,1)]]                       initial state
[[(d1,2)][(d1,3)]]               pop 1, push 2 and 3
[[(d2,4)][(d2,5)][(d1,3)]]       pop 2, push 4 and 5
[[(d2,5)][(d1,3)]]               pop 4 - at the limit, cannot expand
[[(d1,3)]]                       pop 5 - at the limit, cannot expand
[[(d2,6)][(d2,7)]]               pop 3, push 6 and 7
```

## Evaluation

With branching factor $b$, depth limit $l$, solution depth $d$:

- **Complete if $l \ge d$** — conditionally complete, and the condition is unknowable in advance without domain knowledge
- **Time**: $O(b^l)$ worst case
- **Space**: $O(bl)$ — same as DFS with $l$ in place of $m$
- **Non-optimal** — inherits the problem from DFS

## The Catch

Choosing $l$ requires knowing roughly how deep the solution is. Too small and the search is complete-in-form but finds nothing; too large and the depth bound stops helping. [[Iterative Deepening Search]] eliminates the guess by trying every limit in increasing order.

## See Also

- [[Depth-First Search]]
- [[Iterative Deepening Search]]
- [[Uninformed Search]]
- [[CSCE 420]]
