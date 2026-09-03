---
title: "Repeated States"
type: concept
tags: [csce420, repeated-states, cycles, search, hashing]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

The same state can be reached by different paths and so appear in different nodes of the search tree. The lecture's assessment is blunt: **repeated states can be devastating in search problems.**

## Why It Happens

The common case is **problems with reversible operators**. If moving from A to B can be undone by moving B to A, the search tree contains A→B→A→B… and the **search space becomes infinite** even when the underlying state graph is small and finite.

This is the mechanism behind [[Depth-First Search]]'s incompleteness in practice: a finite problem can present an infinite tree.

One framing of the fix: find a **spanning tree** of the state graph — that is, systematically prevent the tree from revisiting graph vertices.

## Three Strategies

In increasing strength and cost:

| Strategy | What it catches |
|---|---|
| **Do not return to the node's parent** | Immediate two-step reversals |
| **Avoid cycles in the path** | Any loop back onto the current path |
| **Do not generate previously generated states** | All repetition, anywhere in the search |

The third uses a **hash table** to make the check efficient. The lecture notes the second is *a huge theoretical problem in its own right*.

## The Space Problem

Strategy three trades the exponential-time problem for an exponential-*space* one — storing every state seen. The lecture leaves this as an open question worth thinking about:

> How do we avoid storing every state? Would using a short **signature** (or checksum) of the full state description help?

The tradeoff is the familiar one for hashing: a compact signature saves space but admits collisions, so two genuinely different states may be wrongly treated as the same — which can cost completeness.

## Interaction With A*

Repeated-state handling interacts with optimality in a way [[A* Search]]'s proof depends on. If revisiting a parent is disallowed outright, search can fail on graphs where the optimal path requires passing back through a region; if it is allowed, those paths carry an inflated $g(n)$ and become non-optimal rather than wrong.

## See Also

- [[Search Problem Formulation]]
- [[Depth-First Search]]
- [[Uninformed Search]]
- [[A* Search]]
- [[CSCE 420]]
