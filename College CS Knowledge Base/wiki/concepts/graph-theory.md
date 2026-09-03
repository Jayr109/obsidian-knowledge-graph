---
title: "Graph Theory"
type: concept
tags: [graphs, graph-theory, adjacency-matrix, adjacency-list, handshake-lemma, dag]
sources: [lecture-8-graphs, lecture-9-bfs-and-dfs]
course: CSCE 411
updated: 2026-04-09
---

# Graph Theory

A graph is a mathematical structure representing pairwise relationships between objects. Graphs are among the most versatile tools in CS — many problems can be reduced to graph problems.

> "If your problem doesn't have a graph, try to make it have a graph!"
> — CSCE 411, Lecture 8

## Graph ADT

A graph G = (V, E) consists of:
- A set of **vertices** (nodes) V
- A set of **edges** E, where each edge connects two vertices

Standard notation: **n = |V|**, **m = |E|**

Key operations:
- `check_adjacency(u, v)` — is there an edge between u and v?
- `get_edges(v)` — return all neighbors of vertex v

## Types of Graphs

- **Undirected**: edges are unordered pairs {u, v}; {u,v} = {v,u}
- **Directed (digraph)**: edges are ordered pairs (u, v); direction matters
- **Weighted**: edges or vertices carry numeric weights
- **Simple**: no self-loops or multi-edges (default assumption unless stated otherwise)

## Terminology

| Term | Definition |
|---|---|
| Degree deg(v) | Number of edges incident to v (undirected) |
| In-degree | Number of incoming edges (directed) |
| Out-degree | Number of outgoing edges (directed) |
| Regular graph | All vertices have the same degree |
| Walk | Sequence of vertices connected by edges (repetition allowed) |
| Path | Walk with no repeated vertices |
| Cycle | Walk of positive length from v to v, no repeated edges or vertices |
| Connected | Every pair of vertices has a path between them (undirected) |
| Component | Maximal connected subgraph |
| DAG | Directed acyclic graph — models dependencies |

## Handshake Lemma

**Σ deg(v) = 2|E|**

Each edge contributes exactly 2 to the total degree sum (one for each endpoint).

**Application**: every 3-regular graph has an even number of vertices.
- Proof: 3n = Σ deg(v) = 2m, so 3n is even, which means n must be even. ∎

## Graph Representations

| Representation | Space | Adjacency Query | Neighbor Iteration |
|---|---|---|---|
| Adjacency Matrix | O(n²) | O(1) | O(n) |
| Adjacency List | O(n + m) | O(deg(v)) | O(deg(v)) |

- **Adjacency matrix**: n × n boolean matrix. Fast lookup; expensive in space for sparse graphs.
- **Adjacency list**: array of lists, one per vertex. Preferred for sparse graphs (m << n²).

## Applications

| Domain | Vertices | Edges |
|---|---|---|
| Social networks (Facebook) | People | Friendship (undirected) |
| Social networks (Twitter) | Accounts | Follow (directed) |
| Web graph | Web pages | Hyperlinks (directed) |
| Transportation | Cities/stations | Roads/routes (weighted) |
| Images | Pixels | Pixel adjacency |
| Register allocation | Variables | Interference |
| Dependency graphs | Tasks/packages | Dependencies (DAG) |

## See Also

- [[BFS and DFS]]
- [[SSSP]]
- [[Minimum Spanning Trees]]
- [[Maximum Flow]]
- [[CSCE 411]]
