---
title: "Lecture 27 — NP Verifiers"
type: source
tags: [complexity, NP, verifiers, NP-completeness, Cook-Levin, CSCE-411]
sources: []
course: CSCE 411
updated: 2026-09-13
---

Lecture 27 deepens the NP verifier framework with concrete examples and introduces NP-completeness via the Cook-Levin theorem. The learning objective is to be able to *prove* a problem is in NP by explicitly constructing a verifier and proving its correctness.

## Slide-by-Slide Summary

**Slides 1–7 — Review: P, Brute Force, Exponential Time (partially visual)**
Recap of P, the brute force paradigm, and the EXP class. Several slides were visual-only.

**Slide 8 — The Class NP (visual)**
Formal definition slide; content visual. See [[Lecture 26 — NP]] for text definition.

**Slide 9 — Graph Coloring (visual)**
Illustration of a valid 4-coloring of a sample graph.

**Slide 10 — Example: 3-COL (visual)**
3-Coloring problem statement. Visual slide.

**Slide 11 — Verifier for 3-Coloring (visual)**
Explicit verifier construction for 3-COL. Visual slide — key construction:
- Certificate: an assignment of colors {1, 2, 3} to every vertex.
- Verifier: (1) check |c| is polynomial (it is: one color per vertex); (2) check each vertex gets a color in {1,2,3}; (3) check every edge (u,v) has c(u) ≠ c(v). Runs in O(n + m).

**Slides 12–13 — Co-NP (visual)**

**Slide 14 — NP & Co-NP**
Restatement: NP = YES instances have short justifications; Co-NP = NO instances have short justifications.

**Slide 15 (visual)**

**Slides 16–22 — NP Problem Examples**

*Vertex Cover*: Given graph G and integer k, does G have a vertex cover of size ≤ k? (A vertex cover is a set S of vertices such that every edge has at least one endpoint in S.) Certificate: the set S itself. Verifier: check |S| ≤ k and every edge is covered — O(n + m).

*Travelling Salesman Problem (TSP)*: Given a complete weighted graph and budget B, does a Hamiltonian cycle of total weight ≤ B exist? Certificate: the cycle (ordering of vertices). Verifier: check it visits all vertices exactly once and total weight ≤ B — O(n).

*Clique*: Given graph G and integer k, does G contain a clique of size k? (A clique is a set of k vertices all mutually adjacent.) Certificate: the k vertices. Verifier: check all pairs are connected — O(k²) = O(n²).

*SAT (Satisfiability)*: Given a propositional formula φ in CNF, does a satisfying truth assignment exist? Certificate: a truth assignment to all variables. Verifier: evaluate φ under the assignment — O(|φ|). Brute force: try all 2^n assignments.

*Circuit-SAT*: Given a Boolean circuit C, does an input assignment that outputs 1 exist? Certificate: the input assignment. Verifier: simulate the circuit — O(|C|). Brute force: try all 2^n inputs; checking a single assignment is O(|C|).

**Slide 23 — All NP Problems Can Be Brute Forced**
Every NP problem has a poly-time verifier. Strategy: enumerate all poly-size certificates (exponential many), run the verifier on each. This gives an exponential-time algorithm for every NP problem: NP ⊆ EXP.

**Slide 24 — Complexity Classes Venn Diagram**
```
EXP
  ├── NP
  │    └── P
  └── Co-NP
       └── P
```
P ⊆ NP ∩ Co-NP ⊆ EXP. Whether P = NP (or NP = Co-NP) is open; the diagram reflects the *believed* strict containments.

**Slides 25–26 — NP Completeness**
We cannot prove that NP problems require exponential time, but we can provide *evidence of hardness* via reductions.

**Cook-Levin Theorem**: CIRCUIT-SAT is NP-Complete. Every problem in NP reduces to CIRCUIT-SAT in polynomial time.

All problems introduced in this lecture (3-COL, Vertex Cover, TSP, Clique, SAT, Circuit-SAT) are NP-complete. Next lecture: how to prove NP-completeness via polynomial reductions.

## Verifier Proof Template

To prove L ∈ NP, provide:
1. **Certificate**: describe what c is; argue |c| = poly(|x|).
2. **Completeness**: if x ∈ L, exhibit a c such that V(x, c) = 1.
3. **Soundness**: if x ∉ L, argue that for all c, V(x, c) = 0.
4. **Efficiency**: argue V runs in poly time.

## NP-Complete Problems Mentioned

| Problem | Certificate | Verifier runtime |
|---------|-------------|-----------------|
| 3-COL | Vertex coloring | O(n + m) |
| Vertex Cover | Set S of vertices | O(n + m) |
| TSP | Hamiltonian cycle ordering | O(n) |
| Clique | Set of k vertices | O(n²) |
| SAT | Truth assignment | O(\|φ\|) |
| Circuit-SAT | Input assignment | O(\|C\|) |

## See Also

- [[NP and Complexity Classes]]
- [[NP Completeness]]
- [[Lecture 26 — NP]]
- [[Decidability and Undecidability]]
- [[CSCE 411]]
- [[Vertex Cover]]
