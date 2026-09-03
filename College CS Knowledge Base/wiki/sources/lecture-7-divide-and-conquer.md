---
title: "Lecture 7 — Divide and Conquer"
type: source
tags: [lecture, divide-and-conquer, binary-search, karatsuba, master-theorem, recursion]
sources: [lecture-7-divide-and-conquer]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 7 — Divide and Conquer

**Course**: CSCE 411 | **Slides**: 19

## Core Concepts

### Reduction

The most important technique in algorithm design: solve problem X by using an algorithm for problem Y as a subroutine. The algorithm for Y is treated as a black box.

### Recursion

A special case of reduction where X = Y on a smaller input. Correctness is proven by induction — assume the recursive call works correctly on smaller inputs.

## Linear Search vs. Binary Search

| Algorithm | Precondition | Runtime | Recurrence |
|---|---|---|---|
| Linear Search | None (unsorted OK) | O(n) | — |
| Binary Search | Array must be sorted | O(log n) | T(n) = T(n/2) + O(1) |

Linear search on an unsorted array is **optimal** — without any order guarantee, every element must potentially be examined.

## Master Theorem

Solves recurrences of the form T(n) = aT(n/b) + f(n), where a ≥ 1, b > 1:

- **Case 1**: f(n) = O(n^(log_b a − ε)) → T(n) = Θ(n^log_b a)
- **Case 2**: f(n) = Θ(n^(log_b a)) → T(n) = Θ(n^log_b a · log n)
- **Case 3**: f(n) = Ω(n^(log_b a + ε)) and regularity condition → T(n) = Θ(f(n))

## Divide and Conquer Paradigm

1. **Divide**: split input into independent sub-instances
2. **Conquer**: solve each sub-instance recursively (base case: trivially small)
3. **Combine**: merge sub-solutions into a final answer

Subproblems must be **independent** (no overlap — this distinguishes D&C from dynamic programming).

## Integer Multiplication

**Grade-school multiplication**: O(n²) for n-digit numbers.

**Naive D&C multiply**: split each n-digit number into two halves (x = x₁·B^(n/2) + x₀). Requires 4 half-size multiplications.
- Recurrence: T(n) = 4T(n/2) + O(n) → O(n²). No improvement.

**Karatsuba's Algorithm**: reduces 4 multiplications to 3 via algebraic identity.
- Recurrence: T(n) = 3T(n/2) + O(n) → O(n^log₂3) ≈ O(n^1.585)
- Key: x₁y₀ + x₀y₁ = (x₁+x₀)(y₁+y₀) − x₁y₁ − x₀y₀

## See Also

- [[Divide and Conquer]]
- [[Binary Search]]
- [[Karatsuba's Algorithm]]
- [[Master Theorem]]
- [[CSCE 411]]
