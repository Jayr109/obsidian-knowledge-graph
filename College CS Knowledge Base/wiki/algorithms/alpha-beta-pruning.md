---
title: "Alpha-Beta Pruning"
type: algorithm
tags: [csce420, games, adversarial-search, pruning, minimax]
sources: [csce420-midterm-practice, csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Alpha-beta pruning computes the exact [[Minimax]] value while skipping subtrees that provably cannot influence it. It carries two bounds down the recursion:

- $\alpha$ — the best (highest) value found so far along the path for MAX; a lower bound on the root value
- $\beta$ — the best (lowest) value found so far along the path for MIN; an upper bound

Both start at $\alpha = -\infty$, $\beta = +\infty$ at the root.

## Cutoff Rule

At any node, once $\alpha \ge \beta$, stop expanding the remaining children and return. The reasoning: MIN already has an option at or below what MAX has already secured elsewhere, so MAX will never let play reach this node — whatever the unexamined children hold cannot matter.

- At a **MAX** node: update $\alpha \leftarrow \max(\alpha, \text{value})$; cut when $\alpha \ge \beta$.
- At a **MIN** node: update $\beta \leftarrow \min(\beta, \text{value})$; cut when $\beta \le \alpha$.

The value returned at the root is identical to plain minimax. Only the node count changes: $O(b^{d/2})$ with perfect move ordering, versus $O(b^d)$ without pruning — which doubles the depth reachable in fixed time.

## The Infinite-Bound Test

A cut requires comparing $\alpha$ against $\beta$ where **both are finite**. If a node still holds an inherited $\beta = +\infty$ (because no sibling has been evaluated yet on the MIN side above it), then $\alpha \ge \beta$ can never hold for finite values, and no cut is possible there regardless of the numbers. This is the trick the midterm problem tests.

## Worked Example (Midterm Practice, Problem 6)

Tree structure, with △ = MAX and ▽ = MIN, all of $X, Y, Z, W, A, B$ finite:

```
                 △  root
                /  \
          ▽ X       ▽ N
                   /   \
                △ M     △ B
               /   \
          ▽ W       ▽ A      ← CUT #2 on this edge
         /   \
     △ Y      △ Z            ← CUT #1 on this edge
```

Trace with $\alpha = -\infty$, $\beta = +\infty$ at the root:

1. Root (MAX) evaluates its first child, the leaf $X$. Root sets $\alpha = X$ — **finite**.
2. Root's second child $N$ (MIN) inherits $\alpha = X$, $\beta = +\infty$.
3. $N$'s first child $M$ (MAX) inherits $\alpha = X$, $\beta = +\infty$.
4. $M$'s first child $W$ (MIN) inherits $\alpha = X$, $\beta = +\infty$.
5. $W$ evaluates its first child $Y$, setting $\beta = Y$ — **finite**.

**CUT #1** is the cut at $W$ before evaluating $Z$. The test is $\beta \le \alpha$, i.e. $Y \le X$ — a comparison **between two finite values**. It can therefore fire, and the note in the problem ("$W = Y$ in case of cut, or $W = \min(Y,Z)$ otherwise") describes exactly this outcome. **Cut #1 is possible.**

**CUT #2** is the cut at $M$ before evaluating $A$. After $W$ returns, $M$ sets $\alpha = \max(X, W)$ — finite — but $M$'s $\beta$ is still the inherited $+\infty$, because $M$ is $N$'s *first* child and no sibling value has come back to tighten it. The test $\alpha \ge \beta$ becomes finite $\ge +\infty$, which never holds. **Cut #2 is impossible.**

**Answer: Cut #1 only.**

> Worked here from the figure; the practice exam ships without an answer key.

## From the Lecture

### The Two Cuts, Stated Directly

- **$\alpha$ = best MAX value so far.** When the current max exceeds a successor's min value, stop exploring that MIN subtree — it can only get worse for MAX.
- **$\beta$ = best MIN value so far.** When the current min is below a successor's max value, stop exploring that MAX subtree.

Initialize along the path from the root: $\alpha \leftarrow -\infty$, $\beta \leftarrow +\infty$.

### The Algorithms

```
function Max-Value (state, game, alpha, beta) returns utility value
  if Cutoff(state) then return Utility(state)
  v <- -infinity
  for each s in Successor(state) do
    v <- Max(v, Min-Value(s, game, alpha, beta))
    if v >= beta then return v            /* beta CUT */
    alpha <- Max(alpha, v)
  return v

function Min-Value (state, game, alpha, beta) returns utility value
  if Cutoff(state) then return Utility(state)
  v <- +infinity
  for each s in Successor(state) do
    v <- Min(v, Max-Value(s, game, alpha, beta))
    if v <= alpha then return v           /* alpha CUT */
    beta <- Min(beta, v)
  return v
```

### The Symmetry Worth Memorizing

| At a node | Updates | Cuts when | Returns if no cut |
|---|---|---|---|
| **MAX** | only $\alpha$ | $v \ge \beta$ | max of successors |
| **MIN** | only $\beta$ | $v \le \alpha$ | min of successors |

Each node type updates *its own* bound and tests against the *other* one. Mixing these up is the most common error.

### Properties

- **Pruning does not affect the final result** — it is exact, not approximate
- **Good move ordering improves effectiveness**
- With perfect ordering, time complexity is $b^{m/2}$ — which **doubles the searchable depth**

Since $b^{m/2} = (\sqrt{b})^m$, chess's $b = 35$ effectively becomes $\sqrt{35} \approx 6$, easily reaching 8-ply.

### Ordering Direction

- For **MIN**, sort successors' utilities in **increasing** order
- For **MAX**, sort in **decreasing** order

In both cases: examine the move most likely to cause a cut first.

## See Also

- [[Minimax]]
- [[Expectimax]]
- [[Adversarial Search]]
