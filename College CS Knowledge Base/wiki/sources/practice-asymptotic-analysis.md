---
title: "Practice — Asymptotic Analysis"
type: source
tags: [csce411, practice, asymptotic-analysis, big-o, big-omega, algorithms]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Practice — Asymptotic Analysis

**Source file:** `raw/CSCE_411_Asymptotic_Analysis_Practice_Solutions (2).pdf`
**Course:** CSCE 411, Spring 2026
**Date:** Friday, January 30, 2026
**Topics:** Big-O proofs, algorithm runtime analysis

## Problem 1: Prove √n/100 = Ω(log²n)

**Claim:** √n/100 = Ω(log²n), i.e., there exist c, n₀ such that √n/100 ≥ c · log²n for all n ≥ n₀.

**Proof by induction:**
Setting c = 1/14400 and n₀ = 1 works.

**Intuition:** Polynomial functions (even fractional powers like √n) grow faster than any polylogarithmic function (log^k n). The ratio √n / log²n → ∞ as n → ∞.

## Problem 2: Runtime of ExchangeSort

**Algorithm:** A sorting algorithm based on iteratively swapping elements that are out of order.

**Claim:** ExchangeSort runs in Θ(n³).

**Analysis via inversions:**
- An **inversion** is a pair (i,j) with i < j but A[i] > A[j].
- An n-element array has at most O(n²) inversions.
- Each outer loop iteration eliminates exactly 1 inversion (a single exchange fixes one out-of-order pair).
- The inner loop to find the next inversion to fix runs in Θ(n).

**Total:** (# inversions) × (inner loop cost) = Θ(n²) × Θ(n) = **Θ(n³)**.

## Problem 3: Big-O Properties for Products and Quotients

Let f, g, f', g' be positive functions with f'(n) = O(f(n)) and g'(n) = O(g(n)).

| Statement | Answer | Notes |
|-----------|--------|-------|
| f'(n) · g'(n) = O(f(n) · g(n)) | **TRUE** | If f' ≤ C₁f and g' ≤ C₂g, then f'g' ≤ C₁C₂fg |
| f'(n)^(g'(n)) = O(f(n)^(g(n))) | **Case-dependent** | Exponentiation does not preserve O bounds in general; depends on growth rates of exponents |
| f'(n) / g'(n) = O(f(n) / g(n)) | **FALSE** | Counterexample: f'=1, g'=1/n, f=1, g=1. Then f'/g'=n but f/g=1, and n ≠ O(1). The O bound on g' in the denominator can make the ratio larger, not smaller. |

## See Also

- [[Asymptotic Analysis]]
- [[CSCE 411]]
