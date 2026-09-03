---
title: "Lecture 19 — Dynamic Programming (I)"
type: source
tags: [dynamic-programming, memoization, tabulation, lis, bottom-up, top-down]
sources: [lecture-19-dynamic-programming-1]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 19 — Dynamic Programming (I)

CSCE 411, Calvin Beideman, 14 slides.

## Recap: Backtracking → Memoization → DP

The progression from lecture 18:
1. Recursive backtracking — correct but exponential
2. Add memoization — correct and polynomial (when subproblem count is polynomial)
3. Convert to bottom-up iterative table — DP

---

## Top-Down DP (Memoization)

Add a memo table to the recursive algorithm. Before computing a subproblem, check if its answer is already in the table.

**Advantage**: only computes subproblems that are actually needed (e.g., for a yes/no Subset Sum problem, may terminate early).

---

## Bottom-Up DP (Tabulation)

Fill the DP table iteratively in dependency order (compute smaller subproblems before larger ones). No recursion overhead, no stack overflow risk.

**Usually faster in practice** than top-down.

**Focus of CSCE 411**: bottom-up DP.

---

## DP Design Framework

### Step 1: Formulate Recursively
- Define subproblems precisely
- Write the recurrence relation
- Specify the base case(s)
- Explain how the original answer is obtained from subproblem answers

### Step 2: Build Bottom-Up
- Identify all subproblems
- Choose the memoization data structure (array, 2D array, map, etc.)
- Determine evaluation order (so dependencies are computed before they're needed)
- Analyze runtime

### Step 3: Runtime Analysis
```
Runtime = (# subproblems) × (work per subproblem, excluding recursive calls)
```

---

## LIS Revisited

Two formulations of LIS DP:

**2-parameter**: LIS(i, j) = length of LIS ending at index i, with previous element at index j. More subproblems but straightforward.

**1-parameter**: LIS(i) = length of LIS ending at index i. Fewer subproblems; the recurrence requires a max over valid predecessors.

---

## MemoFib Runtime

`MemoFib(n)`:
- Time: O(n) — n distinct subproblems, O(1) work each
- Space: O(n) — memo table of size n

---

## See Also

- [[Dynamic Programming]]
- [[Longest Increasing Subsequence]]
- [[CSCE 411]]
