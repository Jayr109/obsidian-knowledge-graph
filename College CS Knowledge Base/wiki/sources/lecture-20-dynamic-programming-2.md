---
title: "Lecture 20 — Dynamic Programming (II)"
type: source
tags: [dynamic-programming, CSCE 411, lecture]
sources: []
course: CSCE 411
updated: 2026-04-09
---

Lecture 20 of [[CSCE 411]], taught by [[Calvin Beideman]]. Covers continued practice with [[Dynamic Programming]] algorithm design, focusing on sequence and grid DP problems.

## Source File

`raw/Lecture20_Dynamic_Programming_2.pptx` — 15 slides

## Key Topics

### Exam 2 Announcement
- Covers BFS & DFS through Dynamic Programming.
- Two sheets of notes allowed.
- Format similar to Exam 1; review sheet and sample exam on Canvas.

### Designing a DP Algorithm
- Framework: define subproblems → write recurrence → specify base cases → evaluate order → recover solution.
- *(Slide content was header-only; visual diagrams not captured.)*

### Longest Increasing Subsequence (LIS)
- Two DP formulations presented:
  1. O(n²): `L[i] = 1 + max{ L[j] : j < i, A[j] < A[i] }`
  2. O(n log n): alternative recurrence using patience sorting / binary search.
- See [[Longest Increasing Subsequence]] for full detail.

### Subset Sum
- Two formulations ("Subset Sum" and "Subset Sum, Take 2").
- Standard 2D table DP: `DP[i][t] = DP[i-1][t] OR DP[i-1][t-sᵢ]`
- See [[Subset Sum]] for full detail.

### Cherry Collecting (LeetCode Hard)
- Problem: two robots starting at top corners of a grid, collect cherries, cannot occupy the same cell simultaneously.
- DP over synchronized positions of both robots.
- Source: [LeetCode Cherry Pickup II](https://leetcode.com/problems/cherry-pickup-ii/)
- *(Recurrence and algorithm details were in visual slides not captured.)*

## Preview of Next Lecture

"Next time: Graph DP" — covered in [[Lecture 22 — Graph DP]].

## See Also

- [[Dynamic Programming]]
- [[Longest Increasing Subsequence]]
- [[Subset Sum]]
- [[CSCE 411]]
