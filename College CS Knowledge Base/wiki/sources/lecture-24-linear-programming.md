---
title: "Lecture 24 — Linear Programming"
type: source
tags: [linear-programming, CSCE 411, lecture]
sources: []
course: CSCE 411
updated: 2026-04-09
---

Lecture 24 of [[CSCE 411]], taught by [[Calvin Beideman]]. Introduces [[Linear Programming]] as a problem formulation framework — what LPs are, what they can express, and the geometric structure of their feasible regions.

## Source File

`raw/Lecture24_Linear_Programming.pptx` — 12 slides

## Learning Objectives

- Understand what a linear program is.
- Become able to represent a problem using a linear program.

## Key Topics

### What is a Linear Program?

An LP has a linear objective function and linear constraints. *(Formal definition slide was visual — equations not captured in text extraction.)*

### What is NOT a Linear Program?

Products of variables, absolute values, quadratic terms, etc. are all non-linear. *(Examples were visual.)*

### LP for Max-Flow

Max-flow can be expressed as an LP: variables for flow on each edge, constraints for capacity and flow conservation, objective to maximize total flow. *(Full formulation was visual.)*

### Min-Cost Max-Flow

Extension: add per-edge costs to the max-flow LP and minimize total cost while achieving max flow. *(Visual slide.)*

### Feasibility and Boundedness

- **Feasible**: at least one vector satisfies all constraints.
- **Infeasible**: no vector satisfies all constraints.
- **Bounded**: a finite optimal value exists.
- **Unbounded**: objective can be made arbitrarily good (no finite optimum).

### Geometric Structure

- **Feasible Region**: convex polytope (set of all feasible points).
- **Convexity**: the feasible region is always convex for LPs.
- **Vertices**: corners of the feasible polytope; optimal solutions always occur at vertices.
- **Tight Constraints**: hold with equality at the current point.
- **Slack Constraints**: hold as strict inequalities.

*(Feasible region diagrams were visual — not captured in text extraction.)*

## See Also

- [[Linear Programming]]
- [[Simplex Algorithm]]
- [[Lecture 25 — Linear Programming (II)]]
- [[CSCE 411]]
