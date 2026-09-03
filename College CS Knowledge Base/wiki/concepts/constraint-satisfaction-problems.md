---
title: "Constraint Satisfaction Problems"
type: concept
tags: [csce420, csp, search, heuristics, map-coloring, backtracking]
sources: [csce420-midterm-practice, csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

A constraint satisfaction problem (CSP) is defined by a set of variables $X_1, \dots, X_n$, a domain $D_i$ of allowed values for each, and a set of constraints restricting which combinations are legal. A solution assigns every variable a value from its domain with no constraint violated. Unlike ordinary search, the *state has structure* — which lets CSP solvers use general-purpose heuristics that know nothing about the domain.

Canonical example: **map coloring**, where each region is a variable, the domain is a set of colors, and adjacent regions must differ.

## Solving by Backtracking

Depth-first assignment of one variable at a time, undoing an assignment when a constraint fails. Naive backtracking is slow; the standard accelerations are ordering heuristics.

## Ordering Heuristics

**Which variable to assign next?**

- **Minimum Remaining Values (MRV)** — choose the variable with the fewest legal values left. Fails fast: if a variable is about to have no options, find out now rather than after more work.
- **Degree heuristic** — tie-break by choosing the variable involved in the most constraints on remaining unassigned variables.

**Which value to try first?**

- **Least Constraining Value (LCV)** — choose the value that rules out the fewest choices for the *neighboring* variables in the constraint graph. This is the opposite bias from MRV, and deliberately so: pick the variable most likely to fail, but the value most likely to succeed.

## Worked Example (Midterm Practice, Problem 4)

The figure shows a rectangle split into four regions with $color \in \{Red, Green, Blue\}$: $v_1$ occupies the left, $v_2$ the upper middle, $v_3$ the lower middle, and $v_4$ the entire right column. Reading the borders, the adjacency graph is:

- $v_1 - v_2$, $v_1 - v_3$ (the slanted border)
- $v_2 - v_3$ (the short interior border)
- $v_2 - v_4$, $v_3 - v_4$ (the vertical border)
- $v_1$ and $v_4$ are **not** adjacent — the problem's note to "read the variable number carefully" points at exactly this.

Suppose $v_1 = \text{Red}$ and $v_2 = \text{Green}$, and $v_4$ is the next variable to assign. Then:

- $v_3$ is adjacent to $v_1$ (Red) and $v_2$ (Green), so its only remaining value is **Blue**.
- $v_4$ is adjacent to $v_2$ (Green) and $v_3$, so its candidate values are Red and Blue.

Applying LCV to $v_4$:

| Value for $v_4$ | Values left for $v_3$ | Choices eliminated |
|---|---|---|
| Blue | none — $v_3$ has no legal value | fatal |
| **Red** | {Blue} | fewest |

So LCV selects **Red** for $v_4$: it is the value that leaves neighbors the most room. Choosing Blue would wipe out $v_3$'s last option and force a backtrack.

> Worked here from the figure; the practice exam ships without an answer key.

## From the Lecture

### CSP as a Search Problem

Mapped onto [[Search Problem Formulation]]:

- **State**: values of a set of variables
- **Goal**: test whether a set of constraints is met
- **Operators**: set values of variables

General search works, but **specialized CSP solvers work better** — because the goal decomposes into separate constraints rather than being a monolithic test, so constraints can prune the branching factor as you go.

### Kinds of Constraints

- **Unary, binary, higher-order** — how many variables must simultaneously satisfy it
- **Absolute vs. preference** constraints
- Variables have a **domain**, discrete or continuous, fixing the possible values

The lecture situates CSP inside the broader **constrained optimization** problems of operations research — a cost function plus constraints, which may be linear, nonlinear, convex, or nonconvex. Straightforward solutions exist only for limited subclasses; linear programs, for instance, yield to the simplex method. See [[Linear Programming]].

### Complexity

CSPs include **NP-complete** problems such as 3-SAT, so finding solutions can require exponential time.

### Two Solving Strategies

| Strategy | Behavior |
|---|---|
| **Backtracking** | Back up when a constraint is violated |
| **Forward checking** | Do not expand further if look-ahead reveals a violation |

**Forward checking is often faster and simple to implement** — it detects failure earlier, before descending into a doomed subtree.

### The Three Ordering Heuristics

For **variable selection**:

- **Most-constrained-variable** — pick the variable with fewest remaining values
- **Most-constraining-variable** — pick the variable involved in the most constraints

For **value assignment**:

- **Least-constraining-value** — pick the value ruling out the fewest values for other variables

The underlying tension the lecture names: **reducing the branching factor now vs. leaving freedom for future choices.** Variable heuristics pursue the first (fail fast on the hardest variable); the value heuristic pursues the second (keep options open).

## See Also

- [[Local Search]]
- [[Heuristic Search]]
- [[Backtracking]]
- [[CSCE 420]]
