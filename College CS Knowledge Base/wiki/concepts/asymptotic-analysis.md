---
title: "Asymptotic Analysis"
type: concept
tags: [asymptotic-analysis, big-o, runtime, complexity, word-ram]
sources: [lecture-6-asymptotic-analysis]
course: CSCE 411
updated: 2026-04-09
---

# Asymptotic Analysis

Asymptotic analysis is the standard tool for comparing algorithm efficiency. It abstracts away hardware differences and constant factors, expressing runtime as a function of input size n in the limit.

## Model of Computation

CSCE 411 uses the **Word-RAM model**:
- Memory is an array of words; each read/write takes O(1)
- Arithmetic, comparisons, and memory accesses each cost O(1)
- More realistic than Turing machines for algorithm analysis — TMs lack random access

**Input size n**: number of items (array length, vertex count, etc.) unless otherwise stated.

**Worst-case runtime**: the default throughout CSCE 411. Best-case is unrealistic; average-case is harder to compute and often matches worst-case asymptotically.

## Notation

- **O(f(n))** — upper bound.
  ∃ c, n₀ > 0 such that T(n) ≤ c·f(n) for all n ≥ n₀

- **Ω(f(n))** — lower bound.
  ∃ c, n₀ > 0 such that T(n) ≥ c·f(n) for all n ≥ n₀

- **Θ(f(n))** — tight bound.
  T(n) = Θ(f(n)) iff T(n) = O(f(n)) and T(n) = Ω(f(n))

## Proving Big-O

To prove T(n) = O(f(n)): choose explicit constants c and n₀, then verify T(n) ≤ c·f(n) for all n ≥ n₀.

**Example**: T(n) = 8n + 4. Claim: T(n) = O(n).
- Choose c = 9, n₀ = 4.
- For all n ≥ 4: 8n + 4 ≤ 9n iff 4 ≤ n. ✓

## Hierarchy of Common Runtimes

O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)

## Useful Properties

- If f'(n) ∈ O(f(n)) and g'(n) ∈ O(g(n)), then f'(n)·g'(n) = O(f(n)·g(n))
- Θ is transitive and symmetric
- For functions Z⁺ → R⁺: f(n) = O(g(n)) and g(n) = O(f(n)) implies f(n) = Θ(g(n))
- Can always choose n₀ = 1 for functions with positive range

## Common Algorithm Runtimes

| Algorithm | Runtime |
|---|---|
| FindMin (naive nested loop) | O(n²) |
| Selection Sort | O(n²) |
| Bubble Sort | O(n²) |
| Insertion Sort | O(n²) worst, O(n) best |
| Merge Sort | O(n log n) |
| Binary Search | O(log n) |

## See Also

- [[Divide and Conquer]]
- [[Master Theorem]]
- [[CSCE 411]]
