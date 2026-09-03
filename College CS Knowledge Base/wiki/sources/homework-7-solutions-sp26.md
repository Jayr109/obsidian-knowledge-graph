---
title: "Homework 7 Solutions — Spring 2026"
type: source
tags: [homework, CSCE-411, LP, integer-programming, NP, complexity, bipartite-matching]
sources: []
course: CSCE 411
updated: 2026-05-03
---

Homework 7 for CSCE 411-501, Spring 2026. Due Monday, April 27, 2026. 4 problems covering LP formulation, LP relaxation of integer programs, Co-NP, and NP closure properties.

## Q1: Government Spending (LP Formulation)

**Problem**: x programs p₁,…,pₓ; y senators s₁,…,sy. Senator sᵢ cares about program set Sᵢ and requires ≥ $10,000 allocated to those programs collectively. Budget b. Can the budget pass?

**LP Formulation** (minimize total spending; check if optimum ≤ b):

```
minimize   Σᵢ dᵢ
subject to  Σ_{pⱼ ∈ Sᵢ} dⱼ ≥ 10000     for all 1 ≤ i ≤ y
            dᵢ ≥ 0                        for all 1 ≤ i ≤ x
```

Variable dᵢ = dollars allocated to program pᵢ. A valid budget exists iff the LP optimum ≤ b. Since LP is solvable in polynomial time (ellipsoid method, interior point), this is a polynomial-time algorithm.

## Q2: LP Relaxation for Bipartite Matching

**(a) Integer Program for Bipartite Matching**

One binary variable xₑ per edge e, indicating inclusion in matching:

```
maximize   Σ_{e ∈ E} xₑ
subject to  Σ_{e ∈ δ({v})} xₑ ≤ 1     for all v ∈ V    (at most one matched edge per vertex)
            xₑ ≥ 0                      for all e ∈ E
            xₑ ∈ ℤ                      for all e ∈ E
```

Note: this IP also correctly describes matching in *non-bipartite* graphs, but for a triangle the LP relaxation assigns each edge xₑ = 1/2 — a non-integral fractional solution.

**(b) LP Relaxation Has Integral Optimum**

Remove the integrality constraint. The resulting LP:

```
maximize   Σ xₑ
subject to  Σ_{e ∈ δ({v})} xₑ ≤ 1     for all v ∈ V
            xₑ ≥ 0                      for all e ∈ E
```

**Proof**: this LP describes maximum flow in the network G′ built from G by:
- Directing each edge of G from the X-side to Y-side of the bipartition
- Adding source s with unit-capacity edges to all X vertices
- Adding sink t with unit-capacity edges from all Y vertices
- All edge capacities = 1

The LP variable xₑ equals flow through edge e; constraints enforce capacity ≤ 1 at each vertex (degree constraint). Since all capacities in G′ are integral, [[Edmonds-Karp Algorithm]] finds an integral maximum flow. This integral flow is an integral optimal solution to the LP relaxation.

See [[LP Relaxation]] and [[König's Theorem]] for context.

**(c) Dual of the LP Relaxation**

Primal has one variable per edge, one constraint per vertex → dual has one variable per vertex, one constraint per edge:

```
minimize   Σ_{v ∈ V} yᵥ
subject to  yᵤ + yᵥ ≥ 1     for all {u,v} ∈ E
            yᵥ ≥ 0           for all v ∈ V
```

**(d) The Dual Represents Minimum Vertex Cover**

The dual LP is exactly a fractional minimum vertex cover: yᵥ = 1 means v is in the cover; yᵤ + yᵥ ≥ 1 means every edge has at least one endpoint in the cover; minimize the cover size.

**Consequence (König's Theorem)**: By strong LP duality, the LP optima are equal. Since the LP relaxation of bipartite matching has an integral optimum (part b), and the dual is the LP relaxation of vertex cover (which is also integral on bipartite graphs by the same flow argument), we get:

> **In every bipartite graph, max matching = min vertex cover.** ([[König's Theorem]])

## Q3: Primes ∈ Co-NP

**Claim**: PRIMES = {⟨n⟩ : n is prime} is in Co-NP.

**Proof**: We give a verifier for Σ* − PRIMES (i.e., for composite numbers and 1):

```
V(x, c):
  If x does not encode a non-negative integer n: Accept
  If n = 1: Accept
  If c does not encode a pair (k₁, k₂) of non-negative integers: Reject
  If k₁ = 1 or k₂ = 1: Reject
  If k₁ · k₂ = n: Accept
  Reject
```

**Completeness**: if n ∉ PRIMES (n is composite or 1), certificate ⟨a,b⟩ with a·b=n and a,b≠1 makes V accept. Certificate size is linear in |n|.

**Soundness**: if n ∈ PRIMES (n is prime), no factorization k₁·k₂ = n exists with k₁,k₂ ≠ 1, so V rejects for all c.

**Efficiency**: V runs in poly time — the only non-trivial step is multiplication k₁·k₂, which takes O(n^{1.59}) using [[Karatsuba's Algorithm]].

*Note*: We do NOT assume a poly-time primality test (AKS theorem); Co-NP membership is proved purely via the factorization certificate.

## Q4: Complexity Class Closures

**(a) L₁ − L₂ ∈ NP if L₁ ∈ NP and L₂ ∈ Co-NP**

L₁ ∈ NP gives verifier V₁ for L₁; L₂ ∈ Co-NP gives verifier V₂ for Σ*−L₂. Combine:

```
V(x, c):
  If c does not encode a pair (c₁, c₂): Reject
  If V₁(x, c₁) and V₂(x, c₂) both accept: Accept
  Reject
```

- *Completeness*: x ∈ L₁−L₂ → x ∈ L₁ (c₁ exists for V₁) and x ∉ L₂ (c₂ exists for V₂). Both accept.
- *Soundness*: x ∉ L₁−L₂ → either x ∉ L₁ (V₁ always rejects) or x ∈ L₂ (V₂ always rejects). Cannot both accept.
- *Efficiency*: V₁ and V₂ run in poly time; splitting c takes O(|c|) = poly(|x|). ✓

**(b) L* ∈ NP if L ∈ NP**

L ∈ NP gives verifier VL. Certificate for L* is a decomposition of x into substrings plus their NP certificates:

```
V(x, c):
  Decode c as (X, C) — lists of strings and certificates
  k ← |X|
  If k = 0, |C| ≠ k, or concat(X) ≠ x: Reject
  For i from 1 to k:
    If VL(X[i], C[i]) rejects: Reject
  Accept
```

- *Completeness*: x ∈ L* → x = y₁…yk where each yᵢ ∈ L with certificate cᵢ. Certificate ⟨y₁,…,yk,c₁,…,ck⟩ makes V accept. Total size ≤ |x| (strings) + k·poly(|x|) (certificates) = poly(|x|).
- *Soundness*: x ∉ L* → any decomposition has some piece not in L → VL rejects on that piece.
- *Efficiency*: k ≤ |x|+1; calls VL k times (poly time each); checking concatenation takes O(|x|).

## See Also

- [[Linear Programming]]
- [[LP Relaxation]]
- [[Bipartite Matching]]
- [[König's Theorem]]
- [[Vertex Cover]]
- [[NP and Complexity Classes]]
- [[NP Completeness]]
- [[Maximum Flow]]
- [[Edmonds-Karp Algorithm]]
- [[Karatsuba's Algorithm]]
- [[Homework 6 Solutions — Spring 2026]]
- [[CSCE 411]]
