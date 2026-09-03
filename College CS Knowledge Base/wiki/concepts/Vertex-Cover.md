---
title: "Vertex Cover"
type: concept
tags: [graphs, NP-complete, approximation, vertex-cover, CSCE-411]
sources: [lecture-27-np-verifiers, lecture-31-approximation-algorithms]
course: CSCE 411
updated: 2026-04-27
---

A **vertex cover** of an undirected graph G = (V, E) is a set C ⊆ V such that every edge has at least one endpoint in C. The decision problem **Vertex Cover** asks: given ⟨G, k⟩, is there a vertex cover of size ≤ k? It is NP-complete in general, but tractable on restricted graph classes and admits a clean 2-approximation.

## The Problem

- **Input**: undirected graph G = (V, E), integer k.
- **Question**: ∃ C ⊆ V with |C| ≤ k and every edge has an endpoint in C?

The optimization version (find the smallest vertex cover) is the natural setting; we'll mention both.

## Complexity Status

| Setting | Complexity |
|---|---|
| General graphs (decision) | **NP-complete** |
| General graphs (optimization) | NP-hard; 2-approximation in poly time |
| Trees | Poly-time exact via [[Maximum Weight Independent Set\|tree DP]] |
| Bipartite graphs | Poly-time exact via [[Linear Programming\|LP]] (totally unimodular) |

### NP-completeness

Vertex Cover is in NP: certificate = the cover C; verifier checks |C| ≤ k and that every edge has an endpoint in C — O(m).

NP-hardness: standard reduction Clique ≤_p Vertex Cover via the complement graph. ⟨G, k⟩ ∈ Clique iff ⟨Ḡ, n−k⟩ ∈ Vertex Cover. (Proof: a clique in G is exactly an independent set in Ḡ; the complement of a vertex cover is an independent set; |VC| + |IS| = n.)

## Relation to Independent Set and Clique

For any graph G with n vertices:

$$C \text{ is a vertex cover} \iff V \setminus C \text{ is an independent set}.$$

Hence:
- min Vertex Cover + max Independent Set = n.
- max Independent Set in G = max Clique in Ḡ.

These three problems are **interreducible** via complement / set-complement. All three are NP-complete on general graphs.

## Algorithms

### Trees: Tree DP (Exact, O(n))

Root the tree arbitrarily; for each vertex v compute:

- f(v, 0) = size of min VC of v's subtree where **v is not in the cover**.
- f(v, 1) = size of min VC of v's subtree where **v is in the cover**.

Recurrences (children c):
- f(v, 0) = Σ_c f(c, 1) (every edge (v, c) must have c in the cover, since v isn't).
- f(v, 1) = 1 + Σ_c min(f(c, 0), f(c, 1)).

Answer: min(f(root, 0), f(root, 1)). O(n).

This is the same shape as the [[Maximum Weight Independent Set]] tree DP — the two problems are dual on trees as well.

### Bipartite Graphs: König's Theorem + LP

In a bipartite graph, **min Vertex Cover = max Matching** (König's theorem). Solve max matching by reduction to [[Maximum Flow]] in O(VE), then derive a min VC of equal size.

Equivalently, the natural integer LP for Vertex Cover has a totally unimodular constraint matrix on bipartite graphs, so the LP relaxation has integer optimum — solving the LP gives an exact min VC.

### General Graphs: 2-Approximation via Maximal Matching

```
C ← ∅
while G has any uncovered edge:
    pick an arbitrary uncovered edge (u, v)
    add both u and v to C
    mark all edges incident to u or v as covered
return C
```

- Equivalently: build a maximal matching M; output both endpoints of every matched edge.
- **Approximation ratio**: |C| = 2|M| ≤ 2·OPT, since OPT must cover every edge in M (and M-edges are vertex-disjoint, so OPT needs at least |M| distinct vertices).
- **Runtime**: O(n + m).

This is the canonical example in [[Approximation Algorithms]] — see also [[Lecture 31 — Approximation Algorithms]].

### General Graphs: Why Greedy (Pick Max-Degree) Fails

The "natural" greedy — repeatedly pick the highest-degree vertex, add it to C, remove its edges — has **no constant approximation ratio**. For any α, a graph exists where greedy outputs more than α·OPT vertices.

The matching-based 2-approximation does the seemingly-wasteful thing (take both endpoints) and gets a tight guarantee. The seemingly-clever thing (take the most useful vertex) gets nothing.

Lower bound: under the Unique Games Conjecture, no poly-time (2 − ε)-approximation exists. The matching-based 2-approx is conjecturally tight.

## Why Vertex Cover Is the Canonical Example

Vertex Cover threads through nearly every chapter of CSCE 411 second-half:

- **[[Maximum Flow]] / [[Bipartite Matching]]**: König's theorem connects min VC to max matching on bipartite graphs.
- **[[Linear Programming]]**: bipartite VC = LP solution; general VC has LP-rounding 2-approximation.
- **[[Dynamic Programming]] / [[Graph DP]]**: tree DP solves it exactly on trees.
- **[[Maximum Weight Independent Set]]**: dual problem on the complement.
- **[[NP Completeness]]**: NP-complete via reduction from Clique (or directly from 3-SAT).
- **[[Approximation Algorithms]]**: 2-approximation example; counterexample to the "natural greedy works" intuition.

It's a single concrete problem that demonstrates almost every algorithmic paradigm in the course.

## See Also

- [[Approximation Algorithms]]
- [[NP Completeness]]
- [[Maximum Weight Independent Set]]
- [[Linear Programming]]
- [[Bipartite Matching]]
- [[Maximum Flow]]
- [[Lecture 27 — NP Verifiers]]
- [[Lecture 31 — Approximation Algorithms]]
- [[CSCE 411]]
