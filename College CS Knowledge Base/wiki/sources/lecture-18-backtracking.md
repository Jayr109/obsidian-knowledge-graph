---
title: "Lecture 18 — Recursive Backtracking"
type: source
tags: [backtracking, dynamic-programming, memoization, lis, recursion]
sources: [lecture-18-backtracking]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 18 — Recursive Backtracking

CSCE 411, Calvin Beideman, 22 slides.

## Substrings vs Subsequences

- **Substring**: contiguous sequence of characters/elements
- **Subsequence**: elements in order but not necessarily contiguous

---

## LIS as Motivating Example

**LIS (Longest Increasing Subsequence)**: find the longest subsequence of an array where elements are strictly increasing.

**Greedy fails**: counterexamples show greedy strategies don't work:
- [2, 3, 1] — greedy might commit to wrong prefix
- [3, 1, 2] — locally optimal early choices block longer solutions

---

## Recursive Backtracking

For problems requiring a sequence of decisions: try all choices, backtrack on failure, return the best result. Pass a minimal "summary of choices so far" to recursive calls.

**Two views of LIS**:
1. Choose which element comes next in the subsequence
2. For each element, decide to include it or skip it

Both formulations are correct but both are O(2ⁿ) — exponential.

---

## Memoization

Avoid recomputing the same subproblems by storing answers in a table. Before computing, check if the answer is already stored.

**Key insight**:
```
Runtime = (# distinct subproblems) × (work per subproblem)
```

**Fibonacci example**:
- Naive recursion: O(2ⁿ) — recomputes same values exponentially many times
- Memoized: O(n) — each subproblem computed exactly once

---

## Dynamic Programming = Recursive Backtracking + Memoization

DP converts exponential backtracking into polynomial time **when the number of distinct subproblems is polynomial**.

### DP Design Steps

1. **Specification**: what problem does each subproblem solve? Define clearly.
2. **Pseudocode**: write recursive solution with base case.
3. **Solution**: determine which subproblem input gives the answer to the original problem.

---

## See Also

- [[Dynamic Programming]]
- [[Longest Increasing Subsequence]]
- [[Subset Sum]]
- [[CSCE 411]]
