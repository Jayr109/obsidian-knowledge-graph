---
title: "Practice — Dynamic Programming"
type: source
tags: [csce411, practice, dynamic-programming, lis, subsequence]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Practice — Dynamic Programming

**Source file:** `raw/CSCE_411_Dynamic_Programming_Practice_Solutions (2).pdf`
**Course:** CSCE 411, Spring 2026
**Topics:** DP design, Longest Decreasing Subsequence (variant of LIS)

## DP Design Framework (Recap)

Three-step process for DP problems:

1. **Formulate recursively:**
   - Define the subproblems clearly
   - Write the recurrence with base cases
   - Explain how the final answer is obtained from subproblems

2. **Build bottom-up:**
   - Identify all subproblems
   - Choose data structure (array, 2D table, etc.)
   - Determine evaluation order (ensure subproblems are solved before they're needed)

3. **Analyze runtime:**
   - Runtime = (number of subproblems) × (work per subproblem)

## Problem 1: Longest Decreasing Subsequence

**Problem:** Find the length of the longest decreasing subsequence of array A[1..n].

### 2-Parameter Formulation

**Subproblem:** LIS(i, j) = length of the longest decreasing subsequence of A[i..n] where all elements are strictly less than A[j].

**Recurrence:**
- LIS(i, j) = max(
    LIS(i+1, j),                           — skip A[i]
    1 + LIS(i+1, i) if A[i] < A[j]         — take A[i] (it satisfies the bound)
  )

**Base case:** LIS(n+1, j) = 0 for all j.

**Answer:** LIS(1, 0) where A[0] = +∞ (sentinel — no upper bound initially, but we want decreasing, so starting sentinel is large).

**Time/Space:** Θ(n²) subproblems, O(1) per subproblem → **Θ(n²) time, Θ(n²) space**.

### 1-Parameter Formulation

**Subproblem:** LDS(i) = length of the longest decreasing subsequence **starting at index i** (A[i] is included).

**Recurrence:**
LDS(i) = 1 + max{ LDS(j) : j > i and A[j] < A[i] }

(If no such j exists, LDS(i) = 1.)

**Base case:** LDS(n) = 1.

**Answer:** max{ LDS(i) : 1 ≤ i ≤ n }

**Evaluation order:** Right to left (i = n down to 1).

**Time/Space:** Θ(n) subproblems, O(n) work per subproblem → **Θ(n²) time, Θ(n) space**.

### Comparison

| Formulation | Time | Space | Notes |
|-------------|------|-------|-------|
| 2-parameter LDS(i,j) | Θ(n²) | Θ(n²) | More subproblems, cleaner recursion |
| 1-parameter LDS(i) | Θ(n²) | Θ(n) | Fewer subproblems, more work per subproblem |

Both are analogous to standard LIS formulations — the decreasing variant is symmetric.

## See Also

- [[Dynamic Programming]]
- [[Longest Increasing Subsequence]]
- [[CSCE 411]]
