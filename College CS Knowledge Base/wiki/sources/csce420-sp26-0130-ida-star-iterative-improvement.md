---
title: "CSCE 420 Spring 2026 — 01-30 IDA*, Iterative Improvement"
type: source
tags: [csce420, lecture-recording, spring-2026, ida-star, dfs-contour, call-stack, epsilon-admissible, beam-search, hill-climbing, ridge, simulated-annealing]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-01-30
deck: slide02
exam: midterm
updated: 2026-09-17
---

Spring 2026 lecture, 48 min. Heuristic design, the full IDA* recursion traced on the call stack, beam search, and iterative improvement through the start of simulated annealing. Slides 73–89.

> Spring 2026 offering. *"Most likely we'll finish informed search today; iterative improvement and CSP next week, then game playing."* HW1 due Feb 8.

## The Tip That Recurs Every Semester

*"We are all computer scientists, so when we see a search problem we have in our own mind how to do the search. But if you do that, you'll make mistakes. The only way to get a correct answer is to actually follow the algorithm — just execute every step."* The same instruction appears in the Fall 2025 [[CSCE 420 Midterm Review]] for alpha-beta.

Aside: in his own test, **IDS was the only uninformed algorithm that could solve the depth-14 8-puzzle** — 3.4 million visits — versus 535 for A* with h₁ and 113 with h₂.

## Heuristic Design

**Relaxation**, with a concrete tile: to move tile 5 home in the real puzzle you must shuffle several other tiles; Manhattan distance says *"you just need to go 1, 2, 3"* — because the relaxed problem removes the other tiles. Air travel relaxes road travel, giving straight-line distance.

**Composite**: if neither h₁ nor h₂ dominates everywhere, take **max(h₁, h₂)** — admissible, and dominates both. **Statistical**: sample h against true cost, for *"very complex and large tasks where you can't strictly prove admissibility."* See [[Admissible Heuristics]].

## IDA* — The One Algorithm That Is Not General Search

*"All of the other algorithms — BFS, DFS, DLS, IDS, best-first, greedy, A* — are based on general search. IDA* is different. It's recursively implemented."* There is **no node list**; *"the analog of the node list is the call stack, because that's where the memory of the search state is."*

### The recursion, as he traced it

- Initial f-limit = **f(root)**. (A student asked; that is the answer.)
- `DFS-Contour(root, f-limit)`: if f(root) > f-limit, **return f(root) as the new candidate limit** without expanding. If goal, return it. Otherwise recurse into each successor **with the same f-limit**, and return the **minimum** f returned by any child.
- Every call that exceeds the limit pops off the stack immediately. Nodes outside the contour *"are outside the boundary and removed from your memory."*
- The top-level loop re-calls from the **same root** with the new limit — *"just like iterative deepening search."*

He tracked call numbers 1–8 on the board: calls 3, 5, 7, 8 hit the limit and popped; at the deepest point the stack held 1, 2, 4, 6. **Space = height of the call stack = linear in depth**, because the exploration inside each contour is depth-first.

### Time

Depends on **two things**: heuristic quality (as for A*), and **how many distinct values h can take**. Few distinct values → few contours → *"could approach the level of A*."* Worst case the f-limit rises by 1 each round: *"if A* visits n nodes, IDA* visits 1 in the first iteration, then 2, … — n(n+1)/2, on the order of n². This is already exponential, and this is exponential squared."*

**ε-admissible**: *"I'm okay with suboptimality within a range of 10 — increment by 10 instead of 1."* Solution is suboptimal by at most ε. See [[IDA*]].

## Beam Search

Sort as in best-first but keep only the first n — the beam width. For continuous-time domains and huge branching factors. See [[Beam Search]].

## Iterative Improvement — Why It Is a Different Kind of Search

The wiring example: a room with a desk, TV, lamp, and one outlet. *Any* wiring that reaches all three powers them — *"these will all achieve the goal"* — but a tangled one is worse than a tidy one. So every configuration is a solution and the task is **quality**. Same for circuit-board wiring: minimize total wire length and board area. *"These are typical of optimization problems."*

Three methods: **hill climbing** (maximize; pick the better local move), **gradient descent** (minimize; use the partial derivative — direction from its sign, step from its magnitude), **simulated annealing** (allow the wrong direction with some probability).

**Hill climbing vs. greedy best-first** — he made the contrast explicit: greedy has a node list and only a few goal states; hill climbing has **no node list, a single node**, and every state is a goal.

## The Three Failure Modes, Drawn

- **Local maximum**: from the peak, left and right both descend, *"so you're stuck. If you knew the landscape you'd keep going right, but you only look at local information."*
- **Plateau**: *"you may just wander around here randomly for a very long time without making any progress."*
- **Ridge**: viewed from above, a tilted ridge with N/S/E/W-only moves — every one of the four moves loses height. *"If you had another operator that allowed diagonal moves, you could quickly gain height."* The ridge is a failure of the **operator set**, not the landscape.

Remedies: random restart (*"generally an initialization problem"*), keep the n best ([[Beam Search]]), parallel restarts on multicore, and simulated annealing. See [[Hill Climbing]].

## Simulated Annealing — Opening

Metallurgy: cool quickly and *"crystals form and the whole thing becomes brittle — you can shatter it with a hammer."* Cool slowly and internal stress relieves into a stable low-energy state. In SA, **the goal is to minimize energy — the opposite of hill climbing.** ΔE = E_new − E_old: if ≤ 0, accept; if > 0, *"in hill climbing this is not allowed, but here you may accept it with a certain probability."* Ran out of time at the probability formula — continued 02-02. See [[Simulated Annealing]].

## See Also

- [[CSCE 420 Spring 2026 — 01-28 Greedy, A*, Heuristics]]
- [[CSCE 420 Spring 2026 — 02-02 Simulated Annealing, CSP, Game Playing]]
- [[IDA*]]
- [[Local Search]]
- [[CSCE 420]]
