---
title: "Strongly Connected Components"
type: algorithm
tags: [scc, dfs, directed-graph, graph, kosaraju]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Strongly Connected Components

A **Strongly Connected Component (SCC)** of a directed graph is a maximal set of vertices such that every vertex in the set can reach every other vertex in the set. SCCs partition the vertices of any directed graph.

## Definitions

- **Strongly connected**: vertices u and v are strongly connected if there is a path u→v AND a path v→u
- **Weakly connected**: the vertices are connected when edge directions are ignored
- **SCC**: a maximal strongly connected subgraph

The **condensation** of a directed graph (contracting each SCC to a single node) is always a DAG.

---

## Algorithm (Two-Pass DFS / Kosaraju)

Uses G^R: the reversal of G (same vertices, all edges reversed).

```
1. Run DFS on G; record finish times for each vertex
2. Compute G^R (reverse all edges)
3. Run DFS on G^R, processing vertices in decreasing finish-time order
4. Each DFS tree in step 3 is one SCC
```

**Intuition**: the vertex that finishes last in G is the "root" of its SCC. Running DFS on G^R from that root finds exactly the vertices that can reach the root in G — i.e., the full SCC.

**Runtime**: O(n + m) — two DFS passes plus graph reversal, all linear.

---

## Properties

- Every directed graph has a unique SCC decomposition
- The condensation (DAG of SCCs) enables many algorithms that require acyclicity
- A vertex with no outgoing edges in the condensation is a "sink SCC"

---

## See Also

- [[BFS and DFS]]
- [[Topological Sort]]
- [[Graph Theory]]
- [[CSCE 411]]
