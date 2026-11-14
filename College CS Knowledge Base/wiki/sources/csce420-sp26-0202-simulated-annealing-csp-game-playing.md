---
title: "CSCE 420 Spring 2026 — 02-02 Simulated Annealing, CSP, Game Playing"
type: source
tags: [csce420, lecture-recording, spring-2026, simulated-annealing, rejection-method, csp, map-coloring, game-playing, minimax, utility]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-02-02
deck: slide02
exam: midterm
updated: 2026-09-17
---

Spring 2026 lecture, 51 min. Finishes simulated annealing with worked probabilities and the rejection method, covers CSP through the map-coloring exercise, and opens game playing through minimax. Slides 89–111.

## Simulated Annealing — The Two Random Numbers

The algorithm needs **two** random draws per step, which the slide does not spell out:

1. **Pick an action at random.** If ΔE ≤ 0, accept unconditionally.
2. If ΔE > 0, compute P(ΔE) = e^(−ΔE/kT) and **draw a second uniform random number**; accept iff it falls below P. That second draw is the **rejection method**.

### The probabilities, with his numbers

**Fixed T = 5, vary ΔE:** ΔE = 2 → P ≈ 0.7; ΔE = 4 → P ≈ 0.4; ΔE = 10 → very low. *"A slight increase in energy is accepted with pretty high probability; if the increase is very big, the probability decreases significantly."*

**Fixed ΔE = 2, vary T:** T = 1 → P ≈ 0.1; T = 5 → P ≈ 0.65; T = 10 → P ≈ 0.82. Higher temperature → more suboptimal moves accepted.

So two knobs: **how bad the move is**, and **how hot the system is**. See [[Simulated Annealing]].

### The rejection method

Generate uniform points in [0, 1]. Those below P are accepted, those above rejected; with enough trials *"about 70% of the points would be accepted and 30% rejected."* He demoed a Python screencast on Canvas (Resources → rejection method) with a clear boundary at **0.3** — that is the `demos/rejection-method.mp4` file, archived as `raw/CSCE420_demo_rejection-method.mp4`: a scatter of accepted (blue, x < 0.3) and rejected (orange) samples with a running accept/reject bar chart. Two random numbers in the script: one picks the action, one is compared to P.

### Schedule and applications

Start hot (*"T = 10, most moves accepted even with high energy increase"*), then decrease — the **temperature reduction schedule**. Too fast → stuck in a local minimum; too slow → wasted time early. Linear vs. quadratic decrease is *"dependent on the particular domain."* To maximize instead, minimize −E.

Applications: VLSI wire routing and placement (minimize area and wire length), scheduling, traffic control — and **neural network training**: *"initially a high learning rate, then gradually decrease it"* is the same concept. Connects to [[Gradient Descent]].

## CSP — The Map-Coloring Exercise, Fully Worked

Four regions v1–v4, colors {R, G, B}, no adjacent regions the same. Given v1 = Red, v2 = Green:

**Variable selection** — which of v3, v4 next? v3 borders both colored regions (two active constraints: not green, not red); v4 borders one. **Most-constrained-variable → pick v3.**

**Value selection** — suppose v4 is chosen; it cannot be green, so red or blue. If **blue**: v3 then cannot be red, green, *or* blue — unsolvable. If **red**: v3 can still be blue. **Least-constraining-value → red.** *"Humans have an intuitive notion of what value to pick; this is the formal version."*

Also stated: constraint *optimization* (constraints plus an objective) is operations research — linear, nonlinear, convex, non-convex — *"we're not going to go into too much detail."* CSPs include NP-complete problems like 3-SAT, but constraints decompose the goal and shrink branching. See [[Constraint Satisfaction Problems]].

## Game Playing — Framing

Not shooters — *"traditional board games like chess, or even simpler."* Chess: b ≈ 35, ~100 total moves → 35^100 nodes, against ~10^40 legal board states. *"Game playing can be a little bit like real life — ups and downs and surprises."*

**Battleship** explained as the deterministic-but-imperfect-information cell: no dice, but ship positions are hidden; you infer from hit/miss reports.

**Utility is relative to the first player.** If the second player wins, utility is **−1**, *"because from the first player's perspective, the first player lost."* Every terminal is +1/−1/0 regardless of who is to move; MAX maximizes, MIN minimizes. See [[Game Playing]].

## Minimax — The Optimality Caveat

Worked on the 3×3 tree (leaves 3,12,8 / 2,4,6 / 14,5,2 → MIN returns 3, 2, 2 → MAX picks 3). Then the point the slide only states: **optimal only if the opponent is optimal.** *"If your opponent is not playing optimally, it could return 8 instead of 3, or 14. If you took the risk and went that way you'd get 14 — so this move is no longer optimal."* Without the assumption, *"the outcome is theoretically not provable in any way."*

The recursion has three cases — leaf returns utility; MAX node returns max of children's Minimax-Value; MIN node returns min — and *"it's a recursive function."* Space is **linear** via the call stack, same as [[IDA*]].

A student asked what non-±1 utilities mean: a card game where each terminal is dollars won or lost. Under mutual optimality you earn exactly the minimax value; against a suboptimal opponent you may earn more — or lose $10. Always relative to the first player. See [[Minimax]].

## See Also

- [[CSCE 420 Spring 2026 — 01-30 IDA*, Iterative Improvement]]
- [[CSCE 420 Spring 2026 — 02-04 Alpha-Beta Pruning]]
- [[Simulated Annealing]]
- [[Constraint Satisfaction Problems]]
- [[CSCE 420]]
