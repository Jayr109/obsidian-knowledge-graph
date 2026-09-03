---
title: "Dynamic Programming"
type: concept
tags: [dynamic-programming, optimization, algorithms]
sources: [lecture-20-dynamic-programming-2, lecture-22-graph-dp]
course: CSCE 411
updated: 2026-04-09
---

Dynamic programming (DP) is an algorithm design technique for solving optimization problems by breaking them into overlapping subproblems, solving each subproblem once, and storing results (memoization or tabulation) to avoid redundant recomputation. It requires **optimal substructure**: an optimal solution must be constructible from optimal solutions to subproblems.

## When to Use DP

DP applies when:
1. **Optimal substructure** — the problem's optimal solution contains optimal solutions to subproblems.
2. **Overlapping subproblems** — the same subproblems recur many times (distinguishes DP from divide & conquer, where subproblems are disjoint).

## Comparison with Other Paradigms

| Paradigm | Subproblems | Approach |
|---|---|---|
| Divide & Conquer | Disjoint | Solve all, combine |
| Dynamic Programming | Overlapping | Solve all, memoize |
| [[Greedy Algorithms\|Greedy]] | Overlapping | Solve only 1 (greedy choice) |

All three rely on optimal substructure. The key question is whether the greedy choice property holds — if yes, greedy suffices; if no, DP is needed.

## Design Process (CSCE 411 Framework)

1. Define the subproblems.
2. Write a recurrence relating subproblems.
3. Specify base cases.
4. Determine evaluation order (bottom-up) or use memoization (top-down).
5. Recover the solution (backtracking through memoized table).

## Algorithms Covered in CSCE 411

- [[Longest Increasing Subsequence]] — 1D array DP; O(n²) or O(n log n)
- [[Subset Sum]] — 2D table DP; pseudopolynomial time
- Cherry Collecting — 2D grid, two robots, simultaneous movement
- [[Floyd-Warshall]] — all-pairs shortest paths; O(V³)
- [[Maximum Weight Independent Set]] in trees — tree DP via subtree subproblems
- [[Longest Valley Subsequence]] — 2D anchor-both-ends DP; O(n³); Final Exam Q4

## Choosing Subproblems for Graph DP

When the input is a graph (not an array), natural subproblems must exploit structure:
- For general graphs: subarrays of adjacency matrix/list (used by [[Floyd-Warshall]])
- For trees: subtrees rooted at each node (used by [[Maximum Weight Independent Set]])

## See Also

- [[Greedy Algorithms]]
- [[Graph DP]]
- [[Floyd-Warshall]]
- [[Longest Increasing Subsequence]]
- [[Subset Sum]]
- [[Maximum Weight Independent Set]]
- [[CSCE 411]]
