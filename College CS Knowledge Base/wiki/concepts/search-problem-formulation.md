---
title: "Search Problem Formulation"
type: concept
tags: [csce420, search, state-space, operators, problem-formulation]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

A search problem is defined by the tuple $\langle$ **initial state, operators, goal states, path cost** $\rangle$. Getting this formulation right is prior to choosing any algorithm — the representation determines the branching factor, the size of the state space, and often whether the problem is tractable at all.

## The Components

| Component | Definition |
|---|---|
| **Initial state** | Description of the current situation as given in the problem |
| **Operators** | Functions from any state to a set of successor (neighbor) states |
| **Goal** | A subset of states, or a test rule |
| **Path cost** | Used when we need the *best* solution, not just *a* solution |
| **State space** | The set of all states reachable from the initial state by repeated application of operators |

Note that the state space is *derived*, not specified — it is whatever the operators generate.

## Choosing a State Representation

A state is a data structure — a variable assignment, a set of properties, an order in a list, a bitmap, a graph. It should capture all the ways the world could be. Typically it is static and discrete (symbolic), though it need not be.

Three criteria for a good representation:

- **Concise** — keep only the relevant features
- **Explicit** — easy to compute what is needed, when needed
- **Embeds constraints** — the representation itself rules out illegal states

The 8-puzzle illustrates the tradeoff. The same state admits several encodings — a flat list `(0 2 3 1 8 4 7 6 5)`, a nested row list `((0 2 3) (1 8 4) (7 6 5))`, or a position-indexed list `((0 1 7) (2 8 6) (3 4 5))`. Ask of each: how easy is it to **compare**, to **operate on**, and to **store**?

## Operators

An operator maps a state to a *subset* of states — multiple outcomes are possible. Examples: drive to a neighboring city, place a piece on a chess board, add a person to a meeting schedule, slide a tile in the 8-puzzle.

Characteristics:

- Often require **instantiation** — filling in variables
- **Encode constraints** — only certain operations are legal
- Generally **discrete**; continuous parameters produce infinite branching

## Specifying Goals

Three ways, in increasing difficulty:

- **Set of states** — enumerate the eligible states
- **Partial description** — e.g. a certain variable exceeds some value
- **Constraints** — hard to enumerate all matching states, and sometimes hard to produce a solution at all, though easy to verify one. The lecture flags this explicitly as the **P vs. NP** situation.

Other considerations in choosing a formulation: space, time, and quality — the exact-versus-approximate tradeoff.

## Worked Example: The 8-Puzzle

- **State**: location of the 8 numbered tiles and the blank
- **Operators**: blank moves left, right, up, or down
- **Goal test**: state matches the target configuration
- **Path cost**: each step costs 1 — so path cost equals path length equals search tree depth

Generalizes to the 15-puzzle and to the $(N^2-1)$-puzzle.

## See Also

- [[General Search Algorithm]]
- [[Uninformed Search]]
- [[Repeated States]]
- [[CSCE 420]]
