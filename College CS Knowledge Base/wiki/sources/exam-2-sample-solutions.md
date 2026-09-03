---
title: "Exam 2 Sample Solutions — Spring 2026"
type: source
tags: [csce411, exam, practice, solutions, bfs, dfs, sssp, mst, max-flow, bipartite-matching]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Exam 2 Sample Solutions — Spring 2026

**Source file:** `raw/CSCE411_Sp26_Exam_2_Sample_Solutions (1).pdf`
**Course:** CSCE 411, Spring 2026
**Format:** Practice exam with same format and topic coverage as Exam 2.
**Coverage:** BFS/DFS through Bipartite Matching — same scope as [[Exam 2 Solutions — Spring 2026|Exam 2]].

## T/F Key Results

| Statement | Answer | Reasoning |
|-----------|--------|-----------|
| In undirected graph, DFS tree has no cross edges | **TRUE** | All non-tree edges in undirected DFS are back edges (ancestor–descendant) |
| Directed graph with Hamiltonian path → only 1 SCC | **FALSE** | A Hamiltonian path visits all vertices, but cycles (SCCs > 1) can still exist |
| BFS finds connected components in O(m+n) | **TRUE** | Standard BFS runtime — linear in edges + vertices |
| Dijkstra: each edge relaxed at most once | **TRUE** | With a proper priority queue (decrease-key), each edge is processed once when its source vertex is extracted |
| Prim-Jarník always generates same MST regardless of start vertex | **FALSE** | May produce different MST structures with same total cost when tie-breaking differs |
| Lightest edge with one endpoint in S, one in T is in some MST | **TRUE** if (S,T) is a valid cut; **FALSE** in general | The cut property applies only when (S,T) partitions V — arbitrary S,T sets don't guarantee this |
| Capacity of s-t cut = Σ(c(u,v) − c(v,u)) | **TRUE** | Net capacity definition for directed cuts |
| Edmonds-Karp is polynomial even for arbitrary rational capacities | **TRUE** | Edmonds-Karp (BFS augmentation) runs in O(VE²) regardless of capacity values |
| Fastest known max-flow is O(m^(1+o(1))) | **TRUE** | Recent result (Chen et al. 2022) achieves nearly linear max flow |
| No M-augmenting paths → M is perfect matching | **FALSE** | No augmenting paths → M is a **maximum** matching (largest possible), not necessarily perfect (which requires matching all vertices) |
| Every stable matching instance has a solution | **TRUE** | Gale-Shapley algorithm always terminates with a stable matching |
| LCS recurrence (standard form) | **TRUE** | Standard DP recurrence is correct |

## Relationship to Exam 2

Some T/F questions overlap with [[Exam 2 Solutions — Spring 2026|Exam 2 Solutions]] — this sample exam serves as practice for the same material. Differences in question phrasing reveal important edge cases (e.g., "maximum matching" vs "perfect matching").

## See Also

- [[BFS and DFS]]
- [[SSSP]]
- [[Minimum Spanning Trees]]
- [[Maximum Flow]]
- [[Bipartite Matching]]
- [[CSCE 411]]
