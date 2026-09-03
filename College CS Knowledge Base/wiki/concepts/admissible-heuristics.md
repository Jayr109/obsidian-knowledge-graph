---
title: "Admissible Heuristics"
type: concept
tags: [csce420, heuristics, admissibility, dominance, relaxation]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

A heuristic $h(n)$ estimates the cost of the cheapest path from node $n$ to a goal. It is **admissible** if it never overestimates that cost — the condition [[A* Search]] requires for optimality. Beyond admissibility, the practical question is how to design heuristics that are as *large* as possible without crossing the line.

## Definition and Requirement

$h(n)$ = estimated cost of the cheapest path from the state at node $n$ to a goal state.

The only strict requirement is that **$h(n) = 0$ at the goal**. Admissibility — never overestimating the true cost $h^*(n)$ — is the additional condition A* needs.

> "Heuristics" means *to find* or *to discover*, or more technically *how to solve problems* (Polya, 1957).

## Example: Straight-Line Distance

For route finding, $h_{SLD}(n)$ — straight-line distance to the goal — is admissible because no road can be shorter than the direct line. It requires domain knowledge: coordinates for each city, plus the general fact that cities toward the goal have smaller SLD.

## Example: The 8-Puzzle

Two admissible heuristics:

- $h_1(n)$ = number of misplaced tiles
- $h_2(n)$ = total Manhattan (city-block) distance

For a sample state, $h_1(n) = 7$ (not counting the blank) and $h_2(n) = 2+3+3+2+4+2+0+2 = 18$.

## Dominance

If $h_2(n) \ge h_1(n)$ for all $n$ and both are admissible, then **$h_2$ dominates $h_1$** and is better for search.

Measured search cost at solution depth $d = 14$:

| Method | Nodes visited |
|---|---|
| [[Iterative Deepening Search]] | 3,473,941 |
| A* with $h_1$ | 539 |
| A* with $h_2$ | 113 |

**Why bigger is better**: A* visits every node with $f < f^*$. Since $f = g + h$, the visited set is $\{n : h(n) < f^* - g(n)\}$ — so a **larger $h$ shrinks the set of visited nodes**. Admissibility caps how large $h$ may be; dominance says get as close to that cap as possible.

## Designing Heuristics by Relaxation

The systematic method: **relax the problem** — remove constraints — and use the exact cost of the relaxed problem as the heuristic. A relaxed problem is easier, so its cost is a lower bound, so the heuristic is admissible by construction.

| Problem | Relaxation | Heuristic |
|---|---|---|
| 8-puzzle | Tiles may move anywhere | $h_1$ (misplaced tiles) |
| 8-puzzle | Tiles may move to any adjacent location | $h_2$ (Manhattan distance) |
| Travel | Traveller may go by air, not just road | Straight-line distance |

## Other Design Methods

- **Composite heuristics**: $h(n) = \max(h_1(n), \dots, h_m(n))$ — the max of admissible heuristics is admissible and dominates each.
- **Statistical information**: sample $h$ against true cost to goal and learn how they relate.

## See Also

- [[A* Search]]
- [[Greedy Best-First Search]]
- [[IDA*]]
- [[Heuristic Search]]
- [[CSCE 420]]
