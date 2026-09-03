---
title: "Lecture 15 — Maximum Flow"
type: source
tags: [max-flow, ford-fulkerson, edmonds-karp, residual-graph, min-cut]
sources: [lecture-15-maximum-flow]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 15 — Maximum Flow

CSCE 411, Calvin Beideman, 29 slides.

## Flow Networks

A **flow network** is a directed graph G = (V, E) with:
- A **source** s and **sink** t
- Edge **capacities** c(u, v) ≥ 0

A **flow** f assigns a value f(u,v) to each edge satisfying:
- **Capacity**: 0 ≤ f(u,v) ≤ c(u,v)
- **Conservation**: flow in = flow out for every vertex except s and t

**Max-flow problem**: maximize total flow from s to t.

**Multiple sources/sinks**: add a super-source connected to all sources and a super-sink connected from all sinks, each with infinite capacity.

---

## Historical Context

Ford and Fulkerson (1950s) studied the Soviet railway network — primarily interested in the **min-cut** (the "sabotage problem": which edges to cut to minimally disconnect the network). The max-flow/min-cut duality fell out of that work.

---

## s-t Cut

An **s-t cut** is a partition (S, T) of V with s ∈ S and t ∈ T. The **capacity** of the cut = sum of capacities of edges from S to T.

**Max-Flow Min-Cut Theorem (Ford-Fulkerson, 1956)**: The value of a maximum flow equals the capacity of a minimum s-t cut.

---

## Residual Graph

Given flow f on G, the residual graph G_f has:
- **Forward edge** (u, v): residual capacity c(u,v) − f(u,v) (can push more)
- **Backward edge** (v, u): residual capacity f(u,v) (can cancel existing flow)

An **augmenting path** is any s-t path in G_f. Augmenting along it increases total flow by the bottleneck (minimum residual capacity on the path).

---

## Ford-Fulkerson Algorithm

Repeatedly find augmenting paths in the residual graph; stop when none exist.

**Correctness**: by the Max-Flow Min-Cut Theorem — no augmenting path ↔ flow is maximum.

**Runtime**:
- Integer capacities: O(|f*| · m) — each augmentation increases flow by ≥ 1
- Irrational capacities: may not terminate

**Bad case**: two crossing edges with capacity 1000; alternating augmenting path choices → 2000 iterations (exponential in the bit-length of capacities).

---

## Edmonds-Karp Algorithm

Ford-Fulkerson using **BFS** to select augmenting paths (shortest path by hop count).

**Runtime**: O(nm²) — polynomial regardless of capacities or flow values.

---

## Modern Progress

The fastest known max-flow algorithm runs in O(m^(1+o(1))) time (recent theoretical result).

---

## See Also

- [[Maximum Flow]]
- [[Ford-Fulkerson Algorithm]]
- [[Edmonds-Karp Algorithm]]
- [[Bipartite Matching]]
- [[CSCE 411]]
