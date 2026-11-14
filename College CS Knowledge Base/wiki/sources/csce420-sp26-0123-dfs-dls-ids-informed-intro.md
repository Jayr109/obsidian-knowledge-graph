---
title: "CSCE 420 Spring 2026 — 01-23 DFS, DLS, IDS, Informed Search Intro"
type: source
tags: [csce420, lecture-recording, spring-2026, search, dfs, dls, ids, bidirectional, repeated-states, greedy, heuristic, dfs-ipynb]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-01-23
deck: slide02
exam: midterm
updated: 2026-09-17
---

Spring 2026 lecture, 51 min. Finishes uninformed search (slides 26–42), then opens informed search through the start of the Romania greedy trace (43–53). Includes a live walkthrough of the HW1 starter notebook `dfs.ipynb`.

> Spring 2026 offering. Logistics mentioned — HW1 covering material "through the end of next week," possible Wednesday cancellation for jury duty — are that semester's.

## The dfs.ipynb Walkthrough — Read This Before HW1

The notebook represents a tree as a **nested Python list**: `[2, [7, 11], 5]` is a root with three children — leaf 2, a subtree `[7, 11]`, leaf 5. The goal test `goal_p` is *integer greater than 10*.

**The `expand` function, and its one subtlety:**

- If the node is an **int**, it is a leaf → return `[]` (nothing to expand).
- If the node is a **list**, return the node **itself**.

The subtlety: the list that goes *in* is one node; the identical list coming *out* is treated by the caller as **several nodes** — its elements — which get appended individually. *"It just happens that the way the search task is represented, when you return this node itself, it now has a different meaning."* He recommended running it by hand today to see why the node list grows from 1 item to 3.

**DFS → BFS is one line.** The queuing step is `node_list = expanded + node_list` (front). A commented line below swaps the order to `node_list + expanded` (back). Switching it changes the visit order from `root, 2, [7,11], 7, 11` to `root, 2, [7,11], 5, 7, …` — BFS takes one more step to find the goal here.

**Not included:** iterative deepening. That is left to the student. See [[CSCE 420 Homework 1 — Search]].

## DFS Evaluation — The Failure Mode, Stated Vividly

Incomplete because of infinite branches: *"even if the goal is the second branch at the root, it'll still just miss it — in a very contrived case."* Time O(b^m) — with the goal at the tip you visit everything regardless of strategy. Space is *"really good, linear with depth, because you're only storing these dangling nodes on the path"* — about **b − 1 nodes per level**. Good for many shallow goals; bad for deep or infinite spaces. See [[Depth-First Search]].

## DLS and IDS

- **DLS** gives DFS *"a chance to be complete and optimal, but not always."* The node carries its depth; at the limit, visited nodes are simply not expanded. Non-optimality shown with a deeper goal found first while a shallower one sits unexplored. See [[Depth-Limited Search]].
- **IDS** revisits: node 1 four times, node 2 three times on the demo tree; visit counts *"1 + 3 + 7 + 15 + …, sort of like n squared"* — his loose board estimate; the formal result on the slide is O(b^d). Complete, exponential time (*"you cannot help that in any of these"*), linear space, and **optimal** *"because you are increasing the depth limit one by one — unlike DLS."* His verdict: *"one of the best algorithms if you don't have anything really intelligent to do."* See [[Iterative Deepening Search]].

## Bidirectional and Repeated States

Bidirectional halves the depth: b^(d+1) → b^(d/2). Works for puzzles with an explicit goal state; *"for chess, this may not be good."* See [[Bidirectional Search]].

Repeated states got a board example: four states A–D in a line with left/right operators. The graph is linear, but *"if you run your algorithm you'll end up with a search tree which blows up exponentially with depth"* — the whole subtree under a repeated node is replicated. Don't return to the parent (cheap); avoid cycles (hard to compute); keep a visited list (can itself become exponentially large). See [[Repeated States]].

## Informed Search — Opening

*"Basically the minimum thing you can do in artificial intelligence."* Best-first is *"an abstract search algorithm"* — its behavior depends entirely on the evaluation function plugged in. Greedy sorts by h(n); A* by g(n) + h(n). The only informed algorithm that is *not* best-first-based is IDA*. See [[Best-First Search]].

**Heuristic intuition:** *"H is the best guess, or a pretty good guess, on how far the goal is."* Only requirement: h = 0 at the goal.

**Greedy's failure, on an island map.** With straight-line distance as h, greedy heads for the neighbor closest to the goal — into a *"gulf region without any bridge."* From there the only move is back to the parent, and *"you get back and forth, back and forth — you get stuck."* This is the incompleteness on [[Greedy Best-First Search]] made concrete: h alone has no memory of cost spent.

**Romania, started:** from Arad, neighbors S=253, T=329, Z=374 → sorted `[S, T, Z]` → visit Sibiu → … → Bucharest at cost 450. The full trace resumes next lecture.

## See Also

- [[CSCE 420 Spring 2026 — 01-21 Uninformed Search]]
- [[CSCE 420 Spring 2026 — 01-28 Greedy, A*, Heuristics]]
- [[CSCE 420 Homework 1 — Search]]
- [[Uninformed Search]]
- [[CSCE 420]]
