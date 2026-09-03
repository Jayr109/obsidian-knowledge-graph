---
title: "Minimum Spanning Trees"
type: concept
tags: [mst, prim, kruskal, light-edge, graph, spanning-tree]
sources: [lecture-11-msts]
course: CSCE 411
updated: 2026-04-09
---

# Minimum Spanning Trees

A **Minimum Spanning Tree (MST)** of a weighted undirected connected graph is a spanning tree with minimum total edge weight. MSTs are foundational in network design and optimization.

## Definition

A **spanning tree** of G is a subgraph that is a tree (connected, acyclic) and includes all vertices. A spanning tree of n vertices has exactly n−1 edges.

An **MST** is a spanning tree with minimum sum of edge weights.

## Applications

- Borůvka (1926): designing an electrical grid
- Circuit design: minimize total wire length
- TSP approximation: an MST-based tour is ≤ 2× optimal for metric TSP

## Key Theorem: Light Edge Property

**Theorem**: For every cut (S, T) of G, the lightest edge crossing the cut is in some MST.

This is the foundation for both [[Prim-Jarník Algorithm]] and [[Kruskal's Algorithm]]. Both algorithms greedily add the lightest "safe" edge, justified by this property.

## Algorithms

- [[Prim-Jarník Algorithm]] — grow one tree from a single vertex; structurally like Dijkstra for MSTs
- [[Kruskal's Algorithm]] — process all edges sorted by weight; add if no cycle forms

## Uniqueness

If all edge weights are distinct, the MST is unique.

## Graph Layering (Related Technique)

Creating k+1 copies of a graph to handle constrained path problems (e.g. "at most k toll roads"). Each layer represents using one more constrained edge. Converts a constrained problem to standard BFS/Dijkstra on the layered graph. Runtime: O(k(m + n)).

## See Also

- [[Prim-Jarník Algorithm]]
- [[Kruskal's Algorithm]]
- [[Disjoint Sets]]
- [[Graph Theory]]
- [[CSCE 411]]
