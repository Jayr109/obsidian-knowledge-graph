---
title: "Maximum Flow"
type: concept
tags: [max-flow, min-cut, ford-fulkerson, edmonds-karp, flow-network]
sources: [lecture-15-maximum-flow]
course: CSCE 411
updated: 2026-04-09
---

# Maximum Flow

Maximum flow finds the maximum amount of "flow" that can be sent from a source s to a sink t in a directed graph with edge capacities. It models throughput in networks — bandwidth, transportation, supply chains.

## Flow Networks

- Directed graph G = (V, E) with source s and sink t
- Each edge (u, v) has capacity c(u, v) ≥ 0
- A **flow** f assigns f(u, v) to each edge satisfying:
  - **Capacity**: 0 ≤ f(u,v) ≤ c(u,v)
  - **Conservation**: flow in = flow out for all vertices except s and t
- **Value of flow**: total flow leaving s (= total flow entering t)

## Max-Flow Min-Cut Theorem

**Theorem (Ford-Fulkerson, 1956)**: In any flow network, the value of a maximum flow equals the capacity of a minimum s-t cut.

An **s-t cut** (S, T) partitions V with s ∈ S, t ∈ T; its capacity = Σ c(u,v) for u ∈ S, v ∈ T.

## Algorithms

- [[Ford-Fulkerson Algorithm]] — augmenting paths; O(|f*| · m) for integer capacities
- [[Edmonds-Karp Algorithm]] — BFS augmenting paths; O(nm²); polynomial always
- Modern: O(m^(1+o(1))) — recent theoretical result

## Applications

- Soviet railway network (original application, Ford-Fulkerson 1950s)
- [[Bipartite Matching]] (reduce to max flow)
- Project selection, network reliability, baseball elimination
- **Fruit Salad / inventory feasibility** (Final Exam Q5): given x fruit types with inventory A[i], y customers each with per-fruit limits B[i][j] and total demand C[i], check if all customers can be satisfied simultaneously. Reduction: source → fruit vertex fᵢ (capacity A[i]) → customer vertex cⱼ (capacity B[j][i]) → sink (capacity C[j]). Max flow = Σ C[i] iff feasible. Graph has O(x+y) vertices and O(xy) edges; runs in O((xy)^{1+o(1)}).

## See Also

- [[Ford-Fulkerson Algorithm]]
- [[Edmonds-Karp Algorithm]]
- [[Bipartite Matching]]
- [[Linear Programming]]
- [[CSCE 411]]
