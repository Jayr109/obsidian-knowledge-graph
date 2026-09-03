---
title: "Longest Increasing Subsequence"
type: algorithm
tags: [dynamic-programming, sequences, algorithms]
sources: [lecture-20-dynamic-programming-2]
course: CSCE 411
updated: 2026-04-09
---

The Longest Increasing Subsequence (LIS) problem asks: given a sequence of numbers, find the length of the longest subsequence in which each element is strictly greater than the previous. This is a classic [[Dynamic Programming]] problem covered in CSCE 411 Lecture 20.

## Problem Definition

**Input**: Array A[1..n]
**Output**: Length (and optionally the actual subsequence) of the longest strictly increasing subsequence of A.

**Example**: A = [3, 1, 4, 1, 5, 9, 2, 6] → LIS = [1, 4, 5, 9] or [1, 4, 5, 6], length 4.

## DP Formulation

**Subproblem**: Let `L[i]` = length of the LIS ending at index i.

**Recurrence**:
```
L[i] = 1 + max{ L[j] : j < i and A[j] < A[i] }
       (or 1 if no such j exists)
```

**Base case**: `L[i] = 1` for all i (every single element is a subsequence of length 1).

**Answer**: `max(L[1], L[2], ..., L[n])`

**Time**: O(n²) — two nested loops.
**Space**: O(n) — the L table.

## Alternative O(n log n) Formulation

A different recurrence using patience sorting yields an O(n log n) algorithm (covered in Lecture 20 as "Another DP Alg for LIS"). The key idea: maintain a list of the smallest tail elements for increasing subsequences of each length, using binary search to update.

*Note: The visual details of the alternative recurrence were on diagram-heavy slides not fully captured in text extraction.*

## See Also

- [[Dynamic Programming]]
- [[Subset Sum]]
- [[CSCE 411]]
