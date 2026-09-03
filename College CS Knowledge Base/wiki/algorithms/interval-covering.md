---
title: "Interval Covering"
type: algorithm
tags: [greedy, intervals, algorithms]
sources: [exam-3-solutions-sp26]
course: CSCE 411
updated: 2026-05-03
---

Interval Covering asks for the **minimum-size set of integer points** that "stabs" every interval in a collection — i.e., every interval contains at least one chosen point. It is solvable by a greedy algorithm in O(n log n) and is distinct from [[Interval Scheduling]], which selects disjoint intervals rather than placing covering points.

## Problem Definition

**Input**: A set of intervals I = {(s₁,f₁), …, (sₙ,fₙ)} where sᵢ, fᵢ ∈ ℤ≥0 and sᵢ < fᵢ.

**Output**: A minimum-size set S ⊆ ℤ≥0 such that for every interval (sᵢ, fᵢ) ∈ I, there exists x ∈ S with sᵢ ≤ x ≤ fᵢ.

**Example**: I = {(1,7),(2,4),(3,8),(5,6),(7,10)} → S = {2, 6, 7}, size 3.

## Greedy Algorithm

```
IntervalCover(I):
  If I is empty, return ∅
  Sort intervals by finish time (ascending)
  Result ← [f₁]          // add the finish time of the first interval
  For i from 2 to n:
    If sᵢ > last element of Result:
      Append fᵢ to Result
  Return Result
```

**Invariant**: after processing interval i, every interval among (s₁,f₁),…,(sᵢ,fᵢ) is stabbed by some element of Result.

## Correctness

**All intervals covered**: iterating in finish-time order, when we reach (sᵢ, fᵢ):
- If sᵢ ≤ last element of Result (call it x = fⱼ for some j < i): since intervals are sorted by finish, fⱼ ≤ fᵢ, so x ∈ [sᵢ, fᵢ]. Covered.
- If sᵢ > x: we add fᵢ, which trivially covers (sᵢ, fᵢ).

**Minimum size**: each point added to Result is the finish time of some interval (sᵢ, fᵢ) that was not yet covered when we reached it. The start times of these uncovered intervals are strictly increasing (each new uncovered interval starts after the previous result element). Hence the intervals that "forced" each addition are **pairwise disjoint** — any valid cover S must contain a distinct point inside each such interval. Therefore |S| ≥ |Result|.

## Runtime

- Sort: Θ(n log n)
- Single pass: Θ(n)
- **Total: Θ(n log n)**

## Contrast with Interval Scheduling

| Problem | Goal | Output | Algorithm |
|---------|------|--------|-----------|
| [[Interval Scheduling]] | Maximum non-overlapping intervals | Subset of intervals | Earliest-finish-time greedy |
| **Interval Covering** | Minimum stabbing points | Set of integers | Earliest-finish-time greedy (same sort!) |

The sorting key is identical; the greedy decision differs. In scheduling, we select the interval with earliest finish; in covering, we always add the finish time and only add a new one when the current interval is not yet stabbed.

## See Also

- [[Interval Scheduling]]
- [[Greedy Algorithms]]
- [[Exam 3 Solutions — Spring 2026]]
- [[CSCE 411]]
