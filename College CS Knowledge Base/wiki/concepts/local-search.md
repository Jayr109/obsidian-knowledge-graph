---
title: "Local Search"
type: concept
tags: [csce420, search, optimization, hill-climbing, simulated-annealing]
sources: [csce420-midterm-practice, csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Local search abandons the search tree entirely. Instead of building paths from a start state, it keeps a single current state and moves to a neighbor, using constant memory. The path to the goal is irrelevant — only the final state matters. This suits optimization problems (n-queens, VLSI layout, scheduling) where the goal is a good configuration, not a route.

## Hill Climbing

Repeatedly move to the best-valued neighbor; stop when no neighbor is better. Simple and memory-cheap, but it gets stuck on:

- **Local maxima** — every neighbor is worse, but the global optimum is elsewhere
- **Plateaus / shoulders** — flat regions where no move improves anything
- **Ridges** — a sequence of local maxima that no single move can traverse

Every one of these is a consequence of the same rule: never accept a worse move.

## Escaping Local Optima

The fix is to sometimes accept a worse move. [[Simulated Annealing]] does this with a temperature-controlled probability, borrowing the metallurgical annealing schedule: accept bad moves freely at high temperature, then cool until the search behaves like hill climbing.

Other approaches in this family: random-restart hill climbing (run many times from random starts), local beam search (keep $k$ states), and genetic algorithms (recombine states) — the latter appearing in the [[History of AI]] timeline in the 1960s.

## From the Lecture

The lecture files these under **iterative improvement algorithms**: start with a *complete configuration* — all variables assigned — and gradually improve it, rather than constructing a solution by search.

Members: [[Hill Climbing]] (maximize a cost function), **gradient descent** (minimize one), and [[Simulated Annealing]] (probabilistic).

This suits domains where **all nodes are solutions** and the goal is to improve solution quality — optimization problems.

### Hill Climbing's Three Failure Modes

| Problem | Description |
|---|---|
| **Local maxima** | A peak below the global one; all neighbours worse |
| **Plateau** | A flat region giving no gradient signal |
| **Ridge** | A narrow ascending path no single step can follow |

**Hardness depends on the shape of the landscape** — the algorithm is fixed, so all difficulty is topological.

### Remedies

- **Random restart** — move to a random point and search again
- **Keep $n$ best nodes** — [[Beam Search]]
- **Parallel search**
- **[[Simulated Annealing]]** — the principled fix

A distinction worth keeping: hill climbing keeps **no queue**, only the current best node, and does not backtrack. That makes it different from [[Greedy Best-First Search]], which is also greedy but does maintain a node list to return to.

## See Also

- [[Simulated Annealing]]
- [[Heuristic Search]]
- [[Constraint Satisfaction Problems]]
