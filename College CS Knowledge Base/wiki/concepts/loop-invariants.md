---
title: "Loop Invariants"
type: concept
tags: [loop-invariants, correctness, proofs, induction, iterative-algorithms]
sources: [lecture-2-proofs-programs-problem-solving]
course: CSCE 411
updated: 2026-08-25
---

A loop invariant is a property that holds before and after every iteration of a loop, used to prove that an iterative algorithm is correct. It is the iterative counterpart to induction on recursive algorithms — the invariant plays the role of the inductive hypothesis.

## The Three Obligations

To prove correctness with a loop invariant, establish all three:

| Step | What to show |
|---|---|
| **Initialization** | The invariant holds before the first iteration |
| **Maintenance** | If it holds before an iteration, it still holds after that iteration |
| **Termination** | When the loop exits, the invariant plus the exit condition gives the desired result |

Initialization and maintenance mirror the base case and inductive step. Termination is the extra obligation that induction alone does not supply — it is where the invariant is cashed out into the actual correctness claim.

## Worked Example: InsertionSort

**Invariant**: after k iterations of the outer `for` loop, A[1..k] is sorted.

- **Initialization**: A[1..1] is trivially sorted — a single element.
- **Maintenance**: inserting A[k+1] into the already-sorted A[1..k] by shifting yields sorted A[1..k+1].
- **Termination**: after n−1 iterations, A[1..n] is sorted — the postcondition.

## Worked Example: Bubble Sort

The same structure applies: after k passes, the k largest elements occupy their final positions at the end of the array. Termination after n−1 passes leaves the whole array sorted.

## Choosing the Invariant

The invariant must be strong enough that the exit condition implies the postcondition, but weak enough to actually survive each iteration. An invariant that is too weak proves nothing at termination; one that is too strong fails maintenance.

This mirrors the parallel question for recursive algorithms — *what should we induct on?* — where the right measure is often not an obvious input parameter. For Euclid's GCD the correct measure is the second argument, which strictly decreases because `a mod b < b`. See [[Proofs and Induction]].

## See Also

- [[Proofs and Induction]]
- [[Dynamic Programming]]
- [[CSCE 411]]
