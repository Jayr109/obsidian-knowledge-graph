---
title: "Homework 4 Solutions — Spring 2026"
type: source
tags: [csce411, homework, solutions, shortest-paths, graph-algorithms, bfs, scc, topological-sort]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Homework 4 Solutions — Spring 2026

**Source file:** `raw/CSCE_411_HW4_Sp26_Solutions (1).pdf`
**Course:** CSCE 411, Spring 2026
**Due:** Monday, March 16, 2026
**Topics:** Shortest Paths, Graph Algorithms

## Problem 1: Shortest Paths with Red Edges

**Problem:** Find the shortest s-t path in a graph with two edge types (red/blue), using **at most k red edges**.

**Solution: Graph Layering**

Construct a layered graph G' with k+1 copies of G (layers 0 through k):

- **Blue edges:** Stay within the same layer. If (u,v) is blue in G, add edge (uᵢ, vᵢ) for each layer i.
- **Red edges:** Move to the next layer. If (u,v) is red in G, add edge (uᵢ, v_{i+1}) for each layer i < k.

**Query:** Run BFS on G' from s₀ (vertex s in layer 0) to find the shortest path to any copy tᵢ of t (layers 0 through k). The layer index tracks how many red edges have been used.

**Correctness:** A path from s to t using exactly j ≤ k red edges corresponds to a path from s₀ to tⱼ in G'. The shortest such path in G' corresponds to the shortest constrained path in G.

**Runtime:** G' has O(k·n) vertices and O(k·m) edges. BFS runs in O(k(m+n)).

## Problem 2: Go Club Tournament

**Problem:** A tournament has been played (complete directed graph — each pair has one directed edge representing who beat whom). Find a ranking of players consistent with the majority of match outcomes.

**Solution: SCC Condensation + Topological Sort**

1. Compute the **Strongly Connected Components (SCCs)** of the directed tournament graph.
2. Build the **condensation graph** (DAG of SCCs): each SCC becomes a single node, edges go between SCCs if there's an edge between them in the original graph.
3. **Topologically sort** the condensation DAG — this gives a linear ordering of the SCCs.
4. Within each SCC, players have equivalent results against each other (they form a cycle); order them arbitrarily within the SCC.

**Why this works:** The condensation of any directed graph is a DAG, so a topological sort always exists. The resulting ranking is consistent with the majority of results in the sense that players ranked higher beat (or drew against) those ranked lower in aggregate across SCCs.

**Runtime:** SCC computation via Kosaraju's or Tarjan's algorithm: O(n+m). Topological sort: O(n+m). Total: O(n+m).

## See Also

- [[BFS and DFS]]
- [[SSSP]]
- [[Topological Sort]]
- [[Strongly Connected Components]]
- [[Minimum Spanning Trees]]
- [[CSCE 411]]
