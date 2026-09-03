---
title: "Subset Sum"
type: algorithm
tags: [dynamic-programming, decision-problem, algorithms]
sources: [lecture-20-dynamic-programming-2]
course: CSCE 411
updated: 2026-04-09
---

Subset Sum is a classic decision problem: given a set of integers and a target value T, determine whether any subset of the integers sums to exactly T. It is solvable in pseudopolynomial time via [[Dynamic Programming]].

## Problem Definition

**Input**: Set of integers S = {s₁, s₂, ..., sₙ}, target T.
**Output**: True if there exists a subset of S that sums to T; False otherwise.

**Example**: S = {3, 1, 4, 2}, T = 6 → True (subsets {3,1,2} or {4,2}).

## DP Formulation

**Subproblem**: Let `DP[i][t]` = True if some subset of {s₁, ..., sᵢ} sums to t.

**Recurrence**:
```
DP[i][t] = DP[i-1][t]              (don't include sᵢ)
         OR DP[i-1][t - sᵢ]        (include sᵢ, if t ≥ sᵢ)
```

**Base cases**:
- `DP[0][0]` = True (empty subset sums to 0)
- `DP[0][t]` = False for t > 0

**Answer**: `DP[n][T]`

**Time**: O(n · T) — pseudopolynomial (polynomial in n and T, but T can be exponential in input bit length).
**Space**: O(n · T) — the 2D table (can be reduced to O(T) with rolling array).

## Notes

- Subset Sum is NP-complete in general (when T is part of the input size in bits). The DP is not polynomial in the *input length* — it's polynomial in the *value* of T.
- A variant ("Subset Sum, Take 2") was presented in Lecture 20, likely involving a reformulation or optimization of the recurrence. *(Visual details of that slide not captured in text extraction.)*

## See Also

- [[Dynamic Programming]]
- [[Longest Increasing Subsequence]]
- [[CSCE 411]]
