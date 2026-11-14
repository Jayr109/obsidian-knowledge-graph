---
title: "CSCE 420 Homework 1 Solutions — Fall 2026"
type: source
tags: [csce420, homework, hw1, solutions, answer-key, dfs, bfs, ids, admissibility, greedy, a-star, fall-2026]
sources: []
course: CSCE 420
semester: Fall 2026
exam: midterm
updated: 2026-11-04
---

The **instructor's official released answer key** for Fall 2026 Homework 1, posted after the due date. Archived as `raw/CSCE420_HW1_Fall2026_solutions.pdf`. The assignment itself — asks, conventions and grading rules — is at [[CSCE 420 Homework 1 — Search]].

> **This is the released key, not derived work.** Unlike the practice exams (which ship without answers and whose KB solutions were worked out during ingest), everything below is the instructor's own. Where the key's convention differs from your own working, **the key is what the midterm grades against**.

All problems refer to the sheet's Figure 1 (a binary-ish tree numbered 1–21, children left to right) and Figure 2 (a weighted graph A–H with a heuristic table).

## Uninformed Search (Problems 1–5)

**P1 — DFS, goal 20.** Visit order to that point: `[1, 2, 4, 8, 16, 17, 9, 18, 19, 5, 10, 20]`. Immediately before 20 is taken out the node list is `[20, 21, 11, 3]`, so the nodes **remaining** are `[21, 11, 3]`.

**P2 — BFS, goal 5.** The node list evolves `[1]` → `[2,3]` → `[3,4,5]` → `[4,5,6,7]` → `[5,6,7,8,9]`. Node 5 is then taken out **for the goal check and not yet expanded**, so 10 and 11 were never added: remaining `[6,7,8,9]`, visited `[1,2,3,4,5]`. The "not yet expanded" detail is the whole problem.

**P3 — why BFS space is O(b^(d+1)), not O(b^d).** While visiting depth d, BFS has already **generated and stored the children at depth d+1**; there can be as many as b^(d+1) of them. The frontier therefore holds next-level nodes before the goal is visited.

**P4 — can DLS be incomplete on a finite tree?** **Yes** — whenever the limit is below the goal depth. Worked instance: node 20 sits at **depth 4** via `1 → 2 → 5 → 10 → 20`, so any limit `L < 4` (e.g. L = 3) fails to find it. Finiteness of the tree is irrelevant.

**P5 — IDS node count before goal 10** (repeats counted, goal visit excluded). Node 10 is at depth 3.

| Limit | Visit order | Count |
|---|---|---|
| 0 | `[1]` | 1 |
| 1 | `[1, 2, 3]` | 3 |
| 2 | `[1, 2, 4, 5, 3, 6, 7]` | 7 |
| 3 | `[1, 2, 4, 8, 9, 5]` before the goal | 6 |

**Total 1 + 3 + 7 + 6 = 17.** See [[Iterative Deepening Search]].

## Heuristics and Informed Search (Problems 6–8)

**P6 — admissibility.** Compute h\*(n) backward from the goal H:

| Node | h(n) | h\*(n) |
|---|---|---|
| A | 22 | 44 |
| B | 10 | 80 |
| C | 22 | 64 |
| D | 23 | 24 |
| E | 14 | 60 |
| F | 16 | 17 |
| G | 10 | 50 |
| H | 0 | 0 |

The branch points: `h*(D) = 24` because `D→H` (24) beats `D→G→H` (25 + 50 = 75); `h*(C) = 64` because `C→D→H` (40 + 24) beats `C→F→H` (90 + 17 = 107); `h*(A) = 44` via `A→D` (20 + 24), beating A→C (78), A→E (70) and A→B (93). **h(n) ≤ h\*(n) at every node, so the heuristic is admissible.** See [[Admissible Heuristics]].

**P7 — greedy best-first, A to H.** Ties broken **oldest first**. Node lists: `[A_22]` → `[B_10, E_14, C_22, D_23]` → `[G_10, E_14, C_22, D_23]` → `[H_0, E_14, C_22, D_23]`, then H is visited and the search stops. Visit order `[A, B, G, H]`; path **A → B → G → H**; cost **13 + 30 + 50 = 93**. See [[Greedy Best-First Search]].

**P8 — A\*, same graph.** `f(n) = g(n) + h(n)`, ties oldest first, and **the same node may appear more than once with different f** because the path differs.

| After visiting | Node list |
|---|---|
| — | `[A_22]` |
| A | `[AB_23, AE_24, AC_36, AD_43]` |
| AB | `[AE_24, AC_36, AD_43, ABG_53]` |
| AE | `[AEG_30, AC_36, AD_43, ABG_53]` |
| AEG | `[AC_36, AD_43, ABG_53, AEGH_70]` |
| AC | `[AD_43, ABG_53, AEGH_70, ACD_77, ACF_120]` |
| AD | `[ADH_44, ABG_53, ADG_55, AEGH_70, ACD_77, ACF_120]` |

ADH is next out, its final node is the goal, and the search terminates. Visit order `[A, B, E, G, C, D, H]`; path **A → D → H**; cost **20 + 24 = 44**.

**The comparison the problem is built around: greedy found cost 93, A\* found 44.** Greedy committed to B because h(B) = 10 looked best locally and never reconsidered; A\* kept `AD_43` alive in the list and expanded it once the cheap-looking branches had grown their g. Note `AEG_30` beating `ABG_53` — the same node G reached by a cheaper path. See [[A* Search]].

## Programming (Problems 9–10)

Both build on `dfs.ipynb` and must print the same output as their written counterparts.

**P9 — greedy best-first.** Use **h(n) as the node-list priority**: pop the first node, add its children, re-sort by increasing h, with a **stable sort** so an older node stays ahead on ties. Output reproduces P7 exactly — node lists `[A(22)]`, `[B(10), E(14), C(22), D(23)]`, `[G(10), E(14), C(22), D(23)]`, `[H(0), E(14), C(22), D(23)]`; visit order `[A, B, G, H]`; cost **93**.

**P10 — A\*.** Same loop with **f(n) = g(n) + h(n)** as priority. The path to each node is retained *"because the same graph node can appear in the node list with different g(n) and f(n) values."* Node lists: `[A(22)]`, `[AB(23), AE(24), AC(36), AD(43)]`, `[AE(24), AC(36), AD(43), ABG(53)]`, `[AEG(30), AC(36), AD(43), ABG(53)]`, `[AC(36), AD(43), ABG(53), AEGH(70)]`, `[AD(43), ABG(53), AEGH(70), ACD(77), ACF(120)]`, `[ADH(44), ABG(53), ADG(55), AEGH(70), ACD(77), ACF(120)]`. Visit order `[A, B, E, G, C, D, H]`; path `[A, D, H]`; cost **44**.

## See Also

- [[CSCE 420 Homework 1 — Search]]
- [[CSCE 420 Homework 2 Solutions — Fall 2026]]
- [[CSCE 420 Midterm Review]]
- [[A* Search]]
- [[Admissible Heuristics]]
- [[CSCE 420]]
