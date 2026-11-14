---
title: "CSCE 420 Spring 2026 — 01-21 Uninformed Search"
type: source
tags: [csce420, lecture-recording, spring-2026, search, uninformed, bfs, dfs, general-search, 8-puzzle]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-01-21
deck: slide02
exam: midterm
updated: 2026-09-17
---

Spring 2026 lecture, 50 min, Zoom transcript. First technical lecture: slide02 from the start through the definition of depth-first search (slides 1–27). Archived at `raw/CSCE420_Spring2026_lecture_transcripts/GMT20260121-*.vtt`.

> Spring 2026 offering — dates and deadlines are that semester's. Content is [[CSCE 420 Lecture 2 — Search and Game Playing]] as actually taught.

## Course Rules Stated Here (apply to every homework)

Announced while opening HW1 on Canvas:

- **Individual assignments — no discussion.**
- **All code must use the provided data structure and function interface** in the notebook.
- **All coding assignments require a Colab revision screenshot** for credit.

## Framing He Added

- **Search is underrated.** *"If you cannot come up with a clever solution, you'll end up using search. Search can be the last resort… it should not be too underrated."*
- **Where AI starts.** Uninformed search *"is just something you learn in data structures or algorithms — nothing especially AI about that. Starting from informed search, we enter the territory of AI. This is perhaps the simplest algorithm in AI."* The dividing line is *domain knowledge*.
- **One algorithm, many behaviors.** *"7 or 8 different search algorithms under uninformed and informed search — all of those, except the very last one [IDA*], are based on this general search algorithm, just by changing the queuing function."* See [[General Search Algorithm]].

## The 8-Puzzle Design Decision

The slides list state representations; the lecture explains the **operator** choice. Defining `up/down/left/right` per tile means defining moves for every tile. Instead, **the operators move the blank** — `left` = *move the blank left*. One set of four operators, and illegal moves (blank at an edge) are simply unavailable. This is the "embeds constraints" criterion from [[Search Problem Formulation]] in practice. Also stated: when expanding, *"you don't want to go back to your parent state"* — the first [[Repeated States]] rule, before that topic is formally reached.

Anecdote: the same sliding puzzle appears in *Resident Evil 4*, and the shortest solution was debated at length on Reddit.

## General Search, Traced Live

He walked the loop on the board: make a node from the initial state (state + bookkeeping, including the **path** so the solution can be returned) → node list `[1]` → pop 1 (*"this is a visit"*) → expand to `[2, 3]` → **queuing function** decides placement. After popping 2 and expanding to `[4, 5]`, with `3` still in the list: enqueue-front gives `[4, 5, 3]`, enqueue-back gives `[3, 4, 5]`. *"Your search behavior completely changes just because of the queuing function"* — the front case is DFS, the back case is BFS.

Four criteria, with visit defined again as *"taking out a particular node from the node list."*

## BFS — The Precise Space Bound

The slides give O(b^(d+1)). He derived it: at depth d there are b^d nodes; expanding them produces b · b^d = b^(d+1) in the list. *"To be precise, once you reach the goal you don't expand it any further, so it's b^(d+1) − b."* The big-O is unchanged. This is HW1 Problem 3.

## Why Space Beats Time — The Argument on the Slides Is Only Half of It

*"If you have infinite time, you can just run it and your computer will not crash. But if you run out of memory, it's very quick to just crash."*

His example: the longest continuously running program in history is the **Pioneer 10 flight computer, running since 1972** — over 50 years on very limited storage, because it had time but not space. *"The lesson is space will run out more quickly than time."*

Then two supplementary slides on why exponentials are bad, both of which are image-only in the PDF:

- **Paper folding**: ~42 folds of ordinary paper reaches the Moon; **one more fold is a round trip.**
- **Scale of the universe** (htwins.net/scale2): observable universe ≈ 10^27 m; Planck length ≈ 10^-35 m. The whole range is only ~60 orders of magnitude — and search trees blow past that.

## Uniform Cost, DFS

- **Uniform cost** is BFS with a cost per node — *"it goes through the nodes with the same cost first."* See [[Uniform-Cost Search]].
- **DFS** is *"severely flawed, but you can make it better and better by adding more features"* — DLS, then IDS, which *"would be the best algorithm in uninformed search."* Only the enqueue-at-front definition was reached; the evaluation is next lecture.

## See Also

- [[CSCE 420 Spring 2026 — 01-16 Modern AI, Limitations, Future]]
- [[CSCE 420 Spring 2026 — 01-23 DFS, DLS, IDS, Informed Search Intro]]
- [[CSCE 420 Lecture 2 — Search and Game Playing]]
- [[CSCE 420 Homework 1 — Search]]
- [[Breadth-First Search]]
- [[CSCE 420]]
