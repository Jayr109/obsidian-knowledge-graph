---
title: "Hill Climbing"
type: algorithm
tags: [csce420, hill-climbing, iterative-improvement, local-maxima, optimization]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Hill climbing is the basic **iterative improvement** algorithm: start from a complete configuration and repeatedly move to a better neighbour, keeping only the current best node. It maximizes an objective; **gradient descent** is the same algorithm minimizing a cost function.

## Iterative Improvement

The class of algorithms starts with a **complete configuration** — all variables assigned — and gradually improves it, rather than building a solution incrementally by search. Members: hill climbing, gradient descent, and [[Simulated Annealing]].

This suits domains where **all nodes are solutions** and the goal is to improve solution *quality* — i.e. optimization problems.

## The Algorithm

- **No queue** — keep only the best node
- **Greedy, no backtracking**

Note the contrast the lecture draws: hill climbing is *different from* [[Greedy Best-First Search]], which uses a heuristic function but does maintain a node list. Hill climbing keeps nothing to return to.

## Three Failure Modes

| Problem | What it looks like |
|---|---|
| **Local maxima** | A peak lower than the global one; every neighbour is worse, so the search stops |
| **Plateau** | A flat region; no neighbour is better, so there is no signal to follow |
| **Ridge** | A narrow ascending path that no single-step move can follow |

**Hardness depends on the shape of the landscape** — the algorithm is fixed, so all the difficulty lives in the objective's topology.

## Remedies

- **Random restart** — jump to a random point in the landscape and search again
- **Keep $n$ best nodes** — [[Beam Search]]
- **Parallel search**
- **[[Simulated Annealing]]** — allow downhill moves with a probability that decreases over time

Simulated annealing is the principled fix: rather than avoiding local maxima by luck (restart) or by breadth (beam), it makes escape a controlled property of the search itself.

## See Also

- [[Simulated Annealing]]
- [[Local Search]]
- [[Beam Search]]
- [[Greedy Best-First Search]]
- [[CSCE 420]]
