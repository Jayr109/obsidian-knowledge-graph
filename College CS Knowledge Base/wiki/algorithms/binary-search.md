---
title: "Binary Search"
type: algorithm
tags: [binary-search, divide-and-conquer, searching, sorted-array]
sources: [lecture-7-divide-and-conquer]
course: CSCE 411
updated: 2026-04-09
---

# Binary Search

Binary Search finds a target value in a sorted array in O(log n) time by repeatedly halving the search space.

## Precondition

The array must be **sorted**. For unsorted arrays, linear search is optimal — without any order guarantee, every element must potentially be examined (Ω(n) lower bound).

## Algorithm

```
BinarySearch(A[1..n], target, low=1, high=n):
  if low > high:
    return NOT_FOUND
  mid = ⌊(low + high) / 2⌋
  if A[mid] == target:
    return mid
  if A[mid] < target:
    return BinarySearch(A, target, mid+1, high)
  else:
    return BinarySearch(A, target, low, mid-1)
```

## Runtime

**Recurrence**: T(n) = T(n/2) + O(1)

By Master Theorem (Case 2 with f(n) = O(1) = O(n^0) and log_b a = log₂1 = 0):
T(n) = **O(log n)**

## Correctness

**Invariant**: if target exists in A[1..n], then target ∈ A[low..high].

- Each recursive call eliminates one half of the remaining search space based on the comparison A[mid] vs. target.
- Terminates when low > high (target not in array) or A[mid] = target (found).

## Variants

- **Finding i such that A[i] = i** (sorted array of distinct integers): define f(i) = A[i] − i, which is non-decreasing. Binary search on f(i) = 0. Also O(log n).
- **Lower/upper bound queries**: find first or last occurrence of a target in an array with duplicates. Same O(log n), different termination condition.
- **Rotated sorted array — find rotation count** (Final Exam Q3): given a k-step rotation of a sorted array of distinct integers, find k in O(log n) by binary-searching for the maximum element. Elements at or before the maximum satisfy A[mid] ≥ A[1]; elements after satisfy A[mid] < A[1]. Binary search on this predicate locates imax; answer is n − imax.

```
FindMax(A[1..n], low=1, high=n):
  if low = high: return n − low        // n − imax = rotation count
  mid = ⌈(low + high) / 2⌉
  if A[mid] < A[1]: return FindMax(A, low, mid − 1)
  return FindMax(A, mid, high)
```

Correctness invariant: low ≤ imax ≤ high at every call. The search space halves each call, giving O(log n) total.

## Comparison: Linear vs. Binary Search

| | Linear Search | Binary Search |
|---|---|---|
| Precondition | None | Array sorted |
| Runtime | O(n) | O(log n) |
| Optimality | Optimal for unsorted | Optimal for sorted |

## See Also

- [[Divide and Conquer]]
- [[Asymptotic Analysis]]
- [[CSCE 411]]
