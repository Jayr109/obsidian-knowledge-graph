---
title: "Increment and Triple"
type: algorithm
tags: [greedy, number-theory, algorithms]
sources: [homework-6-solutions-sp26]
course: CSCE 411
updated: 2026-05-03
---

The Increment and Triple problem asks: starting from x = 1, using only "increment by 1" or "triple" (×3) operations, what is the minimum number of steps to reach a target y? It is solved optimally by a **greedy backward algorithm** in O(log³ y) time.

## Problem Definition

**Input**: A positive integer y.

**Output**: The minimum number of increment/triple steps to reach y starting from x = 1.

**Example**: y = 411. Optimal sequence (9 steps):
1 → 3 → 4 → 5 → 15 → 45 → 135 → 136 → 137 → 411.

## Algorithm

Work backward from y, greedily undoing the last step:

```
MinSteps(y):
  if y = 1: return 0
  if y mod 3 = 0: return 1 + MinSteps(y / 3)     // last step was a triple
  else: return 1 + MinSteps(y − 1)                // last step was an increment
```

## Correctness

Proof by strong induction on y.

**Base case** (y = 1): 0 steps needed. ✓

**Inductive step**: assume MinSteps gives the correct answer for all y′ < y.

- *y not divisible by 3*: The last step of any optimal sequence must be an increment (tripling would require y to be divisible by 3). Therefore MinSteps(y) = 1 + MinSteps(y−1), which is correct by induction.

- *y divisible by 3*: Claim that every optimal sequence ends with a triple.

  Suppose for contradiction OPT ends with an increment. Two sub-cases:
  1. OPT uses only increments: uses y−1 steps. But our algorithm uses at most y/3 steps (a triple then increments from 1 → y/3), and y/3 < y−1 for y ≥ 3 — contradiction.
  2. OPT has at least one triple step. Let the last triple be z → 3z. Then OPT uses MinSteps(z) + 1 + (y − 3z) total steps (min steps to reach z, the triple, then y−3z increments). Consider instead: reach y/3 by incrementing from z (cost y/3 − z), then triple (cost 1). This uses MinSteps(z) + (y/3 − z) + 1 steps, which is strictly fewer since y/3 − z < y − 3z for any z < y/3 — contradiction.

  So OPT must end with a triple. MinSteps(y) = 1 + MinSteps(y/3), correct by induction. ✓

## Runtime

**Number of recursive calls**: at least 1 in every 3 steps is a triple (each triple reduces y by a factor of 3). So the number of calls is at most 3 log₃ y = O(log y).

**Arithmetic cost per call**: inputs are at most y, so integers have O(log y) digits.
- Subtraction (y−1): O(log y)
- Division (y/3): O(log² y) using grade-school long division

**Total**: O(log y) calls × O(log² y) per call = **O(log³ y)** — polynomial in the input length |⟨y⟩| = O(log y). ✓

## Key Insight

The problem illustrates that **working backwards** can simplify greedy reasoning: rather than asking "what should my next step be?" we ask "what must my last step have been?" When y is divisible by 3, the last step *must* be a triple to be optimal — any ending sequence of increments is wasteful compared to tripling sooner.

## See Also

- [[Greedy Algorithms]]
- [[Homework 6 Solutions — Spring 2026]]
- [[CSCE 411]]
