---
title: "Lecture 25 — Linear Programming (II)"
type: source
tags: [linear-programming, simplex, CSCE 411, lecture]
sources: []
course: CSCE 411
updated: 2026-04-09
---

Lecture 25 of [[CSCE 411]], taught by [[Calvin Beideman]]. Continues [[Linear Programming]], covering conversion to standard/equational form, the [[Simplex Algorithm]], LP duality, and other LP algorithms.

## Source File

`raw/Lecture25_LP_Pt2.pptx` — 21 slides

## Learning Objectives

- Convert a linear program to standard or equational form.
- Solve a linear program using the simplex method.
- Understand how to compute the dual of a linear program.
- Know the weak and strong duality theorems.

## Key Topics

### Review: Feasible Regions and Vertices

Recap of [[Lecture 24 — Linear Programming]]: feasible region is convex, optimal solutions occur at vertices.

### Standard (Canonical) Form

Maximize cᵀx subject to Ax ≤ b, x ≥ 0.

**Theorem**: Every LP can be converted to standard form.
- Minimization → multiply objective by -1.
- Unbounded variables → substitute xᵢ = xᵢ⁺ - xᵢ⁻, both ≥ 0.

*(Additional conversion details were visual.)*

### Equational Form

Maximize cᵀx subject to Ax = b, x ≥ 0.

Convert from standard by introducing slack variables s: Ax + s = b, s ≥ 0.

### Simplex Algorithm (Dantzig, 1947)

Key insight: feasible region is convex → no local maxima → adjacent vertex always improves objective if not yet at optimum.

Algorithm walks vertices (Basic Feasible Solutions) via **pivots** — swapping one basic variable for one nonbasic variable.

Visual example traversal:
```
(-3, 3) → value -6
(-3, 1) → value -4
( 0,-2) → value  2
( 4, 0) → value  4  ← optimal
```

See [[Simplex Algorithm]] for full detail including BFS definition, pivot mechanics, and finding the first BFS.

### LP Duality

Every primal LP has a dual LP.
- **Weak Duality**: primal objective ≤ dual objective (for max primal).
- **Strong Duality**: if both primal and dual are feasible, optimal values are equal.

*(Dual construction and proof details were visual.)*

### Other LP Algorithms

- **Ellipsoid Algorithm**: first polynomial worst-case LP algorithm.
- **Interior Point Methods**: polynomial; competitive with Simplex in practice.

## See Also

- [[Linear Programming]]
- [[Simplex Algorithm]]
- [[Lecture 24 — Linear Programming]]
- [[CSCE 411]]
