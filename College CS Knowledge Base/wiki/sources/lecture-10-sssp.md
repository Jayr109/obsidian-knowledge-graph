---
title: "Lecture 10 — Single Source Shortest Paths"
type: source
tags: [sssp, dijkstra, bellman-ford, graph, shortest-paths, bfs]
sources: [lecture-10-sssp]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 10 — Single Source Shortest Paths

CSCE 411, Calvin Beideman, 49 slides.

## Overview

**SSSP (Single Source Shortest Paths)**: given a weighted directed graph and a source vertex s, find the shortest path from s to every reachable vertex. The output is a **shortest path tree** rooted at s.

Shortest path trees are not necessarily unique. BFS gives a valid shortest path tree for unweighted graphs.

---

## BFS for SSSP (Unweighted)

BFS visits vertices in increasing distance (hop count) order from the source. This makes it correct for unweighted SSSP.

- **Runtime**: O(n + m)
- Produces a valid shortest path tree

---

## Tense Edges and Relaxation

A **tense edge** is an edge (u, v) where:

```
dist[v] > dist[u] + w(u,v)
```

**Relaxing** a tense edge means updating dist[v] = dist[u] + w(u,v).

---

## The Universal SSSP Algorithm (Ford/Dantzig/Minty, 1950s)

> Repeatedly relax tense edges until none remain.

All SSSP algorithms are special cases of this framework — they differ only in which tense edge is relaxed next and how the graph is structured.

---

## Dijkstra's Algorithm (Non-Negative Weights)

Always extract the minimum-distance unvisited vertex, then relax all its outgoing edges.

**Correctness invariant**: when a vertex is extracted from the priority queue, its distance is final.

**Proof sketch**: all edge weights are non-negative, so no future relaxation can improve the distance to an already-extracted vertex.

**Fails for negative edges**: a negative edge can reduce the distance of an already-finalized vertex, but Dijkstra never revisits it.

**Runtime**:
| Priority Queue | Runtime |
|---|---|
| Binary heap | O((n + m) log n) |
| Fibonacci heap | O(m + n log n) — optimal for general graphs |

---

## Bellman-Ford (Negative Edges, No Negative Cycles)

Run n−1 rounds; each round relaxes all m edges.

- **Runtime**: O(nm)
- **Negative cycle detection**: if any edge is still tense after n−1 rounds, a negative cycle exists on some path from s

---

## DAG Shortest Paths

Process vertices in topological order, relaxing all outgoing edges at each step.

- **Runtime**: O(n + m)
- Works with negative edges (no cycles possible in a DAG)

---

## Algorithm Comparison

| Graph Type | Algorithm | Runtime |
|---|---|---|
| Unweighted | BFS | O(n + m) |
| Non-negative weights | Dijkstra (binary heap) | O((n + m) log n) |
| Non-negative weights | Dijkstra (Fibonacci heap) | O(m + n log n) |
| Negative edges, no neg cycles | Bellman-Ford | O(nm) |
| DAG (any weights) | DAG Shortest Paths | O(n + m) |

**Negative cycles**: SSSP is undefined if a negative cycle lies on any path from s to the target — the path length can be made arbitrarily small by looping.

---

## See Also

- [[BFS and DFS]]
- [[Dijkstra's Algorithm]]
- [[Bellman-Ford Algorithm]]
- [[Graph Theory]]
- [[SSSP]]
- [[CSCE 411]]
