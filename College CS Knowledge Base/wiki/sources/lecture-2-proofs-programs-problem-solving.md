---
title: "Lecture 2 — Proofs, Programs & Problem Solving"
type: source
tags: [lecture, proofs, induction, loop-invariants, correctness, algorithms]
sources: [lecture-2-proofs-programs-problem-solving]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 2 — Proofs, Programs & Problem Solving

**Course**: CSCE 411 | **Instructor**: Calvin Beideman | **Slides**: 15

## Motivational Quote

> "It's not about being smart or even fast... you need a plan — that's the hard part — and you have to see the bigger picture."
> — Terrance Tao (paraphrased, on problem solving)

## Learning Objectives

- Write cleaner, more rigorous proofs
- Construct induction proofs for algorithm correctness
- Define and apply loop invariants
- Prove correctness of iterative algorithms

## Euclid's GCD Algorithm (~300 B.C.)

```
Euclid(a, b):
  if b == 0: return a
  else: return Euclid(b, a mod b)
```

**Correctness proof via induction**: the key insight is choosing *what to induct on*. Inducting on `x` or `y` directly does not work cleanly. Instead, induct on `y` (the second argument), which strictly decreases at each recursive call because `a mod b < b`.

- **Base case**: b = 0 → return a, which is correct since gcd(a, 0) = a.
- **Inductive hypothesis**: assume Euclid(b, a mod b) correctly computes gcd(b, a mod b).
- **Inductive step**: use the identity gcd(a, b) = gcd(b, a mod b) to conclude correctness.

**Key analogy**: induction and recursion are structurally analogous — both assume the smaller version works and use it to handle the larger version.

## InsertionSort Correctness via Loop Invariants

**Loop invariant**: after k iterations of the outer for loop, A[1..k] is sorted.

- **Initialization**: A[1..1] is trivially sorted (single element).
- **Maintenance**: inserting A[k+1] into sorted A[1..k] (by shifting) yields sorted A[1..k+1].
- **Termination**: after n−1 iterations, A[1..n] is sorted.

## Bubble Sort (Bonus)

Similar loop invariant structure can be applied to Bubble Sort. After k passes, the k largest elements are in their correct positions at the end of the array.

## Key Insight: "What Should We Induct On?"

For recursive algorithms, the right induction measure is usually not an obvious input parameter. For Euclid's GCD, the right choice is `y` (or equivalently, `min(x, y)` or the number of recursive calls remaining). Choosing the wrong measure leads to a proof that doesn't go through.

## See Also

- [[Proofs and Induction]]
- [[Loop Invariants]]
- [[CSCE 411]]
