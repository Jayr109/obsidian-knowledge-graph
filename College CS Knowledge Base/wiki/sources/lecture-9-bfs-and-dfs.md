---
title: "Lecture 9 — BFS and DFS"
type: source
tags: [lecture, bfs, dfs, graph-traversal, topological-sort, scc, dag, flood-fill]
sources: [lecture-9-bfs-and-dfs]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 9 — BFS and DFS

**Course**: CSCE 411 | **Slides**: 36

*Note: Exam 1 announced this lecture, covering material through the previous Friday.*

## Whatever-First Search (WFS)

A unified framework for graph traversal. Maintains a "bag" of vertices to visit:

- **Bag = Stack** → Depth-First Search (DFS)
- **Bag = Queue** → Breadth-First Search (BFS)
- **Bag = Priority Queue** → Dijkstra's / Prim's (covered later)

**Runtime**: O(n + m) for all variants — each vertex and edge is processed at most once.

## Trees and Edge Classifications

A WFS produces a **search tree** (BFS tree or DFS tree). Edges in a directed graph are classified:

| Edge Type | Description |
|---|---|
| Tree edge | Edge used to discover a new vertex |
| Forward edge | From ancestor to non-child descendant (DFS only) |
| Back edge | From descendant to ancestor |
| Cross edge | All other edges |

**Key fact**: a graph is acyclic iff DFS finds no back edges.

## Applications

### Flood Fill
Convert an image to a graph (pixels as vertices, adjacency as edges), then run WFS from a seed pixel. Runtime: O(#pixels). Used in paint bucket tools, connected component labeling.

### Cycle Detection
A directed graph has a cycle iff DFS produces a back edge. Detect by maintaining an **ancestor set** during DFS; a back edge points to a vertex currently in the ancestor set.

## DAGs and Dependencies

A **DAG** (directed acyclic graph) models dependency relationships (build systems, course prerequisites, task scheduling). The absence of cycles is what makes topological ordering possible.

## Topological Sort

Orders vertices of a DAG such that for every edge (u, v), u appears before v.

**Algorithm**: reverse postorder of DFS traversal.
- Run DFS; record the **finish time** (postorder) of each vertex.
- Reverse the postorder sequence.

**Common mistake**: preorder DFS traversal (recording when a vertex is first visited) is **not** always a valid topological order.

## Reachability

reach(v) = set of all vertices reachable from v via directed edges = the result of running WFS from v.

## Strongly Connected Components (SCCs)

A **strongly connected component** of a directed graph is a maximal set of vertices such that every vertex is reachable from every other vertex in the set.

**Algorithm** (Kosaraju's / two-pass DFS):
1. Run DFS on G; record finish times.
2. Construct the **reversed graph** G^R (reverse all edge directions).
3. Run DFS on G^R in decreasing order of finish times.
4. Each DFS tree in step 3 is one SCC.

## See Also

- [[BFS and DFS]]
- [[Topological Sort]]
- [[Strongly Connected Components]]
- [[Graph Theory]]
- [[CSCE 411]]
