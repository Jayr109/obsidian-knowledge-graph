---
title: "CSCE 420 Lecture 2 — Search and Game Playing"
type: source
tags: [lecture, csce420, search, uninformed, informed, csp, game-playing]
sources: []
course: CSCE 420
updated: 2026-09-01
---

Slide deck 2 of [[CSCE 420]], by [[Yoonsuck Choe]]. 138 slides — the largest deck in the course and the foundation of its first half. Covers uninformed search, informed search, iterative improvement, constraint satisfaction, and game playing.

This is the instructor's own treatment of material that previously existed in this knowledge base only as reconstructions from [[CSCE 420 Midterm Practice]]. Those pages have been reconciled against it.

## Structure

| Slides | Section |
|---|---|
| 1–14 | Search problem definition; the 8-puzzle |
| 15–24 | General search; evaluation criteria; BFS; uniform cost |
| 25–35 | DFS, depth-limited, iterative deepening |
| 36–42 | Bidirectional search; avoiding repeated states |
| 43–55 | Informed search; best-first; heuristic functions; greedy |
| 56–74 | A*; optimality; complexity; heuristic design |
| 75–81 | IDA*; beam search |
| 82–93 | Iterative improvement: hill climbing, simulated annealing |
| 94–101 | Constraint satisfaction search |
| 102–130 | Game playing: minimax, alpha-beta, games of chance |
| 131–138 | Game AI history |

## The Organizing Idea

Every search strategy in the deck is the **same algorithm with a different queuing function** — see [[General Search Algorithm]]. That reduces a dozen algorithms to one design decision: where do newly expanded nodes go in the node list?

| Strategy | Queuing function |
|---|---|
| [[Breadth-First Search]] | Enqueue at end |
| [[Depth-First Search]] | Enqueue at front (stack push) |
| [[Uniform-Cost Search]] | Sorted by $g(n)$ |
| [[Greedy Best-First Search]] | Sorted by $h(n)$ |
| [[A* Search]] | Sorted by $g(n) + h(n)$ |

## Terminology the Deck Insists On

> **A visit is the act of fetching a node out of the node list and goal-testing it.** Visit is *different* from expand.

Time complexity is counted in visits. Depth is 0 at the root. Both conventions matter for reading the complexity results correctly, and both are stated as explicit notes on the slides.

## The Space Argument

The deck's through-line for uninformed search is that **space, not time, is the binding constraint**. BFS is complete and optimal but needs $O(b^{d+1})$ memory; DFS needs only $O(bm)$ but is incomplete. [[Iterative Deepening Search]] resolves this — DFS's space with BFS's guarantees, at a constant-factor cost in repeated work.

The same argument recurs one level up: [[A* Search]] is complete and optimal but usually exponential in space, so [[IDA*]] applies the identical iterative-deepening trick with $f$-cost in place of depth.

## Results Worth Extracting

- **A* optimality**: $f(n) \le f(G_1) < f(G_2)$, which holds exactly because $h$ is admissible.
- **A* subexponential condition**: $|h(n) - h^*(n)| \le O(\log h^*(n))$ — and the lecture's verdict that most heuristics fail it, making exponential space the normal case.
- **Dominance**: at depth 14, iterative deepening visits 3,473,941 nodes; A* with $h_1$ visits 539; A* with $h_2$ visits 113. See [[Admissible Heuristics]].
- **IDA* worst case**: if each $f$-contour adds one node, IDA* visits $O(N^2)$ where A* visits $N$.
- **Alpha-beta**: perfect ordering gives $b^{m/2} = (\sqrt{b})^m$, so chess's $b=35$ behaves like $b \approx 6$.
- **Greedy vs. A\* on Romania**: 450 vs. 418 — the cost of dropping $g(n)$.

## Visual-Only Slides

Several slides carry only figures or a "google search" placeholder and have no substantive text: the Romania map renderings (52, 60), various supplementary illustration slides (3, 4, 12, 22, 23, 54, 93, 129, 133, 134, 138), and the worked exercise trees for minimax and alpha-beta (110, 118, 119). The exercise solutions in particular are diagrammatic — the alpha-beta solution slide marks A-CUT and B-CUT positions on a tree that is not recoverable from the text layer.

## Pages Created

**New (17)**: [[Search Problem Formulation]], [[General Search Algorithm]], [[Uninformed Search]], [[Breadth-First Search]], [[Depth-First Search]], [[Uniform-Cost Search]], [[Depth-Limited Search]], [[Iterative Deepening Search]], [[Bidirectional Search]], [[Repeated States]], [[Best-First Search]], [[Greedy Best-First Search]], [[Admissible Heuristics]], [[Beam Search]], [[Hill Climbing]], [[Game Playing]], [[Game AI Milestones]]

**Reconciled (10)**: [[A* Search]], [[IDA*]], [[Heuristic Search]], [[Local Search]], [[Simulated Annealing]], [[Constraint Satisfaction Problems]], [[Minimax]], [[Alpha-Beta Pruning]], [[Expectimax]], [[Adversarial Search]]

## See Also

- [[CSCE 420]]
- [[Yoonsuck Choe]]
- [[General Search Algorithm]]
- [[Game Playing]]
- [[CSCE 420 Midterm Practice]]
