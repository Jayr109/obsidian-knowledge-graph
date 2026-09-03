---
title: "Game Playing"
type: concept
tags: [csce420, game-playing, minimax, utility, horizon-effect, evaluation-function]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Game playing treats an adversarial game as a search problem in which an **unpredictable opponent** controls half the moves. It is one of the oldest domains in AI, and the lecture's framing is that it is **more like real life than mechanical search**.

## Why Games Are an Attractive AI Problem

- **Abstract** — no messy perception or actuation
- **Fully accessible** world state in most cases
- **Clear and exact** computer representation
- **Challenging** — uncertainty from the opponent, plus complexity that makes full search impossible

The chess numbers: branching factor about 35, and 50 moves by each player gives $35^{100}$ nodes to search — against roughly $10^{40}$ legal board states. Full search is not merely expensive but impossible.

## Games vs. Ordinary Search

Two differences change everything:

| Difference | Consequence |
|---|---|
| "Unpredictable" opponent | The solution is a **contingency plan**, not a path |
| Time limits | Unlikely to reach a goal — **must approximate** |

A search solution is a sequence of moves; a game solution must specify a response to every opponent reply.

## The Historical Plan of Attack

1. Algorithm for perfect play — Von Neumann, 1944
2. Finite horizon, approximate evaluation — Zuse 1945; Shannon 1950; Samuel 1952–57
3. Pruning to reduce costs — McCarthy, 1956

Each step is a concession to intractability, and together they are still the architecture of a classical game player: [[Minimax]] for perfect play, evaluation functions for the horizon, [[Alpha-Beta Pruning]] for cost.

## Types of Games

|  | Deterministic | Chance |
|---|---|---|
| **Perfect information** | chess, checkers, go, othello | backgammon, monopoly |
| **Imperfect information** | battleship | bridge, poker, scrabble |

CSCE 420 covers the deterministic perfect-information case ([[Minimax]], [[Alpha-Beta Pruning]]) and the chance perfect-information case ([[Expectimax]]).

## Two-Person Perfect-Information Games

The formal setup, parallel to [[Search Problem Formulation]]:

- **Initial state**: initial position and who goes first
- **Operators**: legal moves
- **Terminal test**: is the game over?
- **Utility function**: the outcome — e.g. win $+1$, lose $-1$, draw $0$

Two players, **MAX** and **MIN**, take turns; each turn generates one **ply**. The game is zero-sum: one player's victory is the other's defeat. What is needed is a strategy to win *no matter what the opponent does*.

## Resource Limits and the Horizon Effect

Under a time limit only a fixed number of paths can be evaluated. Three responses:

- **Evaluation function** — how desirable is a given state?
- **Cutoff test** — a depth limit
- **Pruning** — see [[Alpha-Beta Pruning]]

The depth limit creates the **horizon effect**: interesting or devastating events can lie just beyond the search horizon, invisible to the player.

## Evaluation Functions

For chess, typically a linear weighted sum of features:

$$\text{Eval}(s) = \sum_i w_i f_i(s)$$

where $f_i(s)$ is, for example, (number of white piece X) − (number of black piece X). Other features include degree of control over the centre.

**Exact values do not matter** for minimax — only the *order* of the successors' minimax values. This stops being true once chance enters; see [[Expectimax]].

## See Also

- [[Minimax]]
- [[Alpha-Beta Pruning]]
- [[Expectimax]]
- [[Adversarial Search]]
- [[Game AI Milestones]]
- [[CSCE 420]]
