---
title: "Lecture 8 — Graphs"
type: source
tags: [lecture, graphs, graph-theory, adjacency-matrix, adjacency-list, handshake-lemma]
sources: [lecture-8-graphs]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 8 — Graphs

**Course**: CSCE 411 | **Slides**: 28

## Motivation

> "If your problem doesn't have a graph, try to make it have a graph!"

Graphs are among the most versatile modeling tools in CS. Real-world examples:
- **Social networks**: Facebook (undirected), Twitter (directed)
- **Web graph**: pages as vertices, hyperlinks as directed edges (digraph)
- **Transportation**: cities as vertices, roads/routes as edges (possibly weighted)
- **Images**: pixels as vertices, adjacency as edges
- **Register allocation**: interference graphs in compilers

## Graph ADT

A graph G = (V, E). Standard notation: n = |V|, m = |E|.

Key operations:
- `check_adjacency(u, v)` — is there an edge between u and v?
- `get_edges(v)` — return all neighbors of vertex v

## Types of Graphs

- **Undirected**: edges are unordered pairs {u, v}; {u,v} = {v,u}
- **Directed (digraph)**: edges are ordered pairs (u, v); direction matters
- **Weighted**: edges or vertices carry numeric weights
- **Simple**: no self-loops, no multi-edges (default assumption)

## Degree and the Handshake Lemma

- **Degree** deg(v): number of edges incident to v (undirected)
- **In-degree / Out-degree**: for directed graphs
- **Handshake Lemma**: Σ deg(v) = 2|E| (each edge contributes 2 to the total degree sum)
- **Regular graph**: all vertices have the same degree
- **Theorem**: every 3-regular graph has an even number of vertices.
  - Proof: 3n = Σ deg(v) = 2m, so n = 2m/3; for n to be an integer, m must be divisible by 3, and n must be even.

## Representations

| Representation | Space | Adjacency Query | Neighbor Iteration |
|---|---|---|---|
| Adjacency Matrix | O(n²) | O(1) | O(n) |
| Adjacency List | O(n + m) | O(deg(v)) | O(deg(v)) |

- **Adjacency matrix**: n×n boolean matrix; A[i][j] = 1 iff edge (i,j) exists. Fast lookup but expensive in space for sparse graphs.
- **Adjacency list**: array of lists, one per vertex. Space-efficient for sparse graphs (m << n²).

## Graph Terminology

- **Walk**: sequence of vertices connected by edges (vertices and edges may repeat)
- **Path**: walk with no repeated vertices
- **Cycle**: walk of positive length from v back to v, no repeated edges or vertices
- **Connected**: every pair of vertices has a path between them (undirected)
- **Component**: maximal connected subgraph
- **DAG**: directed acyclic graph; models dependencies

## See Also

- [[Graph Theory]]
- [[BFS and DFS]]
- [[CSCE 411]]
