---
title: "Exam 2 Solutions — Spring 2026"
type: source
tags: [csce411, exam, solutions, bfs, dfs, sssp, mst, max-flow, bipartite-matching, gale-shapley]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Exam 2 Solutions — Spring 2026

**Source file:** `raw/CSCE411_Sp26_Exam_2_Solutions.pdf`
**Course:** CSCE 411, Spring 2026
**Format:** 50-minute exam; 2 pages of exam aids allowed.
**Coverage:** BFS/DFS through Bipartite Matching — graph algorithms, SSSP, MST, Max Flow, Matching.

## T/F Key Results

| Statement | Answer | Reasoning |
|-----------|--------|-----------|
| BFS tree for undirected graph has no cross edges | **TRUE** | In undirected BFS, all non-tree edges connect vertices within the same or adjacent BFS layers — no cross edges |
| Undirected DFS tree has no cross edges — all non-tree edges are back edges | **TRUE** | In undirected DFS, any non-tree edge connects an ancestor to a descendant (back edge) |
| DAG with n vertices has n SCCs | **TRUE** | In a DAG, no vertex can reach another vertex and have that vertex reach back — every SCC is a singleton |
| Every directed graph has a topological sort | **FALSE** | Only DAGs (directed acyclic graphs) admit topological orderings; cycles prevent it |
| Dijkstra with Fibonacci heap is fastest for unweighted directed SSSP | **FALSE** | BFS is faster — O(n+m) vs Dijkstra's O(m + n log n) |
| Unique MST when all edge weights distinct | **TRUE** | Cycle property + cut property together imply uniqueness |
| Prim-Jarník (Fibonacci heap) asymptotically faster than Kruskal's for dense graphs | **TRUE** | Prim: O(m + n log n); Kruskal: O(m log m). For dense graphs (m = Θ(n²)), Prim wins |
| Value of flow ≥ value of s-t cut | **FALSE** | By max-flow min-cut theorem, max flow value = min cut capacity; any flow ≤ any cut capacity |
| Ford-Fulkerson with arbitrary augmenting paths: O(2^n) time | **FALSE** | Worse — may not even terminate for irrational capacities; O(2^n) is not a tight bound |
| If all L-vertices have degree \|R\| in bipartite graph → perfect matching exists | **TRUE** | Hall's theorem: every subset of L has enough neighbors in R |
| If M is max matching → no M-alternating paths exist | **FALSE** | M-alternating paths can exist; it's M-augmenting paths (alternating paths that increase matching size) that cannot exist in a maximum matching |
| Gale-Shapley: each hospital gets #1 doctor on list | **FALSE** | Algorithm is hospital-optimal (each hospital gets best possible partner given stable outcomes) but not necessarily their first choice |
| LCS recurrence (standard form) | **TRUE** | Standard DP recurrence for Longest Common Subsequence is correct as stated |

## Long Answer Highlights

### Q2: Max Flow
Specific flow values given in problem; solution involves verifying flow conservation, capacity constraints, and optimality via residual graph / min cut argument.

### Q3: Bipartite Matching — Augmenting Path
**Answer:** The augmenting path found is: **c → f → b → e → a → d**
This is an M-augmenting path in the given bipartite graph — alternating between unmatched and matched edges, starting and ending at unmatched vertices.

## See Also

- [[BFS and DFS]]
- [[SSSP]]
- [[Minimum Spanning Trees]]
- [[Maximum Flow]]
- [[Bipartite Matching]]
- [[Gale-Shapley Algorithm]]
- [[CSCE 411]]
