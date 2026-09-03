---
title: "Heuristic Search"
type: concept
tags: [csce420, search, heuristics, a-star, admissibility]
sources: [csce420-midterm-practice, csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Heuristic (informed) search uses domain knowledge to decide which node to expand next, in the form of an evaluation function. The standard form is

$$f(n) = g(n) + h(n)$$

where $g(n)$ is the known cost from the start node to $n$ and $h(n)$ is a heuristic estimate of the remaining cost from $n$ to a goal. Best-first search always expands the frontier node with smallest $f$.

## Key Properties

- **Admissible** — $h(n)$ never overestimates the true remaining cost. Admissibility is what makes [[A* Search]] optimal for tree search.
- **Consistent (monotone)** — $h(n) \le c(n, n') + h(n')$ for every successor $n'$. Consistency implies admissibility and gives optimality for graph search.
- **Complete** — finds a solution if one exists.
- **Optimal** — the solution found is a least-cost one.

## Contours

The geometric picture the course leans on: because $f$ increases as you move outward from the start, the set of nodes with $f(n) \le k$ forms a **contour** around the start node. [[A* Search]] expands nodes in order of increasing $f$, so it fills in contour by contour. In the midterm figure, distance from the initial node on the page is drawn proportional to $f$, so the f-contour is literally an arc.

This is the shared picture behind both [[A* Search]] and [[IDA*]] — the difference between them is not *which* nodes fall inside a contour but *how much of that contour you keep in memory*.

## The Space Problem

A* is complete and optimal, but keeps every generated node in memory, so its space complexity is exponential in the depth of the solution. Since it generates nodes faster than memory frees up, A* typically runs out of space long before it runs out of time. [[IDA*]] is the course's answer: re-run a depth-first search with an increasing f-limit, keeping only the current path.

| | Time | Space | Complete | Optimal |
|---|---|---|---|---|
| [[A* Search]] | Exponential | **Exponential** — all generated nodes | Yes | Yes (admissible $h$) |
| [[IDA*]] | Exponential (re-expands) | **Linear in current depth** — the call stack | Yes | Yes (admissible $h$) |

## From the Lecture

**Informed search** is defined as obtaining an evaluation function from domain knowledge. The lecture organises the whole family around [[Best-First Search]] — order nodes by evaluation-function value — with the members differing only in what that function is:

| Algorithm | Eval-Fn | Complete? | Optimal? |
|---|---|---|---|
| [[Uniform-Cost Search]] | $g(n)$ | Yes | Yes |
| [[Greedy Best-First Search]] | $h(n)$ | No | No |
| [[A* Search]] | $g(n) + h(n)$ | Yes | Yes (admissible $h$) |
| [[Beam Search]] | any, best $n$ kept | No | No |
| [[IDA*]] | $g(n)+h(n)$, bounded | Yes | Yes |

Greedy is fast but *incomplete and non-optimal*; A* fixes both by adding the cost already incurred.

The unit also covers **iterative improvement** — [[Hill Climbing]] and [[Simulated Annealing]] — which start from a complete configuration rather than searching for one. See [[Local Search]].

For heuristic design (admissibility, dominance, relaxation, composite heuristics), see [[Admissible Heuristics]].

## See Also

- [[A* Search]]
- [[IDA*]]
- [[Local Search]]
- [[Adversarial Search]]
- [[CSCE 420]]
