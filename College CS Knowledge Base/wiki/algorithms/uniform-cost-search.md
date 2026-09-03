---
title: "Uniform-Cost Search"
type: algorithm
tags: [csce420, uniform-cost, path-cost, uninformed-search]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Uniform-cost search is [[Breadth-First Search]] generalized to non-unit step costs: instead of visiting the shallowest node in the node list, visit the one with the **lowest path cost** $g(n)$.

## Definition

> BFS with visiting of the lowest-cost node in the node list, where path cost is $g(\text{node})$.

BFS is the special case in which $g(n) = \text{Depth}(n)$ — every step costs 1, so the cheapest node is always the shallowest.

## Why It Matters

Once step costs vary, "shallowest" and "cheapest" come apart, and BFS's optimality guarantee fails: a shallow goal reached by expensive steps can cost more than a deeper goal reached by cheap ones. Ordering the node list by $g(n)$ restores optimality.

## Relationship to A*

Uniform-cost is the $h(n) = 0$ case of [[A* Search]]. Writing $f(n) = g(n) + h(n)$, dropping the heuristic leaves $f(n) = g(n)$ — exactly uniform-cost. This is why A* is introduced in lecture as **"Uniform Cost + Heuristic Search"**: it adds a forward-looking estimate to a backward-looking cost that was already there.

The three sit on one axis:

| Algorithm | Evaluation function |
|---|---|
| Uniform-Cost | $g(n)$ — cost so far |
| [[Greedy Best-First Search]] | $h(n)$ — estimated cost remaining |
| [[A* Search]] | $g(n) + h(n)$ — both |

Uniform-cost and greedy are the two degenerate ends; A* is the combination, and it is the one that is both complete and optimal.

## See Also

- [[Breadth-First Search]]
- [[A* Search]]
- [[Greedy Best-First Search]]
- [[Uninformed Search]]
- [[CSCE 420]]
