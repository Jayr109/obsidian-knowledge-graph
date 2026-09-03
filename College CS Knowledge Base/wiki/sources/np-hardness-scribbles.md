---
title: "NP-Hardness Scribbles"
type: source
tags: [CSCE-411, NP-hardness, reductions, 3-COL, kCol, worked-example, handwritten]
sources: []
course: CSCE 411
updated: 2026-04-27
---

A single-page handwritten worked example proving **3-COL ≤_p kCol** — i.e., that the parameterized k-coloring problem is NP-hard. Demonstrates the simplest possible flavor of Karp reduction: a near-identity function that wraps the input with a constant.

## The Problem

**3-COL** = {⟨G⟩ : G has a valid 3-coloring}
**kCol** = {⟨G, k⟩ : G has a valid k-coloring}

To show kCol is NP-hard, reduce from a known NP-hard problem (3-COL) via a Karp reduction.

## The Reduction

```
f(⟨G⟩):
    return ⟨G, 3⟩
```

That is, take an instance of 3-COL (just a graph) and produce the corresponding instance of kCol with k = 3 hard-coded.

## Correctness

Need to prove ⟨G⟩ ∈ 3-COL ⟺ ⟨G, 3⟩ ∈ kCol.

**1. (⇒) If ⟨G⟩ ∈ 3-COL then ⟨G, 3⟩ ∈ kCol.**
   G has a valid 3-coloring; the kCol instance asks for a valid 3-coloring (k = 3). The same coloring witnesses both. *(Beideman's note: "Duh".)*

**2. (⇐) If ⟨G, 3⟩ ∈ kCol then ⟨G⟩ ∈ 3-COL.**
   ⟨G, 3⟩ ∈ kCol means G has a valid 3-coloring; that's exactly what ⟨G⟩ ∈ 3-COL says.

**3. f runs in polynomial time.**
   f just appends the constant `3` to its input. O(|⟨G⟩|).

## Why This Is Worth Studying

The naïve reaction is "this is too easy to be a real reduction." But it's a real Karp reduction, and the structure is the standard template:

1. Define f explicitly.
2. Prove both directions of the iff.
3. Argue f runs in polynomial time.

When the source problem is a *special case* of the target (3-COL is the k=3 case of kCol), the reduction is essentially the inclusion. The technique is also a useful warm-up before tackling problems with non-trivial gadgets.

This is also a model for the symmetric proof — kCol is in NP iff there's a poly-time verifier (which there is: just check the supplied coloring uses ≤ k colors and no two adjacent vertices share a color), so kCol is *NP-complete*.

## Source Context

Single PDF page (visual / handwritten). Originally a worked-example aid distributed alongside [[Lecture 29 — NP-Hardness Proofs]] and reinforced by [[Practice — NP-Hardness]] problem 1, which asks for exactly this proof.

## See Also

- [[NP Completeness]]
- [[Karp Reductions]]
- [[Lecture 29 — NP-Hardness Proofs]]
- [[Practice — NP-Hardness]]
- [[CSCE 411]]
