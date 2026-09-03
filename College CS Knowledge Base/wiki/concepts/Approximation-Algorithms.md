---
title: "Approximation Algorithms"
type: concept
tags: [approximation, NP-hardness, optimization, vertex-cover, max-cut, FPTAS, CSCE-411]
sources: [lecture-31-approximation-algorithms]
course: CSCE 411
updated: 2026-04-27
---

An **approximation algorithm** is a polynomial-time algorithm for an optimization problem that produces a solution provably close to optimal. Approximation algorithms are the principled response to NP-hardness: when finding the *best* solution in poly time is impossible (assuming P ≠ NP), we trade exact optimality for tractable runtime.

## Why Approximate?

If a problem is [[NP Completeness|NP-hard]], then assuming P ≠ NP no polynomial-time algorithm finds the optimum for *every* input. We can relax along three axes:

1. **Time** — accept exponential time; design *faster* exponentials (e.g., 2^(n/2) instead of 2ⁿ; effective for small inputs).
2. **Inputs** — solve only special cases. Examples: [[Vertex Cover]] in poly time on trees ([[Maximum Weight Independent Set|tree DP]]) and on bipartite graphs ([[Linear Programming|LP rounding]]).
3. **Optimality** — accept a "good enough" solution. *This is the approximation-algorithm strategy.*

## Optimization vs. Decision

[[NP and Complexity Classes|NP]] is technically a class of *decision* problems (yes/no). Most NP problems have natural *optimization* counterparts:

| Decision form | Optimization form |
|---|---|
| Is there a vertex cover of size ≤ k? | Find the minimum vertex cover. |
| Is there a tour of weight ≤ B? | Find the minimum-weight TSP tour. |
| Is there a cut crossing ≥ k edges? | Find the maximum cut. |

Approximation only makes sense for the optimization form — "approximating yes/no" is meaningless.

## Approximation Ratio

For a **minimization** problem (e.g., min vertex cover), an algorithm A is an **α-approximation** (α ≥ 1) if for every input I:

$$\frac{A(I)}{\text{OPT}(I)} \le \alpha.$$

Smaller α (closer to 1) is better. A 2-approximation guarantees output ≤ 2 · OPT.

For a **maximization** problem (e.g., max cut), the inequality flips:

$$\frac{A(I)}{\text{OPT}(I)} \ge \frac{1}{\alpha} \quad\text{or equivalently}\quad A(I) \ge (1/\alpha) \cdot \text{OPT}(I).$$

Some texts use ρ ≤ 1 for maximization (e.g., "1/2-approximation" for Max-Cut). The convention varies.

## Approximation Schemes

A stronger guarantee than a fixed α: a *family* of algorithms parameterized by ε > 0.

- **PTAS** (Polynomial-Time Approximation Scheme): for every fixed ε > 0, A_ε is a (1+ε)-approximation running in poly(n) time. Constants in the runtime may depend on ε (often badly — e.g., n^(1/ε)).
- **FPTAS** (Fully Polynomial-Time Approximation Scheme): also requires runtime polynomial in 1/ε. The strongest standard guarantee. Example: Subset-Sum has an FPTAS (despite being NP-complete).

A problem with an FPTAS is "easy" in a strong approximation sense — arbitrarily good approximation, scaling well in the precision parameter.

## Two Canonical Course Examples

### Greedy Max-Cut (1/2-Approximation)

**Greedy Max-Cut**: place each vertex on the side that maximizes its crossing-edge count, one at a time.

- Output: at least m/2 edges cross.
- OPT ≤ m trivially.
- ⇒ Output ≥ (1/2)·OPT. **1/2-approximation.**

Stunningly simple, no clever construction. The greedy works *because* any vertex's contribution to the cut is at least half its degree (it picks the better side).

### VertexCoverApprox (2-Approximation via Maximal Matching)

**Algorithm**:
```
C ← ∅
while G has any edge:
    pick an edge (u, v)
    add both u and v to C
    remove all edges incident to u or v
return C
```

- Equivalently: build a maximal matching M; return both endpoints of each matched edge.
- OPT must cover every edge in M ⇒ OPT ≥ |M|.
- Output |C| = 2|M| ≤ 2·OPT. **2-approximation.**
- Runtime: O(n + m).

**Counterintuitive**: this algorithm picks both endpoints of an arbitrary edge — looks "wasteful" — but achieves 2-approximation. The natural greedy (pick highest-degree vertex) achieves *no* constant ratio.

### Greedy Vertex Cover Has No Constant Ratio

**Greedy**: repeatedly pick the highest-degree vertex; add to cover; remove its edges.

[[Lecture 31 — Approximation Algorithms]] showed greedy is **not a 1.33-, 1.74-, 2.08-, 3-, 10-, or 999,999-approximation** — for any constant α there's a graph where greedy outputs > α·OPT.

The construction (Ryan O'Donnell): a bipartite graph designed so that greedy is repeatedly tempted to take "high-degree trap" vertices on one side, eventually forcing it to also cover the small side.

**Key lesson**: an intuitive greedy may have unbounded worst-case approximation ratio. Approximation guarantees require careful analysis — natural greediness doesn't suffice.

## Hardness of Approximation

Some problems are not just NP-hard to solve exactly, but also NP-hard to approximate within certain ratios. Examples (not derived in CSCE 411 but worth knowing):

- TSP (general metric): no constant-factor approximation unless P = NP.
- TSP (metric / triangle inequality): 1.5-approximation via Christofides.
- Vertex Cover: hard to approximate within (2 − ε) under the Unique Games Conjecture; 2 is tight.
- Max-3SAT: hard to approximate within 7/8 + ε (Håstad).

The 2-approximation for Vertex Cover is, in this sense, *optimal under widely-believed assumptions*.

## Relationship to Other Topics

- [[Linear Programming]]: LP relaxation + rounding is a major approximation technique. Bipartite VC is solved exactly via LP (totally unimodular); general VC has an LP-rounding 2-approximation (round any variable ≥ 1/2 up).
- [[Maximum Weight Independent Set]]: NP-hard on general graphs; tree DP gives exact poly-time on trees — a "special case" rather than approximation.
- [[Subset Sum]]: O(nT) DP is pseudopolynomial; an FPTAS rounds the items to a coarse scale and runs the DP, achieving (1+ε)-approximation in poly(n, 1/ε).
- [[Greedy Algorithms]]: many approximations are greedy; some greedies (like max-cut) work, others (vertex cover) fail badly.

## See Also

- [[Vertex Cover]]
- [[NP Completeness]]
- [[Greedy Algorithms]]
- [[Linear Programming]]
- [[Maximum Weight Independent Set]]
- [[Subset Sum]]
- [[Lecture 31 — Approximation Algorithms]]
- [[CSCE 411]]
