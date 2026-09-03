---
title: "Greedy Algorithms"
type: concept
tags: [greedy, optimization, algorithms]
sources: [lecture-23-greedy-algorithms]
course: CSCE 411
updated: 2026-04-09
---

Greedy algorithms make a sequence of locally optimal decisions — choosing the best available option at each step without backtracking — and hope (or prove) that this yields a globally optimal solution. They have no formal definition, but are characterized by simplicity, speed, and the requirement to prove correctness carefully.

## Characteristics

- Make small incremental decisions without backtracking.
- Make locally optimal (greedy) choices, without considering the global picture.
- Often follow simple fixed priority rules (e.g., earliest finish time, smallest frequency).
- Usually very fast, but incorrect for many problems.

## When Greedy Works

A problem must exhibit **both** of the following:

1. **Optimal Substructure** — an optimal solution contains optimal solutions to subproblems. (Shared with [[Dynamic Programming]] and divide & conquer.)
2. **Greedy Choice Property** — a globally optimal solution can be reached by always making the locally optimal (greedy) choice. This is what distinguishes greedy from DP.

If greedy choice property holds, you only need to explore one subproblem at each step (instead of all subproblems as in DP).

## Paradigm Comparison

| Paradigm | Subproblems explored | Requires |
|---|---|---|
| Divide & Conquer | All (disjoint) | Optimal substructure |
| [[Dynamic Programming]] | All (overlapping, memoized) | Optimal substructure |
| Greedy | 1 (greedy choice) | Optimal substructure + greedy choice property |

## Proving Correctness

Greedy algorithms are not obviously correct — they require proof. Two main techniques:

### Exchange Argument
1. Suppose there is an optimal solution different from the greedy one.
2. Find the first difference between the two solutions.
3. Argue that swapping the optimal solution's choice for the greedy choice does not make the solution worse.
4. Conclude the greedy solution is at least as good as any optimal solution, hence optimal.

### Induction on Greedy Choice Property
Show that making the greedy choice at each step is "safe" — it can always be extended to an optimal solution.

## Classic Example: Making Change

Given coin denominations, greedily pick the largest coin that fits. This works for standard US denominations but **fails** for arbitrary denominations (e.g., coins {1, 3, 4}: to make 6¢, greedy gives 4+1+1=3 coins, but optimal is 3+3=2 coins).

## Greedy Backward Reasoning

Sometimes the correct greedy strategy is found by working **backward** from the goal: instead of asking "what should I do next?", ask "what must the last step have been?" This simplifies the exchange argument.

Example — [[Increment and Triple]]: to reach y from 1 using increment/triple steps optimally, work backward. If y is divisible by 3, the last step must have been a triple (otherwise a wasteful sequence of increments could be replaced with tripling earlier). If y is not divisible by 3, the last step must have been an increment. This yields an O(log³ y) algorithm.

## Algorithms

- [[Interval Scheduling]] — earliest finish time greedy; provably optimal; "latest start" also works
- [[Interval Covering]] — sort by finish time, greedily add finish point when interval uncovered; O(n log n)
- [[Huffman Coding]] — merge two least-frequent characters; provably optimal prefix-free code
- [[Increment and Triple]] — greedy backward (triple if divisible by 3, else increment); O(log³ y)

## See Also

- [[Dynamic Programming]]
- [[Interval Scheduling]]
- [[Interval Covering]]
- [[Huffman Coding]]
- [[Increment and Triple]]
- [[Homework 6 Solutions — Spring 2026]]
- [[CSCE 411]]
