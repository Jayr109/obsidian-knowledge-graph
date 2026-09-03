---
title: "Bidirectional Search"
type: algorithm
tags: [csce420, bidirectional-search, uninformed-search]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Bidirectional search (BDS) runs two searches at once — forward from the initial state and backward from the goal — and stops when they meet. Halving the effective depth turns $O(b^{d})$ into $O(b^{d/2})$, an exponential saving.

## The Complexity Argument

$$O(b^{d/2}) \text{ for BDS} \quad\text{vs.}\quad O(b^{d+1}) \text{ for BFS}$$

Two searches of depth $d/2$ are dramatically cheaper than one of depth $d$, because the cost is exponential in depth. This is the same square-root-style saving that [[Alpha-Beta Pruning]] achieves in game trees.

## Five Considerations

BDS is rarely as easy as it looks. The lecture lists what must be settled first:

1. **How do we back-trace from the goal?**
2. **Successors and predecessors** — are the operators reversible?
3. **Are goals explicit?** We must know the goal state to search backward from it.
4. **Check overlap** in the two branches — detecting the meeting point is itself work.
5. **Which strategy** for each half — BFS or DFS, and the same for both or different?

Point 3 is the most restrictive. Many problems specify goals as a *test* rather than a state (see [[Search Problem Formulation]]), and one cannot search backward from a predicate.

## Where It Applies

The lecture poses these as questions rather than answering them:

- **8-puzzle** — is it a good strategy? The goal is an explicit configuration and moves are reversible, so the preconditions hold.
- **Chess** — would it be? The goal is any checkmate position, not one known state, and there are vast numbers of them.

The general rule: BDS suits domains with an **explicit, unique goal state** and **reversible operators**.

## See Also

- [[Uninformed Search]]
- [[Breadth-First Search]]
- [[Search Problem Formulation]]
- [[CSCE 420]]
