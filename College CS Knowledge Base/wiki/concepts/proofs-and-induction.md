---
title: "Proofs and Induction"
type: concept
tags: [proofs, induction, loop-invariants, correctness, algorithms]
sources: [lecture-2-proofs-programs-problem-solving]
course: CSCE 411
updated: 2026-04-09
---

# Proofs and Induction

Induction and recursion are structurally analogous: both assume you can solve a smaller version of a problem and use that to solve the larger one. This analogy is the foundation for proving recursive algorithm correctness.

> "It's not about being smart or even fast... you need a plan — that's the hard part — and you have to see the bigger picture."
> — Terrance Tao (on problem solving, quoted in Lecture 2)

## Mathematical Induction

Standard structure for an induction proof:

1. **Base case**: prove the statement for n = 1 (or the smallest valid input)
2. **Induction hypothesis**: assume the statement holds for all k < n (strong induction) or for k = n − 1 (weak induction)
3. **Induction step**: prove the statement for n, using the hypothesis

## Proving Correctness of Recursive Algorithms

Induct on a **well-ordered measure** that strictly decreases with each recursive call. Common choices:
- Value of a parameter (e.g., the second argument in Euclid's GCD)
- Number of recursive calls remaining
- Size of the remaining input

### Example — Euclid's GCD Algorithm (~300 B.C.)

```
Euclid(a, b):
  if b == 0: return a
  else: return Euclid(b, a mod b)
```

**What to induct on**: induct on `b` (the second argument), NOT on `a` or on `max(a, b)`. The key property is that `a mod b < b`, so `b` strictly decreases at each call.

- **Base case**: b = 0 → return a. Correct since gcd(a, 0) = a by definition.
- **IH**: Euclid(b, a mod b) correctly returns gcd(b, a mod b).
- **Step**: use the identity gcd(a, b) = gcd(b, a mod b). By IH, Euclid(b, a mod b) = gcd(b, a mod b) = gcd(a, b). ✓

**Key insight**: choosing the wrong induction variable (e.g., `a`) leads to a proof that does not go through. Identifying the right measure is the hard part.

## Loop Invariants

A loop invariant is a predicate that holds before every iteration of a loop (including before the first iteration and after the last). Used to prove correctness of iterative algorithms.

### Structure of a Loop Invariant Proof

1. **Initialization**: the invariant holds before the first iteration
2. **Maintenance**: if the invariant holds before iteration k, it holds before iteration k+1
3. **Termination**: when the loop exits, the invariant yields the desired result

### Example — InsertionSort

```
InsertionSort(A[1..n]):
  for k = 1 to n-1:
    insert A[k+1] into its correct position in A[1..k]
```

**Invariant**: after k iterations of the outer for loop, A[1..k] is sorted.

- **Initialization**: before any iteration (k = 0), A[1..0] is vacuously sorted. After 1 iteration, A[1..1] is trivially sorted (single element).
- **Maintenance**: A[1..k] is sorted (by IH); inserting A[k+1] into the correct position in A[1..k] yields sorted A[1..k+1].
- **Termination**: after n−1 iterations, A[1..n] is sorted. ✓

## See Also

- [[CSCE 411]]
- [[Divide and Conquer]]
- [[Greedy Algorithms]]
