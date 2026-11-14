---
title: "Minimax"
type: algorithm
tags: [csce420, games, adversarial-search, game-tree]
sources: [csce420-midterm-practice, csce420-lecture-02-search-and-game-playing, csce420-fall2026-0918-minmax-notebook-walkthrough]
course: CSCE 420
updated: 2026-09-18
---

Minimax computes the optimal move in a two-player, zero-sum, perfect-information game by backing utilities up the game tree: MAX nodes take the maximum over children, MIN nodes take the minimum, and leaves carry the utility of a terminal position. It assumes the opponent plays optimally, so the value it returns is the best outcome you can guarantee.

## Recurrence

$$
\text{minimax}(n) =
\begin{cases}
\text{Utility}(n) & n \text{ terminal} \\
\max_{s \in \text{succ}(n)} \text{minimax}(s) & n \text{ is a MAX node} \\
\min_{s \in \text{succ}(n)} \text{minimax}(s) & n \text{ is a MIN node}
\end{cases}
$$

Implemented as a depth-first recursion, so space is $O(bd)$ but time is $O(b^d)$ — the full tree.

## Properties

- **Complete** if the tree is finite
- **Optimal** against an optimal opponent
- Only the *ordering* of leaf utilities matters — any monotone rescaling of the utilities yields the same chosen move. (This stops being true once chance nodes enter; see [[Expectimax]].)

## Practical Limits

$O(b^d)$ is unusable for real games. Two fixes, and they are different in kind:

1. **[[Alpha-Beta Pruning]]** — exact. Skips subtrees that cannot change the answer, giving the same value in as few as $O(b^{d/2})$ nodes.
2. **Depth-limited search with an evaluation function** — approximate. Stop at a cutoff depth and estimate the value of the position heuristically. This is where the error in real game players comes from.

## From the Lecture

### The Procedure

Generate the whole tree and apply the utility function to the leaves, then propagate upward: at a **MIN** node assign the min of the successors' utilities, at a **MAX** node the max. The governing **assumption is that the opponent acts optimally**.

```
function Minimax-Decision (game) returns operator
  return operator leading to a child state with
         max(Minimax-Value(child state, game))

function Minimax-Value(state, game) returns utility value
  if Goal(state), return Utility(state)
  if Max's move then return max of successors' Minimax-Value
  else                return min of successors' Minimax-Value
```

### Evaluation

With branching factor $b$ and maximum depth $m$:

- **Complete** — if the game tree is finite
- **Optimal** — *if the opponent is optimal*; against a suboptimal opponent minimax may leave value on the table
- **Time**: $b^m$
- **Space**: $bm$ — depth-first, but only when the utility values of all nodes are known

### Resource Limits

Full minimax is impossible in real games (chess: $b \approx 35$, giving $35^{100}$ nodes for 50 moves each). Three responses:

- **Evaluation function** — estimate how desirable a state is
- **Cutoff test** — a depth limit
- **Pruning** — [[Alpha-Beta Pruning]]

The depth limit produces the **horizon effect**: decisive events just beyond the cutoff are invisible.

### Evaluation Functions

For chess, a linear weighted sum $\text{Eval}(s) = \sum_i w_i f_i(s)$, where $f_i$ might be (number of white piece X) − (number of black piece X), plus features like control of the centre.

**Exact values do not matter — only the order** of the successors' minimax values. That ceases to be true once chance nodes appear; see [[Expectimax]].

See [[Game Playing]] for the full framing.

## The Course Implementation (`minmax.ipynb`)

The HW2 starter, walked through in [[CSCE 420 Fall 2026 — 09-18 minmax.ipynb Walkthrough]], is one recursive function `minmax_value(tree, node_type)` with three cases — leaf, MAX, MIN — where the node type is passed as a parameter and flipped on every recursive call, and ±∞ are `99999` / `-99999`. The game tree is a nested Python list, so leaves may sit at different depths. A printed `CALL`/`returns` trace with indentation shows the recursion; on the demo tree `[[7, [3, 8, 1], [15, 9]], [12, [17, 13]]]` the root value is 12.

## See Also

- [[Alpha-Beta Pruning]]
- [[Expectimax]]
- [[Adversarial Search]]
