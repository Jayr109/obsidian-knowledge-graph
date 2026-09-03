---
title: "Lecture 22 — Graph DP"
type: source
tags: [dynamic-programming, graphs, CSCE 411, lecture]
sources: []
course: CSCE 411
updated: 2026-04-09
---

Lecture 22 of [[CSCE 411]], taught by [[Calvin Beideman]]. Covers [[Dynamic Programming]] applied to graph problems — All-Pairs Shortest Paths via [[Floyd-Warshall]] and Maximum Weight Independent Set in trees.

## Source File

`raw/Lecture22_Graph_DP.pptx` — 15 slides

## Learning Objectives

- Develop DP algorithms for graph problems.
- Memoize a DP algorithm using a tree when appropriate.

## Key Topics

### All-Pairs Shortest Paths (APSP)

**Reduction to SSSP**: Run single-source shortest paths from every vertex — O(V · SSSP).

**Divide & Conquer Recurrence**: intermediate approach; leads to O(V³ log V) — less efficient than Floyd-Warshall.

**[[Floyd-Warshall]]**: DP over intermediate vertices, O(V³). Handles negative edges (no negative cycles).

### Fun Fact: Beideman's Academic Lineage

Robert Floyd → Ronald Rivest → Avrim Blum → Santosh Vempala → Karthekeyan Chandrasekaran → [[Calvin Beideman]].

The same Robert Floyd is co-inventor of [[Floyd-Warshall]].

### Independent Sets

- Max Weight Independent Set (MWIS) is NP-hard on general graphs.
- On trees: tractable via tree DP.
- **Key insight**: choose subproblems as subtrees, not subarrays.
- [[Maximum Weight Independent Set]] covers the full recurrence.

### MWIS Example

Tree with nodes weighted 80, 62, 99, 20, 35 (and others); optimal IS = 296 total weight.

## See Also

- [[Graph DP]]
- [[Floyd-Warshall]]
- [[Maximum Weight Independent Set]]
- [[Calvin Beideman]]
- [[CSCE 411]]
