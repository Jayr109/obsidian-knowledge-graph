---
title: "CSCE 420 Spring 2026 — 01-28 Greedy, A*, Heuristics"
type: source
tags: [csce420, lecture-recording, spring-2026, greedy, a-star, admissibility, optimality-proof, f-contour, 8-puzzle, romania]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-01-28
deck: slide02
exam: midterm
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. Full greedy and A* traces on Romania, the A* optimality proof at the board, the subexponential condition with numbers, and the 8-puzzle heuristics. Slides 51–74. He said at the 30-minute mark: *"You can now solve everything in Homework 1, including all the coding problems."*

> Spring 2026 offering. HW1 due Feb 8 and HW2 due Mar 1 are that semester's dates.

## The Greedy Trace, and How the Path Comes Back

Visit A → expand to T, Z, S → sort by h → `[S, T, Z]`. Visit S → expand (not back to the parent) to R, F, O → merge with leftovers and sort → `[F, R, T, Z, O]`. Visit F → only child B (h = 0) goes to the front. Visit B: goal. **Visit order A, S, F, B; cost 140 + 99 + 211 = 450.**

**How the solution path is recovered** — not on the slide: *"When A expands to S, it keeps some information in S saying I came from A. When S expands, S tells F: you came from me, and I already know I came from A."* The path lives in the node's bookkeeping and is read back from the goal. This is what the HW1 notebook's node structure is for.

Contrast he drew on the map: DFS would take leftmost branches to a huge total; BFS would expand the whole frontier around Arad first.

## Why Romania? (Norvig's own answer)

He looked it up. Choosing the US, UK, etc. was rejected because *"readers would bring their own knowledge"* — they know to head east from LA. With Romania, readers have heard of Bucharest but have no idea how to get there from Arad, *"so they are in the same state of knowledge the search algorithm is in."* Madagascar was rejected because too many cities start with A or M; Romania's cities happen to start with distinct letters (A, B, C, D, E, F, G, H, I, L, M, N, O, P, R, S, T, U, V, Z).

## Greedy's Evaluation — When h Is Bad

*"What if the heuristic values are really bad? Then you end up in a systematic search"* — exponential time, and **space equal to time**, *"very similar to a breadth-first search situation."* The slide's O(b^m) is the worst case where h carries no information. See [[Greedy Best-First Search]].

## A* — "f(F) Is Not Unique"

He asked the class directly: is f(F) unique? **No.** Via A→S→F, f(F) = 140 + 99 + 178 = 417. Via A→T→L→…→F it is far larger. *"Even though you reached F, this is very, very important."* The same state carries a different f depending on the path taken to it — this is why HW1 Problem 8 tells you to subscript nodes with their path.

Monotonicity / pathmax was mentioned and dismissed: *"You won't need this in our class."*

## The A* Trace — Two Things Students Miss

Visit order **A, S, R, P, F, B**; cost **418**. Two oddities he dwelt on:

1. **B enters the node list early but is not visited yet.** When P is expanded, B (f = 418) goes in — but F (f = 417) is still ahead of it. *"You have to wait until everything else with a smaller f-value than this B is visited. Then it appears on top."* Goal-test happens on visit, not on generation.
2. **Two C's coexist in the node list.** One expanded from R (f = 526), one from P (f = 615). Same state, different f, both retained.

**Student question: why keep the second C?** His answer: you *could* drop the worse duplicate — *"if C would eventually lead to the goal, this one will never be visited"* — but detecting it means scanning the list for other instances, which *"could be a huge overhead"* if C is at the far end or absent. Fine for small problems; not free in general. This is the [[Repeated States]] tradeoff inside A*.

## The Optimality Proof, Boardwork

Two properties, then one chain:

- **(1) Suboptimality**: f(G₁) < f(G₂), because at any goal h = 0 so f = g, and G₁ is the cheaper goal.
- **(2) Admissibility**: h(n) ≤ h*(n). Add g(n) to both sides: f(n) = g(n) + h(n) ≤ g(n) + h*(n) = f(G₁).

Chain: f(n) ≤ f(G₁) < f(G₂), so **f(n) < f(G₂)**. *"Whenever n and G₂ occupy the node list, n will be moved in front of G₂"* — and this holds for **every** n on the optimal path, so the optimal goal is always reached first. See [[A* Search]].

**Inflated path cost**: a looping path like A→C→E→C→A→F has a larger g, so it sorts behind the direct path and is never visited before it.

## The f-Contour Lemma, Verified on the Data

A* visits in increasing f. Visited nodes: A 366, S 393, R 413, P 415, F 417, B 418 — all ≤ 418. Every unvisited node has f > 418. *"Every node with f less than f* will be visited."* Consequence: a larger admissible h → smaller set below f* → fewer visits.

## The Subexponential Condition, With Numbers

|h − h*| ≤ O(log h*). *"If h* is 100 and we assume log base 10, the error needs to be ≤ 2. If it's 1000, ≤ 3. That's a very strict requirement."* Most heuristics fail it, so **space is usually exponential** — the frontier outside the current contour is retained, *"awfully similar to the breadth-first case."* Motivation for [[IDA*]].

## 8-Puzzle Heuristics, Worked

For the sample state: **h₁ = 7** (misplaced tiles; only 7 is home; blank not counted). **h₂ = 18** — per-tile sliding distances ignoring other tiles (tile 1 needs 2, tile 2 needs 3, …). *"Which is better, h₁ or h₂?"* **h₂ — smaller error** — *"but here's a hidden assumption: both are admissible."*

Reported node counts: h₁ ≈ 540 (he said 545 here and 535 on 01-30; the slide says 539), h₂ = 113, iterative deepening **over 3 million**. *"This is why informed search is very powerful."* See [[Admissible Heuristics]].

## See Also

- [[CSCE 420 Spring 2026 — 01-23 DFS, DLS, IDS, Informed Search Intro]]
- [[CSCE 420 Spring 2026 — 01-30 IDA*, Iterative Improvement]]
- [[CSCE 420 Homework 1 — Search]]
- [[A* Search]]
- [[CSCE 420]]
