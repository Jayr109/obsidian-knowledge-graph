---
title: "Lecture 28 — NP-Completeness"
type: source
tags: [CSCE-411, NP, NP-complete, Cook-Levin, Karp-reductions, lecture]
sources: []
course: CSCE 411
updated: 2026-04-27
---

CSCE 411 lecture by Calvin Beideman (21 slides). Defines Karp (polynomial-time many-one) reductions and contrasts them with Turing reductions, then defines NP-hard and NP-complete. Establishes the Cook-Levin theorem (CIRCUIT-SAT is NP-complete) as the foundational NP-completeness result, and reduces CIRCUIT-SAT to SAT to seed the NP-completeness chain.

## Slides Index

| # | Title | Notes |
|---|-------|-------|
| 1 | Title — NP-Completeness | Beideman |
| 2 | Learning Objectives | Prove L ∈ NP, define NP-hard/complete, find examples |
| 3 | What does NP stand for? | Nondeterministic polynomial time; verifier definition equivalent |
| 4 | Complexity Class Review | (visual) |
| 5 | Complexity Classes Venn Diagram | P, NP, CoNP, EXP |
| 6 | The Class NP | (visual — verifier definition) |
| 7 | Karp Reductions | (visual — definition slide) |
| 8 | Turing Reductions | (visual — contrast slide) |
| 9–12 | Properties of Karp Reductions (I–IV) | (visual — formal statements) |
| 13 | Hardness and Completeness | (visual — definitions) |
| 14 | NP Completeness | Can't prove exponential lower bound; relative hardness instead |
| 15 | NP-Hard But Not NP-Complete | Theorem 5: HALTS is NP-Hard (but undecidable, so not NP-complete) |
| 16 | Do NP-Complete Languages Exist? | CIRCUIT-SAT diagram (AND, AND, NOT, OR) |
| 17 | CIRCUIT-SAT in NP | Certificate = truth assignment; verifier simulates circuit |
| 18 | CIRCUIT-SAT is NP-Hard | **Cook-Levin Theorem** |
| 19 | Using Reductions to prove NP-Hardness | (visual — schema) |
| 20 | SAT is NP-Complete | In NP via truth-assignment certificate |
| 21 | SAT is NP-Hard | Reduction from CIRCUIT-SAT (covered in Lecture 29) |

Many slides are visual-only (formal definitions, circuit diagrams). Text extraction captured titles, learning objectives, and the verifier/certificate descriptions.

## Key Takeaways

### Reduction Types: Karp vs. Turing

Two distinct notions of reduction were introduced previously, and now formally distinguished:

- **[[Karp Reductions]]** (polynomial-time many-one): single transformation L₁ ≤_p L₂ via a poly-time function f, where x ∈ L₁ iff f(x) ∈ L₂. Used for NP-hardness.
- **[[Turing Reductions]]**: oracle-style; can call the oracle for L₂ multiple times. Used for undecidability (e.g., reducing HALT to other halting variants).

Karp reductions are *more restrictive* than Turing reductions, but the appropriate tool for NP-hardness (the polynomial-time complexity class is closed under Karp reductions in the right way).

### NP-Hardness vs. NP-Completeness

- **NP-hard**: every L' ∈ NP satisfies L' ≤_p L.
- **NP-complete**: NP-hard *and* in NP.

A problem can be NP-hard but not NP-complete: HALTS is NP-hard (Theorem 5 — every NP problem reduces to it via Karp reductions, since HALTS is "harder than" NP) but undecidable, so not in NP.

### The Cook-Levin Theorem

**Theorem (Cook 1971, Levin 1973)**: CIRCUIT-SAT is NP-complete.

- **In NP**: certificate is a truth assignment to input wires; verifier simulates the circuit gate-by-gate. Certificate is shorter than the input (which encodes the whole circuit), so poly-size; simulation is poly-time.
- **NP-hard**: every L ∈ NP has a poly-time verifier V; for any input x, build a circuit that simulates V(x, ·). The circuit is satisfiable iff some certificate makes V accept iff x ∈ L. Construction is poly-time in |x|.

This is the *first* NP-completeness result and seeds the entire chain: every subsequent NP-completeness proof reduces from a known NP-complete problem (eventually rooted at CIRCUIT-SAT).

### SAT is NP-Complete

Once CIRCUIT-SAT is NP-hard, we get SAT NP-hardness via reduction CIRCUIT-SAT ≤_p SAT (constructed in Lecture 29 with a careful gadget — naïve recursive expansion can produce exponential blowup).

In NP: certificate = truth assignment to formula variables; verifier evaluates connectives in poly time.

## Cross-References

- Defined here: Karp reductions, NP-hard, NP-complete, Cook-Levin theorem, CIRCUIT-SAT, SAT
- Builds on: [[Lecture 26 — NP]] (P, NP, EXP, verifiers), [[Lecture 27 — NP Verifiers]] (verifier proofs for VC, Clique, TSP)
- Continues into: [[Lecture 29 — NP-Hardness Proofs]] (full reduction chain, 3-SAT, 3-COL)

## See Also

- [[NP Completeness]]
- [[NP and Complexity Classes]]
- [[Karp Reductions]]
- [[Turing Reductions]]
- [[Lecture 26 — NP]]
- [[Lecture 27 — NP Verifiers]]
- [[Lecture 29 — NP-Hardness Proofs]]
- [[CSCE 411]]
