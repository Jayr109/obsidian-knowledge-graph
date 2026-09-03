---
title: "A* Search"
type: algorithm
tags: [csce420, search, heuristics, optimality, best-first]
sources: [csce420-midterm-practice, csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

A* is best-first search using $f(n) = g(n) + h(n)$: expand the frontier node whose estimated total path cost is smallest. With an admissible heuristic it is **complete and optimal**. Its fatal practical weakness is memory: it stores every generated node, so space is exponential.

## Algorithm

1. Put the start node on the frontier (a priority queue keyed by $f$).
2. Pop the node with lowest $f$. If it is a goal, return the path.
3. Expand it; for each successor compute $f = g + h$ and add it to the frontier.
4. Keep an explored set to avoid re-expanding states.
5. Repeat until the frontier is empty (failure).

## Complexity

| | |
|---|---|
| Time | Exponential in solution depth (better with a sharper $h$) |
| Space | **Exponential** — all generated nodes stay in memory |
| Complete | Yes |
| Optimal | Yes, with admissible $h$ (tree search) or consistent $h$ (graph search) |

Space is the binding constraint. A* generates nodes far faster than any practical machine can store them, which is the entire motivation for [[IDA*]].

## What Stays in Memory (Midterm Practice, Problem 2)

The figure shows a tree rooted at A, drawn so that distance from A is proportional to $f$, with a red arc marking the current f-contour. Structure:

- A → B, C
- B → D, E
- D → F, G
- E → H, I
- C → J, K, L

Visit order is A, B, D, E, C, and the current node is C.

**A\*** keeps everything it has generated — both the explored nodes and the entire frontier. By the time C is the current node, A, B, D, E have been expanded and their children generated, so memory holds essentially every node inside and on the f-contour: **A, B, C, D, E, F, G, H, I** — the explored set plus the frontier siblings. This is the whole shaded region under the arc, and it grows exponentially with depth.

**IDA\*** keeps only the recursion stack of the current DFS-CONTOUR call. The path from the root to C is A → C, so memory holds only **A and C** (plus, depending on implementation, the sibling children of nodes on that path awaiting their turn in the loop). Everything under B was explored and discarded when the recursive call returned.

The contrast is the point of the problem: A* memory grows with the *area* under the contour, IDA* memory grows with the *depth* of the current path.

> Worked here from the figure; the practice exam ships without an answer key.

## From the Lecture

The lecture introduces A* as **"Uniform Cost + Heuristic Search"** — the point being that $g(n)$ was already present in [[Uniform-Cost Search]] and $h(n)$ already present in [[Greedy Best-First Search]]; A* is their combination, and only the combination is both complete and optimal.

```
function A*-Search (problem)
  g(n): current cost up till n
  h(n): estimated cost from n to goal
  return Best-First-Search(problem, g + h)
```

### The Romania Comparison

On the Arad-to-Bucharest map, greedy best-first returns a path costing **450**; A* returns **418**, routing through Rimnicu Vilcea and Pitesti. The eight-unit gap is the whole argument for retaining $g(n)$: Fagaras *looks* closer to Bucharest, but the road through it is longer.

### The Optimality Argument

A node $n$ on the way to the optimal goal $G_1$ is visited before a suboptimal goal $G_2$:

$$f(n) = g(n) + h(n) \le g(n) + h^*(n) = f(G_1)$$

Since $f(G_1) < f(G_2)$, it follows that $f(n) < f(G_2)$ — so $n$ is always visited first. The inequality holds precisely because $h$ is admissible, i.e. $h^*(n) \ge h(n)$.

**Lemma**: A* visits nodes in order of increasing $f(n)$, gradually adding **$f$-contours** just as [[Breadth-First Search]] adds depth layers. If the goal has value $f^*$, then **every node with $f < f^*$ will be visited** — which is exactly why a larger admissible $h$ means less work. See [[Admissible Heuristics]].

### Monotonicity and Pathmax

Usually $f$ never decreases along a path (**monotonicity**). Where it does — $f(\text{Child}) < f(\text{Parent})$ — apply the **pathmax** correction:

$$f(\text{Child}) = \max\big(f(\text{Parent}),\; g(\text{Child}) + h(\text{Child})\big)$$

### The Condition for Subexponential Growth

A* is complete and optimal, but space is exponential unless the heuristic is very good. The stated condition:

$$|h(n) - h^*(n)| \le O(\log h^*(n))$$

That is, the error must grow **less than linearly** in the true remaining cost. The lecture's verdict is pessimistic: for most heuristics the error is at least proportional to the true cost, i.e. $\ge O(h^*(n)) > O(\log h^*(n))$. So exponential space is the normal case, not the exception — which is the motivation for [[IDA*]].

### Repeated States and Optimality

Two options, both problematic, from the lecture's worked graph:

1. **Visit of parent disallowed** — search can outright fail at some nodes.
2. **Visit of parent allowed** — paths through those nodes carry an inflated $g(n)$ and become non-optimal rather than wrong.

See [[Repeated States]].

## See Also

- [[IDA*]]
- [[Heuristic Search]]
- [[Local Search]]
- [[CSCE 420]]
