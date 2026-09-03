---
title: "NP Completeness"
type: concept
tags: [complexity, NP-complete, Cook-Levin, reductions, hardness, CSCE-411]
sources: [lecture-27-np-verifiers, lecture-28-np-completeness, lecture-29-np-hardness-proofs]
course: CSCE 411
updated: 2026-04-27
---

NP-completeness identifies the hardest problems in NP. A problem is NP-complete if it is (1) in NP, and (2) every other NP problem [[Karp Reductions|Karp-reduces]] to it in polynomial time. NP-complete problems are equivalent in difficulty — a poly-time algorithm for any one would give poly-time algorithms for all of NP.

## Motivation: Providing Evidence of Hardness

We cannot (currently) prove that any NP problem requires exponential time. But we can provide *relative hardness* evidence: if problem A is as hard as problem B (via a [[Karp Reductions|polynomial-time reduction]]), then solving A efficiently would solve B efficiently.

NP-completeness crystallizes this: an NP-complete problem is "as hard as the whole class NP."

## Definitions

**[[Karp Reductions|Karp reduction]]** (polynomial-time many-one): L₁ ≤_p L₂ if there exists a polynomial-time computable function f such that x ∈ L₁ iff f(x) ∈ L₂. Reductions *preserve* difficulty: if L₂ ∈ P then L₁ ∈ P; contrapositively, if L₁ ∉ P then L₂ ∉ P.

Karp reductions are the standard tool for NP-hardness proofs. They differ from [[Turing Reductions]] (used for undecidability): a Turing reduction is an oracle algorithm; a Karp reduction is a single transformation.

**NP-hard**: L is NP-hard if every L' ∈ NP satisfies L' ≤_p L. Solving L in poly time would place all of NP in P.

**NP-complete**: L is NP-complete if L ∈ NP and L is NP-hard.

### NP-Hard ≠ NP-Complete

A problem can be NP-hard without being NP-complete — it may sit *outside* NP entirely.

**Theorem 5 (Lecture 28)**: HALTS is NP-hard.

But HALTS is undecidable, so it's not in NP. Hence NP-hard but not NP-complete. This shows NP-hardness is a *lower bound* on difficulty (not an upper bound).

The space:

```
       NP-hard
      ┌────────────────────────────┐
      │   undecidable (HALTS)      │
      │   …                         │
      │  ┌──────────────────────┐   │
      │  │     NP-complete      │   │
      │  │   (CIRCUIT-SAT, SAT, │   │
      │  │   3-SAT, 3-COL, …)   │   │
      │  └──────────────────────┘   │
      └────────────────────────────┘
```

## The Cook-Levin Theorem

**Theorem (Cook 1971, Levin 1973)**: CIRCUIT-SAT is NP-complete.

*Why this works*: Every NP problem has a poly-time verifier V(x, c). For any input x, we can build a Boolean circuit that simulates V on input x with a "free" certificate wire — the circuit is satisfiable iff x ∈ L. This reduction is polynomial in |x|. So CIRCUIT-SAT is at least as hard as every problem in NP.

CIRCUIT-SAT is also in NP (certificate = satisfying assignment; verifier = simulate the circuit), making it NP-complete.

## The Standard NP-Completeness Chain

[[Lecture 29 — NP-Hardness Proofs]] establishes the standard chain:

$$\text{CIRCUIT-SAT} \le_p \text{SAT} \le_p \text{3-SAT} \le_p \text{3-COL}$$

Each link is a poly-time Karp reduction:

| Reduction | Technique |
|---|---|
| CIRCUIT-SAT ≤_p SAT | One auxiliary variable per gate; clauses encode y ⟺ op(x₁, x₂) (avoids exponential blowup of naïve recursion) |
| SAT ≤_p 3-SAT | Convert each clause to CNF with at most 3 literals per clause; auxiliary variables split long clauses |
| 3-SAT ≤_p 3-COL | Color palette gadget {T, F, X} + variable gadget (forces T or F) + clause gadget (3-colorable iff clause has a T literal) |

## NP-Complete Problems

All of the following were established as NP-complete in CSCE 411 lectures 26–29. The reductions form a chain from CIRCUIT-SAT downward.

| Problem | Input | YES iff... |
|---------|-------|-----------|
| **Circuit-SAT** | Boolean circuit C | ∃ input assignment making C output 1 |
| **SAT** | CNF formula φ | ∃ truth assignment satisfying all clauses |
| **3-SAT** | 3-CNF formula | ∃ truth assignment (each clause has exactly 3 literals) |
| **3-Coloring (3-COL)** | Graph G | ∃ valid 3-coloring of G |
| **kCol** | Graph G, integer k | ∃ valid k-coloring of G |
| **[[Vertex Cover]]** | Graph G, integer k | ∃ vertex cover of size ≤ k |
| **Clique** | Graph G, integer k | ∃ clique of size ≥ k |
| **Independent Set** | Graph G, integer k | ∃ independent set of size ≥ k |
| **TSP** | Complete weighted graph, budget B | ∃ Hamiltonian cycle of weight ≤ B |
| **Ham-Cycle** | Graph G | ∃ cycle visiting every vertex |
| **Subset Sum** | Set of integers, target T | ∃ subset summing to T |
| **Partition** | Set of integers | Set splits into two equal-sum halves |
| **Half-Cycle** | Graph G | ∃ cycle visiting ≥ \|V\|/2 vertices |

Note: [[Subset Sum]] was already in the wiki as a DP problem (O(nT) pseudopolynomial). That algorithm is not polynomial in the *input size* (T can be exponentially large in its bit representation) — consistent with NP-completeness.

## Proving NP-Completeness

Standard approach (once Cook-Levin is established):

1. **Show L ∈ NP**: give a poly-time verifier (certificate, completeness, soundness, efficiency).
2. **Show L is NP-hard**: pick a known NP-complete problem L', and give a poly-time Karp reduction L' ≤_p L.

The reduction proves that if L could be solved in poly time, so could L' — and since L' is NP-hard, so is L.

### Karp Reduction Tips (Lecture 29)

**Direction**: reduce *from* known-hard to new — never the reverse.

**Problem choice**: pick a known NP-complete problem with similar structure to L:
- Boolean formulas → SAT or 3-SAT
- Graphs → VERTEX-COVER, CLIQUE, INDEPENDENT-SET, 3-COL, HAM-PATH
- Sets of integers → SUBSET-SUM
- Default: 3-SAT (constrained, regular structure makes gadgets clean)

**Function design**: start by mapping *solutions to solutions*. Build **gadgets** that translate each constraint of L' into a substructure of L. (E.g., for 3-SAT → 3-COL, map variables to vertices and truth values to colors; build a clause gadget that's 3-colorable iff at least one literal is T.)

**Verify**: prove both directions of x ∈ L' ⟺ f(x) ∈ L; argue f runs in poly time. Watch for exponential blowup from naïve duplication.

See [[Karp Reductions]] for the full treatment and [[Practice — NP-Hardness]] for worked examples (kCol, kCycle, Partition, HalfClique, NAE-4SAT).

## Implications

- If **P = NP**: all NP-complete problems have poly-time algorithms; cryptography (as currently conceived) breaks down.
- If **P ≠ NP** (widely believed): NP-complete problems have no poly-time algorithm; they require exponential time in the worst case.
- NP-completeness is a signal to *stop searching* for a fast exact algorithm and instead look for [[Approximation Algorithms|approximations]], heuristics, special-case algorithms (e.g., [[Vertex Cover]] in trees or bipartite graphs), or faster exponentials.

See [[Approximation Algorithms]] for the principled response — "relax one of: time, inputs, or optimality."

## Relationship to Prior Course Material

- [[Subset Sum]]: the DP solution is pseudopolynomial (O(nT)), not poly — consistent with NP-completeness. Has an FPTAS.
- [[Maximum Weight Independent Set]]: NP-hard on general graphs; the O(n) tree DP exploits tree structure (special case).
- [[Vertex Cover]]: NP-complete on general graphs; poly on trees (DP) and bipartite (LP); 2-approximation via maximal matching.
- [[Decidability and Undecidability]]: undecidable problems (like the Halting Problem) are *outside* EXP entirely — strictly harder than NP-complete problems. HALTS is NP-hard but undecidable, hence not NP-complete.
- Karp reductions used here vs. [[Turing Reductions]] used to prove undecidability: Turing reductions are more powerful (they allow oracle calls); Karp reductions are the right tool for NP because they preserve more structure.

## See Also

- [[NP and Complexity Classes]]
- [[Karp Reductions]]
- [[Turing Reductions]]
- [[Approximation Algorithms]]
- [[Vertex Cover]]
- [[Subset Sum]]
- [[Maximum Weight Independent Set]]
- [[Decidability and Undecidability]]
- [[Lecture 26 — NP]]
- [[Lecture 27 — NP Verifiers]]
- [[Lecture 28 — NP-Completeness]]
- [[Lecture 29 — NP-Hardness Proofs]]
- [[NP-Hardness Scribbles]]
- [[Practice — NP-Hardness]]
- [[CSCE 411]]
