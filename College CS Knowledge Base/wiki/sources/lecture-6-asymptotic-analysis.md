---
title: "Lecture 6 — Asymptotic Analysis"
type: source
tags: [lecture, asymptotic-analysis, big-o, runtime, word-ram]
sources: [lecture-6-asymptotic-analysis]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 6 — Asymptotic Analysis

**Course**: CSCE 411 | **Slides**: 21

## Learning Objectives

- Compare algorithm efficiency independently of hardware
- Define and apply Big-O, Ω, and Θ notation
- Prove Big-O bounds by choosing explicit constants

## Model of Computation: Word-RAM

CSCE 411 uses the **Word-RAM model** (not Turing machines) for runtime analysis:
- Memory is an array of words; each word can be read/written in O(1) time
- Arithmetic, comparisons, and memory accesses each cost O(1)
- Motivation: Turing machines lack random access memory, making them unrealistic for measuring algorithm performance

## Runtime Measurement

- **Input size n**: number of items (array length, vertex count, etc.)
- **Worst-case runtime**: default throughout the course; more robust than best-case or average-case

## Asymptotic Notation

- **O(f(n))**: upper bound. ∃ c, n₀ > 0 such that T(n) ≤ c·f(n) for all n ≥ n₀
- **Ω(f(n))**: lower bound. ∃ c, n₀ > 0 such that T(n) ≥ c·f(n) for all n ≥ n₀
- **Θ(f(n))**: tight bound. T(n) = Θ(f(n)) iff T(n) = O(f(n)) and T(n) = Ω(f(n))

## Proving Big-O: The Method

Choose explicit constants c and n₀, then verify the inequality holds for all n ≥ n₀.

**Example**: T(n) = 8n + 4. Claim: T(n) = O(n).
- Choose c = 9, n₀ = 4.
- For all n ≥ 4: 8n + 4 ≤ 9n (since 4 ≤ n). ✓

## Complexity Hierarchy

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)

## Runtime Analysis Examples

| Algorithm | Runtime | Notes |
|---|---|---|
| FindMin (naive) | O(n²) | Nested loop over all pairs |
| Selection Sort | O(n²) | Scan for minimum n times |
| Bubble Sort | O(n²) | n passes of n comparisons |

## See Also

- [[Asymptotic Analysis]]
- [[CSCE 411]]
