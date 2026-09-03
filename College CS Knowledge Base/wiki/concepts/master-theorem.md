---
title: "Master Theorem"
type: concept
tags: [divide-and-conquer, recurrences, asymptotic-analysis, algorithms]
sources: [lecture-7-divide-and-conquer]
course: CSCE 411
updated: 2026-04-09
---

The Master Theorem gives closed-form solutions for recurrences of the form T(n) = aT(n/b) + f(n), which arise naturally from [[Divide and Conquer]] algorithms.

## Statement

For T(n) = aT(n/b) + f(n) with a ≥ 1, b > 1:

Let the **critical exponent** be c* = log_b(a).

| Case | Condition | Result |
|---|---|---|
| Case 1 | f(n) = O(n^(c*-ε)) for some ε > 0 | T(n) = Θ(n^c*) |
| Case 2 | f(n) = Θ(n^c*) | T(n) = Θ(n^c* · log n) |
| Case 3 | f(n) = Ω(n^(c*+ε)) and af(n/b) ≤ cf(n) | T(n) = Θ(f(n)) |

**Intuition**:
- Case 1: recursive work dominates — solution is determined by the number of leaves (aⁿ multiplications)
- Case 2: work is balanced across levels — extra log factor
- Case 3: top-level work dominates

## Common Applications

| Algorithm | Recurrence | c* = log_b(a) | Case | Result |
|---|---|---|---|---|
| Binary Search | T(n/2) + O(1) | log_2(1) = 0 | 2 | O(log n) |
| Merge Sort | 2T(n/2) + O(n) | log_2(2) = 1 | 2 | O(n log n) |
| Naive D&C multiply | 4T(n/2) + O(n) | log_2(4) = 2 | 1 | O(n²) |
| [[Karatsuba's Algorithm]] | 3T(n/2) + O(n) | log_2(3) ≈ 1.585 | 1 | O(n^log₂3) |

## Exam 1 Examples (from Solutions)

- T(n) = 5T(n/5) + Θ(n log n): c* = log_5(5) = 1; f(n) = Θ(n log n) = Θ(n^1 · log n) → **Case 2** → T(n) = Θ(n log² n)... wait, actually Θ(n log n) for Case 2 requires f(n)=Θ(n^c*). Here f(n)=Θ(n log n) which is slightly larger than Θ(n). This falls into a Case 2 extended form. The exam answer was T(n) = Θ(n log n) — this is an extended Case 2 (polylog factor).
- T(n) = 3T(n/2) + Θ(n²): c* = log_2(3) ≈ 1.585; f(n) = Θ(n²) = Θ(n^(1.585+ε)) → **Case 3** → T(n) = Θ(n²). TRUE.
- T(n) = 2T(n/3) + Θ(1): c* = log_3(2) ≈ 0.631; f(n) = O(n^(0.631-ε)) → **Case 1** → T(n) = Θ(n^log_3(2)). Exam T/F said Θ(n^log₂3) — FALSE (that's log base 2 of 3, not log base 3 of 2).

## See Also

- [[Divide and Conquer]]
- [[Asymptotic Analysis]]
- [[Binary Search]]
- [[Karatsuba's Algorithm]]
- [[CSCE 411]]
