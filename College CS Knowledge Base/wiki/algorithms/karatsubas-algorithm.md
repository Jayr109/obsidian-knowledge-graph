---
title: "Karatsuba's Algorithm"
type: algorithm
tags: [karatsuba, divide-and-conquer, multiplication, integer-arithmetic, master-theorem]
sources: [lecture-7-divide-and-conquer]
course: CSCE 411
updated: 2026-04-09
---

# Karatsuba's Algorithm

Karatsuba's algorithm multiplies two n-digit numbers faster than grade-school O(n²) multiplication using a divide-and-conquer insight that reduces 4 recursive multiplications to 3.

## Background

**Grade-school multiplication**: O(n²) — for each of n digits in one number, multiply and shift against all n digits of the other.

**Naive D&C multiply**: split each n-digit number into two n/2-digit halves:

```
x = x₁ · B^(n/2) + x₀
y = y₁ · B^(n/2) + y₀
```

```
xy = x₁y₁ · B^n  +  (x₁y₀ + x₀y₁) · B^(n/2)  +  x₀y₀
```

This requires **4 recursive multiplications** of n/2-digit numbers.
- Recurrence: T(n) = 4T(n/2) + O(n) → O(n²) by Master Theorem. No improvement over grade-school.

## Karatsuba's Key Insight

Compute only **3 multiplications**:

```
P₁ = x₁ · y₁
P₂ = x₀ · y₀
P₃ = (x₁ + x₀) · (y₁ + y₀)
```

Recover the cross term using only addition and subtraction:
```
x₁y₀ + x₀y₁ = P₃ − P₁ − P₂
```

Final result:
```
xy = P₁ · B^n  +  (P₃ − P₁ − P₂) · B^(n/2)  +  P₂
```

Addition and subtraction are O(n), so no additional multiplications are needed.

## Recurrence and Runtime

T(n) = 3T(n/2) + O(n)

By Master Theorem (Case 1: log₂3 ≈ 1.585 > 1, so leaves dominate):

**T(n) = Θ(n^log₂3) ≈ Θ(n^1.585)**

Compared to grade-school O(n²), this is a significant asymptotic improvement for large n.

## Notes

- Numbers with non-power-of-2 digit counts can be padded with leading zeros without affecting correctness.
- Historically significant: Karatsuba (1960) disproved Kolmogorov's conjecture that O(n²) was optimal for integer multiplication.
- Further improvements exist: Toom-Cook (generalizes to k subproblems), Schonhage-Strassen, and Harvey-Hoeven (O(n log n) — 2019).

## See Also

- [[Divide and Conquer]]
- [[Asymptotic Analysis]]
- [[Master Theorem]]
- [[CSCE 411]]
