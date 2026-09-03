---
title: "Bipartite Matching"
type: concept
tags: [bipartite-matching, matching, stable-matching, max-flow, gale-shapley]
sources: [lecture-16-bipartite-matching]
course: CSCE 411
updated: 2026-04-09
---

# Bipartite Matching

Bipartite matching finds the maximum set of edges with no shared endpoints in a bipartite graph. It is solvable in polynomial time and many natural optimization problems reduce to it.

## Definitions

- **Bipartite graph**: vertices split into L and R; edges only between L and R
- **Matching**: set of edges with no shared vertex
- **Maximum matching**: largest matching; size ≤ min(|L|, |R|)
- **Perfect matching**: every vertex is matched; requires |L| = |R|
- **M-augmenting path**: alternating path (unmatched → matched → unmatched...) starting and ending at unmatched vertices; exists ↔ matching is not maximum

## Reduction to Max Flow

Add super-source s with unit-capacity edges to all L vertices; add super-sink t with unit-capacity edges from all R vertices; all L→R edges have capacity 1.

**Max flow = max matching.**

Since all capacities are integers, max flow produces an integer flow, which corresponds directly to a valid matching.

**Runtime**: O(m · n) using Edmonds-Karp on this network (|f*| ≤ n)

## Stable Matching

When participants have preference lists, a **stable matching** has no **unstable pair** — a pair (a, b) where a prefers b over their current match AND b prefers a over their current match.

**[[Gale-Shapley Algorithm]]**: hospitals make offers to their top remaining doctor; doctors hold the best offer received and reject the rest. Always produces a stable matching in O(n²).

**Properties**:
- Hospital-optimal: best achievable for hospitals across all stable matchings
- Doctor-pessimal: worst achievable for doctors across all stable matchings
- Reversing (doctors make offers) → doctor-optimal, hospital-pessimal

## LP Formulation and König's Theorem

Bipartite matching can be formulated as an integer program (one 0/1 variable xₑ per edge, degree constraint per vertex). See [[LP Relaxation]].

**The LP relaxation has an integral optimum** on bipartite graphs: the LP is equivalent to max flow in a unit-capacity network; since capacities are integral, [[Edmonds-Karp Algorithm]] finds an integral solution.

**The dual LP** of the bipartite matching LP is the minimum vertex cover LP (one variable yᵥ per vertex, constraint yᵤ + yᵥ ≥ 1 per edge). By strong LP duality and integrality of both primal and dual:

> **König's Theorem**: in every bipartite graph, max |M| = min |C| (max matching size = min vertex cover size).

This connects bipartite matching to [[Vertex Cover]] and is a canonical application of LP duality to combinatorics. See [[König's Theorem]] for the full proof.

## See Also

- [[Maximum Flow]]
- [[Gale-Shapley Algorithm]]
- [[Stable Matching]]
- [[König's Theorem]]
- [[LP Relaxation]]
- [[Vertex Cover]]
- [[Homework 7 Solutions — Spring 2026]]
- [[CSCE 411]]
