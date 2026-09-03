---
title: "Practice — NP-Hardness"
type: source
tags: [CSCE-411, NP-hardness, reductions, practice, kCol, kCycle, Partition, HalfClique, NAE-4Sat]
sources: []
course: CSCE 411
updated: 2026-04-27
---

CSCE 411 practice problem set on NP-hardness reductions (no solutions provided in the file). Five problems, each asking for a Karp reduction proving the listed language is NP-hard. Solutions sketched here are derived from the techniques in [[Lecture 29 — NP-Hardness Proofs]].

## Permitted Source Problems

The handout states the following may be assumed NP-complete:

| Language | Definition |
|---|---|
| **3-SAT** | Boolean formulas in 3-CNF (each clause is OR of exactly 3 literals) |
| **Clique** | ⟨G, k⟩ : G has a k-clique |
| **Subset-Sum** | ⟨S, k⟩ : ∃ subset of S summing to k |
| **Ham-Cycle** | ⟨G⟩ : G has a Hamiltonian cycle |
| **3-COL** | ⟨G⟩ : G has a valid 3-coloring |

Recall: NP-Complete = NP-hard + in NP. The handout asks only for NP-hardness, but each language below is also in NP (verifier in each case is a short certificate-check; see [[Lecture 27 — NP Verifiers]] for the template).

## Problem 1 — kCol

**kCol** = {⟨G, k⟩ : G has a valid k-coloring}.

**Reduction (3-COL ≤_p kCol)**: f(⟨G⟩) = ⟨G, 3⟩. Identity-with-constant.

This is the [[NP-Hardness Scribbles]] worked example. Both directions hold trivially because 3-COL is literally the k=3 instance of kCol.

## Problem 2 — kCycle

**kCycle** = {⟨G, k⟩ : G has a cycle of length k}.

**Reduction approach (Ham-Cycle ≤_p kCycle)**: f(⟨G⟩) = ⟨G, |V(G)|⟩.

A Hamiltonian cycle is exactly a cycle of length n = |V(G)|. So G has a Hamiltonian cycle iff G has a cycle of length |V(G)|.

- (⇒) Ham-Cycle in G ⇒ length-|V| cycle in G.
- (⇐) A length-|V(G)| cycle in G visits every vertex (no repeats — it's a cycle), hence Hamiltonian.
- f is poly-time (compute |V(G)| from the encoding).

## Problem 3 — Partition

**Partition** = {⟨S⟩ : S can be split into U, V with U ∪ V = S, U ∩ V = ∅, Σ U = Σ V}.

**Reduction approach (Subset-Sum ≤_p Partition)**: standard textbook reduction.

Given ⟨S, k⟩, let T = Σ S. Construct S' from S by adding two new elements: a = (T - 2k) + B and b = 2k + B - T (or similar — the standard pad), where B is large enough to make all elements positive. The construction ensures S' partitions iff S has a subset summing to k.

**Cleaner alternative**: add to S a new element x = T - 2k (assuming T ≥ 2k; else add 2k - T and adjust). Then Σ S' = 2(T - k) (or 2T - 2k = 2(T-k)). Each side of a Partition must sum to T - k. The side containing the new element x = T - 2k contributes that to its sum, leaving k to be made up from elements of S — exactly a Subset-Sum solution for target k.

Bidirectional check and poly-time of f are standard.

## Problem 4 — HalfClique

**HalfClique** = {⟨G⟩ : G has a clique of size |V(G)|/2}.

**Reduction approach (Clique ≤_p HalfClique)**: pad the graph to make k a half.

Given ⟨G, k⟩ with |V(G)| = n: build G' by adding either isolated vertices or a separate clique to make the target clique size exactly half of |V(G')|.

- If k ≥ n/2: add 2k − n isolated vertices, so |V(G')| = 2k. Then HalfClique asks for a clique of size k — same as Clique on G (the isolated vertices can't extend a clique).
- If k < n/2: add a separate (n − 2k)-clique disjoint from G. Now |V(G')| = 2(n−k) and HalfClique asks for a clique of size n−k. The disjoint clique contributes (n−2k) to any clique containing it, and Clique on G can contribute at most k (assuming the desired k-clique exists), giving (n−2k) + k = n−k. Conversely, an (n−k)-clique in G' must contain at least k of G's vertices (since the disjoint clique only has n−2k), and those form a k-clique in G.

**Key idea**: padding shifts the threshold to "half" without changing the clique structure of interest.

## Problem 5 — NAE-4SAT

**NAE-4SAT** = {⟨φ⟩ : φ is a collection of 4-literal clauses, with an assignment where in each clause the literals are *not all equal*}.

(NAE = "Not All Equal" — every clause must have at least one True and at least one False literal.)

**Reduction approach (3-SAT ≤_p NAE-4SAT)**: introduce a global "false" anchor.

Given a 3-SAT formula φ over variables x₁, …, xₙ: introduce a new variable z, and convert each 3-clause (ℓ₁ ∨ ℓ₂ ∨ ℓ₃) to the 4-clause (ℓ₁ ∨ ℓ₂ ∨ ℓ₃ ∨ z) interpreted as an NAE-clause.

**Correctness intuition**:
- (⇒) If φ is satisfiable by some assignment α, set z = False. Each 3-clause has a True literal; the 4-clause has at least one True (a literal) and at least one False (z) — NAE satisfied.
- (⇐) If the NAE-4SAT instance is satisfied by an assignment β, examine z's value:
  - If z = False under β: each NAE-clause has a True among (ℓ₁, ℓ₂, ℓ₃), so β restricted to original variables satisfies φ.
  - If z = True: flip the entire assignment (NAE is closed under complement — flipping all variables in an NAE-satisfied clause keeps it NAE-satisfied since "not all equal" is symmetric). Now z = False and the previous case applies.

**Key idea**: NAE constraints are *complementation-invariant*; pick a representative orientation by anchoring z = False.

## Common Patterns Across the Five Problems

| Problem | Source | Reduction Pattern |
|---|---|---|
| kCol | 3-COL | Hard-code parameter (identity-with-constant) |
| kCycle | Ham-Cycle | Hard-code parameter (k = n) |
| Partition | Subset-Sum | Add a balancing element |
| HalfClique | Clique | Pad to make k = n/2 |
| NAE-4SAT | 3-SAT | Add a "polarity anchor" variable |

These five reductions illustrate four general techniques: parameter hard-coding (kCol, kCycle), arithmetic padding (Partition), graph padding (HalfClique), and polarity anchoring (NAE-4SAT). Each follows [[Lecture 29 — NP-Hardness Proofs]]'s tip on **problem choice**: pick a source whose structure already matches the target.

## See Also

- [[NP Completeness]]
- [[Karp Reductions]]
- [[NP-Hardness Scribbles]]
- [[Lecture 29 — NP-Hardness Proofs]]
- [[Lecture 28 — NP-Completeness]]
- [[CSCE 411]]
