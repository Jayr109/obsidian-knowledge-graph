---
title: "CSCE 411"
type: course
tags: [algorithms, course, undergraduate]
sources: [lecture-2-proofs-programs-problem-solving, lecture-4-decidability-and-undecidability, lecture-5-undecidability-reductions, lecture-6-asymptotic-analysis, lecture-7-divide-and-conquer, lecture-8-graphs, lecture-9-bfs-and-dfs, lecture-10-sssp, lecture-11-msts, lecture-15-maximum-flow, lecture-16-bipartite-matching, lecture-18-backtracking, lecture-19-dynamic-programming-1, lecture-20-dynamic-programming-2, lecture-22-graph-dp, lecture-23-greedy-algorithms, lecture-24-linear-programming, lecture-25-linear-programming-2, lecture-26-np, lecture-27-np-verifiers, lecture-28-np-completeness, lecture-29-np-hardness-proofs, lecture-31-approximation-algorithms, notes-section-1-foundational-notation, notes-section-2-logic-and-proofs, notes-chapter-3-decidability, exam-1-solutions, exam-2-solutions, exam-2-sample-solutions, exam-3-solutions-sp26, final-exam-sp26, hw2-solutions, hw3-solutions, hw4-solutions, hw5-solutions, homework-6-solutions-sp26, homework-7-solutions-sp26, practice-proofs, practice-undecidability, practice-asymptotic-analysis, practice-divide-conquer-graphs, practice-shortest-paths-msts, practice-dynamic-programming, practice-dp-and-greedy, practice-np-hardness, np-hardness-scribbles]
updated: 2026-08-27
---

CSCE 411 is an undergraduate algorithms course taught by [[Calvin Beideman]]. It covers the design and analysis of algorithms, progressing from graph traversal through dynamic programming, greedy algorithms, linear programming, NP-completeness, and approximation algorithms.

## Instructor

[[Calvin Beideman]] — whose academic lineage traces directly to Robert Floyd (of [[Floyd-Warshall]]).

## Lectures Ingested

All 23 ingested lecture decks. Lectures 3, 12, 13, 14, 17, 21, and 30 are not in the knowledge base.

| # | Lecture | Content |
|---|---|---|
| 2 | [[Lecture 2 — Proofs, Programs & Problem Solving]] | [[Proofs and Induction]], [[Loop Invariants]], GCD, InsertionSort |
| 4 | [[Lecture 4 — Decidability and Undecidability]] | [[Turing Machines]], [[Halting Problem]], [[Turing Reductions]] |
| 5 | [[Lecture 5 — Undecidability Reductions]] | reduction proofs practice |
| 6 | [[Lecture 6 — Asymptotic Analysis]] | [[Asymptotic Analysis]], Word-RAM model |
| 7 | [[Lecture 7 — Divide and Conquer]] | [[Divide and Conquer]], [[Binary Search]], [[Karatsuba's Algorithm]], [[Master Theorem]] |
| 8 | [[Lecture 8 — Graphs]] | [[Graph Theory]], representations, Handshake Lemma |
| 9 | [[Lecture 9 — BFS and DFS]] | [[BFS and DFS]], [[Topological Sort]], [[Strongly Connected Components]] |
| 10 | [[Lecture 10 — Single Source Shortest Paths]] | [[SSSP]], [[Dijkstra's Algorithm]], [[Bellman-Ford Algorithm\|Bellman-Ford]], DAG SP |
| 11 | [[Lecture 11 — Minimum Spanning Trees]] | [[Minimum Spanning Trees]], [[Prim-Jarník Algorithm\|Prim-Jarník]], [[Kruskal's Algorithm]], [[Disjoint Sets]] |
| 15 | [[Lecture 15 — Maximum Flow]] | [[Maximum Flow]], [[Ford-Fulkerson Algorithm\|Ford-Fulkerson]], [[Edmonds-Karp Algorithm\|Edmonds-Karp]], max-flow min-cut |
| 16 | [[Lecture 16 — Bipartite Matching]] | [[Bipartite Matching]], [[Gale-Shapley Algorithm\|Gale-Shapley]], [[Stable Matching]] |
| 18 | [[Lecture 18 — Recursive Backtracking]] | [[Backtracking]], memoization intro |
| 19 | [[Lecture 19 — Dynamic Programming (I)]] | [[Dynamic Programming]], top-down vs bottom-up, design framework |
| 20 | [[Lecture 20 — Dynamic Programming (II)]] | [[Longest Increasing Subsequence]], [[Subset Sum]], Cherry Collecting |
| 22 | [[Lecture 22 — Graph DP]] | [[Graph DP]], [[Floyd-Warshall]], [[Maximum Weight Independent Set]] in trees |
| 23 | [[Lecture 23 — Greedy Algorithms]] | [[Greedy Algorithms]], [[Interval Scheduling]], [[Huffman Coding]], exchange arguments |
| 24 | [[Lecture 24 — Linear Programming]] | [[Linear Programming]], feasibility, boundedness, convexity |
| 25 | [[Lecture 25 — Linear Programming (II)]] | standard/equational form, [[Simplex Algorithm]], LP duality |
| 26 | [[Lecture 26 — NP]] | [[NP and Complexity Classes]], verifiers, certificates, 2-COL vs 3-COL |
| 27 | [[Lecture 27 — NP Verifiers]] | verifier proofs, Cook-Levin, Circuit-SAT, SAT, [[Vertex Cover]], TSP, Clique |
| 28 | [[Lecture 28 — NP-Completeness]] | [[Karp Reductions]], NP-hard vs [[NP Completeness\|NP-complete]], HALTS |
| 29 | [[Lecture 29 — NP-Hardness Proofs]] | full chain SAT→3-SAT→3-COL; gadget construction |
| 31 | [[Lecture 31 — Approximation Algorithms]] | [[Approximation Algorithms]], FPTAS, [[Vertex Cover]] 2-approx, Max-Cut greedy |

## Other Ingested Sources

**Course notes:** [[Course Notes — Section 1: Foundational Notation]] · [[Course Notes — Section 2: Review of Logic and Proofs]] · [[Course Notes — Chapter 3: Decidability and Undecidability]]

**Exams:** [[Exam 1 Solutions — Spring 2026]] · [[Exam 2 Solutions — Spring 2026]] · [[Exam 2 Sample Solutions — Spring 2026]] · [[Exam 3 Solutions — Spring 2026]] · [[Final Exam Solutions — Spring 2026]]

**Homework:** [[Homework 2 Solutions — Spring 2026|HW 2]] · [[Homework 3 Solutions — Spring 2026|HW 3]] · [[Homework 4 Solutions — Spring 2026|HW 4]] · [[Homework 5 Solutions — Spring 2026|HW 5]] · [[Homework 6 Solutions — Spring 2026|HW 6]] · [[Homework 7 Solutions — Spring 2026|HW 7]]

**Practice sets:** [[Practice — Proofs]] · [[Practice — Undecidability]] · [[Practice — Asymptotic Analysis]] · [[Practice — Divide & Conquer and Graphs]] · [[Practice — Shortest Paths and MSTs]] · [[Practice — Dynamic Programming]] · [[Practice — DP and Greedy]] · [[Practice — NP-Hardness]] · [[NP-Hardness Scribbles]]

## Exam Notes

- Exam 2 (referenced in Lecture 20): covers BFS & DFS through Dynamic Programming; two sheets of notes allowed.
- Exam 3 (referenced in Lectures 26–27): covers Dynamic Programming, Greedy Algorithms, Linear Programming; two sheets of notes; 4 problems (1 T/F, 1 short answer, 2 proof/algorithm).
- **Final Exam (referenced in Lectures 29 and 31)**: Tuesday May 5, 10:30 AM – 12:30 PM, in classroom. Cumulative. 2 pages of exam aids. 6 problems, drop 1 (1 T/F with ~10 parts, 1 NP-completeness, 4 from earlier-exam material — possibly including topics in scope but not previously asked). Review sheet on NP and sample exam to be posted.

## Key Themes

- All major paradigms (divide & conquer, DP, greedy) rely on **optimal substructure**.
- The distinction between paradigms is how many subproblems they explore: greedy explores 1, DP explores all, D&C explores disjoint ones.
- Correctness proofs for greedy algorithms typically use **exchange arguments**.

## See Also

- [[Overview]]
- [[CSCE 313]] — companion systems course
- [[Dynamic Programming]]
- [[Greedy Algorithms]]
- [[Linear Programming]]
- [[Calvin Beideman]]
