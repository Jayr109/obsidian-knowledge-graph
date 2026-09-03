---
title: "Blue-Green Trees"
type: algorithm
tags: [tree-DP, dynamic-programming, counting, graphs]
sources: [homework-6-solutions-sp26]
course: CSCE 411
updated: 2026-05-03
---

The Blue-Green Tree problem asks for the number of valid ways to 2-color the vertices of a binary tree such that no two consecutive blue vertices appear on any root-to-leaf path, and no three consecutive green vertices appear. It is solved by a **3-state tree DP** and is notable for a runtime analysis that involves multiplying exponentially large integers, requiring [[Karatsuba's Algorithm]].

## Problem Definition

A **blue-green coloring** of a binary tree T is valid if, on every root-to-leaf path:
- No two consecutive vertices are blue (no BB)
- No three consecutive vertices are green (no GGG)

**Input**: A binary tree T with n vertices.

**Output**: The number of distinct valid blue-green colorings of T (an integer, potentially exponential in n).

## Algorithm: 3-State Tree DP

For each vertex v define three values:

- **BG(v, 0)** = number of valid colorings of v's subtree where v is **blue**
- **BG(v, 1)** = number of valid colorings of v's subtree where v is **green**
- **BG(v, 2)** = number of valid colorings of v's subtree where v is **green** and all children of v must be **blue**

**Recurrence** (∏ ranges over children x of v):

```
BG(v, 0) = ∏_{x ∈ Children(v)} BG(x, 1)
           // v is blue → each child must be green (no two consecutive blue)

BG(v, 1) = ∏_{x ∈ Children(v)} (BG(x, 0) + BG(x, 2))
           // v is green → each child can be blue (BG(x,0)) OR green-with-forced-blue-grandchildren (BG(x,2))
           // We cannot allow child x to be freely green, because then v–x–? could have three greens in a row

BG(v, 2) = ∏_{x ∈ Children(v)} BG(x, 0)
           // v is green with children forced blue → each child is blue

BG(leaf, i) = 1 for all i ∈ {0, 1, 2}
           // A single-vertex subtree has exactly one coloring regardless of imposed color
```

**Answer** = BG(root, 0) + BG(root, 1).

## Why State 2 Is Needed

Without state 2, we cannot distinguish "v is green and its parent was also green" from "v is green and its parent was blue." But the constraint on v's children (must be blue to avoid GGG) only applies in the first case. State 2 encodes "green, and the no-three-consecutive constraint has been triggered at this node."

## Implementation

Postorder traversal fills BG values bottom-up. Augment each vertex v with three fields: v.BG0, v.BG1, v.BG2. Each vertex is processed after its children.

```
BlueGreen(T):
  for each v in T (postorder):
    if v is a leaf:
      v.BG0, v.BG1, v.BG2 ← 1
    else:
      v.BG0 ← ∏_{x ∈ Children(v)} x.BG1
      v.BG1 ← ∏_{x ∈ Children(v)} (x.BG0 + x.BG2)
      v.BG2 ← ∏_{x ∈ Children(v)} x.BG0
  return root.BG0 + root.BG1
```

## Runtime Analysis

**Number of multiplications**: O(n) — each vertex contributes to its parent's product exactly once.

**Size of numbers**: The answer can be as large as 2ⁿ (upper bound: 2ⁿ total colorings regardless of rules). Therefore intermediate values have up to O(n) digits.

**Cost per multiplication**: O(n) digits × O(n) digits using [[Karatsuba's Algorithm]] takes O(n^{log₂ 3}) ≈ O(n^{1.585}) time.

**Total runtime**: O(n) multiplications × O(n^{log₂ 3}) each = **O(n^{1 + log₂ 3}) ≈ O(n^{2.585})**.

This is a non-obvious runtime: the bottleneck is not the tree traversal (O(n)) but the arithmetic on exponentially large intermediate results.

## Contrast with MWIS Tree DP

[[Maximum Weight Independent Set]] on trees also uses a 2-state DP (include/exclude). Blue-Green Trees require a 3rd state because the constraint on a child depends on the grandparent's color (GGG avoidance looks 2 levels up), not just the parent's. The standard 2-state DP would be insufficient.

## See Also

- [[Graph DP]]
- [[Dynamic Programming]]
- [[Karatsuba's Algorithm]]
- [[Maximum Weight Independent Set]]
- [[Homework 6 Solutions — Spring 2026]]
- [[CSCE 411]]
