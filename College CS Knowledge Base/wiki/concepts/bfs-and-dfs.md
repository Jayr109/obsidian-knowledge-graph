---
title: "BFS and DFS"
type: concept
tags: [graph, bfs, dfs, traversal, sssp, topological-sort, scc]
sources: [lecture-10-sssp]
course: CSCE 411
updated: 2026-04-09
---

# BFS and DFS

BFS (Breadth-First Search) and DFS (Depth-First Search) are the two canonical graph traversal algorithms, both special cases of **Whatever-First Search (WFS)**. They form the foundation for dozens of graph algorithms.

## Whatever-First Search (WFS)

General framework: maintain a "bag" of vertices to visit; extract one, mark it, add unvisited neighbors.

- **DFS**: bag = **stack** (LIFO) → goes deep before backtracking
- **BFS**: bag = **queue** (FIFO) → visits all vertices at distance k before distance k+1

**Runtime**: O(n + m) for both — each vertex and edge is processed at most once.

---

## BFS Trees and DFS Trees

Each traversal produces a rooted spanning tree. Edge classifications:

| Edge Type | Description |
|---|---|
| Tree edge | Used to discover a new vertex |
| Forward edge | (u,v) where u is ancestor of v (non-tree, DFS only) |
| Back edge | (v,u) where u is ancestor of v — indicates a cycle |
| Cross edge | Neither endpoint is an ancestor of the other |

In undirected graphs: BFS and DFS trees have only tree edges and (for DFS) back edges.

---

## BFS for SSSP (Unweighted)

BFS visits vertices in order of increasing hop-distance from the source. The BFS tree is a valid **shortest path tree** for unweighted graphs.

The DFS tree is **NOT** a shortest path tree.

---

## DFS Applications

### Cycle Detection

A directed graph contains a cycle if and only if DFS finds a back edge.

**Implementation**: track the "ancestor set" (vertices currently on the DFS call stack) using a boolean array. A back edge is one leading to a vertex in the ancestor set.

### Topological Sort

For a DAG: reverse postorder of DFS traversal.

- Preorder (DFS discovery order) is **NOT** always a topological sort.
- **Algorithm**: run DFS; when a vertex finishes (all descendants visited), prepend it to the output list.
- **Runtime**: O(n + m)

### Strongly Connected Components (SCCs)

A maximal set of vertices where every vertex can reach every other.

**Algorithm** (two DFS passes, e.g. Kosaraju): one DFS on G to record finish times, one DFS on G-reversed in reverse finish-time order. Each DFS tree in the second pass is one SCC.

---

## Reach

`reach(v)` = all vertices reachable from v via directed paths = result of WFS from v.

In undirected graphs, `reach(v)` = connected component of v.

---

## See Also

- [[Graph Theory]]
- [[SSSP]]
- [[Topological Sort]]
- [[Strongly Connected Components]]
- [[CSCE 411]]
