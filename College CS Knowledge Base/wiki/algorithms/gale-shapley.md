---
title: "Gale-Shapley Algorithm"
type: algorithm
tags: [stable-matching, gale-shapley, bipartite-matching, deferred-acceptance]
sources: [lecture-16-bipartite-matching]
course: CSCE 411
updated: 2026-04-09
---

# Gale-Shapley Algorithm

Gale-Shapley (also called the **Deferred Acceptance Algorithm**) finds a stable matching between two equal-sized groups (e.g. doctors and hospitals) in O(n²) time. It guarantees a stable matching always exists.

## Algorithm

```
GaleShapley (hospitals make offers):
  All hospitals and doctors are unmatched
  while some hospital h is unmatched and has not offered to all doctors:
    d = h's highest-ranked doctor not yet offered
    if d is unmatched:
      tentatively match (h, d)
    else if d prefers h over current match h':
      unmatch (h', d)
      tentatively match (h, d)
      // h' is now unmatched and will offer again
```

## Termination

Each hospital offers to each doctor at most once → at most n² offers → always terminates.

## Correctness

**Claim**: the returned matching has no unstable pairs.

**Proof**: Let (d, h) be any unmatched pair. Let d' be h's matched doctor.
- If h prefers d' over d → (d, h) is not unstable by definition.
- If h prefers d over d' → h must have offered d before d'. Since d rejected h, d must already be matched to a hospital it prefers over h → (d, h) is not unstable.

## Optimality Properties

- **Hospital-optimal**: each hospital is matched to the best doctor they can be matched with in any stable matching
- **Doctor-pessimal**: each doctor is matched to the worst hospital they can be matched with in any stable matching
- Swapping roles (doctors make offers) → doctor-optimal, hospital-pessimal

## Runtime

O(n²) — at most n² offers, each O(1) with appropriate data structures (preference lists + pointer to next unoffered doctor).

## See Also

- [[Bipartite Matching]]
- [[Stable Matching]]
- [[CSCE 411]]
