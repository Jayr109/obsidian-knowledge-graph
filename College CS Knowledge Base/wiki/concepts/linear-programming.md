---
title: "Linear Programming"
type: concept
tags: [linear-programming, optimization, algorithms]
sources: [lecture-24-linear-programming, lecture-25-linear-programming-2]
course: CSCE 411
updated: 2026-04-09
---

Linear programming (LP) is a method for optimizing a linear objective function subject to linear constraints. It is one of the most broadly applicable tools in optimization, capable of expressing problems like max-flow, min-cost flow, and many scheduling problems.

## What is a Linear Program?

An LP consists of:
- A **linear objective function** to maximize (or minimize): e.g., maximize cᵀx
- **Linear constraints**: Ax ≤ b (inequalities) or Ax = b (equalities)
- **Nonnegativity constraints**: x ≥ 0 (in standard form)

**What is NOT a linear program:** any objective or constraint that is nonlinear — products of variables, absolute values, quadratic terms, etc.

## Key Properties

**Feasibility**: An LP is feasible if at least one vector x satisfies all constraints; infeasible otherwise.

**Boundedness**: An LP is bounded if the objective function has a finite optimal value; unbounded if the objective can be made arbitrarily large (or small for minimization).

**Feasible Region**: The set of all vectors satisfying the constraints. For LPs, this is always a **convex polytope** (or empty if infeasible).

**Vertices (Basic Feasible Solutions)**: Optimal solutions to LPs, if they exist, always occur at vertices of the feasible region. The [[Simplex Algorithm]] exploits this.

**Tight vs. Slack Constraints**: A constraint is tight (active) at a point if it holds with equality; slack if the inequality is strict.

## Standard (Canonical) Form

Maximize cᵀx subject to Ax ≤ b, x ≥ 0.

Every LP can be converted to standard form:
- **Minimization → Maximization**: multiply objective by -1
- **Unbounded variables**: replace xᵢ with xᵢ⁺ - xᵢ⁻ where both ≥ 0

## Equational Form

Maximize cᵀx subject to Ax = b, x ≥ 0.

Convert from standard form by introducing **slack variables**: replace Ax ≤ b with Ax + s = b, s ≥ 0.

## Applications

- **Max-Flow**: LP can express max-flow as a linear program over flow variables with capacity and conservation constraints.
- **Min-Cost Max-Flow**: extends max-flow LP with a cost objective.

## LP Duality

Every LP (primal) has a corresponding **dual LP**. Key theorems:
- **Weak Duality**: the primal objective value ≤ dual objective value (for maximization primal).
- **Strong Duality**: if both primal and dual are feasible, their optimal values are equal.
- **Dual of a feasible LP may be infeasible**: feasibility of P does not guarantee feasibility of the dual. (Exam 3 T/F, item j.)
- **Not every optimal solution is at a vertex**: at least one optimal occurs at a vertex; but if the optimal face is a continuum, non-vertex optima exist too. (Exam 3 T/F, item i.)

*(Visual content from Lecture 25 slides not fully captured in text extraction.)*

### Dual Construction Procedure (Standard Form)

Given primal in standard form (maximize cᵀx, Ax ≤ b, x ≥ 0):
1. One dual variable yᵢ per primal constraint.
2. Dual objective: **minimize** bᵀy.
3. One dual constraint per primal variable xⱼ: Σᵢ Aᵢⱼ yᵢ ≥ cⱼ.
4. Dual non-negativity: y ≥ 0.

**Worked example** (Exam 3 Q2): primal with 3 constraints → 3 dual variables y₁,y₂,y₃; dual objective minimizes 14y₁ + 8y₂ + 12y₃ (the RHS values of primal constraints). See [[Exam 3 Solutions — Spring 2026]] Q2 for the full construction.

### Duality and Combinatorial Problems

LP duality can reveal surprising identities between combinatorial problems:
- The dual of the bipartite matching LP is the minimum vertex cover LP.
- By strong duality + integrality: **max bipartite matching = min vertex cover** ([[König's Theorem]]).

See [[LP Relaxation]] for when LP optima are integral, and when LP relaxations equal their IP counterparts.

## Algorithms

- [[Simplex Algorithm]] — walks vertices of the feasible polytope; exponential worst case but fast in practice
- Ellipsoid Algorithm — polynomial worst case (theoretical importance)
- Interior Point Methods — polynomial; competitive with Simplex in practice

## See Also

- [[Simplex Algorithm]]
- [[LP Relaxation]]
- [[König's Theorem]]
- [[Bipartite Matching]]
- [[Vertex Cover]]
- [[Exam 3 Solutions — Spring 2026]]
- [[Homework 7 Solutions — Spring 2026]]
- [[CSCE 411]]
