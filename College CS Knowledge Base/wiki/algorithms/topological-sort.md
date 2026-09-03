---
title: "Topological Sort"
type: algorithm
tags: [dag, topological-sort, dfs, graph, ordering]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Topological Sort

A topological sort of a DAG is a linear ordering of its vertices such that for every directed edge (u, v), u appears before v. It exists if and only if the graph is a DAG.

## Problem Definition

**Input**: Directed Acyclic Graph (DAG) G = (V, E)
**Output**: Linear ordering v₁, v₂, ..., vₙ such that for every edge (vᵢ, vⱼ), i < j

**Applications**: course prerequisites, build systems (make/cmake), task scheduling, dependency resolution.

---

## Algorithm: Reverse Postorder DFS

```
TopologicalSort(G):
  Run DFS on G; track finish times
  Output vertices in reverse order of finish time
```

**Key insight**: in DFS, a vertex v finishes (all its descendants are fully explored) before any vertex that v points to finishes. Therefore, reversing finish order yields a valid topological order.

**Why preorder fails**: if DFS starts at A, visits B then C, and there is an edge C→B, then B comes before C in DFS discovery order — but B depends on C, which is wrong.

**Runtime**: O(n + m) — one DFS pass.

---

## Detecting DAGs

A directed graph is a DAG if and only if DFS finds no back edges. Back edge detection can be integrated into the topological sort pass at no extra cost.

---

## Example (from Lecture 9)

Course prerequisites graph: {120, 221, 222, 312, 313, 314, 315, 410, 411}

- DFS postorder (finish order): 410, 313, 315, 312, 411, 222, 314, 221, 120
- Topological sort (reversed): 120, 221, 314, 222, 411, 312, 315, 313, 410

---

## See Also

- [[BFS and DFS]]
- [[Graph Theory]]
- [[Strongly Connected Components]]
- [[CSCE 411]]
