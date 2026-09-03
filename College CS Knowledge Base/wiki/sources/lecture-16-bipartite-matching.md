---
title: "Lecture 16 — Bipartite Matching"
type: source
tags: [bipartite-matching, stable-matching, gale-shapley, max-flow, matching]
sources: [lecture-16-bipartite-matching]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 16 — Bipartite Matching

CSCE 411, Calvin Beideman, 27 slides.

## Matching Definitions

- **Matching**: set of edges with no shared vertices
- **Maximum matching**: largest possible matching
- **Perfect matching**: every vertex is matched; size = n/2; requires |L| = |R| in bipartite graphs
- **Bipartite graph**: vertices split into sets L and R; edges only between L and R. Max matching ≤ min(|L|, |R|).

**Application**: Beideman's own TA-to-lab scheduling problem.

---

## Bipartite Matching via Max Flow

Construct a flow network:
- Add super-source s with unit-capacity edges to all vertices in L
- Add super-sink t with unit-capacity edges from all vertices in R
- Direct all L→R edges with capacity 1

**Max flow = max matching.**

**Correctness**: since all capacities are integers, max flow produces an integer flow, which corresponds directly to a valid matching.

---

## Stable Matching Motivation

**Unstable pair**: a pair (d, h) where doctor d prefers hospital h over their current match AND hospital h prefers doctor d over their current match.

**Stable matching**: a matching with no unstable pairs.

**Simple fix fails**: repeatedly fixing unstable pairs can cycle back to a previous state (Beideman demonstrated a concrete cycling example).

**Real-world**: the **National Resident Matching Program (NRMP)** uses stable matching to assign medical school graduates to residency programs.

---

## Gale-Shapley Algorithm

Hospitals make offers to their top remaining unrejected doctor. Doctors tentatively accept the best offer received so far, rejecting all others.

**Runtime**: O(n²)

**Termination**: each hospital offers to each doctor at most once → at most n² offers.

**Correctness**: if hospital h offered doctor d but d rejected h, d is already matched to a preferred hospital. Therefore the pair (d, h) cannot be unstable.

---

## Optimality Properties

- **Hospital-optimality**: Gale-Shapley matches each hospital with their best achievable doctor across all stable matchings
- **Doctor-pessimality**: Gale-Shapley matches each doctor with their worst achievable hospital across all stable matchings
- Reversing the proposer (doctors make offers) → doctor-optimal, hospital-pessimal

---

## See Also

- [[Bipartite Matching]]
- [[Maximum Flow]]
- [[Gale-Shapley Algorithm]]
- [[Stable Matching]]
- [[CSCE 411]]
