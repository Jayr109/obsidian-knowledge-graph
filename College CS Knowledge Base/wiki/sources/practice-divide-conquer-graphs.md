---
title: "Practice — Divide & Conquer and Graphs"
type: source
tags: [csce411, practice, divide-and-conquer, binary-search, graphs, trees]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Practice — Divide & Conquer and Graphs

**Source file:** `raw/CSCE_411_Divide___Conquer_and_Graphs_Practice_Solutions (1).pdf`
**Course:** CSCE 411, Spring 2026
**Topics:** Divide & Conquer, Binary Search variants, Graph Theory proofs

## Problem 1: Fixed-Point Search

**Problem:** Given a sorted array A of distinct integers, find an index i such that A[i] = i (a "fixed point"), or report none exists.

**Key observation:** Define h(i) = A[i] − i. Since A contains distinct integers and is sorted, h is strictly monotone increasing. If a fixed point exists, h(i) = 0.

**Solution:** Binary search on h:
1. Compute h(mid) = A[mid] − mid
2. If h(mid) = 0: found a fixed point at mid
3. If h(mid) > 0: fixed point (if any) must be to the left — search left half
4. If h(mid) < 0: fixed point (if any) must be to the right — search right half

**Runtime:** O(log n) — standard binary search on a monotone function.

## Problem 2: Flawed Tree Proof

**Flawed claim:** "Every n-vertex graph with n−1 edges is a tree."

**Why the proof is flawed:** This statement is **FALSE** — the converse of a true statement was assumed.

**True statement:** Every tree with n vertices has exactly n−1 edges.
The converse (n vertices + n−1 edges → tree) is **not always true.**

**Counterexample:**
- Take a triangle (3 vertices, 3 edges forming a cycle): K₃
- Add one isolated vertex (4th vertex, no additional edges)
- Result: 4 vertices, 3 edges = n−1 edges for n=4
- But this graph is NOT a tree: it contains a cycle (the triangle) and the 4th vertex is disconnected

A tree must be both **connected** and **acyclic**. The correct characterization requires: n vertices, n−1 edges, AND connected (or equivalently, AND acyclic). Any two of the three properties {n vertices, n−1 edges, connected, acyclic} together imply the third for a simple graph.

## See Also

- [[Binary Search]]
- [[Divide and Conquer]]
- [[Graph Theory]]
- [[CSCE 411]]
