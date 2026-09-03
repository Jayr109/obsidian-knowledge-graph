---
title: "Karp Reductions"
type: concept
tags: [reductions, NP-hardness, complexity, polynomial-time, CSCE-411]
sources: [lecture-28-np-completeness, lecture-29-np-hardness-proofs]
course: CSCE 411
updated: 2026-04-27
---

A **Karp reduction** (polynomial-time many-one reduction) is the standard tool for proving NP-hardness. It is a *single* polynomial-time computable transformation f from instances of one problem to instances of another, preserving the YES/NO answer. Karp reductions are weaker than [[Turing Reductions]] (no oracle calls allowed) but exactly the right notion for the polynomial-time class.

## Definition

For languages L₁, L₂ over some alphabet, a **Karp reduction** L₁ ≤_p L₂ is a polynomial-time computable function f such that for every input x:

$$x \in L_1 \iff f(x) \in L_2.$$

We say "L₁ is polynomial-time reducible to L₂" or "L₁ many-one reduces to L₂."

Notation:
- L₁ ≤_p L₂ — L₂ is at least as hard as L₁
- f is the *reduction function*

## Properties

### Transitivity
If L₁ ≤_p L₂ and L₂ ≤_p L₃, then L₁ ≤_p L₃ (compose the two reduction functions).

### Hardness Transfer (the reason we use them)
If L₁ ≤_p L₂ and L₂ ∈ P, then L₁ ∈ P. Equivalently: if L₁ ∉ P, then L₂ ∉ P.

This is the contrapositive that justifies NP-hardness proofs: if I show some hard L₁ reduces to my new problem L₂, then L₂ is at least as hard as L₁.

### NP Closure
NP is closed under Karp reductions: if L₁ ≤_p L₂ and L₂ ∈ NP, then L₁ ∈ NP. (Combine the reduction function with L₂'s verifier.)

### Identity
Every L is Karp-reducible to itself via the identity function.

## Karp vs. Turing Reductions

Both are notions of "L₁ is reducible to L₂." They differ in power:

| Aspect | Karp Reduction | [[Turing Reductions\|Turing Reduction]] |
|---|---|---|
| Transformation | Single function f | Algorithm with oracle for L₂ |
| Oracle calls | One implicit (run f, then check L₂) | Many; can be adaptive |
| Complexity bound | Poly-time computable f | Poly-time + oracle calls |
| Used for | NP-hardness | Undecidability (course used for HALT, ATM, etc.) |
| Strictly weaker? | Yes — strictly weaker than Turing | More powerful |

**Why does this matter?** Some hardness arguments require oracle-style queries (e.g., "use the L₂ oracle to do binary search"). These are valid Turing reductions but may not be Karp reductions. For NP-hardness we *want* the more restrictive Karp notion because it preserves more structure (e.g., Co-NP membership) and matches the way most natural reductions are constructed.

A useful mental check: **a Karp reduction is a transformation; a Turing reduction is a program that calls an oracle.**

## How to Construct a Karp Reduction (Tips from Lecture 29)

To prove L is NP-hard via L' ≤_p L, where L' is a known NP-hard problem:

**1. Direction**. Reduce *from* the known hard problem *to* the new problem. The other direction would only show L is *easier than or equal to* L', which proves nothing about L's hardness.

**2. Choose L' wisely**. Pick a problem whose structure naturally matches L:

| L is about... | Try L' = |
|---|---|
| Boolean formulas | SAT, 3-SAT |
| Graphs | VERTEX-COVER, CLIQUE, INDEPENDENT-SET, 3-COL, HAM-PATH |
| Sets of integers | SUBSET-SUM |
| Other / unclear | 3-SAT (most flexible default) |

**3. Build the function f**. Start by mapping *solutions to solutions* — what's a solution in L', what's a solution in L, and how should they correspond? Then design **gadgets** that translate each constraint of L' into a substructure of L.

**4. Prove correctness**. Both directions of x ∈ L' ⟺ f(x) ∈ L must be checked.

**5. Argue poly-time**. The construction f must run in time polynomial in |x|. Watch out for naïve recursion that duplicates substructures and produces exponential blowup (see [[Lecture 29 — NP-Hardness Proofs]] on the failed CIRCUIT-SAT → SAT attempt).

## Common Reduction Patterns

From [[Practice — NP-Hardness]]:

- **Hard-code a parameter**: kCol from 3-COL (set k=3); kCycle from Ham-Cycle (set k=n).
- **Pad with extra elements/vertices**: HalfClique from Clique (add vertices to shift the size threshold to n/2); Partition from Subset-Sum (add a balancing element).
- **Polarity anchor variable**: NAE-4SAT from 3-SAT (add a "false" anchor variable to each clause).
- **Auxiliary variables to avoid blowup**: SAT from CIRCUIT-SAT (one variable per gate output).
- **Gadget construction**: 3-COL from 3-SAT (variable gadget to force T/F coloring; clause gadget colorable iff at least one literal is T).

## Worked Examples in the Course

- [[NP-Hardness Scribbles]]: 3-COL ≤_p kCol via f(⟨G⟩) = ⟨G, 3⟩.
- [[Lecture 29 — NP-Hardness Proofs]]: full chain CIRCUIT-SAT → SAT → 3-SAT → 3-COL.
- [[Practice — NP-Hardness]]: 5 reductions covering parameter hard-coding, padding, and polarity-anchor patterns.

## See Also

- [[Turing Reductions]]
- [[NP Completeness]]
- [[NP and Complexity Classes]]
- [[Lecture 28 — NP-Completeness]]
- [[Lecture 29 — NP-Hardness Proofs]]
- [[NP-Hardness Scribbles]]
- [[Practice — NP-Hardness]]
- [[CSCE 411]]
