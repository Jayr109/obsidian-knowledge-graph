---
title: "Adversarial Search"
type: concept
tags: [csce420, games, minimax, alpha-beta, expectimax, chance]
sources: [csce420-midterm-practice, csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Adversarial search is search in the presence of an opponent whose interests are opposed to yours. The state space becomes a **game tree** with alternating levels: MAX nodes (your move, drawn △) and MIN nodes (the opponent's, drawn ▽), with utilities at the leaves. Adding a third node type — chance nodes — extends the framework to games with dice.

## Node Types

| Node | Symbol | Value |
|------|--------|-------|
| MAX | △ | $\max$ over children |
| MIN | ▽ | $\min$ over children |
| Chance | ○ | expectation: $\sum_i p_i \cdot v_i$ over children |

The backing-up rule is the only thing that changes between them, and it is what defines each algorithm: [[Minimax]] uses the first two, [[Expectimax]] adds the third, and [[Alpha-Beta Pruning]] is an optimization of minimax that leaves the computed value unchanged.

## Why Pruning Matters

Game trees are astronomically large — chess has a branching factor around 35 and games run 50+ moves per side, so full minimax is hopeless. [[Alpha-Beta Pruning]] cuts subtrees that provably cannot affect the root value. With perfect move ordering it examines $O(b^{d/2})$ nodes instead of $O(b^d)$, effectively doubling the searchable depth.

Note that pruning is exact, not approximate: alpha-beta returns the same value as minimax. The approximation in real game players comes from elsewhere — cutting off search at a depth limit and applying a heuristic evaluation function.

## Games of Chance

When a die is rolled between moves, the value of a chance node is the probability-weighted average of its children. An important consequence: with chance nodes, the *magnitudes* of leaf utilities matter, not just their order. A monotone transformation of the utilities can change which move is best — unlike plain minimax, where only the ordering matters. See [[Expectimax]].

## Course Coverage

Midterm Practice Problem 5 asks for the value of a chance node in a mixed MAX/chance/MIN tree ([[Expectimax]]), and Problem 6 asks which of two marked cuts in an alpha-beta tree is legal ([[Alpha-Beta Pruning]]). Both are worked on their respective pages.

## From the Lecture

### Types of Games

|  | Deterministic | Chance |
|---|---|---|
| **Perfect information** | chess, checkers, go, othello | backgammon, monopoly |
| **Imperfect information** | battleship | bridge, poker, scrabble |

CSCE 420 covers the top row: deterministic perfect-information via [[Minimax]] and [[Alpha-Beta Pruning]], chance perfect-information via [[Expectimax]].

### Why Games Differ From Search

| Difference | Consequence |
|---|---|
| "Unpredictable" opponent | The solution is a **contingency plan**, not a path |
| Time limits | Goal unlikely to be reached — **must approximate** |

### The Historical Plan of Attack

1. Algorithm for perfect play — Von Neumann, 1944
2. Finite horizon, approximate evaluation — Zuse 1945; Shannon 1950; Samuel 1952–57
3. Pruning to reduce costs — McCarthy, 1956

Those three steps are still the architecture of a classical game player. See [[Game Playing]] for the full treatment and [[Game AI Milestones]] for the historical record from Deep Blue to MuZero.

## See Also

- [[Minimax]]
- [[Alpha-Beta Pruning]]
- [[Expectimax]]
- [[Heuristic Search]]
- [[CSCE 420]]
