---
title: "Simplex Algorithm"
type: algorithm
tags: [linear-programming, optimization, algorithms]
sources: [lecture-25-linear-programming-2]
course: CSCE 411
updated: 2026-04-09
---

The Simplex Algorithm (Dantzig, 1947) is the foundational method for solving [[Linear Programming|linear programs]]. It walks along the vertices (Basic Feasible Solutions) of the convex feasible polytope, improving the objective value at each step, until it reaches the optimum.

## Core Idea

Because the feasible region of an LP is convex, there are no local optima — any non-optimal vertex has at least one adjacent vertex with a better objective value. The Simplex algorithm exploits this:

> If we are not at the optimal solution, all points between our current vertex and the optimal vertex must be feasible. Therefore, at least one adjacent vertex will improve our objective value.

The algorithm never gets stuck in a local maximum.

## Working with Equational Form

Simplex operates on LPs in **equational form**: Ax = b, x ≥ 0 (see [[Linear Programming]] for conversion).

**Basic Feasible Solution (BFS)**: A vertex of the feasible polytope in equational form. For a system with m equality constraints and n variables, a BFS has exactly m basic variables (nonzero) and n-m nonbasic variables (zero). The basic variables are determined by solving the system with the nonbasic variables set to 0.

## Pivoting

A **pivot** moves from one BFS to an adjacent BFS by:
1. Selecting a nonbasic variable to become basic (enters the basis — improves objective).
2. Selecting a basic variable to become nonbasic (leaves the basis — maintains feasibility).
3. Updating the tableau via row operations.

## Visual Intuition (from Lecture 25)

Example traversal on a 2D LP:
```
(-3, 3) → objective value -6
(-3, 1) → objective value -4
( 0,-2) → objective value  2
( 4, 0) → objective value  4  ← optimal
```
The initial choice of pivot direction (clockwise vs. counterclockwise) was arbitrary — both directions improve the objective.

## Complexity

- **Worst case**: exponential (pathological inputs like Klee-Minty cube can cause cycling through all 2ⁿ vertices).
- **Average case / practice**: extremely fast; one of the most widely used algorithms in practice.

## Finding the First BFS

A non-trivial step: requires an auxiliary LP or Phase I simplex to find an initial feasible vertex.

## Other LP Algorithms

- **Ellipsoid Algorithm**: first polynomial-time LP algorithm (theoretical importance, slow in practice).
- **Interior Point Methods**: polynomial; competitive with Simplex on large instances; works from the interior of the feasible region rather than along vertices.

## See Also

- [[Linear Programming]]
- [[CSCE 411]]
