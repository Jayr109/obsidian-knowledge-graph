---
title: "Divide and Conquer"
type: concept
tags: [divide-and-conquer, recursion, recurrences, master-theorem, algorithms]
sources: [lecture-7-divide-and-conquer]
course: CSCE 411
updated: 2026-04-09
---

# Divide and Conquer

Divide and Conquer (D&C) is an algorithm design paradigm that solves problems by breaking them into smaller **independent** subproblems of the same type, solving them recursively, and combining the results. Unlike [[Dynamic Programming]], D&C subproblems are disjoint — there is no overlapping substructure to memoize.

## The Paradigm

1. **Divide**: split the input into independent sub-instances
2. **Conquer**: solve each sub-instance recursively (base case: trivially small input)
3. **Combine**: merge sub-solutions into the full solution

## Reduction (Broader Context)

The most important technique in algorithm design: solve problem X by using a black-box algorithm for problem Y as a subroutine. Recursion is the special case where X = Y on a strictly smaller input. Correctness of recursive algorithms is proven by induction (see [[Proofs and Induction]]).

## Recurrence Relations

D&C algorithms have runtimes described by recurrences:

| Algorithm | Recurrence | Solved Runtime |
|---|---|---|
| Binary Search | T(n) = T(n/2) + O(1) | O(log n) |
| Merge Sort | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Naive D&C Multiply | T(n) = 4T(n/2) + O(n) | O(n²) — no improvement |
| Karatsuba | T(n) = 3T(n/2) + O(n) | O(n^log₂3) ≈ O(n^1.585) |

## Master Theorem

Solves recurrences of the form T(n) = aT(n/b) + f(n) where a ≥ 1, b > 1:

- **Case 1**: f(n) = O(n^(log_b a − ε)) for some ε > 0
  → T(n) = Θ(n^log_b a) *(leaves dominate)*
- **Case 2**: f(n) = Θ(n^(log_b a))
  → T(n) = Θ(n^log_b a · log n) *(leaves and root are balanced)*
- **Case 3**: f(n) = Ω(n^(log_b a + ε)) and regularity condition af(n/b) ≤ cf(n)
  → T(n) = Θ(f(n)) *(root dominates)*

## Key Algorithms

- [[Binary Search]] — O(log n); requires sorted input
- [[Karatsuba's Algorithm]] — O(n^log₂3); integer multiplication

## Comparison with Other Paradigms

| Paradigm | Subproblems | Overlap? | Combines? |
|---|---|---|---|
| Divide and Conquer | Independent | No | Yes |
| Dynamic Programming | Overlapping | Yes (memoize) | Yes |
| Greedy | Sequential | No | No (local choice) |

## See Also

- [[Binary Search]]
- [[Karatsuba's Algorithm]]
- [[Master Theorem]]
- [[Dynamic Programming]]
- [[CSCE 411]]
