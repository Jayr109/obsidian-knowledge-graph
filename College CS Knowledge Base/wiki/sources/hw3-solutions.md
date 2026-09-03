---
title: "Homework 3 Solutions — Spring 2026"
type: source
tags: [csce411, homework, solutions, asymptotic-analysis, divide-and-conquer, big-o]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Homework 3 Solutions — Spring 2026

**Source file:** `raw/CSCE_411_HW3_Sp26_Solutions (2).pdf`
**Course:** CSCE 411, Spring 2026
**Due:** Monday, February 23, 2026
**Topics:** Asymptotic Analysis and Divide & Conquer

## Problem 1: Simplifying Big-O (n₀ = 1 Always Works)

**Claim:** For f, g : Z⁺ → R⁺, if f(n) = O(g(n)), then there exists a constant c such that f(n) ≤ c · g(n) for **all** n ≥ 1 (i.e., we can always take n₀ = 1).

**Proof:** Suppose f(n) ≤ c₀ · g(n) for all n ≥ n₀. Define:

c' = max(c₀, max{f(k)/g(k) : 1 ≤ k < n₀})

Then for n < n₀: f(n)/g(n) ≤ c' by construction.
For n ≥ n₀: f(n) ≤ c₀ · g(n) ≤ c' · g(n).

So f(n) ≤ c' · g(n) for all n ≥ 1. The max exists since it is taken over a finite set.

**Consequence:** When proving O bounds, we may always assume n₀ = 1 without loss of generality — only the constant c matters.

## Problem 2: More Big-O Properties

### Part (a): Sum of Θ-Equivalent Functions
**Claim:** If f₁(n) = Θ(f(n)) and f₂(n) = Θ(f(n)), then f₁(n) + f₂(n) = Θ(f(n)).

**Proof:** Let c₁ ≤ f₁(n)/f(n) ≤ C₁ and c₂ ≤ f₂(n)/f(n) ≤ C₂ for large n.
Then (c₁+c₂)·f(n) ≤ f₁(n)+f₂(n) ≤ (C₁+C₂)·f(n). So the sum is Θ(f(n)).

### Part (b): Infinite Sum — NOT Always Θ(n · f(n))
**Claim (FALSE):** ∑ᵢ₌₁ⁿ fᵢ(n) = Θ(n · f(n)) when each fᵢ(n) = Θ(f(n)).

**Counterexample:** Let f(n) = 1 and fᵢ(n) = i (each fᵢ is Θ(1), so f(n) = 1 qualifies).

∑ᵢ₌₁ⁿ i = n(n+1)/2 = Θ(n²)

But n · f(n) = n · 1 = Θ(n). So the sum is Θ(n²), not Θ(n).

**Lesson:** The hidden constants in the Θ bounds can depend on the index i, so summing n terms can give a factor of n² rather than n.

## Problem 3: Minimum Finding — Unusual Recursive Algorithm

**Setup:** An algorithm for finding the minimum of an array that splits into two subarrays of size ⌈2n/3⌉ (overlapping).

**Recurrence:** T(n) = 2T(2n/3) + Θ(1)

**Analysis via Master Theorem:**
- a = 2, b = 3/2, f(n) = Θ(1)
- n^(log_{3/2} 2) = n^(log 2 / log 1.5) ≈ n^1.71

Case 1 applies: f(n) = O(n^(log_{3/2} 2 - ε)) for some ε > 0.

**Runtime:** T(n) = Θ(n^(log_{3/2} 2)) ≈ Θ(n^1.71)

This is worse than the standard O(n) minimum-finding algorithm — the overlap in the recursive calls causes extra work.

## See Also

- [[Asymptotic Analysis]]
- [[Divide and Conquer]]
- [[CSCE 411]]
