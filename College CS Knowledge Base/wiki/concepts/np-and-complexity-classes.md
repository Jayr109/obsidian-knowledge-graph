---
title: "NP and Complexity Classes"
type: concept
tags: [complexity, NP, P, CoNP, EXP, decision-problems, verifiers]
sources: [lecture-26-np, lecture-27-np-verifiers]
course: CSCE 411
updated: 2026-04-21
---

Complexity classes partition decision problems by the computational resources required to solve them. The classes P, NP, Co-NP, and EXP form a hierarchy that captures the fundamental question of which problems are tractably solvable and which are inherently hard.

## Decision Problems and Languages

A *decision problem* asks a YES/NO question about an input. We represent it as a *language* L: the set of all inputs for which the answer is YES. An algorithm *decides* L if it correctly answers YES or NO for every input.

Input instances are encoded as strings over some alphabet. The size of an instance x is its encoding length |x|.

## The Class P

**P** is the class of decision problems (languages) decidable by a deterministic algorithm in **polynomial time** — time O(|x|^k) for some constant k.

Why polynomial? Polynomial time is:
- **Robust**: independent of reasonable model of computation (RAM, TM, etc.)
- **Closed**: a polynomial number of calls to poly-time subroutines yields a poly-time algorithm
- **Historically validated**: nearly every tractable problem discovered has a polynomial algorithm

To prove L ∈ P: exhibit a polynomial-time algorithm. Examples in CSCE 411: [[BFS and DFS]], [[Dijkstra's Algorithm]], [[Floyd-Warshall]], [[Simplex Algorithm]], 2-Coloring.

**Search vs. Decision**: Many search problems (find an optimal value) reduce to decision problems via binary search. E.g., "find max flow value" → "is there a flow ≥ k?" using binary search over k.

## The Class NP

**NP** (Nondeterministic Polynomial time) is the class of decision problems for which every YES instance has a **short, efficiently verifiable certificate**.

Formally, L ∈ NP iff there exists a polynomial-time *verifier* V such that:
- **Completeness**: for every x ∈ L, ∃ certificate c with |c| = poly(|x|) and V(x, c) = 1
- **Soundness**: for every x ∉ L, for all c, V(x, c) = 0

The certificate c is sometimes called a *witness* — it "witnesses" that x is a YES instance.

### Verifier Proof Template

To prove L ∈ NP:
1. **Certificate**: describe c; argue |c| = poly(|x|)
2. **Completeness**: if x ∈ L, exhibit c such that V(x, c) = 1
3. **Soundness**: if x ∉ L, argue ∀c, V(x, c) = 0
4. **Efficiency**: argue V runs in poly time

### Examples in NP

| Problem | Certificate | Verifier |
|---------|-------------|---------|
| 3-Coloring | Assignment of 3 colors to vertices | Check adjacent vertices differ — O(n+m) |
| Vertex Cover | Set S of ≤ k vertices | Check every edge has endpoint in S — O(m) |
| Clique | Set of k vertices | Check all pairs adjacent — O(k²) |
| TSP | Hamiltonian cycle ordering | Check all vertices visited, total weight ≤ B — O(n) |
| SAT | Truth assignment to variables | Evaluate formula — O(\|φ\|) |
| Circuit-SAT | Input assignment | Simulate circuit — O(\|C\|) |
| Subset Sum | Subset S | Verify S ⊆ input set and sum equals target — O(n) |

Note: P ⊆ NP. Any poly-time algorithm is itself a verifier (with empty certificate).

## Brute Force and EXP

Every NP problem has a brute-force exponential algorithm: enumerate all poly-size certificates, run the verifier on each. This shows **NP ⊆ EXP**.

**EXP** is the class of problems decidable in exponential time O(2^{poly(|x|)}).

Brute force works when: (1) possible solutions can be enumerated, and (2) checking each is easy. The exponential blowup is in the enumeration, not the checking.

## The Class Co-NP

**Co-NP** is the class of decision problems for which every NO instance has a short, efficiently verifiable certificate. Formally, L ∈ Co-NP iff its complement L̄ ∈ NP.

Examples: "This graph is NOT 3-colorable" — no known short certificate. "This formula is a tautology (true under all assignments)" — Co-NP.

P ⊆ Co-NP (same argument as P ⊆ NP). Whether NP = Co-NP is open; believed false.

## The Complexity Hierarchy

```
EXP
  ├── NP  ──────────────────────────────────────────────── (NP-complete problems live at the top)
  │    └── P  ────────────────────────────────────────────
  └── Co-NP
       └── P
```

Known: P ⊆ NP ⊆ EXP, P ⊆ Co-NP ⊆ EXP, P ⊆ NP ∩ Co-NP.

Believed (unproven): P ≠ NP, NP ≠ Co-NP, NP ≠ EXP.

The **P vs. NP** question — whether every problem whose solutions are verifiable in poly time is also *solvable* in poly time — is the central open problem in theoretical computer science.

## Closure Properties

P is closed under: complement, union, intersection, polynomial-time reductions. This makes it robust as a complexity class.

NP is closed under union and intersection; whether it's closed under complement (= whether NP = Co-NP) is open.

**Additional closure properties proved in HW7** (via verifier constructions):

- **L₁ − L₂ ∈ NP** if L₁ ∈ NP and L₂ ∈ Co-NP: combine verifier V₁ for L₁ with verifier V₂ for Σ*−L₂; accept iff both accept. Certificate = ⟨c₁, c₂⟩.
- **L* ∈ NP** if L ∈ NP: certificate = decomposition of x into k substrings y₁…yk (each in L) plus NP certificates for each piece. Verifier checks concatenation and runs VL on each piece. Runtime: poly in |x| since k ≤ |x|+1.

## Co-NP Examples

**PRIMES ∈ Co-NP** (HW7 Q3): PRIMES = {⟨n⟩ : n is prime}. To show PRIMES ∈ Co-NP, give a verifier for composite numbers (the complement):
- Certificate for non-primality: a factorization ⟨k₁, k₂⟩ with k₁ · k₂ = n and k₁, k₂ ≠ 1.
- Verifier checks this multiplication in poly time (O(n^{1.59}) via Karatsuba).
- No certificate exists for primes (cannot factor them non-trivially).

*Note*: PRIMES is actually in P (AKS algorithm, 2002), but we don't assume this — Co-NP membership requires only a poly-time verifier for the complement, not a poly-time decider.

## See Also

- [[NP Completeness]]
- [[Decidability and Undecidability]]
- [[Linear Programming]]
- [[Subset Sum]]
- [[Lecture 26 — NP]]
- [[Lecture 27 — NP Verifiers]]
- [[CSCE 411]]
