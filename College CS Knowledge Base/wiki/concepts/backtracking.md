---
title: "Backtracking"
type: concept
tags: [backtracking, recursion, algorithms]
sources: [lecture-18-backtracking]
course: CSCE 411
updated: 2026-04-09
---

Recursive backtracking is an algorithm design technique for problems that require making a sequence of decisions to construct a solution. At each step the algorithm makes one choice, recurses on the remaining decisions, and — if the choice leads to a dead end — backtracks and tries another option.

## When to Use Backtracking

Backtracking applies when:
- The solution can be built by a sequence of decisions
- At each step there are multiple valid choices
- Some sequences of choices lead to invalid or suboptimal solutions

It is essentially recursive brute force: try all possibilities, use the best result.

## Design Template

1. **Specification** — clearly state in English what problem your subproblem solves (often a generalization of the original problem with extra parameters to track choices made so far)
2. **Pseudocode** — recursive algorithm using smaller versions of the same problem; include base case; pass a minimal summary of choices made so far
3. **Solution** — what inputs to the generalized subproblem answer the original question

Keep the "choices so far" summary as small as possible. For LIS, only the last element chosen is needed — not the whole sequence.

## Runtime

Backtracking typically runs in exponential time — O(2ⁿ) or O(n!) — because it explores all possible choices. This is acceptable for small inputs but impractical for large ones.

**Upgrade path**: if the number of *distinct subproblems* (distinct parameter combinations) is polynomial, memoization converts the exponential backtracking into polynomial [[Dynamic Programming]].

## Relationship to Dynamic Programming

> "DP = Recursive Backtracking + Memoization"

The transformation:
1. Identify that many recursive calls share the same subproblem parameters
2. Add a memo table; look up before computing
3. Top-down memoization → bottom-up tabulation

## Classic Examples

- **LIS** (Backtracking → DP): naive O(2ⁿ) → O(n²) DP
- **Subset Sum** (Backtracking → DP): try include/exclude each item → O(n·T) DP
- **Fibonacci** (Backtracking → DP): naive O(2ⁿ) → O(n) with memoization

## Why Greedy Fails First

For problems like LIS, greedy approaches (e.g. always take the smallest available next element) fail with simple counterexamples ([2,3,1] or [3,1,2]). This motivates trying all choices — backtracking — before applying DP.

## See Also

- [[Dynamic Programming]]
- [[Longest Increasing Subsequence]]
- [[Subset Sum]]
- [[Greedy Algorithms]]
- [[CSCE 411]]
