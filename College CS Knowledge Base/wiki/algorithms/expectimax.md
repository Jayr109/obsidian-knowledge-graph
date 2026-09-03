---
title: "Expectimax"
type: algorithm
tags: [csce420, games, chance, expectation, adversarial-search]
sources: [csce420-midterm-practice, csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Expectimax extends [[Minimax]] to games with an element of chance (dice, card deals) by adding a third node type. Between the MAX and MIN levels sits a **chance node**, whose value is the probability-weighted average of its children rather than a max or a min.

## Recurrence

$$
\text{value}(n) =
\begin{cases}
\text{Utility}(n) & n \text{ terminal} \\
\max_s \text{value}(s) & n \text{ is MAX} \\
\min_s \text{value}(s) & n \text{ is MIN} \\
\sum_s P(s) \cdot \text{value}(s) & n \text{ is a chance node}
\end{cases}
$$

For a fair three-outcome die, $P(s) = \frac{1}{3}$ for each child.

## Why Utility Magnitudes Now Matter

In plain minimax only the *order* of leaf utilities affects the chosen move, so any monotone rescaling is harmless. With chance nodes this breaks: an expectation is a weighted sum, so doubling one leaf's utility can flip which branch has the higher expected value even though the ordering is unchanged. Evaluation functions for games of chance must therefore be **positive linear transformations of actual expected utility**, not just order-preserving scores.

## Worked Example (Midterm Practice, Problem 5)

The tree has a MAX root with three chance-node children (dice rolls, $p = \frac{1}{3}$ each); the question asks for the value of the **second** chance node, shaded gray. Its three children are MIN nodes:

| Die roll | Child (MIN node) | Value |
|---|---|---|
| 1 | MIN over leaves 7, 6, 9 | $\min(7,6,9) = 6$ |
| 2 | MIN node shown as 3 | 3 |
| 3 | MIN node shown as 9 | 9 |

The value of the chance node is the expectation over the three equally likely rolls:

$$\text{value} = \tfrac{1}{3}\min(7,6,9) + \tfrac{1}{3}(3) + \tfrac{1}{3}(9) = \tfrac{1}{3}(6) + \tfrac{1}{3}(3) + \tfrac{1}{3}(9)$$

which reduces to $6$, though the problem explicitly says the formula is the answer and no arithmetic is required.

The step students miss is the inner $\min$: the leftmost child is not a leaf but a MIN node with three leaves under it, so its value must be backed up before the expectation is taken.

> Worked here from the figure; the practice exam ships without an answer key.

## From the Lecture

### Naming

The lecture calls this **expectiminimax** — the three-way recurrence over MAX nodes, MIN nodes, and chance nodes. "Expectimax" is the same algorithm; the practice exam uses the shorter name.

### The Formal Recurrence

With $a$ an action and $r$ a random outcome:

$$\text{Expectiminimax}(s) = \begin{cases}
\text{Utility}(s, \text{MAX}) & s \text{ terminal}\\
\max_a \text{Expectiminimax}(\text{Result}(s,a)) & \text{MAX node}\\
\min_a \text{Expectiminimax}(\text{Result}(s,a)) & \text{MIN node}\\
\sum_r P(r)\,\text{Expectiminimax}(\text{Result}(s,r)) & \text{chance node}
\end{cases}$$

built on the expected value $E(X) = \sum_{x \in X} x P(x)$.

### Chance as a Ply

Rolling dice or drawing a card **forms a new ply** in the game tree, interleaved with the MAX and MIN plies. Backgammon is the standard example.

### Two Design Consequences

1. **The value of the evaluation function matters, not just its scale.** Under plain [[Minimax]] only the *order* of successor values matters, so any monotonic rescaling is harmless. Once values are averaged with probability weights, the actual magnitudes change the expectation — so an evaluation function that was fine for minimax can be wrong here.

2. **Time complexity becomes $b^m n^m$**, where $n$ is the number of distinct dice rolls. The chance plies multiply the tree.

Pruning is still possible, but the lecture notes it must be done carefully — [[Alpha-Beta Pruning]]'s bounds do not transfer unchanged, because a chance node's value is not determined by any single successor.

## See Also

- [[Minimax]]
- [[Alpha-Beta Pruning]]
- [[Adversarial Search]]
