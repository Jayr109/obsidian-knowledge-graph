---
title: "Stable Matching"
type: concept
tags: [stable-matching, gale-shapley, bipartite-matching, nrmp]
sources: [lecture-16-bipartite-matching]
course: CSCE 411
updated: 2026-04-09
---

# Stable Matching

The Stable Matching problem asks for a matching between two groups with preference lists such that no pair mutually prefers each other over their current partners.

## Definition

Given sets A and B each of size n, where each element has a ranked preference list over the other set:

- A **matching** pairs each element of A with one element of B
- A pair (a, b) is **unstable** if a prefers b over its current match AND b prefers a over its current match
- A **stable matching** has no unstable pairs

## Existence

Every instance of the stable matching problem has at least one stable matching. This is proven constructively by the [[Gale-Shapley Algorithm]], which always produces one.

## Real-World Applications

- **National Resident Matching Program (NRMP)**: matching medical school graduates to hospital residency programs in the US since 1952
- College admissions and school choice programs
- Organ donor matching

## Asymmetry of Stable Matchings

Multiple stable matchings may exist for the same input. The Gale-Shapley algorithm produces the one that is:
- **Optimal** for the proposing side (best achievable in any stable matching)
- **Pessimal** for the receiving side (worst achievable in any stable matching)

## See Also

- [[Gale-Shapley Algorithm]]
- [[Bipartite Matching]]
- [[CSCE 411]]
