---
title: "CSCE 420 Homework 1 — Search"
type: source
tags: [csce420, homework, hw1, search, uninformed, informed, a-star, greedy, fall-2026]
sources: []
course: CSCE 420
semester: Fall 2026
exam: midterm
updated: 2026-10-20
---

Homework 1 of the user's **Fall 2026** section. 100 points, 10 problems — 8 written, 2 programming — on [[CSCE 420 Lecture 2 — Search and Game Playing]]. Archived as `raw/CSCE420_HW1_Fall2026.pdf` with the starter notebook `raw/CSCE420_HW1_Fall2026_dfs.ipynb`.

> **Past due; the instructor's key has been released.** This page records what is *asked* and the conventions the sheet lays down, because those conventions are exactly what the midterm tests. The official answers are at [[CSCE 420 Homework 1 Solutions — Fall 2026]].

## Conventions the Sheet Fixes — These Are Exam Conventions

The three notes at the top are the same three the lecture insists on, now stated as grading rules:

| Convention | Statement |
|---|---|
| **Node list order** | `[a, b, c, d, ...]` — `a` is the first element taken out for inspection; the rest are ordered left to right. `Get-First-Node([a, b, c, d ...]) = a`. |
| **Depth** | 0 at the root; +1 per edge downward. Depth = number of operators executed to reach the level. |
| **Visit** | Taking a node *out* of the node list for the goal check. Nodes expanded and *put into* the list are **not yet visited**. |
| **Child order** | Children of a node are explored **left to right** for every method. |
| **Tie-breaking** | When sorting by `h(·)` or `f(·)` and values tie, **put the oldest node ahead of new nodes**. |

The visit definition is the one that decides Problems 1, 2, and 5. See [[General Search Algorithm]].

## Part 1 — Uninformed Search (Problems 1–5, 25 pts)

A 31-node complete binary tree numbered breadth-first (1 at the root; children of *n* are 2*n* and 2*n*+1), exactly the tree used on the lecture slides.

| # | Method | Asked |
|---|---|---|
| 1 | [[Depth-First Search]] | Goal 20. When it is visited: what remains in the node list (in order), and what was visited before it, in order |
| 2 | [[Breadth-First Search]] | Goal 5. Same two questions. Note: when 5 is taken out it has **not** yet been expanded |
| 3 | BFS space | Why is BFS space O(b^(d+1)) and not O(b^d)? |
| 4 | [[Depth-Limited Search]] | Can DLS be incomplete on this *finite* tree? Give an example or explain why not |
| 5 | [[Iterative Deepening Search]] | Goal 10. How many nodes are visited before it — **including repeated visits** across iterations, excluding the goal visit itself |

Problem 5 is the one that checks whether you understand IDS restarts from scratch at each limit. Problem 3 is the depth-convention question — the +1 is the frontier at depth *d*+1 that BFS has already generated when it visits the goal at depth *d*.

## Part 2 — Informed Search (Problems 6–8, 35 pts)

An 8-node weighted graph A–H with edge costs and a heuristic table:

```
h: A=22  B=10  C=22  D=23  E=14  F=16  G=10  H=0
```

| # | Asked |
|---|---|
| 6 | Show *h* is **admissible**: compute h*(n) for every node and check h(n) ≤ h*(n). Work backward from the goal: h*(H)=0, h*(G)=50, h*(D)=24 (shortest of two paths). For C consider both C→D and C→F |
| 7 | Run [[Greedy Best-First Search]] by hand, A to H. Show node-list contents at every iteration, visit order, solution path, and solution cost |
| 8 | Repeat with [[A* Search]]; also show f(n) for every expanded node. Which finds the cheaper solution? |

### The tip in Problem 8 that matters on the exam

*The same node can appear in the node list with different f(n) values depending on the path taken.* Their example: f(D) = 14 + 40 + 23 = 77 via A→C→D, but f(D) = 20 + 23 = 43 via A→D. So **track the path** — write the node with its path as a subscript, `ACD`, and the f-value as another, `ACD₇₇`. This is the mechanical form of the [[Repeated States]] discussion, and it is what makes an A* trace gradeable.

## Part 3 — Programming (Problems 9–10, 40 pts)

Both extend `dfs.ipynb`, which implements DFS on the Figure 2 graph:

- **9** — implement greedy best-first; print the same output as Problem 7.
- **10** — implement A*; print the same output as Problem 8.

Full credit requires a **screenshot of the pinned Colab revision**. A "Homework #1 Explanations" page on Canvas is linked from the assignment.

### The Canvas "Homework #1 Explanation" Page

Read from the Canvas page (screenshots, 2026-09-18). It walks the starter notebook in three parts and fixes the recipe for Problems 9–10:

1. **Tree data structure** — LISP-style nested lists; `[2, [3, 4], 5]` is a root with three children, the middle one a subtree. `expand(node)` returns the node itself, and the caller treats the returned list as *several* nodes to enqueue — the subtlety the [[CSCE 420 Spring 2026 — 01-23 DFS, DLS, IDS, Informed Search Intro|01-23 lecture]] also flagged.
2. **DFS** — the `Visiting:` debug line *is* the visit in the sheet's sense (taken out of the node list). Demo tree `[2, [3, [7, 11]], [9, 20], 5]` with goal "leaf > 10" visits the root, 2, `[3, [7, 11]]`, 3, `[7, 11]`, 7, then matches 11.
3. **`Node` class for graph search** — `MAT` is the adjacency matrix with **row = from, column = to, cell = cost, 0 = no edge**; `H` is the heuristic list indexed by state. Each `Node` carries `state`, `cost` (g so far), `h`, and `path` as a string, so solution path and cost are read straight off the goal node — no parent pointers needed.

**The required recipe:** rewrite `MAT` (8×8) and `H` to exactly match Figure 2; in the Part 2 `dfs()` loop replace `expand()` with `Node.expand()` and `goalp()` with a state check; get plain DFS working on the graph first; then greedy and A* are that same loop with the node list **sorted by h(·) or cost + h(·)** after the enqueue — which is what the placeholder `Node.sort(node_list, eval_fn)` is for. The lecture rule "all code must use the provided data structure and function interface" applies.

## What It Tells You About the Midterm

Everything here is midterm scope — see [[CSCE 420 Midterm Review]]. The Spring 2026 instructor said the exam is *"very similar to the practice exam"* and told students to *"review your homework questions"*; the written problems above are the form those questions take: hand-traces with node lists, an admissibility check, and a greedy-vs-A* comparison.

## See Also

- [[CSCE 420 Homework 1 Solutions — Fall 2026]]
- [[CSCE 420 Midterm Review]]
- [[CSCE 420 Lecture 2 — Search and Game Playing]]
- [[Uninformed Search]]
- [[Admissible Heuristics]]
- [[CSCE 420 Homework 2 — Game Playing, Logic]]
- [[CSCE 420]]
